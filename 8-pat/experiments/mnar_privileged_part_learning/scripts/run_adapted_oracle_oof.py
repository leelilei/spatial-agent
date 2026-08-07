#!/usr/bin/env python3
"""Five-fold limited-backbone adaptation gate using train data only."""

from __future__ import annotations

import argparse
import copy
import json
import statistics
from pathlib import Path

import numpy as np
import open_clip
import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
from sklearn.metrics import balanced_accuracy_score, recall_score
from torch.utils.data import DataLoader, Dataset


class ImagesAndMasks(Dataset):
    def __init__(self, root, rows, masks, preprocess, indices):
        self.root = root
        self.rows = rows
        self.masks = masks
        self.preprocess = preprocess
        self.indices = list(indices)

    def __len__(self):
        return len(self.indices)

    def __getitem__(self, item):
        index = self.indices[item]
        row = self.rows[index]
        if row["split"] != "train":
            raise RuntimeError("PAT-C-260728-003 may decode train images only.")
        with Image.open(self.root / row["relative_path"]) as image:
            tensor = self.preprocess(image.convert("RGB"))
        return tensor, self.masks[index], int(row["class_index"]), index


class AdaptedModel(nn.Module):
    def __init__(self, visual, classes, use_prpool):
        super().__init__()
        self.visual = visual
        self.use_prpool = use_prpool
        if use_prpool:
            self.attention = nn.Sequential(
                nn.Conv2d(768, 256, 3, padding=1),
                nn.ReLU(inplace=True),
                nn.Conv2d(256, 5, 3, padding=1),
            )
            self.classifier = nn.Linear(5 * 768, classes)
        else:
            self.classifier = nn.Linear(512, classes)

    def forward(self, images):
        output = self.visual.forward_intermediates(
            images,
            indices=1,
            normalize_intermediates=True,
            output_fmt="NLC",
        )
        if not self.use_prpool:
            features = F.normalize(output["image_features"], dim=-1)
            return self.classifier(features), None
        patches = output["image_intermediates"][-1]
        batch, tokens, dimension = patches.shape
        feature_map = patches.transpose(1, 2).reshape(batch, dimension, 14, 14)
        raw_attention = self.attention(feature_map)
        attention = raw_attention.sigmoid()
        pooled = (
            feature_map[:, None, ...] * attention[:, :, None, ...]
        ).mean(dim=(-1, -2))
        pooled = F.normalize(pooled, p=2, dim=-1)
        return self.classifier(pooled.flatten(1)), raw_attention


def auxiliary_loss(raw_attention, targets, part_weight, reg_weight):
    loss = torch.zeros((), device=raw_attention.device)
    for kernel in (1, 2, 4, 7):
        logits = F.max_pool2d(raw_attention[:, :4], kernel)
        expected = F.max_pool2d(targets, kernel)
        loss = loss + F.binary_cross_entropy_with_logits(logits, expected)
    complement = raw_attention[:, 4].sigmoid().mean(dim=(-1, -2))
    return part_weight * loss / 4 - reg_weight * (
        complement * (1 - complement)
    ).mean()


def weights_for(labels, classes):
    counts = torch.bincount(labels, minlength=classes).float().clamp_min(1)
    return (counts.sum() / (classes * counts)).cuda()


