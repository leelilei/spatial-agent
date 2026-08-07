#!/usr/bin/env python3
"""Post-screen strong-Ridge preservation diagnostic for PAT-H-260729-002."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from sklearn.linear_model import RidgeClassifier

from sparse_anchor_utils import (
    balanced_accuracy,
    class_recall,
    fused_candidate_predictions,
    l2_normalize,
)


CLASSES = 200
PART_ALPHAS = (0.01, 0.025, 0.05, 0.1, 0.25, 0.5)
PATCH_WEIGHTS = (0.25, 0.5, 0.75, 1.0)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def zscore_rows(scores):
    scores = np.asarray(scores, dtype=np.float64)
    return (scores - scores.mean(axis=1, keepdims=True)) / np.maximum(
        scores.std(axis=1, keepdims=True), 1e-12
    )


def class_bootstrap_interval(delta, seed=9521, draws=20000):
    rng = np.random.default_rng(seed)
    indices = rng.integers(0, len(delta), (draws, len(delta)))
    values = delta[indices].mean(axis=1) * 100.0
    return [float(x) for x in np.quantile(values, [0.025, 0.5, 0.975])]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--feature-dir", type=Path, required=True)
    parser.add_argument("--h1-results", type=Path, required=True)
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
    cls = l2_normalize(np.load(args.feature_dir / "cls.npy", mmap_mode="r"))
    combined = l2_normalize(
        np.concatenate(
            [
                l2_normalize(np.load(args.feature_dir / "cls.npy", mmap_mode="r")),
                l2_normalize(
                    np.load(args.feature_dir / "mean_patch.npy", mmap_mode="r")
                ),
            ],
            axis=1,
        )
    )
    cls_scores = np.full((len(labels), CLASSES), np.nan, dtype=np.float32)
    patch_scores = np.full_like(cls_scores, np.nan)
    for fold in range(5):
        train = np.flatnonzero(folds != fold)
        evaluate_on = np.flatnonzero(folds == fold)
        cls_model = RidgeClassifier(alpha=1.0).fit(cls[train], labels[train])
        patch_model = RidgeClassifier(alpha=1.0).fit(
            combined[train], labels[train]
        )
        cls_scores[evaluate_on] = cls_model.decision_function(
            cls[evaluate_on]
        ).astype(np.float32)
        patch_scores[evaluate_on] = patch_model.decision_function(
            combined[evaluate_on]
        ).astype(np.float32)
    predictions = {"CLS_RIDGE": cls_scores.argmax(axis=1)}
    cls_z = zscore_rows(cls_scores)
    patch_z = zscore_rows(patch_scores)
    for weight in PATCH_WEIGHTS:
        predictions[f"RIDGE_ENSEMBLE_W{weight:g}"] = (
            cls_z + weight * patch_z
        ).argmax(axis=1)
    h1 = np.load(args.h1_results / "sparse_anchor_predictions.npz")
    if not np.array_equal(labels, h1["labels"]):
        raise RuntimeError("PAT-H-260729-001 labels mismatch")
    candidates = h1["candidates"].astype(np.int64)
    equal_scores = h1["equal_part_scores"]
    aware_scores = h1["confusion_aware_scores"]
    ridge_prediction = predictions["CLS_RIDGE"]
    ridge_present = np.any(candidates == ridge_prediction[:, None], axis=1)
    candidate_ridge_scores = np.take_along_axis(cls_scores, candidates, axis=1)
    for name, local_scores in (
        ("EQUAL", equal_scores),
        ("CA_SAP", aware_scores),
    ):
        for alpha in PART_ALPHAS:
            prediction = ridge_prediction.copy()
            reranked = fused_candidate_predictions(
                candidates,
                candidate_ridge_scores,
                local_scores,
                alpha,
            )
            prediction[ridge_present] = reranked[ridge_present]
            predictions[f"RIDGE_{name}_A{alpha:g}"] = prediction
    metrics = {
        name: balanced_accuracy(labels, prediction)
        for name, prediction in predictions.items()
    }
    baseline = metrics["CLS_RIDGE"]
    candidate_arms = [name for name in metrics if name != "CLS_RIDGE"]
    best_arm = max(candidate_arms, key=metrics.__getitem__)
    gain_pp = 100.0 * (metrics[best_arm] - baseline)
    baseline_recall = class_recall(labels, predictions["CLS_RIDGE"])
    winner_recall = class_recall(labels, predictions[best_arm])
    delta = winner_recall - baseline_recall
    summary = {
        "experiment_id": protocol["experiment_id"],
        "metrics": metrics,
        "ridge_prediction_present_in_stored_top10_rate": float(
            ridge_present.mean()
        ),
        "best_arm": best_arm,
        "best_gain_pp_vs_cls_ridge": gain_pp,
        "screen_success": bool(gain_pp >= 0.5),
        "winner_class_bootstrap_delta_pp": class_bootstrap_interval(delta),
        "winner_positive_classes": int(np.sum(delta > 0)),
        "winner_negative_classes": int(np.sum(delta < 0)),
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
    }
    np.savez_compressed(
        args.output_dir / "ridge_part_residual_predictions.npz",
        labels=labels,
        image_ids=image_ids,
        cls_ridge_scores=cls_scores,
        cls_patch_ridge_scores=patch_scores,
        **{f"{name}_predictions": value for name, value in predictions.items()},
    )
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
