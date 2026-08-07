#!/usr/bin/env python3
"""Evaluate a frozen WikiChurches positive-anchor fusion on test once."""

from __future__ import annotations

import argparse
import csv
import json
import statistics
from pathlib import Path

import torch


def accuracy(logits: torch.Tensor, labels: torch.Tensor) -> float:
    return 100.0 * float((logits.argmax(dim=-1) == labels).float().mean())


def sample_sd(values: list[float]) -> float:
    return statistics.stdev(values) if len(values) > 1 else 0.0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--local-test", type=Path, required=True)
    parser.add_argument("--prediction-dir", type=Path, required=True)
    parser.add_argument("--frozen-config", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    frozen = json.loads(args.frozen_config.read_text(encoding="utf-8"))
    local = torch.load(args.local_test, map_location="cpu")
    if local["split"] != "test" or int(local["test_images_encoded"]) <= 0:
        raise RuntimeError("Local confirmation artifact is not test data")
    if not (
        local["experiment_id"]
        == frozen["experiment_id"]
        == protocol["experiment_id"]
    ):
        raise RuntimeError("Experiment identity mismatch")

    shots_values = [int(value) for value in protocol["shots"]]
    seeds = [int(value) for value in protocol["confirmation_seeds"]]
    labels = local["labels"].long()
    rows = []
    for shots in shots_values:
        choice = frozen["selected_by_shot"][str(shots)]
        ratio = float(choice["topk_patch_ratio"])
        gamma = float(choice["gamma"])
        official_local = local["official_local_scores"][str(ratio)].float()
        random_local = local["random_local_scores"][str(ratio)].float()
        for seed in seeds:
            path = args.prediction_dir / f"tipf_s{shots}_seed{seed}.pt"
            if not path.is_file():
                raise FileNotFoundError(path)
            prediction = torch.load(path, map_location="cpu")
            if (
                int(prediction["shots"]) != shots
                or int(prediction["seed"]) != seed
                or bool(prediction["validation_only"])
                or prediction["test_logits"] is None
            ):
                raise RuntimeError(f"Invalid confirmation prediction: {path}")
            if not torch.equal(prediction["test_labels"].long(), labels):
                raise RuntimeError(f"Test label/order mismatch: {path}")
            logits = prediction["test_logits"].float()
            baseline_accuracy = accuracy(logits, labels)
            official_accuracy = accuracy(logits + gamma * official_local, labels)
            random_accuracies = [
                accuracy(logits + gamma * bank_scores, labels)
                for bank_scores in random_local
            ]
            random_accuracy = statistics.mean(random_accuracies)
            rows.append(
                {
                    "shots": shots,
                    "seed": seed,
                    "topk_patch_ratio": ratio,
                    "gamma": gamma,
                    "baseline_accuracy": baseline_accuracy,
                    "official_accuracy": official_accuracy,
                    "official_delta": official_accuracy - baseline_accuracy,
                    "random_mean_accuracy": random_accuracy,
                    "random_mean_delta": random_accuracy - baseline_accuracy,
                    "official_minus_random_delta": (
                        official_accuracy - random_accuracy
                    ),
                }
            )

    shot_summary = []
    for shots in shots_values:
        shot_rows = [row for row in rows if row["shots"] == shots]
        official_deltas = [row["official_delta"] for row in shot_rows]
        random_deltas = [row["random_mean_delta"] for row in shot_rows]
        shot_summary.append(
            {
                "shots": shots,
                "mean_baseline_accuracy": statistics.mean(
                    row["baseline_accuracy"] for row in shot_rows
                ),
                "mean_official_accuracy": statistics.mean(
                    row["official_accuracy"] for row in shot_rows
                ),
                "mean_official_delta": statistics.mean(official_deltas),
                "sd_official_delta": sample_sd(official_deltas),
                "official_wins": sum(delta > 0 for delta in official_deltas),
                "mean_random_delta": statistics.mean(random_deltas),
                "official_minus_random_delta": (
                    statistics.mean(official_deltas)
                    - statistics.mean(random_deltas)
                ),
            }
        )

    positive_mean_shots = sum(
        row["mean_official_delta"] > 0 for row in shot_summary
    )
    official_wins = sum(row["official_delta"] > 0 for row in rows)
    overall_official_delta = statistics.mean(
        row["official_delta"] for row in rows
    )
    overall_random_delta = statistics.mean(
        row["random_mean_delta"] for row in rows
    )
    worst_shot_delta = min(row["mean_official_delta"] for row in shot_summary)
    rule = protocol["confirmation_go_rule"]
    conditions = {
        "positive_mean_shots": {
            "observed": positive_mean_shots,
            "required": int(rule["positive_mean_shots_at_least"]),
            "pass": positive_mean_shots
            >= int(rule["positive_mean_shots_at_least"]),
        },
        "official_paired_wins": {
            "observed": official_wins,
            "required": int(rule["official_paired_wins_at_least"]),
            "pass": official_wins >= int(rule["official_paired_wins_at_least"]),
        },
        "official_overall_delta_greater_than_random": {
            "official": overall_official_delta,
            "random": overall_random_delta,
            "pass": overall_official_delta > overall_random_delta,
        },
        "minimum_shot_mean_delta": {
            "observed": worst_shot_delta,
            "required": float(rule["minimum_allowed_shot_mean_delta"]),
            "pass": worst_shot_delta
            >= float(rule["minimum_allowed_shot_mean_delta"]),
        },
    }
    decision = {
        "experiment_id": protocol["experiment_id"],
        "stage": "frozen_test_confirmation",
        "decision": (
            "GO"
            if all(condition["pass"] for condition in conditions.values())
            else "NO_GO"
        ),
        "conditions": conditions,
        "overall_mean_official_delta": overall_official_delta,
        "overall_mean_random_delta": overall_random_delta,
        "test_images_encoded": int(local["test_images_encoded"]),
    }

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for name, output_rows in (
        ("per_run_test.csv", rows),
        ("per_shot_summary.csv", shot_summary),
    ):
        with (args.out_dir / name).open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(output_rows[0]))
            writer.writeheader()
            writer.writerows(output_rows)
    (args.out_dir / "decision.json").write_text(
        json.dumps(decision, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# WikiChurches positive-anchor frozen confirmation",
        "",
        f"Decision: **{decision['decision']}**.",
        "",
        "| Shots | Baseline | Official | Official Δ | SD | Random Δ | O−R | Wins |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in shot_summary:
        lines.append(
            f"| {row['shots']} | {row['mean_baseline_accuracy']:.2f} | "
            f"{row['mean_official_accuracy']:.2f} | "
            f"{row['mean_official_delta']:+.2f} | "
            f"{row['sd_official_delta']:.2f} | "
            f"{row['mean_random_delta']:+.2f} | "
            f"{row['official_minus_random_delta']:+.2f} | "
            f"{row['official_wins']}/{len(seeds)} |"
        )
    lines.extend(["", "## Gate", ""])
    for name, condition in conditions.items():
        lines.append(
            f"- {name}: {'PASS' if condition['pass'] else 'FAIL'} "
            f"({json.dumps(condition, sort_keys=True)})"
        )
    (args.out_dir / "README.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(decision, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
