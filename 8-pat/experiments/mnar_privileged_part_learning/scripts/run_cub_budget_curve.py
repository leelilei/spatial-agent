#!/usr/bin/env python3
"""Run the frozen CUB sparse-keypoint budget-response experiment."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

import run_cub_missingness_screen as screen


BUDGETS = (1, 2, 4)


def arm_name(budget, seed):
    return f"K{budget}_S{seed}"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--selections", type=Path, required=True)
    parser.add_argument("--stored-reference", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--oracle-protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    oracle_protocol = json.loads(args.oracle_protocol.read_text())
    rows = [json.loads(line) for line in args.manifest.read_text().splitlines()]
    labels = np.asarray([row["class_index"] for row in rows])
    folds = np.asarray([row["fold"] for row in rows])
    selection_file = np.load(args.selections)
    reference = np.load(args.stored_reference)
    if not np.array_equal(labels, reference["labels"]):
        raise RuntimeError("Stored reference labels do not match manifest")

    raw = oracle_protocol["optimization"]
    settings = {
        "head_learning_rate": raw["head_learning_rate"],
        "backbone_learning_rate": raw["backbone_learning_rate"],
        "weight_decay": raw["weight_decay"],
        "part_loss_weight": raw["part_loss_weight"],
        "regularizer_weight": raw["complementary_regularizer_weight"],
        "batch_size": raw["batch_size"],
        "epochs": int(protocol["training"]["fixed_epochs"]),
    }
    seeds = [int(value) for value in protocol["sampling"]["selection_seeds"]]
    fold_seeds = [
        int(value)
        for value in protocol["training"][
            "fold_seeds_shared_across_all_budget_arms"
        ]
    ]
    predictions = {}
    arm_order = [
        arm_name(budget, seed) for budget in BUDGETS for seed in seeds
    ]
    for arm in arm_order:
        selected_by_fold = selection_file[f"selected_{arm}"]
        oof = np.full(len(rows), -1, dtype=np.int64)
        for fold in range(5):
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
                arm,
            )
            oof[row_indices] = prediction
        if (oof < 0).any():
            raise RuntimeError(f"Incomplete OOF predictions for {arm}")
        predictions[arm] = oof

    global_prediction = reference["global_predictions"]
    oracle_prediction = reference["prpool_predictions"]
    global_ba = screen.balanced_accuracy(labels, global_prediction)
    oracle_ba = screen.balanced_accuracy(labels, oracle_prediction)
    global_recall = screen.class_recall(labels, global_prediction)
    oracle_gain = oracle_ba - global_ba
    arms = {}
    aggregates = {}
    for budget in BUDGETS:
        budget_values = []
        for seed in seeds:
            arm = arm_name(budget, seed)
            prediction = predictions[arm]
            ba = screen.balanced_accuracy(labels, prediction)
            recall = screen.class_recall(labels, prediction)
            delta = recall - global_recall
            budget_values.append(ba)
            arms[arm] = {
                "budget_per_class": budget,
                "selection_seed": seed,
                "oof_ba": ba,
                "delta_pp_vs_global": 100 * (ba - global_ba),
                "retained_oracle_gain_fraction": (
                    (ba - global_ba) / oracle_gain
                ),
                "negative_transfer_class_rate_vs_global": float(
                    np.mean(delta < 0)
                ),
                "worst_class_delta_pp_vs_global": 100 * float(delta.min()),
            }
        values = np.asarray(budget_values)
        aggregates[f"K{budget}"] = {
            "mean_oof_ba": float(values.mean()),
            "sample_std_oof_ba": float(values.std(ddof=1)),
            "min_oof_ba": float(values.min()),
            "max_oof_ba": float(values.max()),
            "range_pp": 100 * float(values.max() - values.min()),
            "mean_delta_pp_vs_global": 100
            * float(values.mean() - global_ba),
            "mean_retained_oracle_gain_fraction": float(
                (values.mean() - global_ba) / oracle_gain
            ),
        }

    k1 = aggregates["K1"]
    sparse_value_gate = (
        k1["mean_retained_oracle_gain_fraction"] >= 0.60
        and all(
            arms[arm_name(1, seed)]["delta_pp_vs_global"] >= 2.0
            for seed in seeds
        )
    )
    robustness_gate = k1["range_pp"] <= 2.0
    summary = {
        "experiment_id": protocol["experiment_id"],
        "fixed_epochs": settings["epochs"],
        "stored_global_oof_ba": global_ba,
        "stored_full_oracle_oof_ba": oracle_ba,
        "stored_oracle_gain_pp": 100 * oracle_gain,
        "sparse_annotation_value_gate_pass": sparse_value_gate,
        "selection_robustness_gate_pass": robustness_gate,
        "overall_gate_pass": sparse_value_gate and robustness_gate,
        "official_test_images_decoded_or_encoded": 0,
        "arms": arms,
        "aggregates": aggregates,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        args.output_dir / "cub_budget_curve_predictions.npz",
        labels=labels,
        global_predictions=global_prediction,
        full_oracle_predictions=oracle_prediction,
        **{
            f"{key}_predictions": value
            for key, value in predictions.items()
        },
    )
    (args.output_dir / "cub_budget_curve_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
