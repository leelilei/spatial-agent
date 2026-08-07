"""Shared frozen-feature heads and training utilities for PAT-C-260728-001."""

from __future__ import annotations

import copy
import random
from dataclasses import dataclass

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import balanced_accuracy_score, recall_score


class GlobalHead(nn.Module):
    def __init__(self, global_dim: int, classes: int):
        super().__init__()
        self.classifier = nn.Linear(global_dim, classes)

    def forward(self, global_features: torch.Tensor, patch_features=None):
        logits = self.classifier(global_features)
        return logits, None


class PrivilegedPartHead(nn.Module):
    def __init__(
        self,
        global_dim: int,
        patch_dim: int,
        classes: int,
        parts: int = 4,
    ):
        super().__init__()
        self.parts = parts
        self.global_classifier = nn.Linear(global_dim, classes)
        self.part_attention = nn.Linear(patch_dim, parts)
        self.local_classifier = nn.Linear(parts * patch_dim, classes)

    def forward(
        self, global_features: torch.Tensor, patch_features: torch.Tensor
    ):
        global_logits = self.global_classifier(global_features)
        attention_logits = self.part_attention(patch_features).transpose(1, 2)
        attention = attention_logits.softmax(dim=-1)
        pooled = torch.einsum("bkp,bpd->bkd", attention, patch_features)
        local_logits = self.local_classifier(pooled.flatten(1))
        return global_logits, local_logits, attention_logits


def part_segmentation_loss(
    attention_logits: torch.Tensor, targets: torch.Tensor
) -> torch.Tensor:
    flat_targets = targets.flatten(2)
    bce = F.binary_cross_entropy_with_logits(attention_logits, flat_targets)
    probability = attention_logits.sigmoid()
    intersection = (probability * flat_targets).sum(dim=-1)
    denominator = probability.sum(dim=-1) + flat_targets.sum(dim=-1)
    dice = 1.0 - ((2.0 * intersection + 1.0) / (denominator + 1.0))
    return bce + dice.mean()