def build_model(classes, use_prpool, cache_dir):
    clip_model, _, preprocess = open_clip.create_model_and_transforms(
        "ViT-B-16-quickgelu",
        pretrained="openai",
        cache_dir=str(cache_dir),
        precision="fp32",
    )
    for parameter in clip_model.parameters():
        parameter.requires_grad = False
    for parameter in clip_model.visual.transformer.resblocks[-1].parameters():
        parameter.requires_grad = True
    for parameter in clip_model.visual.ln_post.parameters():
        parameter.requires_grad = True
    model = AdaptedModel(clip_model.visual, classes, use_prpool).cuda()
    return model, preprocess


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
    masks,
    train_indices,
    eval_indices,
    settings,
    classes,
    use_prpool,
    cache_dir,
    seed,
):
    torch.manual_seed(seed)
    model, preprocess = build_model(classes, use_prpool, cache_dir)
    train_dataset = ImagesAndMasks(
        root, rows, masks, preprocess, train_indices
    )
    eval_dataset = ImagesAndMasks(root, rows, masks, preprocess, eval_indices)
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
    backbone_parameters = list(
        model.visual.transformer.resblocks[-1].parameters()
    ) + list(model.visual.ln_post.parameters())
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
    train_labels = torch.tensor(
        [rows[index]["class_index"] for index in train_indices],
        dtype=torch.long,
    )
    class_weights = weights_for(train_labels, classes)
    best_metric, best_epoch, best_state, stale = -1.0, 0, None, 0
    for epoch in range(1, settings["maximum_epochs"] + 1):
        model.train()
        for images, mask, target, _ in train_loader:
            images = images.cuda(non_blocking=True)
            mask = mask.cuda(non_blocking=True)
            target = target.cuda(non_blocking=True)
            optimizer.zero_grad(set_to_none=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                logits, raw_attention = model(images)
                loss = F.cross_entropy(
                    logits.float(), target, weight=class_weights
                )
            if use_prpool:
                loss = loss + auxiliary_loss(
                    raw_attention.float(),
                    mask.float(),
                    settings["part_loss_weight"],
                    settings["regularizer_weight"],
                )
            loss.backward()
            optimizer.step()
        prediction, actual, _ = evaluate(model, eval_loader)
        metric = balanced_accuracy_score(actual, prediction)
        if metric > best_metric + 1e-8:
            best_metric, best_epoch = float(metric), epoch
            best_state = copy.deepcopy(model.state_dict())
            stale = 0
        else:
            stale += 1
            if stale >= settings["patience"]:
                break
        print(
            json.dumps(
                {
                    "arm": "ADAPTED_PRPOOL_ORACLE"
                    if use_prpool
                    else "ADAPTED_GLOBAL",
                    "fold_seed": seed,
                    "epoch": epoch,
                    "fold_balanced_accuracy": metric,
                },
                sort_keys=True,
            ),
            flush=True,
        )
    model.load_state_dict(best_state)
    prediction, actual, row_indices = evaluate(model, eval_loader)
    del model
    torch.cuda.empty_cache()
    return prediction, actual, row_indices, best_epoch


def run_arm(root, rows, masks, settings, classes, use_prpool, cache_dir):
    folds = np.asarray([row["fold"] for row in rows])
    oof = np.full(len(rows), -1, dtype=np.int64)
    epochs = []
    for fold, seed in enumerate(settings["seeds_by_fold"]):
        train = np.flatnonzero(folds != fold)
        evaluate_on = np.flatnonzero(folds == fold)
        prediction, _, indices, best_epoch = fit_fold(
            root,
            rows,
            masks,
            train,
            evaluate_on,
            settings,
            classes,
            use_prpool,
            cache_dir,
            seed,
        )
        oof[indices] = prediction
        epochs.append(best_epoch)
    return oof, int(round(statistics.median(epochs)))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--targets", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path("/root/workspace/models/open_clip"),
    )
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    rows = [json.loads(line) for line in args.manifest.read_text().splitlines()]
    masks = torch.from_numpy(np.load(args.targets)["masks"])
    labels = np.asarray([row["class_index"] for row in rows])
    classes = int(labels.max() + 1)
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
        "seeds_by_fold": raw["seeds_by_fold"],
    }
    global_prediction, global_epoch = run_arm(
        args.dataset_root,
        rows,
        masks,
        settings,
        classes,
        False,
        args.cache_dir,
    )
    prpool_prediction, prpool_epoch = run_arm(
        args.dataset_root,
        rows,
        masks,
        settings,
        classes,
        True,
        args.cache_dir,
    )
    global_ba = float(balanced_accuracy_score(labels, global_prediction))
    prpool_ba = float(balanced_accuracy_score(labels, prpool_prediction))
    global_recall = recall_score(
        labels, global_prediction, labels=np.arange(classes), average=None
    )
    prpool_recall = recall_score(
        labels, prpool_prediction, labels=np.arange(classes), average=None
    )
    gain = 100 * (prpool_ba - global_ba)
    worst = 100 * float((prpool_recall - global_recall).min())
    threshold = protocol["go_no_go"]
    summary = {
        "experiment_id": protocol["experiment_id"],
        "adapted_global_ba": global_ba,
        "adapted_global_epoch": global_epoch,
        "adapted_prpool_oracle_ba": prpool_ba,
        "adapted_prpool_epoch": prpool_epoch,
        "gain_pp": gain,
        "worst_class_delta_pp": worst,
        "gate_pass": bool(
            gain
            >= threshold[
                "adapted_prpool_gain_pp_over_adapted_global_at_least"
            ]
            and worst >= threshold["worst_class_delta_pp_at_least"]
        ),
        "validation_images_read_or_encoded": 0,
        "test_images_read_or_encoded": 0,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    np.savez(
        args.output_dir / "adapted_oracle_oof_predictions.npz",
        labels=labels,
        adapted_global_predictions=global_prediction,
        adapted_prpool_predictions=prpool_prediction,
    )
    (args.output_dir / "adapted_oracle_oof_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
