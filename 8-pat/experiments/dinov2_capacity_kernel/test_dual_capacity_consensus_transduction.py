import torch

from screen_dual_capacity_consensus_transduction import (
    consensus_assignment,
    sinkhorn,
)


def test_sinkhorn_respects_row_and_column_marginals():
    logits = torch.tensor(
        [[3.0, 1.0], [2.0, 0.0], [0.0, 2.0], [1.0, 3.0]]
    )
    assignment = sinkhorn(logits, examples_per_class=2, iterations=200)
    assert torch.allclose(assignment.sum(dim=1), torch.ones(4), atol=1e-5)
    assert torch.allclose(assignment.sum(dim=0), torch.full((2,), 2.0), atol=1e-5)


def test_identical_capacity_assignments_are_fixed_point_consensus():
    assignment = torch.tensor(
        [[0.8, 0.2], [0.7, 0.3], [0.3, 0.7], [0.2, 0.8]]
    )
    consensus = consensus_assignment(
        assignment, assignment, examples_per_class=2, sinkhorn_iterations=200
    )
    assert torch.allclose(consensus, assignment, atol=1e-5)
