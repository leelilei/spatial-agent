"""Matched transductive few-shot baselines on frozen feature tensors.

The implementations follow the public TIM, LaplacianShot, and PT-MAP update
rules but accept precomputed DINO features and arbitrary high-way tasks.
"""

from __future__ import annotations

import torch


def l2_normalize(x: torch.Tensor) -> torch.Tensor:
    return x / x.norm(dim=1, keepdim=True).clamp_min(1e-12)


def squared_euclidean(x: torch.Tensor, prototypes: torch.Tensor) -> torch.Tensor:
    distance = (
        x.square().sum(dim=1, keepdim=True)
        + prototypes.square().sum(dim=1).unsqueeze(0)
        - 2.0 * x @ prototypes.T
    )
    return distance.clamp_min(0.0)


def sinkhorn_logits(
    logits: torch.Tensor,
    column_counts: torch.Tensor,
    iterations: int = 100,
) -> torch.Tensor:
    """Return row-normalized assignments with specified class column masses."""
    if not torch.isclose(
        column_counts.sum(),
        torch.tensor(float(len(logits)), device=logits.device),
        atol=1e-4,
    ):
        raise ValueError("column counts must sum to the number of query samples")
    assignment = torch.exp(
        (logits - logits.max(dim=1, keepdim=True).values).clamp(-60.0, 0.0)
    ).clamp_min(1e-12)
    for _ in range(iterations):
        assignment = assignment / assignment.sum(dim=1, keepdim=True).clamp_min(1e-12)
        assignment = assignment * (
            column_counts / assignment.sum(dim=0).clamp_min(1e-12)
        )
    return assignment / assignment.sum(dim=1, keepdim=True).clamp_min(1e-12)


def sinkhorn_cost(
    cost: torch.Tensor,
    column_counts: torch.Tensor,
    regularization: float = 10.0,
    iterations: int = 1000,
) -> torch.Tensor:
    return sinkhorn_logits(-regularization * cost, column_counts, iterations)


def prototype_refinement(
    support: torch.Tensor,
    query: torch.Tensor,
    column_counts: torch.Tensor,
    temperature: float = 0.05,
    sinkhorn_iterations: int = 100,
    refinement_steps: int = 3,
    mix: float = 0.5,
) -> torch.Tensor:
    prototypes = support.clone()
    for _ in range(refinement_steps):
        assignment = sinkhorn_logits(
            (query @ prototypes.T) / temperature,
            column_counts,
            sinkhorn_iterations,
        )
        centres = (assignment.T @ query) / assignment.sum(dim=0)[:, None].clamp_min(1e-12)
        prototypes = l2_normalize((1.0 - mix) * support + mix * centres)
    return sinkhorn_logits(
        (query @ prototypes.T) / temperature,
        column_counts,
        sinkhorn_iterations,
    )


def _class_means(
    support: torch.Tensor, support_labels: torch.Tensor, classes: int
) -> torch.Tensor:
    one_hot = torch.nn.functional.one_hot(support_labels, classes).to(support.dtype)
    return (one_hot.T @ support) / one_hot.sum(dim=0)[:, None].clamp_min(1e-12)


def tim_adm(
    support: torch.Tensor,
    support_labels: torch.Tensor,
    query: torch.Tensor,
    temperature: float = 15.0,
    loss_weights: tuple[float, float, float] = (0.1, 1.0, 0.1),
    iterations: int = 150,
    update_alpha: float = 1.0,
) -> torch.Tensor:
    """TIM-ADM following the official NeurIPS 2020 alternating updates."""
    classes = int(support_labels.max().item()) + 1
    weights = _class_means(support, support_labels, classes)
    y_one_hot = torch.nn.functional.one_hot(support_labels, classes).to(support.dtype)
    n_support = len(support)
    n_query = len(query)
    support_weight, marginal_weight, conditional_weight = loss_weights
    source_scale = support_weight / (1.0 + conditional_weight)
    query_scale = n_support / n_query

    def probabilities(x: torch.Tensor) -> torch.Tensor:
        logits = temperature * (
            x @ weights.T
            - 0.5 * weights.square().sum(dim=1).unsqueeze(0)
            - 0.5 * x.square().sum(dim=1, keepdim=True)
        )
        return logits.softmax(dim=1)

    for _ in range(iterations):
        p_support = probabilities(support)
        p_query = probabilities(query)
        exponent = 1.0 + conditional_weight
        marginal_exponent = marginal_weight / (marginal_weight + 1.0)
        q = p_query.pow(exponent)
        q = q / q.sum(dim=0, keepdim=True).clamp_min(1e-12).pow(marginal_exponent)
        q = q / q.sum(dim=1, keepdim=True).clamp_min(1e-12)

        source_part = source_scale * (y_one_hot.T @ support)
        source_part = source_part + source_scale * (
            weights * p_support.sum(dim=0)[:, None] - p_support.T @ support
        )
        source_norm = source_scale * y_one_hot.sum(dim=0)[:, None]
        query_part = query_scale * (q.T @ query)
        query_part = query_part + query_scale * (
            weights * p_query.sum(dim=0)[:, None] - p_query.T @ query
        )
        query_norm = query_scale * q.sum(dim=0)[:, None]
        new_weights = (source_part + query_part) / (
            source_norm + query_norm
        ).clamp_min(1e-12)
        weights = weights + update_alpha * (new_weights - weights)
    return probabilities(query)


