#!/usr/bin/env python3
"""Image-level last-block LoRA PEFT screen for PAT-H-260729-010."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from pathlib import Path

import numpy as np
from PIL import Image
from sklearn.svm import SVC

from sparse_anchor_utils import balanced_accuracy, class_recall, l2_normalize


IMAGE_SIZE = 392
DIMENSION = 768
CLASSES = 200
LORA_RANK = 8
LORA_ALPHA = 16.0
LORA_DROPOUT = 0.05
HEAD_SCALE = 20.0
EPOCHS = 12
BATCH_SIZE = 8
LORA_LR = 2e-4
HEAD_LR = 2e-3
WEIGHT_DECAY = 0.01
LABEL_SMOOTHING = 0.1
TRUST_WEIGHT = 0.1
FOLD_SEEDS = (9601, 9602, 9603, 9604, 9605)
NORMALIZE_MEAN = (0.485, 0.456, 0.406)
NORMALIZE_STD = (0.229, 0.224, 0.225)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def seed_everything(seed: int) -> None:
    import torch

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


class CUBTrainDataset:
    def __init__(self, root: Path, rows: list[dict], indices: np.ndarray):
        self.root = root
        self.rows = rows
        self.indices = np.asarray(indices)

    def __len__(self):
        return len(self.indices)

    def __getitem__(self, position):
        from torchvision import transforms
        from torchvision.transforms import InterpolationMode

        index = int(self.indices[position])
        row = self.rows[index]
        if row["split"] != "train" or row["source_split"] != "official_train":
            raise RuntimeError("PEFT may decode official train only")
        with Image.open(self.root / row["relative_path"]) as source:
            image = source.convert("RGB")
        transform = transforms.Compose(
            [
                transforms.RandomResizedCrop(
                    IMAGE_SIZE,
                    scale=(0.75, 1.0),
                    ratio=(0.85, 1.15),
                    interpolation=InterpolationMode.BICUBIC,
                    antialias=True,
                ),
                transforms.RandomHorizontalFlip(p=0.5),
                transforms.ColorJitter(0.15, 0.15, 0.15, 0.05),
                transforms.ToTensor(),
                transforms.Normalize(NORMALIZE_MEAN, NORMALIZE_STD),
            ]
        )
        return transform(image), index, int(row["class_index"])


class CUBEvalDataset:
    def __init__(self, root: Path, rows: list[dict]):
        self.root = root
        self.rows = rows

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, index):
        from torchvision.transforms import InterpolationMode
        from torchvision.transforms import functional as TF

        row = self.rows[index]
        if row["split"] != "train" or row["source_split"] != "official_train":
            raise RuntimeError("PEFT may decode official train only")
        with Image.open(self.root / row["relative_path"]) as source:
            image = source.convert("RGB")
        image = TF.resize(
            image,
            [IMAGE_SIZE, IMAGE_SIZE],
            interpolation=InterpolationMode.BICUBIC,
            antialias=True,
        )
        image = TF.normalize(
            TF.to_tensor(image), NORMALIZE_MEAN, NORMALIZE_STD
        )
        return image, index


def make_lora_linear(base):
    import torch
    from torch import nn

    class LoRALinear(nn.Module):
        def __init__(self, base_layer):
            super().__init__()
            self.base = base_layer
            for parameter in self.base.parameters():
                parameter.requires_grad = False
            self.lora_dropout = nn.Dropout(LORA_DROPOUT)
            self.lora_a = nn.Linear(
                base_layer.in_features, LORA_RANK, bias=False
            )
            self.lora_b = nn.Linear(
                LORA_RANK, base_layer.out_features, bias=False
            )
            nn.init.kaiming_uniform_(self.lora_a.weight, a=math.sqrt(5))
            nn.init.zeros_(self.lora_b.weight)
            self.scaling = LORA_ALPHA / LORA_RANK

        def forward(self, values):
            return self.base(values) + self.scaling * self.lora_b(
                self.lora_a(self.lora_dropout(values))
            )

    return LoRALinear(base).to(device=base.weight.device, dtype=base.weight.dtype)


def build_model_and_head(prototypes):
    import torch
    from torch import nn
    from torch.nn import functional as F

    model = torch.hub.load(
        "facebookresearch/dinov2", "dinov2_vitb14"
    ).cuda()
    for parameter in model.parameters():
        parameter.requires_grad = False
    last = model.blocks[-1]
    last.attn.qkv = make_lora_linear(last.attn.qkv)
    last.attn.proj = make_lora_linear(last.attn.proj)
    last.mlp.fc1 = make_lora_linear(last.mlp.fc1)
    last.mlp.fc2 = make_lora_linear(last.mlp.fc2)

    class CosineHead(nn.Module):
        def __init__(self, initial):
            super().__init__()
            self.weight = nn.Parameter(
                torch.as_tensor(initial, dtype=torch.float32)
            )

        def forward(self, features):
            return HEAD_SCALE * F.normalize(features, dim=-1) @ F.normalize(
                self.weight, dim=-1
            ).T

    head = CosineHead(prototypes).cuda()
    trainable = [p for p in model.parameters() if p.requires_grad]
    expected_lora = sum(p.numel() for p in trainable)
    if expected_lora != 98304:
        raise RuntimeError(f"unexpected LoRA parameter count {expected_lora}")
    return model, head, trainable


def class_prototypes(features, labels):
    return l2_normalize(
        np.stack(
            [
                features[labels == class_index].mean(axis=0)
                for class_index in range(CLASSES)
            ]
        )
    )


def train_fold(
    model,
    head,
    lora_parameters,
    loader,
    frozen_features,
    epochs,
    fold,
):
    import torch
    from torch.nn import functional as F

    optimizer = torch.optim.AdamW(
        [
            {"params": lora_parameters, "lr": LORA_LR},
            {"params": head.parameters(), "lr": HEAD_LR},
        ],
        weight_decay=WEIGHT_DECAY,
    )
    steps = max(1, epochs * len(loader))
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
        optimizer, T_max=steps
    )
    scaler = torch.amp.GradScaler("cuda")
    frozen_gpu = torch.as_tensor(
        frozen_features, dtype=torch.float32, device="cuda"
    )
    epoch_records = []
    for epoch in range(epochs):
        model.train()
        head.train()
        total_loss = total_correct = total_examples = 0
        for images, indices, labels in loader:
            images = images.cuda(non_blocking=True)
            indices = indices.cuda(non_blocking=True)
            labels = labels.cuda(non_blocking=True)
            optimizer.zero_grad(set_to_none=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                adapted = model.forward_features(images)["x_norm_clstoken"]
                logits = head(adapted)
                classification = F.cross_entropy(
                    logits, labels, label_smoothing=LABEL_SMOOTHING
                )
                target = frozen_gpu[indices]
                trust = (
                    1.0 - (F.normalize(adapted, dim=-1) * target).sum(dim=-1)
                ).mean()
                loss = classification + TRUST_WEIGHT * trust
            scaler.scale(loss).backward()
            scaler.step(optimizer)
            scaler.update()
            scheduler.step()
            total_loss += float(loss.detach()) * len(labels)
            total_correct += int((logits.argmax(dim=1) == labels).sum())
            total_examples += len(labels)
        record = {
            "fold": fold,
            "epoch": epoch + 1,
            "loss": total_loss / total_examples,
            "train_accuracy": total_correct / total_examples,
            "lora_lr": optimizer.param_groups[0]["lr"],
            "head_lr": optimizer.param_groups[1]["lr"],
        }
        epoch_records.append(record)
        print(json.dumps({"status": "PEFT_EPOCH_COMPLETE", **record}), flush=True)
    return epoch_records


def extract_adapted_features(model, loader, total):
    import torch

    store = np.full((total, DIMENSION), np.nan, dtype=np.float32)
    model.eval()
    with torch.inference_mode():
        for images, indices in loader:
            images = images.cuda(non_blocking=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                adapted = model.forward_features(images)["x_norm_clstoken"]
            store[indices.numpy()] = adapted.float().cpu().numpy()
    if np.isnan(store).any():
        raise RuntimeError("adapted feature extraction contains NaN")
    return l2_normalize(store)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--feature-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main():
    import torch
    from torch.utils.data import DataLoader

    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    rows = [json.loads(line) for line in args.manifest.read_text().splitlines()]
    if len(rows) != 2000:
        raise RuntimeError(f"expected 2000 rows, got {len(rows)}")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    labels = np.load(args.feature_dir / "labels.npy")
    folds = np.load(args.feature_dir / "folds.npy")
    image_ids = np.load(args.feature_dir / "image_ids.npy")
    frozen = l2_normalize(
        np.load(args.feature_dir / "cls.npy", mmap_mode="r")
    )
    if not np.array_equal(labels, [row["class_index"] for row in rows]):
        raise RuntimeError("manifest/feature labels mismatch")
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True
    torch.backends.cudnn.benchmark = True
    predictions = {
        name: np.full(len(labels), -1, dtype=np.int64)
        for name in ("FROZEN_RBF", "PEFT_HEAD", "PEFT_RBF")
    }
    fold_records = []
    folds_to_run = (0,) if args.smoke else tuple(range(5))
    epochs = 1 if args.smoke else EPOCHS
    eval_loader = DataLoader(
        CUBEvalDataset(args.dataset_root, rows),
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=8,
        pin_memory=True,
        persistent_workers=True,
    )
    for fold in folds_to_run:
        seed = FOLD_SEEDS[fold]
        seed_everything(seed)
        train_indices = np.flatnonzero(folds != fold)
        eval_indices = np.flatnonzero(folds == fold)
        prototypes = class_prototypes(
            frozen[train_indices], labels[train_indices]
        )
        model, head, lora_parameters = build_model_and_head(prototypes)
        train_loader = DataLoader(
            CUBTrainDataset(args.dataset_root, rows, train_indices),
            batch_size=args.batch_size,
            shuffle=True,
            num_workers=8,
            pin_memory=True,
            persistent_workers=True,
            drop_last=False,
            generator=torch.Generator().manual_seed(seed),
        )
        records = train_fold(
            model,
            head,
            lora_parameters,
            train_loader,
            frozen,
            epochs,
            fold,
        )
        adapted = extract_adapted_features(model, eval_loader, len(labels))
        frozen_rbf = SVC(C=3.0, kernel="rbf", gamma="scale").fit(
            frozen[train_indices], labels[train_indices]
        )
        peft_rbf = SVC(C=3.0, kernel="rbf", gamma="scale").fit(
            adapted[train_indices], labels[train_indices]
        )
        predictions["FROZEN_RBF"][eval_indices] = frozen_rbf.predict(
            frozen[eval_indices]
        )
        predictions["PEFT_RBF"][eval_indices] = peft_rbf.predict(
            adapted[eval_indices]
        )
        with torch.inference_mode():
            head_logits = head(
                torch.as_tensor(
                    adapted[eval_indices],
                    dtype=torch.float32,
                    device="cuda",
                )
            )
        predictions["PEFT_HEAD"][eval_indices] = (
            head_logits.argmax(dim=1).cpu().numpy()
        )
        trainable_state = {
            name: value.detach().cpu()
            for name, value in model.state_dict().items()
            if "lora_" in name
        }
        torch.save(
            {
                "fold": fold,
                "seed": seed,
                "protocol_sha256": sha256(args.protocol),
                "lora_state": trainable_state,
                "head_state": head.state_dict(),
            },
            args.output_dir / f"fold_{fold}_peft_state.pt",
        )
        fold_record = {
            "fold": fold,
            "seed": seed,
            "epochs": records,
            "eval_images": len(eval_indices),
            "frozen_rbf_ba": balanced_accuracy(
                labels[eval_indices],
                predictions["FROZEN_RBF"][eval_indices],
            ),
            "peft_head_ba": balanced_accuracy(
                labels[eval_indices],
                predictions["PEFT_HEAD"][eval_indices],
            ),
            "peft_rbf_ba": balanced_accuracy(
                labels[eval_indices],
                predictions["PEFT_RBF"][eval_indices],
            ),
        }
        fold_records.append(fold_record)
        print(json.dumps({"status": "PEFT_FOLD_COMPLETE", **fold_record}), flush=True)
        del model, head, adapted
        torch.cuda.empty_cache()

    completed = np.isin(folds, folds_to_run)
    metrics = {
        name: balanced_accuracy(labels[completed], value[completed])
        for name, value in predictions.items()
    }
    reference_recall = class_recall(
        labels[completed], predictions["FROZEN_RBF"][completed]
    )
    candidate_recall = class_recall(
        labels[completed], predictions["PEFT_RBF"][completed]
    )
    delta = candidate_recall - reference_recall
    gain_pp = 100.0 * (metrics["PEFT_RBF"] - metrics["FROZEN_RBF"])
    negative_rate = float(np.mean(delta < 0))
    worst_drop = float(delta.min())
    summary = {
        "experiment_id": protocol["experiment_id"],
        "mode": "smoke" if args.smoke else "formal",
        "folds_completed": list(folds_to_run),
        "predictions_completed": int(completed.sum()),
        "metrics": metrics,
        "peft_rbf_gain_pp_vs_frozen": gain_pp,
        "negative_class_rate": negative_rate,
        "worst_class_recall_drop": worst_drop,
        "screen_success": bool(
            not args.smoke
            and gain_pp >= 1.0
            and negative_rate <= 0.25
            and worst_drop >= -0.3
        ),
        "fold_records": fold_records,
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
    }
    np.savez_compressed(
        args.output_dir
        / ("smoke_predictions.npz" if args.smoke else "formal_predictions.npz"),
        labels=labels[completed],
        image_ids=image_ids[completed],
        **{
            f"{name}_predictions": value[completed]
            for name, value in predictions.items()
        },
    )
    (args.output_dir / ("smoke_summary.json" if args.smoke else "summary.json")).write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
