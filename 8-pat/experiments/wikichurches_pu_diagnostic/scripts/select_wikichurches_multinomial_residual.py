#!/usr/bin/env python3
"""Select a train-only ridge multinomial local residual on validation."""

from __future__ import annotations

import argparse
import csv
import json
import statistics
from pathlib import Path

import torch
import torch.nn.functional as F


def accuracy(logits: torch.Tensor, labels: torch.Tensor) -> float:
    return 100.0 * float((logits.argmax(dim=-1) == labels).float().mean())


def balanced_accuracy(
    logits: torch.Tensor,
    labels: torch.Tensor,
    class_count: int,
) -> float:
    predictions = logits.argmax(dim=-1)
    recalls = [
        float(
            (
                predictions[labels == class_index]
                == labels[labels == class_index]
            )
            .float()
            .mean()
        )
        for class_index in range(class_count)
    ]
    return 100.0 * statistics.mean(recalls)


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


def make_stratified_folds(
    labels: torch.Tensor,
    class_count: int,
    fold_count: int,
    seed: int,
) -> list[torch.Tensor]:
    generator = torch.Generator().manual_seed(seed)
    folds: list[list[int]] = [[] for _ in range(fold_count)]
    for class_index in range(class_count):
        indices = torch.where(labels == class_index)[0]
        permutation = indices[torch.randperm(len(indices), generator=generator)]
        for position, index in enumerate(permutation.tolist()):
            folds[position % fold_count].append(index)
    return [torch.tensor(sorted(fold), dtype=torch.long) for fold in folds]


def fit_head(
    features: torch.Tensor,
    labels: torch.Tensor,
    ridge_lambda: float,
    std_floor: float,
    class_count: int,
) -> dict[str, torch.Tensor]:
    x = features.double()
    y = labels.long()
    mean = x.mean(dim=0)
    scale = x.std(dim=0, correction=0).clamp_min(std_floor)
    standardized = (x - mean) / scale
    weights = torch.zeros(
        standardized.shape[1],
        class_count,
        dtype=torch.float64,
        requires_grad=True,
    )
    intercept = torch.zeros(
        class_count,
        dtype=torch.float64,
        requires_grad=True,
    )
    counts = torch.bincount(y, minlength=class_count).double()
    class_weights = len(y) / (class_count * counts)
    optimizer = torch.optim.LBFGS(
        [weights, intercept],
        lr=1.0,
        max_iter=500,
        tolerance_grad=1e-10,
        tolerance_change=1e-12,
        history_size=100,
        line_search_fn="strong_wolfe",
    )

    def closure() -> torch.Tensor:
        optimizer.zero_grad()
        logits = standardized @ weights + intercept
        loss = F.cross_entropy(logits, y, weight=class_weights)
        loss = loss + 0.5 * ridge_lambda * weights.square().sum()
        loss.backward()
        return loss

    optimizer.step(closure)
    with torch.no_grad():
        final_logits = standardized @ weights + intercept
        final_loss = float(
            F.cross_entropy(final_logits, y, weight=class_weights)
            + 0.5 * ridge_lambda * weights.square().sum()
        )
    return {
        "feature_mean": mean.float(),
        "feature_scale": scale.float(),
        "weights": weights.detach().float(),
        "intercept": intercept.detach().float(),
        "train_objective": torch.tensor(final_loss),
    }


def apply_head(features: torch.Tensor, head: dict[str, torch.Tensor]) -> torch.Tensor:
    standardized = (
        features.float() - head["feature_mean"]
    ) / head["feature_scale"]
    logits = standardized @ head["weights"] + head["intercept"]
    return logits - logits.mean(dim=-1, keepdim=True)


