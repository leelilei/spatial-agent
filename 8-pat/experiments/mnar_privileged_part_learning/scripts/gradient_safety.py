"""Classification-protective auxiliary-gradient projection."""

from __future__ import annotations

from dataclasses import dataclass

import torch


@dataclass
class ProjectionDiagnostics:
    conflict: bool
    cosine_before: float
    dot_before: float
    dot_after: float
    classification_norm: float
    auxiliary_norm: float


def protect_classification_gradient(
    classification_gradients,
    auxiliary_gradients,
    epsilon: float = 1e-12,
):
    """Project a conflicting auxiliary task off the classification gradient."""
    if len(classification_gradients) != len(auxiliary_gradients):
        raise ValueError("Gradient list length mismatch")
    shared = [
        (classification, auxiliary)
        for classification, auxiliary in zip(
            classification_gradients, auxiliary_gradients, strict=True
        )
        if classification is not None and auxiliary is not None
    ]
    if not shared:
        raise RuntimeError("Objectives have no shared trainable parameters")
    dot = sum(
        torch.sum(classification.float() * auxiliary.float())
        for classification, auxiliary in shared
    )
    classification_squared = sum(
        torch.sum(classification.float().square())
        for classification, _ in shared
    )
    auxiliary_squared = sum(
        torch.sum(auxiliary.float().square())
        for _, auxiliary in shared
    )
    conflict = bool(dot.detach().item() < 0 and classification_squared > epsilon)
    coefficient = (
        dot / classification_squared
        if conflict
        else torch.zeros((), device=dot.device)
    )
    protected = []
    for classification, auxiliary in zip(
        classification_gradients, auxiliary_gradients, strict=True
    ):
        if auxiliary is None:
            protected.append(None)
        elif classification is None or not conflict:
            protected.append(auxiliary)
        else:
            protected.append(auxiliary - coefficient * classification)
    dot_after = sum(
        torch.sum(classification.float() * adjusted.float())
        for classification, adjusted in zip(
            classification_gradients, protected, strict=True
        )
        if classification is not None and adjusted is not None
    )
    denominator = (
        classification_squared.sqrt() * auxiliary_squared.sqrt()
    ).clamp_min(epsilon)
    diagnostics = ProjectionDiagnostics(
        conflict=conflict,
        cosine_before=float((dot / denominator).detach()),
        dot_before=float(dot.detach()),
        dot_after=float(dot_after.detach()),
        classification_norm=float(classification_squared.sqrt().detach()),
        auxiliary_norm=float(auxiliary_squared.sqrt().detach()),
    )
    return protected, diagnostics


def assign_combined_gradients(
    parameters, classification_gradients, protected_auxiliary_gradients
) -> None:
    for parameter, classification, auxiliary in zip(
        parameters,
        classification_gradients,
        protected_auxiliary_gradients,
        strict=True,
    ):
        if classification is None and auxiliary is None:
            parameter.grad = None
        elif classification is None:
            parameter.grad = auxiliary.detach()
        elif auxiliary is None:
            parameter.grad = classification.detach()
        else:
            parameter.grad = (classification + auxiliary).detach()
