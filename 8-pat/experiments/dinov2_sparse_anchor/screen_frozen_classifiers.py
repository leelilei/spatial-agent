#!/usr/bin/env python3
"""Frozen DINOv2 classifier/global-local screen for PAT-H-260729-003."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from sklearn.linear_model import RidgeClassifier
from sklearn.svm import SVC

from sparse_anchor_utils import balanced_accuracy, class_recall, l2_normalize


RIDGE_ALPHAS = (0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0)
SVC_CS = (1.0, 3.0, 10.0, 30.0)
FUSION_WEIGHTS = (0.1, 0.25, 0.5, 0.75)
CLASSES = 200


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def zscore_rows(scores: np.ndarray) -> np.ndarray:
    scores = np.asarray(scores, dtype=np.float64)
    return (scores - scores.mean(axis=1, keepdims=True)) / np.maximum(
        scores.std(axis=1, keepdims=True), 1e-12
    )


def prototype_scores(
    train_features: np.ndarray,
    train_labels: np.ndarray,
    eval_features: np.ndarray,
) -> np.ndarray:
    prototypes = np.stack(
        [train_features[train_labels == label].mean(axis=0) for label in range(CLASSES)]
    )
    prototypes = l2_normalize(prototypes)
    return eval_features @ prototypes.T


def class_bootstrap_interval(delta, seed=9522, draws=20000):
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
    cls = l2_normalize(np.load(args.feature_dir / "cls.npy", mmap_mode="r"))
    patch = l2_normalize(np.load(args.feature_dir / "mean_patch.npy", mmap_mode="r"))

    scores: dict[str, np.ndarray] = {}
    for alpha in RIDGE_ALPHAS:
        scores[f"RIDGE_CLS_A{alpha:g}"] = np.full(
            (len(labels), CLASSES), np.nan, dtype=np.float32
        )
    scores["PROTO_CLS"] = np.full(
        (len(labels), CLASSES), np.nan, dtype=np.float32
    )
    for c_value in SVC_CS:
        scores[f"RBF_CLS_C{c_value:g}"] = np.full(
            (len(labels), CLASSES), np.nan, dtype=np.float32
        )
        scores[f"RBF_PATCH_C{c_value:g}"] = np.full(
            (len(labels), CLASSES), np.nan, dtype=np.float32
        )

    for fold in range(5):
        train = np.flatnonzero(folds != fold)
        evaluate_on = np.flatnonzero(folds == fold)
        for alpha in RIDGE_ALPHAS:
            model = RidgeClassifier(alpha=alpha).fit(cls[train], labels[train])
            scores[f"RIDGE_CLS_A{alpha:g}"][evaluate_on] = model.decision_function(
                cls[evaluate_on]
            ).astype(np.float32)
        scores["PROTO_CLS"][evaluate_on] = prototype_scores(
            cls[train], labels[train], cls[evaluate_on]
        ).astype(np.float32)
        for c_value in SVC_CS:
            for view_name, train_x, eval_x in (
                ("CLS", cls[train], cls[evaluate_on]),
                ("PATCH", patch[train], patch[evaluate_on]),
            ):
                model = SVC(C=c_value, kernel="rbf", gamma="scale").fit(
                    train_x, labels[train]
                )
                decision = model.decision_function(eval_x)
                scores[f"RBF_{view_name}_C{c_value:g}"][evaluate_on] = decision.astype(
                    np.float32
                )
        print(f"completed fold {fold}", flush=True)

    predictions = {name: value.argmax(axis=1) for name, value in scores.items()}
    for alpha in RIDGE_ALPHAS:
        ridge_name = f"RIDGE_CLS_A{alpha:g}"
        ridge_z = zscore_rows(scores[ridge_name])
        proto_z = zscore_rows(scores["PROTO_CLS"])
        for weight in FUSION_WEIGHTS:
            name = f"RIDGE_PROTO_A{alpha:g}_W{weight:g}"
            predictions[name] = (ridge_z + weight * proto_z).argmax(axis=1)
    for c_value in SVC_CS:
        cls_z = zscore_rows(scores[f"RBF_CLS_C{c_value:g}"])
        patch_z = zscore_rows(scores[f"RBF_PATCH_C{c_value:g}"])
        for weight in FUSION_WEIGHTS:
            name = f"RBF_GLOBAL_LOCAL_C{c_value:g}_W{weight:g}"
            predictions[name] = (cls_z + weight * patch_z).argmax(axis=1)

    metrics = {
        name: balanced_accuracy(labels, prediction)
        for name, prediction in predictions.items()
    }
    baseline_name = "RIDGE_CLS_A1"
    baseline = metrics[baseline_name]
    best_arm = max(metrics, key=metrics.__getitem__)
    gain_pp = 100.0 * (metrics[best_arm] - baseline)
    baseline_recall = class_recall(labels, predictions[baseline_name])
    winner_recall = class_recall(labels, predictions[best_arm])
    delta = winner_recall - baseline_recall
    summary = {
        "experiment_id": protocol["experiment_id"],
        "metrics": dict(sorted(metrics.items(), key=lambda item: item[1], reverse=True)),
        "baseline_arm": baseline_name,
        "best_arm": best_arm,
        "best_gain_pp_vs_cls_ridge_a1": gain_pp,
        "screen_success": bool(gain_pp >= 0.5),
        "winner_class_bootstrap_delta_pp": class_bootstrap_interval(delta),
        "winner_positive_classes": int(np.sum(delta > 0)),
        "winner_negative_classes": int(np.sum(delta < 0)),
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
    }
    np.savez_compressed(
        args.output_dir / "frozen_classifier_predictions.npz",
        labels=labels,
        image_ids=image_ids,
        **{f"{name}_scores": value for name, value in scores.items()},
        **{f"{name}_predictions": value for name, value in predictions.items()},
    )
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
