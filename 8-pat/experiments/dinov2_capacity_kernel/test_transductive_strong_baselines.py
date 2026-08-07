import torch

from transductive_strong_baselines import (
    laplacian_components,
    laplacian_from_components,
    prototype_refinement,
    pt_map,
    signed_power,
    sinkhorn_logits,
    tim_adm,
)


def _toy_task():
    support = torch.tensor([[1.0, 0.0], [-1.0, 0.0]])
    labels = torch.tensor([0, 1])
    query = torch.tensor([[0.9, 0.1], [0.8, -0.1], [-0.9, 0.1], [-0.8, -0.1]])
    counts = torch.tensor([2.0, 2.0])
    truth = torch.tensor([0, 0, 1, 1])
    return support, labels, query, counts, truth


def test_sinkhorn_matches_requested_marginals():
    logits = torch.tensor([[2.0, 0.0], [1.0, 0.0], [0.0, 1.0], [0.0, 2.0]])
    result = sinkhorn_logits(logits, torch.tensor([2.0, 2.0]), iterations=200)
    assert torch.allclose(result.sum(0), torch.tensor([2.0, 2.0]), atol=1e-5)
    assert torch.allclose(result.sum(1), torch.ones(4), atol=1e-5)


def test_signed_power_preserves_sign():
    values = torch.tensor([[-4.0, -1.0, 0.0, 1.0, 4.0]])
    transformed = signed_power(values, 0.5)
    assert torch.allclose(transformed, torch.tensor([[-2.0, -1.0, 0.0, 1.0, 2.0]]), atol=1e-5)


def test_all_transductive_methods_solve_separated_toy_task():
    support, labels, query, counts, truth = _toy_task()
    dctpr = prototype_refinement(support, query, counts).argmax(1)
    tim = tim_adm(support, labels, query, iterations=20).argmax(1)
    pt = pt_map(support, labels, query, counts, use_signed_power=True).argmax(1)
    unary, neighbors = laplacian_components(support, query, False)
    lap = laplacian_from_components(unary, neighbors, 0.5).argmax(1)
    assert torch.equal(dctpr, truth)
    assert torch.equal(tim, truth)
    assert torch.equal(pt, truth)
    assert torch.equal(lap, truth)
