#!/usr/bin/env python3
"""Pure NumPy utilities for permutation-aware sparse attention calibration."""

from __future__ import annotations

import numpy as np
from scipy.optimize import linear_sum_assignment


def fold_selected_indices(selected, train_indices, total_rows, expected_budget):
    """Validate that a sparse mask contains only allowed fold-training rows."""

    selected = np.asarray(selected, dtype=np.bool_)
    train_indices = np.asarray(train_indices, dtype=np.int64)
    if selected.shape != (total_rows,):
        raise ValueError("selection mask length does not match the manifest")
    allowed = np.zeros(total_rows, dtype=np.bool_)
    allowed[train_indices] = True
    if np.any(selected & ~allowed):
        raise ValueError("selection mask includes outer-fold evaluation rows")
    indices = np.flatnonzero(selected & allowed)
    if len(indices) != expected_budget:
        raise ValueError(
            f"expected {expected_budget} selected rows, got {len(indices)}"
        )
    return indices


def _validate_maps(attention, targets):
    attention = np.asarray(attention, dtype=np.float64)
    targets = np.asarray(targets, dtype=np.float64)
    if attention.ndim != 4 or targets.ndim != 4:
        raise ValueError("attention and targets must be [N,C,H,W]")
    if attention.shape[0] != targets.shape[0]:
        raise ValueError("attention and targets must contain the same images")
    if attention.shape[2:] != targets.shape[2:]:
        raise ValueError("attention and targets must have the same map size")
    if attention.shape[1] < targets.shape[1]:
        raise ValueError("there must be at least one channel per semantic part")
    return attention, targets


def spatial_nll_cost(attention, targets, eps=1e-8):
    """Return semantic-part by attention-channel spatial negative log mass.

    Only images where a semantic target is visible contribute to that part.
    Attention maps may be logits or probabilities; logits are converted with a
    sigmoid before spatial normalization.
    """

    attention, targets = _validate_maps(attention, targets)
    part_count = targets.shape[1]
    channel_count = part_count
    candidate = attention[:, :channel_count]
    if candidate.min() < 0.0 or candidate.max() > 1.0:
        candidate = 1.0 / (1.0 + np.exp(-np.clip(candidate, -40.0, 40.0)))
    candidate = candidate / (
        candidate.sum(axis=(-1, -2), keepdims=True) + eps
    )
    visible = targets.sum(axis=(-1, -2)) > 0
    cost = np.full((part_count, channel_count), 1e6, dtype=np.float64)
    for part in range(part_count):
        rows = np.flatnonzero(visible[:, part])
        if len(rows) == 0:
            continue
        mask = targets[rows, part] > 0
        for channel in range(channel_count):
            mass = (candidate[rows, channel] * mask).sum(axis=(-1, -2))
            cost[part, channel] = float(-np.log(mass + eps).mean())
    return cost


def solve_part_to_channel(cost):
    """Solve one-to-one semantic-part to attention-channel assignment."""

    cost = np.asarray(cost, dtype=np.float64)
    if cost.ndim != 2 or cost.shape[0] != cost.shape[1]:
        raise ValueError("cost must be a square [parts, channels] matrix")
    if not np.isfinite(cost).all():
        raise ValueError("cost contains NaN or infinity")
    parts, channels = linear_sum_assignment(cost)
    mapping = np.full(cost.shape[0], -1, dtype=np.int64)
    mapping[parts] = channels
    validate_mapping(mapping, cost.shape[0])
    return mapping


def validate_mapping(mapping, part_count):
    mapping = np.asarray(mapping, dtype=np.int64)
    if mapping.shape != (part_count,):
        raise ValueError("mapping must contain exactly one channel per part")
    if mapping.min() < 0 or mapping.max() >= part_count:
        raise ValueError("mapping channel is out of range")
    if len(np.unique(mapping)) != part_count:
        raise ValueError("mapping must be one-to-one")
    return mapping


def attention_hit_counts(attention, targets, mapping):
    """Count visible targets whose matched channel argmax hits the target mask."""

    attention, targets = _validate_maps(attention, targets)
    mapping = validate_mapping(mapping, targets.shape[1])
    hits = 0
    visible_count = 0
    width = attention.shape[-1]
    for part, channel in enumerate(mapping):
        visible = targets[:, part].sum(axis=(-1, -2)) > 0
        if not visible.any():
            continue
        flat_argmax = attention[visible, channel].reshape(visible.sum(), -1).argmax(1)
        yy, xx = np.divmod(flat_argmax, width)
        masks = targets[visible, part] > 0
        hits += int(masks[np.arange(len(yy)), yy, xx].sum())
        visible_count += int(visible.sum())
    return hits, visible_count


def derive_mapping(attention, targets):
    """Convenience wrapper used by the runner and unit tests."""

    return solve_part_to_channel(spatial_nll_cost(attention, targets))
