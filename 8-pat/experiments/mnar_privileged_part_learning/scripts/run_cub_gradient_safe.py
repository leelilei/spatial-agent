#!/usr/bin/env python3
"""Run paired Random-K1 gradient-safety screening for PAT-D-260728-008."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader

import run_cub_missingness_screen as screen
import run_cub_prpool_oof as base
from gradient_safety import (
    assign_combined_gradients,
    protect_classification_gradient,
)


def evaluate(model, loader):
    return screen.evaluate(model, loader)


def fit_fold_safe(
    root,
    rows,
    train_indices,
    eval_indices,
    selected,
    settings,
    seed,
    arm,
):
    torch.manual_seed(seed)
    np.random.seed(seed)
    model = base.CUBModel(classes=200, use_prpool=True).cuda()
    train_dataset = screen.SelectedCUB(
        root, rows, train_indices, training=True, seed=seed, selected=selected
    )
    eval_dataset = screen.SelectedCUB(
        root, rows, eval_indices, training=False, seed=seed, selected=selected
    )
    generator = torch.Generator().manual_seed(seed)
    train_loader = DataLoader(
        train_dataset,
        batch_size=settings["batch_size"],
        shuffle=True,
        generator=generator,
        num_workers=8,
        pin_memory=True,
        persistent_workers=True,
    )
    eval_loader = DataLoader(
        eval_dataset,
        batch_size=settings["batch_size"],
        shuffle=False,
        num_workers=8,
        pin_memory=True,
        persistent_workers=True,
    )
    backbone_parameters = list(model.features.layer4.parameters())
    backbone_ids = {id(parameter) for parameter in backbone_parameters}
    head_parameters = [
        parameter
        for parameter in model.parameters()
        if parameter.requires_grad and id(parameter) not in backbone_ids
    ]
    optimizer = torch.optim.AdamW(
        [
            {"params": head_parameters, "lr": settings["head_learning_rate"]},
            {
                "params": backbone_parameters,
                "lr": settings["backbone_learning_rate"],
            },
        ],
        weight_decay=settings["weight_decay"],
    )
    parameters = [
        parameter for parameter in model.parameters() if parameter.requires_grad
    ]
    fold_batches = 0
    fold_conflicts = 0
    fold_cosines = []
    fold_dots_after = []
    for epoch in range(1, settings["epochs"] + 1):
        model.train()
        running_classification = 0.0
        running_auxiliary = 0.0
        annotated_seen = 0
        epoch_batches = 0
        epoch_conflicts = 0
        epoch_cosines = []
        epoch_dots_after = []
        for images, targets, labels, _, annotated in train_loader:
            images = images.cuda(non_blocking=True)
            targets = targets.cuda(non_blocking=True)
            labels = labels.cuda(non_blocking=True)
            annotated = annotated.cuda(non_blocking=True)
            optimizer.zero_grad(set_to_none=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                logits, raw_attention = model(images)
                classification_loss = F.cross_entropy(
                    logits.float(), labels
                )
            auxiliary_loss = screen.selected_auxiliary_loss(
                raw_attention.float(),
                targets.float(),
                annotated,
                settings["part_loss_weight"],
                settings["regularizer_weight"],
            )
            classification_gradients = torch.autograd.grad(
                classification_loss,
                parameters,
                retain_graph=True,
                allow_unused=True,
            )
            auxiliary_gradients = torch.autograd.grad(
                auxiliary_loss,
                parameters,
                allow_unused=True,
            )
            protected, diagnostics = protect_classification_gradient(
                classification_gradients, auxiliary_gradients
            )
            assign_combined_gradients(
                parameters, classification_gradients, protected
            )
            optimizer.step()
            count = len(labels)
            running_classification += float(
                classification_loss.detach()
            ) * count
            running_auxiliary += float(auxiliary_loss.detach()) * count
            annotated_seen += int(annotated.sum())
            epoch_batches += 1
            epoch_conflicts += int(diagnostics.conflict)
            epoch_cosines.append(diagnostics.cosine_before)
            epoch_dots_after.append(diagnostics.dot_after)
        fold_batches += epoch_batches
        fold_conflicts += epoch_conflicts
        fold_cosines.extend(epoch_cosines)
        fold_dots_after.extend(epoch_dots_after)
        print(
            json.dumps(
                {
                    "arm": arm,
                    "fold_seed": seed,
                    "epoch": epoch,
                    "mean_classification_loss": (
                        running_classification / len(train_dataset)
                    ),
                    "mean_auxiliary_loss": (
                        running_auxiliary / len(train_dataset)
                    ),
                    "annotated_seen": annotated_seen,
                    "gradient_conflict_fraction": (
                        epoch_conflicts / epoch_batches
                    ),
                    "mean_gradient_cosine_before": float(
                        np.mean(epoch_cosines)
                    ),
                    "max_abs_dot_after_projection": float(
                        np.max(np.abs(epoch_dots_after))
                    ),
                },
                sort_keys=True,
            ),
            flush=True,
        )
    prediction, actual, row_indices = evaluate(model, eval_loader)
    diagnostics = {
        "arm": arm,
        "fold_seed": seed,
        "batches": fold_batches,
        "conflicting_batches": fold_conflicts,
        "gradient_conflict_fraction": fold_conflicts / fold_batches,
        "mean_gradient_cosine_before": float(np.mean(fold_cosines)),
        "max_abs_dot_after_projection": float(
            np.max(np.abs(fold_dots_after))
        ),
    }
    del model
    torch.cuda.empty_cache()
    return prediction, actual, row_indices, diagnostics


def bootstrap_interval(values, replicates, seed):
    values = np.asarray(values, dtype=np.float64)
    rng = np.random.default_rng(seed)
    draws = rng.integers(0, len(values), size=(replicates, len(values)))
    means = values[draws].mean(axis=1)
    return {
        "lower_95_pp": 100 * float(np.quantile(means, 0.025)),
        "upper_95_pp": 100 * float(np.quantile(means, 0.975)),
    }


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--selections", type=Path, required=True)
    parser.add_argument("--stored-reference", type=Path, required=True)
    parser.add_argument("--naive-reference", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--oracle-protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--fold-limit", type=int, default=5)
    parser.add_argument("--epoch-limit", type=int, default=9)
    parser.add_argument("--selection-seeds", nargs="+", type=int)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    oracle_protocol = json.loads(args.oracle_protocol.read_text())
    rows = [json.loads(line) for line in args.manifest.read_text().splitlines()]
    if any(
        row["split"] != "train" or row["source_split"] != "official_train"
        for row in rows
    ):
        raise RuntimeError("PAT-D-260728-008 may decode official train only")
    labels = np.asarray([row["class_index"] for row in rows])
    folds = np.asarray([row["fold"] for row in rows])
    selection_file = np.load(args.selections)
    stored_reference = np.load(args.stored_reference)
    naive_reference = np.load(args.naive_reference)
    if not np.array_equal(labels, stored_reference["labels"]):
        raise RuntimeError("Stored reference labels do not match manifest")
    if not np.array_equal(labels, naive_reference["labels"]):
        raise RuntimeError("Naive reference labels do not match manifest")
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
    selection_seeds = (
        args.selection_seeds
        or [int(seed) for seed in protocol["data"]["random_selection_seeds"]]
    )
    allowed = set(protocol["data"]["random_selection_seeds"])
    if not set(selection_seeds) <= allowed:
        raise RuntimeError("Unregistered selection seed requested")
    fold_seeds = [int(seed) for seed in protocol["training"]["fold_seeds"]]
    fold_count = min(int(protocol["data"]["folds"]), args.fold_limit)
    predictions = {}
    training_diagnostics = []
    for selection_seed in selection_seeds:
        arm = f"SAFE_K1_S{selection_seed}"
        selected_by_fold = selection_file[
            f"selected_K1_S{selection_seed}"
        ]
        oof = np.full(len(rows), -1, dtype=np.int64)
        for fold in range(fold_count):
            prediction, _, row_indices, diagnostics = fit_fold_safe(
                args.dataset_root,
                rows,
                np.flatnonzero(folds != fold),
                np.flatnonzero(folds == fold),
                selected_by_fold[fold],
                settings,
                fold_seeds[fold],
                arm,
            )
            oof[row_indices] = prediction
            diagnostics["fold"] = fold
            diagnostics["selection_seed"] = selection_seed
            training_diagnostics.append(diagnostics)
        predictions[arm] = oof
    complete = (
        fold_count == int(protocol["data"]["folds"])
        and set(selection_seeds) == allowed
    )
    global_prediction = stored_reference["global_predictions"]
    global_recall = screen.class_recall(labels, global_prediction)
    summary = {
        "experiment_id": protocol["experiment_id"],
        "run_mode": "FORMAL" if complete else "SMOKE",
        "folds_completed": fold_count,
        "epochs": settings["epochs"],
        "selection_seeds": selection_seeds,
        "official_test_images_decoded_or_encoded": 0,
        "training_diagnostics": training_diagnostics,
    }
    if complete:
        groups = []
        class_deltas = []
        for selection_seed in selection_seeds:
            naive = naive_reference[f"K1_S{selection_seed}_predictions"]
            safe = predictions[f"SAFE_K1_S{selection_seed}"]
            naive_recall = screen.class_recall(labels, naive)
            safe_recall = screen.class_recall(labels, safe)
            paired_class_delta = safe_recall - naive_recall
            class_deltas.append(paired_class_delta)
            naive_negative = float(
                np.mean((naive_recall - global_recall) < 0)
            )
            safe_negative = float(
                np.mean((safe_recall - global_recall) < 0)
            )
            groups.append(
                {
                    "selection_seed": selection_seed,
                    "naive_oof_ba": screen.balanced_accuracy(labels, naive),
                    "safe_oof_ba": screen.balanced_accuracy(labels, safe),
                    "paired_ba_improvement_pp": 100
                    * float(paired_class_delta.mean()),
                    "naive_negative_transfer_class_rate": naive_negative,
                    "safe_negative_transfer_class_rate": safe_negative,
                    "negative_transfer_rate_change_pp": 100
                    * (safe_negative - naive_negative),
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
                        + selection_seed,
                    ),
                }
            )
        paired_ba = np.asarray(
            [group["paired_ba_improvement_pp"] for group in groups]
        )
        negative_change = np.asarray(
            [group["negative_transfer_rate_change_pp"] for group in groups]
        )
        benefit = protocol["confirmation_gate"]["benefit_branch"]
        safety = protocol["confirmation_gate"]["safety_branch"]
        benefit_pass = (
            paired_ba.mean()
            >= benefit["minimum_mean_paired_ba_improvement_pp"]
            and int(np.sum(paired_ba > 0))
            >= benefit["minimum_positive_selection_seeds"]
            and negative_change.mean()
            <= benefit["maximum_mean_negative_transfer_rate_increase_pp"]
        )
        safety_pass = (
            paired_ba.mean() >= -safety["maximum_mean_ba_deficit_pp"]
            and -negative_change.mean()
            >= safety["minimum_mean_negative_transfer_rate_reduction_pp"]
            and int(np.sum(negative_change < 0))
            >= safety["minimum_safety_positive_selection_seeds"]
        )
        mean_class_delta = np.stack(class_deltas).mean(axis=0)
        summary.update(
            {
                "groups": groups,
                "mean_paired_ba_improvement_pp": float(paired_ba.mean()),
                "mean_negative_transfer_rate_change_pp": float(
                    negative_change.mean()
                ),
                "positive_ba_selection_seeds": int(np.sum(paired_ba > 0)),
                "safety_positive_selection_seeds": int(
                    np.sum(negative_change < 0)
                ),
                "aggregate_class_bootstrap_95_interval": bootstrap_interval(
                    mean_class_delta,
                    int(
                        protocol["confirmation_gate"]["bootstrap"][
                            "replicates"
                        ]
                    ),
                    int(
                        protocol["confirmation_gate"]["bootstrap"]["seed"]
                    ),
                ),
                "benefit_branch_pass": bool(benefit_pass),
                "safety_branch_pass": bool(safety_pass),
                "overall_gate_pass": bool(benefit_pass or safety_pass),
                "next_stage": (
                    "FREEZE_CCT20PLUS_ORACLE_AND_SAFETY_TRANSFER"
                    if benefit_pass or safety_pass
                    else "STOP_GRADIENT_SAFETY_MECHANISM"
                ),
            }
        )
    else:
        summary["gate_evaluated"] = False
        summary["prediction_counts"] = {
            arm: int(np.sum(values >= 0))
            for arm, values in predictions.items()
        }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        args.output_dir / "cub_gradient_safe_predictions.npz",
        labels=labels,
        global_predictions=global_prediction,
        **{
            f"{arm}_predictions": values
            for arm, values in predictions.items()
        },
    )
    (args.output_dir / "cub_gradient_safe_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
