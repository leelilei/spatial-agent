"""Image-only active annotation selection utilities for PAT-D-260728-005.

This module is deliberately independent of CUB keypoint rendering.  Its public
interfaces accept only a sanitized selector manifest and frozen ordinary-image
features.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ALLOWED_SELECTOR_KEYS = (
    "relative_path",
    "class_index",
    "fold",
    "image_id",
)
STRATEGIES = (
    "MEDOID",
    "BOUNDARY",
    "DISCRIMINATIVE",
    "BALANCED_ANNOTATION_VALUE",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sanitize_row(row) -> dict:
    """Copy only selector-authorized fields without enumerating source fields."""
    clean = {key: row[key] for key in ALLOWED_SELECTOR_KEYS}
    clean["class_index"] = int(clean["class_index"])
    clean["fold"] = int(clean["fold"])
    try:
        clean["image_id"] = int(clean["image_id"])
    except (TypeError, ValueError):
        clean["image_id"] = str(clean["image_id"])
    clean["relative_path"] = str(clean["relative_path"])
    return clean


def load_and_sanitize_manifest(path: Path) -> list[dict]:
    rows = [
        sanitize_row(json.loads(line))
        for line in path.read_text().splitlines()
        if line.strip()
    ]
    if not rows:
        raise RuntimeError("Selector manifest is empty")
    if any(row["fold"] < 0 for row in rows):
        raise RuntimeError("Every selector row must have a non-negative fold")
    return rows


def write_selector_manifest(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = "".join(
        json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n"
        for row in rows
    )
    path.write_text(payload)


def l2_normalize(values: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(values, axis=1, keepdims=True)
    if np.any(norms <= 0):
        raise RuntimeError("Frozen feature contains a zero-norm row")
    return values / norms


def percentile_rank(values: np.ndarray) -> np.ndarray:
    """Deterministic [1/n, 1] average-tie percentile ranks."""
    values = np.asarray(values, dtype=np.float64)
    result = np.empty(len(values), dtype=np.float64)
    order = np.argsort(values, kind="mergesort")
    start = 0
    while start < len(values):
        end = start + 1
        while end < len(values) and values[order[end]] == values[order[start]]:
            end += 1
        average_position = 0.5 * ((start + 1) + end)
        result[order[start:end]] = average_position / len(values)
        start = end
    return result


def score_fold(
    features: np.ndarray,
    labels: np.ndarray,
    folds: np.ndarray,
    fold: int,
) -> dict[str, np.ndarray]:
    """Score fold-training candidates using image features and labels only."""
    features = l2_normalize(np.asarray(features, dtype=np.float64))
    labels = np.asarray(labels, dtype=np.int64)
    folds = np.asarray(folds, dtype=np.int64)
    train = folds != fold
    classes = np.unique(labels)
    centroids = {}
    for class_index in classes:
        indices = np.flatnonzero(train & (labels == class_index))
        if len(indices) < 2:
            raise RuntimeError(
                f"Fold {fold} class {class_index} has fewer than 2 candidates"
            )
        centroid = features[indices].mean(axis=0)
        centroid /= np.linalg.norm(centroid)
        centroids[int(class_index)] = centroid

    representativeness = np.full(len(labels), np.nan, dtype=np.float64)
    margin = np.full(len(labels), np.nan, dtype=np.float64)
    uncertainty = np.full(len(labels), np.nan, dtype=np.float64)
    balanced = np.full(len(labels), np.nan, dtype=np.float64)
    centroid_matrix = np.stack([centroids[int(c)] for c in classes])

    for class_position, class_index in enumerate(classes):
        indices = np.flatnonzero(train & (labels == class_index))
        class_sum = features[indices].sum(axis=0)
        own_similarity = np.empty(len(indices), dtype=np.float64)
        for offset, row_index in enumerate(indices):
            leave_one_out = class_sum - features[row_index]
            leave_one_out /= np.linalg.norm(leave_one_out)
            own_similarity[offset] = features[row_index] @ leave_one_out
        other_centroids = np.delete(centroid_matrix, class_position, axis=0)
        nearest_other = (features[indices] @ other_centroids.T).max(axis=1)
        class_margin = own_similarity - nearest_other
        class_uncertainty = -class_margin
        rep_rank = percentile_rank(own_similarity)
        uncertainty_rank = percentile_rank(class_uncertainty)
        harmonic = (
            2.0
            * rep_rank
            * uncertainty_rank
            / (rep_rank + uncertainty_rank)
        )
        representativeness[indices] = own_similarity
        margin[indices] = class_margin
        uncertainty[indices] = class_uncertainty
        balanced[indices] = harmonic

    return {
        "representativeness": representativeness,
        "margin": margin,
        "uncertainty": uncertainty,
        "balanced_annotation_value": balanced,
    }


def select_one_per_class(
    scores: dict[str, np.ndarray],
    labels: np.ndarray,
    folds: np.ndarray,
    image_ids: np.ndarray,
    fold: int,
    strategy: str,
) -> np.ndarray:
    if strategy not in STRATEGIES:
        raise ValueError(f"Unknown strategy: {strategy}")
    score_name = {
        "MEDOID": "representativeness",
        "BOUNDARY": "uncertainty",
        "DISCRIMINATIVE": "margin",
        "BALANCED_ANNOTATION_VALUE": "balanced_annotation_value",
    }[strategy]
    values = scores[score_name]
    selected = np.zeros(len(labels), dtype=np.bool_)
    for class_index in np.unique(labels):
        candidates = np.flatnonzero(
            (folds != fold) & (labels == class_index)
        )
        candidate_scores = values[candidates]
        if np.isnan(candidate_scores).any():
            raise RuntimeError("Training candidate has no selector score")
        best_score = candidate_scores.max()
        tied = candidates[np.isclose(candidate_scores, best_score)]
        def image_id_key(index):
            value = image_ids[index]
            try:
                return 0, int(value)
            except (TypeError, ValueError):
                return 1, str(value)

        winner = min(tied.tolist(), key=image_id_key)
        selected[winner] = True
    return selected


def validate_selection(
    selected: np.ndarray,
    labels: np.ndarray,
    folds: np.ndarray,
    fold: int,
    expected_classes: int,
) -> None:
    if selected.dtype != np.bool_:
        raise RuntimeError("Selection mask must be boolean")
    if np.any(selected & (folds == fold)):
        raise RuntimeError("OOF row selected for annotation")
    if int(selected.sum()) != expected_classes:
        raise RuntimeError("Selection does not contain one row per class")
    counts = np.bincount(labels[selected], minlength=expected_classes)
    if not np.array_equal(counts, np.ones(expected_classes, dtype=int)):
        raise RuntimeError("Per-class K1 budget invariant failed")
