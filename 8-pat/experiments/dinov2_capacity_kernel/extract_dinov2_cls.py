#!/usr/bin/env python3
"""Extract train-only DINOv2 CLS features for capacity comparisons."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image
from torch.utils.data import DataLoader, Dataset


IMAGE_SIZE = 392
MEAN = (0.485, 0.456, 0.406)
STD = (0.229, 0.224, 0.225)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_rows(path: Path) -> list[dict]:
    rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    if not rows:
        raise ValueError("manifest is empty")
    for row in rows:
        if row.get("split") != "train" or row.get("source_split") != "official_train":
            raise RuntimeError("only CUB official-train rows are permitted")
    return rows


class TrainOnlyImages(Dataset):
    def __init__(self, root: Path, rows: list[dict]):
        self.root = root
        self.rows = rows

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, index):
        from torchvision.transforms import InterpolationMode
        from torchvision.transforms import functional as TF

        row = self.rows[index]
        with Image.open(self.root / row["relative_path"]) as source:
            image = source.convert("RGB")
        image = TF.resize(
            image,
            [IMAGE_SIZE, IMAGE_SIZE],
            interpolation=InterpolationMode.BICUBIC,
            antialias=True,
        )
        image = TF.normalize(TF.to_tensor(image), MEAN, STD)
        return image, index


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--model-name", required=True)
    parser.add_argument("--hub-repo", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=4)
    return parser.parse_args()


def main():
    import torch

    args = parse_args()
    rows = load_rows(args.manifest)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    model = torch.hub.load(
        str(args.hub_repo), args.model_name, source="local", pretrained=True
    ).eval().cuda()
    for parameter in model.parameters():
        parameter.requires_grad = False
    feature_dim = int(model.embed_dim)
    features = np.lib.format.open_memmap(
        args.output_dir / "cls.npy",
        mode="w+",
        dtype=np.float32,
        shape=(len(rows), feature_dim),
    )
    dataset = TrainOnlyImages(args.dataset_root, rows)
    loader = DataLoader(
        dataset,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=8,
        pin_memory=True,
        persistent_workers=True,
    )
    complete = 0
    with torch.inference_mode():
        for images, indices in loader:
            images = images.cuda(non_blocking=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                output = model.forward_features(images)["x_norm_clstoken"]
            idx = indices.numpy()
            features[idx] = output.float().cpu().numpy()
            complete += len(idx)
            if complete % 200 == 0 or complete == len(rows):
                print(json.dumps({"images_complete": complete, "images_total": len(rows)}), flush=True)
    features.flush()
    np.save(args.output_dir / "labels.npy", np.asarray([r["class_index"] for r in rows]))
    np.save(args.output_dir / "folds.npy", np.asarray([r["fold"] for r in rows]))
    np.save(args.output_dir / "image_ids.npy", np.asarray([r["image_id"] for r in rows]))
    metadata = {
        "model_name": args.model_name,
        "feature_dim": feature_dim,
        "images": len(rows),
        "input_size": IMAGE_SIZE,
        "manifest_sha256": sha256(args.manifest),
        "official_test_images_decoded_or_encoded": 0,
    }
    (args.output_dir / "metadata.json").write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
