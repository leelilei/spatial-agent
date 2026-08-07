#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from pathlib import Path


METHODS = ("tip_adapter_f", "toga")
SHOTS = (1, 2, 4, 8, 16)
SEEDS = (1, 2, 3)
PAPER_TIP_F = {1: 59.5, 2: 66.1, 4: 74.1, 8: 77.9, 16: 84.5}
PAPER_TOGA = {1: 67.4, 2: 74.9, 4: 80.3, 8: 84.1, 16: 89.4}


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
        records.append(record)

    expected = {
        (seed, shots, method)
        for seed in SEEDS
        for shots in SHOTS
        for method in METHODS
    }
    observed = {
        (int(record["seed"]), int(record["shots"]), record["method"])
        for record in records
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
            "best_alpha": float(record["fine_tuned"]["best_alpha"]),
            "best_beta": float(record["fine_tuned"]["best_beta"]),
        }
        rows.append(row)
        by_key[(row["seed"], row["shots"], row["method"])] = row

    rows.sort(key=lambda row: (row["shots"], row["seed"], row["method"]))
    with (args.out_dir / "per_run_results.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    summary_rows = []
    paired_deltas: dict[int, list[float]] = {}
    all_deltas = []
    for shots in SHOTS:
        tip_values = [
            by_key[(seed, shots, "tip_adapter_f")]["final_test_accuracy"]
            for seed in SEEDS
        ]
        toga_values = [
            by_key[(seed, shots, "toga")]["final_test_accuracy"]
            for seed in SEEDS
        ]
        deltas = [
            toga - tip for toga, tip in zip(toga_values, tip_values, strict=True)
        ]
        paired_deltas[shots] = deltas
        all_deltas.extend(deltas)
        for method, values, target in (
            ("tip_adapter_f", tip_values, PAPER_TIP_F[shots]),
            ("toga", toga_values, PAPER_TOGA[shots]),
        ):
            mean, sd = mean_sd(values)
            summary_rows.append(
                {
                    "shots": shots,
                    "method": method,
                    "mean_test_accuracy": mean,
                    "sd_test_accuracy": sd,
                    "paper_accuracy": target,
                    "gap_to_paper": mean - target,
                    "seed_values": ";".join(f"{value:.6f}" for value in values),
                }
            )

    with (args.out_dir / "summary.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summary_rows[0]))
        writer.writeheader()
        writer.writerows(summary_rows)

    lines = [
        "# TOGA EuroSAT official-direction reproduction",
        "",
        "Protocol: CoOp/Tip-Adapter fixed split; CLIP ViT-B/16; official "
        "dataset/shot presets; seeds 1/2/3; validation-selected checkpoints "
        "and cache hyperparameters; test evaluated only after selection.",
        "",
        "## Test accuracy",
        "",
        "| Shots | Internal Tip-F | TOGA | Paired Δ | Paper Tip-F | Paper TOGA | TOGA gap |",
        "|---:|---:|---:|---:|---:|---:|---:|",
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
        toga_mean = statistics.mean(toga_values)
        lines.append(
            f"| {shots} | {fmt(tip_values)} | {fmt(toga_values)} | "
            f"{fmt(paired_deltas[shots])} | {PAPER_TIP_F[shots]:.1f} | "
            f"{PAPER_TOGA[shots]:.1f} | {toga_mean - PAPER_TOGA[shots]:+.2f} |"
        )

    overall_mean, overall_sd = mean_sd(all_deltas)
    wins = sum(delta > 0 for delta in all_deltas)
    ties = sum(math.isclose(delta, 0.0, abs_tol=1e-12) for delta in all_deltas)
    mean_abs_toga_gap = statistics.mean(
        abs(
            statistics.mean(
                [
                    by_key[(seed, shots, "toga")]["final_test_accuracy"]
                    for seed in SEEDS
                ]
            )
            - PAPER_TOGA[shots]
        )
        for shots in SHOTS
    )
    lines.extend(
        [
            "",
            "## Diagnostics",
            "",
            f"- Mean paired TOGA − internal Tip-F delta: "
            f"{overall_mean:+.2f} ± {overall_sd:.2f} percentage points.",
            f"- Direction count: TOGA wins {wins}/15, ties {ties}/15, "
            f"loses {15 - wins - ties}/15.",
            f"- Mean absolute gap between reproduced and paper TOGA curves: "
            f"{mean_abs_toga_gap:.2f} percentage points.",
            "- The internal Tip-F control uses the repository's TOGA-tuned "
            "shot preset; it is not assumed identical to the historical "
            "Tip-Adapter-F row quoted by the paper.",
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
                for seed, delta in zip(SEEDS, paired_deltas[shots], strict=True)
            )
        )

    (args.out_dir / "README.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
