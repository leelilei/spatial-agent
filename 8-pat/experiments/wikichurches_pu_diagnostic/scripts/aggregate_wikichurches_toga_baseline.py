#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path


METHODS = ("tip_adapter_f", "toga")
SHOTS = (1, 4, 16)
SEEDS = (1, 2, 3)


def mean_sd(values: list[float]) -> tuple[float, float]:
    return statistics.mean(values), statistics.stdev(values)


def fmt(values: list[float]) -> str:
    mean, sd = mean_sd(values)
    return f"{mean:.2f} ± {sd:.2f}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-dir", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    records = []
    for path in sorted(args.json_dir.glob("*.json")):
        with path.open(encoding="utf-8") as handle:
            record = json.load(handle)
        record["_path"] = str(path)
        records.append(record)

    expected = {
        (seed, shots, method)
        for seed in SEEDS
        for shots in SHOTS
        for method in METHODS
    }
    observed = {
        (int(r["seed"]), int(r["shots"]), r["method"])
        for r in records
    }
    if observed != expected:
        missing = sorted(expected - observed)
        extra = sorted(observed - expected)
        raise SystemExit(f"Incomplete matrix; missing={missing}, extra={extra}")

    rows = []
    by_key = {}
    for record in records:
        row = {
            "seed": int(record["seed"]),
            "shots": int(record["shots"]),
            "method": record["method"],
            "zero_shot_test_accuracy": float(
                record["shared_baselines"]["zero_shot_test_accuracy"]
            ),
            "tip_adapter_test_accuracy": float(
                record["shared_baselines"]["tip_adapter_test_accuracy"]
            ),
            "final_val_accuracy": float(record["fine_tuned"]["final_val_accuracy"]),
            "final_test_accuracy": float(
                record["fine_tuned"]["final_test_accuracy"]
            ),
            "best_epoch": int(record["fine_tuned"]["best_epoch"]),
        }
        rows.append(row)
        by_key[(row["seed"], row["shots"], row["method"])] = row

    with (args.out_dir / "per_run_results.csv").open(
        "w",
        newline="",
        encoding="utf-8",
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(
            sorted(rows, key=lambda r: (r["shots"], r["seed"], r["method"]))
        )

    summary_rows = []
    for shots in SHOTS:
        for method in METHODS:
            values = [
                by_key[(seed, shots, method)]["final_test_accuracy"]
                for seed in SEEDS
            ]
            mean, sd = mean_sd(values)
            summary_rows.append(
                {
                    "shots": shots,
                    "method": method,
                    "mean_test_accuracy": mean,
                    "sd_test_accuracy": sd,
                    "seed_values": ";".join(f"{v:.6f}" for v in values),
                }
            )

    with (args.out_dir / "summary.csv").open(
        "w",
        newline="",
        encoding="utf-8",
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summary_rows[0]))
        writer.writeheader()
        writer.writerows(summary_rows)

    paired_deltas = {}
    all_deltas = []
    for shots in SHOTS:
        deltas = [
            by_key[(seed, shots, "toga")]["final_test_accuracy"]
            - by_key[(seed, shots, "tip_adapter_f")]["final_test_accuracy"]
            for seed in SEEDS
        ]
        paired_deltas[shots] = deltas
        all_deltas.extend(deltas)

    lines = [
        "# WikiChurches-4 TOGA mother-method screening",
        "",
        "Protocol: church-disjoint official splits; 1/4/16-shot; seeds 1/2/3; "
        "validation-selected checkpoints; test evaluated only after selection.",
        "",
        "## Test accuracy",
        "",
        "| Shots | Tip-Adapter-F | TOGA | Paired Δ (TOGA − Tip-F) |",
        "|---:|---:|---:|---:|",
    ]
    for shots in SHOTS:
        tip_values = [
            by_key[(seed, shots, "tip_adapter_f")]["final_test_accuracy"]
            for seed in SEEDS
        ]
        toga_values = [
            by_key[(seed, shots, "toga")]["final_test_accuracy"]
            for seed in SEEDS
        ]
        lines.append(
            f"| {shots} | {fmt(tip_values)} | {fmt(toga_values)} | "
            f"{fmt(paired_deltas[shots])} |"
        )

    overall_mean, overall_sd = mean_sd(all_deltas)
    wins = sum(delta > 0 for delta in all_deltas)
    ties = sum(math.isclose(delta, 0.0, abs_tol=1e-12) for delta in all_deltas)
    lines.extend(
        [
            "",
            "## Screening interpretation",
            "",
            f"- Mean paired delta across the 9 matched runs: "
            f"{overall_mean:+.2f} ± {overall_sd:.2f} percentage points.",
            f"- Direction count: TOGA wins {wins}/9, ties {ties}/9, "
            f"loses {9 - wins - ties}/9.",
            "- This is a fixed-hyperparameter domain-transfer screen, not a "
            "paper-level reproduction or a tuned WikiChurches result.",
            "",
            "## Per-seed paired deltas",
            "",
        ]
    )
    for shots in SHOTS:
        lines.append(
            f"- {shots}-shot: "
            + ", ".join(
                f"seed {seed}: {delta:+.2f}"
                for seed, delta in zip(SEEDS, paired_deltas[shots])
            )
        )

    (args.out_dir / "README.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

