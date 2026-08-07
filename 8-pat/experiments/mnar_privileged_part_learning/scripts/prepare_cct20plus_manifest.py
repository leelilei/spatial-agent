#!/usr/bin/env python3
"""Audit CCT20+ keypoints and freeze an official-train grouped OOF manifest."""

from __future__ import annotations

import argparse
import ast
import collections
import csv
import hashlib
import json
import tarfile
from pathlib import Path

import numpy as np
from sklearn.model_selection import StratifiedGroupKFold


PART_COLUMNS = (
    "body",
    "head",
    "left-back-leg",
    "left-front-leg",
    "left-wing",
    "right-back-leg",
    "right-front-leg",
    "right-wing",
    "tail",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def md5_file(path: Path) -> str:
    digest = hashlib.md5()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json_member(archive_path: Path, suffix: str):
    with tarfile.open(archive_path, "r:gz") as archive:
        matches = [
            member for member in archive.getmembers()
            if member.name.endswith(suffix)
        ]
        if len(matches) != 1:
            raise RuntimeError(
                f"Expected one {suffix} in split archive, found {len(matches)}"
            )
        handle = archive.extractfile(matches[0])
        if handle is None:
            raise RuntimeError(f"Could not read {matches[0].name}")
        return json.load(handle)


def parse_point(value: str) -> list[float | int]:
    x, y = ast.literal_eval(value)
    visible = int(float(x) >= 0 and float(y) >= 0)
    return [float(x), float(y), visible]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--images-archive", type=Path, required=True)
    parser.add_argument("--split-archive", type=Path, required=True)
    parser.add_argument("--keypoints", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    data_config = protocol["data"]
    if md5_file(args.images_archive) != data_config["image_archive_md5"]:
        raise RuntimeError("CCT20 1024px image archive MD5 mismatch")
    if md5_file(args.split_archive) != data_config["split_archive_md5"]:
        raise RuntimeError("CCT20 split archive MD5 mismatch")
    train = load_json_member(args.split_archive, "train_annotations.json")
    image_by_id = {str(image["id"]): image for image in train["images"]}
    annotations_by_image = collections.defaultdict(list)
    for annotation in train["annotations"]:
        annotations_by_image[str(annotation["image_id"])].append(annotation)
    category_names = {
        int(category["id"]): category["name"]
        for category in train["categories"]
    }
    with args.keypoints.open(newline="") as handle:
        keypoint_rows = list(csv.DictReader(handle))
    id_counts = collections.Counter(
        row["image_id"] for row in keypoint_rows
    )
    eligible_pre_class = []
    exclusions = collections.Counter()
    for row in keypoint_rows:
        image_id = row["image_id"]
        if id_counts[image_id] != 1:
            exclusions["duplicate_image_id"] += 1
            continue
        if image_id not in image_by_id:
            exclusions["not_official_train"] += 1
            continue
        annotations = annotations_by_image[image_id]
        if len(annotations) != 1:
            exclusions["not_single_instance"] += 1
            continue
        if int(annotations[0]["category_id"]) != int(row["category_id"]):
            exclusions["category_mismatch"] += 1
            continue
        eligible_pre_class.append(row)
    counts = collections.Counter(
        int(row["category_id"]) for row in eligible_pre_class
    )
    minimum = int(data_config["minimum_eligible_keypoint_images_per_class"])
    eligible_categories = sorted(
        category for category, count in counts.items() if count >= minimum
    )
    eligible_rows = [
        row for row in eligible_pre_class
        if int(row["category_id"]) in eligible_categories
    ]
    for row in eligible_pre_class:
        if int(row["category_id"]) not in eligible_categories:
            exclusions["class_below_minimum"] += 1

    labels = np.asarray(
        [eligible_categories.index(int(row["category_id"])) for row in eligible_rows]
    )
    groups = np.asarray(
        [str(image_by_id[row["image_id"]]["seq_id"]) for row in eligible_rows]
    )
    per_class_group_counts = {
        category: len(
            {
                str(image_by_id[row["image_id"]]["seq_id"])
                for row in eligible_rows
                if int(row["category_id"]) == category
            }
        )
        for category in eligible_categories
    }
    folds = min(
        int(data_config["maximum_folds"]),
        min(per_class_group_counts.values()),
    )
    if folds < int(data_config["minimum_folds"]):
        raise RuntimeError(
            f"Only {folds} grouped folds possible; protocol requires >=3"
        )
    splitter = StratifiedGroupKFold(
        n_splits=folds, shuffle=True, random_state=260728001
    )
    fold_values = np.full(len(eligible_rows), -1, dtype=np.int64)
    dummy = np.zeros(len(eligible_rows))
    for fold, (_, evaluate) in enumerate(
        splitter.split(dummy, labels, groups=groups)
    ):
        fold_values[evaluate] = fold
    if (fold_values < 0).any():
        raise RuntimeError("Grouped fold assignment is incomplete")
    for fold in range(folds):
        train_groups = set(groups[fold_values != fold])
        eval_groups = set(groups[fold_values == fold])
        if train_groups & eval_groups:
            raise RuntimeError("Sequence group leaked across an OOF fold")
        observed = set(labels[fold_values == fold])
        if observed != set(range(len(eligible_categories))):
            raise RuntimeError(f"Fold {fold} does not cover every class")

    manifest = []
    for row_index, (row, fold) in enumerate(
        zip(eligible_rows, fold_values, strict=True)
    ):
        image = image_by_id[row["image_id"]]
        category_id = int(row["category_id"])
        manifest.append(
            {
                "row_index": row_index,
                "image_id": row["image_id"],
                "relative_path": (
                    "eccv_18_all_images_sm/" + image["file_name"]
                ),
                "class_index": eligible_categories.index(category_id),
                "category_id": category_id,
                "category_name": category_names[category_id],
                "fold": int(fold),
                "seq_id": str(image["seq_id"]),
                "location": int(image["location"]),
                "original_width": int(image["width"]),
                "original_height": int(image["height"]),
                "keypoints": [parse_point(row[name]) for name in PART_COLUMNS],
                "split": "train",
                "source_split": "official_train",
            }
        )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = args.output_dir / "cct20plus_train_manifest.jsonl"
    manifest_path.write_text(
        "".join(
            json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n"
            for row in manifest
        )
    )
    audit = {
        "experiment_id": protocol["experiment_id"],
        "paper_reported_keypoint_rows": int(
            data_config["reported_keypoint_rows"]
        ),
        "current_upstream_csv_rows": len(keypoint_rows),
        "row_difference_vs_paper": (
            len(keypoint_rows) - int(data_config["reported_keypoint_rows"])
        ),
        "current_unique_image_ids": len(id_counts),
        "eligible_before_class_threshold": len(eligible_pre_class),
        "exclusions": dict(exclusions),
        "eligible_categories": [
            {
                "category_id": category,
                "category_name": category_names[category],
                "rows": counts[category],
                "sequence_groups": per_class_group_counts[category],
            }
            for category in eligible_categories
        ],
        "eligible_rows": len(manifest),
        "folds": folds,
        "fold_sizes": {
            str(fold): int(np.sum(fold_values == fold))
            for fold in range(folds)
        },
        "image_archive_md5": md5_file(args.images_archive),
        "split_archive_md5": md5_file(args.split_archive),
        "keypoint_csv_sha256": sha256_file(args.keypoints),
        "manifest_sha256": sha256_file(manifest_path),
        "cis_test_images_decoded_or_encoded": 0,
        "trans_test_images_decoded_or_encoded": 0,
    }
    (args.output_dir / "cct20plus_data_audit.json").write_text(
        json.dumps(audit, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(audit, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
