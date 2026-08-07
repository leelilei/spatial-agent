#!/usr/bin/env python3
"""Nested-OOF capacity-complementary score selector for PAT-J-260729-002."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from sklearn.svm import SVC

from screen_dual_capacity_kernel import CLASSES, balanced_accuracy, class_recall, load_pair


FUSION_WEIGHTS = tuple(np.round(np.arange(0.1, 1.0, 0.1), 1))
ROUTE_THRESHOLDS = (0.0, 0.25, 0.5, 0.75, 1.0)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def zscore_rows(scores: np.ndarray) -> np.ndarray:
    scores = np.asarray(scores, dtype=np.float64)
    return (scores - scores.mean(axis=1, keepdims=True)) / np.maximum(
        scores.std(axis=1, keepdims=True), 1e-12
    )


def rank_scores(scores: np.ndarray) -> np.ndarray:
    order = np.argsort(-scores, axis=1)
    ranks = np.empty_like(order)
    rows = np.arange(len(scores))[:, None]
    ranks[rows, order] = np.arange(scores.shape[1])[None, :]
    return -ranks.astype(np.float64)


def top_margin(scores: np.ndarray) -> np.ndarray:
    top2 = np.partition(scores, -2, axis=1)[:, -2:]
    return top2.max(axis=1) - top2.min(axis=1)


def fit_components(train_x, train_y, eval_x):
    model = SVC(C=3.0, kernel="rbf", gamma="scale").fit(train_x, train_y)
    if not np.array_equal(model.classes_, np.arange(CLASSES)):
        raise RuntimeError("SVC score columns do not match class indices")
    return model.predict(eval_x), model.decision_function(eval_x)


def candidate_predictions(b_pred, l_pred, b_scores, l_scores):
    bz = zscore_rows(b_scores)
    lz = zscore_rows(l_scores)
    br = rank_scores(b_scores)
    lr = rank_scores(l_scores)
    result = {"B_ONLY": b_pred.copy(), "L_ONLY": l_pred.copy()}
    for weight in FUSION_WEIGHTS:
        suffix = f"{int(round(weight * 100)):03d}"
        result[f"ZSCORE_L{suffix}"] = (
            (1.0 - weight) * bz + weight * lz
        ).argmax(axis=1)
        result[f"RANK_L{suffix}"] = (
            (1.0 - weight) * br + weight * lr
        ).argmax(axis=1)
    margin_delta = top_margin(lz) - top_margin(bz)
    for threshold in ROUTE_THRESHOLDS:
        name = f"ROUTE_T{int(round(threshold * 100)):03d}"
        result[name] = np.where(margin_delta >= threshold, l_pred, b_pred)
    return result


def mode_order(name: str) -> int:
    if name == "B_ONLY":
        return 0
    if name.startswith("ROUTE_"):
        return 1
    if name.startswith("ZSCORE_"):
        return 2
    if name.startswith("RANK_"):
        return 3
    return 4


def select_candidate(labels, b_pred, l_pred, b_scores, l_scores):
    candidates = candidate_predictions(b_pred, l_pred, b_scores, l_scores)
    metrics = {name: balanced_accuracy(labels, pred) for name, pred in candidates.items()}
    switches = {name: int(np.sum(pred != b_pred)) for name, pred in candidates.items()}
    selected = max(
        candidates,
        key=lambda name: (metrics[name], -switches[name], -mode_order(name), name),
    )
    return selected, metrics, switches


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
        for name in ("B_RBF", "L_RBF", "CCSS")
    }
    fold_details = []
    noninferior = 0
    for outer_fold in sorted(np.unique(folds)):
        outer_train = np.flatnonzero(folds != outer_fold)
        outer_eval = np.flatnonzero(folds == outer_fold)
        inner_b_pred = np.full(len(outer_train), -1, dtype=np.int64)
        inner_l_pred = np.full(len(outer_train), -1, dtype=np.int64)
        inner_b_scores = np.full((len(outer_train), CLASSES), np.nan)
        inner_l_scores = np.full((len(outer_train), CLASSES), np.nan)
        for inner_fold in sorted(np.unique(folds[outer_train])):
            local_eval = np.flatnonzero(folds[outer_train] == inner_fold)
            inner_eval = outer_train[local_eval]
            inner_train = outer_train[folds[outer_train] != inner_fold]
            inner_b_pred[local_eval], inner_b_scores[local_eval] = fit_components(
                b[inner_train], labels[inner_train], b[inner_eval]
            )
            inner_l_pred[local_eval], inner_l_scores[local_eval] = fit_components(
                l[inner_train], labels[inner_train], l[inner_eval]
            )
        selected, inner_metrics, switches = select_candidate(
            labels[outer_train], inner_b_pred, inner_l_pred, inner_b_scores, inner_l_scores
        )
        b_pred, b_scores = fit_components(b[outer_train], labels[outer_train], b[outer_eval])
        l_pred, l_scores = fit_components(l[outer_train], labels[outer_train], l[outer_eval])
        outer_candidates = candidate_predictions(b_pred, l_pred, b_scores, l_scores)
        predictions["B_RBF"][outer_eval] = b_pred
        predictions["L_RBF"][outer_eval] = l_pred
        predictions["CCSS"][outer_eval] = outer_candidates[selected]
        fold_metrics = {
            name: balanced_accuracy(labels[outer_eval], pred[outer_eval])
            for name, pred in predictions.items()
        }
        noninferior += int(fold_metrics["CCSS"] >= fold_metrics["B_RBF"])
        detail = {
            "outer_fold": int(outer_fold),
            "selected_candidate": selected,
            "inner_selected_metric": inner_metrics[selected],
            "inner_b_metric": inner_metrics["B_ONLY"],
            "inner_l_metric": inner_metrics["L_ONLY"],
            "inner_switches_from_b": switches[selected],
            "outer_metrics": fold_metrics,
        }
        fold_details.append(detail)
        print(json.dumps(detail, sort_keys=True), flush=True)
    metrics = {name: balanced_accuracy(labels, pred) for name, pred in predictions.items()}
    delta = class_recall(labels, predictions["CCSS"]) - class_recall(labels, predictions["B_RBF"])
    gain_b = 100.0 * (metrics["CCSS"] - metrics["B_RBF"])
    gain_l = 100.0 * (metrics["CCSS"] - metrics["L_RBF"])
    positive = int(np.sum(delta > 0))
    negative = int(np.sum(delta < 0))
    worst = float(delta.min())
    gates = {
        "gain_over_b_at_least_1pp": bool(gain_b >= 1.0 - 1e-12),
        "at_least_4_noninferior_outer_folds": bool(noninferior >= 4),
        "negative_classes_not_more_than_positive": bool(negative <= positive),
        "worst_class_delta_at_least_minus_0_3": bool(worst >= -0.3 - 1e-12),
    }
    summary = {
        "experiment_id": protocol["experiment_id"],
        "metrics": metrics,
        "ccss_gain_over_b_pp": gain_b,
        "ccss_gain_over_l_pp": gain_l,
        "noninferior_outer_folds_vs_b": noninferior,
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
        args.output_dir / "capacity_score_selector_predictions.npz",
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
