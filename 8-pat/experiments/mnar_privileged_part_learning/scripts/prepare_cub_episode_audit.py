#!/usr/bin/env python3
"""Freeze three CUB train-only 10-shot episodes and Random-K1 masks."""

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


def sample_episode_ids(candidates_by_class, shots, seed):
    """Sample a sorted tuple of image IDs per class without replacement."""
    rng = np.random.default_rng(int(seed))
    selected = {}
    for class_id in sorted(candidates_by_class):
        candidates = np.asarray(
            sorted(candidates_by_class[class_id]), dtype=np.int64
        )
        if len(candidates) < shots:
            raise RuntimeError(
                f"Class {class_id} has {len(candidates)} images, needs {shots}"
            )
        selected[class_id] = tuple(
            sorted(rng.choice(candidates, size=shots, replace=False).tolist())
        )
    return selected


def assign_folds(selected_by_class, folds, seed):
    """Assign exactly shots/folds images per class to every fold."""
    rng = np.random.default_rng(int(seed))
    assignments = {}
    for class_id in sorted(selected_by_class):
        image_ids = np.asarray(selected_by_class[class_id], dtype=np.int64)
        if len(image_ids) % folds:
            raise RuntimeError("shots_per_class must be divisible by folds")
        permutation = rng.permutation(image_ids)
        assignments.update(
            {
                int(image_id): int(position % folds)
                for position, image_id in enumerate(permutation.tolist())
            }
        )
    return assignments


