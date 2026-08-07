#!/usr/bin/env python3
"""Train-only mechanism gate for a Privileged-Pooling-inspired head."""

from __future__ import annotations

import argparse
import copy
import csv
import json
import statistics
from itertools import product
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import balanced_accuracy_score, recall_score


class PatchAverageHead(nn.Module):
    def __init__(self, patch_dim: int, classes: int):
        super().__init__()
        self.classifier = nn.Linear(patch_dim, classes)

    def forward(self, patches: torch.Tensor):
        return self.classifier(patches.mean(dim=1)), None


class PrivilegedPoolingHead(nn.Module):
    def __init__(self, patch_dim: int, classes: int):
        super().__init__()
        self.attention = nn.Sequential(
            nn.Conv2d(patch_dim, 256, 3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 5, 3, padding=1),
        )
        self.classifier = nn.Linear(5 * patch_dim, classes)

    def forward(self, patches: torch.Tensor):
        batch, tokens, dimension = patches.shape
        if tokens != 196:
            raise RuntimeError(f"Expected 196 patch tokens, got {tokens}")
        feature_map = patches.transpose(1, 2).reshape(batch, dimension, 14, 14)
        raw_attention = self.attention(feature_map)
        attention = raw_attention.sigmoid()
        pooled = (
            feature_map[:, None, ...] * attention[:, :, None, ...]
        ).mean(dim=(-1, -2))
        pooled = F.normalize(pooled, p=2, dim=-1)
        return self.classifier(pooled.flatten(1)), (attention, raw_attention)


def class_weights(labels: torch.Tensor, classes: int) -> torch.Tensor:
    counts = torch.bincount(labels, minlength=classes).float().clamp_min(1)
    return counts.sum() / (classes * counts)


def attention_loss(
    raw_attention: torch.Tensor,
    targets: torch.Tensor,
    part_weight: float,
    regularizer_weight: float,
) -> torch.Tensor:
    supervised_logits = raw_attention[:, :4]
    loss = torch.zeros((), device=raw_attention.device)
    for kernel in (1, 2, 4, 7):
        predicted_logits = F.max_pool2d(
            supervised_logits, kernel_size=kernel
        )
        expected = F.max_pool2d(targets, kernel_size=kernel)
        loss = loss + F.binary_cross_entropy_with_logits(
            predicted_logits, expected
        )
    loss = part_weight * loss / 4.0
    complement_mean = raw_attention[:, 4].sigmoid().mean(dim=(-1, -2))
    variance = complement_mean * (1.0 - complement_mean)
    return loss - regularizer_weight * variance.mean()


def predict(model, patches, labels, indices, batch_size):
    model.eval()
    predicted, actual = [], []
    with torch.inference_mode():
        for chunk in np.array_split(
            indices, max(1, int(np.ceil(len(indices) / batch_size)))
        ):
            index = torch.as_tensor(chunk, device=patches.device)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                logits, _ = model(patches[index])
            predicted.append(logits.argmax(1).cpu().numpy())
            actual.append(labels[index].cpu().numpy())
    return np.concatenate(predicted), np.concatenate(actual)


