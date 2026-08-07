#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
import statistics
from pathlib import Path


SHOTS = (1, 4, 16)
SEEDS = (1, 2, 3)
BASELINE_ID = "c0_baseline"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-dir", type=Path, required=True)
    parser.add_argument("--candidate-file", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    candidate_document = json.loads(
        args.candidate_file.read_text(encoding="utf-8")
    )
    candidate_ids = tuple(candidate_document["candidates"])
    records = []
    for path in sorted(args.json_dir.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if not record.get("validation_only"):
            raise SystemExit(f"Non-validation-only result found: {path}")
        if (
            record["shared_baselines"]["zero_shot_test_accuracy"] is not None
            or record["shared_baselines"]["tip_adapter_test_accuracy"] is not None
            or record["fine_tuned"]["final_test_accuracy"] is not None
        ):
            raise SystemExit(f"Test metric found in validation screen: {path}")
        match = re.fullmatch(r"(.+)_s(1|4|16)_seed([123])\.json", path.name)
        if match is None:
            raise SystemExit(f"Unexpected validation result filename: {path}")
        candidate_id = match.group(1)
        records.append(
            {
                "candidate_id": candidate_id,
                "shots": int(record["shots"]),
                "seed": int(record["seed"]),
                "final_val_accuracy": float(
                    record["fine_tuned"]["final_val_accuracy"]
                ),
                "checkpoint_val_accuracy": float(
                    record["fine_tuned"]["checkpoint_selection_val_accuracy"]
                ),
                "best_epoch": int(record["fine_tuned"]["best_epoch"]),
                "best_alpha": float(record["fine_tuned"]["best_alpha"]),
                "best_beta": float(record["fine_tuned"]["best_beta"]),
            }
        )

    expected = {
        (candidate_id, shots, seed)
        for candidate_id in candidate_ids
        for shots in SHOTS
        for seed in SEEDS
    }
    observed = {
        (row["candidate_id"], row["shots"], row["seed"])
        for row in records
    }
    if observed != expected:
        raise SystemExit(
            f"Incomplete validation matrix; missing={sorted(expected-observed)}, "
            f"extra={sorted(observed-expected)}"
        )

    records.sort(
        key=lambda row: (row["shots"], row["candidate_id"], row["seed"])
    )
    with (args.out_dir / "per_run_validation.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)

    by_key = {
        (row["candidate_id"], row["shots"], row["seed"]): row
        for row in records
    }
    summary_rows = []
    selected = {}
    for shots in SHOTS:
        baseline = [
            by_key[(BASELINE_ID, shots, seed)]["final_val_accuracy"]
            for seed in SEEDS
        ]
        shot_rows = []
        for candidate_id in candidate_ids:
            values = [
                by_key[(candidate_id, shots, seed)]["final_val_accuracy"]
                for seed in SEEDS
            ]
            paired_deltas = [
                value - reference
                for value, reference in zip(values, baseline, strict=True)
            ]
            mean_delta = statistics.mean(paired_deltas)
            sd_delta = statistics.stdev(paired_deltas)
            robust_score = mean_delta - 0.5 * sd_delta
            row = {
                "shots": shots,
                "candidate_id": candidate_id,
                "mean_val_accuracy": statistics.mean(values),
                "sd_val_accuracy": statistics.stdev(values),
                "worst_val_accuracy": min(values),
                "mean_paired_delta_vs_c0": mean_delta,
                "sd_paired_delta_vs_c0": sd_delta,
                "robust_score": robust_score,
                "seed_values": ";".join(f"{value:.6f}" for value in values),
                "paired_deltas": ";".join(
                    f"{delta:.6f}" for delta in paired_deltas
                ),
            }
            shot_rows.append(row)
            summary_rows.append(row)

        best = max(
            shot_rows,
            key=lambda row: (
                row["robust_score"],
                row["mean_paired_delta_vs_c0"],
                row["mean_val_accuracy"],
                row["candidate_id"] == BASELINE_ID,
            ),
        )
        if best["robust_score"] <= 0:
            best = next(
                row for row in shot_rows if row["candidate_id"] == BASELINE_ID
            )
        candidate_id = best["candidate_id"]
        selected[str(shots)] = {
            "candidate_id": candidate_id,
            "hyperparameters": candidate_document["candidates"][candidate_id],
            "selection": {
                key: best[key]
                for key in (
                    "mean_val_accuracy",
                    "sd_val_accuracy",
                    "worst_val_accuracy",
                    "mean_paired_delta_vs_c0",
                    "sd_paired_delta_vs_c0",
                    "robust_score",
                )
            },
        }

    with (args.out_dir / "candidate_summary.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summary_rows[0]))
        writer.writeheader()
        writer.writerows(summary_rows)

    frozen = {
        "selection_protocol": candidate_document["protocol"],
        "baseline_candidate": BASELINE_ID,
        "selected_by_shot": selected,
        "confirmation_seeds": [4, 5, 6],
        "confirmation_test_policy": (
            "Evaluate test once after hyperparameters are frozen."
        ),
    }
    (args.out_dir / "frozen_configs.json").write_text(
        json.dumps(frozen, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# WikiChurches TOGA validation-only screen",
        "",
        "Selection score: mean paired validation delta versus c0 minus "
        "0.5 × sample SD of the paired deltas. Test metrics are asserted null.",
        "",
        "| Shots | Selected | Mean val | Mean paired Δ | SD paired Δ | Score |",
        "|---:|---|---:|---:|---:|---:|",
    ]
    for shots in SHOTS:
        choice = selected[str(shots)]
        metrics = choice["selection"]
        lines.append(
            f"| {shots} | {choice['candidate_id']} | "
            f"{metrics['mean_val_accuracy']:.2f} | "
            f"{metrics['mean_paired_delta_vs_c0']:+.2f} | "
            f"{metrics['sd_paired_delta_vs_c0']:.2f} | "
            f"{metrics['robust_score']:+.2f} |"
        )
    (args.out_dir / "README.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
