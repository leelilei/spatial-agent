#!/usr/bin/env python3
"""Create deterministic official-test manifests without decoding test images."""

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


def parse_two_column(path: Path) -> dict[int, str]:
    return {
        int(line.split(maxsplit=1)[0]): line.split(maxsplit=1)[1]
        for line in path.read_text().splitlines()
        if line.strip()
    }


def write_manifest(path: Path, rows: list[dict]) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows))
    return sha256(path)


def prepare_cub(root: Path, protocol: dict, output_root: Path) -> dict:
    cfg = protocol["official_test"]["cub"]
    images = parse_two_column(root / "images.txt")
    labels = {key: int(value) - 1 for key, value in parse_two_column(
        root / "image_class_labels.txt"
    ).items()}
    split = {key: int(value) for key, value in parse_two_column(
        root / "train_test_split.txt"
    ).items()}
    selected = []
    class_counts = {}
    for class_index in range(int(cfg["classes"])):
        candidates = sorted(
            (image_id for image_id in images
             if labels[image_id] == class_index and split[image_id] == 0)
        )
        class_counts[str(class_index)] = len(candidates)
        if len(candidates) < 10:
            raise RuntimeError(f"CUB class {class_index} has fewer than 10 test images")
        for position, image_id in enumerate(candidates[:10]):
            relative_path = Path("images") / images[image_id]
            if not (root / relative_path).is_file():
                raise FileNotFoundError(root / relative_path)
            selected.append({
                "dataset": "CUB-200-2011",
                "split": "test",
                "source_split": "official_test",
                "class_index": class_index,
                "image_id": image_id,
                "relative_path": str(relative_path),
                "fold": position % 5,
            })
    selected.sort(key=lambda row: (row["class_index"], row["image_id"]))
    manifest = output_root / "cub" / "episode_1" / "cub_test_10shot_manifest.jsonl"
    return {
        "episodes": 1,
        "rows_per_episode": [len(selected)],
        "class_test_count_min": min(class_counts.values()),
        "class_test_count_max": max(class_counts.values()),
        "manifest_sha256": {"1": write_manifest(manifest, selected)},
    }


def prepare_dogs(root: Path, protocol: dict, output_root: Path) -> dict:
    cfg = protocol["official_test"]["stanford_dogs"]
    test_list = root / "test_list.mat"
    data = loadmat(test_list)
    files = np.asarray([mat_string(value) for value in data["file_list"].reshape(-1)])
    labels = data["labels"].reshape(-1).astype(np.int64) - 1
    classes = int(cfg["classes"])
    seed = int(cfg["selection_seed"])
    episodes: list[list[dict]] = [[] for _ in range(int(cfg["episodes"]))]
    class_counts = {}
    for class_index in range(classes):
        indices = np.flatnonzero(labels == class_index)
        class_counts[str(class_index)] = int(len(indices))
        if len(indices) < 30:
            raise RuntimeError(f"Dogs class {class_index} has fewer than 30 test images")
        rng = np.random.default_rng(seed + class_index)
        chosen = indices[rng.permutation(len(indices))[:30]]
        for episode_index in range(3):
            subset = chosen[10 * episode_index:10 * (episode_index + 1)]
            for position, index in enumerate(subset):
                image_id = files[index]
                relative_path = Path("Images") / image_id
                if not (root / relative_path).is_file():
                    raise FileNotFoundError(root / relative_path)
                episodes[episode_index].append({
                    "dataset": "Stanford Dogs",
                    "split": "test",
                    "source_split": "official_test",
                    "class_index": class_index,
                    "image_id": image_id,
                    "relative_path": str(relative_path),
                    "fold": position % 5,
                })
    hashes = {}
    all_ids = []
    for episode_index, rows in enumerate(episodes, start=1):
        rows.sort(key=lambda row: (row["class_index"], row["image_id"]))
        manifest = output_root / "dogs" / f"episode_{episode_index}" / "dogs_test_10shot_manifest.jsonl"
        hashes[str(episode_index)] = write_manifest(manifest, rows)
        all_ids.extend(row["image_id"] for row in rows)
    if len(all_ids) != len(set(all_ids)):
        raise RuntimeError("Stanford Dogs official-test episodes overlap")
    return {
        "episodes": 3,
        "rows_per_episode": [len(rows) for rows in episodes],
        "class_test_count_min": min(class_counts.values()),
        "class_test_count_max": max(class_counts.values()),
        "unique_selected_images": len(set(all_ids)),
        "pairwise_episode_overlap": 0,
        "test_list_sha256": sha256(test_list),
        "manifest_sha256": hashes,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cub-root", type=Path, required=True)
    parser.add_argument("--dogs-root", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()
    protocol = json.loads(args.protocol.read_text())
    args.output_root.mkdir(parents=True, exist_ok=True)
    summary = {
        "experiment_id": protocol["experiment_id"],
        "protocol_sha256": sha256(args.protocol),
        "cub": prepare_cub(args.cub_root, protocol, args.output_root),
        "stanford_dogs": prepare_dogs(args.dogs_root, protocol, args.output_root),
        "official_test_images_decoded_or_encoded": 0,
    }
    (args.output_root / "selection_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
