import numpy as np
import pytest

from sparse_anchor_utils import (
    fused_candidate_predictions,
    l2_normalize,
    validate_sparse_selection,
)


def test_normalization():
    value = l2_normalize(np.array([[3.0, 4.0]]))
    assert np.allclose(value, [[0.6, 0.8]])


def test_fusion_can_rerank_top_candidates():
    candidates = np.array([[4, 7], [2, 9]])
    global_scores = np.array([[3.0, 2.9], [4.0, 2.0]])
    local_scores = np.array([[0.1, 0.9], [0.9, 0.1]])
    prediction = fused_candidate_predictions(
        candidates, global_scores, local_scores, alpha=1.0
    )
    assert np.array_equal(prediction, np.array([7, 2]))


def test_selection_rejects_outer_fold_and_wrong_class_budget():
    labels = np.array([0, 0, 1, 1])
    with pytest.raises(ValueError, match="outer-fold"):
        validate_sparse_selection(
            np.array([True, False, True, False]),
            np.array([0, 1, 3]),
            labels,
            classes=2,
        )
    with pytest.raises(ValueError, match="exactly one"):
        validate_sparse_selection(
            np.array([True, True, False, False]),
            np.arange(4),
            labels,
            classes=2,
        )
