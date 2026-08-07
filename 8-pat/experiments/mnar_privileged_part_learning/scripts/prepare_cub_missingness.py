#!/usr/bin/env python3
"""Freeze equal-budget CUB keypoint-annotation selections for PAT-D-260728-002."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image
from torch.utils.data import DataLoader

import run_cub_prpool_oof as base


MECHANISMS = ("MCAR", "MAR_X", "MNAR_Z", "SI_HARD")


def ranks(values):
    order = np.argsort(values, kind="stable")
    output = np.empty(len(values), dtype=np.float64)
    output[order] = np.arange(len(values), dtype=np.float64)
    return output / max(1, len(values) - 1)


def softmax_probabilities(values, temperature):
    values = np.asarray(values, dtype=np.float64)
    std = values.std()
    standardized = (values - values.mean()) / (std if std > 1e-12 else 1.0)
    logits = standardized / temperature
    logits -= logits.max()
    weights = np.exp(logits)
    return weights / weights.sum()


def extract_features(root, rows, batch_size):
    dataset = base.CUBTrainOnly(
        root, rows, range(len(rows)), training=False, seed=7601
    )
    loader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=8,
        pin_memory=True,
        persistent_workers=True,
    )
    model = base.ResNetFeatures().cuda().eval()
    features = np.zeros((len(rows), 2048), dtype=np.float32)
    with torch.inference_mode():
        for images, _, _, row_indices in loader:
            images = images.cuda(non_blocking=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                fmap = model(images)
                pooled = F.normalize(
                    F.adaptive_avg_pool2d(fmap, 1).flatten(1), dim=-1
                )
            features[row_indices.numpy()] = pooled.float().cpu().numpy()
    del model
    torch.cuda.empty_cache()
    return features


def keypoint_completeness(root, rows):
    scores = np.zeros(len(rows), dtype=np.float64)
    visible_counts = np.zeros(len(rows), dtype=np.float64)
    coverages = np.zeros(len(rows), dtype=np.float64)
    for index, row in enumerate(rows):
        if row["split"] != "train" or row["source_split"] != "official_train":
            raise RuntimeError("PAT-D-260728-002 may inspect official train only")
        with Image.open(root / row["relative_path"]) as image:
            width, height = image.size
        points = np.asarray(
            [[point[0], point[1]] for point in row["keypoints"] if point[2]],
            dtype=np.float64,
        )
        visible_counts[index] = len(points) / 15.0
        if len(points) >= 2:
            span = points.max(axis=0) - points.min(axis=0)
            coverages[index] = float(
                (span[0] * span[1]) / max(1.0, width * height)
            )
    labels = np.asarray([row["class_index"] for row in rows])
    for class_index in np.unique(labels):
        indices = np.flatnonzero(labels == class_index)
        scores[indices] = 0.7 * ranks(visible_counts[indices]) + 0.3 * ranks(
            coverages[indices]
        )
    return scores, visible_counts, coverages


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=64)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    rows = [json.loads(line) for line in args.manifest.read_text().splitlines()]
    labels = np.asarray([row["class_index"] for row in rows])
    folds = np.asarray([row["fold"] for row in rows])
    if any(
        row["split"] != "train" or row["source_split"] != "official_train"
        for row in rows
    ):
        raise RuntimeError("Manifest is not official-train-only")

    features = extract_features(args.dataset_root, rows, args.batch_size)
    completeness, visible_counts, coverages = keypoint_completeness(
        args.dataset_root, rows
    )
    selection = {
        mechanism: np.zeros((5, len(rows)), dtype=np.bool_)
        for mechanism in MECHANISMS
    }
    typicality = np.full((5, len(rows)), np.nan, dtype=np.float32)
    seed = int(protocol["screening"]["seed"])
    temperature = float(
        protocol["screening"]["temperature_for_weighted_sampling"]
    )

    for fold in range(5):
        for class_index in range(200):
            candidates = np.flatnonzero(
                (labels == class_index) & (folds != fold)
            )
            if len(candidates) != 8:
                raise RuntimeError(
                    f"Expected 8 train candidates, got {len(candidates)}"
                )
            class_features = features[candidates]
            centroid = F.normalize(
                torch.from_numpy(class_features.mean(axis=0)), dim=0
            ).numpy()
            scores_x = class_features @ centroid
            typicality[fold, candidates] = scores_x
            score_z = completeness[candidates]

            mechanism_seed = seed + 10000 * fold + 100 * class_index
            rng_mcar = np.random.default_rng(mechanism_seed + 1)
            rng_mar = np.random.default_rng(mechanism_seed + 2)
            rng_mnar = np.random.default_rng(mechanism_seed + 3)
            chosen = {
                "MCAR": rng_mcar.choice(candidates, 2, replace=False),
                "MAR_X": rng_mar.choice(
                    candidates,
                    2,
                    replace=False,
                    p=softmax_probabilities(scores_x, temperature),
                ),
                "MNAR_Z": rng_mnar.choice(
                    candidates,
                    2,
                    replace=False,
                    p=softmax_probabilities(score_z, temperature),
                ),
            }
            combined = 0.5 * ranks(scores_x) + 0.5 * ranks(score_z)
            top_order = np.lexsort(
                (
                    np.asarray([rows[index]["image_id"] for index in candidates]),
                    -combined,
                )
            )
            chosen["SI_HARD"] = candidates[top_order[:2]]
            for mechanism, indices in chosen.items():
                selection[mechanism][fold, indices] = True

    for mechanism, values in selection.items():
        for fold in range(5):
            selected = values[fold]
            if selected.sum() != 400:
                raise RuntimeError(
                    f"{mechanism} fold {fold}: expected 400 selected"
                )
            per_class = np.bincount(labels[selected], minlength=200)
            if set(per_class.tolist()) != {2}:
                raise RuntimeError(
                    f"{mechanism} fold {fold}: class budget mismatch"
                )
            if np.any(selected & (folds == fold)):
                raise RuntimeError(
                    f"{mechanism} fold {fold}: selected an OOF image"
                )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "cub_missingness_selections.npz"
    np.savez_compressed(
        output,
        **{f"selected_{key}": value for key, value in selection.items()},
        typicality=typicality,
        completeness=completeness.astype(np.float32),
        visible_keypoint_fraction=visible_counts.astype(np.float32),
        keypoint_spatial_coverage=coverages.astype(np.float32),
    )
    sha256 = hashlib.sha256(output.read_bytes()).hexdigest()
    summary = {
        "experiment_id": protocol["experiment_id"],
        "selection_sha256": sha256,
        "screening_seed": seed,
        "images": len(rows),
        "official_test_images_decoded_or_encoded": 0,
        "mechanisms": {},
    }
    for mechanism, values in selection.items():
        selected_x, unselected_x, selected_z, unselected_z = [], [], [], []
        for fold in range(5):
            train = folds != fold
            chosen = values[fold]
            selected_x.extend(typicality[fold, chosen].tolist())
            unselected_x.extend(typicality[fold, train & ~chosen].tolist())
            selected_z.extend(completeness[chosen].tolist())
            unselected_z.extend(completeness[train & ~chosen].tolist())
        summary["mechanisms"][mechanism] = {
            "selected_per_fold": 400,
            "selected_per_class_per_fold": 2,
            "mean_typicality_selected": float(np.mean(selected_x)),
            "mean_typicality_unselected": float(np.mean(unselected_x)),
            "mean_completeness_selected": float(np.mean(selected_z)),
            "mean_completeness_unselected": float(np.mean(unselected_z)),
        }
    (
        args.output_dir / "cub_missingness_selection_summary.json"
    ).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

