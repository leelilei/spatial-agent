#!/usr/bin/env python3
"""Untouched-episode confirmation of frozen dual-geometry rank fusion."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image
from sklearn.linear_model import RidgeClassifier
from sklearn.svm import SVC

from sparse_anchor_utils import balanced_accuracy, class_recall, l2_normalize


IMAGE_SIZE = 392
FEATURE_DIM = 768
CLASSES = 200
NORMALIZE_MEAN = (0.485, 0.456, 0.406)
NORMALIZE_STD = (0.229, 0.224, 0.225)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def zscore_rows(scores: np.ndarray) -> np.ndarray:
    scores = np.asarray(scores, dtype=np.float64)
    return (scores - scores.mean(axis=1, keepdims=True)) / np.maximum(
        scores.std(axis=1, keepdims=True), 1e-12
    )


def descending_rank_scores(scores: np.ndarray) -> np.ndarray:
    order = np.argsort(-scores, axis=1)
    ranks = np.empty_like(order)
    rows = np.arange(len(scores))[:, None]
    ranks[rows, order] = np.arange(scores.shape[1])[None, :]
    return -ranks.astype(np.float64)


class EpisodeDataset:
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
            raise RuntimeError("confirmation may decode official train only")
        with Image.open(self.root / row["relative_path"]) as source:
            image = source.convert("RGB")
        image = TF.resize(
            image,
            [IMAGE_SIZE, IMAGE_SIZE],
            interpolation=InterpolationMode.BICUBIC,
            antialias=True,
        )
        return TF.normalize(TF.to_tensor(image), NORMALIZE_MEAN, NORMALIZE_STD), index


def extract_episode(model, dataset_root, manifest, feature_dir, batch_size):
    import torch
    from torch.utils.data import DataLoader

    rows = [json.loads(line) for line in manifest.read_text().splitlines()]
    if len(rows) != 2000:
        raise RuntimeError(f"expected 2000 rows in {manifest}, got {len(rows)}")
    manifest_hash = sha256(manifest)
    metadata_path = feature_dir / "metadata.json"
    required = [
        feature_dir / "cls.npy",
        feature_dir / "labels.npy",
        feature_dir / "folds.npy",
        feature_dir / "image_ids.npy",
        metadata_path,
    ]
    if all(path.exists() for path in required):
        metadata = json.loads(metadata_path.read_text())
        if metadata.get("manifest_sha256") == manifest_hash:
            print(json.dumps({"status": "FEATURE_CACHE_RESUMED", "manifest": str(manifest)}))
            return
    feature_dir.mkdir(parents=True, exist_ok=True)
    loader = DataLoader(
        EpisodeDataset(dataset_root, rows),
        batch_size=batch_size,
        shuffle=False,
        num_workers=8,
        pin_memory=True,
        persistent_workers=True,
    )
    store = np.lib.format.open_memmap(
        feature_dir / "cls.npy",
        mode="w+",
        dtype=np.float32,
        shape=(len(rows), FEATURE_DIM),
    )
    complete = 0
    with torch.inference_mode():
        for images, indices in loader:
            images = images.cuda(non_blocking=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                cls = model.forward_features(images)["x_norm_clstoken"]
            idx = indices.numpy()
            store[idx] = cls.float().cpu().numpy()
            complete += len(idx)
            if complete % 400 == 0 or complete == len(rows):
                print(
                    json.dumps(
                        {
                            "status": "FEATURE_EXTRACTION",
                            "manifest": str(manifest),
                            "images_complete": complete,
                            "images_total": len(rows),
                        }
                    ),
                    flush=True,
                )
    store.flush()
    np.save(feature_dir / "labels.npy", [row["class_index"] for row in rows])
    np.save(feature_dir / "folds.npy", [row["fold"] for row in rows])
    np.save(feature_dir / "image_ids.npy", [row["image_id"] for row in rows])
    metadata_path.write_text(
        json.dumps(
            {
                "backbone": "dinov2_vitb14",
                "images": len(rows),
                "input_size": IMAGE_SIZE,
                "manifest_sha256": manifest_hash,
                "official_test_images_decoded_or_encoded": 0,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )


def prototype_scores(train_x, train_y, eval_x):
    prototypes = np.stack(
        [train_x[train_y == label].mean(axis=0) for label in range(CLASSES)]
    )
    return eval_x @ l2_normalize(prototypes).T


def evaluate_episode(feature_dir):
    labels = np.load(feature_dir / "labels.npy")
    folds = np.load(feature_dir / "folds.npy")
    image_ids = np.load(feature_dir / "image_ids.npy")
    features = l2_normalize(np.load(feature_dir / "cls.npy", mmap_mode="r"))
    rbf_scores = np.full((len(labels), CLASSES), np.nan, dtype=np.float32)
    ridge_scores = np.full_like(rbf_scores, np.nan)
    proto_scores = np.full_like(rbf_scores, np.nan)
    for fold in range(5):
        train = np.flatnonzero(folds != fold)
        evaluate_on = np.flatnonzero(folds == fold)
        rbf = SVC(C=3.0, kernel="rbf", gamma="scale").fit(
            features[train], labels[train]
        )
        ridge = RidgeClassifier(alpha=0.1).fit(features[train], labels[train])
        rbf_scores[evaluate_on] = rbf.decision_function(
            features[evaluate_on]
        ).astype(np.float32)
        ridge_scores[evaluate_on] = ridge.decision_function(
            features[evaluate_on]
        ).astype(np.float32)
        proto_scores[evaluate_on] = prototype_scores(
            features[train], labels[train], features[evaluate_on]
        ).astype(np.float32)
        print(json.dumps({"status": "CONFIRM_FOLD_COMPLETE", "fold": fold}), flush=True)
    rbf_z = zscore_rows(rbf_scores)
    linear = zscore_rows(zscore_rows(ridge_scores) + 0.75 * zscore_rows(proto_scores))
    fused = descending_rank_scores(rbf_z) + 0.5 * descending_rank_scores(linear)
    predictions = {
        "RBF_CLS_C3": rbf_z.argmax(axis=1),
        "RIDGE_PROTO": linear.argmax(axis=1),
        "RANK_W0.5": fused.argmax(axis=1),
    }
    metrics = {
        name: balanced_accuracy(labels, prediction)
        for name, prediction in predictions.items()
    }
    baseline_recall = class_recall(labels, predictions["RBF_CLS_C3"])
    winner_recall = class_recall(labels, predictions["RANK_W0.5"])
    delta = winner_recall - baseline_recall
    return {
        "metrics": metrics,
        "gain_pp": 100.0 * (metrics["RANK_W0.5"] - metrics["RBF_CLS_C3"]),
        "positive_classes": int(np.sum(delta > 0)),
        "negative_classes": int(np.sum(delta < 0)),
    }, labels, image_ids, predictions


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--episode2-manifest", type=Path, required=True)
    parser.add_argument("--episode3-manifest", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--feature-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=16)
    return parser.parse_args()


def main():
    import torch

    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True
    torch.backends.cudnn.benchmark = True
    model = torch.hub.load("facebookresearch/dinov2", "dinov2_vitb14").eval().cuda()
    for parameter in model.parameters():
        parameter.requires_grad = False
    manifests = {2: args.episode2_manifest, 3: args.episode3_manifest}
    for episode, manifest in manifests.items():
        extract_episode(
            model,
            args.dataset_root,
            manifest,
            args.feature_root / f"episode_{episode}",
            args.batch_size,
        )
    del model
    torch.cuda.empty_cache()

    episode_results = {
        "1": {
            "metrics": {"RBF_CLS_C3": 0.861, "RANK_W0.5": 0.866},
            "gain_pp": 0.5,
            "source": "PAT-H-260729-004 frozen screen",
        }
    }
    prediction_payload = {}
    for episode in (2, 3):
        result, labels, image_ids, predictions = evaluate_episode(
            args.feature_root / f"episode_{episode}"
        )
        episode_results[str(episode)] = result
        prediction_payload[f"episode_{episode}_labels"] = labels
        prediction_payload[f"episode_{episode}_image_ids"] = image_ids
        for name, value in predictions.items():
            prediction_payload[f"episode_{episode}_{name}_predictions"] = value
    gains = np.asarray(
        [episode_results[str(episode)]["gain_pp"] for episode in (1, 2, 3)]
    )
    gate = bool(
        gains.mean() >= 0.3
        and np.sum(gains > 0) >= 2
        and gains.min() >= -0.25
    )
    summary = {
        "experiment_id": protocol["experiment_id"],
        "episodes": episode_results,
        "mean_gain_pp": float(gains.mean()),
        "positive_episode_directions": int(np.sum(gains > 0)),
        "worst_episode_gain_pp": float(gains.min()),
        "confirmation_success": gate,
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
    }
    np.savez_compressed(
        args.output_dir / "rank_fusion_confirmation_predictions.npz",
        **prediction_payload,
    )
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
