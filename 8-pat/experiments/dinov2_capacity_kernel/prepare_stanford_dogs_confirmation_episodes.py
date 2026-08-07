#!/usr/bin/env python3
"""Create Stanford Dogs Episodes 4-6, disjoint from PAT-K-006 Episodes 1-3."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.io import loadmat

from prepare_stanford_dogs_episodes import mat_string, sha256


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-list", type=Path, required=True)
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--prior-data-root", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    if args.train_list.name != "train_list.mat":
        raise RuntimeError("only the official train_list.mat is permitted")
    data = loadmat(args.train_list)
    files = np.asarray([mat_string(value) for value in data["file_list"].reshape(-1)])
    labels = data["labels"].reshape(-1).astype(np.int64) - 1
    classes = int(protocol["confirmation_data"]["classes"])
    seed = int(protocol["confirmation_data"]["selection_seed"])
    prior_ids = set()
    for episode in (1, 2, 3):
        manifest = args.prior_data_root / f"episode_{episode}" / "stanford_dogs_train_10shot_manifest.jsonl"
        for line in manifest.read_text().splitlines():
            prior_ids.add(json.loads(line)["image_id"])
    rows_by_episode = [[] for _ in range(3)]
    for class_index in range(classes):
        indices = np.flatnonzero(labels == class_index)
        rng = np.random.default_rng(seed + class_index)
        chosen = indices[rng.permutation(len(indices))[30:60]]
        for episode_index in range(3):
            for position, index in enumerate(chosen[10 * episode_index:10 * (episode_index + 1)]):
                image_id = files[index]
                if image_id in prior_ids:
                    raise RuntimeError("confirmation image overlaps Episodes 1-3")
                relative_path = Path("Images") / image_id
                if not (args.dataset_root / relative_path).is_file():
                    raise FileNotFoundError(args.dataset_root / relative_path)
                rows_by_episode[episode_index].append({
                    "dataset": "Stanford Dogs",
                    "split": "train",
                    "source_split": "official_train",
                    "class_index": class_index,
                    "image_id": image_id,
                    "relative_path": str(relative_path),
                    "fold": position % 5,
                })
    args.output_root.mkdir(parents=True, exist_ok=True)
    all_new_ids = []
    manifest_hashes = {}
    for episode, rows in zip((4, 5, 6), rows_by_episode):
        rows.sort(key=lambda row: (row["class_index"], row["image_id"]))
        episode_dir = args.output_root / f"episode_{episode}"
        episode_dir.mkdir(parents=True, exist_ok=True)
        manifest = episode_dir / "stanford_dogs_train_10shot_manifest.jsonl"
        manifest.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows))
        manifest_hashes[str(episode)] = sha256(manifest)
        all_new_ids.extend(row["image_id"] for row in rows)
    if len(all_new_ids) != len(set(all_new_ids)) or prior_ids.intersection(all_new_ids):
        raise RuntimeError("confirmation episodes are not fully disjoint")
    summary = {
        "experiment_id": protocol["experiment_id"],
        "episodes": [4, 5, 6],
        "rows_per_episode": [len(rows) for rows in rows_by_episode],
        "unique_confirmation_images": len(set(all_new_ids)),
        "prior_episode_images_checked": len(prior_ids),
        "overlap_with_episodes_1_to_3": 0,
        "pairwise_confirmation_overlap": 0,
        "manifest_sha256": manifest_hashes,
        "train_list_sha256": sha256(args.train_list),
        "protocol_sha256": sha256(args.protocol),
        "official_test_list_loaded": False,
        "official_test_images_decoded_or_encoded": 0,
    }
    (args.output_root / "selection_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
