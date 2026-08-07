#!/usr/bin/env python3
"""Run the preregistered CUB three-episode reliability audit."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader

import run_cub_missingness_screen as screen
import run_cub_prpool_oof as base


ARMS = ("GLOBAL", "RANDOM_K1", "FULL_KEYPOINT_ORACLE")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fit_global_fold(
    root, rows, train_indices, eval_indices, settings, seed, arm
):
    torch.manual_seed(seed)
    np.random.seed(seed)
    model = base.CUBModel(classes=200, use_prpool=False).cuda()
    train_dataset = base.CUBTrainOnly(
        root, rows, train_indices, training=True, seed=seed
    )
    eval_dataset = base.CUBTrainOnly(
        root, rows, eval_indices, training=False, seed=seed
    )
    generator = torch.Generator().manual_seed(seed)
    train_loader = DataLoader(
        train_dataset,
        batch_size=settings["batch_size"],
        shuffle=True,
        generator=generator,
        num_workers=8,
        pin_memory=True,
        persistent_workers=True,
    )
    eval_loader = DataLoader(
        eval_dataset,
        batch_size=settings["batch_size"],
        shuffle=False,
        num_workers=8,
        pin_memory=True,
        persistent_workers=True,
    )
    backbone_parameters = list(model.features.layer4.parameters())
    backbone_ids = {id(parameter) for parameter in backbone_parameters}
    head_parameters = [
        parameter
        for parameter in model.parameters()
        if parameter.requires_grad and id(parameter) not in backbone_ids
    ]
    optimizer = torch.optim.AdamW(
        [
            {
                "params": head_parameters,
                "lr": settings["head_learning_rate"],
            },
            {
                "params": backbone_parameters,
                "lr": settings["backbone_learning_rate"],
            },
        ],
        weight_decay=settings["weight_decay"],
    )
    for epoch in range(1, settings["epochs"] + 1):
        model.train()
        running_loss = 0.0
        for images, _, labels, _ in train_loader:
            images = images.cuda(non_blocking=True)
            labels = labels.cuda(non_blocking=True)
            optimizer.zero_grad(set_to_none=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                logits, _ = model(images)
                loss = F.cross_entropy(logits.float(), labels)
            loss.backward()
            optimizer.step()
            running_loss += float(loss.detach()) * len(labels)
        print(
            json.dumps(
                {
                    "arm": arm,
                    "fold_seed": seed,
                    "epoch": epoch,
                    "mean_train_loss": running_loss / len(train_dataset),
                },
                sort_keys=True,
            ),
            flush=True,
        )
    prediction, actual, row_indices = base.evaluate(model, eval_loader)
    del model
    torch.cuda.empty_cache()
    return prediction, actual, row_indices


def load_checkpoint(path, labels, image_ids):
    if not path.exists():
        return {}
    checkpoint = np.load(path)
    if not np.array_equal(checkpoint["labels"], labels):
        raise RuntimeError("Checkpoint labels mismatch")
    if not np.array_equal(checkpoint["image_ids"], image_ids):
        raise RuntimeError("Checkpoint image IDs mismatch")
    predictions = {}
    for arm in ARMS:
        key = f"{arm}_predictions"
        if key in checkpoint.files:
            values = checkpoint[key]
            if len(values) == len(labels) and np.all(values >= 0):
                predictions[arm] = values
    return predictions


def save_checkpoint(path, labels, image_ids, predictions):
    np.savez_compressed(
        path,
        labels=labels,
        image_ids=image_ids,
        **{
            f"{arm}_predictions": values
            for arm, values in predictions.items()
        },
    )


def run_episode(
    dataset_root,
    episode_dir,
    output_dir,
    settings,
    fold_seeds,
    smoke,
):
    rows = [
        json.loads(line)
        for line in (episode_dir / "cub_train_10shot_manifest.jsonl")
        .read_text()
        .splitlines()
    ]
    if any(
        row["split"] != "train" or row["source_split"] != "official_train"
        for row in rows
    ):
        raise RuntimeError("Episode contains a non-train image")
    labels = np.asarray([row["class_index"] for row in rows])
    folds = np.asarray([row["fold"] for row in rows])
    image_ids = np.asarray([row["image_id"] for row in rows])
    k1 = np.load(episode_dir / "random_k1_selection.npz")[
        "selected_random_k1"
    ]

    episode_number = int(rows[0]["episode"])
    checkpoint_path = output_dir / (
        f"episode_{episode_number}_smoke_checkpoint.npz"
        if smoke
        else f"episode_{episode_number}_checkpoint.npz"
    )
    predictions = {} if smoke else load_checkpoint(
        checkpoint_path, labels, image_ids
    )
    folds_to_run = [0] if smoke else list(range(5))
    for arm in ARMS:
        if arm in predictions:
            print(
                json.dumps(
                    {
                        "episode": episode_number,
                        "arm": arm,
                        "status": "RESUMED_FROM_COMPLETE_CHECKPOINT",
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
            continue
        oof = np.full(len(rows), -1, dtype=np.int64)
        for fold in folds_to_run:
            train_indices = np.flatnonzero(folds != fold)
            eval_indices = np.flatnonzero(folds == fold)
            seed = int(fold_seeds[fold])
            if arm == "GLOBAL":
                prediction, _, row_indices = fit_global_fold(
                    dataset_root,
                    rows,
                    train_indices,
                    eval_indices,
                    settings,
                    seed,
                    arm,
                )
            else:
                selected = (
                    k1[fold]
                    if arm == "RANDOM_K1"
                    else np.ones(len(rows), dtype=np.bool_)
                )
                prediction, _, row_indices = screen.fit_fold(
                    dataset_root,
                    rows,
                    train_indices,
                    eval_indices,
                    selected,
                    settings,
                    seed,
                    arm,
                )
            oof[row_indices] = prediction
        if smoke:
            evaluated = oof >= 0
            if int(evaluated.sum()) != 400:
                raise RuntimeError("Smoke prediction count mismatch")
        elif np.any(oof < 0):
            raise RuntimeError(f"Incomplete OOF predictions for {arm}")
        predictions[arm] = oof
        save_checkpoint(checkpoint_path, labels, image_ids, predictions)
    return labels, image_ids, predictions


def class_recall(labels, predictions):
    return np.asarray(
        [
            np.mean(predictions[labels == class_index] == class_index)
            for class_index in range(200)
        ]
    )


def balanced_accuracy(labels, predictions):
    return float(class_recall(labels, predictions).mean())


def bootstrap_class_mean_interval(class_deltas, seed=9099, draws=10000):
    rng = np.random.default_rng(seed)
    indices = rng.integers(0, len(class_deltas), size=(draws, len(class_deltas)))
    values = class_deltas[indices].mean(axis=1)
    return [float(x) for x in np.quantile(values, [0.025, 0.975])]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--episode-data-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--oracle-protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    oracle_protocol = json.loads(args.oracle_protocol.read_text())
    raw = oracle_protocol["optimization"]
    settings = {
        "head_learning_rate": raw["head_learning_rate"],
        "backbone_learning_rate": raw["backbone_learning_rate"],
        "weight_decay": raw["weight_decay"],
        "part_loss_weight": raw["part_loss_weight"],
        "regularizer_weight": raw["complementary_regularizer_weight"],
        "batch_size": raw["batch_size"],
        "epochs": (
            1 if args.smoke else int(protocol["training"]["fixed_epochs"])
        ),
    }
    fold_seeds = [
        int(x)
        for x in protocol["training"][
            "fold_model_seeds_shared_across_all_arms_and_episodes"
        ]
    ]
    args.output_dir.mkdir(parents=True, exist_ok=True)
    episode_numbers = [1] if args.smoke else [1, 2, 3]
    episode_outputs = []
    for episode_number in episode_numbers:
        labels, image_ids, predictions = run_episode(
            args.dataset_root,
            args.episode_data_dir / f"episode_{episode_number}",
            args.output_dir,
            settings,
            fold_seeds,
            args.smoke,
        )
        if args.smoke:
            evaluated = predictions["GLOBAL"] >= 0
            arm_metrics = {
                arm: balanced_accuracy(
                    labels[evaluated], values[evaluated]
                )
                for arm, values in predictions.items()
            }
            summary = {
                "experiment_id": protocol["experiment_id"],
                "mode": "SMOKE",
                "episode": 1,
                "fold": 0,
                "epochs": 1,
                "evaluated_images": int(evaluated.sum()),
                "arms": arm_metrics,
                "official_test_images_decoded_or_encoded": 0,
            }
            (args.output_dir / "smoke_summary.json").write_text(
                json.dumps(summary, indent=2, sort_keys=True) + "\n"
            )
            print(json.dumps(summary, indent=2, sort_keys=True))
            return

        metrics = {}
        global_recall = class_recall(labels, predictions["GLOBAL"])
        for arm in ARMS:
            recall = class_recall(labels, predictions[arm])
            delta = recall - global_recall
            metrics[arm] = {
                "oof_balanced_accuracy": balanced_accuracy(
                    labels, predictions[arm]
                ),
                "delta_pp_vs_global": 100 * float(delta.mean()),
                "negative_transfer_class_rate_vs_global": (
                    0.0 if arm == "GLOBAL" else float(np.mean(delta < 0))
                ),
                "worst_class_delta_pp_vs_global": 100 * float(delta.min()),
            }
        episode_outputs.append(
            {
                "episode": episode_number,
                "metrics": metrics,
                "labels": labels,
                "image_ids": image_ids,
                "predictions": predictions,
            }
        )
        np.savez_compressed(
            args.output_dir / f"episode_{episode_number}_predictions.npz",
            labels=labels,
            image_ids=image_ids,
            **{
                f"{arm}_predictions": values
                for arm, values in predictions.items()
            },
        )
        print(
            json.dumps(
                {
                    "episode": episode_number,
                    "metrics": metrics,
                    "status": "EPISODE_COMPLETE",
                },
                sort_keys=True,
            ),
            flush=True,
        )

    k1_gains = np.asarray(
        [
            item["metrics"]["RANDOM_K1"]["delta_pp_vs_global"]
            for item in episode_outputs
        ]
    )
    oracle_gains = np.asarray(
        [
            item["metrics"]["FULL_KEYPOINT_ORACLE"][
                "delta_pp_vs_global"
            ]
            for item in episode_outputs
        ]
    )
    negative_rates = np.asarray(
        [
            item["metrics"]["RANDOM_K1"][
                "negative_transfer_class_rate_vs_global"
            ]
            for item in episode_outputs
        ]
    )
    pooled_labels = np.concatenate(
        [item["labels"] for item in episode_outputs]
    )
    pooled_predictions = {
        arm: np.concatenate(
            [item["predictions"][arm] for item in episode_outputs]
        )
        for arm in ARMS
    }
    pooled_global_recall = class_recall(
        pooled_labels, pooled_predictions["GLOBAL"]
    )
    pooled_k1_recall = class_recall(
        pooled_labels, pooled_predictions["RANDOM_K1"]
    )
    pooled_oracle_recall = class_recall(
        pooled_labels, pooled_predictions["FULL_KEYPOINT_ORACLE"]
    )
    pooled_k1_delta = pooled_k1_recall - pooled_global_recall
    pooled_oracle_delta = pooled_oracle_recall - pooled_global_recall

    sparse_value_reliable = bool(
        k1_gains.mean() >= 3.0 and np.sum(k1_gains >= 3.0) >= 2
    )
    positive_ceiling_reliable = bool(
        oracle_gains.mean() >= 2.0 and np.sum(oracle_gains >= 2.0) >= 2
    )
    negative_rate_range_pp = 100 * float(
        negative_rates.max() - negative_rates.min()
    )
    class_risk_reliable = bool(negative_rate_range_pp <= 10.0)
    overall_go = bool(
        sparse_value_reliable
        and positive_ceiling_reliable
        and class_risk_reliable
    )
    summary = {
        "experiment_id": protocol["experiment_id"],
        "mode": "FORMAL",
        "fixed_epochs": settings["epochs"],
        "protocol_sha256": sha256(args.protocol),
        "official_test_images_decoded_or_encoded": 0,
        "episodes": [
            {
                "episode": item["episode"],
                "metrics": item["metrics"],
            }
            for item in episode_outputs
        ],
        "aggregates": {
            "random_k1_gain_pp_mean": float(k1_gains.mean()),
            "random_k1_gain_pp_sample_std": float(k1_gains.std(ddof=1)),
            "random_k1_episodes_gain_at_least_3pp": int(
                np.sum(k1_gains >= 3.0)
            ),
            "full_oracle_gain_pp_mean": float(oracle_gains.mean()),
            "full_oracle_gain_pp_sample_std": float(
                oracle_gains.std(ddof=1)
            ),
            "full_oracle_episodes_gain_at_least_2pp": int(
                np.sum(oracle_gains >= 2.0)
            ),
            "random_k1_negative_transfer_rate_mean": float(
                negative_rates.mean()
            ),
            "random_k1_negative_transfer_rate_range_pp": (
                negative_rate_range_pp
            ),
            "pooled_random_k1_gain_pp": 100
            * float(pooled_k1_delta.mean()),
            "pooled_random_k1_gain_class_bootstrap_95ci_pp": [
                100 * x
                for x in bootstrap_class_mean_interval(pooled_k1_delta)
            ],
            "pooled_random_k1_negative_transfer_class_rate": float(
                np.mean(pooled_k1_delta < 0)
            ),
            "pooled_random_k1_worst_class_delta_pp": 100
            * float(pooled_k1_delta.min()),
            "pooled_full_oracle_gain_pp": 100
            * float(pooled_oracle_delta.mean()),
        },
        "gates": {
            "sparse_value_reliable": sparse_value_reliable,
            "positive_ceiling_reliable": positive_ceiling_reliable,
            "class_risk_reliable": class_risk_reliable,
            "overall_go": overall_go,
            "next_action": (
                "FORMULATE_CLASS_LEVEL_ALLOCATION_OR_WORST_CLASS_RISK"
                if overall_go
                else "STOP_CUB_SPARSE_KEYPOINT_DIRECTION"
            ),
        },
    }
    (args.output_dir / "cub_episode_audit_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    np.savez_compressed(
        args.output_dir / "cub_episode_audit_pooled_predictions.npz",
        labels=pooled_labels,
        **{
            f"{arm}_predictions": values
            for arm, values in pooled_predictions.items()
        },
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
