#!/usr/bin/env python3
"""Fixed-epoch severe CUB missing-keypoint screening experiment."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

import run_cub_missingness_screen as screen
import run_cub_prpool_oof as base


MECHANISMS = (
    "MCAR_1",
    "MAR_X_ATYPICAL",
    "MNAR_Z_INCOMPLETE",
    "SI_POSE",
)


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
        "epochs": 9,
    }
    predictions = {}
    seed = int(protocol["screening"]["seed"])
    for mechanism in MECHANISMS:
        selected_by_fold = selection_file[f"selected_{mechanism}"]
        oof = np.full(len(rows), -1, dtype=np.int64)
        for fold in range(5):
            train_indices = np.flatnonzero(folds != fold)
            eval_indices = np.flatnonzero(folds == fold)
            fold_seed = seed + 100 + fold
            prediction, _, row_indices = screen.fit_fold(
                args.dataset_root,
                rows,
                train_indices,
                eval_indices,
                selected_by_fold[fold],
                settings,
                fold_seed,
                mechanism,
            )
            oof[row_indices] = prediction
        if (oof < 0).any():
            raise RuntimeError(f"Incomplete OOF predictions for {mechanism}")
        predictions[mechanism] = oof

    global_prediction = reference["global_predictions"]
    oracle_prediction = reference["prpool_predictions"]
    global_recall = screen.class_recall(labels, global_prediction)
    mcar_recall = screen.class_recall(labels, predictions["MCAR_1"])
    global_ba = screen.balanced_accuracy(labels, global_prediction)
    mcar_ba = screen.balanced_accuracy(labels, predictions["MCAR_1"])
    mcar_negative_rate = float(np.mean((mcar_recall - global_recall) < 0))
    results = {
        "GLOBAL_STORED_REFERENCE": {"oof_ba": global_ba},
        "FULL_KEYPOINT_ORACLE_STORED_REFERENCE": {
            "oof_ba": screen.balanced_accuracy(labels, oracle_prediction)
        },
    }
    gate_pass = False
    for mechanism in MECHANISMS:
        prediction = predictions[mechanism]
        recall = screen.class_recall(labels, prediction)
        delta_global = recall - global_recall
        negative_rate = float(np.mean(delta_global < 0))
        ba = screen.balanced_accuracy(labels, prediction)
        result = {
            "oof_ba": ba,
            "delta_pp_vs_global": 100 * (ba - global_ba),
            "delta_pp_vs_mcar": 100 * (ba - mcar_ba),
            "negative_transfer_class_rate_vs_global": negative_rate,
            "worst_class_delta_pp_vs_global": 100 * float(
                delta_global.min()
            ),
        }
        if mechanism != "MCAR_1":
            gap = negative_rate - mcar_negative_rate
            result["negative_transfer_class_rate_gap_vs_mcar"] = gap
            if result["delta_pp_vs_mcar"] <= -2.0 or gap >= 0.10:
                gate_pass = True
        results[f"NAIVE_{mechanism}"] = result

    summary = {
        "experiment_id": protocol["experiment_id"],
        "screening_seed": seed,
        "fixed_epochs": settings["epochs"],
        "selection_bias_supported": gate_pass,
        "gate_pass": gate_pass,
        "official_test_images_decoded_or_encoded": 0,
        "results": results,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        args.output_dir / "cub_severe_missingness_screen_predictions.npz",
        labels=labels,
        global_predictions=global_prediction,
        full_oracle_predictions=oracle_prediction,
        **{
            f"{key}_predictions": value
            for key, value in predictions.items()
        },
    )
    (
        args.output_dir / "cub_severe_missingness_screen_summary.json"
    ).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
