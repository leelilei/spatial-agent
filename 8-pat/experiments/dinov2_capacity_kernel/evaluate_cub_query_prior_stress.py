#!/usr/bin/env python3
"""Evaluate frozen methods under deterministic imbalanced CUB query sets."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import torch

from diagnose_1shot_transductive_regime import support_rotations
from evaluate_cub_published_transductive_baselines import episode_tensors
from transductive_strong_baselines import (
    laplacian_components,
    laplacian_from_components,
    prototype_refinement,
    pt_map,
    tim_adm,
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def class_counts(classes: int, regime: str, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    if regime == "MILD_3_9":
        counts = np.asarray([3] * (classes // 2) + [9] * (classes - classes // 2))
    elif regime == "SEVERE_1_9":
        counts = np.asarray(list(range(1, 10)) * 22 + [5, 5])
        if len(counts) != classes:
            raise ValueError("SEVERE_1_9 schedule requires 200 classes")
    else:
        raise ValueError(regime)
    return counts[rng.permutation(classes)]


def query_subset(
    full_query: np.ndarray,
    labels: np.ndarray,
    image_ids: np.ndarray,
    counts: np.ndarray,
) -> np.ndarray:
    selected = []
    for class_index, count in enumerate(counts):
        candidates = full_query[labels[full_query] == class_index]
        candidates = candidates[np.argsort(image_ids[candidates].astype(str))]
        selected.extend(candidates[: int(count)])
    return np.asarray(selected, dtype=np.int64)


def metrics(labels: np.ndarray, predictions: np.ndarray) -> dict[str, float]:
    classes = np.unique(labels)
    return {
        "micro_accuracy": float(np.mean(labels == predictions)),
        "macro_balanced_accuracy": float(
            np.mean([np.mean(predictions[labels == c] == c) for c in classes])
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b-feature-dirs", type=Path, nargs=3, required=True)
    parser.add_argument("--l-feature-dirs", type=Path, nargs=3, required=True)
    parser.add_argument("--baseline-summary", type=Path, required=True)
    parser.add_argument("--baseline-protocol", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--device", default="cuda")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    stress_protocol = json.loads(args.protocol.read_text())
    baseline_protocol = json.loads(args.baseline_protocol.read_text())
    baseline_summary = json.loads(args.baseline_summary.read_text())
    lambdas = baseline_summary["laplacian_selection"]["selected"]
    dctpr = baseline_protocol["dctpr"]
    tim_cfg = baseline_protocol["published_baselines"]["TIM_ADM"]
    pt_cfg = baseline_protocol["published_baselines"]["SIGNED_PT_MAP"]
    device = torch.device(args.device)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    episode_results = []

    for episode, b_dir, l_dir in zip((1, 2, 3), args.b_feature_dirs, args.l_feature_dirs):
        features, labels, image_ids = episode_tensors(b_dir, l_dir, device)
        for regime_index, regime in enumerate(("MILD_3_9", "SEVERE_1_9")):
            counts_np = class_counts(200, regime, seed=27500 + 100 * episode + regime_index)
            rows = []
            saved_indices = []
            saved_labels = []
            saved_predictions: dict[str, list[np.ndarray]] = {}
            for rotation, (support, full_query) in enumerate(
                support_rotations(labels, image_ids)
            ):
                query = query_subset(full_query, labels, image_ids, counts_np)
                support_x, query_x = features[support], features[query]
                support_y = torch.as_tensor(labels[support], dtype=torch.long, device=device)
                query_y = labels[query]
                oracle_counts = torch.as_tensor(counts_np, dtype=torch.float32, device=device)
                uniform_counts = torch.full(
                    (200,), float(len(query) / 200), dtype=torch.float32, device=device
                )
                predictions = {
                    "BL_NCC": (query_x @ support_x.T).argmax(1).cpu().numpy(),
                    "DCTPR_UNIFORM": prototype_refinement(
                        support_x, query_x, uniform_counts,
                        dctpr["temperature"], dctpr["sinkhorn_iterations"],
                        dctpr["refinement_steps"], dctpr["support_query_mix"]
                    ).argmax(1).cpu().numpy(),
                    "DCTPR_ORACLE": prototype_refinement(
                        support_x, query_x, oracle_counts,
                        dctpr["temperature"], dctpr["sinkhorn_iterations"],
                        dctpr["refinement_steps"], dctpr["support_query_mix"]
                    ).argmax(1).cpu().numpy(),
                    "TIM_ADM": tim_adm(
                        support_x, support_y, query_x,
                        tim_cfg["temperature"], tuple(tim_cfg["loss_weights"]),
                        tim_cfg["iterations"], tim_cfg["alpha"]
                    ).argmax(1).cpu().numpy(),
                    "SIGNED_PT_MAP_UNIFORM": pt_map(
                        support_x, support_y, query_x, uniform_counts, True,
                        pt_cfg["power"], pt_cfg["ot_lambda"],
                        pt_cfg["map_alpha"], pt_cfg["iterations"]
                    ).argmax(1).cpu().numpy(),
                    "SIGNED_PT_MAP_ORACLE": pt_map(
                        support_x, support_y, query_x, oracle_counts, True,
                        pt_cfg["power"], pt_cfg["ot_lambda"],
                        pt_cfg["map_alpha"], pt_cfg["iterations"]
                    ).argmax(1).cpu().numpy(),
                }
                for name, rectified, key in (
                    ("LAPLACIANSHOT", False, "L2N"),
                    ("LAPLACIANSHOT_PR", True, "PROTO_RECT"),
                ):
                    unary, neighbors = laplacian_components(support_x, query_x, rectified, 3)
                    predictions[name] = laplacian_from_components(
                        unary, neighbors, lambdas[key], 20
                    ).argmax(1).cpu().numpy()
                row_metrics = {name: metrics(query_y, pred) for name, pred in predictions.items()}
                rows.append({"rotation": rotation, "metrics": row_metrics})
                saved_indices.append(query)
                saved_labels.append(query_y)
                for name, pred in predictions.items():
                    saved_predictions.setdefault(name, []).append(pred)
                print(json.dumps({"episode": episode, "regime": regime, **rows[-1]}, sort_keys=True))
            aggregate = {
                name: {
                    metric: float(np.mean([row["metrics"][name][metric] for row in rows]))
                    for metric in ("micro_accuracy", "macro_balanced_accuracy")
                }
                for name in rows[0]["metrics"]
            }
            np.savez_compressed(
                args.output_dir / f"episode_{episode}_{regime.lower()}_predictions.npz",
                query_indices=np.stack(saved_indices),
                query_labels=np.stack(saved_labels),
                class_counts=counts_np,
                **{f"{name}_predictions": np.stack(values) for name, values in saved_predictions.items()},
            )
            episode_results.append({
                "episode": episode,
                "regime": regime,
                "class_count_min": int(counts_np.min()),
                "class_count_max": int(counts_np.max()),
                "aggregate": aggregate,
                "uniform_oracle_gap_pp": {
                    "DCTPR": 100.0 * (
                        aggregate["DCTPR_ORACLE"]["macro_balanced_accuracy"]
                        - aggregate["DCTPR_UNIFORM"]["macro_balanced_accuracy"]
                    ),
                    "SIGNED_PT_MAP": 100.0 * (
                        aggregate["SIGNED_PT_MAP_ORACLE"]["macro_balanced_accuracy"]
                        - aggregate["SIGNED_PT_MAP_UNIFORM"]["macro_balanced_accuracy"]
                    ),
                },
                "rotations": rows,
            })
    summary = {
        "experiment_id": stress_protocol["experiment_id"],
        "selected_laplacian_lambdas": lambdas,
        "results": episode_results,
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
        "baseline_summary_sha256": sha256(args.baseline_summary),
    }
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
