#!/usr/bin/env python3
"""Full-keypoint semantic-part-query oracle gate for PAT-I-260729-001."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from sklearn.linear_model import RidgeClassifier
from sklearn.svm import SVC

from sparse_anchor_utils import balanced_accuracy, class_recall, l2_normalize


CLASSES = 200
PARTS = 15
BACKGROUND_CLASS = 15
PATCH_GRID = 28
PATCH_COUNT = PATCH_GRID * PATCH_GRID
FEATURE_DIM = 768
BACKGROUND_PER_IMAGE = 4
BACKGROUND_MIN_DISTANCE = 3


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def deterministic_background_indices(
    keypoint_indices: np.ndarray,
    count: int,
    seed: int,
    grid: int = PATCH_GRID,
    minimum_distance: int = BACKGROUND_MIN_DISTANCE,
) -> np.ndarray:
    keypoint_indices = np.asarray(keypoint_indices, dtype=np.int64)
    visible = keypoint_indices[keypoint_indices >= 0]
    candidates = np.arange(grid * grid, dtype=np.int64)
    if len(visible):
        yy, xx = np.divmod(candidates, grid)
        key_y, key_x = np.divmod(visible, grid)
        distance = np.maximum(
            np.abs(yy[:, None] - key_y[None, :]),
            np.abs(xx[:, None] - key_x[None, :]),
        )
        candidates = candidates[np.all(distance >= minimum_distance, axis=1)]
    if len(candidates) < count:
        raise RuntimeError("not enough background patches after keypoint exclusion")
    rng = np.random.default_rng(seed)
    return np.sort(rng.choice(candidates, size=count, replace=False))


def build_detector_training_set(
    patches: np.ndarray,
    keypoint_indices: np.ndarray,
    train_indices: np.ndarray,
    fold_seed: int,
) -> tuple[np.ndarray, np.ndarray, dict]:
    features = []
    targets = []
    part_counts = np.zeros(PARTS, dtype=np.int64)
    background_count = 0
    for row_index in np.asarray(train_indices, dtype=np.int64):
        row_keypoints = np.asarray(keypoint_indices[row_index], dtype=np.int64)
        row_patches = np.asarray(patches[row_index], dtype=np.float32)
        for part, patch_index in enumerate(row_keypoints):
            if patch_index < 0:
                continue
            features.append(row_patches[int(patch_index)])
            targets.append(part)
            part_counts[part] += 1
        background = deterministic_background_indices(
            row_keypoints,
            count=BACKGROUND_PER_IMAGE,
            seed=fold_seed * 100_003 + int(row_index),
        )
        features.extend(row_patches[background])
        targets.extend([BACKGROUND_CLASS] * len(background))
        background_count += len(background)
    x = l2_normalize(np.asarray(features, dtype=np.float32))
    y = np.asarray(targets, dtype=np.int64)
    if len(np.unique(y)) != PARTS + 1:
        raise RuntimeError("detector training set does not cover all part labels")
    diagnostics = {
        "training_tokens": int(len(y)),
        "visible_part_tokens": int(part_counts.sum()),
        "background_tokens": int(background_count),
        "part_counts": part_counts.tolist(),
    }
    return x, y, diagnostics


def spatial_softmax_pool_numpy(
    patches: np.ndarray,
    scores: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    patches = l2_normalize(np.asarray(patches, dtype=np.float32))
    scores = np.asarray(scores, dtype=np.float32)
    if patches.ndim != 3 or scores.shape != (len(patches), PARTS, patches.shape[1]):
        raise ValueError("unexpected patch or score shape")
    centered = scores - scores.mean(axis=2, keepdims=True)
    scale = np.maximum(scores.std(axis=2, keepdims=True), 1e-6)
    standardized = centered / scale
    standardized -= standardized.max(axis=2, keepdims=True)
    weights = np.exp(standardized)
    weights /= weights.sum(axis=2, keepdims=True)
    pooled = np.einsum("bpt,btd->bpd", weights, patches)
    pooled = l2_normalize(pooled)
    aggregate = l2_normalize(pooled.mean(axis=1))
    predicted_patch = scores.argmax(axis=2).astype(np.int16)
    return aggregate, predicted_patch


def detector_parameters(detector: RidgeClassifier) -> tuple[np.ndarray, np.ndarray]:
    coefficient = np.asarray(detector.coef_, dtype=np.float32)
    intercept = np.asarray(detector.intercept_, dtype=np.float32)
    if coefficient.shape != (PARTS + 1, FEATURE_DIM):
        raise RuntimeError(f"unexpected detector coefficient shape {coefficient.shape}")
    return coefficient[:PARTS], intercept[:PARTS]


def pool_semantic_parts(
    patches: np.ndarray,
    detector: RidgeClassifier,
    indices: np.ndarray,
    batch_size: int = 16,
) -> tuple[np.ndarray, np.ndarray]:
    import torch

    coefficient, intercept = detector_parameters(detector)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    weight = torch.from_numpy(coefficient.T).to(device)
    bias = torch.from_numpy(intercept).to(device)
    aggregate = np.empty((len(indices), FEATURE_DIM), dtype=np.float32)
    predicted_patch = np.empty((len(indices), PARTS), dtype=np.int16)
    with torch.inference_mode():
        for start in range(0, len(indices), batch_size):
            stop = min(start + batch_size, len(indices))
            batch_indices = indices[start:stop]
            token = torch.from_numpy(
                np.asarray(patches[batch_indices], dtype=np.float32)
            ).to(device)
            token = torch.nn.functional.normalize(token, dim=-1)
            scores = torch.matmul(token, weight) + bias
            scores = scores.transpose(1, 2)
            centered = scores - scores.mean(dim=2, keepdim=True)
            scale = scores.std(dim=2, keepdim=True, unbiased=False).clamp_min(1e-6)
            spatial_weight = torch.softmax(centered / scale, dim=2)
            pooled = torch.einsum("bpt,btd->bpd", spatial_weight, token)
            pooled = torch.nn.functional.normalize(pooled, dim=-1)
            part_mean = torch.nn.functional.normalize(pooled.mean(dim=1), dim=-1)
            aggregate[start:stop] = part_mean.cpu().numpy()
            predicted_patch[start:stop] = scores.argmax(dim=2).short().cpu().numpy()
    return aggregate, predicted_patch


def uniform_part_representation(mean_patch: np.ndarray) -> np.ndarray:
    return l2_normalize(np.asarray(mean_patch, dtype=np.float32))


def combined_representation(cls: np.ndarray, part: np.ndarray) -> np.ndarray:
    cls = l2_normalize(cls)
    part = l2_normalize(part)
    return l2_normalize(np.concatenate([cls, part], axis=1))


def localization_hit_counts(
    predicted_patch: np.ndarray,
    keypoint_indices: np.ndarray,
    grid: int = PATCH_GRID,
) -> tuple[int, int]:
    predicted_patch = np.asarray(predicted_patch, dtype=np.int64)
    keypoint_indices = np.asarray(keypoint_indices, dtype=np.int64)
    if predicted_patch.shape != keypoint_indices.shape:
        raise ValueError("predicted and target keypoint arrays differ")
    visible = keypoint_indices >= 0
    pred_y, pred_x = np.divmod(predicted_patch, grid)
    true_y, true_x = np.divmod(np.maximum(keypoint_indices, 0), grid)
    hit = (
        np.maximum(np.abs(pred_y - true_y), np.abs(pred_x - true_x)) <= 1
    ) & visible
    return int(hit.sum()), int(visible.sum())


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--feature-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=16)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    labels = np.load(args.feature_dir / "labels.npy")
    folds = np.load(args.feature_dir / "folds.npy")
    image_ids = np.load(args.feature_dir / "image_ids.npy")
    cls = l2_normalize(np.load(args.feature_dir / "cls.npy", mmap_mode="r"))
    mean_patch = np.load(args.feature_dir / "mean_patch.npy", mmap_mode="r")
    patches = np.load(args.feature_dir / "patches.npy", mmap_mode="r")
    keypoint_indices = np.load(args.feature_dir / "kp_patch.npy", mmap_mode="r")
    metadata = json.loads((args.feature_dir / "metadata.json").read_text())

    if patches.shape != (len(labels), PATCH_COUNT, FEATURE_DIM):
        raise RuntimeError(f"unexpected dense patch cache shape {patches.shape}")
    if metadata.get("official_test_images_decoded_or_encoded") != 0:
        raise RuntimeError("feature metadata does not preserve the official-test lock")

    arm_names = ("CLS_RBF", "K0_UNIFORM_PART_RBF", "FULL_SEMANTIC_PART_RBF")
    predictions = {
        name: np.full(len(labels), -1, dtype=np.int64) for name in arm_names
    }
    full_predicted_patch = np.full((len(labels), PARTS), -1, dtype=np.int16)
    k0_predicted_patch = np.zeros((len(labels), PARTS), dtype=np.int16)
    fold_details = []
    full_hit_total = full_visible_total = 0
    k0_hit_total = k0_visible_total = 0
    uniform_part = uniform_part_representation(mean_patch)
    k0_representation = combined_representation(cls, uniform_part)

    for outer_fold in sorted(np.unique(folds)):
        train = np.flatnonzero(folds != outer_fold)
        evaluate_on = np.flatnonzero(folds == outer_fold)
        detector_x, detector_y, detector_diagnostics = build_detector_training_set(
            patches,
            keypoint_indices,
            train,
            fold_seed=9701 + int(outer_fold),
        )
        detector = RidgeClassifier(alpha=1.0, class_weight="balanced")
        detector.fit(detector_x, detector_y)
        del detector_x, detector_y

        full_train_part, _ = pool_semantic_parts(
            patches, detector, train, batch_size=args.batch_size
        )
        full_eval_part, fold_predicted_patch = pool_semantic_parts(
            patches, detector, evaluate_on, batch_size=args.batch_size
        )
        full_predicted_patch[evaluate_on] = fold_predicted_patch
        full_train_representation = combined_representation(
            cls[train], full_train_part
        )
        full_eval_representation = combined_representation(
            cls[evaluate_on], full_eval_part
        )

        representation_by_arm = {
            "CLS_RBF": (cls[train], cls[evaluate_on]),
            "K0_UNIFORM_PART_RBF": (
                k0_representation[train],
                k0_representation[evaluate_on],
            ),
            "FULL_SEMANTIC_PART_RBF": (
                full_train_representation,
                full_eval_representation,
            ),
        }
        fold_metrics = {}
        for name, (train_x, eval_x) in representation_by_arm.items():
            classifier = SVC(C=3.0, kernel="rbf", gamma="scale")
            classifier.fit(train_x, labels[train])
            fold_prediction = classifier.predict(eval_x)
            predictions[name][evaluate_on] = fold_prediction
            fold_metrics[name] = balanced_accuracy(
                labels[evaluate_on], fold_prediction
            )

        full_hits, full_visible = localization_hit_counts(
            fold_predicted_patch, keypoint_indices[evaluate_on]
        )
        k0_hits, k0_visible = localization_hit_counts(
            k0_predicted_patch[evaluate_on], keypoint_indices[evaluate_on]
        )
        full_hit_total += full_hits
        full_visible_total += full_visible
        k0_hit_total += k0_hits
        k0_visible_total += k0_visible
        fold_details.append(
            {
                "outer_fold": int(outer_fold),
                "metrics": fold_metrics,
                "full_localization_hits": full_hits,
                "k0_localization_hits": k0_hits,
                "visible_keypoints": full_visible,
                "detector": detector_diagnostics,
            }
        )
        print(
            json.dumps(
                {
                    "outer_fold": int(outer_fold),
                    "metrics": fold_metrics,
                    "full_hit_rate": full_hits / full_visible,
                    "k0_hit_rate": k0_hits / k0_visible,
                },
                sort_keys=True,
            ),
            flush=True,
        )

    for name, value in predictions.items():
        if np.any(value < 0):
            raise RuntimeError(f"incomplete OOF predictions for {name}")
    metrics = {
        name: balanced_accuracy(labels, value)
        for name, value in predictions.items()
    }
    primary = predictions["FULL_SEMANTIC_PART_RBF"]
    k0 = predictions["K0_UNIFORM_PART_RBF"]
    k0_recall = class_recall(labels, k0)
    primary_recall = class_recall(labels, primary)
    class_delta = primary_recall - k0_recall
    gain_over_k0_pp = 100.0 * (
        metrics["FULL_SEMANTIC_PART_RBF"] - metrics["K0_UNIFORM_PART_RBF"]
    )
    gain_over_cls_pp = 100.0 * (
        metrics["FULL_SEMANTIC_PART_RBF"] - metrics["CLS_RBF"]
    )
    full_hit_rate = full_hit_total / full_visible_total
    k0_hit_rate = k0_hit_total / k0_visible_total
    hit_gain_pp = 100.0 * (full_hit_rate - k0_hit_rate)
    positive_classes = int(np.sum(class_delta > 0))
    negative_classes = int(np.sum(class_delta < 0))
    worst_delta = float(class_delta.min())
    gates = {
        "gain_over_k0_at_least_0_50pp": bool(gain_over_k0_pp >= 0.5 - 1e-12),
        "gain_over_cls_at_least_0_50pp": bool(gain_over_cls_pp >= 0.5 - 1e-12),
        "hit_rate_gain_at_least_10pp": bool(hit_gain_pp >= 10.0 - 1e-12),
        "negative_classes_not_more_than_positive": bool(
            negative_classes <= positive_classes
        ),
        "worst_class_delta_at_least_minus_0_20": bool(worst_delta >= -0.2),
    }
    summary = {
        "experiment_id": protocol["experiment_id"],
        "metrics": metrics,
        "gain_over_k0_pp": gain_over_k0_pp,
        "gain_over_cls_rbf_pp": gain_over_cls_pp,
        "full_localization_hit_rate": full_hit_rate,
        "k0_localization_hit_rate": k0_hit_rate,
        "localization_hit_rate_gain_pp": hit_gain_pp,
        "full_localization_hits": full_hit_total,
        "k0_localization_hits": k0_hit_total,
        "visible_keypoints": full_visible_total,
        "positive_class_count_vs_k0": positive_classes,
        "negative_class_count_vs_k0": negative_classes,
        "worst_class_recall_delta_vs_k0": worst_delta,
        "gates": gates,
        "screen_success": bool(all(gates.values())),
        "fold_details": fold_details,
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
    }
    np.savez_compressed(
        args.output_dir / "semantic_part_query_predictions.npz",
        labels=labels,
        folds=folds,
        image_ids=image_ids,
        full_predicted_patch=full_predicted_patch,
        k0_predicted_patch=k0_predicted_patch,
        k0_class_recall=k0_recall,
        full_class_recall=primary_recall,
        class_recall_delta_vs_k0=class_delta,
        **{f"{name}_predictions": value for name, value in predictions.items()},
    )
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
