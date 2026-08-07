#!/usr/bin/env python3
"""Pure NumPy utilities for PAT-H-260729-001."""

from __future__ import annotations

import numpy as np


def l2_normalize(values, axis=-1, eps=1e-12):
    values = np.asarray(values, dtype=np.float32)
    return values / np.maximum(
        np.linalg.norm(values, axis=axis, keepdims=True), eps
    )


def class_recall(labels, predictions, classes=200):
    labels = np.asarray(labels)
    predictions = np.asarray(predictions)
    return np.asarray(
        [
            np.mean(predictions[labels == class_index] == class_index)
            for class_index in range(classes)
        ],
        dtype=np.float64,
    )


def balanced_accuracy(labels, predictions, classes=200):
    return float(class_recall(labels, predictions, classes).mean())


def log_softmax(values, axis=-1):
    values = np.asarray(values, dtype=np.float64)
    shifted = values - values.max(axis=axis, keepdims=True)
    return shifted - np.log(np.exp(shifted).sum(axis=axis, keepdims=True))


def fused_candidate_predictions(
    candidates,
    global_scores,
    local_scores,
    alpha,
    local_temperature=0.07,
):
    candidates = np.asarray(candidates, dtype=np.int64)
    if candidates.shape != np.asarray(global_scores).shape:
        raise ValueError("candidate and global-score shapes differ")
    if candidates.shape != np.asarray(local_scores).shape:
        raise ValueError("candidate and local-score shapes differ")
    fused = log_softmax(global_scores) + float(alpha) * log_softmax(
        np.asarray(local_scores) / float(local_temperature)
    )
    return candidates[np.arange(len(candidates)), fused.argmax(axis=1)]


def validate_sparse_selection(selected, train_indices, labels, classes=200):
    selected = np.asarray(selected, dtype=np.bool_)
    labels = np.asarray(labels, dtype=np.int64)
    allowed = np.zeros(len(labels), dtype=np.bool_)
    allowed[np.asarray(train_indices, dtype=np.int64)] = True
    if selected.shape != labels.shape:
        raise ValueError("selection mask and labels differ in length")
    if np.any(selected & ~allowed):
        raise ValueError("selection contains outer-fold evaluation images")
    selected_indices = np.flatnonzero(selected)
    counts = np.bincount(labels[selected_indices], minlength=classes)
    if not np.all(counts == 1):
        raise ValueError("selection must contain exactly one image per class")
    return selected_indices


def evaluate_screen(
    labels,
    predictions,
    primary_global="CLS_PATCH_LOGREG",
    alphas=(0.25, 0.5, 1.0, 2.0),
):
    metrics = {
        key: balanced_accuracy(labels, value)
        for key, value in predictions.items()
    }
    global_ba = metrics[primary_global]
    equal_keys = [f"EQUAL_A{alpha:g}" for alpha in alphas]
    aware_keys = [f"CA_SAP_A{alpha:g}" for alpha in alphas]
    best_equal = max(equal_keys, key=metrics.__getitem__)
    best_aware = max(aware_keys, key=metrics.__getitem__)
    absolute_pp = 100.0 * (metrics[best_aware] - global_ba)
    mechanism_pp = 100.0 * (metrics[best_aware] - metrics[best_equal])
    return {
        "metrics": metrics,
        "foundation_gate_pass": bool(global_ba >= 0.76),
        "best_equal_arm": best_equal,
        "best_confusion_aware_arm": best_aware,
        "best_confusion_aware_gain_pp_vs_global": absolute_pp,
        "best_confusion_aware_gain_pp_vs_best_equal": mechanism_pp,
        "screen_success": bool(absolute_pp >= 1.0 and mechanism_pp >= 0.5),
    }
