import numpy as np
import torch

from screen_dual_capacity_prior_recovery import estimate_counts, js_reliability


def test_js_reliability_is_one_for_identical_posteriors():
    p = torch.tensor([[0.7, 0.3], [0.2, 0.8]], dtype=torch.float32)
    assert torch.allclose(js_reliability(p, p), torch.ones(2), atol=1e-6)


def test_estimated_counts_are_positive_and_conserve_mass():
    support = torch.eye(3)
    query = torch.tensor([[1.0, 0.0, 0.0], [0.9, 0.1, 0.0], [0.0, 1.0, 0.0]])
    counts, diagnostics = estimate_counts(support, query, support, query, 0.05, 1.0)
    assert torch.all(counts > 0)
    assert np.isclose(float(counts.sum()), len(query), atol=1e-6)
    assert diagnostics["max_count"] > diagnostics["min_count"]


def test_zero_shrinkage_limit_is_uniform():
    support = torch.eye(2)
    query = torch.tensor([[1.0, 0.0], [1.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
    counts, _ = estimate_counts(support, query, support, query, 0.05, 0.0)
    assert torch.allclose(counts, torch.tensor([2.0, 2.0]), atol=1e-6)
