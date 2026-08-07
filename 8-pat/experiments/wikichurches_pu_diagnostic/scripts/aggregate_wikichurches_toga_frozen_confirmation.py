#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from pathlib import Path


METHODS = ("tip_adapter_f", "toga")
SHOTS = (1, 4, 16)
SEEDS = (4, 5, 6)


def mean_sd(values: list[float]) -> tuple[float, float]:
    return statistics.mean(values), statistics.stdev(values)


def formatted(values: list[float]) -> str:
    mean, sd = mean_sd(values)
    return f"{mean:.2f} ± {sd:.2f}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-dir", type=Path, required=True)
    parser.add_argument("--protocol-file", type=Path, required=True)
    parser.add_argument("--frozen-file", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    protocol = json.loads(args.protocol_file.read_text(encoding="utf-8"))
    frozen = json.loads(args.frozen_file.read_text(encoding="utf-8"))
    records = [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(args.json_dir.glob("*.json"))
    ]
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
        raise SystemExit(
            f"Incomplete confirmation matrix; "
            f"missing={sorted(expected-observed)}, extra={sorted(observed-expected)}"
        )

    rows = []
    by_key = {}
    for record in records:
        if record.get("validation_only"):
            raise SystemExit("Validation-only result found in confirmation matrix")
        row = {
            "shots": int(record["shots"]),
            "seed": int(record["seed"]),
            "method": record["method"],
            "final_val_accuracy": float(record["fine_tuned"]["final_val_accuracy"]),
            "final_test_accuracy": float(record["fine_tuned"]["final_test_accuracy"]),
            "best_epoch": int(record["fine_tuned"]["best_epoch"]),
            "best_alpha": float(record["fine_tuned"]["best_alpha"]),
            "best_beta": float(record["fine_tuned"]["best_beta"]),
        }
        rows.append(row)
        by_key[(row["shots"], row["seed"], row["method"])] = row
    rows.sort(key=lambda row: (row["shots"], row["seed"], row["method"]))
    with (args.out_dir / "per_run_results.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    shot_summaries = []
    all_deltas = []
    paired_by_shot = {}
    for shots in SHOTS:
        tip_values = [
            by_key[(shots, seed, "tip_adapter_f")]["final_test_accuracy"]
            for seed in SEEDS
        ]
        toga_values = [
            by_key[(shots, seed, "toga")]["final_test_accuracy"]
            for seed in SEEDS
        ]
        deltas = [
            toga - tip for toga, tip in zip(toga_values, tip_values, strict=True)
        ]
        paired_by_shot[shots] = deltas
        all_deltas.extend(deltas)
        delta_mean, delta_sd = mean_sd(deltas)
        shot_summaries.append(
            {
                "shots": shots,
                "selected_candidate": frozen["selected_by_shot"][str(shots)][
                    "candidate_id"
                ],
                "tip_f_mean": statistics.mean(tip_values),
                "tip_f_sd": statistics.stdev(tip_values),
                "toga_mean": statistics.mean(toga_values),
                "toga_sd": statistics.stdev(toga_values),
                "paired_delta_mean": delta_mean,
                "paired_delta_sd": delta_sd,
                "wins": sum(delta > 0 for delta in deltas),
                "ties": sum(math.isclose(delta, 0.0, abs_tol=1e-12) for delta in deltas),
                "paired_deltas": ";".join(f"{delta:.6f}" for delta in deltas),
            }
        )
    with (args.out_dir / "summary.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(shot_summaries[0]))
        writer.writeheader()
        writer.writerows(shot_summaries)

    rule = protocol["go_rule"]
    positive_shots = sum(row["paired_delta_mean"] > 0 for row in shot_summaries)
    wins = sum(delta > 0 for delta in all_deltas)
    ties = sum(math.isclose(delta, 0.0, abs_tol=1e-12) for delta in all_deltas)
    worst_shot_mean = min(row["paired_delta_mean"] for row in shot_summaries)
    checks = {
        "positive_mean_shots": positive_shots
        >= rule["positive_mean_shots_at_least"],
        "paired_wins": wins >= rule["paired_wins_at_least"],
        "worst_shot_mean": worst_shot_mean
        >= rule["minimum_allowed_shot_mean_delta"],
    }
    decision = "GO" if all(checks.values()) else "NO-GO"
    decision_record = {
        "decision": decision,
        "predeclared_rule": rule,
        "observed": {
            "positive_mean_shots": positive_shots,
            "paired_wins": wins,
            "paired_ties": ties,
            "paired_losses": len(all_deltas) - wins - ties,
            "worst_shot_mean_delta": worst_shot_mean,
            "overall_mean_paired_delta": statistics.mean(all_deltas),
            "overall_sd_paired_delta": statistics.stdev(all_deltas),
        },
        "checks": checks,
    }
    (args.out_dir / "decision.json").write_text(
        json.dumps(decision_record, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# WikiChurches frozen-confirmation test",
        "",
        "Protocol: hyperparameters selected without constructing or evaluating "
        "the test split on seeds 1/2/3, then frozen before this single test "
        "evaluation on fresh seeds 4/5/6.",
        "",
        "| Shots | Frozen candidate | Tip-F | TOGA | Paired Δ | Wins |",
        "|---:|---|---:|---:|---:|---:|",
    ]
    for row in shot_summaries:
        shots = row["shots"]
        tip_values = [
            by_key[(shots, seed, "tip_adapter_f")]["final_test_accuracy"]
            for seed in SEEDS
        ]
        toga_values = [
            by_key[(shots, seed, "toga")]["final_test_accuracy"]
            for seed in SEEDS
        ]
        lines.append(
            f"| {shots} | {row['selected_candidate']} | "
            f"{formatted(tip_values)} | {formatted(toga_values)} | "
            f"{formatted(paired_by_shot[shots])} | {row['wins']}/3 |"
        )
    lines.extend(
        [
            "",
            f"Predeclared decision: **{decision}**.",
            "",
            f"- Positive shot-level mean deltas: {positive_shots}/3.",
            f"- Pairwise directions: {wins} wins, {ties} ties, "
            f"{len(all_deltas) - wins - ties} losses.",
            f"- Overall paired delta: {statistics.mean(all_deltas):+.2f} ± "
            f"{statistics.stdev(all_deltas):.2f} percentage points.",
            f"- Worst shot-level mean delta: {worst_shot_mean:+.2f} points.",
        ]
    )
    (args.out_dir / "README.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
