#!/usr/bin/env python3
"""Run frozen DCTPR and published baselines on Stanford Dogs episodes."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import torch

from evaluate_cub_published_transductive_baselines import PUBLISHED, evaluate_episode


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b-feature-dirs", type=Path, nargs=3, required=True)
    parser.add_argument("--l-feature-dirs", type=Path, nargs=3, required=True)
    parser.add_argument("--cub-protocol", type=Path, required=True)
    parser.add_argument("--cub-baseline-summary", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--device", default="cuda")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cub_protocol = json.loads(args.cub_protocol.read_text())
    cub_summary = json.loads(args.cub_baseline_summary.read_text())
    protocol = json.loads(args.protocol.read_text())
    lambdas = cub_summary["laplacian_selection"]["selected"]
    args.output_dir.mkdir(parents=True, exist_ok=True)
    device = torch.device(args.device)
    episodes = [
        evaluate_episode(
            episode, b_dir, l_dir, cub_protocol, lambdas, args.output_dir, device
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
    episode_gains = [
        100.0 * (
            episode["aggregate"]["DCTPR"]["mean"]
            - episode["aggregate"]["BL_NCC"]["mean"]
        )
        for episode in episodes
    ]
    paired_positive = sum(
        row["metrics"]["DCTPR"] > row["metrics"]["BL_NCC"]
        for episode in episodes for row in episode["rotations"]
    )
    gates = {
        "dctpr_gain_at_least_3pp_each_episode": bool(
            all(gain >= 3.0 - 1e-12 for gain in episode_gains)
        ),
        "dctpr_within_1pp_of_strongest_published": bool(
            100.0 * (overall["DCTPR"] - overall[strongest]) >= -1.0 - 1e-12
        ),
        "dctpr_positive_all_30_rotations": bool(paired_positive == 30),
    }
    summary = {
        "experiment_id": protocol["experiment_id"],
        "selected_laplacian_lambdas_from_cub": lambdas,
        "episodes": episodes,
        "overall_mean": overall,
        "strongest_published_baseline": strongest,
        "dctpr_episode_gain_over_bl_ncc_pp": episode_gains,
        "dctpr_positive_rotations": paired_positive,
        "gates": gates,
        "paper_level_empirical_route_go": bool(all(gates.values())),
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
        "cub_baseline_summary_sha256": sha256(args.cub_baseline_summary),
    }
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