def serialize_head(head: dict[str, torch.Tensor]) -> dict[str, object]:
    return {
        key: (
            float(value)
            if value.ndim == 0
            else value.tolist()
        )
        for key, value in head.items()
    }


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
        == protocol["parent_experiment_id"]
    ):
        raise RuntimeError("Parent experiment identity mismatch")

    ratio_key = str(float(protocol["topk_patch_ratio"]))
    train_features = calibration["official_calibration_scores"][ratio_key].float()
    train_labels = calibration["labels"].long()
    labels = local["labels"].long()
    style_names = list(local["style_names"])
    class_count = len(style_names)
    std_floor = 0.02
    fold_count = 4
    fold_seed = 260727005
    folds = make_stratified_folds(
        train_labels,
        class_count,
        fold_count,
        fold_seed,
    )
    all_indices = torch.arange(len(train_labels))
    lambdas = [
        float(value)
        for value in protocol["residual_head"]["ridge_lambda_grid"]
    ]
    cv_rows = []
    for ridge_lambda in lambdas:
        fold_scores = []
        out_of_fold_logits = torch.empty(
            len(train_labels),
            class_count,
            dtype=torch.float32,
        )
        for fold_index, validation_indices in enumerate(folds):
            train_mask = torch.ones(len(train_labels), dtype=torch.bool)
            train_mask[validation_indices] = False
            training_indices = all_indices[train_mask]
            head = fit_head(
                train_features[training_indices],
                train_labels[training_indices],
                ridge_lambda,
                std_floor,
                class_count,
            )
            fold_logits = apply_head(
                train_features[validation_indices],
                head,
            )
            out_of_fold_logits[validation_indices] = fold_logits
            fold_scores.append(
                balanced_accuracy(
                    fold_logits,
                    train_labels[validation_indices],
                    class_count,
                )
            )
        mean_score = statistics.mean(fold_scores)
        sd_score = sample_sd(fold_scores)
        per_class = class_accuracies(
            out_of_fold_logits,
            train_labels,
            class_count,
        )
        cv_rows.append(
            {
                "ridge_lambda": ridge_lambda,
                "mean_fold_balanced_accuracy": mean_score,
                "sd_fold_balanced_accuracy": sd_score,
                "robust_cv_score": mean_score - 0.25 * sd_score,
                "oof_balanced_accuracy": balanced_accuracy(
                    out_of_fold_logits,
                    train_labels,
                    class_count,
                ),
                "minimum_oof_class_recall": min(per_class),
                **{
                    f"oof_recall_{style_names[index]}": value
                    for index, value in enumerate(per_class)
                },
            }
        )
    selected_cv = max(
        cv_rows,
        key=lambda row: (
            row["robust_cv_score"],
            row["mean_fold_balanced_accuracy"],
            row["ridge_lambda"],
        ),
    )
    selected_lambda = float(selected_cv["ridge_lambda"])
    official_head = fit_head(
        train_features,
        train_labels,
        selected_lambda,
        std_floor,
        class_count,
    )
    official_evidence = apply_head(
        local["official_local_scores"][ratio_key].float(),
        official_head,
    )

    random_train = calibration["random_calibration_scores"][ratio_key].float()
    random_heads = [
        fit_head(
            bank_features,
            train_labels,
            selected_lambda,
            std_floor,
            class_count,
        )
        for bank_features in random_train
    ]
    random_evidence = torch.stack(
        [
            apply_head(bank_scores.float(), head)
            for bank_scores, head in zip(
                local["random_local_scores"][ratio_key],
                random_heads,
                strict=True,
            )
        ]
    )

    shots_values = [int(value) for value in protocol["shots"]]
    seeds = [int(value) for value in protocol["development_seeds"]]
    thresholds = [
        float(value)
        for value in protocol["confidence_gate"]["threshold_grid"]
    ]
    temperature = float(protocol["confidence_gate"]["temperature"])
    gammas = [float(value) for value in protocol["fusion_gamma_grid"]]
    style_safety_floor = float(
        protocol["candidate_safety"][
            "minimum_style_mean_delta_within_each_shot"
        ]
    )
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
                class_delta_by_style = [[] for _ in range(class_count)]
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
                    class_deltas = [
                        official - baseline
                        for official, baseline in zip(
                            official_class,
                            baseline_class,
                            strict=True,
                        )
                    ]
                    for class_index, delta in enumerate(class_deltas):
                        class_delta_by_style[class_index].append(delta)
                    detail = {
                        "seed": seed,
                        "baseline_accuracy": baseline_accuracy,
                        "official_accuracy": official_accuracy,
                        "official_delta": official_accuracy - baseline_accuracy,
                        "random_mean_accuracy": random_accuracy,
                        "random_mean_delta": random_accuracy - baseline_accuracy,
                        "class_deltas": class_deltas,
                        "mean_gate": float(gate.mean()),
                    }
                    seed_details.append(detail)
                    official_deltas.append(detail["official_delta"])
                    random_deltas.append(detail["random_mean_delta"])
                style_mean_deltas = [
                    statistics.mean(values) for values in class_delta_by_style
                ]
                worst_style_index = min(
                    range(class_count),
                    key=lambda index: style_mean_deltas[index],
                )
                safe = style_mean_deltas[worst_style_index] >= style_safety_floor
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
                    "worst_style": style_names[worst_style_index],
                    "worst_style_mean_delta": style_mean_deltas[
                        worst_style_index
                    ],
                    "style_safe": safe,
                }
                candidate_rows.append(row)
                shot_candidates.append((row, seed_details))

        eligible = [item for item in shot_candidates if item[0]["style_safe"]]
        if not eligible:
            raise RuntimeError(f"No style-safe candidate for {shots}-shot")
        best_row, best_details = max(
            eligible,
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
                for item in eligible
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
                    "worst_style",
                    "worst_style_mean_delta",
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
        "train_head_robust_cv_balanced_accuracy": {
            "observed": float(selected_cv["robust_cv_score"]),
            "required": float(
                rule["train_head_robust_cv_balanced_accuracy_at_least"]
            ),
            "pass": float(selected_cv["robust_cv_score"])
            >= float(rule["train_head_robust_cv_balanced_accuracy_at_least"]),
        },
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
        "selected_ridge_lambda": selected_lambda,
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
        "topk_patch_ratio": float(protocol["topk_patch_ratio"]),
        "selected_ridge_lambda": selected_lambda,
        "head_cv_selection": selected_cv,
        "official_head": serialize_head(official_head),
        "random_heads": [serialize_head(head) for head in random_heads],
        "gate_temperature": temperature,
        "selected_by_shot": selected_by_shot,
        "development_seeds": seeds,
        "confirmation_seeds": protocol["confirmation_seeds"],
    }

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for name, rows in (
        ("head_cv_grid.csv", cv_rows),
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
        "# WikiChurches multinomial-residual validation-only selection",
        "",
        f"Decision: **{decision['decision']}**. Test images encoded: "
        f"**{decision['test_images_encoded']}**.",
        "",
        f"Selected ridge λ: **{selected_lambda:g}**; train-CV robust balanced "
        f"accuracy: **{selected_cv['robust_cv_score']:.2f}%**.",
        "",
        "| Shots | Gate τ | Gamma | Official Δ | SD | Robust | Random Δ | O−R | Wins | Worst style Δ |",
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
            f"{metrics['worst_style']} {metrics['worst_style_mean_delta']:+.2f} |"
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
