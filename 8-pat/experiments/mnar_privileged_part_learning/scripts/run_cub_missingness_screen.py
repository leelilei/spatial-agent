#!/usr/bin/env python3
"""Fixed-epoch CUB missing-keypoint screening experiment."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader

import run_cub_prpool_oof as base


MECHANISMS = ("MCAR", "MAR_X", "MNAR_Z", "SI_HARD")


class SelectedCUB(base.CUBTrainOnly):
    def __init__(self, root, rows, indices, training, seed, selected):
        super().__init__(root, rows, indices, training, seed)
        self.selected = selected

    def __getitem__(self, item):
        image, targets, label, row_index = super().__getitem__(item)
        return (
            image,
            targets,
            label,
            row_index,
            bool(self.selected[row_index]),
        )


def selected_auxiliary_loss(
    raw_attention, targets, selected, part_weight, reg_weight
):
    complement = raw_attention[:, 15].sigmoid().mean(dim=(-1, -2))
    loss = -reg_weight * (complement * (1 - complement)).mean()
    if selected.any():
        part_logits = raw_attention[selected, :15]
        part_targets = targets[selected]
        part_loss = torch.zeros((), device=raw_attention.device)
        for kernel in (1, 2, 3, 6):
            logits = F.max_pool2d(part_logits, kernel)
            expected = F.max_pool2d(part_targets, kernel)
            part_loss = part_loss + F.binary_cross_entropy_with_logits(
                logits, expected
            )
        loss = loss + part_weight * part_loss / 4
    return loss


def evaluate(model, loader):
    model.eval()
    predictions, labels, indices = [], [], []
    with torch.inference_mode():
        for images, _, target, row_index, _ in loader:
            images = images.cuda(non_blocking=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                logits, _ = model(images)
            predictions.append(logits.argmax(1).cpu().numpy())
            labels.append(target.numpy())
            indices.append(row_index.numpy())
    return (
        np.concatenate(predictions),
        np.concatenate(labels),
        np.concatenate(indices),
    )


def fit_fold(
    root,
    rows,
    train_indices,
    eval_indices,
    selected,
    settings,
    seed,
    mechanism,
):
    torch.manual_seed(seed)
    np.random.seed(seed)
    model = base.CUBModel(classes=200, use_prpool=True).cuda()
    train_dataset = SelectedCUB(
        root, rows, train_indices, training=True, seed=seed, selected=selected
    )
    eval_dataset = SelectedCUB(
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
            {
                "params": head_parameters,
                "lr": settings["head_learning_rate"],
            },
            {
                "params": backbone_parameters,
                "lr": settings["backbone_learning_rate"],
            },
        ],
        weight_decay=settings["weight_decay"],
    )
    for epoch in range(1, settings["epochs"] + 1):
        model.train()
        running_loss = 0.0
        annotated_seen = 0
        for images, targets, labels, _, annotated in train_loader:
            images = images.cuda(non_blocking=True)
            targets = targets.cuda(non_blocking=True)
            labels = labels.cuda(non_blocking=True)
            annotated = annotated.cuda(non_blocking=True)
            optimizer.zero_grad(set_to_none=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                logits, raw_attention = model(images)
                loss = F.cross_entropy(logits.float(), labels)
            loss = loss + selected_auxiliary_loss(
                raw_attention.float(),
                targets.float(),
                annotated,
                settings["part_loss_weight"],
                settings["regularizer_weight"],
            )
            loss.backward()
            optimizer.step()
            running_loss += float(loss.detach()) * len(labels)
            annotated_seen += int(annotated.sum())
        print(
            json.dumps(
                {
                    "mechanism": mechanism,
                    "fold_seed": seed,
                    "epoch": epoch,
                    "mean_train_loss": running_loss / len(train_dataset),
                    "annotated_seen": annotated_seen,
                },
                sort_keys=True,
            ),
            flush=True,
        )
    prediction, actual, row_indices = evaluate(model, eval_loader)
    del model
    torch.cuda.empty_cache()
    return prediction, actual, row_indices


def balanced_accuracy(labels, predictions):
    return float(
        np.mean(
            [
                np.mean(predictions[labels == class_index] == class_index)
                for class_index in range(200)
            ]
        )
    )


def class_recall(labels, predictions):
    return np.asarray(
        [
            np.mean(predictions[labels == class_index] == class_index)
            for class_index in range(200)
        ]
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
        raise RuntimeError("Stored PAT-D-260728-001 labels do not match manifest")

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
    for mechanism_index, mechanism in enumerate(MECHANISMS):
        selected_by_fold = selection_file[f"selected_{mechanism}"]
        oof = np.full(len(rows), -1, dtype=np.int64)
        for fold in range(5):
            train_indices = np.flatnonzero(folds != fold)
            eval_indices = np.flatnonzero(folds == fold)
            fold_seed = seed + 100 + fold
            prediction, _, row_indices = fit_fold(
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
    global_recall = class_recall(labels, global_prediction)
    mcar_recall = class_recall(labels, predictions["MCAR"])
    global_ba = balanced_accuracy(labels, global_prediction)
    mcar_ba = balanced_accuracy(labels, predictions["MCAR"])
    results = {
        "GLOBAL_STORED_REFERENCE": {
            "oof_ba": global_ba,
        },
        "FULL_KEYPOINT_ORACLE_STORED_REFERENCE": {
            "oof_ba": balanced_accuracy(labels, oracle_prediction),
        },
    }
    selection_bias_supported = False
    for mechanism in MECHANISMS:
        prediction = predictions[mechanism]
        recall = class_recall(labels, prediction)
        delta_global = recall - global_recall
        negative_rate = float(np.mean(delta_global < 0))
        ba = balanced_accuracy(labels, prediction)
        result = {
            "oof_ba": ba,
            "delta_pp_vs_global": 100 * (ba - global_ba),
            "delta_pp_vs_mcar": 100 * (ba - mcar_ba),
            "negative_transfer_class_rate_vs_global": negative_rate,
            "worst_class_delta_pp_vs_global": 100 * float(delta_global.min()),
        }
        if mechanism != "MCAR":
            negative_rate_gap = negative_rate - float(
                np.mean((mcar_recall - global_recall) < 0)
            )
            result[
                "negative_transfer_class_rate_gap_vs_mcar"
            ] = negative_rate_gap
            if result["delta_pp_vs_mcar"] <= -2.0 or negative_rate_gap >= 0.10:
                selection_bias_supported = True
        results[f"NAIVE_{mechanism}"] = result

    summary = {
        "experiment_id": protocol["experiment_id"],
        "screening_seed": seed,
        "fixed_epochs": settings["epochs"],
        "selection_bias_supported": selection_bias_supported,
        "gate_pass": selection_bias_supported,
        "official_test_images_decoded_or_encoded": 0,
        "results": results,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        args.output_dir / "cub_missingness_screen_predictions.npz",
        labels=labels,
        global_predictions=global_prediction,
        full_oracle_predictions=oracle_prediction,
        **{f"{key}_predictions": value for key, value in predictions.items()},
    )
    (args.output_dir / "cub_missingness_screen_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
