#!/usr/bin/env python3
"""Train fold task heads and freeze K2 facility masks for PAT-D-260728-007."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

from cub_active_selection import load_and_sanitize_manifest
from cub_subset_selection import (
    STRATEGIES,
    exact_facility_pair,
    feature_similarity,
    implicit_gradient_similarity,
    validate_k2_mask,
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def train_task_head(features, labels, config, seed):
    torch.manual_seed(seed)
    np.random.seed(seed)
    torch.use_deterministic_algorithms(True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    values = F.normalize(
        torch.as_tensor(features, dtype=torch.float32, device=device), dim=1
    )
    targets = torch.as_tensor(labels, dtype=torch.long, device=device)
    classes = int(targets.max().item()) + 1
    model = torch.nn.Linear(values.shape[1], classes).to(device)
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=float(config["learning_rate"]),
        weight_decay=float(config["weight_decay"]),
    )
    generator = torch.Generator(device=device).manual_seed(seed)
    batch_size = int(config["batch_size"])
    epochs = int(config["epochs"])
    final_loss = None
    for _ in range(epochs):
        permutation = torch.randperm(
            len(values), generator=generator, device=device
        )
        for indices in permutation.split(batch_size):
            optimizer.zero_grad(set_to_none=True)
            logits = model(values[indices])
            loss = F.cross_entropy(
                logits,
                targets[indices],
                label_smoothing=float(config["label_smoothing"]),
            )
            loss.backward()
            optimizer.step()
            final_loss = float(loss.detach())
    with torch.inference_mode():
        logits = model(values)
        probabilities = logits.softmax(dim=1)
        accuracy = float((logits.argmax(1) == targets).float().mean())
        mean_confidence = float(probabilities.max(dim=1).values.mean())
    return (
        probabilities.cpu().numpy(),
        {
            "seed": seed,
            "epochs": epochs,
            "final_batch_loss": final_loss,
            "fold_train_accuracy": accuracy,
            "mean_max_probability": mean_confidence,
        },
    )


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--selector-manifest", type=Path, required=True)
    parser.add_argument("--features", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    rows = load_and_sanitize_manifest(args.selector_manifest)
    feature_file = np.load(args.features)
    features = feature_file["features"].astype(np.float32)
    labels = np.asarray([row["class_index"] for row in rows], dtype=np.int64)
    folds = np.asarray([row["fold"] for row in rows], dtype=np.int64)
    image_ids = np.asarray([row["image_id"] for row in rows])
    if not np.array_equal(labels, feature_file["labels"]):
        raise RuntimeError("Feature labels do not match selector manifest")
    if not np.array_equal(folds, feature_file["folds"]):
        raise RuntimeError("Feature folds do not match selector manifest")
    if not np.array_equal(image_ids, feature_file["image_ids"]):
        raise RuntimeError("Feature image IDs do not match selector manifest")
    fold_count = int(protocol["data"]["folds"])
    classes = len(np.unique(labels))
    selections = {
        strategy: np.zeros((fold_count, len(rows)), dtype=np.bool_)
        for strategy in STRATEGIES
    }
    pair_rows = []
    head_diagnostics = []
    head_config = protocol["selector"]["fold_task_head"]
    head_seeds = [int(seed) for seed in head_config["seeds"]]
    for fold in range(fold_count):
        train_indices = np.flatnonzero(folds != fold)
        probabilities, diagnostics = train_task_head(
            features[train_indices],
            labels[train_indices],
            head_config,
            head_seeds[fold],
        )
        diagnostics["fold"] = fold
        head_diagnostics.append(diagnostics)
        probability_by_row = {
            int(row_index): probabilities[offset]
            for offset, row_index in enumerate(train_indices)
        }
        for class_index in range(classes):
            candidates = np.flatnonzero(
                (folds != fold) & (labels == class_index)
            )
            if len(candidates) != 8:
                raise RuntimeError(
                    f"Fold {fold} class {class_index}: expected 8 candidates"
                )
            candidate_features = features[candidates]
            candidate_probabilities = np.stack(
                [probability_by_row[int(index)] for index in candidates]
            )
            kernels = {
                "FEATURE_FACILITY": feature_similarity(candidate_features),
                "GRADIENT_FACILITY": implicit_gradient_similarity(
                    candidate_features,
                    candidate_probabilities,
                    labels[candidates],
                ),
            }
            for strategy, kernel in kernels.items():
                pair_offsets, objective = exact_facility_pair(
                    kernel, image_ids[candidates]
                )
                selected_rows = candidates[pair_offsets]
                selections[strategy][fold, selected_rows] = True
                pair_rows.append(
                    {
                        "fold": fold,
                        "class_index": class_index,
                        "strategy": strategy,
                        "row_index_1": int(selected_rows[0]),
                        "row_index_2": int(selected_rows[1]),
                        "image_id_1": int(image_ids[selected_rows[0]]),
                        "image_id_2": int(image_ids[selected_rows[1]]),
                        "facility_objective": objective,
                    }
                )
        for strategy in STRATEGIES:
            validate_k2_mask(
                selections[strategy][fold],
                labels,
                folds,
                fold,
                classes,
            )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "cub_gradient_coverage_selections.npz"
    np.savez_compressed(
        output,
        **{
            f"selected_{strategy}": mask
            for strategy, mask in selections.items()
        },
    )
    pair_path = args.output_dir / "cub_gradient_coverage_pairs.csv"
    with pair_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(pair_rows[0]))
        writer.writeheader()
        writer.writerows(pair_rows)
    diagnostics_path = args.output_dir / "task_head_diagnostics.json"
    diagnostics_path.write_text(
        json.dumps(head_diagnostics, indent=2, sort_keys=True) + "\n"
    )
    overlap = {
        str(fold): float(
            np.mean(
                selections["FEATURE_FACILITY"][fold]
                & selections["GRADIENT_FACILITY"][fold]
            )
            * len(rows)
            / (2 * classes)
        )
        for fold in range(fold_count)
    }
    summary = {
        "experiment_id": protocol["experiment_id"],
        "strategies": list(STRATEGIES),
        "folds": fold_count,
        "classes": classes,
        "budget_per_class": 2,
        "selected_per_fold": 2 * classes,
        "pair_overlap_fraction_by_fold": overlap,
        "selection_sha256": sha256_file(output),
        "pairs_sha256": sha256_file(pair_path),
        "task_head_diagnostics_sha256": sha256_file(diagnostics_path),
        "selector_manifest_sha256": sha256_file(args.selector_manifest),
        "feature_file_sha256": sha256_file(args.features),
        "selector_keypoint_field_accesses": 0,
        "official_test_images_decoded_or_encoded": 0,
    }
    (args.output_dir / "cub_gradient_coverage_selection_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
