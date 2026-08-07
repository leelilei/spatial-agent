"""Exact image-only K2 facility selection for PAT-D-260728-007."""

from __future__ import annotations

import itertools

import numpy as np


STRATEGIES = ("FEATURE_FACILITY", "GRADIENT_FACILITY")


def normalize_rows(values: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=np.float64)
    norms = np.linalg.norm(values, axis=1, keepdims=True)
    if np.any(norms <= 0):
        raise RuntimeError("Cannot normalize a zero-norm selector vector")
    return values / norms


def feature_similarity(features: np.ndarray) -> np.ndarray:
    normalized = normalize_rows(features)
    return normalized @ normalized.T


def implicit_gradient_similarity(
    features: np.ndarray,
    probabilities: np.ndarray,
    labels: np.ndarray,
) -> np.ndarray:
    """Cosine kernel for vec((p-y) outer f) without materializing gradients."""
    probabilities = np.asarray(probabilities, dtype=np.float64)
    labels = np.asarray(labels, dtype=np.int64)
    if probabilities.shape[0] != len(labels):
        raise RuntimeError("Probability/label row mismatch")
    errors = probabilities.copy()
    errors[np.arange(len(labels)), labels] -= 1.0
    return feature_similarity(features) * (
        normalize_rows(errors) @ normalize_rows(errors).T
    )


def image_id_key(value):
    try:
        return 0, int(value)
    except (TypeError, ValueError):
        return 1, str(value)


def exact_facility_pair(
    similarity: np.ndarray, image_ids: np.ndarray
) -> tuple[np.ndarray, float]:
    similarity = np.asarray(similarity, dtype=np.float64)
    if similarity.ndim != 2 or similarity.shape[0] != similarity.shape[1]:
        raise RuntimeError("Facility similarity must be square")
    if len(similarity) < 2:
        raise RuntimeError("At least two candidates are required")
    best_pair = None
    best_score = -float("inf")
    best_key = None
    for left, right in itertools.combinations(range(len(similarity)), 2):
        score = float(
            np.maximum(similarity[:, left], similarity[:, right]).mean()
        )
        pair_key = tuple(
            sorted(
                (image_id_key(image_ids[left]), image_id_key(image_ids[right]))
            )
        )
        if (
            score > best_score + 1e-12
            or (
                abs(score - best_score) <= 1e-12
                and (best_key is None or pair_key < best_key)
            )
        ):
            best_pair = np.asarray([left, right], dtype=np.int64)
            best_score = score
            best_key = pair_key
    return best_pair, best_score


def validate_k2_mask(
    selected: np.ndarray,
    labels: np.ndarray,
    folds: np.ndarray,
    fold: int,
    classes: int,
) -> None:
    if selected.dtype != np.bool_:
        raise RuntimeError("Selection mask must be boolean")
    if np.any(selected & (folds == fold)):
        raise RuntimeError("OOF row selected by K2 selector")
    if int(selected.sum()) != 2 * classes:
        raise RuntimeError("K2 selection count mismatch")
    counts = np.bincount(labels[selected], minlength=classes)
    if not np.array_equal(counts, np.full(classes, 2, dtype=int)):
        raise RuntimeError("K2 per-class budget mismatch")
