#!/usr/bin/env python3
"""Freeze image-only K1 selections for PAT-D-260728-005."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

from cub_active_selection import (
    STRATEGIES,
    load_and_sanitize_manifest,
    score_fold,
    select_one_per_class,
    sha256_file,
    validate_selection,
)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--selector-manifest", type=Path, required=True)
    parser.add_argument("--features", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    rows = load_and_sanitize_manifest(args.selector_manifest)
    feature_file = np.load(args.features)
    features = feature_file["features"]
    labels = np.asarray([row["class_index"] for row in rows])
    folds = np.asarray([row["fold"] for row in rows])
    image_ids = np.asarray([row["image_id"] for row in rows])
    if not np.array_equal(labels, feature_file["labels"]):
        raise RuntimeError("Feature labels do not match selector manifest")
    if not np.array_equal(folds, feature_file["folds"]):
        raise RuntimeError("Feature folds do not match selector manifest")
    if not np.array_equal(image_ids, feature_file["image_ids"]):
        raise RuntimeError("Feature image IDs do not match selector manifest")
    expected_folds = int(protocol["data"]["folds"])
    expected_classes = len(np.unique(labels))
    selections = {
        strategy: np.zeros((expected_folds, len(rows)), dtype=np.bool_)
        for strategy in STRATEGIES
    }
    score_rows = []

    for fold in range(expected_folds):
        scores = score_fold(features, labels, folds, fold)
        for strategy in STRATEGIES:
            selected = select_one_per_class(
                scores, labels, folds, image_ids, fold, strategy
            )
            validate_selection(
                selected, labels, folds, fold, expected_classes
            )
            selections[strategy][fold] = selected
        for row_index in np.flatnonzero(folds != fold):
            score_rows.append(
                {
                    "fold": fold,
                    "row_index": int(row_index),
                    "image_id": int(image_ids[row_index]),
                    "class_index": int(labels[row_index]),
                    "representativeness": float(
                        scores["representativeness"][row_index]
                    ),
                    "margin": float(scores["margin"][row_index]),
                    "uncertainty": float(scores["uncertainty"][row_index]),
                    "balanced_annotation_value": float(
                        scores["balanced_annotation_value"][row_index]
                    ),
                    **{
                        f"selected_{strategy}": int(
                            selections[strategy][fold, row_index]
                        )
                        for strategy in STRATEGIES
                    },
                }
            )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "cub_active_selections.npz"
    np.savez_compressed(
        output,
        **{
            f"selected_{strategy}": values
            for strategy, values in selections.items()
        },
    )
    score_path = args.output_dir / "cub_active_candidate_scores.csv"
    with score_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(score_rows[0]))
        writer.writeheader()
        writer.writerows(score_rows)
    summary = {
        "experiment_id": protocol["experiment_id"],
        "strategies": list(STRATEGIES),
        "folds": expected_folds,
        "classes": expected_classes,
        "budget_per_class": 1,
        "selected_per_fold": expected_classes,
        "selection_sha256": sha256_file(output),
        "scores_sha256": sha256_file(score_path),
        "selector_manifest_sha256": sha256_file(args.selector_manifest),
        "feature_file_sha256": sha256_file(args.features),
        "selector_keypoint_field_accesses": 0,
        "official_test_images_decoded_or_encoded": 0,
    }
    (args.output_dir / "cub_active_selection_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
