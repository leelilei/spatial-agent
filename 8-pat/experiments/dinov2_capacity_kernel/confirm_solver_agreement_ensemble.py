#!/usr/bin/env python3
"""Confirm the frozen SAGE solver-agreement rule on Dogs Episodes 4-6."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import torch

from diagnose_1shot_transductive_regime import support_rotations
from evaluate_cub_published_transductive_baselines import episode_tensors
from transductive_strong_baselines import pt_map, tim_adm


SINGLE_SOLVERS = ("TIM_ADM", "MAP_RAW", "SIGNED_PT_MAP")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b-feature-dirs", type=Path, nargs=3, required=True)
    parser.add_argument("--l-feature-dirs", type=Path, nargs=3, required=True)
    parser.add_argument("--solver-protocol", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--device", default="cuda")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    solver_protocol = json.loads(args.solver_protocol.read_text())
    protocol = json.loads(args.protocol.read_text())
    tim_cfg = solver_protocol["published_baselines"]["TIM_ADM"]
    map_cfg = solver_protocol["published_baselines"]["MAP_RAW"]
    pt_cfg = solver_protocol["published_baselines"]["SIGNED_PT_MAP"]
    device = torch.device(args.device)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    episodes = []
    for episode, b_dir, l_dir in zip((4, 5, 6), args.b_feature_dirs, args.l_feature_dirs):
        features, labels, image_ids = episode_tensors(b_dir, l_dir, device)
        rows = []
        saved_queries, saved_labels = [], []
        saved_predictions: dict[str, list[np.ndarray]] = {}
        agreement_rates = []
        for rotation, (support, query) in enumerate(support_rotations(labels, image_ids)):
            support_x, query_x = features[support], features[query]
            support_y = torch.as_tensor(labels[support], dtype=torch.long, device=device)
            query_y = labels[query]
            counts = torch.full((len(support),), float(len(query) // len(support)), device=device)
            predictions = {
                "TIM_ADM": tim_adm(
                    support_x, support_y, query_x,
                    tim_cfg["temperature"], tuple(tim_cfg["loss_weights"]),
                    tim_cfg["iterations"], tim_cfg["alpha"]
                ).argmax(1).cpu().numpy(),
                "MAP_RAW": pt_map(
                    support_x, support_y, query_x, counts, False, 0.5,
                    map_cfg["ot_lambda"], map_cfg["map_alpha"], map_cfg["iterations"]
                ).argmax(1).cpu().numpy(),
                "SIGNED_PT_MAP": pt_map(
                    support_x, support_y, query_x, counts, True, pt_cfg["power"],
                    pt_cfg["ot_lambda"], pt_cfg["map_alpha"], pt_cfg["iterations"]
                ).argmax(1).cpu().numpy(),
            }
            agree = predictions["TIM_ADM"] == predictions["MAP_RAW"]
            predictions["SAGE"] = np.where(
                agree, predictions["TIM_ADM"], predictions["SIGNED_PT_MAP"]
            )
            agreement_rates.append(float(agree.mean()))
            metrics = {name: float(np.mean(pred == query_y)) for name, pred in predictions.items()}
            rows.append({"rotation": rotation, "metrics": metrics, "tim_map_agreement_rate": agreement_rates[-1]})
            saved_queries.append(query)
            saved_labels.append(query_y)
            for name, pred in predictions.items():
                saved_predictions.setdefault(name, []).append(pred)
            print(json.dumps({"episode": episode, **rows[-1]}, sort_keys=True), flush=True)
        aggregate = {
            name: {
                "mean": float(np.mean([row["metrics"][name] for row in rows])),
                "sample_std": float(np.std([row["metrics"][name] for row in rows], ddof=1)),
            }
            for name in rows[0]["metrics"]
        }
        np.savez_compressed(
            args.output_dir / f"episode_{episode}_predictions.npz",
            query_indices=np.stack(saved_queries),
            query_labels=np.stack(saved_labels),
            **{f"{name}_predictions": np.stack(values) for name, values in saved_predictions.items()},
        )
        episodes.append({
            "episode": episode,
            "aggregate": aggregate,
            "mean_tim_map_agreement_rate": float(np.mean(agreement_rates)),
            "rotations": rows,
        })
    overall = {
        name: float(np.mean([episode["aggregate"][name]["mean"] for episode in episodes]))
        for name in episodes[0]["aggregate"]
    }
    strongest_single = max(SINGLE_SOLVERS, key=lambda name: overall[name])
    episode_superior = sum(
        episode["aggregate"]["SAGE"]["mean"]
        > episode["aggregate"][strongest_single]["mean"]
        for episode in episodes
    )
    paired_noninferior = sum(
        row["metrics"]["SAGE"]
        >= row["metrics"][strongest_single]
        for episode in episodes for row in episode["rotations"]
    )
    gain_pp = 100.0 * (overall["SAGE"] - overall[strongest_single])
    gates = {
        "mean_gain_at_least_0_10pp": bool(gain_pp >= 0.10 - 1e-12),
        "superior_in_at_least_2_episodes": bool(episode_superior >= 2),
        "paired_noninferior_at_least_18_of_30": bool(paired_noninferior >= 18),
    }
    summary = {
        "experiment_id": protocol["experiment_id"],
        "method": "SAGE",
        "rule": protocol["development_evidence"]["selected_rule"],
        "episodes": episodes,
        "overall_mean": overall,
        "strongest_single_solver": strongest_single,
        "sage_gain_over_strongest_single_pp": gain_pp,
        "sage_superior_episode_count": episode_superior,
        "sage_paired_noninferior_rotations": paired_noninferior,
        "gates": gates,
        "matched_protocol_new_best_confirmed": bool(all(gates.values())),
        "global_sota_claim_allowed": False,
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
        "solver_protocol_sha256": sha256(args.solver_protocol),
    }
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
