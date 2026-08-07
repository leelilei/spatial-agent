#!/usr/bin/env python3
"""Create three disjoint 10-shot Stanford Dogs official-train episodes."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.io import loadmat


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mat_string(value) -> str:
    current = value
    while isinstance(current, np.ndarray):
        if current.size != 1:
            raise ValueError("expected a scalar MATLAB string cell")
        current = current.reshape(-1)[0]
    return str(current)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-list", type=Path, required=True)
    parser.add_argument("--dataset-root", type=Path, required=True)
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
    classes = int(protocol["data"]["classes"])
    if set(np.unique(labels)) != set(range(classes)):
        raise RuntimeError("unexpected Stanford Dogs train labels")
    selected_by_episode: list[list[dict]] = [[] for _ in range(3)]
    seed = int(protocol["data"]["selection_seed"])
    class_counts = {}
    for class_index in range(classes):
        indices = np.flatnonzero(labels == class_index)
        class_counts[str(class_index)] = int(len(indices))
        if len(indices) < 30:
            raise RuntimeError(f"class {class_index} has fewer than 30 train images")
        rng = np.random.default_rng(seed + class_index)
        chosen = indices[rng.permutation(len(indices))[:30]]
        for episode_index in range(3):
            for position, index in enumerate(chosen[10 * episode_index:10 * (episode_index + 1)]):
                relative_path = Path("Images") / files[index]
                if not (args.dataset_root / relative_path).is_file():
                    raise FileNotFoundError(args.dataset_root / relative_path)
                selected_by_episode[episode_index].append({
                    "dataset": "Stanford Dogs",
                    "split": "train",
                    "source_split": "official_train",
                    "class_index": class_index,
                    "image_id": files[index],
                    "relative_path": str(relative_path),
                    "fold": position % 5,
                })
    args.output_root.mkdir(parents=True, exist_ok=True)
    episode_hashes = {}
    all_ids = []
    for episode, rows in enumerate(selected_by_episode, start=1):
        rows.sort(key=lambda row: (row["class_index"], row["image_id"]))
        episode_dir = args.output_root / f"episode_{episode}"
        episode_dir.mkdir(parents=True, exist_ok=True)
        manifest = episode_dir / "stanford_dogs_train_10shot_manifest.jsonl"
        manifest.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows))
        episode_hashes[str(episode)] = sha256(manifest)
        all_ids.extend(row["image_id"] for row in rows)
    if len(all_ids) != len(set(all_ids)):
        raise RuntimeError("Stanford Dogs episodes are not disjoint")
    summary = {
        "experiment_id": protocol["experiment_id"],
        "train_list_sha256": sha256(args.train_list),
        "protocol_sha256": sha256(args.protocol),
        "classes": classes,
        "official_train_rows": int(len(files)),
        "class_train_count_min": int(min(class_counts.values())),
        "class_train_count_max": int(max(class_counts.values())),
        "episode_rows": [len(rows) for rows in selected_by_episode],
        "unique_selected_images": len(set(all_ids)),
        "pairwise_episode_overlap": 0,
        "episode_manifest_sha256": episode_hashes,
        "official_test_list_loaded": False,
        "official_test_images_decoded_or_encoded": 0
    }
    (args.output_root / "selection_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
