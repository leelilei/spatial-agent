#!/usr/bin/env python3
"""Extract frozen DINOv2 features after verifying the immutable test lock."""

from __future__ import annotations

import argparse
import hashlib
import json
import time
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
    if not rows or any(row.get("split") != "test" or row.get("source_split") != "official_test" for row in rows):
        raise RuntimeError("only locked official-test manifests are permitted")
    return rows


class LockedOfficialTestImages(Dataset):
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
        image = TF.resize(image, [IMAGE_SIZE, IMAGE_SIZE], interpolation=InterpolationMode.BICUBIC, antialias=True)
        image = TF.normalize(TF.to_tensor(image), MEAN, STD)
        return image, index


def main() -> None:
    import torch

    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--model-name", required=True)
    parser.add_argument("--hub-repo", type=Path, required=True)
    parser.add_argument("--lock", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=4)
    args = parser.parse_args()
    lock = json.loads(args.lock.read_text())
    if lock.get("status") != "LOCKED_BEFORE_OFFICIAL_TEST_IMAGE_DECODING":
        raise RuntimeError("official-test lock is not sealed")
    manifest_hash = sha256(args.manifest)
    known = lock["manifest_sha256"]
    if manifest_hash not in set(known.get("cub", {}).values()) | set(known.get("stanford_dogs", {}).values()):
        raise RuntimeError("manifest is not listed in the immutable lock")
    rows = load_rows(args.manifest)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    model = torch.hub.load(str(args.hub_repo), args.model_name, source="local", pretrained=True).eval().cuda()
    for parameter in model.parameters():
        parameter.requires_grad = False
    features = np.lib.format.open_memmap(args.output_dir / "cls.npy", mode="w+", dtype=np.float32, shape=(len(rows), int(model.embed_dim)))
    loader = DataLoader(LockedOfficialTestImages(args.dataset_root, rows), batch_size=args.batch_size, shuffle=False, num_workers=8, pin_memory=True, persistent_workers=True)
    complete = 0
    if torch.cuda.is_available():
        torch.cuda.reset_peak_memory_stats()
        torch.cuda.synchronize()
    start = time.perf_counter()
    with torch.inference_mode():
        for images, indices in loader:
            images = images.cuda(non_blocking=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                output = model.forward_features(images)["x_norm_clstoken"]
            features[indices.numpy()] = output.float().cpu().numpy()
            complete += len(indices)
            if complete % 200 == 0 or complete == len(rows):
                print(json.dumps({"images_complete": complete, "images_total": len(rows)}), flush=True)
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    elapsed = time.perf_counter() - start
    features.flush()
    np.save(args.output_dir / "labels.npy", np.asarray([row["class_index"] for row in rows]))
    np.save(args.output_dir / "folds.npy", np.asarray([row["fold"] for row in rows]))
    np.save(args.output_dir / "image_ids.npy", np.asarray([row["image_id"] for row in rows]))
    metadata = {
        "model_name": args.model_name,
        "feature_dim": int(model.embed_dim),
        "images": len(rows),
        "input_size": IMAGE_SIZE,
        "manifest_sha256": manifest_hash,
        "lock_sha256": sha256(args.lock),
        "official_test_images_decoded_or_encoded": len(rows),
        "feature_extraction_seconds": elapsed,
        "feature_extraction_seconds_per_image": elapsed / len(rows),
        "peak_gpu_memory_bytes": int(torch.cuda.max_memory_allocated()) if torch.cuda.is_available() else 0,
    }
    (args.output_dir / "metadata.json").write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    print(json.dumps(metadata, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
