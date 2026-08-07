#!/usr/bin/env python3
"""Run and automatically gate PAT-D-260728-005."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

import run_cub_missingness_screen as screen
from cub_active_selection import STRATEGIES, sha256_file


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--selections", type=Path, required=True)
    parser.add_argument("--stored-reference", type=Path, required=True)
    parser.add_argument("--random-reference", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--oracle-protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--fold-limit", type=int, default=5)
    parser.add_argument("--epoch-limit", type=int, default=9)
    parser.add_argument("--strategies", nargs="+", choices=STRATEGIES)
    return parser.parse_args()


def branch_status(ba, negative_rate, gate):
    benefit = gate["benefit_branch"]
    safety = gate["safety_branch"]
    benefit_pass = (
        ba >= benefit["minimum_oof_ba"]
        and negative_rate
        <= benefit["maximum_negative_transfer_class_rate"]
    )
    safety_pass = (
        ba >= safety["minimum_oof_ba"]
        and negative_rate
        <= safety["maximum_negative_transfer_class_rate"]
    )
    return benefit_pass, safety_pass


def choose_winner(results):
    benefit = [
        (name, value)
        for name, value in results.items()
        if value["benefit_branch_pass"]
    ]
    if benefit:
        benefit.sort(
            key=lambda item: (
                -item[1]["oof_ba"],
                item[1]["negative_transfer_class_rate_vs_global"],
                -item[1]["worst_class_delta_pp_vs_global"],
                item[0],
            )
        )
        return benefit[0][0], "BENEFIT"
    safety = [
        (name, value)
        for name, value in results.items()
        if value["safety_branch_pass"]
    ]
    if safety:
        safety.sort(
            key=lambda item: (
                item[1]["negative_transfer_class_rate_vs_global"],
                -item[1]["oof_ba"],
                -item[1]["worst_class_delta_pp_vs_global"],
                item[0],
            )
        )
        return safety[0][0], "SAFETY"
    return None, None


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    oracle_protocol = json.loads(args.oracle_protocol.read_text())
    rows = [json.loads(line) for line in args.manifest.read_text().splitlines()]
    if any(
        row["split"] != "train" or row["source_split"] != "official_train"
        for row in rows
    ):
        raise RuntimeError("PAT-D-260728-005 may decode official train only")
    labels = np.asarray([row["class_index"] for row in rows])
    folds = np.asarray([row["fold"] for row in rows])
    selection_file = np.load(args.selections)
    reference = np.load(args.stored_reference)
    random_reference = np.load(args.random_reference)
    if not np.array_equal(labels, reference["labels"]):
        raise RuntimeError("Stored reference labels do not match manifest")
    if not np.array_equal(labels, random_reference["labels"]):
        raise RuntimeError("Random reference labels do not match manifest")

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
    strategies = args.strategies or list(STRATEGIES)
    fold_seeds = [int(v) for v in protocol["training"]["fold_seeds"]]
    fold_count = min(int(protocol["data"]["folds"]), args.fold_limit)
    predictions = {}
    for strategy in strategies:
        selected_by_fold = selection_file[f"selected_{strategy}"]
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
                strategy,
            )
            oof[row_indices] = prediction
        predictions[strategy] = oof

    complete = fold_count == int(protocol["data"]["folds"])
    global_prediction = reference["global_predictions"]
    summary = {
        "experiment_id": protocol["experiment_id"],
        "run_mode": "FORMAL" if complete else "SMOKE",
        "folds_completed": fold_count,
        "epochs": settings["epochs"],
        "strategies": strategies,
        "selection_sha256": sha256_file(args.selections),
        "official_test_images_decoded_or_encoded": 0,
    }
    if complete:
        global_ba = screen.balanced_accuracy(labels, global_prediction)
        global_recall = screen.class_recall(labels, global_prediction)
        results = {}
        for strategy, prediction in predictions.items():
            recall = screen.class_recall(labels, prediction)
            delta = recall - global_recall
            ba = screen.balanced_accuracy(labels, prediction)
            negative_rate = float(np.mean(delta < 0))
            benefit_pass, safety_pass = branch_status(
                ba, negative_rate, protocol["screening_gate"]
            )
            results[strategy] = {
                "oof_ba": ba,
                "delta_pp_vs_global": 100 * (ba - global_ba),
                "negative_transfer_class_rate_vs_global": negative_rate,
                "worst_class_delta_pp_vs_global": 100 * float(delta.min()),
                "benefit_branch_pass": benefit_pass,
                "safety_branch_pass": safety_pass,
                "overall_gate_pass": benefit_pass or safety_pass,
            }
        winner, branch = choose_winner(results)
        random_names = [
            f"K1_S{seed}_predictions"
            for seed in protocol["controls"][
                "random_reference_selection_seeds"
            ]
        ]
        random_metrics = []
        for name in random_names:
            prediction = random_reference[name]
            delta = screen.class_recall(labels, prediction) - global_recall
            random_metrics.append(
                {
                    "arm": name.replace("_predictions", ""),
                    "oof_ba": screen.balanced_accuracy(labels, prediction),
                    "negative_transfer_class_rate_vs_global": float(
                        np.mean(delta < 0)
                    ),
                    "worst_class_delta_pp_vs_global": 100
                    * float(delta.min()),
                }
            )
        summary.update(
            {
                "stored_global_oof_ba": global_ba,
                "random_k1_reference": random_metrics,
                "results": results,
                "overall_gate_pass": winner is not None,
                "winner": winner,
                "winner_branch": branch,
                "next_stage": (
                    "PAT-D-260728-006"
                    if winner is not None
                    else "STOP_BEFORE_CONFIRMATION_AND_FINAL_TEST"
                ),
            }
        )
    else:
        summary.update(
            {
                "prediction_counts": {
                    name: int(np.sum(values >= 0))
                    for name, values in predictions.items()
                },
                "gate_evaluated": False,
            }
        )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        args.output_dir / "cub_active_selection_predictions.npz",
        labels=labels,
        global_predictions=global_prediction,
        **{
            f"{name}_predictions": values
            for name, values in predictions.items()
        },
    )
    (args.output_dir / "cub_active_selection_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
