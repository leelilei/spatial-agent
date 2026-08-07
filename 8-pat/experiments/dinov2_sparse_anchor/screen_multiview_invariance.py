#!/usr/bin/env python3
"""Deterministic multi-view DINOv2 feature-consensus screen."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image
from sklearn.svm import SVC

from sparse_anchor_utils import balanced_accuracy, class_recall, l2_normalize


IMAGE_SIZE = 392
RESIZE_SHORT = 448
FEATURE_DIM = 768
NORMALIZE_MEAN = (0.485, 0.456, 0.406)
NORMALIZE_STD = (0.229, 0.224, 0.225)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class MultiViewDataset:
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
            raise RuntimeError("screen may decode official train only")
        with Image.open(self.root / row["relative_path"]) as source:
            image = source.convert("RGB")
        stretch = TF.resize(
            image,
            [IMAGE_SIZE, IMAGE_SIZE],
            interpolation=InterpolationMode.BICUBIC,
            antialias=True,
        )
        center = TF.center_crop(
            TF.resize(
                image,
                RESIZE_SHORT,
                interpolation=InterpolationMode.BICUBIC,
                antialias=True,
            ),
            [IMAGE_SIZE, IMAGE_SIZE],
        )
        views = [
            stretch,
            TF.hflip(stretch),
            center,
            TF.hflip(center),
        ]
        tensors = [
            TF.normalize(TF.to_tensor(view), NORMALIZE_MEAN, NORMALIZE_STD)
            for view in views
        ]
        return np.stack(tensors), index


def extract_views(dataset_root, manifest, feature_dir, batch_size):
    import torch
    from torch.utils.data import DataLoader

    rows = [json.loads(line) for line in manifest.read_text().splitlines()]
    if len(rows) != 2000:
        raise RuntimeError(f"expected 2000 rows, got {len(rows)}")
    manifest_hash = sha256(manifest)
    metadata_path = feature_dir / "metadata.json"
    views_path = feature_dir / "multiview_cls.npy"
    if views_path.exists() and metadata_path.exists():
        metadata = json.loads(metadata_path.read_text())
        if metadata.get("manifest_sha256") == manifest_hash:
            print(json.dumps({"status": "MULTIVIEW_CACHE_RESUMED"}))
            return
    feature_dir.mkdir(parents=True, exist_ok=True)
    model = torch.hub.load("facebookresearch/dinov2", "dinov2_vitb14").eval().cuda()
    for parameter in model.parameters():
        parameter.requires_grad = False
    loader = DataLoader(
        MultiViewDataset(dataset_root, rows),
        batch_size=batch_size,
        shuffle=False,
        num_workers=8,
        pin_memory=True,
        persistent_workers=True,
    )
    store = np.lib.format.open_memmap(
        views_path,
        mode="w+",
        dtype=np.float32,
        shape=(len(rows), 4, FEATURE_DIM),
    )
    complete = 0
    with torch.inference_mode():
        for views, indices in loader:
            batch, count, channels, height, width = views.shape
            views = views.reshape(batch * count, channels, height, width).cuda(
                non_blocking=True
            )
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                cls = model.forward_features(views)["x_norm_clstoken"]
            cls = cls.float().cpu().numpy().reshape(batch, count, FEATURE_DIM)
            store[indices.numpy()] = cls
            complete += batch
            if complete % 400 == 0 or complete == len(rows):
                print(
                    json.dumps(
                        {
                            "status": "MULTIVIEW_EXTRACTION",
                            "images_complete": complete,
                            "images_total": len(rows),
                        }
                    ),
                    flush=True,
                )
    store.flush()
    metadata_path.write_text(
        json.dumps(
            {
                "backbone": "dinov2_vitb14",
                "images": len(rows),
                "views": ["stretch", "stretch_flip", "center", "center_flip"],
                "manifest_sha256": manifest_hash,
                "official_test_images_decoded_or_encoded": 0,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
    del model
    torch.cuda.empty_cache()


def class_bootstrap_interval(delta, seed=9524, draws=20000):
    rng = np.random.default_rng(seed)
    indices = rng.integers(0, len(delta), (draws, len(delta)))
    values = delta[indices].mean(axis=1) * 100.0
    return [float(x) for x in np.quantile(values, [0.025, 0.5, 0.975])]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--base-feature-dir", type=Path, required=True)
    parser.add_argument("--feature-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=4)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    extract_views(args.dataset_root, args.manifest, args.feature_dir, args.batch_size)
    labels = np.load(args.base_feature_dir / "labels.npy")
    folds = np.load(args.base_feature_dir / "folds.npy")
    image_ids = np.load(args.base_feature_dir / "image_ids.npy")
    base = l2_normalize(np.load(args.base_feature_dir / "cls.npy", mmap_mode="r"))
    views = l2_normalize(
        np.load(args.feature_dir / "multiview_cls.npy", mmap_mode="r")
    )
    if not np.allclose(base, views[:, 0], atol=2e-3, rtol=2e-3):
        raise RuntimeError("stretch view does not reproduce frozen base feature")
    feature_arms = {
        "SINGLE_STRETCH": base,
        "CONSENSUS_STRETCH_FLIP": l2_normalize(views[:, :2].mean(axis=1)),
        "CONSENSUS_CENTER_FLIP": l2_normalize(views[:, 2:].mean(axis=1)),
        "CONSENSUS_ALL4": l2_normalize(views.mean(axis=1)),
    }
    predictions = {
        name: np.full(len(labels), -1, dtype=np.int64) for name in feature_arms
    }
    for fold in range(5):
        train = np.flatnonzero(folds != fold)
        evaluate_on = np.flatnonzero(folds == fold)
        for name, features in feature_arms.items():
            model = SVC(C=3.0, kernel="rbf", gamma="scale").fit(
                features[train], labels[train]
            )
            predictions[name][evaluate_on] = model.predict(features[evaluate_on])
        print(json.dumps({"status": "MULTIVIEW_FOLD_COMPLETE", "fold": fold}), flush=True)
    metrics = {
        name: balanced_accuracy(labels, prediction)
        for name, prediction in predictions.items()
    }
    baseline_name = "SINGLE_STRETCH"
    candidate_names = [name for name in metrics if name != baseline_name]
    best_arm = max(candidate_names, key=metrics.__getitem__)
    gain_pp = 100.0 * (metrics[best_arm] - metrics[baseline_name])
    baseline_recall = class_recall(labels, predictions[baseline_name])
    winner_recall = class_recall(labels, predictions[best_arm])
    delta = winner_recall - baseline_recall
    summary = {
        "experiment_id": protocol["experiment_id"],
        "metrics": metrics,
        "best_arm": best_arm,
        "gain_pp_vs_single_view_rbf": gain_pp,
        "screen_success": bool(gain_pp >= 0.5),
        "winner_positive_classes": int(np.sum(delta > 0)),
        "winner_negative_classes": int(np.sum(delta < 0)),
        "winner_class_bootstrap_delta_pp": class_bootstrap_interval(delta),
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
    }
    np.savez_compressed(
        args.output_dir / "multiview_predictions.npz",
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
