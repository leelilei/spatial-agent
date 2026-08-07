#!/usr/bin/env python3
"""Encode frozen global CLIP features for train/validation shift analysis."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import torch
from PIL import Image, ImageOps


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TOGA_ROOT = Path(
    os.environ.get("TOGA_ROOT", str(PROJECT_ROOT / "vendor" / "TOGA"))
)
sys.path.insert(0, str(TOGA_ROOT))
import clip as openai_clip  # noqa: E402


STYLE_ID_TO_INDEX = {
    "Q46261": 0,
    "Q176483": 1,
    "Q236122": 2,
    "Q840829": 3,
}
STYLE_NAMES = ("Romanesque", "Gothic", "Renaissance", "Baroque")


def read_split(path: Path) -> tuple[list[str], torch.Tensor]:
    names = []
    labels = []
    with path.open(encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            fields = line.split()
            if len(fields) != 2 or fields[1] not in STYLE_ID_TO_INDEX:
                raise ValueError(f"{path}:{line_number}: invalid row")
            names.append(fields[0])
            labels.append(STYLE_ID_TO_INDEX[fields[1]])
    if len(names) != len(set(names)):
        raise RuntimeError(f"Duplicate image in {path}")
    return names, torch.tensor(labels, dtype=torch.long)


def encode(
    names: list[str],
    image_dir: Path,
    model: torch.nn.Module,
    preprocess,
    device: torch.device,
    batch_size: int,
) -> torch.Tensor:
    outputs = []
    with torch.inference_mode():
        for start in range(0, len(names), batch_size):
            batch_names = names[start : start + batch_size]
            images = torch.stack(
                [
                    preprocess(
                        ImageOps.exif_transpose(
                            Image.open(image_dir / name)
                        ).convert("RGB")
                    )
                    for name in batch_names
                ]
            ).to(device)
            features = model.encode_image(images).float()
            features = features / features.norm(
                dim=-1,
                keepdim=True,
            ).clamp_min(1e-12)
            outputs.append(features.cpu())
            print(
                f"global_encoded={min(start + batch_size, len(names))}/"
                f"{len(names)}",
                flush=True,
            )
    return torch.cat(outputs)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--image-dir", type=Path, required=True)
    parser.add_argument("--labels-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--out-file", type=Path, required=True)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--batch-size", type=int, default=64)
    args = parser.parse_args()

    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    train_names, train_labels = read_split(args.labels_dir / "wc4_train.txt")
    val_names, val_labels = read_split(args.labels_dir / "wc4_val.txt")
    if set(train_names) & set(val_names):
        raise RuntimeError("Train/validation image overlap")
    missing = [
        name
        for name in train_names + val_names
        if not (args.image_dir / name).is_file()
    ]
    if missing:
        raise FileNotFoundError(f"Missing images: {missing[:5]}")

    device = torch.device(args.device)
    model, preprocess = openai_clip.load("ViT-B/16", device=device)
    model.eval()
    train_features = encode(
        train_names,
        args.image_dir,
        model,
        preprocess,
        device,
        args.batch_size,
    )
    val_features = encode(
        val_names,
        args.image_dir,
        model,
        preprocess,
        device,
        args.batch_size,
    )
    output = {
        "experiment_id": protocol["experiment_id"],
        "model": "ViT-B/16",
        "style_names": STYLE_NAMES,
        "train_names": train_names,
        "train_labels": train_labels,
        "train_features": train_features,
        "val_names": val_names,
        "val_labels": val_labels,
        "val_features": val_features,
        "test_images_encoded": 0,
    }
    args.out_file.parent.mkdir(parents=True, exist_ok=True)
    torch.save(output, args.out_file)
    summary = {
        "experiment_id": protocol["experiment_id"],
        "model": output["model"],
        "feature_dimension": train_features.shape[1],
        "train_images": len(train_names),
        "validation_images": len(val_names),
        "test_images_encoded": 0,
    }
    args.out_file.with_suffix(".json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