def select_random_k1(labels, folds, image_ids, seed):
    """Select exactly one non-OOF image per class and outer fold."""
    selected = np.zeros((5, len(labels)), dtype=np.bool_)
    for fold in range(5):
        for class_index in range(200):
            candidates = np.flatnonzero(
                (labels == class_index) & (folds != fold)
            )
            if len(candidates) != 8:
                raise RuntimeError(
                    f"fold {fold}, class {class_index}: "
                    f"expected 8 candidates, got {len(candidates)}"
                )
            candidates = candidates[np.argsort(image_ids[candidates])]
            rng = np.random.default_rng(
                int(seed) + 10000 * fold + 100 * class_index
            )
            chosen = int(rng.choice(candidates))
            selected[fold, chosen] = True
    return selected


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
    labels_by_id = read_pairs(cub / "image_class_labels.txt", int)
    split = read_pairs(cub / "train_test_split.txt", int)

    keypoints = defaultdict(lambda: [[0.0, 0.0, 0] for _ in range(15)])
    for line in (cub / "parts" / "part_locs.txt").read_text().splitlines():
        image_id, part_id, x, y, visible = line.split()
        keypoints[int(image_id)][int(part_id) - 1] = [
            float(x),
            float(y),
            int(visible),
        ]

    candidates_by_class = defaultdict(list)
    for image_id, class_id in labels_by_id.items():
        if split[image_id] == 1:
            candidates_by_class[class_id].append(image_id)
    if len(candidates_by_class) != int(data["classes"]):
        raise RuntimeError("Official-train class count mismatch")

    subset_seeds = [int(x) for x in data["episode_subset_seeds"]]
    fold_seeds = [int(x) for x in data["episode_fold_seeds"]]
    selection_seeds = [
        int(x)
        for x in protocol["annotation_sampling"][
            "random_k1_selection_seeds_by_episode"
        ]
    ]
    if not (
        len(subset_seeds) == len(fold_seeds) == len(selection_seeds) == 3
    ):
        raise RuntimeError("Exactly three episode seeds are required")

    shots = int(data["shots_per_class_per_episode"])
    number_of_folds = int(data["folds"])
    episode_sets = []
    summaries = []
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for episode_index, (subset_seed, fold_seed, selection_seed) in enumerate(
        zip(subset_seeds, fold_seeds, selection_seeds), start=1
    ):
        selected_ids = sample_episode_ids(
            candidates_by_class, shots, subset_seed
        )
        assignments = assign_folds(
            selected_ids, number_of_folds, fold_seed
        )
        episode_sets.append(
            {image_id for values in selected_ids.values() for image_id in values}
        )
        rows = []
        for class_id in sorted(selected_ids):
            for image_id in selected_ids[class_id]:
                if split[image_id] != 1:
                    raise RuntimeError("Official test image entered episode")
                rows.append(
                    {
                        "image_id": image_id,
                        "relative_path": str(
                            Path("CUB_200_2011")
                            / "images"
                            / images[image_id]
                        ),
                        "class_index": class_id - 1,
                        "fold": assignments[image_id],
                        "keypoints": keypoints[image_id],
                        "split": "train",
                        "source_split": "official_train",
                        "episode": episode_index,
                    }
                )
        rows.sort(key=lambda row: (row["class_index"], row["image_id"]))
        labels = np.asarray([row["class_index"] for row in rows])
        folds = np.asarray([row["fold"] for row in rows])
        image_ids = np.asarray([row["image_id"] for row in rows])
        class_counts = Counter(labels.tolist())
        fold_counts = Counter(folds.tolist())
        if set(class_counts.values()) != {shots}:
            raise RuntimeError("Episode class balance failed")
        if set(fold_counts.values()) != {len(rows) // number_of_folds}:
            raise RuntimeError("Episode fold balance failed")

        selected_k1 = select_random_k1(
            labels, folds, image_ids, selection_seed
        )
        for fold in range(number_of_folds):
            mask = selected_k1[fold]
            if int(mask.sum()) != 200:
                raise RuntimeError("K1 total budget mismatch")
            if set(np.bincount(labels[mask], minlength=200).tolist()) != {1}:
                raise RuntimeError("K1 per-class budget mismatch")
            if np.any(mask & (folds == fold)):
                raise RuntimeError("OOF image selected for annotation")

        episode_dir = args.output_dir / f"episode_{episode_index}"
        episode_dir.mkdir(parents=True, exist_ok=True)
        manifest = episode_dir / "cub_train_10shot_manifest.jsonl"
        manifest.write_text(
            "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows)
        )
        selection = episode_dir / "random_k1_selection.npz"
        np.savez_compressed(selection, selected_random_k1=selected_k1)
        episode_summary = {
            "episode": episode_index,
            "subset_seed": subset_seed,
            "fold_seed": fold_seed,
            "selection_seed": selection_seed,
            "images": len(rows),
            "classes": len(class_counts),
            "shots_per_class": shots,
            "fold_counts": dict(sorted(fold_counts.items())),
            "selected_per_outer_fold": [
                int(selected_k1[fold].sum())
                for fold in range(number_of_folds)
            ],
            "manifest_sha256": sha256(manifest),
            "selection_sha256": sha256(selection),
            "official_test_images_decoded_or_encoded": 0,
        }
        (episode_dir / "episode_summary.json").write_text(
            json.dumps(episode_summary, indent=2, sort_keys=True) + "\n"
        )
        summaries.append(episode_summary)

    pairwise_overlap = {}
    for left in range(3):
        for right in range(left + 1, 3):
            overlap = len(episode_sets[left] & episode_sets[right])
            pairwise_overlap[f"episode_{left + 1}_vs_{right + 1}"] = {
                "shared_images": overlap,
                "fraction_of_episode": overlap / (200 * shots),
            }
    overall = {
        "experiment_id": protocol["experiment_id"],
        "episodes": summaries,
        "pairwise_overlap": pairwise_overlap,
        "unique_images_across_episodes": len(set.union(*episode_sets)),
        "official_train_class_count_distribution": dict(
            sorted(
                Counter(
                    len(values) for values in candidates_by_class.values()
                ).items()
            )
        ),
        "protocol_sha256": sha256(args.protocol),
        "official_test_images_decoded_or_encoded": 0,
    }
    (args.output_dir / "episode_audit_data_summary.json").write_text(
        json.dumps(overall, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(overall, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
