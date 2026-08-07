#!/usr/bin/env python3
"""Adaptive dual-geometry fusion screen for PAT-H-260729-004."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from sparse_anchor_utils import balanced_accuracy, class_recall


STATIC_WEIGHTS = (0.1, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0)
TEMPERATURES = (0.5, 1.0, 2.0, 4.0)
RANK_WEIGHTS = (0.25, 0.5, 0.75, 1.0)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def zscore_rows(scores: np.ndarray) -> np.ndarray:
    scores = np.asarray(scores, dtype=np.float64)
    return (scores - scores.mean(axis=1, keepdims=True)) / np.maximum(
        scores.std(axis=1, keepdims=True), 1e-12
    )


def top_margin(scores: np.ndarray) -> np.ndarray:
    top2 = np.partition(scores, -2, axis=1)[:, -2:]
    return top2.max(axis=1) - top2.min(axis=1)


def descending_rank_scores(scores: np.ndarray) -> np.ndarray:
    order = np.argsort(-scores, axis=1)
    ranks = np.empty_like(order)
    rows = np.arange(len(scores))[:, None]
    ranks[rows, order] = np.arange(scores.shape[1])[None, :]
    return -ranks.astype(np.float64)


def class_bootstrap_interval(delta, seed=9523, draws=20000):
    rng = np.random.default_rng(seed)
    indices = rng.integers(0, len(delta), (draws, len(delta)))
    values = delta[indices].mean(axis=1) * 100.0
    return [float(x) for x in np.quantile(values, [0.025, 0.5, 0.975])]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--h3-results", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    data = np.load(args.h3_results / "frozen_classifier_predictions.npz")
    labels = data["labels"]
    image_ids = data["image_ids"]
    rbf = zscore_rows(data["RBF_CLS_C3_scores"])
    ridge = zscore_rows(data["RIDGE_CLS_A0.1_scores"])
    proto = zscore_rows(data["PROTO_CLS_scores"])
    linear = zscore_rows(ridge + 0.75 * proto)

    predictions = {
        "RBF_CLS_C3": rbf.argmax(axis=1),
        "RIDGE_PROTO": linear.argmax(axis=1),
    }
    for weight in STATIC_WEIGHTS:
        predictions[f"STATIC_W{weight:g}"] = (rbf + weight * linear).argmax(axis=1)

    rbf_margin = top_margin(rbf)
    linear_margin = top_margin(linear)
    margin_delta = rbf_margin - linear_margin
    for temperature in TEMPERATURES:
        rbf_weight = 1.0 / (1.0 + np.exp(-temperature * margin_delta))
        fused = rbf_weight[:, None] * rbf + (1.0 - rbf_weight[:, None]) * linear
        predictions[f"ADAPTIVE_T{temperature:g}"] = fused.argmax(axis=1)

    rbf_rank = descending_rank_scores(rbf)
    linear_rank = descending_rank_scores(linear)
    for weight in RANK_WEIGHTS:
        predictions[f"RANK_W{weight:g}"] = (
            rbf_rank + weight * linear_rank
        ).argmax(axis=1)

    metrics = {
        name: balanced_accuracy(labels, prediction)
        for name, prediction in predictions.items()
    }
    baseline_name = "RBF_CLS_C3"
    baseline = metrics[baseline_name]
    adaptive_names = [name for name in metrics if name.startswith("ADAPTIVE_")]
    best_adaptive = max(adaptive_names, key=metrics.__getitem__)
    best_arm = max(metrics, key=metrics.__getitem__)
    gain_pp = 100.0 * (metrics[best_arm] - baseline)
    adaptive_gain_pp = 100.0 * (metrics[best_adaptive] - baseline)
    baseline_recall = class_recall(labels, predictions[baseline_name])
    winner_recall = class_recall(labels, predictions[best_arm])
    delta = winner_recall - baseline_recall
    summary = {
        "experiment_id": protocol["experiment_id"],
        "metrics": dict(sorted(metrics.items(), key=lambda item: item[1], reverse=True)),
        "baseline_arm": baseline_name,
        "best_arm": best_arm,
        "best_gain_pp_vs_rbf": gain_pp,
        "best_adaptive_arm": best_adaptive,
        "best_adaptive_gain_pp_vs_rbf": adaptive_gain_pp,
        "screen_success": bool(adaptive_gain_pp >= 0.5),
        "winner_class_bootstrap_delta_pp": class_bootstrap_interval(delta),
        "winner_positive_classes": int(np.sum(delta > 0)),
        "winner_negative_classes": int(np.sum(delta < 0)),
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
    }
    np.savez_compressed(
        args.output_dir / "adaptive_dual_geometry_predictions.npz",
        labels=labels,
        image_ids=image_ids,
        **{f"{name}_predictions": value for name, value in predictions.items()},
    )
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
