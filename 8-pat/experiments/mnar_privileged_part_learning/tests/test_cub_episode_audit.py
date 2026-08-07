import sys
from collections import defaultdict
from pathlib import Path

import numpy as np


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from prepare_cub_episode_audit import (  # noqa: E402
    assign_folds,
    sample_episode_ids,
    select_random_k1,
)


def synthetic_candidates(images_per_class=30):
    return {
        class_id: list(
            range(class_id * images_per_class, (class_id + 1) * images_per_class)
        )
        for class_id in range(1, 201)
    }


def test_episode_sampling_is_deterministic_and_balanced():
    candidates = synthetic_candidates()
    first = sample_episode_ids(candidates, 10, 8801)
    second = sample_episode_ids(candidates, 10, 8801)
    different = sample_episode_ids(candidates, 10, 8802)
    assert first == second
    assert first != different
    assert set(map(len, first.values())) == {10}
    assert all(set(first[key]) <= set(candidates[key]) for key in first)


def test_fold_assignment_has_two_images_per_class():
    selected = sample_episode_ids(synthetic_candidates(), 10, 8801)
    folds = assign_folds(selected, 5, 8811)
    counts = defaultdict(lambda: np.zeros(5, dtype=int))
    for class_id, image_ids in selected.items():
        for image_id in image_ids:
            counts[class_id][folds[image_id]] += 1
    assert all(values.tolist() == [2, 2, 2, 2, 2] for values in counts.values())


def test_random_k1_budget_and_no_oof_access():
    labels = np.repeat(np.arange(200), 10)
    folds = np.tile(np.repeat(np.arange(5), 2), 200)
    image_ids = np.arange(2000)
    first = select_random_k1(labels, folds, image_ids, 8901)
    second = select_random_k1(labels, folds, image_ids, 8901)
    assert np.array_equal(first, second)
    for fold in range(5):
        mask = first[fold]
        assert int(mask.sum()) == 200
        assert set(np.bincount(labels[mask], minlength=200).tolist()) == {1}
        assert not np.any(mask & (folds == fold))
