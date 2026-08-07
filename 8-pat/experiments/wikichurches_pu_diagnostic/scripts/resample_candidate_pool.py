#!/usr/bin/env python3
"""Create fixed Bernoulli resamples from an existing known-q candidate census."""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-pool", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--seeds", type=int, nargs="+", required=True)
    args = parser.parse_args()

    with args.input_pool.open(newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])
    if not rows or "sampling_probability" not in fieldnames:
        raise ValueError("Input pool lacks sampling_probability")
    probabilities = np.asarray(
        [float(row["sampling_probability"]) for row in rows], dtype=float
    )
    if np.any(probabilities <= 0) or np.any(probabilities >= 1):
        raise ValueError("All inclusion probabilities must be in (0, 1)")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_fields = [
        field for field in fieldnames if field not in {"sampled", "sampling_seed"}
    ] + ["sampled", "sampling_seed"]
    audit_lines = [
        f"input={args.input_pool}",
        f"pool_rows={len(rows)}",
        f"expected_sampled={probabilities.sum():.6f}",
        f"q_min={probabilities.min():.9f}",
        f"q_median={np.median(probabilities):.9f}",
        f"q_max={probabilities.max():.9f}",
        "",
    ]
    group_q = defaultdict(float)
    for row, probability in zip(rows, probabilities, strict=True):
        group_q[(row["image_filename"], row["label"])] += float(probability)
    audit_lines.extend(
        [
            f"group_count={len(group_q)}",
            f"group_qsum_min={min(group_q.values()):.9f}",
            f"group_qsum_median={np.median(list(group_q.values())):.9f}",
            f"group_qsum_max={max(group_q.values()):.9f}",
            "",
        ]
    )

    for seed in args.seeds:
        rng = np.random.default_rng(seed)
        sampled = rng.random(len(rows)) < probabilities
        out_path = args.output_dir / f"full_candidate_pool_seed{seed}.csv"
        label_counts: Counter[str] = Counter()
        with out_path.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=output_fields)
            writer.writeheader()
            for row, selected in zip(rows, sampled, strict=True):
                output_row = {
                    field: value
                    for field, value in row.items()
                    if field in output_fields
                }
                output_row["sampled"] = int(selected)
                output_row["sampling_seed"] = seed
                writer.writerow(output_row)
                if selected:
                    label_counts[row["label"]] += 1
        audit_lines.append(
            f"seed={seed} sampled={int(sampled.sum())} "
            f"labels={dict(sorted(label_counts.items()))}"
        )
        print(audit_lines[-1], flush=True)

    (args.output_dir / "resampling_audit.txt").write_text(
        "\n".join(audit_lines) + "\n"
    )


if __name__ == "__main__":
    main()
