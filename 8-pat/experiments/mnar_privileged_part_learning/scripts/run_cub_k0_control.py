#!/usr/bin/env python3
"""Run the architecture-matched PrPool K0 control for PAT-D-260728-010."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def class_recall(labels, predictions):
    return np.asarray(
        [
            np.mean(predictions[labels == class_index] == class_index)
            for class_index in range(200)
        ]
    )


def balanced_accuracy(labels, predictions):
    return float(class_recall(labels, predictions).mean())


def bootstrap_interval(class_deltas, seed=9199, draws=10000):
    rng = np.random.default_rng(seed)
    indices = rng.integers(0, len(class_deltas), (draws, len(class_deltas)))
    return [
        float(value)
        for value in np.quantile(
            class_deltas[indices].mean(axis=1), [0.025, 0.975]
        )
    ]


def evaluate_gates(k1_gains_pp, oracle_gains_pp):
    k1 = np.asarray(k1_gains_pp, dtype=float)
    oracle = np.asarray(oracle_gains_pp, dtype=float)
    sparse = bool(k1.mean() >= 1.0 and np.sum(k1 >= 0.5) >= 2)
    full = bool(
        oracle.mean() >= 2.0 and np.sum(oracle >= 1.0) >= 2
    )
    return sparse, full, bool(sparse and full)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--episode-data-dir", type=Path, required=True)
    parser.add_argument("--reference-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--oracle-protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main():
    import run_cub_missingness_screen as screen

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
    fold_seeds = [int(x) for x in protocol["training"]["fold_model_seeds"]]
    args.output_dir.mkdir(parents=True, exist_ok=True)
    episode_numbers = [1] if args.smoke else [1, 2, 3]
    episode_results = []
    pooled = {"labels": [], "k0": [], "k1": [], "oracle": []}
    for episode_number in episode_numbers:
        episode_dir = args.episode_data_dir / f"episode_{episode_number}"
        rows = [
            json.loads(line)
            for line in (episode_dir / "cub_train_10shot_manifest.jsonl")
            .read_text()
            .splitlines()
        ]
        labels = np.asarray([row["class_index"] for row in rows])
        folds = np.asarray([row["fold"] for row in rows])
        image_ids = np.asarray([row["image_id"] for row in rows])
        if any(
            row["split"] != "train"
            or row["source_split"] != "official_train"
            for row in rows
        ):
            raise RuntimeError("K0 control contains a non-train image")

        reference = np.load(
            args.reference_dir
            / f"episode_{episode_number}_predictions.npz"
        )
        if not np.array_equal(labels, reference["labels"]):
            raise RuntimeError("Reference labels mismatch")
        if not np.array_equal(image_ids, reference["image_ids"]):
            raise RuntimeError("Reference image IDs mismatch")
        k1_prediction = reference["RANDOM_K1_predictions"]
        oracle_prediction = reference["FULL_KEYPOINT_ORACLE_predictions"]

        checkpoint = args.output_dir / (
            f"episode_{episode_number}_k0_smoke.npz"
            if args.smoke
            else f"episode_{episode_number}_k0_predictions.npz"
        )
        if checkpoint.exists() and not args.smoke:
            stored = np.load(checkpoint)
            if (
                np.array_equal(labels, stored["labels"])
                and np.array_equal(image_ids, stored["image_ids"])
                and np.all(stored["PRPOOL_K0_predictions"] >= 0)
            ):
                k0_prediction = stored["PRPOOL_K0_predictions"]
                print(
                    json.dumps(
                        {
                            "episode": episode_number,
                            "status": "RESUMED_FROM_COMPLETE_CHECKPOINT",
                        },
                        sort_keys=True,
                    ),
                    flush=True,
                )
            else:
                raise RuntimeError("Invalid K0 checkpoint")
        else:
            k0_prediction = np.full(len(rows), -1, dtype=np.int64)
            folds_to_run = [0] if args.smoke else list(range(5))
            selected_none = np.zeros(len(rows), dtype=np.bool_)
            for fold in folds_to_run:
                train_indices = np.flatnonzero(folds != fold)
                eval_indices = np.flatnonzero(folds == fold)
                prediction, _, row_indices = screen.fit_fold(
                    args.dataset_root,
                    rows,
                    train_indices,
                    eval_indices,
                    selected_none,
                    settings,
                    fold_seeds[fold],
                    "PRPOOL_K0",
                )
                k0_prediction[row_indices] = prediction
            if args.smoke:
                if int(np.sum(k0_prediction >= 0)) != 400:
                    raise RuntimeError("K0 smoke prediction count mismatch")
            elif np.any(k0_prediction < 0):
                raise RuntimeError("Incomplete K0 predictions")
            np.savez_compressed(
                checkpoint,
                labels=labels,
                image_ids=image_ids,
                PRPOOL_K0_predictions=k0_prediction,
            )

        evaluated = k0_prediction >= 0
        if args.smoke:
            summary = {
                "experiment_id": protocol["experiment_id"],
                "mode": "SMOKE",
                "episode": 1,
                "fold": 0,
                "epochs": 1,
                "evaluated_images": int(evaluated.sum()),
                "prpool_k0_balanced_accuracy": balanced_accuracy(
                    labels[evaluated], k0_prediction[evaluated]
                ),
                "official_test_images_decoded_or_encoded": 0,
            }
            (args.output_dir / "smoke_summary.json").write_text(
                json.dumps(summary, indent=2, sort_keys=True) + "\n"
            )
            print(json.dumps(summary, indent=2, sort_keys=True))
            return

        k0_recall = class_recall(labels, k0_prediction)
        k1_recall = class_recall(labels, k1_prediction)
        oracle_recall = class_recall(labels, oracle_prediction)
        k1_delta = k1_recall - k0_recall
        oracle_delta = oracle_recall - k0_recall
        metrics = {
            "prpool_k0_oof_ba": balanced_accuracy(labels, k0_prediction),
            "random_k1_oof_ba": balanced_accuracy(labels, k1_prediction),
            "full_oracle_oof_ba": balanced_accuracy(
                labels, oracle_prediction
            ),
            "random_k1_gain_pp_vs_k0": 100 * float(k1_delta.mean()),
            "full_oracle_gain_pp_vs_k0": 100
            * float(oracle_delta.mean()),
            "random_k1_negative_transfer_class_rate_vs_k0": float(
                np.mean(k1_delta < 0)
            ),
            "random_k1_worst_class_delta_pp_vs_k0": 100
            * float(k1_delta.min()),
        }
        episode_results.append(
            {"episode": episode_number, "metrics": metrics}
        )
        pooled["labels"].append(labels)
        pooled["k0"].append(k0_prediction)
        pooled["k1"].append(k1_prediction)
        pooled["oracle"].append(oracle_prediction)
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

    k1_gains = [
        item["metrics"]["random_k1_gain_pp_vs_k0"]
        for item in episode_results
    ]
    oracle_gains = [
        item["metrics"]["full_oracle_gain_pp_vs_k0"]
        for item in episode_results
    ]
    sparse_gate, full_gate, overall_gate = evaluate_gates(
        k1_gains, oracle_gains
    )
    pooled_labels = np.concatenate(pooled["labels"])
    pooled_k0 = np.concatenate(pooled["k0"])
    pooled_k1 = np.concatenate(pooled["k1"])
    pooled_oracle = np.concatenate(pooled["oracle"])
    pooled_k0_recall = class_recall(pooled_labels, pooled_k0)
    pooled_k1_delta = (
        class_recall(pooled_labels, pooled_k1) - pooled_k0_recall
    )
    pooled_oracle_delta = (
        class_recall(pooled_labels, pooled_oracle) - pooled_k0_recall
    )
    summary = {
        "experiment_id": protocol["experiment_id"],
        "mode": "FORMAL",
        "fixed_epochs": settings["epochs"],
        "protocol_sha256": sha256(args.protocol),
        "official_test_images_decoded_or_encoded": 0,
        "episodes": episode_results,
        "aggregates": {
            "random_k1_gain_pp_vs_k0_mean": float(np.mean(k1_gains)),
            "random_k1_gain_pp_vs_k0_sample_std": float(
                np.std(k1_gains, ddof=1)
            ),
            "random_k1_episodes_gain_at_least_0_5pp": int(
                np.sum(np.asarray(k1_gains) >= 0.5)
            ),
            "full_oracle_gain_pp_vs_k0_mean": float(
                np.mean(oracle_gains)
            ),
            "full_oracle_episodes_gain_at_least_1pp": int(
                np.sum(np.asarray(oracle_gains) >= 1.0)
            ),
            "pooled_random_k1_gain_pp_vs_k0": 100
            * float(pooled_k1_delta.mean()),
            "pooled_random_k1_gain_class_bootstrap_95ci_pp": [
                100 * value
                for value in bootstrap_interval(pooled_k1_delta)
            ],
            "pooled_random_k1_negative_transfer_class_rate_vs_k0": float(
                np.mean(pooled_k1_delta < 0)
            ),
            "pooled_random_k1_worst_class_delta_pp_vs_k0": 100
            * float(pooled_k1_delta.min()),
            "pooled_full_oracle_gain_pp_vs_k0": 100
            * float(pooled_oracle_delta.mean()),
        },
        "gates": {
            "sparse_keypoint_value_isolated": sparse_gate,
            "full_keypoint_value_isolated": full_gate,
            "overall_go": overall_gate,
            "next_action": (
                "FORMULATE_CLASS_LEVEL_ALLOCATION_OR_WORST_CLASS_RISK"
                if overall_gate
                else "STOP_CUB_SPARSE_KEYPOINT_DIRECTION"
            ),
        },
    }
    (args.output_dir / "cub_k0_control_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    np.savez_compressed(
        args.output_dir / "cub_k0_control_pooled_predictions.npz",
        labels=pooled_labels,
        PRPOOL_K0_predictions=pooled_k0,
        RANDOM_K1_predictions=pooled_k1,
        FULL_KEYPOINT_ORACLE_predictions=pooled_oracle,
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
