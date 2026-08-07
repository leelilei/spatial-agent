#!/usr/bin/env python3
"""Evaluate the frozen multinomial local residual on test once."""

from __future__ import annotations

import argparse
import csv
import json
import statistics
from pathlib import Path

import torch


def accuracy(logits: torch.Tensor, labels: torch.Tensor) -> float:
    return 100.0 * float((logits.argmax(dim=-1) == labels).float().mean())


def class_accuracies(
    logits: torch.Tensor,
    labels: torch.Tensor,
    class_count: int,
) -> list[float]:
    predictions = logits.argmax(dim=-1)
    return [
        100.0
        * float(
            (
                predictions[labels == class_index]
                == labels[labels == class_index]
            )
            .float()
            .mean()
        )
        for class_index in range(class_count)
    ]


def sample_sd(values: list[float]) -> float:
    return statistics.stdev(values) if len(values) > 1 else 0.0


def deserialize_head(document: dict[str, object]) -> dict[str, torch.Tensor]:
    return {
        key: torch.tensor(value, dtype=torch.float32)
        for key, value in document.items()
    }


def apply_head(features: torch.Tensor, head: dict[str, torch.Tensor]) -> torch.Tensor:
    standardized = (
        features.float() - head["feature_mean"]
    ) / head["feature_scale"]
    logits = standardized @ head["weights"] + head["intercept"]
    return logits - logits.mean(dim=-1, keepdim=True)


def normalized_margin(logits: torch.Tensor) -> torch.Tensor:
    top_two = logits.topk(2, dim=-1).values
    scale = logits.std(dim=-1, correction=0).clamp_min(1e-6)
    return (top_two[:, 0] - top_two[:, 1]) / scale


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
        raise RuntimeError("Invalid local test artifact")
    if (
        frozen["experiment_id"] != protocol["experiment_id"]
        or local["experiment_id"] != protocol["parent_experiment_id"]
    ):
        raise RuntimeError("Experiment identity mismatch")

    ratio_key = str(float(frozen["topk_patch_ratio"]))
    labels = local["labels"].long()
    style_names = list(local["style_names"])
    class_count = len(style_names)
    official_evidence = apply_head(
        local["official_local_scores"][ratio_key].float(),
        deserialize_head(frozen["official_head"]),
    )
    random_evidence = torch.stack(
        [
            apply_head(scores.float(), deserialize_head(head))
            for scores, head in zip(
                local["random_local_scores"][ratio_key],
                frozen["random_heads"],
                strict=True,
            )
        ]
    )

    shots_values = [int(value) for value in protocol["shots"]]
    seeds = [int(value) for value in protocol["confirmation_seeds"]]
    temperature = float(frozen["gate_temperature"])
    rows = []
    class_rows = []
    for shots in shots_values:
        choice = frozen["selected_by_shot"][str(shots)]
        threshold = float(choice["gate_threshold"])
        gamma = float(choice["gamma"])
        for seed in seeds:
            path = args.prediction_dir / f"tipf_s{shots}_seed{seed}.pt"
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
            gate = torch.sigmoid(
                (threshold - normalized_margin(logits)) / temperature
            )
            official_logits = logits + gamma * gate[:, None] * official_evidence
            baseline_accuracy = accuracy(logits, labels)
            official_accuracy = accuracy(official_logits, labels)
            random_accuracies = [
                accuracy(
                    logits + gamma * gate[:, None] * bank_evidence,
                    labels,
                )
                for bank_evidence in random_evidence
            ]
            random_accuracy = statistics.mean(random_accuracies)
            rows.append(
                {
                    "shots": shots,
                    "seed": seed,
                    "gate_threshold": threshold,
                    "gamma": gamma,
                    "baseline_accuracy": baseline_accuracy,
                    "official_accuracy": official_accuracy,
                    "official_delta": official_accuracy - baseline_accuracy,
                    "random_mean_accuracy": random_accuracy,
                    "random_mean_delta": random_accuracy - baseline_accuracy,
                    "official_minus_random_delta": (
                        official_accuracy - random_accuracy
                    ),
                    "mean_gate": float(gate.mean()),
                }
            )
            baseline_class = class_accuracies(logits, labels, class_count)
            official_class = class_accuracies(
                official_logits,
                labels,
                class_count,
            )
            for class_name, baseline_value, official_value in zip(
                style_names,
                baseline_class,
                official_class,
                strict=True,
            ):
                class_rows.append(
                    {
                        "shots": shots,
                        "seed": seed,
                        "class_name": class_name,
                        "baseline_accuracy": baseline_value,
                        "official_accuracy": official_value,
                        "delta": official_value - baseline_value,
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
    style_mean_deltas = {
        class_name: statistics.mean(
            row["delta"]
            for row in class_rows
            if row["class_name"] == class_name
        )
        for class_name in style_names
    }
    worst_style = min(style_mean_deltas, key=style_mean_deltas.get)
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
        "worst_style_mean_delta": {
            "style": worst_style,
            "observed": style_mean_deltas[worst_style],
            "required": float(rule["minimum_worst_style_mean_delta"]),
            "pass": style_mean_deltas[worst_style]
            >= float(rule["minimum_worst_style_mean_delta"]),
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
        "style_mean_deltas": style_mean_deltas,
        "overall_mean_official_delta": overall_official_delta,
        "overall_mean_random_delta": overall_random_delta,
        "test_images_encoded": int(local["test_images_encoded"]),
    }

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for name, output_rows in (
        ("per_run_test.csv", rows),
        ("per_shot_summary.csv", shot_summary),
        ("per_class_test.csv", class_rows),
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
        "# WikiChurches multinomial-residual frozen confirmation",
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
    lines.extend(["", "## Style deltas", ""])
    for class_name, delta in style_mean_deltas.items():
        lines.append(f"- {class_name}: {delta:+.2f}pp")
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
