#!/usr/bin/env python3
"""CUB train-only Global versus full-keypoint PrPool OOF gate."""

from __future__ import annotations

import argparse
import copy
import json
import statistics
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
from sklearn.metrics import balanced_accuracy_score, recall_score
from torch.utils.data import DataLoader, Dataset
from torchvision.models import ResNet50_Weights, resnet50
from torchvision.transforms import InterpolationMode, RandomResizedCrop
from torchvision.transforms import functional as TF


IMAGE_SIZE = 384
FEATURE_SIZE = 12
LEFT_RIGHT_SWAPS = ((6, 10), (7, 11), (8, 12))
NORMALIZE_MEAN = (0.485, 0.456, 0.406)
NORMALIZE_STD = (0.229, 0.224, 0.225)


def render_targets(points):
    target = torch.zeros(15, FEATURE_SIZE, FEATURE_SIZE)
    for part, (x, y, visible) in enumerate(points):
        if not visible or x < 0 or y < 0 or x >= IMAGE_SIZE or y >= IMAGE_SIZE:
            continue
        gx = min(FEATURE_SIZE - 1, int(x * FEATURE_SIZE / IMAGE_SIZE))
        gy = min(FEATURE_SIZE - 1, int(y * FEATURE_SIZE / IMAGE_SIZE))
        y0, y1 = max(0, gy - 1), min(FEATURE_SIZE, gy + 2)
        x0, x1 = max(0, gx - 1), min(FEATURE_SIZE, gx + 2)
        target[part, y0:y1, x0:x1] = 1.0
    return target


class CUBTrainOnly(Dataset):
    def __init__(self, root, rows, indices, training, seed):
        self.root = root
        self.rows = rows
        self.indices = list(indices)
        self.training = training
        self.seed = seed

    def __len__(self):
        return len(self.indices)

    def __getitem__(self, item):
        row_index = self.indices[item]
        row = self.rows[row_index]
        if row["split"] != "train" or row["source_split"] != "official_train":
            raise RuntimeError("PAT-D-260728-001 may decode official train only")
        with Image.open(self.root / row["relative_path"]) as source:
            image = source.convert("RGB")
        width, height = image.size
        points = [list(point) for point in row["keypoints"]]

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
                point[0] = point[0] * IMAGE_SIZE / width
                point[1] = point[1] * IMAGE_SIZE / height

        image = TF.normalize(
            TF.to_tensor(image), NORMALIZE_MEAN, NORMALIZE_STD
        )
        return (
            image,
            render_targets(points),
            int(row["class_index"]),
            row_index,
        )


class ResNetFeatures(nn.Module):
    def __init__(self):
        super().__init__()
        backbone = resnet50(weights=ResNet50_Weights.IMAGENET1K_V2)
        self.stem_to_layer3 = nn.Sequential(
            backbone.conv1,
            backbone.bn1,
            backbone.relu,
            backbone.maxpool,
            backbone.layer1,
            backbone.layer2,
            backbone.layer3,
        )
        self.layer4 = backbone.layer4
        for parameter in self.stem_to_layer3.parameters():
            parameter.requires_grad = False

    def forward(self, images):
        self.stem_to_layer3.eval()
        with torch.no_grad():
            features = self.stem_to_layer3(images)
        return self.layer4(features)


class CUBModel(nn.Module):
    def __init__(self, classes, use_prpool):
        super().__init__()
        self.features = ResNetFeatures()
        self.use_prpool = use_prpool
        if use_prpool:
            self.attention = nn.Sequential(
                nn.Conv2d(2048, 256, 3, padding=1),
                nn.ReLU(inplace=True),
                nn.Conv2d(256, 16, 3, padding=1),
            )
            self.classifier = nn.Linear(16 * 2048, classes)
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


def auxiliary_loss(raw_attention, targets, part_weight, reg_weight):
    loss = torch.zeros((), device=raw_attention.device)
    for kernel in (1, 2, 3, 6):
        logits = F.max_pool2d(raw_attention[:, :15], kernel)
        expected = F.max_pool2d(targets, kernel)
        loss = loss + F.binary_cross_entropy_with_logits(logits, expected)
    complement = raw_attention[:, 15].sigmoid().mean(dim=(-1, -2))
    regularizer = (complement * (1 - complement)).mean()
    return part_weight * loss / 4 - reg_weight * regularizer


