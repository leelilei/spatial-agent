#!/usr/bin/env python3
"""Screen DCCR under the frozen PAT-K-260729-002 protocol."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import torch

from diagnose_1shot_transductive_regime import support_rotations
from screen_dual_capacity_kernel import load_pair


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize(x: torch.Tensor) -> torch.Tensor:
    return x / x.norm(dim=1, keepdim=True).clamp_min(1e-12)


def sinkhorn(
    logits: torch.Tensor, examples_per_class: int, iterations: int
) -> torch.Tensor:
    assignment = torch.exp((logits - logits.max(dim=1, keepdim=True).values).clamp(-60.0, 0.0))
    assignment = assignment + 1e-12
    target = torch.full(
        (logits.shape[1],),
        float(examples_per_class),
        dtype=logits.dtype,
        device=logits.device,
    )
    for _ in range(iterations):
        assignment = assignment / assignment.sum(dim=1, keepdim=True).clamp_min(1e-12)
        assignment = assignment * (
            target / assignment.sum(dim=0).clamp_min(1e-12)
        )
    return assignment / assignment.sum(dim=1, keepdim=True).clamp_min(1e-12)


def balanced_assignment(
    query: torch.Tensor,
    prototypes: torch.Tensor,
    temperature: float,
    examples_per_class: int,
    sinkhorn_iterations: int,
) -> torch.Tensor:
    return sinkhorn(
        (query @ prototypes.T) / temperature,
        examples_per_class,
        sinkhorn_iterations,
    )


def single_view_refinement(
    support: torch.Tensor,
    query: torch.Tensor,
    temperature: float,
    examples_per_class: int,
    sinkhorn_iterations: int,
    refinement_steps: int,
    mix: float,
) -> torch.Tensor:
    prototypes = support.clone()
    for _ in range(refinement_steps):
        assignment = balanced_assignment(
            query,
            prototypes,
            temperature,
            examples_per_class,
            sinkhorn_iterations,
        )
        centres = (assignment.T @ query) / assignment.sum(dim=0)[:, None].clamp_min(1e-12)
        prototypes = normalize((1.0 - mix) * support + mix * centres)
    return balanced_assignment(
        query,
        prototypes,
        temperature,
        examples_per_class,
        sinkhorn_iterations,
    )


def consensus_assignment(
    b_assignment: torch.Tensor,
    l_assignment: torch.Tensor,
    examples_per_class: int,
    sinkhorn_iterations: int,
) -> torch.Tensor:
    log_consensus = 0.5 * (
        b_assignment.clamp_min(1e-12).log()
        + l_assignment.clamp_min(1e-12).log()
    )
    return sinkhorn(log_consensus, examples_per_class, sinkhorn_iterations)


def dual_capacity_consensus_refinement(
    support_b: torch.Tensor,
    support_l: torch.Tensor,
    query_b: torch.Tensor,
    query_l: torch.Tensor,
    temperature: float,
    examples_per_class: int,
    sinkhorn_iterations: int,
    refinement_steps: int,
    mix: float,
) -> torch.Tensor:
    prototypes_b = support_b.clone()
    prototypes_l = support_l.clone()
    for _ in range(refinement_steps):
        assignment_b = balanced_assignment(
            query_b,
            prototypes_b,
            temperature,
            examples_per_class,
            sinkhorn_iterations,
        )
        assignment_l = balanced_assignment(
            query_l,
            prototypes_l,
            temperature,
            examples_per_class,
            sinkhorn_iterations,
        )
        consensus = consensus_assignment(
            assignment_b,
            assignment_l,
            examples_per_class,
            sinkhorn_iterations,
        )
        agreement = 1.0 - 0.5 * torch.abs(
            assignment_b - assignment_l
        ).sum(dim=1)
        weights = consensus * agreement.clamp(0.0, 1.0)[:, None]
        mass = weights.sum(dim=0)[:, None].clamp_min(1e-12)
        centres_b = (weights.T @ query_b) / mass
        centres_l = (weights.T @ query_l) / mass
        prototypes_b = normalize((1.0 - mix) * support_b + mix * centres_b)
        prototypes_l = normalize((1.0 - mix) * support_l + mix * centres_l)
    assignment_b = balanced_assignment(
        query_b,
        prototypes_b,
        temperature,
        examples_per_class,
        sinkhorn_iterations,
    )
    assignment_l = balanced_assignment(
        query_l,
        prototypes_l,
        temperature,
        examples_per_class,
        sinkhorn_iterations,
    )
    return consensus_assignment(
        assignment_b,
        assignment_l,
        examples_per_class,
        sinkhorn_iterations,
    )


def accuracy(labels: np.ndarray, predictions: np.ndarray) -> float:
    return float(np.mean(labels == predictions))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b-feature-dir", type=Path, required=True)
    parser.add_argument("--l-feature-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--device", default="cuda")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    fixed = protocol["fixed_inference"]
    b, l, labels, _folds, image_ids = load_pair(
        args.b_feature_dir, args.l_feature_dir
    )
    device = torch.device(args.device)
    b_tensor = normalize(torch.as_tensor(b, dtype=torch.float32, device=device))
    l_tensor = normalize(torch.as_tensor(l, dtype=torch.float32, device=device))
    bl_tensor = normalize(torch.cat([b_tensor, l_tensor], dim=1))
    tensors = {"B": b_tensor, "L": l_tensor, "BL": bl_tensor}
    rows = []
    saved_predictions: dict[str, list[np.ndarray]] = {}
    for rotation, (support, query) in enumerate(
        support_rotations(labels, image_ids)
    ):
        support_y = labels[support]
        query_y = labels[query]
        examples_per_class = len(query) // len(support)
        predictions: dict[str, np.ndarray] = {}
        for name, features in tensors.items():
            support_x = features[support]
            query_x = features[query]
            similarities = query_x @ support_x.T
            predictions[f"{name}_NCC"] = support_y[
                similarities.argmax(dim=1).cpu().numpy()
            ]
            base_assignment = sinkhorn(
                similarities / fixed["temperature"],
                examples_per_class,
                fixed["sinkhorn_iterations"],
            )
            predictions[f"{name}_SINKHORN"] = support_y[
                base_assignment.argmax(dim=1).cpu().numpy()
            ]
            refined = single_view_refinement(
                support_x,
                query_x,
                fixed["temperature"],
                examples_per_class,
                fixed["sinkhorn_iterations"],
                fixed["refinement_steps"],
                fixed["support_query_mix"],
            )
            predictions[f"{name}_REFINE"] = support_y[
                refined.argmax(dim=1).cpu().numpy()
            ]
        dccr = dual_capacity_consensus_refinement(
            b_tensor[support],
            l_tensor[support],
            b_tensor[query],
            l_tensor[query],
            fixed["temperature"],
            examples_per_class,
            fixed["sinkhorn_iterations"],
            fixed["refinement_steps"],
            fixed["support_query_mix"],
        )
        predictions["DCCR"] = support_y[dccr.argmax(dim=1).cpu().numpy()]
        metrics = {name: accuracy(query_y, pred) for name, pred in predictions.items()}
        rows.append({"rotation": rotation, "metrics": metrics})
        for name, prediction in predictions.items():
            saved_predictions.setdefault(name, []).append(prediction)
        print(json.dumps(rows[-1], sort_keys=True), flush=True)
    method_names = sorted(rows[0]["metrics"])
    aggregate = {
        name: {
            "mean": float(np.mean([row["metrics"][name] for row in rows])),
            "sample_std": float(np.std([row["metrics"][name] for row in rows], ddof=1)),
        }
        for name in method_names
    }
    standard_names = [name for name in method_names if name != "DCCR"]
    strongest = max(standard_names, key=lambda name: aggregate[name]["mean"])
    paired_delta = np.asarray(
        [row["metrics"]["DCCR"] - row["metrics"][strongest] for row in rows]
    )
    gain_pp = 100.0 * (aggregate["DCCR"]["mean"] - aggregate[strongest]["mean"])
    gates = {
        "gain_at_least_1pp": bool(gain_pp >= 1.0 - 1e-12),
        "noninferior_at_least_8_rotations": bool(np.sum(paired_delta >= 0.0) >= 8),
        "worst_rotation_delta_at_least_minus_0_5pp": bool(
            100.0 * paired_delta.min() >= -0.5 - 1e-12
        ),
    }
    summary = {
        "experiment_id": protocol["experiment_id"],
        "aggregate": aggregate,
        "strongest_standard_baseline": strongest,
        "dccr_gain_over_strongest_standard_pp": gain_pp,
        "dccr_noninferior_rotations": int(np.sum(paired_delta >= 0.0)),
        "dccr_worst_rotation_delta_pp": float(100.0 * paired_delta.min()),
        "rotations": rows,
        "gates": gates,
        "screen_success": bool(all(gates.values())),
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        args.output_dir / "predictions.npz",
        labels=labels,
        image_ids=image_ids,
        **{
            f"{name}_rotation_predictions": np.stack(predictions_by_rotation)
            for name, predictions_by_rotation in saved_predictions.items()
        },
    )
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
