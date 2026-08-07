#!/usr/bin/env python3
"""Select a WikiChurches positive-anchor fusion on validation data only."""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from pathlib import Path

import torch


def accuracy(logits: torch.Tensor, labels: torch.Tensor) -> float:
    return 100.0 * float((logits.argmax(dim=-1) == labels).float().mean())


def sample_sd(values: list[float]) -> float:
    return statistics.stdev(values) if len(values) > 1 else 0.0


def load_prediction(path: Path, shots: int, seed: int) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    record = torch.load(path, map_location="cpu")
    if int(record["shots"]) != shots or int(record["seed"]) != seed:
        raise RuntimeError(f"Run identity mismatch in {path}")
    if not bool(record["validation_only"]):
        raise RuntimeError(f"Development prediction is not validation-only: {path}")
    if record["test_logits"] is not None or record["test_labels"] is not None:
        raise RuntimeError(f"Test tensors found in development prediction: {path}")
    return record


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--local-val", type=Path, required=True)
    parser.add_argument("--prediction-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    local = torch.load(args.local_val, map_location="cpu")
    if local["split"] != "val" or int(local["test_images_encoded"]) != 0:
        raise RuntimeError("Local development artifact is not validation-only")
    if local["experiment_id"] != protocol["experiment_id"]:
        raise RuntimeError("Protocol/local experiment identity mismatch")

    shots_values = [int(value) for value in protocol["shots"]]
    seeds = [int(value) for value in protocol["development_seeds"]]
    ratios = [float(value) for value in protocol["topk_patch_ratios"]]
    gammas = [float(value) for value in protocol["fusion_gamma_grid"]]
    local_labels = local["labels"].long()
    predictions: dict[tuple[int, int], dict] = {}
    for shots in shots_values:
        for seed in seeds:
            path = args.prediction_dir / f"tipf_s{shots}_seed{seed}.pt"
            prediction = load_prediction(path, shots, seed)
            if not torch.equal(prediction["val_labels"].long(), local_labels):
                raise RuntimeError(f"Validation label/order mismatch: {path}")
            predictions[(shots, seed)] = prediction

    candidate_rows = []
    selected_by_shot = {}
    per_seed_rows = []
    for shots in shots_values:
        shot_candidates = []
        for ratio in ratios:
            official_local = local["official_local_scores"][str(ratio)].float()
            random_local = local["random_local_scores"][str(ratio)].float()
            if random_local.ndim != 3:
                raise RuntimeError("Random local scores must have [banks, images, classes]")
            for gamma in gammas:
                official_deltas = []
                random_deltas = []
                official_accuracies = []
                random_accuracies = []
                seed_details = []
                for seed in seeds:
                    prediction = predictions[(shots, seed)]
                    logits = prediction["val_logits"].float()
                    baseline_accuracy = accuracy(logits, local_labels)
                    official_accuracy = accuracy(
                        logits + gamma * official_local,
                        local_labels,
                    )
                    per_random_accuracy = [
                        accuracy(logits + gamma * bank_scores, local_labels)
                        for bank_scores in random_local
                    ]
                    random_accuracy = statistics.mean(per_random_accuracy)
                    official_delta = official_accuracy - baseline_accuracy
                    random_delta = random_accuracy - baseline_accuracy
                    official_accuracies.append(official_accuracy)
                    random_accuracies.append(random_accuracy)
                    official_deltas.append(official_delta)
                    random_deltas.append(random_delta)
                    seed_details.append(
                        {
                            "seed": seed,
                            "baseline_accuracy": baseline_accuracy,
                            "official_accuracy": official_accuracy,
                            "official_delta": official_delta,
                            "random_mean_accuracy": random_accuracy,
                            "random_mean_delta": random_delta,
                        }
                    )
                mean_delta = statistics.mean(official_deltas)
                sd_delta = sample_sd(official_deltas)
                row = {
                    "shots": shots,
                    "topk_patch_ratio": ratio,
                    "gamma": gamma,
                    "mean_official_accuracy": statistics.mean(official_accuracies),
                    "mean_official_delta": mean_delta,
                    "sd_official_delta": sd_delta,
                    "robust_score": mean_delta - 0.5 * sd_delta,
                    "official_wins": sum(delta > 0 for delta in official_deltas),
                    "mean_random_accuracy": statistics.mean(random_accuracies),
                    "mean_random_delta": statistics.mean(random_deltas),
                    "official_minus_random_delta": (
                        statistics.mean(official_deltas)
                        - statistics.mean(random_deltas)
                    ),
                }
                candidate_rows.append(row)
                shot_candidates.append((row, seed_details))

        best_row, best_details = max(
            shot_candidates,
            key=lambda item: (
                item[0]["robust_score"],
                item[0]["mean_official_delta"],
                item[0]["official_minus_random_delta"],
                -item[0]["gamma"],
                -item[0]["topk_patch_ratio"],
            ),
        )
        if best_row["robust_score"] <= 0:
            best_row, best_details = next(
                item
                for item in shot_candidates
                if item[0]["gamma"] == 0.0
                and item[0]["topk_patch_ratio"] == ratios[0]
            )
        selected_by_shot[str(shots)] = {
            "topk_patch_ratio": best_row["topk_patch_ratio"],
            "gamma": best_row["gamma"],
            "selection_metrics": {
                key: best_row[key]
                for key in (
                    "mean_official_accuracy",
                    "mean_official_delta",
                    "sd_official_delta",
                    "robust_score",
                    "official_wins",
                    "mean_random_accuracy",
                    "mean_random_delta",
                    "official_minus_random_delta",
                )
            },
        }
        for detail in best_details:
            per_seed_rows.append(
                {
                    "shots": shots,
                    "topk_patch_ratio": best_row["topk_patch_ratio"],
                    "gamma": best_row["gamma"],
                    **detail,
                }
            )

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
        "test_images_encoded": int(local["test_images_encoded"]),
    }
    frozen = {
        "experiment_id": protocol["experiment_id"],
        "selection_metric": protocol["selection"]["metric"],
        "selected_by_shot": selected_by_shot,
        "development_seeds": seeds,
        "confirmation_seeds": protocol["confirmation_seeds"],
        "confirmation_test_policy": protocol["selection"]["test_loader_policy"],
    }

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for name, rows in (
        ("candidate_grid.csv", candidate_rows),
        ("selected_per_seed.csv", per_seed_rows),
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
        "# WikiChurches positive-anchor validation-only selection",
        "",
        f"Decision: **{decision['decision']}**. Test images encoded: "
        f"**{decision['test_images_encoded']}**.",
        "",
        "| Shots | Ratio | Gamma | Official Δ | SD | Robust | Random Δ | O−R | Wins |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for shots in shots_values:
        choice = selected_by_shot[str(shots)]
        metrics = choice["selection_metrics"]
        lines.append(
            f"| {shots} | {choice['topk_patch_ratio']:.3g} | "
            f"{choice['gamma']:.3g} | {metrics['mean_official_delta']:+.2f} | "
            f"{metrics['sd_official_delta']:.2f} | "
            f"{metrics['robust_score']:+.2f} | "
            f"{metrics['mean_random_delta']:+.2f} | "
            f"{metrics['official_minus_random_delta']:+.2f} | "
            f"{metrics['official_wins']}/{len(seeds)} |"
        )
    lines.extend(["", "## Gate", ""])
    for name, condition in conditions.items():
        lines.append(
            f"- {name}: {condition['observed']} / {condition['required']} "
            f"({'PASS' if condition['pass'] else 'FAIL'})"
        )
    (args.out_dir / "README.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )
    if not math.isfinite(
        sum(row["robust_score"] for row in candidate_rows)
    ):
        raise RuntimeError("Non-finite validation result")
    print(json.dumps(decision, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
