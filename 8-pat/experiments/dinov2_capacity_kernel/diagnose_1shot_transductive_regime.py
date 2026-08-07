#!/usr/bin/env python3
"""Diagnose whether CUB 200-way 1-shot is a useful lower-accuracy regime.

This is a task-regime diagnostic, not a method-selection or confirmatory run.
Each of the ten rotations uses one labelled support image per class and treats
the remaining nine images per class as an unlabeled, class-balanced query set.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from sklearn.svm import SVC

from screen_dual_capacity_kernel import load_pair


def l2_normalize(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64)
    return x / np.maximum(np.linalg.norm(x, axis=1, keepdims=True), 1e-12)


def balanced_accuracy(labels: np.ndarray, predictions: np.ndarray) -> float:
    classes = np.unique(labels)
    return float(
        np.mean([np.mean(predictions[labels == label] == label) for label in classes])
    )


def support_rotations(
    labels: np.ndarray, image_ids: np.ndarray
) -> list[tuple[np.ndarray, np.ndarray]]:
    """Return rotations in which every image is support exactly once."""
    classes = np.unique(labels)
    per_class = []
    for label in classes:
        indices = np.flatnonzero(labels == label)
        ordered = indices[np.argsort(image_ids[indices].astype(str))]
        per_class.append(ordered)
    shots = {len(indices) for indices in per_class}
    if len(shots) != 1:
        raise ValueError(f"expected a balanced episode, found class sizes {shots}")
    rotations = []
    for rotation in range(shots.pop()):
        support = np.asarray([indices[rotation] for indices in per_class])
        support_mask = np.zeros(len(labels), dtype=bool)
        support_mask[support] = True
        rotations.append((support, np.flatnonzero(~support_mask)))
    return rotations


def nearest_support(
    support_x: np.ndarray, support_y: np.ndarray, query_x: np.ndarray
) -> np.ndarray:
    return support_y[np.argmax(query_x @ support_x.T, axis=1)]


def rbf_svc(
    support_x: np.ndarray, support_y: np.ndarray, query_x: np.ndarray
) -> np.ndarray:
    return SVC(C=3.0, kernel="rbf", gamma="scale").fit(
        support_x, support_y
    ).predict(query_x)


def sinkhorn_balanced(
    logits: np.ndarray, examples_per_class: int, iterations: int = 100
) -> np.ndarray:
    """Normalize positive scores to row mass 1 and fixed class marginals."""
    shifted = logits - logits.max(axis=1, keepdims=True)
    assignment = np.exp(np.clip(shifted, -60.0, 0.0)) + 1e-12
    target_columns = np.full(logits.shape[1], float(examples_per_class))
    for _ in range(iterations):
        assignment /= np.maximum(assignment.sum(axis=1, keepdims=True), 1e-12)
        assignment *= target_columns / np.maximum(
            assignment.sum(axis=0), 1e-12
        )
    assignment /= np.maximum(assignment.sum(axis=1, keepdims=True), 1e-12)
    return assignment


def balanced_prototype_refinement(
    support_x: np.ndarray,
    support_y: np.ndarray,
    query_x: np.ndarray,
    temperature: float,
    refinement_steps: int = 10,
) -> np.ndarray:
    """Standard transductive prototype refinement used as a feasibility probe."""
    classes = np.unique(support_y)
    if not np.array_equal(classes, np.arange(len(classes))):
        raise ValueError("class labels must be contiguous from zero")
    if len(query_x) % len(classes):
        raise ValueError("balanced refinement requires equal query class sizes")
    examples_per_class = len(query_x) // len(classes)
    prototypes = support_x.copy()
    assignment = None
    for _ in range(refinement_steps):
        assignment = sinkhorn_balanced(
            (query_x @ prototypes.T) / temperature, examples_per_class
        )
        query_centres = assignment.T @ query_x
        prototypes = l2_normalize(
            support_x + query_centres / np.maximum(assignment.sum(axis=0)[:, None], 1e-12)
        )
    assert assignment is not None
    return classes[np.argmax(assignment, axis=1)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b-feature-dir", type=Path, required=True)
    parser.add_argument("--l-feature-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    b, l, labels, _folds, image_ids = load_pair(
        args.b_feature_dir, args.l_feature_dir
    )
    fused = l2_normalize(np.concatenate([b, l], axis=1))
    feature_sets = {"B": b, "L": l, "BL_CONCAT": fused}
    temperatures = (0.03, 0.05, 0.07, 0.10, 0.15)
    rows = []
    for rotation, (support, query) in enumerate(
        support_rotations(labels, image_ids)
    ):
        row: dict[str, float | int] = {"rotation": rotation}
        for feature_name, features in feature_sets.items():
            support_x = features[support]
            support_y = labels[support]
            query_x = features[query]
            query_y = labels[query]
            row[f"{feature_name}_NCC"] = balanced_accuracy(
                query_y, nearest_support(support_x, support_y, query_x)
            )
            row[f"{feature_name}_RBF"] = balanced_accuracy(
                query_y, rbf_svc(support_x, support_y, query_x)
            )
            similarities = query_x @ support_x.T
            for temperature in temperatures:
                name = f"{feature_name}_SINKHORN_T{temperature:.2f}"
                assignment = sinkhorn_balanced(
                    similarities / temperature,
                    examples_per_class=len(query_x) // len(support_y),
                )
                row[name] = balanced_accuracy(
                    query_y, support_y[np.argmax(assignment, axis=1)]
                )
        rows.append(row)
        print(json.dumps(row, sort_keys=True), flush=True)
    metric_names = sorted(set(rows[0]) - {"rotation"})
    aggregate = {
        name: {
            "mean": float(np.mean([row[name] for row in rows])),
            "sample_std": float(np.std([row[name] for row in rows], ddof=1)),
            "min": float(np.min([row[name] for row in rows])),
            "max": float(np.max([row[name] for row in rows])),
        }
        for name in metric_names
    }
    result = {
        "status": "TASK_REGIME_DIAGNOSTIC_ONLY",
        "setting": "CUB official-train episode, 200-way 1-shot, 9 balanced unlabeled queries per class",
        "selection_warning": "Temperatures are displayed descriptively and must not be selected as a confirmatory method using these query labels.",
        "rotations": rows,
        "aggregate": aggregate,
        "official_test_images_decoded_or_encoded": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"aggregate": aggregate}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
