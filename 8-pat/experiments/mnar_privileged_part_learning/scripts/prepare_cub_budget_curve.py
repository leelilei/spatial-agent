#!/usr/bin/env python3
"""Freeze nested CUB keypoint-annotation budgets for PAT-D-260728-004."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


BUDGETS = (1, 2, 4)


def arm_name(budget, seed):
    return f"K{budget}_S{seed}"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    rows = [json.loads(line) for line in args.manifest.read_text().splitlines()]
    if any(
        row["split"] != "train" or row["source_split"] != "official_train"
        for row in rows
    ):
        raise RuntimeError("PAT-D-260728-004 may inspect official train only")
    labels = np.asarray([row["class_index"] for row in rows])
    folds = np.asarray([row["fold"] for row in rows])
    image_ids = np.asarray([row["image_id"] for row in rows])
    seeds = [int(value) for value in protocol["sampling"]["selection_seeds"]]
    selections = {
        arm_name(budget, seed): np.zeros((5, len(rows)), dtype=np.bool_)
        for budget in BUDGETS
        for seed in seeds
    }

    for seed in seeds:
        for fold in range(5):
            for class_index in range(200):
                candidates = np.flatnonzero(
                    (labels == class_index) & (folds != fold)
                )
                if len(candidates) != 8:
                    raise RuntimeError(
                        f"Expected 8 train candidates, got {len(candidates)}"
                    )
                candidates = candidates[np.argsort(image_ids[candidates])]
                rng = np.random.default_rng(
                    seed + 10000 * fold + 100 * class_index
                )
                permutation = rng.permutation(candidates)
                for budget in BUDGETS:
                    selections[arm_name(budget, seed)][
                        fold, permutation[:budget]
                    ] = True

    for name, values in selections.items():
        budget = int(name.split("_")[0][1:])
        for fold in range(5):
            selected = values[fold]
            if selected.sum() != 200 * budget:
                raise RuntimeError(
                    f"{name} fold {fold}: selection count mismatch"
                )
            per_class = np.bincount(labels[selected], minlength=200)
            if set(per_class.tolist()) != {budget}:
                raise RuntimeError(f"{name} fold {fold}: class mismatch")
            if np.any(selected & (folds == fold)):
                raise RuntimeError(f"{name} fold {fold}: selected OOF")

    for seed in seeds:
        for fold in range(5):
            k1 = selections[arm_name(1, seed)][fold]
            k2 = selections[arm_name(2, seed)][fold]
            k4 = selections[arm_name(4, seed)][fold]
            if np.any(k1 & ~k2) or np.any(k2 & ~k4):
                raise RuntimeError("Nested budget invariant failed")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "cub_budget_curve_selections.npz"
    np.savez_compressed(
        output,
        **{f"selected_{key}": value for key, value in selections.items()},
    )
    summary = {
        "experiment_id": protocol["experiment_id"],
        "selection_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "selection_seeds": seeds,
        "budgets": list(BUDGETS),
        "arms": list(selections),
        "nested_within_seed": True,
        "official_test_images_decoded_or_encoded": 0,
    }
    (
        args.output_dir / "cub_budget_curve_selection_summary.json"
    ).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
