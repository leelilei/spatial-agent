import numpy as np

from screen_dino_semantic_part_queries import (
    PARTS,
    combined_representation,
    deterministic_background_indices,
    localization_hit_counts,
    spatial_softmax_pool_numpy,
)


def test_background_sampling_is_deterministic_and_far_from_keypoints():
    keypoints = np.full(PARTS, -1, dtype=np.int64)
    keypoints[:2] = [14 * 28 + 14, 5 * 28 + 7]
    first = deterministic_background_indices(keypoints, count=8, seed=11)
    second = deterministic_background_indices(keypoints, count=8, seed=11)
    assert np.array_equal(first, second)
    yy, xx = np.divmod(first, 28)
    for point in keypoints[:2]:
        py, px = divmod(int(point), 28)
        assert np.all(np.maximum(np.abs(yy - py), np.abs(xx - px)) >= 3)


def test_zero_scores_reduce_to_uniform_patch_pooling():
    rng = np.random.default_rng(3)
    patches = rng.normal(size=(2, 9, 4)).astype(np.float32)
    scores = np.zeros((2, PARTS, 9), dtype=np.float32)
    aggregate, predicted = spatial_softmax_pool_numpy(patches, scores)
    normalized = patches / np.linalg.norm(patches, axis=2, keepdims=True)
    expected = normalized.mean(axis=1)
    expected /= np.linalg.norm(expected, axis=1, keepdims=True)
    assert np.allclose(aggregate, expected, atol=1e-6)
    assert np.array_equal(predicted, np.zeros((2, PARTS), dtype=np.int16))


def test_localization_hit_uses_three_by_three_token_neighborhood():
    predicted = np.array([[29, 100, 300]])
    targets = np.array([[0, 101, -1]])
    hits, visible = localization_hit_counts(predicted, targets, grid=28)
    assert (hits, visible) == (2, 2)


def test_combined_representation_has_unit_norm():
    cls = np.array([[3.0, 4.0], [1.0, 0.0]])
    part = np.array([[0.0, 2.0], [0.0, 5.0]])
    combined = combined_representation(cls, part)
    assert combined.shape == (2, 4)
    assert np.allclose(np.linalg.norm(combined, axis=1), 1.0)
