#!/usr/bin/env python3
"""Evaluate matched TIM, LaplacianShot, and PT-MAP baselines on CUB."""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import torch

from diagnose_1shot_transductive_regime import support_rotations
from screen_dual_capacity_kernel import load_pair
from transductive_strong_baselines import (
    l2_normalize,
    laplacian_components,
    laplacian_from_components,
    prototype_refinement,
    pt_map,
    sinkhorn_logits,
    tim_adm,
)


PUBLISHED = (
    "TIM_ADM",
    "MAP_RAW",
    "SIGNED_PT_MAP",
    "LAPLACIANSHOT",
    "LAPLACIANSHOT_PR",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def accuracy(labels: np.ndarray, prediction: np.ndarray) -> float:
    return float(np.mean(labels == prediction))


def timed(device: torch.device, function):
    if device.type == "cuda":
        torch.cuda.synchronize(device)
    start = time.perf_counter()
    result = function()
    if device.type == "cuda":
        torch.cuda.synchronize(device)
    return result, time.perf_counter() - start


def episode_tensors(b_dir: Path, l_dir: Path, device: torch.device):
    b, l, labels, _folds, image_ids = load_pair(b_dir, l_dir)
    b_tensor = l2_normalize(torch.as_tensor(b, dtype=torch.float32, device=device))
    l_tensor = l2_normalize(torch.as_tensor(l, dtype=torch.float32, device=device))
    bl = l2_normalize(torch.cat([b_tensor, l_tensor], dim=1))
    return bl, labels, image_ids


def tune_laplacian(
    features: torch.Tensor,
    labels: np.ndarray,
    image_ids: np.ndarray,
    candidates: list[float],
) -> dict:
    metrics = {"L2N": {str(value): [] for value in candidates},
               "PROTO_RECT": {str(value): [] for value in candidates}}
    for support, query in support_rotations(labels, image_ids):
        support_x, query_x = features[support], features[query]
        query_y = labels[query]
        components = {
            "L2N": laplacian_components(support_x, query_x, False, 3),
            "PROTO_RECT": laplacian_components(support_x, query_x, True, 3),
        }
        for variant, (unary, neighbors) in components.items():
            for candidate in candidates:
                prediction = laplacian_from_components(
                    unary, neighbors, candidate, 20
                ).argmax(dim=1).cpu().numpy()
                metrics[variant][str(candidate)].append(accuracy(query_y, prediction))
    means = {
        variant: {value: float(np.mean(scores)) for value, scores in grid.items()}
        for variant, grid in metrics.items()
    }
    selected = {
        variant: float(max(grid, key=lambda value: (grid[value], -float(value))))
        for variant, grid in means.items()
    }
    return {"candidate_rotation_metrics": metrics, "candidate_means": means, "selected": selected}


def evaluate_episode(
    episode: int,
    b_dir: Path,
    l_dir: Path,
    protocol: dict,
    laplacian_lambdas: dict[str, float],
    output_dir: Path,
    device: torch.device,
) -> dict:
    features, labels, image_ids = episode_tensors(b_dir, l_dir, device)
    dctpr = protocol["dctpr"]
    tim_cfg = protocol["published_baselines"]["TIM_ADM"]
    map_cfg = protocol["published_baselines"]["MAP_RAW"]
    pt_cfg = protocol["published_baselines"]["SIGNED_PT_MAP"]
    rows = []
    saved_queries = []
    saved_labels = []
    saved_predictions: dict[str, list[np.ndarray]] = {}
    runtime: dict[str, list[float]] = {}

    for rotation, (support, query) in enumerate(
        support_rotations(labels, image_ids)
    ):
        support_x, query_x = features[support], features[query]
        support_y = torch.as_tensor(labels[support], dtype=torch.long, device=device)
        query_y = labels[query]
        classes = len(support)
        column_counts = torch.full(
            (classes,), float(len(query) // classes), device=device
        )
        predictions = {}

        similarity = query_x @ support_x.T
        predictions["BL_NCC"] = similarity.argmax(1).cpu().numpy()

        assignment, elapsed = timed(
            device,
            lambda: sinkhorn_logits(
                similarity / dctpr["temperature"],
                column_counts,
                dctpr["sinkhorn_iterations"],
            ),
        )
        predictions["BL_SINKHORN"] = assignment.argmax(1).cpu().numpy()
        runtime.setdefault("BL_SINKHORN", []).append(elapsed)

        assignment, elapsed = timed(
            device,
            lambda: prototype_refinement(
                support_x,
                query_x,
                column_counts,
                dctpr["temperature"],
                dctpr["sinkhorn_iterations"],
                dctpr["refinement_steps"],
                dctpr["support_query_mix"],
            ),
        )
        predictions["DCTPR"] = assignment.argmax(1).cpu().numpy()
        runtime.setdefault("DCTPR", []).append(elapsed)

        assignment, elapsed = timed(
            device,
            lambda: tim_adm(
                support_x,
                support_y,
                query_x,
                tim_cfg["temperature"],
                tuple(tim_cfg["loss_weights"]),
                tim_cfg["iterations"],
                tim_cfg["alpha"],
            ),
        )
        predictions["TIM_ADM"] = assignment.argmax(1).cpu().numpy()
        runtime.setdefault("TIM_ADM", []).append(elapsed)

        for name, use_power, cfg in (
            ("MAP_RAW", False, map_cfg),
            ("SIGNED_PT_MAP", True, pt_cfg),
        ):
            assignment, elapsed = timed(
                device,
                lambda use_power=use_power, cfg=cfg: pt_map(
                    support_x,
                    support_y,
                    query_x,
                    column_counts,
                    use_power,
                    cfg.get("power", 0.5),
                    cfg["ot_lambda"],
                    cfg["map_alpha"],
                    cfg["iterations"],
                ),
            )
            predictions[name] = assignment.argmax(1).cpu().numpy()
            runtime.setdefault(name, []).append(elapsed)

        for name, rectified, lambda_key in (
            ("LAPLACIANSHOT", False, "L2N"),
            ("LAPLACIANSHOT_PR", True, "PROTO_RECT"),
        ):
            def run_laplacian(rectified=rectified, lambda_key=lambda_key):
                unary, neighbors = laplacian_components(
                    support_x, query_x, rectified, 3
                )
                return laplacian_from_components(
                    unary, neighbors, laplacian_lambdas[lambda_key], 20
                )
            assignment, elapsed = timed(device, run_laplacian)
            predictions[name] = assignment.argmax(1).cpu().numpy()
            runtime.setdefault(name, []).append(elapsed)

        metrics = {name: accuracy(query_y, pred) for name, pred in predictions.items()}
        row = {"rotation": rotation, "metrics": metrics}
        rows.append(row)
        saved_queries.append(query)
        saved_labels.append(query_y)
        for name, prediction in predictions.items():
            saved_predictions.setdefault(name, []).append(prediction)
        print(json.dumps({"episode": episode, **row}, sort_keys=True), flush=True)

    aggregate = {
        name: {
            "mean": float(np.mean([row["metrics"][name] for row in rows])),
            "sample_std": float(np.std([row["metrics"][name] for row in rows], ddof=1)),
            "mean_runtime_seconds": float(np.mean(runtime.get(name, [0.0]))),
        }
        for name in sorted(rows[0]["metrics"])
    }
    np.savez_compressed(
        output_dir / f"episode_{episode}_predictions.npz",
        query_indices=np.stack(saved_queries),
        query_labels=np.stack(saved_labels),
        **{
            f"{name}_predictions": np.stack(values)
            for name, values in saved_predictions.items()
        },
    )
    return {"episode": episode, "aggregate": aggregate, "rotations": rows}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b-feature-dirs", type=Path, nargs=3, required=True)
    parser.add_argument("--l-feature-dirs", type=Path, nargs=3, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--device", default="cuda")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    device = torch.device(args.device)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    episode1_features, episode1_labels, episode1_ids = episode_tensors(
        args.b_feature_dirs[0], args.l_feature_dirs[0], device
    )
    candidates = protocol["published_baselines"]["LAPLACIANSHOT"][
        "lambda_candidates_episode_1_only"
    ]
    laplacian_selection = tune_laplacian(
        episode1_features, episode1_labels, episode1_ids, candidates
    )
    print(json.dumps({"laplacian_selection": laplacian_selection["selected"]}, sort_keys=True))

    episodes = [
        evaluate_episode(
            episode,
            b_dir,
            l_dir,
            protocol,
            laplacian_selection["selected"],
            args.output_dir,
            device,
        )
        for episode, b_dir, l_dir in zip(
            (1, 2, 3), args.b_feature_dirs, args.l_feature_dirs
        )
    ]
    overall = {
        name: float(np.mean([episode["aggregate"][name]["mean"] for episode in episodes]))
        for name in episodes[0]["aggregate"]
    }
    strongest = max(PUBLISHED, key=lambda name: overall[name])
    dctpr_delta = 100.0 * (overall["DCTPR"] - overall[strongest])
    beaten = [name for name in PUBLISHED if overall["DCTPR"] > overall[name]]
    gates = {
        "dctpr_within_1pp_of_strongest_published": bool(dctpr_delta >= -1.0 - 1e-12),
        "dctpr_beats_at_least_two_published_families": bool(len(beaten) >= 2),
    }
    summary = {
        "experiment_id": protocol["experiment_id"],
        "laplacian_selection": laplacian_selection,
        "episodes": episodes,
        "overall_mean": overall,
        "strongest_published_baseline": strongest,
        "dctpr_delta_vs_strongest_published_pp": dctpr_delta,
        "published_baselines_beaten_by_dctpr": beaten,
        "gates": gates,
        "paper_route_gate_passed": bool(all(gates.values())),
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
    }
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
