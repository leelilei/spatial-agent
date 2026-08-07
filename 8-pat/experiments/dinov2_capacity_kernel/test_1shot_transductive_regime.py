import numpy as np

from diagnose_1shot_transductive_regime import (
    sinkhorn_balanced,
    support_rotations,
)


def test_support_rotations_use_every_image_once():
    labels = np.repeat(np.arange(3), 4)
    image_ids = np.asarray([f"image-{index:02d}" for index in range(12)])
    rotations = support_rotations(labels, image_ids)
    supports = np.concatenate([support for support, _query in rotations])
    assert len(rotations) == 4
    assert np.array_equal(np.sort(supports), np.arange(12))
    assert all(np.array_equal(labels[support], np.arange(3)) for support, _ in rotations)


def test_sinkhorn_has_balanced_marginals():
    logits = np.asarray(
        [[3.0, 1.0], [2.0, 0.0], [0.0, 2.0], [1.0, 3.0]], dtype=float
    )
    assignment = sinkhorn_balanced(logits, examples_per_class=2, iterations=200)
    assert np.allclose(assignment.sum(axis=1), 1.0, atol=1e-6)
    assert np.allclose(assignment.sum(axis=0), 2.0, atol=1e-6)
