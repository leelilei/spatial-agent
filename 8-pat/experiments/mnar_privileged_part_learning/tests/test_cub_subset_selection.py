from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from cub_subset_selection import (  # noqa: E402
    exact_facility_pair,
    implicit_gradient_similarity,
    validate_k2_mask,
)


class K2SubsetSelectionTests(unittest.TestCase):
    def test_exact_pair_is_deterministic(self):
        similarity = np.asarray(
            [
                [1.0, 0.9, 0.1, 0.0],
                [0.9, 1.0, 0.0, 0.1],
                [0.1, 0.0, 1.0, 0.9],
                [0.0, 0.1, 0.9, 1.0],
            ]
        )
        image_ids = np.asarray([40, 10, 30, 20])
        first, first_score = exact_facility_pair(similarity, image_ids)
        second, second_score = exact_facility_pair(similarity, image_ids)
        np.testing.assert_array_equal(first, second)
        self.assertEqual(first_score, second_score)
        self.assertEqual(set(image_ids[first]), {10, 20})

    def test_implicit_gradient_kernel_is_finite_and_symmetric(self):
        features = np.asarray(
            [[1.0, 0.0], [0.9, 0.1], [0.0, 1.0]]
        )
        probabilities = np.asarray(
            [[0.7, 0.2, 0.1], [0.6, 0.3, 0.1], [0.1, 0.2, 0.7]]
        )
        labels = np.asarray([0, 0, 2])
        kernel = implicit_gradient_similarity(
            features, probabilities, labels
        )
        self.assertTrue(np.isfinite(kernel).all())
        np.testing.assert_allclose(kernel, kernel.T)
        np.testing.assert_allclose(np.diag(kernel), np.ones(3))

    def test_k2_budget_and_oof_control(self):
        labels = np.repeat(np.arange(3), 6)
        folds = np.tile(np.repeat(np.arange(3), 2), 3)
        selected = np.zeros(len(labels), dtype=np.bool_)
        for class_index in range(3):
            candidates = np.flatnonzero(
                (labels == class_index) & (folds != 0)
            )
            selected[candidates[:2]] = True
        validate_k2_mask(selected, labels, folds, 0, 3)
        selected[np.flatnonzero(folds == 0)[0]] = True
        with self.assertRaises(RuntimeError):
            validate_k2_mask(selected, labels, folds, 0, 3)


if __name__ == "__main__":
    unittest.main()
