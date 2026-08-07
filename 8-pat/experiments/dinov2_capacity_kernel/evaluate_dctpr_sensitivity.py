#!/usr/bin/env python3
"""One-factor sensitivity of frozen DCTPR on train-only episodes."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import torch

from diagnose_1shot_transductive_regime import support_rotations
from screen_dual_capacity_kernel import load_pair
from transductive_strong_baselines import l2_normalize, prototype_refinement


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b-feature-dirs", type=Path, nargs="+", required=True)
    parser.add_argument("--l-feature-dirs", type=Path, nargs="+", required=True)
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()
    if len(args.b_feature_dirs) != len(args.l_feature_dirs):
        raise ValueError("B and L episode counts differ")
    device = torch.device(args.device)
    configs = []
    for value in [1, 2, 3, 5]:
        configs.append({"factor": "refinement_steps", "value": value, "steps": value, "mix": 0.5, "temperature": 0.05})
    for value in [0.25, 0.5, 0.75, 1.0]:
        configs.append({"factor": "support_query_mix", "value": value, "steps": 3, "mix": value, "temperature": 0.05})
    for value in [0.025, 0.05, 0.1]:
        configs.append({"factor": "temperature", "value": value, "steps": 3, "mix": 0.5, "temperature": value})
    rows = []
    for config in configs:
        episode_means = []
        for b_dir, l_dir in zip(args.b_feature_dirs, args.l_feature_dirs):
            b, l, labels, _folds, image_ids = load_pair(b_dir, l_dir)
            features = l2_normalize(torch.cat([l2_normalize(torch.as_tensor(b, dtype=torch.float32, device=device)), l2_normalize(torch.as_tensor(l, dtype=torch.float32, device=device))], dim=1))
            scores = []
            for support, query in support_rotations(labels, image_ids):
                support_x, query_x = features[support], features[query]
                counts = torch.full((len(support),), float(len(query) // len(support)), device=device)
                assignment = prototype_refinement(support_x, query_x, counts, config["temperature"], 100, config["steps"], config["mix"])
                scores.append(float(np.mean(labels[query] == labels[support][assignment.argmax(1).cpu().numpy()])))
            episode_means.append(float(np.mean(scores)))
        rows.append({"dataset": args.dataset, **config, "episode_means": episode_means, "overall_mean": float(np.mean(episode_means)), "overall_std": float(np.std(episode_means, ddof=1))})
    args.output_dir.mkdir(parents=True, exist_ok=True)
    result = {"dataset": args.dataset, "reference": {"steps": 3, "mix": 0.5, "temperature": 0.05}, "rows": rows, "episodes_are_shared_image_rotations": True}
    (args.output_dir / "summary.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    with (args.output_dir / "summary.csv").open("w") as handle:
        handle.write("dataset,factor,value,overall_mean,overall_std,episode_means\n")
        for row in rows:
            handle.write(f"{row['dataset']},{row['factor']},{row['value']},{row['overall_mean']:.8f},{row['overall_std']:.8f},\"{row['episode_means']}\"\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
