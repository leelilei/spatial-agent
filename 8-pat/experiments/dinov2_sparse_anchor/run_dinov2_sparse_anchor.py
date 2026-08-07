#!/usr/bin/env python3
"""DINOv2 foundation and sparse semantic-anchor screen on CUB train only."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from torch.utils.data import DataLoader, Dataset

from sparse_anchor_utils import (
    balanced_accuracy,
    evaluate_screen,
    fused_candidate_predictions,
    l2_normalize,
    validate_sparse_selection,
)


IMAGE_SIZE = 392
PATCH_GRID = 28
PATCH_COUNT = PATCH_GRID * PATCH_GRID
FEATURE_DIM = 768
CLASSES = 200
PARTS = 15
TOP_K = 10
ALPHAS = (0.25, 0.5, 1.0, 2.0)
NORMALIZE_MEAN = (0.485, 0.456, 0.406)
NORMALIZE_STD = (0.229, 0.224, 0.225)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class CUBFeatureDataset(Dataset):
    def __init__(self, root, rows):
        self.root = root
        self.rows = rows

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, index):
        import torch
        from torchvision.transforms import InterpolationMode
        from torchvision.transforms import functional as TF

        row = self.rows[index]
        if row["split"] != "train" or row["source_split"] != "official_train":
            raise RuntimeError("PAT-H-260729-001 may decode official train only")
        with Image.open(self.root / row["relative_path"]) as source:
            image = source.convert("RGB")
        width, height = image.size
        patch_indices = np.full(PARTS, -1, dtype=np.int64)
        for part, (x, y, visible) in enumerate(row["keypoints"]):
            if not visible:
                continue
            gx = min(PATCH_GRID - 1, max(0, int(float(x) / width * PATCH_GRID)))
            gy = min(PATCH_GRID - 1, max(0, int(float(y) / height * PATCH_GRID)))
            patch_indices[part] = gy * PATCH_GRID + gx
        image = TF.resize(
            image,
            [IMAGE_SIZE, IMAGE_SIZE],
            interpolation=InterpolationMode.BICUBIC,
            antialias=True,
        )
        image = TF.normalize(
            TF.to_tensor(image), NORMALIZE_MEAN, NORMALIZE_STD
        )
        return image, index, torch.from_numpy(patch_indices)


def feature_paths(directory):
    return {
        "cls": directory / "cls.npy",
        "mean_patch": directory / "mean_patch.npy",
        "patches": directory / "patches.npy",
        "kp_patch": directory / "kp_patch.npy",
        "labels": directory / "labels.npy",
        "folds": directory / "folds.npy",
        "image_ids": directory / "image_ids.npy",
        "metadata": directory / "metadata.json",
    }


def features_complete(paths, manifest_hash):
    if not all(path.exists() for path in paths.values()):
        return False
    metadata = json.loads(paths["metadata"].read_text())
    return bool(
        metadata.get("manifest_sha256") == manifest_hash
        and metadata.get("images") == 2000
        and metadata.get("official_test_images_decoded_or_encoded") == 0
    )


def extract_features(dataset_root, rows, feature_dir, manifest_hash, batch_size):
    import torch

    paths = feature_paths(feature_dir)
    if features_complete(paths, manifest_hash):
        print(json.dumps({"status": "FEATURE_CACHE_RESUMED"}, sort_keys=True))
        return paths
    feature_dir.mkdir(parents=True, exist_ok=True)
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True
    torch.backends.cudnn.benchmark = True
    model = torch.hub.load(
        "facebookresearch/dinov2", "dinov2_vitb14"
    ).eval().cuda()
    for parameter in model.parameters():
        parameter.requires_grad = False
    dataset = CUBFeatureDataset(dataset_root, rows)
    loader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=8,
        pin_memory=True,
        persistent_workers=True,
    )
    n = len(rows)
    cls_store = np.lib.format.open_memmap(
        paths["cls"], mode="w+", dtype=np.float32, shape=(n, FEATURE_DIM)
    )
    mean_store = np.lib.format.open_memmap(
        paths["mean_patch"],
        mode="w+",
        dtype=np.float32,
        shape=(n, FEATURE_DIM),
    )
    patch_store = np.lib.format.open_memmap(
        paths["patches"],
        mode="w+",
        dtype=np.float16,
        shape=(n, PATCH_COUNT, FEATURE_DIM),
    )
    kp_store = np.lib.format.open_memmap(
        paths["kp_patch"], mode="w+", dtype=np.int16, shape=(n, PARTS)
    )
    completed = 0
    with torch.inference_mode():
        for batch_index, (images, indices, kp_patch) in enumerate(loader, 1):
            images = images.cuda(non_blocking=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                output = model.forward_features(images)
            cls = output["x_norm_clstoken"].float().cpu().numpy()
            patches = output["x_norm_patchtokens"].float().cpu().numpy()
            if patches.shape[1:] != (PATCH_COUNT, FEATURE_DIM):
                raise RuntimeError(
                    f"unexpected DINO patch shape {patches.shape}"
                )
            idx = indices.numpy()
            cls_store[idx] = cls
            mean_store[idx] = patches.mean(axis=1)
            patch_store[idx] = patches.astype(np.float16)
            kp_store[idx] = kp_patch.numpy().astype(np.int16)
            completed += len(idx)
            if batch_index % 25 == 0 or completed == n:
                print(
                    json.dumps(
                        {
                            "status": "FEATURE_EXTRACTION",
                            "images_complete": completed,
                            "images_total": n,
                        },
                        sort_keys=True,
                    ),
                    flush=True,
                )
    cls_store.flush()
    mean_store.flush()
    patch_store.flush()
    kp_store.flush()
    np.save(paths["labels"], np.asarray([row["class_index"] for row in rows]))
    np.save(paths["folds"], np.asarray([row["fold"] for row in rows]))
    np.save(paths["image_ids"], np.asarray([row["image_id"] for row in rows]))
    metadata = {
        "backbone": "dinov2_vitb14",
        "images": n,
        "input_size": IMAGE_SIZE,
        "patch_grid": PATCH_GRID,
        "feature_dim": FEATURE_DIM,
        "manifest_sha256": manifest_hash,
        "official_test_images_decoded_or_encoded": 0,
    }
    paths["metadata"].write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n"
    )
    del model
    torch.cuda.empty_cache()
    return paths


def load_features(paths):
    return {
        key: np.load(path, mmap_mode="r")
        for key, path in paths.items()
        if key != "metadata"
    }


def class_centroids(features, labels):
    centers = np.stack(
        [features[labels == class_index].mean(axis=0) for class_index in range(CLASSES)]
    )
    return l2_normalize(centers)


def run_global_oof(features, labels, folds):
    cls = l2_normalize(features["cls"])
    combined = l2_normalize(
        np.concatenate(
            [l2_normalize(features["cls"]), l2_normalize(features["mean_patch"])],
            axis=1,
        )
    )
    predictions = {
        arm: np.full(len(labels), -1, dtype=np.int64)
        for arm in (
            "CLS_PROTO",
            "CLS_RIDGE",
            "CLS_PATCH_RIDGE",
            "CLS_PATCH_LOGREG",
        )
    }
    primary_scores = np.full((len(labels), CLASSES), np.nan, dtype=np.float32)
    for fold in range(5):
        train = np.flatnonzero(folds != fold)
        evaluate_on = np.flatnonzero(folds == fold)
        centers = class_centroids(cls[train], labels[train])
        predictions["CLS_PROTO"][evaluate_on] = (
            cls[evaluate_on] @ centers.T
        ).argmax(axis=1)
        cls_ridge = RidgeClassifier(alpha=1.0)
        cls_ridge.fit(cls[train], labels[train])
        predictions["CLS_RIDGE"][evaluate_on] = cls_ridge.predict(
            cls[evaluate_on]
        )
        combined_ridge = RidgeClassifier(alpha=1.0)
        combined_ridge.fit(combined[train], labels[train])
        predictions["CLS_PATCH_RIDGE"][evaluate_on] = combined_ridge.predict(
            combined[evaluate_on]
        )
        logreg = LogisticRegression(
            C=1.0,
            solver="lbfgs",
            max_iter=400,
            tol=1e-5,
        )
        logreg.fit(combined[train], labels[train])
        primary_scores[evaluate_on] = logreg.decision_function(
            combined[evaluate_on]
        ).astype(np.float32)
        predictions["CLS_PATCH_LOGREG"][evaluate_on] = primary_scores[
            evaluate_on
        ].argmax(axis=1)
        print(
            json.dumps(
                {
                    "status": "GLOBAL_FOLD_COMPLETE",
                    "fold": fold,
                    "CLS_PROTO_BA": balanced_accuracy(
                        labels[evaluate_on],
                        predictions["CLS_PROTO"][evaluate_on],
                    ),
                    "CLS_PATCH_LOGREG_BA": balanced_accuracy(
                        labels[evaluate_on],
                        predictions["CLS_PATCH_LOGREG"][evaluate_on],
                    ),
                },
                sort_keys=True,
            ),
            flush=True,
        )
    return predictions, primary_scores, combined


def build_fold_part_model(
    patch_features,
    kp_patch,
    global_features,
    labels,
    train_indices,
    selected_mask,
    batch_size=32,
):
    import torch

    selected_indices = validate_sparse_selection(
        selected_mask, train_indices, labels, classes=CLASSES
    )
    selected_by_class = np.full(CLASSES, -1, dtype=np.int64)
    selected_by_class[labels[selected_indices]] = selected_indices
    anchors = np.zeros((CLASSES, PARTS, FEATURE_DIM), dtype=np.float32)
    available = np.zeros((CLASSES, PARTS), dtype=np.bool_)
    global_sums = np.zeros((PARTS, FEATURE_DIM), dtype=np.float64)
    global_counts = np.zeros(PARTS, dtype=np.int64)
    for class_index, row_index in enumerate(selected_by_class):
        token_map = np.asarray(patch_features[row_index], dtype=np.float32)
        for part, patch_index in enumerate(kp_patch[row_index]):
            if patch_index < 0:
                continue
            value = token_map[int(patch_index)]
            anchors[class_index, part] = value
            available[class_index, part] = True
            global_sums[part] += value
            global_counts[part] += 1
    if np.any(global_counts == 0):
        raise RuntimeError("a semantic part has no visible fold-training anchor")
    global_fallback = global_sums / global_counts[:, None]
    for class_index in range(CLASSES):
        missing = ~available[class_index]
        anchors[class_index, missing] = global_fallback[missing]
    anchors = l2_normalize(anchors)
    part_sums = torch.zeros(
        CLASSES, PARTS, FEATURE_DIM, dtype=torch.float32, device="cuda"
    )
    class_counts = torch.zeros(CLASSES, dtype=torch.float32, device="cuda")
    matched_chunks = []
    label_chunks = []
    for start in range(0, len(train_indices), batch_size):
        indices = train_indices[start : start + batch_size]
        batch_labels_np = labels[indices]
        patches = torch.from_numpy(
            np.asarray(patch_features[indices], dtype=np.float32)
        ).cuda()
        patches = torch.nn.functional.normalize(patches, dim=-1)
        batch_anchors = torch.from_numpy(anchors[batch_labels_np]).cuda()
        similarity = torch.einsum("btd,bpd->bpt", patches, batch_anchors)
        locations = similarity.argmax(dim=-1)
        matched = torch.gather(
            patches,
            1,
            locations[..., None].expand(-1, -1, FEATURE_DIM),
        )
        batch_labels = torch.from_numpy(batch_labels_np).long().cuda()
        part_sums.index_add_(0, batch_labels, matched)
        class_counts.index_add_(
            0, batch_labels, torch.ones(len(indices), device="cuda")
        )
        matched_chunks.append(matched.half().cpu())
        label_chunks.append(batch_labels.cpu())
    prototypes = torch.nn.functional.normalize(
        part_sums / class_counts[:, None, None], dim=-1
    )
    consistency_sums = torch.zeros(
        CLASSES, PARTS, dtype=torch.float32, device="cuda"
    )
    for matched_cpu, batch_labels_cpu in zip(matched_chunks, label_chunks):
        matched = matched_cpu.float().cuda()
        batch_labels = batch_labels_cpu.long().cuda()
        values = (
            torch.nn.functional.normalize(matched, dim=-1)
            * prototypes[batch_labels]
        ).sum(dim=-1)
        consistency_sums.index_add_(0, batch_labels, values)
    consistency = (
        consistency_sums / class_counts[:, None]
    ).cpu().numpy()
    prototypes_np = prototypes.cpu().numpy()
    centers = class_centroids(global_features[train_indices], labels[train_indices])
    center_similarity = centers @ centers.T
    np.fill_diagonal(center_similarity, -np.inf)
    confusing = np.argsort(-center_similarity, axis=1)[:, :10]
    confusing_parts = prototypes_np[confusing]
    confusing_similarity = np.einsum(
        "cpd,ckpd->ckp", prototypes_np, confusing_parts
    )
    discriminative_margin = 1.0 - confusing_similarity.max(axis=1)
    reliability = np.maximum(consistency, 0.0) * np.maximum(
        discriminative_margin, 1e-4
    )
    reliability = reliability / np.maximum(
        reliability.sum(axis=1, keepdims=True), 1e-12
    )
    diagnostics = {
        "selected_images": int(len(selected_indices)),
        "fallback_anchor_rate": float(np.mean(~available)),
        "mean_propagation_consistency": float(consistency.mean()),
        "mean_discriminative_margin": float(discriminative_margin.mean()),
    }
    return prototypes_np, reliability.astype(np.float32), diagnostics


def score_fold_parts(
    patch_features,
    eval_indices,
    candidates,
    prototypes,
    reliability,
    batch_size=16,
):
    import torch

    equal_scores = np.empty(candidates.shape, dtype=np.float32)
    aware_scores = np.empty(candidates.shape, dtype=np.float32)
    prototypes_gpu = torch.from_numpy(prototypes).cuda()
    reliability_gpu = torch.from_numpy(reliability).cuda()
    for start in range(0, len(eval_indices), batch_size):
        stop = min(len(eval_indices), start + batch_size)
        indices = eval_indices[start:stop]
        candidate_batch_np = candidates[start:stop]
        patches = torch.from_numpy(
            np.asarray(patch_features[indices], dtype=np.float32)
        ).cuda()
        patches = torch.nn.functional.normalize(patches, dim=-1)
        candidate_batch = torch.from_numpy(candidate_batch_np).long().cuda()
        candidate_prototypes = prototypes_gpu[candidate_batch]
        similarity = torch.einsum(
            "btd,bkpd->bkpt", patches, candidate_prototypes
        )
        part_scores = similarity.max(dim=-1).values
        equal = part_scores.mean(dim=-1)
        weights = reliability_gpu[candidate_batch]
        aware = (part_scores * weights).sum(dim=-1)
        equal_scores[start:stop] = equal.cpu().numpy()
        aware_scores[start:stop] = aware.cpu().numpy()
    return equal_scores, aware_scores


def top_candidates(scores, top_k):
    partial = np.argpartition(-scores, top_k - 1, axis=1)[:, :top_k]
    partial_scores = np.take_along_axis(scores, partial, axis=1)
    order = np.argsort(-partial_scores, axis=1)
    candidates = np.take_along_axis(partial, order, axis=1)
    candidate_scores = np.take_along_axis(scores, candidates, axis=1)
    return candidates, candidate_scores


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--selections", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--feature-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--extract-batch-size", type=int, default=8)
    return parser.parse_args()


def main():
    import torch

    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    rows = [
        json.loads(line)
        for line in args.manifest.read_text().splitlines()
    ]
    if len(rows) != 2000:
        raise RuntimeError(f"expected 2000 episode images, got {len(rows)}")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest_hash = sha256(args.manifest)
    protocol_hash = sha256(args.protocol)
    paths = extract_features(
        args.dataset_root,
        rows,
        args.feature_dir,
        manifest_hash,
        args.extract_batch_size,
    )
    features = load_features(paths)
    labels = np.asarray(features["labels"])
    folds = np.asarray(features["folds"])
    expected_labels = np.asarray([row["class_index"] for row in rows])
    if not np.array_equal(labels, expected_labels):
        raise RuntimeError("feature-cache labels mismatch")
    predictions, global_scores, combined = run_global_oof(
        features, labels, folds
    )
    foundation_metrics = {
        arm: balanced_accuracy(labels, value)
        for arm, value in predictions.items()
    }
    foundation_gate = bool(
        foundation_metrics["CLS_PATCH_LOGREG"] >= 0.76
    )
    np.savez_compressed(
        args.output_dir / "foundation_predictions.npz",
        labels=labels,
        image_ids=np.asarray(features["image_ids"]),
        global_scores=global_scores,
        **{f"{arm}_predictions": value for arm, value in predictions.items()},
    )
    if not foundation_gate:
        summary = {
            "experiment_id": protocol["experiment_id"],
            "stage": "FOUNDATION_GATE",
            "foundation_metrics": foundation_metrics,
            "foundation_gate_pass": False,
            "sparse_anchor_executed": False,
            "official_test_images_decoded_or_encoded": 0,
            "protocol_sha256": protocol_hash,
        }
        (args.output_dir / "summary.json").write_text(
            json.dumps(summary, indent=2, sort_keys=True) + "\n"
        )
        print(json.dumps(summary, indent=2, sort_keys=True))
        return
    print(
        json.dumps(
            {
                "status": "FOUNDATION_GATE_PASS",
                "foundation_metrics": foundation_metrics,
            },
            sort_keys=True,
        ),
        flush=True,
    )
    selections = np.load(args.selections)["selected_random_k1"]
    local_predictions = {
        f"{prefix}_A{alpha:g}": np.full(len(labels), -1, dtype=np.int64)
        for prefix in ("EQUAL", "CA_SAP")
        for alpha in ALPHAS
    }
    candidate_store = np.full((len(labels), TOP_K), -1, dtype=np.int16)
    equal_score_store = np.full(
        (len(labels), TOP_K), np.nan, dtype=np.float32
    )
    aware_score_store = np.full(
        (len(labels), TOP_K), np.nan, dtype=np.float32
    )
    fold_diagnostics = []
    for fold in range(5):
        train_indices = np.flatnonzero(folds != fold)
        eval_indices = np.flatnonzero(folds == fold)
        candidates, candidate_global_scores = top_candidates(
            global_scores[eval_indices], TOP_K
        )
        prototypes, reliability, diagnostics = build_fold_part_model(
            features["patches"],
            features["kp_patch"],
            combined,
            labels,
            train_indices,
            selections[fold],
        )
        equal_scores, aware_scores = score_fold_parts(
            features["patches"],
            eval_indices,
            candidates,
            prototypes,
            reliability,
        )
        candidate_store[eval_indices] = candidates
        equal_score_store[eval_indices] = equal_scores
        aware_score_store[eval_indices] = aware_scores
        for alpha in ALPHAS:
            local_predictions[f"EQUAL_A{alpha:g}"][eval_indices] = (
                fused_candidate_predictions(
                    candidates,
                    candidate_global_scores,
                    equal_scores,
                    alpha,
                )
            )
            local_predictions[f"CA_SAP_A{alpha:g}"][eval_indices] = (
                fused_candidate_predictions(
                    candidates,
                    candidate_global_scores,
                    aware_scores,
                    alpha,
                )
            )
        diagnostics.update(
            {
                "fold": fold,
                "top10_global_oracle_coverage": float(
                    np.mean(
                        np.any(
                            candidates == labels[eval_indices, None], axis=1
                        )
                    )
                ),
            }
        )
        fold_diagnostics.append(diagnostics)
        print(
            json.dumps(
                {"status": "SPARSE_ANCHOR_FOLD_COMPLETE", **diagnostics},
                sort_keys=True,
            ),
            flush=True,
        )
        torch.cuda.empty_cache()
    predictions.update(local_predictions)
    decision = evaluate_screen(labels, predictions, alphas=ALPHAS)
    summary = {
        "experiment_id": protocol["experiment_id"],
        "stage": "SPARSE_ANCHOR_SCREEN",
        "foundation_metrics": foundation_metrics,
        "foundation_gate_pass": foundation_gate,
        "fold_diagnostics": fold_diagnostics,
        **decision,
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": protocol_hash,
    }
    np.savez_compressed(
        args.output_dir / "sparse_anchor_predictions.npz",
        labels=labels,
        image_ids=np.asarray(features["image_ids"]),
        candidates=candidate_store,
        equal_part_scores=equal_score_store,
        confusion_aware_scores=aware_score_store,
        **{f"{arm}_predictions": value for arm, value in predictions.items()},
    )
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
