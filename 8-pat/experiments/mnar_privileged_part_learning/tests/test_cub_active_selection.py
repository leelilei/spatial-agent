from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from cub_active_selection import (  # noqa: E402
    STRATEGIES,
    sanitize_row,
    score_fold,
    select_one_per_class,
    validate_selection,
)


class PoisonRow(dict):
    def __getitem__(self, key):
        if key in {"keypoints", "part_locations", "bounding_box"}:
            raise AssertionError("Selector attempted privileged-field access")
        return super().__getitem__(key)


class ActiveSelectionTests(unittest.TestCase):
    def fixture(self):
        rng = np.random.default_rng(123)
        classes, folds, per_fold, dimension = 3, 3, 2, 8
        labels, fold_values, image_ids, features = [], [], [], []
        image_id = 1
        class_bases = np.eye(classes, dimension)
        for class_index in range(classes):
            for fold in range(folds):
                for _ in range(per_fold):
                    labels.append(class_index)
                    fold_values.append(fold)
                    image_ids.append(image_id)
                    features.append(
                        class_bases[class_index]
                        + 0.05 * rng.standard_normal(dimension)
                    )
                    image_id += 1
        return (
            np.asarray(features),
            np.asarray(labels),
            np.asarray(fold_values),
            np.asarray(image_ids),
        )

    def test_sanitizer_never_reads_privileged_fields(self):
        row = PoisonRow(
            relative_path="train/example.jpg",
            class_index=2,
            fold=1,
            image_id=9,
            keypoints="poison",
        )
        clean = sanitize_row(row)
        self.assertEqual(
            set(clean),
            {"relative_path", "class_index", "fold", "image_id"},
        )

    def test_all_selectors_are_deterministic_and_exact_k1(self):
        features, labels, folds, image_ids = self.fixture()
        first = score_fold(features, labels, folds, 0)
        second = score_fold(features, labels, folds, 0)
        for score_name in first:
            np.testing.assert_allclose(
                first[score_name], second[score_name], equal_nan=True
            )
        for strategy in STRATEGIES:
            selected_a = select_one_per_class(
                first, labels, folds, image_ids, 0, strategy
            )
            selected_b = select_one_per_class(
                second, labels, folds, image_ids, 0, strategy
            )
            np.testing.assert_array_equal(selected_a, selected_b)
            validate_selection(selected_a, labels, folds, 0, 3)
            self.assertFalse(np.any(selected_a & (folds == 0)))

    def test_tie_break_uses_lowest_image_id(self):
        features = np.asarray(
            [
                [1.0, 0.0],
                [1.0, 0.0],
                [1.0, 0.0],
                [0.0, 1.0],
                [0.0, 1.0],
                [0.0, 1.0],
            ]
        )
        labels = np.asarray([0, 0, 0, 1, 1, 1])
        folds = np.asarray([0, 1, 2, 0, 1, 2])
        image_ids = np.asarray([99, 5, 7, 100, 2, 3])
        scores = score_fold(features, labels, folds, 0)
        selected = select_one_per_class(
            scores, labels, folds, image_ids, 0, "MEDOID"
        )
        self.assertEqual(set(image_ids[selected]), {2, 5})


if __name__ == "__main__":
    unittest.main()
