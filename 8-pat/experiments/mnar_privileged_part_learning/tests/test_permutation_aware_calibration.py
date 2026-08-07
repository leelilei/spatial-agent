import sys
from pathlib import Path

import numpy as np
import pytest


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from permutation_aware_calibration import (  # noqa: E402
    attention_hit_counts,
    derive_mapping,
    fold_selected_indices,
    solve_part_to_channel,
    spatial_nll_cost,
)


def synthetic_maps():
    targets = np.zeros((4, 3, 5, 5), dtype=np.float64)
    locations = ((0, 0), (2, 3), (4, 1))
    for image in range(4):
        for part, (yy, xx) in enumerate(locations):
            targets[image, part, yy, xx] = 1.0
    part_to_channel = np.array([2, 0, 1])
    attention = np.full((4, 3, 5, 5), -8.0)
    for part, channel in enumerate(part_to_channel):
        yy, xx = locations[part]
        attention[:, channel, yy, xx] = 8.0
    return attention, targets, part_to_channel


def test_assignment_recovers_known_permutation():
    attention, targets, expected = synthetic_maps()
    actual = derive_mapping(attention, targets)
    assert np.array_equal(actual, expected)


def test_assignment_is_deterministic_and_one_to_one():
    cost = np.array([[4.0, 1.0, 3.0], [2.0, 0.0, 5.0], [3.0, 2.0, 2.0]])
    first = solve_part_to_channel(cost)
    second = solve_part_to_channel(cost)
    assert np.array_equal(first, second)
    assert sorted(first.tolist()) == [0, 1, 2]


def test_hit_rate_uses_the_frozen_mapping():
    attention, targets, mapping = synthetic_maps()
    hits, visible = attention_hit_counts(attention, targets, mapping)
    assert hits == visible == 12


def test_shape_and_nan_controls():
    with pytest.raises(ValueError):
        spatial_nll_cost(np.zeros((2, 3, 5)), np.zeros((2, 3, 5, 5)))
    with pytest.raises(ValueError):
        solve_part_to_channel(np.array([[0.0, np.nan], [1.0, 2.0]]))


def test_selection_rejects_outer_fold_leakage_and_wrong_budget():
    selected = np.array([True, False, True, False, False])
    with pytest.raises(ValueError, match="outer-fold"):
        fold_selected_indices(selected, np.array([0, 1, 3, 4]), 5, 1)
    with pytest.raises(ValueError, match="expected 1"):
        fold_selected_indices(selected, np.array([0, 1, 2, 3]), 5, 1)
    actual = fold_selected_indices(
        np.array([True, False, False, False, False]),
        np.array([0, 1, 2, 3]),
        5,
        1,
    )
    assert np.array_equal(actual, np.array([0]))
