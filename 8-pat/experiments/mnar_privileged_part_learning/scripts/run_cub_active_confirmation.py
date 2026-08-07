#!/usr/bin/env python3
"""Run paired multi-seed confirmation for PAT-D-260728-006."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

import run_cub_missingness_screen as screen
from cub_active_selection import sha256_file


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--winner-selections", type=Path, required=True)
    parser.add_argument("--random-selections", type=Path, required=True)
    parser.add_argument("--screen-summary", type=Path, required=True)
    parser.add_argument("--stored-reference", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--oracle-protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--fold-limit", type=int, default=5)
    parser.add_argument("--epoch-limit", type=int, default=9)
    return parser.parse_args()


def bootstrap_interval(per_class_delta, replicates, seed):
    rng = np.random.default_rng(seed)
    values = np.asarray(per_class_delta, dtype=np.float64)
    draws = rng.integers(0, len(values), size=(replicates, len(values)))
    means = values[draws].mean(axis=1)
    return {
        "lower_95_pp": 100 * float(np.quantile(means, 0.025)),
        "upper_95_pp": 100 * float(np.quantile(means, 0.975)),
    }


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    oracle_protocol = json.loads(args.oracle_protocol.read_text())
    screen_summary = json.loads(args.screen_summary.read_text())
    if not screen_summary.get("overall_gate_pass"):
        raise RuntimeError("PAT-D-260728-005 gate has not passed")
    winner = screen_summary.get("winner")
    if not winner:
        raise RuntimeError("PAT-D-260728-005 did not freeze a winner")
    rows = [json.loads(line) for line in args.manifest.read_text().splitlines()]
    if any(
        row["split"] != "train" or row["source_split"] != "official_train"
        for row in rows
    ):
        raise RuntimeError("PAT-D-260728-006 may decode official train only")
    labels = np.asarray([row["class_index"] for row in rows])
    folds = np.asarray([row["fold"] for row in rows])
    winner_file = np.load(args.winner_selections)
    random_file = np.load(args.random_selections)
    reference = np.load(args.stored_reference)
    if not np.array_equal(labels, reference["labels"]):
        raise RuntimeError("Stored reference labels do not match manifest")
    global_prediction = reference["global_predictions"]
    global_recall = screen.class_recall(labels, global_prediction)
    raw = oracle_protocol["optimization"]
    settings = {
        "head_learning_rate": raw["head_learning_rate"],
        "backbone_learning_rate": raw["backbone_learning_rate"],
        "weight_decay": raw["weight_decay"],
        "part_loss_weight": raw["part_loss_weight"],
        "regularizer_weight": raw["complementary_regularizer_weight"],
        "batch_size": raw["batch_size"],
        "epochs": min(
            int(protocol["training"]["fixed_epochs"]), args.epoch_limit
        ),
    }
    fold_count = min(int(protocol["data"]["folds"]), args.fold_limit)
    predictions = {}
    for group in protocol["paired_groups"]:
        group_id = int(group["group"])
        selection_seed = int(group["random_selection_seed"])
        fold_seeds = [int(value) for value in group["fold_model_seeds"]]
        arms = {
            "RANDOM": random_file[f"selected_K1_S{selection_seed}"],
            "WINNER": winner_file[f"selected_{winner}"],
        }
        for arm, selected_by_fold in arms.items():
            key = f"G{group_id}_{arm}"
            oof = np.full(len(rows), -1, dtype=np.int64)
            for fold in range(fold_count):
                train_indices = np.flatnonzero(folds != fold)
                eval_indices = np.flatnonzero(folds == fold)
                prediction, _, row_indices = screen.fit_fold(
                    args.dataset_root,
                    rows,
                    train_indices,
                    eval_indices,
                    selected_by_fold[fold],
                    settings,
                    fold_seeds[fold],
                    key,
                )
                oof[row_indices] = prediction
            predictions[key] = oof

    complete = fold_count == int(protocol["data"]["folds"])
    summary = {
        "experiment_id": protocol["experiment_id"],
        "winner": winner,
        "run_mode": "FORMAL" if complete else "SMOKE",
        "folds_completed": fold_count,
        "epochs": settings["epochs"],
        "winner_selection_sha256": sha256_file(args.winner_selections),
        "random_selection_sha256": sha256_file(args.random_selections),
        "official_test_images_decoded_or_encoded": 0,
    }
    if complete:
        group_results = []
        class_deltas = []
        for group in protocol["paired_groups"]:
            group_id = int(group["group"])
            random_prediction = predictions[f"G{group_id}_RANDOM"]
            winner_prediction = predictions[f"G{group_id}_WINNER"]
            random_recall = screen.class_recall(labels, random_prediction)
            winner_recall = screen.class_recall(labels, winner_prediction)
            paired_class_delta = winner_recall - random_recall
            class_deltas.append(paired_class_delta)
            random_negative = float(np.mean((random_recall-global_recall) < 0))
            winner_negative = float(np.mean((winner_recall-global_recall) < 0))
            group_results.append(
                {
                    "group": group_id,
                    "random_oof_ba": screen.balanced_accuracy(
                        labels, random_prediction
                    ),
                    "winner_oof_ba": screen.balanced_accuracy(
                        labels, winner_prediction
                    ),
                    "paired_ba_improvement_pp": 100
                    * float(paired_class_delta.mean()),
                    "random_negative_transfer_class_rate": random_negative,
                    "winner_negative_transfer_class_rate": winner_negative,
                    "negative_transfer_rate_change_pp": 100
                    * (winner_negative - random_negative),
                    "class_bootstrap_95_interval": bootstrap_interval(
                        paired_class_delta,
                        int(
                            protocol["confirmation_gate"]["bootstrap"][
                                "replicates"
                            ]
                        ),
                        int(
                            protocol["confirmation_gate"]["bootstrap"]["seed"]
                        )
                        + group_id,
                    ),
                }
            )
        paired_ba = np.asarray(
            [value["paired_ba_improvement_pp"] for value in group_results]
        )
        negative_change = np.asarray(
            [
                value["negative_transfer_rate_change_pp"]
                for value in group_results
            ]
        )
        gate = protocol["confirmation_gate"]
        benefit = gate["benefit_branch"]
        safety = gate["safety_branch"]
        benefit_pass = (
            paired_ba.mean()
            >= benefit["minimum_mean_paired_ba_improvement_pp"]
            and int(np.sum(paired_ba > 0))
            >= benefit["minimum_positive_groups"]
            and negative_change.mean()
            <= 100 * benefit["maximum_mean_negative_transfer_rate_increase"]
        )
        safety_positive = (negative_change < 0)
        safety_pass = (
            paired_ba.mean() >= -safety["maximum_mean_ba_deficit_pp"]
            and -negative_change.mean()
            >= safety["minimum_negative_transfer_rate_reduction_pp"]
            and int(np.sum(safety_positive))
            >= safety["minimum_safety_positive_groups"]
        )
        mean_class_delta = np.stack(class_deltas).mean(axis=0)
        summary.update(
            {
                "groups": group_results,
                "mean_paired_ba_improvement_pp": float(paired_ba.mean()),
                "mean_negative_transfer_rate_change_pp": float(
                    negative_change.mean()
                ),
                "positive_ba_groups": int(np.sum(paired_ba > 0)),
                "safety_positive_groups": int(np.sum(safety_positive)),
                "aggregate_class_bootstrap_95_interval": bootstrap_interval(
                    mean_class_delta,
                    int(gate["bootstrap"]["replicates"]),
                    int(gate["bootstrap"]["seed"]),
                ),
                "benefit_branch_pass": benefit_pass,
                "safety_branch_pass": safety_pass,
                "overall_gate_pass": benefit_pass or safety_pass,
                "next_stage": (
                    "PAT-E-260728-001"
                    if benefit_pass or safety_pass
                    else "STOP_BEFORE_CCT_AND_FINAL_TEST"
                ),
            }
        )
    else:
        summary["prediction_counts"] = {
            key: int(np.sum(value >= 0))
            for key, value in predictions.items()
        }
        summary["gate_evaluated"] = False

    args.output_dir.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        args.output_dir / "cub_active_confirmation_predictions.npz",
        labels=labels,
        global_predictions=global_prediction,
        **{
            f"{key}_predictions": value
            for key, value in predictions.items()
        },
    )
    (args.output_dir / "cub_active_confirmation_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
