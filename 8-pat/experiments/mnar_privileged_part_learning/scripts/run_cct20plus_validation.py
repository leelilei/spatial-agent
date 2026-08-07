#!/usr/bin/env python3
"""Run CCT20+ official-train Oracle and sparse-selector development gates."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
from sklearn.metrics import balanced_accuracy_score, f1_score, recall_score
from torch.utils.data import DataLoader, Dataset
from torchvision.transforms import InterpolationMode, RandomResizedCrop
from torchvision.transforms import functional as TF

import run_cub_prpool_oof as cub_base


IMAGE_SIZE = 384
FEATURE_SIZE = 12
PARTS = 9
LEFT_RIGHT_SWAPS = ((2, 5), (3, 6), (4, 7))
NORMALIZE_MEAN = (0.485, 0.456, 0.406)
NORMALIZE_STD = (0.229, 0.224, 0.225)


def render_targets(points):
    target = torch.zeros(PARTS, FEATURE_SIZE, FEATURE_SIZE)
    for part, (x, y, visible) in enumerate(points):
        if not visible or x < 0 or y < 0 or x >= IMAGE_SIZE or y >= IMAGE_SIZE:
            continue
        gx = min(FEATURE_SIZE - 1, int(x * FEATURE_SIZE / IMAGE_SIZE))
        gy = min(FEATURE_SIZE - 1, int(y * FEATURE_SIZE / IMAGE_SIZE))
        y0, y1 = max(0, gy - 1), min(FEATURE_SIZE, gy + 2)
        x0, x1 = max(0, gx - 1), min(FEATURE_SIZE, gx + 2)
        target[part, y0:y1, x0:x1] = 1.0
    return target


class CCTDataset(Dataset):
    def __init__(self, root, rows, indices, training, selected):
        self.root = root
        self.rows = rows
        self.indices = list(indices)
        self.training = training
        self.selected = selected

    def __len__(self):
        return len(self.indices)

    def __getitem__(self, item):
        row_index = self.indices[item]
        row = self.rows[row_index]
        if row["split"] != "train" or row["source_split"] != "official_train":
            raise RuntimeError("CCT development runner may decode train only")
        with Image.open(self.root / row["relative_path"]) as source:
            image = source.convert("RGB")
        width, height = image.size
        points = [list(point) for point in row["keypoints"]]
        for point in points:
            point[0] *= width / row["original_width"]
            point[1] *= height / row["original_height"]

        if self.training:
            top, left, crop_h, crop_w = RandomResizedCrop.get_params(
                image, scale=(0.7, 1.0), ratio=(0.8, 1.25)
            )
            image = TF.resized_crop(
                image,
                top,
                left,
                crop_h,
                crop_w,
                [IMAGE_SIZE, IMAGE_SIZE],
                InterpolationMode.BICUBIC,
                antialias=True,
            )
            for point in points:
                x, y, visible = point
                inside = (
                    bool(visible)
                    and left <= x < left + crop_w
                    and top <= y < top + crop_h
                )
                point[0] = (x - left) * IMAGE_SIZE / crop_w
                point[1] = (y - top) * IMAGE_SIZE / crop_h
                point[2] = int(inside)
            if torch.rand(()) < 0.5:
                image = TF.hflip(image)
                for point in points:
                    point[0] = IMAGE_SIZE - 1 - point[0]
                for left_part, right_part in LEFT_RIGHT_SWAPS:
                    points[left_part], points[right_part] = (
                        points[right_part],
                        points[left_part],
                    )
        else:
            image = TF.resize(
                image,
                [IMAGE_SIZE, IMAGE_SIZE],
                interpolation=InterpolationMode.BICUBIC,
                antialias=True,
            )
            for point in points:
                point[0] *= IMAGE_SIZE / width
                point[1] *= IMAGE_SIZE / height
        image = TF.normalize(
            TF.to_tensor(image), NORMALIZE_MEAN, NORMALIZE_STD
        )
        return (
            image,
            render_targets(points),
            int(row["class_index"]),
            row_index,
            bool(self.selected[row_index]),
        )


class CCTModel(nn.Module):
    def __init__(self, classes, use_prpool):
        super().__init__()
        self.features = cub_base.ResNetFeatures()
        self.use_prpool = use_prpool
        if use_prpool:
            self.attention = nn.Sequential(
                nn.Conv2d(2048, 256, 3, padding=1),
                nn.ReLU(inplace=True),
                nn.Conv2d(256, PARTS + 1, 3, padding=1),
            )
            self.classifier = nn.Linear((PARTS + 1) * 2048, classes)
        else:
            self.classifier = nn.Linear(2048, classes)

    def forward(self, images):
        feature_map = self.features(images)
        if not self.use_prpool:
            pooled = F.adaptive_avg_pool2d(feature_map, 1).flatten(1)
            return self.classifier(pooled), None
        raw_attention = self.attention(feature_map)
        attention = raw_attention.sigmoid()
        pooled = (
            feature_map[:, None, ...] * attention[:, :, None, ...]
        ).mean(dim=(-1, -2))
        pooled = F.normalize(pooled, p=2, dim=-1)
        return self.classifier(pooled.flatten(1)), raw_attention


def selected_auxiliary_loss(
    raw_attention, targets, selected, part_weight, regularizer_weight
):
    complement = raw_attention[:, PARTS].sigmoid().mean(dim=(-1, -2))
    loss = -regularizer_weight * (complement * (1 - complement)).mean()
    if selected.any():
        part_logits = raw_attention[selected, :PARTS]
        part_targets = targets[selected]
        part_loss = torch.zeros((), device=raw_attention.device)
        for kernel in (1, 2, 3, 6):
            logits = F.max_pool2d(part_logits, kernel)
            expected = F.max_pool2d(part_targets, kernel)
            part_loss += F.binary_cross_entropy_with_logits(logits, expected)
        loss += part_weight * part_loss / 4
    return loss


def evaluate(model, loader):
    model.eval()
    predictions, labels, indices = [], [], []
    with torch.inference_mode():
        for images, _, target, row_index, _ in loader:
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                logits, _ = model(images.cuda(non_blocking=True))
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
    arm,
    use_prpool,
):
    torch.manual_seed(seed)
    np.random.seed(seed)
    classes = len({int(row["class_index"]) for row in rows})
    model = CCTModel(classes, use_prpool=use_prpool).cuda()
    train_dataset = CCTDataset(
        root, rows, train_indices, True, selected=selected
    )
    eval_dataset = CCTDataset(
        root, rows, eval_indices, False, selected=selected
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
    for epoch in range(1, settings["epochs"] + 1):
        model.train()
        annotated_seen = 0
        running_loss = 0.0
        for images, targets, labels, _, annotated in train_loader:
            images = images.cuda(non_blocking=True)
            targets = targets.cuda(non_blocking=True)
            labels = labels.cuda(non_blocking=True)
            annotated = annotated.cuda(non_blocking=True)
            optimizer.zero_grad(set_to_none=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                logits, raw_attention = model(images)
                loss = F.cross_entropy(logits.float(), labels)
            if use_prpool:
                loss += selected_auxiliary_loss(
                    raw_attention.float(),
                    targets.float(),
                    annotated,
                    settings["part_loss_weight"],
                    settings["regularizer_weight"],
                )
            loss.backward()
            optimizer.step()
            annotated_seen += int(annotated.sum())
            running_loss += float(loss.detach()) * len(labels)
        print(
            json.dumps(
                {
                    "arm": arm,
                    "fold_seed": seed,
                    "epoch": epoch,
                    "mean_train_loss": running_loss / len(train_dataset),
                    "annotated_seen": annotated_seen,
                },
                sort_keys=True,
            ),
            flush=True,
        )
    result = evaluate(model, eval_loader)
    del model
    torch.cuda.empty_cache()
    return result


def metric_bundle(labels, predictions, classes):
    recall = recall_score(
        labels,
        predictions,
        labels=np.arange(classes),
        average=None,
        zero_division=0,
    )
    return {
        "top1": float(np.mean(labels == predictions)),
        "balanced_accuracy": float(
            balanced_accuracy_score(labels, predictions)
        ),
        "macro_f1": float(
            f1_score(labels, predictions, average="macro", zero_division=0)
        ),
        "class_recall": recall,
    }


def run_arm(
    root,
    rows,
    folds,
    selected_by_fold,
    fold_seeds,
    settings,
    arm,
    use_prpool,
    fold_count,
):
    predictions = np.full(len(rows), -1, dtype=np.int64)
    for fold in range(fold_count):
        train_indices = np.flatnonzero(folds != fold)
        eval_indices = np.flatnonzero(folds == fold)
        prediction, _, row_indices = fit_fold(
            root,
            rows,
            train_indices,
            eval_indices,
            selected_by_fold[fold],
            settings,
            fold_seeds[fold],
            arm,
            use_prpool,
        )
        predictions[row_indices] = prediction
    return predictions


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("oracle", "selector"), required=True)
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--oracle-protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--oracle-summary", type=Path)
    parser.add_argument("--selections", type=Path)
    parser.add_argument("--cub-screen-summary", type=Path)
    parser.add_argument("--fold-limit", type=int, default=5)
    parser.add_argument("--epoch-limit", type=int, default=9)
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
        raise RuntimeError("CCT development manifest contains a forbidden split")
    labels = np.asarray([row["class_index"] for row in rows])
    folds = np.asarray([row["fold"] for row in rows])
    fold_total = len(np.unique(folds))
    fold_count = min(fold_total, args.fold_limit)
    classes = len(np.unique(labels))
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
    all_selected = np.ones((fold_total, len(rows)), dtype=np.bool_)
    no_selected = np.zeros((fold_total, len(rows)), dtype=np.bool_)
    predictions = {}
    if args.mode == "oracle":
        fold_seeds = protocol["training"]["oracle_fold_seeds"]
        predictions["GLOBAL"] = run_arm(
            args.dataset_root,
            rows,
            folds,
            no_selected,
            fold_seeds,
            settings,
            "GLOBAL",
            False,
            fold_count,
        )
        predictions["FULL_KEYPOINT_ORACLE"] = run_arm(
            args.dataset_root,
            rows,
            folds,
            all_selected,
            fold_seeds,
            settings,
            "FULL_KEYPOINT_ORACLE",
            True,
            fold_count,
        )
    else:
        if not args.oracle_summary or not args.selections or not args.cub_screen_summary:
            raise RuntimeError("Selector mode requires oracle, selections, and CUB winner")
        oracle_summary = json.loads(args.oracle_summary.read_text())
        if not oracle_summary.get("oracle_gate_pass"):
            raise RuntimeError("CCT Full Oracle gate did not pass")
        cub_screen = json.loads(args.cub_screen_summary.read_text())
        winner = cub_screen["winner"]
        selection_file = np.load(args.selections)
        for group, (random_seed, fold_seeds) in enumerate(
            zip(
                protocol["training"]["random_selection_seeds"],
                protocol["training"]["paired_selector_seed_packs"],
                strict=True,
            ),
            start=1,
        ):
            for arm, key in (
                ("RANDOM", f"selected_RANDOM_S{random_seed}"),
                ("WINNER", f"selected_WINNER_{winner}"),
            ):
                output_name = f"G{group}_{arm}"
                predictions[output_name] = run_arm(
                    args.dataset_root,
                    rows,
                    folds,
                    selection_file[key],
                    fold_seeds,
                    settings,
                    output_name,
                    True,
                    fold_count,
                )

    complete = fold_count == fold_total
    summary = {
        "experiment_id": protocol["experiment_id"],
        "mode": args.mode.upper(),
        "run_mode": "FORMAL" if complete else "SMOKE",
        "folds_completed": fold_count,
        "folds_total": fold_total,
        "epochs": settings["epochs"],
        "classes": classes,
        "eligible_rows": len(rows),
        "cis_test_images_decoded_or_encoded": 0,
        "trans_test_images_decoded_or_encoded": 0,
    }
    if complete and args.mode == "oracle":
        global_metrics = metric_bundle(
            labels, predictions["GLOBAL"], classes
        )
        oracle_metrics = metric_bundle(
            labels, predictions["FULL_KEYPOINT_ORACLE"], classes
        )
        gain_pp = 100 * (
            oracle_metrics["balanced_accuracy"]
            - global_metrics["balanced_accuracy"]
        )
        summary.update(
            {
                "global": {
                    key: value
                    for key, value in global_metrics.items()
                    if key != "class_recall"
                },
                "full_keypoint_oracle": {
                    key: value
                    for key, value in oracle_metrics.items()
                    if key != "class_recall"
                },
                "oracle_gain_pp": gain_pp,
                "oracle_gate_pass": (
                    gain_pp >= protocol["gates"]["oracle_minimum_gain_pp"]
                ),
            }
        )
    elif complete:
        oracle_summary = json.loads(args.oracle_summary.read_text())
        oracle_predictions_path = args.oracle_summary.parent / "cct20plus_oracle_predictions.npz"
        oracle_predictions = np.load(oracle_predictions_path)
        global_prediction = oracle_predictions["GLOBAL_predictions"]
        global_recall = metric_bundle(
            labels, global_prediction, classes
        )["class_recall"]
        groups = []
        for group in range(1, 4):
            random_metrics = metric_bundle(
                labels, predictions[f"G{group}_RANDOM"], classes
            )
            winner_metrics = metric_bundle(
                labels, predictions[f"G{group}_WINNER"], classes
            )
            random_negative = float(
                np.mean((random_metrics["class_recall"] - global_recall) < 0)
            )
            winner_negative = float(
                np.mean((winner_metrics["class_recall"] - global_recall) < 0)
            )
            groups.append(
                {
                    "group": group,
                    "random_ba": random_metrics["balanced_accuracy"],
                    "winner_ba": winner_metrics["balanced_accuracy"],
                    "paired_ba_improvement_pp": 100
                    * (
                        winner_metrics["balanced_accuracy"]
                        - random_metrics["balanced_accuracy"]
                    ),
                    "random_negative_transfer_class_rate": random_negative,
                    "winner_negative_transfer_class_rate": winner_negative,
                    "negative_transfer_rate_change_pp": 100
                    * (winner_negative - random_negative),
                }
            )
        ba_deltas = np.asarray(
            [group["paired_ba_improvement_pp"] for group in groups]
        )
        safety_deltas = np.asarray(
            [group["negative_transfer_rate_change_pp"] for group in groups]
        )
        benefit = protocol["gates"]["selector_benefit_branch"]
        safety = protocol["gates"]["selector_safety_branch"]
        benefit_pass = (
            ba_deltas.mean()
            >= benefit["minimum_mean_paired_ba_improvement_pp"]
            and int(np.sum(ba_deltas > 0))
            >= benefit["minimum_positive_groups"]
            and safety_deltas.mean()
            <= 100 * benefit["maximum_mean_negative_transfer_rate_increase"]
        )
        safety_pass = (
            ba_deltas.mean() >= -safety["maximum_mean_ba_deficit_pp"]
            and -safety_deltas.mean()
            >= safety["minimum_negative_transfer_rate_reduction_pp"]
            and int(np.sum(safety_deltas < 0))
            >= safety["minimum_safety_positive_groups"]
        )
        summary.update(
            {
                "cub_winner": json.loads(
                    args.cub_screen_summary.read_text()
                )["winner"],
                "groups": groups,
                "mean_paired_ba_improvement_pp": float(ba_deltas.mean()),
                "mean_negative_transfer_rate_change_pp": float(
                    safety_deltas.mean()
                ),
                "benefit_branch_pass": benefit_pass,
                "safety_branch_pass": safety_pass,
                "selector_gate_pass": benefit_pass or safety_pass,
            }
        )
    else:
        summary["gate_evaluated"] = False
        summary["prediction_counts"] = {
            key: int(np.sum(value >= 0))
            for key, value in predictions.items()
        }

    args.output_dir.mkdir(parents=True, exist_ok=True)
    prediction_name = (
        "cct20plus_oracle_predictions.npz"
        if args.mode == "oracle"
        else "cct20plus_selector_predictions.npz"
    )
    summary_name = (
        "cct20plus_oracle_summary.json"
        if args.mode == "oracle"
        else "cct20plus_selector_summary.json"
    )
    np.savez_compressed(
        args.output_dir / prediction_name,
        labels=labels,
        **{
            f"{key}_predictions": value
            for key, value in predictions.items()
        },
    )
    (args.output_dir / summary_name).write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
