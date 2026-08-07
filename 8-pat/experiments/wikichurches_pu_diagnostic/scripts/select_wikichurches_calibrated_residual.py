#!/usr/bin/env python3
"""Select train-calibrated local residual fusion on validation only."""

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


def fit_negative_stats(
    scores: torch.Tensor,
    labels: torch.Tensor,
    std_floor: float,
) -> tuple[torch.Tensor, torch.Tensor]:
    class_count = scores.shape[-1]
    means = []
    scales = []
    for class_index in range(class_count):
        negatives = scores[labels != class_index, class_index]
        means.append(negatives.mean())
        scales.append(negatives.std(correction=0).clamp_min(std_floor))
    return torch.stack(means), torch.stack(scales)


def residual_evidence(
    scores: torch.Tensor,
    means: torch.Tensor,
    scales: torch.Tensor,
) -> torch.Tensor:
    z_scores = (scores - means) / scales
    return z_scores - z_scores.mean(dim=-1, keepdim=True)


def normalized_margin(logits: torch.Tensor) -> torch.Tensor:
    top_two = logits.topk(2, dim=-1).values
    scale = logits.std(dim=-1, correction=0).clamp_min(1e-6)
    return (top_two[:, 0] - top_two[:, 1]) / scale


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--local-val", type=Path, required=True)
    parser.add_argument("--calibration-train", type=Path, required=True)
    parser.add_argument("--prediction-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    local = torch.load(args.local_val, map_location="cpu")
    calibration = torch.load(args.calibration_train, map_location="cpu")
    if local["split"] != "val" or int(local["test_images_encoded"]) != 0:
        raise RuntimeError("Local development artifact is not validation-only")
    if (
        calibration["split"] != "train_loco_calibration"
        or int(calibration["test_images_encoded"]) != 0
    ):
        raise RuntimeError("Invalid train calibration artifact")
    if not (
        local["experiment_id"]
        == calibration["experiment_id"]
        == protocol["experiment_id"]
    ):
        raise RuntimeError("Experiment identity mismatch")

    ratio = float(protocol["topk_patch_ratio"])
    ratio_key = str(ratio)
    std_floor = float(protocol["calibration"]["std_floor"])
    train_labels = calibration["labels"].long()
    official_mean, official_scale = fit_negative_stats(
        calibration["official_calibration_scores"][ratio_key].float(),
        train_labels,
        std_floor,
    )
    random_train = calibration["random_calibration_scores"][ratio_key].float()
    random_stats = [
        fit_negative_stats(bank_scores, train_labels, std_floor)
        for bank_scores in random_train
    ]
    official_evidence = residual_evidence(
        local["official_local_scores"][ratio_key].float(),
        official_mean,
        official_scale,
    )
    random_evidence = torch.stack(
        [
            residual_evidence(
                bank_scores.float(),
                bank_mean,
                bank_scale,
            )
            for bank_scores, (bank_mean, bank_scale) in zip(
                local["random_local_scores"][ratio_key],
                random_stats,
                strict=True,
            )
        ]
    )
    labels = local["labels"].long()
    style_names = list(local["style_names"])
    class_count = len(style_names)
    shots_values = [int(value) for value in protocol["shots"]]
    seeds = [int(value) for value in protocol["development_seeds"]]
    thresholds = [
        float(value)
        for value in protocol["confidence_gate"]["threshold_grid"]
    ]
    temperature = float(protocol["confidence_gate"]["temperature"])
    gammas = [float(value) for value in protocol["fusion_gamma_grid"]]

    predictions = {}
    for shots in shots_values:
        for seed in seeds:
            path = args.prediction_dir / f"tipf_s{shots}_seed{seed}.pt"
            prediction = torch.load(path, map_location="cpu")
            if (
                int(prediction["shots"]) != shots
                or int(prediction["seed"]) != seed
                or not bool(prediction["validation_only"])
                or prediction["test_logits"] is not None
                or prediction["test_labels"] is not None
            ):
                raise RuntimeError(f"Invalid validation prediction: {path}")
            if not torch.equal(prediction["val_labels"].long(), labels):
                raise RuntimeError(f"Validation label/order mismatch: {path}")
            predictions[(shots, seed)] = prediction["val_logits"].float()

    candidate_rows = []
    selected_by_shot = {}
    selected_seed_rows = []
    selected_class_rows = []
    for shots in shots_values:
        shot_candidates = []
        for threshold in thresholds:
            for gamma in gammas:
                seed_details = []
                official_deltas = []
                random_deltas = []
                for seed in seeds:
                    logits = predictions[(shots, seed)]
                    gate = torch.sigmoid(
                        (threshold - normalized_margin(logits)) / temperature
                    )
                    baseline_accuracy = accuracy(logits, labels)
                    official_logits = (
                        logits + gamma * gate[:, None] * official_evidence
                    )
                    official_accuracy = accuracy(official_logits, labels)
                    per_random_accuracy = [
                        accuracy(
                            logits + gamma * gate[:, None] * bank_evidence,
                            labels,
                        )
                        for bank_evidence in random_evidence
                    ]
                    random_accuracy = statistics.mean(per_random_accuracy)
                    baseline_class = class_accuracies(
                        logits,
                        labels,
                        class_count,
                    )
                    official_class = class_accuracies(
                        official_logits,
                        labels,
                        class_count,
                    )
                    detail = {
                        "seed": seed,
                        "baseline_accuracy": baseline_accuracy,
                        "official_accuracy": official_accuracy,
                        "official_delta": official_accuracy - baseline_accuracy,
                        "random_mean_accuracy": random_accuracy,
                        "random_mean_delta": random_accuracy - baseline_accuracy,
                        "class_deltas": [
                            official - baseline
                            for official, baseline in zip(
                                official_class,
                                baseline_class,
                                strict=True,
                            )
                        ],
                        "mean_gate": float(gate.mean()),
                    }
                    seed_details.append(detail)
                    official_deltas.append(detail["official_delta"])
                    random_deltas.append(detail["random_mean_delta"])
                mean_delta = statistics.mean(official_deltas)
                sd_delta = sample_sd(official_deltas)
                row = {
                    "shots": shots,
                    "gate_threshold": threshold,
                    "gamma": gamma,
                    "mean_official_delta": mean_delta,
                    "sd_official_delta": sd_delta,
                    "robust_score": mean_delta - 0.5 * sd_delta,
                    "official_wins": sum(delta > 0 for delta in official_deltas),
                    "mean_random_delta": statistics.mean(random_deltas),
                    "official_minus_random_delta": (
                        statistics.mean(official_deltas)
                        - statistics.mean(random_deltas)
                    ),
                    "mean_gate": statistics.mean(
                        detail["mean_gate"] for detail in seed_details
                    ),
                }
                candidate_rows.append(row)
                shot_candidates.append((row, seed_details))

        best_row, best_details = max(
            shot_candidates,
            key=lambda item: (
                item[0]["robust_score"],
                item[0]["official_minus_random_delta"],
                item[0]["mean_official_delta"],
                -item[0]["gamma"],
                -item[0]["gate_threshold"],
            ),
        )
        if best_row["robust_score"] <= 0:
            best_row, best_details = next(
                item
                for item in shot_candidates
                if item[0]["gamma"] == 0.0
                and item[0]["gate_threshold"] == thresholds[0]
            )
        selected_by_shot[str(shots)] = {
            "gate_threshold": best_row["gate_threshold"],
            "gamma": best_row["gamma"],
            "selection_metrics": {
                key: best_row[key]
                for key in (
                    "mean_official_delta",
                    "sd_official_delta",
                    "robust_score",
                    "official_wins",
                    "mean_random_delta",
                    "official_minus_random_delta",
                    "mean_gate",
                )
            },
        }
        for detail in best_details:
            selected_seed_rows.append(
                {
                    "shots": shots,
                    "gate_threshold": best_row["gate_threshold"],
                    "gamma": best_row["gamma"],
                    **{
                        key: value
                        for key, value in detail.items()
                        if key != "class_deltas"
                    },
                }
            )
            for class_name, delta in zip(
                style_names,
                detail["class_deltas"],
                strict=True,
            ):
                selected_class_rows.append(
                    {
                        "shots": shots,
                        "seed": detail["seed"],
                        "class_name": class_name,
                        "delta": delta,
                    }
                )

    style_mean_deltas = {
        class_name: statistics.mean(
            row["delta"]
            for row in selected_class_rows
            if row["class_name"] == class_name
        )
        for class_name in style_names
    }
    worst_style = min(style_mean_deltas, key=style_mean_deltas.get)
    positive_robust_shots = sum(
        selected_by_shot[str(shots)]["selection_metrics"]["robust_score"] > 0
        for shots in shots_values
    )
    official_better_random_shots = sum(
        selected_by_shot[str(shots)]["selection_metrics"][
            "official_minus_random_delta"
        ]
        > 0
        for shots in shots_values
    )
    official_wins = sum(
        selected_by_shot[str(shots)]["selection_metrics"]["official_wins"]
        for shots in shots_values
    )
    rule = protocol["validation_go_rule"]
    conditions = {
        "positive_robust_score_shots": {
            "observed": positive_robust_shots,
            "required": int(rule["positive_robust_score_shots_at_least"]),
            "pass": positive_robust_shots
            >= int(rule["positive_robust_score_shots_at_least"]),
        },
        "official_better_than_random_shots": {
            "observed": official_better_random_shots,
            "required": int(rule["official_better_than_random_shots_at_least"]),
            "pass": official_better_random_shots
            >= int(rule["official_better_than_random_shots_at_least"]),
        },
        "official_paired_wins": {
            "observed": official_wins,
            "required": int(rule["official_paired_wins_at_least"]),
            "pass": official_wins >= int(rule["official_paired_wins_at_least"]),
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
        "stage": "validation_only",
        "decision": (
            "GO_CONFIRMATION"
            if all(condition["pass"] for condition in conditions.values())
            else "NO_GO"
        ),
        "conditions": conditions,
        "style_mean_deltas": style_mean_deltas,
        "test_images_encoded": (
            int(local["test_images_encoded"])
            + int(calibration["test_images_encoded"])
        ),
    }
    frozen = {
        "experiment_id": protocol["experiment_id"],
        "parent_experiment_id": protocol["parent_experiment_id"],
        "topk_patch_ratio": ratio,
        "std_floor": std_floor,
        "gate_temperature": temperature,
        "official_calibration": {
            "negative_mean": official_mean.tolist(),
            "negative_scale": official_scale.tolist(),
        },
        "random_calibration": [
            {
                "negative_mean": mean.tolist(),
                "negative_scale": scale.tolist(),
            }
            for mean, scale in random_stats
        ],
        "selected_by_shot": selected_by_shot,
        "development_seeds": seeds,
        "confirmation_seeds": protocol["confirmation_seeds"],
    }

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for name, rows in (
        ("candidate_grid.csv", candidate_rows),
        ("selected_per_seed.csv", selected_seed_rows),
        ("selected_per_class.csv", selected_class_rows),
    ):
        with (args.out_dir / name).open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    (args.out_dir / "frozen_config.json").write_text(
        json.dumps(frozen, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (args.out_dir / "decision.json").write_text(
        json.dumps(decision, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# WikiChurches calibrated-residual validation-only selection",
        "",
        f"Decision: **{decision['decision']}**. Test images encoded: "
        f"**{decision['test_images_encoded']}**.",
        "",
        "| Shots | Gate τ | Gamma | Official Δ | SD | Robust | Random Δ | O−R | Wins | Mean gate |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for shots in shots_values:
        choice = selected_by_shot[str(shots)]
        metrics = choice["selection_metrics"]
        lines.append(
            f"| {shots} | {choice['gate_threshold']:.2f} | "
            f"{choice['gamma']:.2f} | {metrics['mean_official_delta']:+.2f} | "
            f"{metrics['sd_official_delta']:.2f} | "
            f"{metrics['robust_score']:+.2f} | "
            f"{metrics['mean_random_delta']:+.2f} | "
            f"{metrics['official_minus_random_delta']:+.2f} | "
            f"{metrics['official_wins']}/{len(seeds)} | "
            f"{metrics['mean_gate']:.2f} |"
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
