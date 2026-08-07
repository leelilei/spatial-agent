#!/usr/bin/env python3
"""Confusion-trust residual adapter screen on frozen DINOv2 features."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path

import numpy as np
from sklearn.svm import SVC

from sparse_anchor_utils import balanced_accuracy, class_recall, l2_normalize


CLASSES = 200
DIMENSION = 768
BOTTLENECK = 128
EPOCHS = 300
LEARNING_RATE = 0.003
WEIGHT_DECAY = 0.001
TEMPERATURE = 0.07
TRUST_WEIGHT = 0.1
HARD_MARGIN = 0.1
HARD_WEIGHT = 0.5
FOLD_SEEDS = (9501, 9502, 9503, 9504, 9505)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def train_adapter(features, labels, seed, hard_weight):
    import torch
    from torch import nn
    from torch.nn import functional as F

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    x = torch.as_tensor(features, dtype=torch.float32, device="cuda")
    y = torch.as_tensor(labels, dtype=torch.long, device="cuda")

    class ResidualAdapter(nn.Module):
        def __init__(self):
            super().__init__()
            self.down = nn.Linear(DIMENSION, BOTTLENECK)
            self.up = nn.Linear(BOTTLENECK, DIMENSION)
            nn.init.zeros_(self.up.weight)
            nn.init.zeros_(self.up.bias)

        def forward(self, values):
            residual = self.up(F.gelu(self.down(values)))
            return F.normalize(values + 0.2 * residual, dim=-1)

    model = ResidualAdapter().cuda()
    optimizer = torch.optim.AdamW(
        model.parameters(), lr=LEARNING_RATE, weight_decay=WEIGHT_DECAY
    )
    counts = torch.bincount(y, minlength=CLASSES).float()
    rows = torch.arange(len(y), device="cuda")
    for epoch in range(EPOCHS):
        model.train()
        z = model(x)
        sums = torch.zeros(CLASSES, DIMENSION, device="cuda")
        sums.index_add_(0, y, z)
        centers = F.normalize(sums / counts[:, None], dim=-1)
        target_centers = F.normalize(
            (sums[y] - z) / (counts[y, None] - 1.0),
            dim=-1,
        )
        logits = z @ centers.T
        target_score = (z * target_centers).sum(dim=-1)
        logits = logits.clone()
        logits[rows, y] = target_score
        prototype_loss = F.cross_entropy(logits / TEMPERATURE, y)
        masked = logits.clone()
        masked[rows, y] = -torch.inf
        hard_negative = masked.max(dim=1).values
        hard_loss = F.relu(HARD_MARGIN - target_score + hard_negative).mean()
        trust_loss = (1.0 - (z * x).sum(dim=-1)).mean()
        loss = (
            prototype_loss
            + hard_weight * hard_loss
            + TRUST_WEIGHT * trust_loss
        )
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        optimizer.step()
        if epoch in (0, 99, 199, 299):
            print(
                json.dumps(
                    {
                        "status": "ADAPTER_TRAIN",
                        "seed": seed,
                        "hard_weight": hard_weight,
                        "epoch": epoch + 1,
                        "loss": float(loss.detach()),
                        "prototype_loss": float(prototype_loss.detach()),
                        "hard_loss": float(hard_loss.detach()),
                        "trust_loss": float(trust_loss.detach()),
                    }
                ),
                flush=True,
            )
    model.eval()
    return model


def transform(model, features):
    import torch

    outputs = []
    with torch.inference_mode():
        for start in range(0, len(features), 512):
            batch = torch.as_tensor(
                features[start : start + 512], dtype=torch.float32, device="cuda"
            )
            outputs.append(model(batch).cpu().numpy())
    return np.concatenate(outputs)


def class_bootstrap_interval(delta, seed=9525, draws=20000):
    rng = np.random.default_rng(seed)
    indices = rng.integers(0, len(delta), (draws, len(delta)))
    values = delta[indices].mean(axis=1) * 100.0
    return [float(x) for x in np.quantile(values, [0.025, 0.5, 0.975])]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--feature-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    labels = np.load(args.feature_dir / "labels.npy")
    folds = np.load(args.feature_dir / "folds.npy")
    image_ids = np.load(args.feature_dir / "image_ids.npy")
    features = l2_normalize(np.load(args.feature_dir / "cls.npy", mmap_mode="r"))
    predictions = {
        "RBF_REFERENCE": np.full(len(labels), -1, dtype=np.int64),
        "PROTO_ADAPTER": np.full(len(labels), -1, dtype=np.int64),
        "CONFUSION_TRUST_ADAPTER": np.full(len(labels), -1, dtype=np.int64),
    }
    for fold, seed in enumerate(FOLD_SEEDS):
        train = np.flatnonzero(folds != fold)
        evaluate_on = np.flatnonzero(folds == fold)
        reference = SVC(C=3.0, kernel="rbf", gamma="scale").fit(
            features[train], labels[train]
        )
        predictions["RBF_REFERENCE"][evaluate_on] = reference.predict(
            features[evaluate_on]
        )
        for name, hard_weight in (
            ("PROTO_ADAPTER", 0.0),
            ("CONFUSION_TRUST_ADAPTER", HARD_WEIGHT),
        ):
            adapter = train_adapter(
                features[train], labels[train], seed, hard_weight
            )
            adapted_train = transform(adapter, features[train])
            adapted_eval = transform(adapter, features[evaluate_on])
            classifier = SVC(C=3.0, kernel="rbf", gamma="scale").fit(
                adapted_train, labels[train]
            )
            predictions[name][evaluate_on] = classifier.predict(adapted_eval)
        print(json.dumps({"status": "ADAPTER_FOLD_COMPLETE", "fold": fold}), flush=True)
    metrics = {
        name: balanced_accuracy(labels, prediction)
        for name, prediction in predictions.items()
    }
    reference = metrics["RBF_REFERENCE"]
    control = metrics["PROTO_ADAPTER"]
    candidate = metrics["CONFUSION_TRUST_ADAPTER"]
    gain_reference = 100.0 * (candidate - reference)
    gain_control = 100.0 * (candidate - control)
    reference_recall = class_recall(labels, predictions["RBF_REFERENCE"])
    candidate_recall = class_recall(labels, predictions["CONFUSION_TRUST_ADAPTER"])
    delta = candidate_recall - reference_recall
    summary = {
        "experiment_id": protocol["experiment_id"],
        "metrics": metrics,
        "candidate_gain_pp_vs_reference": gain_reference,
        "candidate_gain_pp_vs_control": gain_control,
        "screen_success": bool(gain_reference >= 0.5 and gain_control >= 0.25),
        "candidate_positive_classes": int(np.sum(delta > 0)),
        "candidate_negative_classes": int(np.sum(delta < 0)),
        "candidate_class_bootstrap_delta_pp": class_bootstrap_interval(delta),
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
    }
    np.savez_compressed(
        args.output_dir / "adapter_predictions.npz",
        labels=labels,
        image_ids=image_ids,
        **{f"{name}_predictions": value for name, value in predictions.items()},
    )
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
