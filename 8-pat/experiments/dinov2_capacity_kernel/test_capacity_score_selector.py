import numpy as np

from develop_capacity_score_selector import (
    candidate_predictions,
    rank_scores,
    top_margin,
    zscore_rows,
)


def test_zscore_rows_are_centered_and_scaled():
    scores = np.array([[1.0, 2.0, 3.0], [2.0, 4.0, 8.0]])
    value = zscore_rows(scores)
    assert np.allclose(value.mean(axis=1), 0.0)
    assert np.allclose(value.std(axis=1), 1.0)


def test_rank_scores_assign_zero_to_best_class():
    scores = np.array([[0.1, 0.8, 0.3]])
    ranks = rank_scores(scores)
    assert ranks.tolist() == [[-2.0, 0.0, -1.0]]


def test_top_margin_uses_largest_two_scores():
    assert np.allclose(top_margin(np.array([[0.1, 0.9, 0.5]])), [0.4])


def test_route_keeps_b_when_l_margin_advantage_is_small():
    b_scores = np.array([[3.0, 1.0, 0.0], [1.0, 0.9, 0.0]])
    l_scores = np.array([[2.0, 1.9, 0.0], [3.0, 0.0, -1.0]])
    b_pred = np.array([0, 0])
    l_pred = np.array([0, 1])
    candidates = candidate_predictions(b_pred, l_pred, b_scores, l_scores)
    assert candidates["ROUTE_T050"][0] == 0
    assert candidates["ROUTE_T000"].shape == (2,)
