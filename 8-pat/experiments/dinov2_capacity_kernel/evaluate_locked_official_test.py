#!/usr/bin/env python3
"""Evaluate frozen DCTPR and matched solvers on locked official-test features."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import torch

from evaluate_cub_published_transductive_baselines import evaluate_episode


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b-feature-dirs", type=Path, nargs="+", required=True)
    parser.add_argument("--l-feature-dirs", type=Path, nargs="+", required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--baseline-protocol", type=Path, required=True)
    parser.add_argument("--lock", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--dataset", choices=("cub", "dogs"), required=True)
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()
    protocol = json.loads(args.protocol.read_text())
    baseline_protocol = json.loads(args.baseline_protocol.read_text())
    lock = json.loads(args.lock.read_text())
    if lock.get("status") != "LOCKED_BEFORE_OFFICIAL_TEST_IMAGE_DECODING":
        raise RuntimeError("official-test lock is not sealed")
    if len(args.b_feature_dirs) != len(args.l_feature_dirs):
        raise ValueError("B and L episode counts differ")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    device = torch.device(args.device)
    lambdas = protocol["official_test"]["fixed_laplacian_lambdas_from_cub_train_development"]
    episodes = []
    for episode, (b_dir, l_dir) in enumerate(zip(args.b_feature_dirs, args.l_feature_dirs), start=1):
        episodes.append(evaluate_episode(episode, b_dir, l_dir, baseline_protocol, lambdas, args.output_dir, device))
    overall = {name: float(np.mean([ep["aggregate"][name]["mean"] for ep in episodes])) for name in episodes[0]["aggregate"]}
    published = [name for name in overall if name not in {"BL_NCC"}]
    strongest = max(published, key=overall.get)
    extraction = []
    for b_dir, l_dir in zip(args.b_feature_dirs, args.l_feature_dirs):
        b_metadata = json.loads((b_dir / "metadata.json").read_text())
        l_metadata = json.loads((l_dir / "metadata.json").read_text())
        extraction.append({
            "images": b_metadata["images"],
            "b_seconds": b_metadata["feature_extraction_seconds"],
            "l_seconds": l_metadata["feature_extraction_seconds"],
            "total_seconds": b_metadata["feature_extraction_seconds"] + l_metadata["feature_extraction_seconds"],
            "peak_gpu_memory_bytes": max(b_metadata["peak_gpu_memory_bytes"], l_metadata["peak_gpu_memory_bytes"]),
        })
    result = {
        "experiment_id": protocol["experiment_id"],
        "dataset": args.dataset,
        "episodes": episodes,
        "feature_extraction": extraction,
        "overall_mean": overall,
        "strongest_matched_solver": strongest,
        "dctpr_delta_vs_strongest_pp": 100.0 * (overall["DCTPR"] - overall[strongest]),
        "dctpr_delta_vs_bl_ncc_pp": 100.0 * (overall["DCTPR"] - overall["BL_NCC"]),
        "lock_sha256": sha256(args.lock),
        "protocol_sha256": sha256(args.protocol),
        "baseline_protocol_sha256": sha256(args.baseline_protocol),
        "unique_official_test_images_evaluated": sum(row["images"] for row in extraction),
        "model_image_encodings": 2 * sum(row["images"] for row in extraction),
        "interpretation": "locked official-test evaluation; no test label was used for tuning",
    }
    (args.output_dir / "summary.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
