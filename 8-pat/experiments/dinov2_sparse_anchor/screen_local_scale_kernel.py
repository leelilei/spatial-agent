#!/usr/bin/env python3
"""Locally scaled RBF kernel screen on frozen DINOv2 features."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from sklearn.metrics import pairwise_distances
from sklearn.svm import SVC

from sparse_anchor_utils import balanced_accuracy, class_recall, l2_normalize


NEIGHBORS = (3, 5, 7, 15)
BETAS = (0.5, 1.0, 2.0, 4.0)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_scales(train_dist2, eval_dist2, neighbor):
    train_sorted = np.partition(train_dist2, neighbor - 1, axis=1)
    train_sigma = np.sqrt(np.maximum(train_sorted[:, neighbor - 1], 1e-12))
    eval_sorted = np.partition(eval_dist2, neighbor - 1, axis=1)
    eval_sigma = np.sqrt(np.maximum(eval_sorted[:, neighbor - 1], 1e-12))
    return train_sigma, eval_sigma


def class_bootstrap_interval(delta, seed=9527, draws=20000):
    rng = np.random.default_rng(seed)
    indices = rng.integers(0, len(delta), (draws, len(delta)))
    values = delta[indices].mean(axis=1) * 100.0
    return [float(x) for x in np.quantile(values, [0.025, 0.5, 0.975])]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--feature-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    labels = np.load(args.feature_dir / "labels.npy")
    folds = np.load(args.feature_dir / "folds.npy")
    image_ids = np.load(args.feature_dir / "image_ids.npy")
    features = l2_normalize(np.load(args.feature_dir / "cls.npy", mmap_mode="r"))
    arm_names = [
        f"LOCAL_K{neighbor}_B{beta:g}"
        for neighbor in NEIGHBORS
        for beta in BETAS
    ]
    predictions = {
        "GLOBAL_RBF": np.full(len(labels), -1, dtype=np.int64),
        **{
            name: np.full(len(labels), -1, dtype=np.int64)
            for name in arm_names
        },
    }
    for fold in range(5):
        train = np.flatnonzero(folds != fold)
        evaluate_on = np.flatnonzero(folds == fold)
        train_x = features[train]
        eval_x = features[evaluate_on]
        global_rbf = SVC(C=3.0, kernel="rbf", gamma="scale").fit(
            train_x, labels[train]
        )
        predictions["GLOBAL_RBF"][evaluate_on] = global_rbf.predict(eval_x)
        train_dist2 = pairwise_distances(
            train_x, train_x, metric="sqeuclidean", n_jobs=-1
        )
        np.fill_diagonal(train_dist2, np.inf)
        eval_dist2 = pairwise_distances(
            eval_x, train_x, metric="sqeuclidean", n_jobs=-1
        )
        for neighbor in NEIGHBORS:
            train_sigma, eval_sigma = local_scales(
                train_dist2, eval_dist2, neighbor
            )
            train_denominator = np.maximum(
                train_sigma[:, None] * train_sigma[None, :], 1e-12
            )
            eval_denominator = np.maximum(
                eval_sigma[:, None] * train_sigma[None, :], 1e-12
            )
            for beta in BETAS:
                name = f"LOCAL_K{neighbor}_B{beta:g}"
                train_kernel = np.exp(
                    -train_dist2 / (beta * train_denominator)
                )
                np.fill_diagonal(train_kernel, 1.0)
                eval_kernel = np.exp(
                    -eval_dist2 / (beta * eval_denominator)
                )
                classifier = SVC(C=3.0, kernel="precomputed").fit(
                    train_kernel, labels[train]
                )
                predictions[name][evaluate_on] = classifier.predict(eval_kernel)
        print(json.dumps({"status": "LOCAL_KERNEL_FOLD_COMPLETE", "fold": fold}), flush=True)
    metrics = {
        name: balanced_accuracy(labels, prediction)
        for name, prediction in predictions.items()
    }
    candidates = [name for name in metrics if name != "GLOBAL_RBF"]
    best_arm = max(candidates, key=metrics.__getitem__)
    gain_pp = 100.0 * (metrics[best_arm] - metrics["GLOBAL_RBF"])
    baseline_recall = class_recall(labels, predictions["GLOBAL_RBF"])
    winner_recall = class_recall(labels, predictions[best_arm])
    delta = winner_recall - baseline_recall
    summary = {
        "experiment_id": protocol["experiment_id"],
        "metrics": dict(sorted(metrics.items(), key=lambda item: item[1], reverse=True)),
        "best_arm": best_arm,
        "gain_pp_vs_global_rbf": gain_pp,
        "screen_success": bool(gain_pp >= 0.5),
        "winner_positive_classes": int(np.sum(delta > 0)),
        "winner_negative_classes": int(np.sum(delta < 0)),
        "winner_class_bootstrap_delta_pp": class_bootstrap_interval(delta),
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
    }
    np.savez_compressed(
        args.output_dir / "local_kernel_predictions.npz",
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
