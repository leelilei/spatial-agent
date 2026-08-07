#!/usr/bin/env python3
"""Confirm DCTPR on untouched CUB train-only episodes 2 and 3."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import torch

from diagnose_1shot_transductive_regime import support_rotations
from screen_dual_capacity_consensus_transduction import (
    normalize,
    single_view_refinement,
    sinkhorn,
)
from screen_dual_capacity_kernel import load_pair


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b-feature-dirs", type=Path, nargs=2, required=True)
    parser.add_argument("--l-feature-dirs", type=Path, nargs=2, required=True)
    parser.add_argument("--episode-ids", type=int, nargs=2, default=(2, 3))
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--device", default="cuda")
    return parser.parse_args()


def evaluate_episode(
    episode: int,
    b_dir: Path,
    l_dir: Path,
    method: dict,
    device: torch.device,
    output_dir: Path,
) -> dict:
    b, l, labels, _folds, image_ids = load_pair(b_dir, l_dir)
    b_tensor = normalize(torch.as_tensor(b, dtype=torch.float32, device=device))
    l_tensor = normalize(torch.as_tensor(l, dtype=torch.float32, device=device))
    bl_tensor = normalize(torch.cat([b_tensor, l_tensor], dim=1))
    rows = []
    query_indices = []
    query_labels = []
    saved_predictions: dict[str, list[np.ndarray]] = {}
    for rotation, (support, query) in enumerate(
        support_rotations(labels, image_ids)
    ):
        support_y = labels[support]
        query_y = labels[query]
        examples_per_class = len(query) // len(support)
        predictions = {}
        for name, features in {"B": b_tensor, "L": l_tensor}.items():
            refined = single_view_refinement(
                features[support],
                features[query],
                method["temperature"],
                examples_per_class,
                method["sinkhorn_iterations"],
                method["refinement_steps"],
                0.5,
            )
            predictions[f"{name}_REFINE"] = support_y[
                refined.argmax(dim=1).cpu().numpy()
            ]
        bl_similarity = bl_tensor[query] @ bl_tensor[support].T
        predictions["BL_NCC"] = support_y[
            bl_similarity.argmax(dim=1).cpu().numpy()
        ]
        bl_sinkhorn = sinkhorn(
            bl_similarity / method["temperature"],
            examples_per_class,
            method["sinkhorn_iterations"],
        )
        predictions["BL_SINKHORN"] = support_y[
            bl_sinkhorn.argmax(dim=1).cpu().numpy()
        ]
        dctpr = single_view_refinement(
            bl_tensor[support],
            bl_tensor[query],
            method["temperature"],
            examples_per_class,
            method["sinkhorn_iterations"],
            method["refinement_steps"],
            0.5,
        )
        predictions["DCTPR"] = support_y[dctpr.argmax(dim=1).cpu().numpy()]
        metrics = {
            name: float(np.mean(prediction == query_y))
            for name, prediction in predictions.items()
        }
        row = {"rotation": rotation, "metrics": metrics}
        rows.append(row)
        query_indices.append(query)
        query_labels.append(query_y)
        for name, prediction in predictions.items():
            saved_predictions.setdefault(name, []).append(prediction)
        print(json.dumps({"episode": episode, **row}, sort_keys=True), flush=True)
    method_names = sorted(rows[0]["metrics"])
    aggregate = {
        name: {
            "mean": float(np.mean([row["metrics"][name] for row in rows])),
            "sample_std": float(np.std([row["metrics"][name] for row in rows], ddof=1)),
        }
        for name in method_names
    }
    comparators = [name for name in method_names if name != "DCTPR"]
    strongest = max(comparators, key=lambda name: aggregate[name]["mean"])
    np.savez_compressed(
        output_dir / f"episode_{episode}_predictions.npz",
        query_indices=np.stack(query_indices),
        query_labels=np.stack(query_labels),
        **{
            f"{name}_predictions": np.stack(predictions_by_rotation)
            for name, predictions_by_rotation in saved_predictions.items()
        },
    )
    return {
        "episode": episode,
        "aggregate": aggregate,
        "strongest_comparator": strongest,
        "dctpr_gain_over_strongest_pp": 100.0
        * (aggregate["DCTPR"]["mean"] - aggregate[strongest]["mean"]),
        "dctpr_gain_over_bl_ncc_pp": 100.0
        * (aggregate["DCTPR"]["mean"] - aggregate["BL_NCC"]["mean"]),
        "rotations": rows,
    }


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    method = protocol["method"]
    device = torch.device(args.device)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    episodes = [
        evaluate_episode(episode, b_dir, l_dir, method, device, args.output_dir)
        for episode, b_dir, l_dir in zip(
            args.episode_ids, args.b_feature_dirs, args.l_feature_dirs
        )
    ]
    gains = np.asarray(
        [episode["dctpr_gain_over_strongest_pp"] for episode in episodes]
    )
    practical_gains = np.asarray(
        [episode["dctpr_gain_over_bl_ncc_pp"] for episode in episodes]
    )
    gates = {
        "positive_in_each_episode": bool(np.all(gains > 0.0)),
        "mean_gain_at_least_1pp": bool(gains.mean() >= 1.0 - 1e-12),
        "inductive_gain_at_least_5pp_each_episode": bool(
            np.all(practical_gains >= 5.0 - 1e-12)
        ),
    }
    summary = {
        "experiment_id": protocol["experiment_id"],
        "episodes": episodes,
        "mean_dctpr_gain_over_strongest_pp": float(gains.mean()),
        "gates": gates,
        "confirmation_success": bool(all(gates.values())),
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
    }
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
