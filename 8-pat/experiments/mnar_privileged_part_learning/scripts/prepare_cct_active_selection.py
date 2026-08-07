#!/usr/bin/env python3
"""Freeze CCT20+ 12.5%-budget random and image-only selector masks."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from cub_active_selection import (
    STRATEGIES,
    load_and_sanitize_manifest,
    score_fold,
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def score_name(strategy: str) -> str:
    return {
        "MEDOID": "representativeness",
        "BOUNDARY": "uncertainty",
        "DISCRIMINATIVE": "margin",
        "BALANCED_ANNOTATION_VALUE": "balanced_annotation_value",
    }[strategy]


def deterministic_top_k(candidates, values, image_ids, budget):
    def image_id_key(index):
        value = image_ids[index]
        try:
            return 0, int(value)
        except (TypeError, ValueError):
            return 1, str(value)

    ordered = sorted(
        candidates,
        key=lambda index: (-float(values[index]), image_id_key(index)),
    )
    return np.asarray(ordered[:budget], dtype=np.int64)


def validate_mask(mask, labels, folds, fold, fraction):
    if np.any(mask & (folds == fold)):
        raise RuntimeError("CCT selector selected an OOF row")
    for class_index in np.unique(labels):
        candidates = np.flatnonzero(
            (folds != fold) & (labels == class_index)
        )
        expected = math.ceil(fraction * len(candidates))
        observed = int(np.sum(mask & (labels == class_index)))
        if observed != expected:
            raise RuntimeError(
                f"Fold {fold} class {class_index}: {observed} != {expected}"
            )


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--selector-manifest", type=Path, required=True)
    parser.add_argument("--features", type=Path, required=True)
    parser.add_argument("--cub-screen-summary", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    cub_screen = json.loads(args.cub_screen_summary.read_text())
    if not cub_screen.get("overall_gate_pass") or not cub_screen.get("winner"):
        raise RuntimeError("A passing CUB selector winner is required")
    winner = cub_screen["winner"]
    if winner not in STRATEGIES:
        raise RuntimeError(f"Unsupported frozen CUB winner: {winner}")
    rows = load_and_sanitize_manifest(args.selector_manifest)
    feature_file = np.load(args.features)
    features = feature_file["features"]
    labels = np.asarray([row["class_index"] for row in rows])
    folds = np.asarray([row["fold"] for row in rows])
    image_ids = np.asarray([row["image_id"] for row in rows])
    if not np.array_equal(labels, feature_file["labels"]):
        raise RuntimeError("CCT feature labels do not match manifest")
    if not np.array_equal(folds, feature_file["folds"]):
        raise RuntimeError("CCT feature folds do not match manifest")
    if not np.array_equal(image_ids.astype(str), feature_file["image_ids"].astype(str)):
        raise RuntimeError("CCT feature image IDs do not match manifest")
    fold_count = len(np.unique(folds))
    fraction = float(
        protocol["annotation_budget"][
            "fraction_of_eligible_fold_training_rows_per_class"
        ]
    )
    random_seeds = [
        int(seed) for seed in protocol["training"]["random_selection_seeds"]
    ]
    masks = {
        f"RANDOM_S{seed}": np.zeros(
            (fold_count, len(rows)), dtype=np.bool_
        )
        for seed in random_seeds
    }
    masks[f"WINNER_{winner}"] = np.zeros(
        (fold_count, len(rows)), dtype=np.bool_
    )
    budget_rows = []
    for fold in range(fold_count):
        scores = score_fold(features, labels, folds, fold)
        values = scores[score_name(winner)]
        for class_index in np.unique(labels):
            candidates = np.flatnonzero(
                (folds != fold) & (labels == class_index)
            )
            budget = math.ceil(fraction * len(candidates))
            chosen = deterministic_top_k(
                candidates, values, image_ids, budget
            )
            masks[f"WINNER_{winner}"][fold, chosen] = True
            for seed in random_seeds:
                rng = np.random.default_rng(
                    seed + 10000 * fold + 100 * int(class_index)
                )
                random_chosen = rng.permutation(candidates)[:budget]
                masks[f"RANDOM_S{seed}"][fold, random_chosen] = True
            budget_rows.append(
                {
                    "fold": fold,
                    "class_index": int(class_index),
                    "eligible_fold_train_rows": len(candidates),
                    "budget": budget,
                }
            )
        for mask in masks.values():
            validate_mask(mask[fold], labels, folds, fold, fraction)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "cct_active_selections.npz"
    np.savez_compressed(
        output,
        **{f"selected_{name}": value for name, value in masks.items()},
    )
    budget_path = args.output_dir / "cct_active_budgets.csv"
    with budget_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(budget_rows[0]))
        writer.writeheader()
        writer.writerows(budget_rows)
    summary = {
        "experiment_id": protocol["experiment_id"],
        "cub_winner": winner,
        "folds": fold_count,
        "classes": len(np.unique(labels)),
        "budget_fraction": fraction,
        "masks": {
            name: [int(mask[fold].sum()) for fold in range(fold_count)]
            for name, mask in masks.items()
        },
        "selection_sha256": sha256_file(output),
        "budget_sha256": sha256_file(budget_path),
        "selector_keypoint_field_accesses": 0,
        "cis_test_images_decoded_or_encoded": 0,
        "trans_test_images_decoded_or_encoded": 0,
    }
    (args.output_dir / "cct_active_selection_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
