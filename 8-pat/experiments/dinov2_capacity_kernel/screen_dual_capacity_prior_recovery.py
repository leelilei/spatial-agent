#!/usr/bin/env python3
"""Bounded CUB development screen for Dual-Capacity Prior Recovery (DCPR)."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import torch

from diagnose_1shot_transductive_regime import support_rotations
from evaluate_cub_query_prior_stress import class_counts, metrics, query_subset
from screen_dual_capacity_kernel import load_pair
from transductive_strong_baselines import (
    l2_normalize,
    prototype_refinement,
    sinkhorn_logits,
    tim_adm,
)


REGIMES = ("MILD_3_9", "SEVERE_1_9")
SHRINKAGES = (0.25, 0.50, 0.75, 1.00)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def episode_features(b_dir: Path, l_dir: Path, device: torch.device):
    b, l, labels, _folds, image_ids = load_pair(b_dir, l_dir)
    b = l2_normalize(torch.as_tensor(b, dtype=torch.float32, device=device))
    l = l2_normalize(torch.as_tensor(l, dtype=torch.float32, device=device))
    bl = l2_normalize(torch.cat([b, l], dim=1))
    return b, l, bl, labels, image_ids


def js_reliability(p: torch.Tensor, q: torch.Tensor) -> torch.Tensor:
    """Return per-query B/L agreement in [0, 1] from normalized JSD."""
    midpoint = 0.5 * (p + q)
    kl_p = (p * (p.clamp_min(1e-12).log() - midpoint.clamp_min(1e-12).log())).sum(1)
    kl_q = (q * (q.clamp_min(1e-12).log() - midpoint.clamp_min(1e-12).log())).sum(1)
    return (1.0 - 0.5 * (kl_p + kl_q) / np.log(2.0)).clamp(0.0, 1.0)


def estimate_counts(
    support_b: torch.Tensor,
    query_b: torch.Tensor,
    support_l: torch.Tensor,
    query_l: torch.Tensor,
    temperature: float,
    shrinkage: float,
) -> tuple[torch.Tensor, dict[str, float]]:
    p_b = ((query_b @ support_b.T) / temperature).softmax(1)
    p_l = ((query_l @ support_l.T) / temperature).softmax(1)
    consensus = 0.5 * (p_b + p_l)
    reliability = js_reliability(p_b, p_l)
    classes = support_b.shape[0]
    uniform_row = torch.full_like(consensus, 1.0 / classes)
    reliable_posterior = reliability[:, None] * consensus + (1.0 - reliability[:, None]) * uniform_row
    raw_counts = reliable_posterior.sum(0)
    uniform_counts = torch.full_like(raw_counts, float(len(query_b)) / classes)
    counts = (1.0 - shrinkage) * uniform_counts + shrinkage * raw_counts
    counts = counts.clamp_min(1e-3)
    counts = counts * (float(len(query_b)) / counts.sum())
    diagnostics = {
        "mean_reliability": float(reliability.mean().item()),
        "min_count": float(counts.min().item()),
        "max_count": float(counts.max().item()),
    }
    return counts, diagnostics


def dcpr(
    support_b: torch.Tensor,
    query_b: torch.Tensor,
    support_l: torch.Tensor,
    query_l: torch.Tensor,
    support_bl: torch.Tensor,
    query_bl: torch.Tensor,
    dctpr: dict,
    shrinkage: float,
) -> tuple[torch.Tensor, torch.Tensor, dict[str, float]]:
    counts, diagnostics = estimate_counts(
        support_b, query_b, support_l, query_l,
        dctpr["temperature"], shrinkage,
    )
    assignment = prototype_refinement(
        support_bl, query_bl, counts,
        dctpr["temperature"], dctpr["sinkhorn_iterations"],
        dctpr["refinement_steps"], dctpr["support_query_mix"],
    )
    return assignment, counts, diagnostics


def evaluate_cell(
    episode: int,
    regime: str,
    b: torch.Tensor,
    l: torch.Tensor,
    bl: torch.Tensor,
    labels: np.ndarray,
    image_ids: np.ndarray,
    dctpr_cfg: dict,
    tim_cfg: dict,
) -> dict:
    regime_index = REGIMES.index(regime)
    true_counts_np = class_counts(200, regime, seed=27500 + 100 * episode + regime_index)
    rows = []
    saved: dict[str, list[np.ndarray]] = {}
    count_estimates: dict[str, list[np.ndarray]] = {}
    for rotation, (support, full_query) in enumerate(support_rotations(labels, image_ids)):
        query = query_subset(full_query, labels, image_ids, true_counts_np)
        support_b, query_b = b[support], b[query]
        support_l, query_l = l[support], l[query]
        support_bl, query_bl = bl[support], bl[query]
        support_y = torch.as_tensor(labels[support], dtype=torch.long, device=bl.device)
        query_y = labels[query]
        uniform_counts = torch.full((200,), float(len(query)) / 200, device=bl.device)
        oracle_counts = torch.as_tensor(true_counts_np, dtype=torch.float32, device=bl.device)
        predictions = {
            "BL_NCC": (query_bl @ support_bl.T).argmax(1).cpu().numpy(),
            "DCTPR_UNIFORM": prototype_refinement(
                support_bl, query_bl, uniform_counts,
                dctpr_cfg["temperature"], dctpr_cfg["sinkhorn_iterations"],
                dctpr_cfg["refinement_steps"], dctpr_cfg["support_query_mix"],
            ).argmax(1).cpu().numpy(),
            "DCTPR_ORACLE": prototype_refinement(
                support_bl, query_bl, oracle_counts,
                dctpr_cfg["temperature"], dctpr_cfg["sinkhorn_iterations"],
                dctpr_cfg["refinement_steps"], dctpr_cfg["support_query_mix"],
            ).argmax(1).cpu().numpy(),
            "TIM_ADM": tim_adm(
                support_bl, support_y, query_bl,
                tim_cfg["temperature"], tuple(tim_cfg["loss_weights"]),
                tim_cfg["iterations"], tim_cfg["alpha"],
            ).argmax(1).cpu().numpy(),
        }
        diagnostics = {}
        for shrinkage in SHRINKAGES:
            name = f"DCPR_S{shrinkage:.2f}"
            assignment, estimated_counts, diag = dcpr(
                support_b, query_b, support_l, query_l, support_bl, query_bl,
                dctpr_cfg, shrinkage,
            )
            predictions[name] = assignment.argmax(1).cpu().numpy()
            count_estimates.setdefault(name, []).append(estimated_counts.cpu().numpy())
            diagnostics[name] = {
                **diag,
                "count_mae": float(np.mean(np.abs(estimated_counts.cpu().numpy() - true_counts_np))),
            }
        row_metrics = {name: metrics(query_y, pred) for name, pred in predictions.items()}
        rows.append({"rotation": rotation, "metrics": row_metrics, "diagnostics": diagnostics})
        saved.setdefault("query_indices", []).append(query)
        saved.setdefault("query_labels", []).append(query_y)
        for name, pred in predictions.items():
            saved.setdefault(f"{name}_predictions", []).append(pred)
        print(json.dumps({"episode": episode, "regime": regime, **rows[-1]}, sort_keys=True), flush=True)
    aggregate = {
        name: {
            metric: float(np.mean([row["metrics"][name][metric] for row in rows]))
            for metric in ("micro_accuracy", "macro_balanced_accuracy")
        }
        for name in rows[0]["metrics"]
    }
    return {
        "episode": episode,
        "regime": regime,
        "true_counts": true_counts_np.tolist(),
        "aggregate": aggregate,
        "rotations": rows,
        "saved": {name: np.stack(values) for name, values in saved.items()},
        "estimated_counts": {name: np.stack(values) for name, values in count_estimates.items()},
    }


def mean_cells(cells: list[dict], method: str) -> float:
    return float(np.mean([cell["aggregate"][method]["macro_balanced_accuracy"] for cell in cells]))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b-feature-dirs", type=Path, nargs=3, required=True)
    parser.add_argument("--l-feature-dirs", type=Path, nargs=3, required=True)
    parser.add_argument("--baseline-protocol", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--device", default="cuda")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    baseline = json.loads(args.baseline_protocol.read_text())
    dctpr_cfg = baseline["dctpr"]
    tim_cfg = baseline["published_baselines"]["TIM_ADM"]
    device = torch.device(args.device)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    cells = []
    for episode, b_dir, l_dir in zip((1, 2, 3), args.b_feature_dirs, args.l_feature_dirs):
        b, l, bl, labels, image_ids = episode_features(b_dir, l_dir, device)
        for regime in REGIMES:
            cell = evaluate_cell(episode, regime, b, l, bl, labels, image_ids, dctpr_cfg, tim_cfg)
            np.savez_compressed(
                args.output_dir / f"episode_{episode}_{regime.lower()}_predictions.npz",
                class_counts=np.asarray(cell["true_counts"]),
                **cell.pop("saved"),
                **{f"{name}_counts": value for name, value in cell.pop("estimated_counts").items()},
            )
            cells.append(cell)
    development = [cell for cell in cells if cell["episode"] == 1]
    candidate_names = [f"DCPR_S{x:.2f}" for x in SHRINKAGES]
    selected = max(candidate_names, key=lambda name: (mean_cells(development, name), -float(name[-4:])))
    non_oracle = ("BL_NCC", "DCTPR_UNIFORM", "TIM_ADM")
    strongest_development = max(non_oracle, key=lambda name: mean_cells(development, name))
    development_gain = 100.0 * (mean_cells(development, selected) - mean_cells(development, strongest_development))
    uniform_gap = mean_cells(development, "DCTPR_ORACLE") - mean_cells(development, "DCTPR_UNIFORM")
    closed_gap = mean_cells(development, selected) - mean_cells(development, "DCTPR_UNIFORM")
    closure = float(closed_gap / uniform_gap) if uniform_gap > 0 else 0.0
    development_gates = {
        "gain_at_least_1pp": bool(development_gain >= 1.0 - 1e-12),
        "positive_in_both_regimes": bool(all(
            cell["aggregate"][selected]["macro_balanced_accuracy"]
            > cell["aggregate"][strongest_development]["macro_balanced_accuracy"]
            for cell in development
        )),
        "oracle_gap_closure_at_least_30pct": bool(closure >= 0.30 - 1e-12),
    }
    transfer = [cell for cell in cells if cell["episode"] in (2, 3)]
    strongest_transfer = max(non_oracle, key=lambda name: mean_cells(transfer, name))
    transfer_gain = 100.0 * (mean_cells(transfer, selected) - mean_cells(transfer, strongest_transfer))
    superior_cells = sum(
        cell["aggregate"][selected]["macro_balanced_accuracy"]
        > cell["aggregate"][strongest_transfer]["macro_balanced_accuracy"]
        for cell in transfer
    )
    paired_noninferior = sum(
        row["metrics"][selected]["macro_balanced_accuracy"]
        >= row["metrics"][strongest_transfer]["macro_balanced_accuracy"]
        for cell in transfer for row in cell["rotations"]
    )
    transfer_gates = {
        "gain_at_least_0_5pp": bool(transfer_gain >= 0.5 - 1e-12),
        "superior_in_at_least_3_of_4_cells": bool(superior_cells >= 3),
        "paired_noninferior_at_least_28_of_40": bool(paired_noninferior >= 28),
    }
    summary = {
        "experiment_id": protocol["experiment_id"],
        "selected_method": selected,
        "cells": cells,
        "development": {
            "candidate_means": {name: mean_cells(development, name) for name in candidate_names},
            "strongest_non_oracle": strongest_development,
            "selected_gain_pp": development_gain,
            "oracle_gap_closure_fraction": closure,
            "gates": development_gates,
            "go": bool(all(development_gates.values())),
        },
        "internal_transfer": {
            "strongest_non_oracle": strongest_transfer,
            "selected_gain_pp": transfer_gain,
            "superior_cells": superior_cells,
            "paired_noninferior_rotations": paired_noninferior,
            "gates": transfer_gates,
            "go": bool(all(transfer_gates.values())),
        },
        "advance_to_published_baseline_audit": bool(all(development_gates.values()) and all(transfer_gates.values())),
        "sota_claim_allowed": False,
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
        "baseline_protocol_sha256": sha256(args.baseline_protocol),
    }
    (args.output_dir / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
