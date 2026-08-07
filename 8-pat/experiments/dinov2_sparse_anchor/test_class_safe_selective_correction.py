import numpy as np

from screen_class_safe_selective_correction import (
    accepted_pairs,
    apply_policy,
    correction_counts,
    knn_predictions_and_purity,
    pair_statistics,
    top_margin,
)


def test_top_margin_uses_two_largest_scores():
    scores = np.array([[0.1, 0.8, 0.5], [3.0, 1.0, 2.5]])
    assert np.allclose(top_margin(scores), [0.3, 0.5])


def test_knn_tie_breaks_by_similarity_sum():
    train_x = np.array([[1.0, 0.0], [0.9, 0.1], [0.0, 1.0]])
    train_y = np.array([0, 1, 2])
    eval_x = np.array([[1.0, 0.0]])
    prediction, purity = knn_predictions_and_purity(
        train_x, train_y, eval_x, k=3, classes=3
    )
    assert prediction.tolist() == [0]
    assert np.allclose(purity, [1.0 / 3.0])


def test_only_zero_harm_pairs_are_accepted():
    base = np.array([0, 0, 0, 2, 2])
    candidate = np.array([1, 1, 1, 3, 3])
    labels = np.array([1, 1, 0, 3, 2])
    stats = pair_statistics(base, candidate, labels, np.ones(5, dtype=bool))
    assert stats[(0, 1)]["wins"] == 2
    assert stats[(0, 1)]["harms"] == 1
    assert stats[(2, 3)]["wins"] == 1
    assert accepted_pairs(stats) == set()


def test_policy_changes_only_preapproved_ordered_pairs():
    components = {
        "rbf_prediction": np.array([0, 0, 2]),
        "rbf_margin": np.array([0.1, 0.1, 0.1]),
        "prototype_prediction": np.array([1, 2, 3]),
        "knn_3_prediction": np.array([1, 2, 3]),
        "knn_3_purity": np.array([1.0, 1.0, 1.0]),
    }
    policy = {
        "k": 3,
        "margin_cutoff": 0.2,
        "purity_threshold": 1.0,
        "accepted_pairs": {(0, 1), (2, 3)},
    }
    corrected, selected = apply_policy(components, policy)
    assert corrected.tolist() == [1, 0, 3]
    assert selected.tolist() == [True, False, True]
    counts = correction_counts(
        np.array([1, 0, 4]), components["rbf_prediction"], corrected
    )
    assert counts == {"actions": 2, "wins": 1, "harms": 0, "neutral": 1}
