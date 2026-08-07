#!/usr/bin/env python3
"""Five-fold train-only selection for the Global/Full-Part Oracle gate."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import statistics
from itertools import product
from pathlib import Path

import numpy as np
import torch
from sklearn.metrics import balanced_accuracy_score

from train_utils import fit_head, per_class_recall


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--features", type=Path, required=True)
    parser.add_argument("--targets", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def evaluate_candidate(
    global_features: torch.Tensor,
    patch_features: torch.Tensor,
    targets: torch.Tensor,
    labels: torch.Tensor,
    folds: np.ndarray,
    classes: int,
    settings: dict,
) -> dict:
    oof_predictions = np.full(len(labels), -1, dtype=np.int64)
    best_epochs = []
    for fold in range(5):
        train_indices = np.flatnonzero(folds != fold)
        eval_indices = np.flatnonzero(folds == fold)
        result = fit_head(
            global_features=global_features,
            patch_features=patch_features,
            targets=targets,
            labels=labels,
            train_indices=train_indices,
            eval_indices=eval_indices,
            classes=classes,
            learning_rate=settings["learning_rate"],
            weight_decay=settings["weight_decay"],
            maximum_epochs=settings["maximum_epochs"],
            patience=settings["patience"],
            batch_size=settings["batch_size"],
            seed=1307 + fold,
            part_loss_weight=settings.get("part_loss_weight", 0.0),
            gamma=settings.get("gamma", 0.0),
        )
        oof_predictions[eval_indices] = result.predictions
        best_epochs.append(result.best_epoch)
    if (oof_predictions < 0).any():
        raise RuntimeError("OOF predictions are incomplete.")
    actual = labels.detach().cpu().numpy()
    return {
        "balanced_accuracy": float(
            balanced_accuracy_score(actual, oof_predictions)
        ),
        "per_class_recall": per_class_recall(
            actual, oof_predictions, classes
        ).tolist(),
        "best_epochs": best_epochs,
        "selected_epoch": int(round(statistics.median(best_epochs))),
        "predictions": oof_predictions,
    }


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    rows = [
        json.loads(line)
        for line in args.manifest.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    feature_arrays = np.load(args.features)
    target_arrays = np.load(args.targets)
    global_features = torch.from_numpy(
        feature_arrays["global_features"].astype(np.float32)
    ).cuda()
    patch_features = torch.from_numpy(feature_arrays["patch_features"]).cuda()
    targets = torch.from_numpy(target_arrays["masks"]).cuda()
    labels = torch.tensor(
        [row["class_index"] for row in rows], dtype=torch.long, device="cuda"
    )
    folds = np.asarray([row["fold"] for row in rows], dtype=np.int64)
    classes = len({int(value) for value in labels})
    grid = protocol["candidate_grid"]
    common = {
        "maximum_epochs": int(grid["maximum_epochs"]),
        "patience": int(grid["early_stopping_patience"]),
        "batch_size": int(grid["batch_size"]),
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    result_rows: list[dict] = []

    global_candidates = []
    for learning_rate, weight_decay in product(
        grid["classification_learning_rate"], grid["weight_decay"]
    ):
        settings = {
            **common,
            "learning_rate": float(learning_rate),
            "weight_decay": float(weight_decay),
        }
        result = evaluate_candidate(
            global_features,
            patch_features,
            targets,
            labels,
            folds,
            classes,
            settings,
        )
        record = {
            "arm": "GLOBAL",
            **settings,
            "part_loss_weight": 0.0,
            "gamma": 0.0,
            "balanced_accuracy": result["balanced_accuracy"],
            "worst_class_delta_vs_global": 0.0,
            "selected_epoch": result["selected_epoch"],
        }
        result_rows.append(record)
        global_candidates.append((record, result))
        print(json.dumps(record, sort_keys=True), flush=True)

    global_candidates.sort(
        key=lambda pair: (
            -pair[0]["balanced_accuracy"],
            pair[0]["learning_rate"],
            -pair[0]["weight_decay"],
        )
    )
    selected_global, global_result = global_candidates[0]

    oracle_candidates = []
    for part_loss_weight, gamma in product(
        grid["part_loss_weight"], grid["gamma"]
    ):
        settings = {
            **common,
            "learning_rate": selected_global["learning_rate"],
            "weight_decay": selected_global["weight_decay"],
            "part_loss_weight": float(part_loss_weight),
            "gamma": float(gamma),
        }
        result = evaluate_candidate(
            global_features,
            patch_features,
            targets,
            labels,
            folds,
            classes,
            settings,
        )
        deltas = (
            np.asarray(result["per_class_recall"])
            - np.asarray(global_result["per_class_recall"])
        )
        record = {
            "arm": "FULL_PART_ORACLE",
            **settings,
            "balanced_accuracy": result["balanced_accuracy"],
            "gain_vs_global": result["balanced_accuracy"]
            - global_result["balanced_accuracy"],
            "worst_class_delta_vs_global": float(deltas.min()),
            "selected_epoch": result["selected_epoch"],
            "safety_feasible": bool(deltas.min() >= -0.02),
        }
        result_rows.append(record)
        oracle_candidates.append((record, result))
        print(json.dumps(record, sort_keys=True), flush=True)

    feasible = [pair for pair in oracle_candidates if pair[0]["safety_feasible"]]
    ranking_pool = feasible if feasible else oracle_candidates
    ranking_pool.sort(
        key=lambda pair: (
            -pair[0]["balanced_accuracy"],
            pair[0]["gamma"],
            pair[0]["part_loss_weight"],
        )
    )
    selected_oracle, oracle_result = ranking_pool[0]

    csv_path = args.output_dir / "oracle_oof_grid.csv"
    fields = sorted({key for row in result_rows for key in row})
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(result_rows)
    np.savez(
        args.output_dir / "oracle_oof_predictions.npz",
        labels=labels.detach().cpu().numpy(),
        global_predictions=global_result["predictions"],
        oracle_predictions=oracle_result["predictions"],
        folds=folds,
    )
    selection = {
        "experiment_id": protocol["experiment_id"],
        "selection_data": "train-only five-fold OOF",
        "protocol_sha256": sha256_file(args.protocol),
        "manifest_sha256": sha256_file(args.manifest),
        "selected_global": selected_global,
        "selected_oracle": selected_oracle,
        "oracle_constraint_feasible_candidates": len(feasible),
        "validation_read_before_selection": False,
        "test_images_encoded": 0,
    }
    output = args.output_dir / "selected_oracle_hparams.json"
    output.write_text(
        json.dumps(selection, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(selection, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
