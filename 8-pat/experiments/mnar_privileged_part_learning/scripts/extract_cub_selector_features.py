#!/usr/bin/env python3
"""Extract frozen ordinary-image ResNet-50 features for PAT-D-260728-005."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from PIL import Image
from torch.utils.data import DataLoader, Dataset
from torchvision.models import ResNet50_Weights, resnet50

from cub_active_selection import (
    load_and_sanitize_manifest,
    sha256_file,
    write_selector_manifest,
)


class SelectorImageDataset(Dataset):
    def __init__(self, dataset_root: Path, rows: list[dict], transform):
        self.dataset_root = dataset_root
        self.rows = rows
        self.transform = transform

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, index):
        row = self.rows[index]
        with Image.open(self.dataset_root / row["relative_path"]) as source:
            image = source.convert("RGB")
        return self.transform(image), index


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--workers", type=int, default=8)
    return parser.parse_args()


def main():
    args = parse_args()
    rows = load_and_sanitize_manifest(args.manifest)
    if any(
        row["relative_path"].lower().find("/test/") >= 0 for row in rows
    ):
        raise RuntimeError("Selector feature extraction may not inspect test")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    selector_manifest = args.output_dir / "cub_selector_manifest.jsonl"
    write_selector_manifest(rows, selector_manifest)

    weights = ResNet50_Weights.IMAGENET1K_V2
    model = resnet50(weights=weights)
    model.fc = nn.Identity()
    model = model.cuda().eval()
    dataset = SelectorImageDataset(
        args.dataset_root, rows, weights.transforms(crop_size=384)
    )
    loader = DataLoader(
        dataset,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=args.workers,
        pin_memory=True,
        persistent_workers=args.workers > 0,
    )
    features = np.empty((len(rows), 2048), dtype=np.float32)
    seen = np.zeros(len(rows), dtype=np.bool_)
    with torch.inference_mode():
        for images, indices in loader:
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                output = model(images.cuda(non_blocking=True))
            batch_indices = indices.numpy()
            features[batch_indices] = output.float().cpu().numpy()
            seen[batch_indices] = True
    if not seen.all() or not np.isfinite(features).all():
        raise RuntimeError("Feature extraction incomplete or non-finite")

    output = args.output_dir / "cub_selector_resnet50_features.npz"
    np.savez_compressed(
        output,
        features=features,
        labels=np.asarray([row["class_index"] for row in rows]),
        folds=np.asarray([row["fold"] for row in rows]),
        image_ids=np.asarray([row["image_id"] for row in rows]),
        relative_paths=np.asarray([row["relative_path"] for row in rows]),
    )
    summary = {
        "rows": len(rows),
        "feature_dimension": features.shape[1],
        "feature_model": "ResNet50_Weights.IMAGENET1K_V2",
        "selector_manifest_sha256": sha256_file(selector_manifest),
        "feature_file_sha256": sha256_file(output),
        "keypoint_fields_exposed_to_dataset": 0,
        "official_test_images_decoded_or_encoded": 0,
    }
    (args.output_dir / "cub_selector_feature_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
