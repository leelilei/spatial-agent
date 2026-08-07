#!/usr/bin/env python3
"""Fit frozen train-selected Global/Oracle heads and evaluate validation once."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np
import torch
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    f1_score,
)

from train_utils import fit_fixed_head, per_class_recall, predict_head


def load_rows(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-manifest", type=Path, required=True)
    parser.add_argument("--train-features", type=Path, required=True)
    parser.add_argument("--train-targets", type=Path, required=True)
    parser.add_argument("--val-manifest", type=Path, required=True)
    parser.add_argument("--val-features", type=Path, required=True)
    parser.add_argument("--selected-hparams", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def metrics(labels: np.ndarray, predictions: np.ndarray) -> dict:
    return {
        "balanced_accuracy": float(
            balanced_accuracy_score(labels, predictions)
        ),
        "macro_f1": float(
            f1_score(labels, predictions, average="macro", zero_division=0)
        ),
        "top1_accuracy": float(accuracy_score(labels, predictions)),
    }


def main() -> None:
    args = parse_args()
    train_rows = load_rows(args.train_manifest)
    val_rows = load_rows(args.val_manifest)
    train_arrays = np.load(args.train_features)
    val_arrays = np.load(args.val_features)
    target_arrays = np.load(args.train_targets)
    train_global = torch.from_numpy(
        train_arrays["global_features"].astype(np.float32)
    ).cuda()
    train_patch = torch.from_numpy(train_arrays["patch_features"]).cuda()
    train_targets = torch.from_numpy(target_arrays["masks"]).cuda()
    train_labels = torch.tensor(
        [row["class_index"] for row in train_rows],
        dtype=torch.long,
        device="cuda",
    )
    val_global = torch.from_numpy(
        val_arrays["global_features"].astype(np.float32)
    ).cuda()
    val_patch = torch.from_numpy(val_arrays["patch_features"]).cuda()
    val_labels = torch.tensor(
        [row["class_index"] for row in val_rows],
        dtype=torch.long,
        device="cuda",
    )
    classes = int(train_labels.max().item() + 1)
    selection = json.loads(args.selected_hparams.read_text(encoding="utf-8"))
    global_hp = selection["selected_global"]
    oracle_hp = selection["selected_oracle"]

    args.output_dir.mkdir(parents=True, exist_ok=True)
    result_rows = []
    prediction_rows = []
    for seed in (1307, 2607, 5207):
        global_model = fit_fixed_head(
            train_global,
            train_patch,
            train_targets,
            train_labels,
            classes,
            learning_rate=global_hp["learning_rate"],
            weight_decay=global_hp["weight_decay"],
            epochs=global_hp["selected_epoch"],
            batch_size=global_hp["batch_size"],
            seed=seed,
        )
        global_predictions, actual = predict_head(
            global_model,
            val_global,
            val_patch,
            val_labels,
            np.arange(len(val_labels)),
            batch_size=global_hp["batch_size"],
            gamma=0.0,
        )
        del global_model
        torch.cuda.empty_cache()

        oracle_model = fit_fixed_head(
            train_global,
            train_patch,
            train_targets,
            train_labels,
            classes,
            learning_rate=oracle_hp["learning_rate"],
            weight_decay=oracle_hp["weight_decay"],
            epochs=oracle_hp["selected_epoch"],
            batch_size=oracle_hp["batch_size"],
            seed=seed,
            part_loss_weight=oracle_hp["part_loss_weight"],
            gamma=oracle_hp["gamma"],
        )
        oracle_predictions, _ = predict_head(
            oracle_model,
            val_global,
            val_patch,
            val_labels,
            np.arange(len(val_labels)),
            batch_size=oracle_hp["batch_size"],
            gamma=oracle_hp["gamma"],
        )
        del oracle_model
        torch.cuda.empty_cache()

        global_metrics = metrics(actual, global_predictions)
        oracle_metrics = metrics(actual, oracle_predictions)
        global_recall = per_class_recall(actual, global_predictions, classes)
        oracle_recall = per_class_recall(actual, oracle_predictions, classes)
        record = {
            "seed": seed,
            **{f"global_{key}": value for key, value in global_metrics.items()},
            **{f"oracle_{key}": value for key, value in oracle_metrics.items()},
            "oracle_gain_pp": 100.0
            * (
                oracle_metrics["balanced_accuracy"]
                - global_metrics["balanced_accuracy"]
            ),
            "oracle_worst_class_delta_pp": 100.0
            * float((oracle_recall - global_recall).min()),
        }
        result_rows.append(record)
        print(json.dumps(record, sort_keys=True), flush=True)
        for index, row in enumerate(val_rows):
            prediction_rows.append(
                {
                    "seed": seed,
                    "image_id": row["image_id"],
                    "synset": row["synset"],
                    "label": int(actual[index]),
                    "global_prediction": int(global_predictions[index]),
                    "oracle_prediction": int(oracle_predictions[index]),
                }
            )

    with (args.output_dir / "oracle_gate_predictions.csv").open(
        "w", encoding="utf-8", newline=""
    ) as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(prediction_rows[0].keys())
        )
        writer.writeheader()
        writer.writerows(prediction_rows)
    gains = [row["oracle_gain_pp"] for row in result_rows]
    summary = {
        "experiment_id": "PAT-C-260728-001",
        "stage": "FULL_PART_ORACLE feasibility gate",
        "per_seed": result_rows,
        "mean_oracle_gain_pp": float(np.mean(gains)),
        "std_oracle_gain_pp": float(np.std(gains, ddof=1)),
        "all_seed_gains_positive": all(gain > 0 for gain in gains),
        "go_threshold_pp": 2.0,
        "oracle_gate_pass": bool(
            np.mean(gains) >= 2.0 and all(gain > 0 for gain in gains)
        ),
        "validation_used_once_after_train_selection": True,
        "validation_masks_used_as_model_inputs": False,
        "test_images_decoded_or_encoded": 0,
    }
    (args.output_dir / "oracle_gate_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