def signed_power(x: torch.Tensor, power: float = 0.5) -> torch.Tensor:
    return x.sign() * x.abs().clamp_min(1e-12).pow(power)


def pt_map(
    support: torch.Tensor,
    support_labels: torch.Tensor,
    query: torch.Tensor,
    column_counts: torch.Tensor,
    use_signed_power: bool,
    power: float = 0.5,
    ot_lambda: float = 10.0,
    map_alpha: float = 0.2,
    iterations: int = 20,
) -> torch.Tensor:
    """PT-MAP family with an explicit signed-power adaptation for DINO CLS."""
    classes = int(support_labels.max().item()) + 1
    if use_signed_power:
        support = signed_power(support, power)
        query = signed_power(query, power)
    support = l2_normalize(support)
    query = l2_normalize(query)
    support = l2_normalize(support - support.mean(dim=0, keepdim=True))
    query = l2_normalize(query - query.mean(dim=0, keepdim=True))
    prototypes = _class_means(support, support_labels, classes)
    support_mask = torch.nn.functional.one_hot(support_labels, classes).to(support.dtype)
    all_features = torch.cat([support, query], dim=0)
    for _ in range(iterations):
        query_assignment = sinkhorn_cost(
            squared_euclidean(query, prototypes),
            column_counts,
            regularization=ot_lambda,
            iterations=1000,
        )
        mask = torch.cat([support_mask, query_assignment], dim=0)
        estimates = (mask.T @ all_features) / mask.sum(dim=0)[:, None].clamp_min(1e-12)
        prototypes = prototypes + map_alpha * (estimates - prototypes)
    return sinkhorn_cost(
        squared_euclidean(query, prototypes),
        column_counts,
        regularization=ot_lambda,
        iterations=1000,
    )


def laplacian_components(
    support: torch.Tensor,
    query: torch.Tensor,
    prototype_rectification: bool,
    knn_argument: int = 3,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Build official-style unary costs and directed non-self kNN edges."""
    support = l2_normalize(support)
    query = l2_normalize(query)
    prototypes = support.clone()
    if prototype_rectification:
        shifted_query = query + (support.mean(dim=0) - query.mean(dim=0))[None, :]
        augmented = torch.cat([support, shifted_query], dim=0)
        similarities = 10.0 * (augmented @ support.T)
        soft_weights = similarities.softmax(dim=1)
        hard = similarities.argmax(dim=1)
        rectified = []
        for class_index in range(len(support)):
            selected = hard == class_index
            if selected.any():
                weights = soft_weights[selected, class_index][:, None]
                rectified.append((weights * augmented[selected]).mean(dim=0))
            else:
                rectified.append(support[class_index])
        prototypes = torch.stack(rectified)
        query = shifted_query
    unary = squared_euclidean(query, prototypes)
    similarities = query @ query.T
    similarities.fill_diagonal_(-torch.inf)
    neighbors = similarities.topk(k=knn_argument - 1, dim=1).indices
    return unary, neighbors


def laplacian_from_components(
    unary: torch.Tensor,
    neighbors: torch.Tensor,
    laplacian_lambda: float,
    bound_iterations: int = 20,
) -> torch.Tensor:
    assignment = (-unary).softmax(dim=1)
    for _ in range(bound_iterations):
        pairwise = assignment[neighbors].sum(dim=1)
        assignment = (-unary + laplacian_lambda * pairwise).softmax(dim=1)
    return assignment