def fit_fold(
    patches,
    targets,
    labels,
    train_indices,
    eval_indices,
    settings,
    classes,
    seed,
):
    torch.manual_seed(seed)
    use_attention = settings["arm"] == "PRPOOL_ORACLE"
    model = (
        PrivilegedPoolingHead(patches.shape[-1], classes)
        if use_attention
        else PatchAverageHead(patches.shape[-1], classes)
    ).cuda()
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=settings["learning_rate"],
        weight_decay=settings["weight_decay"],
    )
    train_index = torch.as_tensor(train_indices, device=patches.device)
    weights = class_weights(labels[train_index], classes)
    generator = torch.Generator(device=patches.device).manual_seed(seed)
    best_metric, best_epoch, best_state, stale = -1.0, 0, None, 0
    for epoch in range(1, settings["maximum_epochs"] + 1):
        model.train()
        order = train_index[
            torch.randperm(len(train_index), device=patches.device, generator=generator)
        ]
        for index in order.split(settings["batch_size"]):
            optimizer.zero_grad(set_to_none=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                logits, attention_output = model(patches[index])
                loss = F.cross_entropy(logits.float(), labels[index], weight=weights)
            if use_attention:
                _, raw_attention = attention_output
                loss = loss + attention_loss(
                    raw_attention.float(),
                    targets[index].float(),
                    settings["part_loss_weight"],
                    settings["regularizer_weight"],
                )
            loss.backward()
            optimizer.step()
        prediction, actual = predict(
            model, patches, labels, eval_indices, settings["batch_size"]
        )
        metric = balanced_accuracy_score(actual, prediction)
        if metric > best_metric + 1e-8:
            best_metric, best_epoch = float(metric), epoch
            best_state = copy.deepcopy(model.state_dict())
            stale = 0
        else:
            stale += 1
            if stale >= settings["patience"]:
                break
    model.load_state_dict(best_state)
    prediction, actual = predict(
        model, patches, labels, eval_indices, settings["batch_size"]
    )
    return prediction, actual, best_epoch


def evaluate(settings, patches, targets, labels, folds, classes):
    oof = np.full(len(labels), -1, dtype=np.int64)
    epochs = []
    for fold in range(5):
        train = np.flatnonzero(folds != fold)
        evaluate_on = np.flatnonzero(folds == fold)
        prediction, _, epoch = fit_fold(
            patches,
            targets,
            labels,
            train,
            evaluate_on,
            settings,
            classes,
            2607 + fold,
        )
        oof[evaluate_on] = prediction
        epochs.append(epoch)
    actual = labels.cpu().numpy()
    recall = recall_score(
        actual,
        oof,
        labels=np.arange(classes),
        average=None,
        zero_division=0,
    )
    return {
        "balanced_accuracy": float(balanced_accuracy_score(actual, oof)),
        "recall": recall,
        "predictions": oof,
        "selected_epoch": int(round(statistics.median(epochs))),
    }


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--features", type=Path, required=True)
    parser.add_argument("--targets", type=Path, required=True)
    parser.add_argument("--cls-oof", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    rows = [json.loads(line) for line in args.manifest.read_text().splitlines()]
    features = np.load(args.features)
    target_arrays = np.load(args.targets)
    patches = torch.from_numpy(features["patch_features"]).cuda()
    targets = torch.from_numpy(target_arrays["masks"]).cuda()
    labels = torch.tensor(
        [row["class_index"] for row in rows], device="cuda", dtype=torch.long
    )
    folds = np.asarray([row["fold"] for row in rows])
    classes = int(labels.max().item() + 1)
    old_oof = np.load(args.cls_oof)
    cls_predictions = old_oof["global_predictions"]
    actual = labels.cpu().numpy()
    cls_ba = float(balanced_accuracy_score(actual, cls_predictions))
    cls_recall = recall_score(
        actual,
        cls_predictions,
        labels=np.arange(classes),
        average=None,
        zero_division=0,
    )
    optimization = protocol["optimization"]
    common = {
        "maximum_epochs": optimization["maximum_epochs"],
        "patience": optimization["early_stopping_patience"],
        "batch_size": optimization["batch_size"],
    }
    records = []
    patch_candidates = []
    for lr, wd in product(
        optimization["classification_learning_rate"],
        optimization["weight_decay"],
    ):
        settings = {
            **common,
            "arm": "PATCH_AVG",
            "learning_rate": lr,
            "weight_decay": wd,
            "part_loss_weight": 0.0,
            "regularizer_weight": 0.0,
        }
        result = evaluate(settings, patches, targets, labels, folds, classes)
        record = {
            **settings,
            "balanced_accuracy": result["balanced_accuracy"],
            "selected_epoch": result["selected_epoch"],
        }
        records.append(record)
        patch_candidates.append((record, result))
        print(json.dumps(record, sort_keys=True), flush=True)
    patch_candidates.sort(
        key=lambda pair: (
            -pair[0]["balanced_accuracy"],
            pair[0]["learning_rate"],
            -pair[0]["weight_decay"],
        )
    )
    selected_patch, patch_result = patch_candidates[0]
    reference_ba = max(cls_ba, selected_patch["balanced_accuracy"])
    reference_recall = (
        cls_recall
        if cls_ba >= selected_patch["balanced_accuracy"]
        else patch_result["recall"]
    )

    prpool_candidates = []
    for part_weight, reg_weight in product(
        optimization["part_loss_weight"],
        optimization["complementary_regularizer_weight"],
    ):
        settings = {
            **common,
            "arm": "PRPOOL_ORACLE",
            "learning_rate": selected_patch["learning_rate"],
            "weight_decay": selected_patch["weight_decay"],
            "part_loss_weight": part_weight,
            "regularizer_weight": reg_weight,
        }
        result = evaluate(settings, patches, targets, labels, folds, classes)
        worst_delta = float((result["recall"] - reference_recall).min())
        record = {
            **settings,
            "balanced_accuracy": result["balanced_accuracy"],
            "gain_vs_reference_pp": 100 * (result["balanced_accuracy"] - reference_ba),
            "worst_class_delta_pp": 100 * worst_delta,
            "selected_epoch": result["selected_epoch"],
            "safety_feasible": worst_delta >= -0.02,
        }
        records.append(record)
        prpool_candidates.append((record, result))
        print(json.dumps(record, sort_keys=True), flush=True)
    feasible = [pair for pair in prpool_candidates if pair[0]["safety_feasible"]]
    pool = feasible if feasible else prpool_candidates
    pool.sort(
        key=lambda pair: (
            -pair[0]["balanced_accuracy"],
            pair[0]["part_loss_weight"],
            pair[0]["regularizer_weight"],
        )
    )
    selected_prpool, prpool_result = pool[0]
    gate_pass = (
        selected_prpool["gain_vs_reference_pp"]
        >= protocol["go_no_go"]["prpool_gain_pp_at_least"]
        and selected_prpool["worst_class_delta_pp"]
        >= protocol["go_no_go"]["worst_class_delta_pp_at_least"]
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    with (args.output_dir / "prpool_oof_grid.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(
            handle, fieldnames=sorted({key for row in records for key in row})
        )
        writer.writeheader()
        writer.writerows(records)
    np.savez(
        args.output_dir / "prpool_oof_predictions.npz",
        labels=actual,
        clip_cls_predictions=cls_predictions,
        patch_avg_predictions=patch_result["predictions"],
        prpool_predictions=prpool_result["predictions"],
    )
    summary = {
        "experiment_id": protocol["experiment_id"],
        "validation_images_read_or_encoded": 0,
        "test_images_read_or_encoded": 0,
        "clip_cls_global_ba": cls_ba,
        "selected_patch_avg": selected_patch,
        "reference_ba": reference_ba,
        "selected_prpool": selected_prpool,
        "feasible_prpool_candidates": len(feasible),
        "gate_pass": gate_pass,
    }
    (args.output_dir / "prpool_oof_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
