#!/usr/bin/env python3
"""Freeze a train-only CUB 10-shot subset and stratified OOF folds."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np


def read_pairs(path: Path, value_type=str):
    output = {}
    for line in path.read_text().splitlines():
        key, value = line.split(maxsplit=1)
        output[int(key)] = value_type(value)
    return output


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    data = protocol["data"]
    cub = args.dataset_root / "CUB_200_2011"

    images = read_pairs(cub / "images.txt")
    labels = read_pairs(cub / "image_class_labels.txt", int)
    split = read_pairs(cub / "train_test_split.txt", int)

    keypoints = defaultdict(lambda: [[0.0, 0.0, 0] for _ in range(15)])
    for line in (cub / "parts" / "part_locs.txt").read_text().splitlines():
        image_id, part_id, x, y, visible = line.split()
        keypoints[int(image_id)][int(part_id) - 1] = [
            float(x),
            float(y),
            int(visible),
        ]

    by_class = defaultdict(list)
    for image_id, class_id in labels.items():
        if split[image_id] == 1:
            by_class[class_id].append(image_id)

    expected_classes = int(data["classes"])
    if len(by_class) != expected_classes:
        raise RuntimeError(
            f"Expected {expected_classes} train classes, found {len(by_class)}"
        )

    shots = int(data["shots_per_class"])
    subset_rng = np.random.default_rng(int(data["subset_seed"]))
    fold_rng = np.random.default_rng(int(data["fold_seed"]))
    folds = int(data["folds"])
    rows = []
    for class_id in sorted(by_class):
        candidates = np.asarray(sorted(by_class[class_id]), dtype=np.int64)
        if len(candidates) < shots:
            raise RuntimeError(f"Class {class_id} has fewer than {shots} images")
        selected = subset_rng.choice(candidates, size=shots, replace=False)
        selected = selected[fold_rng.permutation(shots)]
        for position, image_id in enumerate(selected.tolist()):
            if split[image_id] != 1:
                raise RuntimeError("Official CUB test image entered manifest")
            rows.append(
                {
                    "image_id": image_id,
                    "relative_path": str(
                        Path("CUB_200_2011") / "images" / images[image_id]
                    ),
                    "class_index": class_id - 1,
                    "fold": position % folds,
                    "keypoints": keypoints[image_id],
                    "split": "train",
                    "source_split": "official_train",
                }
            )

    rows.sort(key=lambda row: (row["class_index"], row["image_id"]))
    class_counts = Counter(row["class_index"] for row in rows)
    fold_counts = Counter(row["fold"] for row in rows)
    if set(class_counts.values()) != {shots}:
        raise RuntimeError("10-shot class balance check failed")
    if set(fold_counts.values()) != {len(rows) // folds}:
        raise RuntimeError("Fold balance check failed")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest = args.output_dir / "cub_train_10shot_manifest.jsonl"
    payload = "".join(
        json.dumps(row, sort_keys=True) + "\n" for row in rows
    )
    manifest.write_text(payload)
    sha256 = hashlib.sha256(payload.encode()).hexdigest()
    summary = {
        "experiment_id": protocol["experiment_id"],
        "images": len(rows),
        "classes": len(class_counts),
        "shots_per_class": shots,
        "fold_counts": dict(sorted(fold_counts.items())),
        "visible_keypoint_rate": float(
            np.mean(
                [
                    point[2]
                    for row in rows
                    for point in row["keypoints"]
                ]
            )
        ),
        "manifest_sha256": sha256,
        "official_test_images_decoded_or_encoded": 0,
    }
    (args.output_dir / "cub_train_10shot_manifest_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

