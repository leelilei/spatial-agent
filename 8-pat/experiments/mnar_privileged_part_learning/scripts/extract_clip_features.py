#!/usr/bin/env python3
"""Extract frozen OpenAI CLIP ViT-B/16 global and final patch features."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import open_clip
import torch
import torch.nn.functional as F
from PIL import Image
from torch.utils.data import DataLoader, Dataset


class ManifestImages(Dataset):
    def __init__(self, root: Path, manifest: Path, transform):
        self.root = root
        self.transform = transform
        self.rows = [
            json.loads(line)
            for line in manifest.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    def __len__(self) -> int:
        return len(self.rows)

    def __getitem__(self, index: int):
        row = self.rows[index]
        if row["split"] == "test":
            raise RuntimeError("PAT-C-260728-001 forbids test image decoding.")
        path = self.root / row["relative_path"]
        with Image.open(path) as image:
            tensor = self.transform(image.convert("RGB"))
        return tensor, int(row["row_index"])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--cache-dir", type=Path, default=Path("/root/workspace/models/open_clip")
    )
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--workers", type=int, default=8)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    model, _, preprocess = open_clip.create_model_and_transforms(
        "ViT-B-16-quickgelu",
        pretrained="openai",
        cache_dir=str(args.cache_dir),
        device="cuda",
        precision="fp16",
    )
    model.eval()
    dataset = ManifestImages(args.dataset_root, args.manifest, preprocess)
    loader = DataLoader(
        dataset,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=args.workers,
        pin_memory=True,
        persistent_workers=args.workers > 0,
    )
    global_features: np.ndarray | None = None
    patch_features: np.ndarray | None = None
    seen = np.zeros(len(dataset), dtype=np.bool_)

    with torch.inference_mode():
        for batch_number, (images, row_indices) in enumerate(loader, start=1):
            images = images.cuda(non_blocking=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                output = model.visual.forward_intermediates(
                    images,
                    indices=1,
                    normalize_intermediates=True,
                    output_fmt="NLC",
                )
                global_batch = F.normalize(
                    output["image_features"].float(), dim=-1
                )
                patch_batch = F.normalize(
                    output["image_intermediates"][-1].float(), dim=-1
                )
            if global_features is None:
                global_features = np.empty(
                    (len(dataset), global_batch.shape[-1]), dtype=np.float16
                )
                patch_features = np.empty(
                    (
                        len(dataset),
                        patch_batch.shape[1],
                        patch_batch.shape[2],
                    ),
                    dtype=np.float16,
                )
            indices = row_indices.numpy()
            global_features[indices] = global_batch.cpu().numpy().astype(np.float16)
            patch_features[indices] = patch_batch.cpu().numpy().astype(np.float16)
            seen[indices] = True
            print(
                f"batch={batch_number}/{len(loader)} "
                f"encoded={int(seen.sum())}/{len(dataset)}",
                flush=True,
            )

    if global_features is None or patch_features is None or not seen.all():
        raise RuntimeError("Feature extraction did not cover the full manifest.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        args.output,
        global_features=global_features,
        patch_features=patch_features,
        row_indices=np.arange(len(dataset), dtype=np.int32),
        encoder=np.asarray(["open_clip:ViT-B-16-quickgelu:openai"]),
        test_images_encoded=np.asarray([0], dtype=np.int8),
    )
    print(
        json.dumps(
            {
                "output": str(args.output),
                "images": len(dataset),
                "global_shape": list(global_features.shape),
                "patch_shape": list(patch_features.shape),
                "test_images_encoded": 0,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
