import numpy as np

from screen_dual_capacity_kernel import gamma_scale, mode_kernel


def test_gamma_scale_matches_sklearn_definition():
    x = np.array([[0.0, 1.0], [2.0, 3.0]], dtype=np.float32)
    assert np.isclose(gamma_scale(x), 1.0 / (x.shape[1] * x.var()))


def test_additive_kernel_is_convex_combination():
    kb = np.array([[1.0, 0.2], [0.2, 1.0]])
    kl = np.array([[1.0, 0.6], [0.6, 1.0]])
    assert np.allclose(mode_kernel("ADD_L025", kb, kl), 0.75 * kb + 0.25 * kl)


def test_geometric_kernel_matches_weighted_product():
    kb = np.array([[1.0, 0.25], [0.25, 1.0]])
    kl = np.array([[1.0, 0.81], [0.81, 1.0]])
    expected = np.sqrt(kb * kl)
    assert np.allclose(mode_kernel("GEO_L050", kb, kl), expected)


def test_endpoint_modes_return_original_kernel():
    kb = np.eye(3)
    kl = np.full((3, 3), 0.5)
    assert np.array_equal(mode_kernel("B_ONLY", kb, kl), kb)
    assert np.array_equal(mode_kernel("L_ONLY", kb, kl), kl)
