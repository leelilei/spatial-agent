#!/usr/bin/env python3
"""Nested-OOF dual-capacity kernel selection for PAT-J-260729-001."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.svm import SVC


MODES = (
    "B_ONLY",
    "L_ONLY",
    "ADD_L025",
    "ADD_L050",
    "ADD_L075",
    "GEO_L025",
    "GEO_L050",
    "GEO_L075",
)
TIE_ORDER = (
    "L_ONLY",
    "B_ONLY",
    "ADD_L050",
    "GEO_L050",
    "ADD_L075",
    "ADD_L025",
    "GEO_L075",
    "GEO_L025",
)
CLASSES = 200


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def l2_normalize(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float32)
    return x / np.maximum(np.linalg.norm(x, axis=1, keepdims=True), 1e-12)


def balanced_accuracy(labels: np.ndarray, prediction: np.ndarray) -> float:
    return float(np.mean([np.mean(prediction[labels == c] == c) for c in range(CLASSES)]))


def class_recall(labels: np.ndarray, prediction: np.ndarray) -> np.ndarray:
    return np.asarray([np.mean(prediction[labels == c] == c) for c in range(CLASSES)])


def gamma_scale(x: np.ndarray) -> float:
    return 1.0 / (x.shape[1] * float(np.var(x)))


def capacity_kernels(
    b_train: np.ndarray,
    l_train: np.ndarray,
    b_eval: np.ndarray,
    l_eval: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    gamma_b = gamma_scale(b_train)
    gamma_l = gamma_scale(l_train)
    return (
        rbf_kernel(b_train, b_train, gamma=gamma_b),
        rbf_kernel(b_eval, b_train, gamma=gamma_b),
        rbf_kernel(l_train, l_train, gamma=gamma_l),
        rbf_kernel(l_eval, l_train, gamma=gamma_l),
    )


def mode_kernel(mode: str, kb: np.ndarray, kl: np.ndarray) -> np.ndarray:
    if mode == "B_ONLY":
        return kb
    if mode == "L_ONLY":
        return kl
    weight = int(mode[-3:]) / 100.0
    if mode.startswith("ADD_"):
        return (1.0 - weight) * kb + weight * kl
    if mode.startswith("GEO_"):
        return np.power(np.maximum(kb, 1e-30), 1.0 - weight) * np.power(
            np.maximum(kl, 1e-30), weight
        )
    raise ValueError(f"unknown mode {mode}")


def predict_mode(
    mode: str,
    b_train: np.ndarray,
    l_train: np.ndarray,
    labels: np.ndarray,
    b_eval: np.ndarray,
    l_eval: np.ndarray,
) -> np.ndarray:
    kb_train, kb_eval, kl_train, kl_eval = capacity_kernels(
        b_train, l_train, b_eval, l_eval
    )
    classifier = SVC(C=3.0, kernel="precomputed")
    classifier.fit(mode_kernel(mode, kb_train, kl_train), labels)
    return classifier.predict(mode_kernel(mode, kb_eval, kl_eval))


def select_mode(
    b: np.ndarray,
    l: np.ndarray,
    labels: np.ndarray,
    folds: np.ndarray,
    outer_train: np.ndarray,
) -> tuple[str, dict[str, float]]:
    predictions = {
        mode: np.full(len(outer_train), -1, dtype=np.int64) for mode in MODES
    }
    for inner_fold in sorted(np.unique(folds[outer_train])):
        local_eval = np.flatnonzero(folds[outer_train] == inner_fold)
        inner_eval = outer_train[local_eval]
        inner_train = outer_train[folds[outer_train] != inner_fold]
        kb_train, kb_eval, kl_train, kl_eval = capacity_kernels(
            b[inner_train], l[inner_train], b[inner_eval], l[inner_eval]
        )
        for mode in MODES:
            classifier = SVC(C=3.0, kernel="precomputed")
            classifier.fit(
                mode_kernel(mode, kb_train, kl_train), labels[inner_train]
            )
            predictions[mode][local_eval] = classifier.predict(
                mode_kernel(mode, kb_eval, kl_eval)
            )
    metrics = {
        mode: balanced_accuracy(labels[outer_train], prediction)
        for mode, prediction in predictions.items()
    }
    order = {mode: -index for index, mode in enumerate(TIE_ORDER)}
    selected = max(MODES, key=lambda mode: (metrics[mode], order[mode]))
    return selected, metrics


def load_pair(b_dir: Path, l_dir: Path):
    names = ("labels.npy", "folds.npy", "image_ids.npy")
    b_meta = {name: np.load(b_dir / name) for name in names}
    l_meta = {name: np.load(l_dir / name) for name in names}
    for name in names:
        if not np.array_equal(b_meta[name], l_meta[name]):
            raise RuntimeError(f"B/L mismatch in {name}")
    b = l2_normalize(np.load(b_dir / "cls.npy", mmap_mode="r"))
    l = l2_normalize(np.load(l_dir / "cls.npy", mmap_mode="r"))
    return b, l, b_meta["labels.npy"], b_meta["folds.npy"], b_meta["image_ids.npy"]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--b-feature-dir", type=Path, required=True)
    parser.add_argument("--l-feature-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    b, l, labels, folds, image_ids = load_pair(args.b_feature_dir, args.l_feature_dir)
    predictions = {
        name: np.full(len(labels), -1, dtype=np.int64)
        for name in ("B_RBF", "L_RBF", "DCKS")
    }
    fold_details = []
    noninferior_folds = 0
    for outer_fold in sorted(np.unique(folds)):
        train = np.flatnonzero(folds != outer_fold)
        evaluate_on = np.flatnonzero(folds == outer_fold)
        selected_mode, inner_metrics = select_mode(b, l, labels, folds, train)
        predictions["B_RBF"][evaluate_on] = predict_mode(
            "B_ONLY", b[train], l[train], labels[train], b[evaluate_on], l[evaluate_on]
        )
        predictions["L_RBF"][evaluate_on] = predict_mode(
            "L_ONLY", b[train], l[train], labels[train], b[evaluate_on], l[evaluate_on]
        )
        predictions["DCKS"][evaluate_on] = predict_mode(
            selected_mode, b[train], l[train], labels[train], b[evaluate_on], l[evaluate_on]
        )
        fold_metrics = {
            name: balanced_accuracy(labels[evaluate_on], pred[evaluate_on])
            for name, pred in predictions.items()
        }
        noninferior_folds += int(fold_metrics["DCKS"] >= fold_metrics["B_RBF"])
        fold_details.append({
            "outer_fold": int(outer_fold),
            "selected_mode": selected_mode,
            "inner_metrics": inner_metrics,
            "outer_metrics": fold_metrics,
        })
        print(json.dumps(fold_details[-1], sort_keys=True), flush=True)
    metrics = {name: balanced_accuracy(labels, pred) for name, pred in predictions.items()}
    delta = class_recall(labels, predictions["DCKS"]) - class_recall(labels, predictions["B_RBF"])
    gain_b = 100.0 * (metrics["DCKS"] - metrics["B_RBF"])
    gain_l = 100.0 * (metrics["DCKS"] - metrics["L_RBF"])
    positive = int(np.sum(delta > 0))
    negative = int(np.sum(delta < 0))
    worst = float(delta.min())
    gates = {
        "gain_over_b_at_least_1pp": bool(gain_b >= 1.0 - 1e-12),
        "at_least_4_noninferior_outer_folds": bool(noninferior_folds >= 4),
        "negative_classes_not_more_than_positive": bool(negative <= positive),
        "worst_class_delta_at_least_minus_0_3": bool(worst >= -0.3 - 1e-12),
    }
    summary = {
        "experiment_id": protocol["experiment_id"],
        "metrics": metrics,
        "dcks_gain_over_b_pp": gain_b,
        "dcks_gain_over_l_pp": gain_l,
        "noninferior_outer_folds_vs_b": noninferior_folds,
        "positive_class_count_vs_b": positive,
        "negative_class_count_vs_b": negative,
        "worst_class_recall_delta_vs_b": worst,
        "fold_details": fold_details,
        "gates": gates,
        "screen_success": bool(all(gates.values())),
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
    }
    np.savez_compressed(
        args.output_dir / "dual_capacity_kernel_predictions.npz",
        labels=labels,
        folds=folds,
        image_ids=image_ids,
        class_recall_delta_vs_b=delta,
        **{f"{name}_predictions": pred for name, pred in predictions.items()},
    )
    (args.output_dir / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