def set_deterministic(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def class_balanced_weights(labels: torch.Tensor, classes: int) -> torch.Tensor:
    counts = torch.bincount(labels, minlength=classes).float().clamp_min(1)
    weights = counts.sum() / (classes * counts)
    return weights.to(labels.device)


@dataclass
class FitResult:
    best_epoch: int
    best_balanced_accuracy: float
    predictions: np.ndarray
    labels: np.ndarray
    state_dict: dict


def fit_head(
    global_features: torch.Tensor,
    patch_features: torch.Tensor,
    targets: torch.Tensor,
    labels: torch.Tensor,
    train_indices: np.ndarray,
    eval_indices: np.ndarray,
    classes: int,
    learning_rate: float,
    weight_decay: float,
    maximum_epochs: int,
    patience: int,
    batch_size: int,
    seed: int,
    part_loss_weight: float = 0.0,
    gamma: float = 0.0,
) -> FitResult:
    set_deterministic(seed)
    use_parts = part_loss_weight > 0.0
    if use_parts:
        model: nn.Module = PrivilegedPartHead(
            global_features.shape[1], patch_features.shape[2], classes
        )
    else:
        model = GlobalHead(global_features.shape[1], classes)
    model.cuda()
    optimizer = torch.optim.AdamW(
        model.parameters(), lr=learning_rate, weight_decay=weight_decay
    )
    device = global_features.device
    train_index_tensor = torch.as_tensor(
        train_indices, dtype=torch.long, device=device
    )
    label_weights = class_balanced_weights(
        labels[train_index_tensor], classes
    )
    generator = torch.Generator(device=device).manual_seed(seed)

    best_metric = -float("inf")
    best_epoch = 0
    best_state = None
    stale = 0
    for epoch in range(1, maximum_epochs + 1):
        model.train()
        permutation = train_index_tensor[
            torch.randperm(
                len(train_index_tensor), generator=generator, device=device
            )
        ]
        for batch_indices in permutation.split(batch_size):
            global_batch = global_features[batch_indices]
            label_batch = labels[batch_indices]
            patch_batch = patch_features[batch_indices] if use_parts else None
            target_batch = targets[batch_indices] if use_parts else None
            optimizer.zero_grad(set_to_none=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                output = model(global_batch, patch_batch)
                if use_parts:
                    global_logits, local_logits, attention_logits = output
                    logits = global_logits + gamma * local_logits
                    loss = F.cross_entropy(
                        logits.float(), label_batch, weight=label_weights
                    )
                    loss = loss + part_loss_weight * part_segmentation_loss(
                        attention_logits.float(), target_batch.float()
                    )
                else:
                    logits, _ = output
                    loss = F.cross_entropy(
                        logits.float(), label_batch, weight=label_weights
                    )
            loss.backward()
            optimizer.step()

        predictions, eval_labels = predict_head(
            model,
            global_features,
            patch_features,
            labels,
            eval_indices,
            batch_size=batch_size,
            gamma=gamma,
        )
        metric = balanced_accuracy_score(eval_labels, predictions)
        if metric > best_metric + 1e-8:
            best_metric = float(metric)
            best_epoch = epoch
            best_state = copy.deepcopy(model.state_dict())
            stale = 0
        else:
            stale += 1
            if stale >= patience:
                break

    if best_state is None:
        raise RuntimeError("No model checkpoint was produced.")
    model.load_state_dict(best_state)
    predictions, eval_labels = predict_head(
        model,
        global_features,
        patch_features,
        labels,
        eval_indices,
        batch_size=batch_size,
        gamma=gamma,
    )
    return FitResult(
        best_epoch=best_epoch,
        best_balanced_accuracy=best_metric,
        predictions=predictions,
        labels=eval_labels,
        state_dict=best_state,
    )


def predict_head(
    model: nn.Module,
    global_features: torch.Tensor,
    patch_features: torch.Tensor,
    labels: torch.Tensor,
    indices: np.ndarray,
    batch_size: int,
    gamma: float,
) -> tuple[np.ndarray, np.ndarray]:
    model.eval()
    predictions = []
    actual = []
    with torch.inference_mode():
        for start in range(0, len(indices), batch_size):
            batch_indices = torch.as_tensor(
                indices[start : start + batch_size],
                dtype=torch.long,
                device=global_features.device,
            )
            global_batch = global_features[batch_indices]
            if isinstance(model, GlobalHead):
                patch_batch = None
            else:
                patch_batch = patch_features[batch_indices]
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                output = model(global_batch, patch_batch)
                if len(output) == 3:
                    global_logits, local_logits, _ = output
                    logits = global_logits + gamma * local_logits
                else:
                    logits, _ = output
            predictions.append(logits.argmax(dim=1).cpu().numpy())
            actual.append(labels[batch_indices].detach().cpu().numpy())
    return np.concatenate(predictions), np.concatenate(actual)


def fit_fixed_head(
    global_features: torch.Tensor,
    patch_features: torch.Tensor,
    targets: torch.Tensor,
    labels: torch.Tensor,
    classes: int,
    learning_rate: float,
    weight_decay: float,
    epochs: int,
    batch_size: int,
    seed: int,
    part_loss_weight: float = 0.0,
    gamma: float = 0.0,
) -> nn.Module:
    """Fit on all supplied training rows for a pre-selected epoch count."""
    set_deterministic(seed)
    use_parts = part_loss_weight > 0.0
    if use_parts:
        model: nn.Module = PrivilegedPartHead(
            global_features.shape[1], patch_features.shape[2], classes
        )
    else:
        model = GlobalHead(global_features.shape[1], classes)
    model.cuda()
    optimizer = torch.optim.AdamW(
        model.parameters(), lr=learning_rate, weight_decay=weight_decay
    )
    label_weights = class_balanced_weights(labels, classes)
    device = global_features.device
    all_indices = torch.arange(len(labels), dtype=torch.long, device=device)
    generator = torch.Generator(device=device).manual_seed(seed)
    for _ in range(epochs):
        model.train()
        permutation = all_indices[
            torch.randperm(len(all_indices), generator=generator, device=device)
        ]
        for batch_indices in permutation.split(batch_size):
            global_batch = global_features[batch_indices]
            label_batch = labels[batch_indices]
            patch_batch = patch_features[batch_indices] if use_parts else None
            target_batch = targets[batch_indices] if use_parts else None
            optimizer.zero_grad(set_to_none=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                output = model(global_batch, patch_batch)
                if use_parts:
                    global_logits, local_logits, attention_logits = output
                    logits = global_logits + gamma * local_logits
                    loss = F.cross_entropy(
                        logits.float(), label_batch, weight=label_weights
                    )
                    loss = loss + part_loss_weight * part_segmentation_loss(
                        attention_logits.float(), target_batch.float()
                    )
                else:
                    logits, _ = output
                    loss = F.cross_entropy(
                        logits.float(), label_batch, weight=label_weights
                    )
            loss.backward()
            optimizer.step()
    return model


def per_class_recall(
    labels: np.ndarray, predictions: np.ndarray, classes: int
) -> np.ndarray:
    return recall_score(
        labels,
        predictions,
        labels=np.arange(classes),
        average=None,
        zero_division=0,
    )
