#!/usr/bin/env python3
"""Recompute archived PAT-K-004/005/006 metrics and split invariants."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def assert_close(actual: float, expected: float, context: str) -> None:
    if not np.isclose(actual, expected, atol=1e-12):
        raise AssertionError(f"{context}: {actual} != {expected}")


def audit_balanced(root: Path, expected_episodes: int) -> int:
    summary = json.loads((root / "formal" / "summary.json").read_text())
    if summary["official_test_images_decoded_or_encoded"] != 0:
        raise AssertionError("official test access is nonzero")
    checked = 0
    for episode in summary["episodes"]:
        episode_id = episode["episode"]
        archive = np.load(root / "formal" / f"episode_{episode_id}_predictions.npz")
        labels = archive["query_labels"]
        if labels.shape[0] != 10:
            raise AssertionError("expected ten support rotations")
        for method, reported in episode["aggregate"].items():
            predictions = archive[f"{method}_predictions"]
            if predictions.shape != labels.shape:
                raise AssertionError(f"{method} prediction shape mismatch")
            rotation_scores = np.mean(predictions == labels, axis=1)
            assert_close(float(rotation_scores.mean()), reported["mean"], f"episode {episode_id} {method}")
            checked += predictions.size
    if len(summary["episodes"]) != expected_episodes:
        raise AssertionError("unexpected episode count")
    return checked


def macro_accuracy(labels: np.ndarray, predictions: np.ndarray) -> float:
    return float(
        np.mean([
            np.mean(predictions[labels == class_index] == class_index)
            for class_index in np.unique(labels)
        ])
    )


def audit_stress(root: Path) -> int:
    summary = json.loads((root / "formal" / "summary.json").read_text())
    if summary["official_test_images_decoded_or_encoded"] != 0:
        raise AssertionError("official test access is nonzero")
    checked = 0
    for result in summary["results"]:
        episode = result["episode"]
        regime = result["regime"].lower()
        archive = np.load(root / "formal" / f"episode_{episode}_{regime}_predictions.npz")
        labels = archive["query_labels"]
        for method, reported in result["aggregate"].items():
            predictions = archive[f"{method}_predictions"]
            micro = float(np.mean(predictions == labels))
            macros = [macro_accuracy(y, p) for y, p in zip(labels, predictions)]
            assert_close(micro, reported["micro_accuracy"], f"stress {episode} {regime} {method} micro")
            assert_close(float(np.mean(macros)), reported["macro_balanced_accuracy"], f"stress {episode} {regime} {method} macro")
            checked += predictions.size
    return checked


def audit_dogs_features_and_manifests(root: Path) -> None:
    selection = json.loads((root / "data" / "selection_summary.json").read_text())
    if selection["official_test_list_loaded"] or selection["official_test_images_decoded_or_encoded"] != 0:
        raise AssertionError("Stanford Dogs test data was accessed")
    ids = set()
    for episode in (1, 2, 3):
        manifest = root / "data" / f"episode_{episode}" / "stanford_dogs_train_10shot_manifest.jsonl"
        rows = [json.loads(line) for line in manifest.read_text().splitlines()]
        if len(rows) != 1200:
            raise AssertionError("unexpected Dogs manifest size")
        if any(row["split"] != "train" or row["source_split"] != "official_train" for row in rows):
            raise AssertionError("non-train row in Dogs manifest")
        episode_ids = {row["image_id"] for row in rows}
        if ids.intersection(episode_ids):
            raise AssertionError("Dogs episodes overlap")
        ids.update(episode_ids)
        b_dir = root / "features" / f"b_episode_{episode}"
        l_dir = root / "features" / f"l_episode_{episode}"
        for name in ("labels.npy", "folds.npy", "image_ids.npy"):
            if not np.array_equal(np.load(b_dir / name), np.load(l_dir / name)):
                raise AssertionError(f"Dogs B/L mismatch: episode {episode} {name}")
        for feature_dir in (b_dir, l_dir):
            metadata = json.loads((feature_dir / "metadata.json").read_text())
            if metadata["official_test_images_decoded_or_encoded"] != 0:
                raise AssertionError("feature metadata reports test access")
    if len(ids) != 3600:
        raise AssertionError("unexpected unique Dogs image count")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pat-k004", type=Path, required=True)
    parser.add_argument("--pat-k005", type=Path, required=True)
    parser.add_argument("--pat-k006", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    checked = audit_balanced(args.pat_k004, 3)
    checked += audit_stress(args.pat_k005)
    audit_dogs_features_and_manifests(args.pat_k006)
    checked += audit_balanced(args.pat_k006, 3)
    print(json.dumps({
        "status": "PASS",
        "prediction_values_recomputed": checked,
        "dogs_unique_train_images": 3600,
        "official_test_images_decoded_or_encoded": 0,
    }, indent=2))


if __name__ == "__main__":
    main()