def evaluate(model, loader):
    model.eval()
    predictions, labels, indices = [], [], []
    with torch.inference_mode():
        for images, _, target, row_index in loader:
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
    settings,
    use_prpool,
    seed,
):
    torch.manual_seed(seed)
    np.random.seed(seed)
    model = CUBModel(classes=200, use_prpool=use_prpool).cuda()
    train_dataset = CUBTrainOnly(
        root, rows, train_indices, training=True, seed=seed
    )
    eval_dataset = CUBTrainOnly(
        root, rows, eval_indices, training=False, seed=seed
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
    best_metric, best_epoch, best_state, stale = -1.0, 0, None, 0
    for epoch in range(1, settings["maximum_epochs"] + 1):
        model.train()
        for images, targets, labels, _ in train_loader:
            images = images.cuda(non_blocking=True)
            targets = targets.cuda(non_blocking=True)
            labels = labels.cuda(non_blocking=True)
            optimizer.zero_grad(set_to_none=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                logits, raw_attention = model(images)
                loss = F.cross_entropy(logits.float(), labels)
            if use_prpool:
                loss = loss + auxiliary_loss(
                    raw_attention.float(),
                    targets.float(),
                    settings["part_loss_weight"],
                    settings["regularizer_weight"],
                )
            loss.backward()
            optimizer.step()

        prediction, actual, _ = evaluate(model, eval_loader)
        metric = balanced_accuracy_score(actual, prediction)
        print(
            json.dumps(
                {
                    "arm": "PRPOOL_FULL_KEYPOINT_ORACLE"
                    if use_prpool
                    else "GLOBAL",
                    "fold_seed": seed,
                    "epoch": epoch,
                    "fold_balanced_accuracy": metric,
                },
                sort_keys=True,
            ),
            flush=True,
        )
        if metric > best_metric + 1e-8:
            best_metric, best_epoch = float(metric), epoch
            best_state = copy.deepcopy(model.state_dict())
            stale = 0
        else:
            stale += 1
            if stale >= settings["patience"]:
                break
    model.load_state_dict(best_state)
    prediction, actual, row_indices = evaluate(model, eval_loader)
    del model
    torch.cuda.empty_cache()
    return prediction, actual, row_indices, best_epoch


def run_arm(root, rows, settings, use_prpool):
    folds = np.asarray([row["fold"] for row in rows])
    oof = np.full(len(rows), -1, dtype=np.int64)
    epochs = []
    for fold, seed in enumerate(settings["seeds_by_fold"]):
        train = np.flatnonzero(folds != fold)
        evaluate_on = np.flatnonzero(folds == fold)
        prediction, _, indices, best_epoch = fit_fold(
            root,
            rows,
            train,
            evaluate_on,
            settings,
            use_prpool,
            seed,
        )
        oof[indices] = prediction
        epochs.append(best_epoch)
    if (oof < 0).any():
        raise RuntimeError("OOF predictions are incomplete")
    return oof, int(round(statistics.median(epochs)))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    rows = [json.loads(line) for line in args.manifest.read_text().splitlines()]
    labels = np.asarray([row["class_index"] for row in rows])
    raw = protocol["optimization"]
    settings = {
        "head_learning_rate": raw["head_learning_rate"],
        "backbone_learning_rate": raw["backbone_learning_rate"],
        "weight_decay": raw["weight_decay"],
        "part_loss_weight": raw["part_loss_weight"],
        "regularizer_weight": raw["complementary_regularizer_weight"],
        "batch_size": raw["batch_size"],
        "maximum_epochs": raw["maximum_epochs"],
        "patience": raw["early_stopping_patience"],
        "seeds_by_fold": raw["fold_training_seeds"],
    }
    global_prediction, global_epoch = run_arm(
        args.dataset_root, rows, settings, False
    )
    prpool_prediction, prpool_epoch = run_arm(
        args.dataset_root, rows, settings, True
    )
    global_ba = float(balanced_accuracy_score(labels, global_prediction))
    prpool_ba = float(balanced_accuracy_score(labels, prpool_prediction))
    global_recall = recall_score(
        labels, global_prediction, labels=np.arange(200), average=None
    )
    prpool_recall = recall_score(
        labels, prpool_prediction, labels=np.arange(200), average=None
    )
    gain = 100 * (prpool_ba - global_ba)
    class_delta = prpool_recall - global_recall
    threshold = protocol["go_no_go"]["prpool_gain_pp_over_global_at_least"]
    summary = {
        "experiment_id": protocol["experiment_id"],
        "global_oof_ba": global_ba,
        "global_median_best_epoch": global_epoch,
        "prpool_full_keypoint_oracle_oof_ba": prpool_ba,
        "prpool_median_best_epoch": prpool_epoch,
        "gain_pp": gain,
        "worst_class_delta_pp": 100 * float(class_delta.min()),
        "negative_transfer_class_rate": float(np.mean(class_delta < 0)),
        "gate_pass": bool(gain >= threshold),
        "official_test_images_decoded_or_encoded": 0,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    np.savez(
        args.output_dir / "cub_prpool_oof_predictions.npz",
        labels=labels,
        global_predictions=global_prediction,
        prpool_predictions=prpool_prediction,
    )
    (args.output_dir / "cub_prpool_oof_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
