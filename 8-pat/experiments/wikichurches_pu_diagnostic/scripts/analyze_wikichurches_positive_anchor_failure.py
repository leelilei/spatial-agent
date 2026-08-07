#!/usr/bin/env python3
"""Post-hoc diagnosis of the validation-only positive-anchor NO-GO."""

from __future__ import annotations

import argparse
import csv
import json
import statistics
from pathlib import Path

import torch


def accuracy(predictions: torch.Tensor, labels: torch.Tensor) -> float:
    return 100.0 * float((predictions == labels).float().mean())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--local-val", type=Path, required=True)
    parser.add_argument("--prediction-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--ratio", type=float, default=0.01)
    parser.add_argument("--gamma", type=float, default=20.0)
    args = parser.parse_args()

    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    local = torch.load(args.local_val, map_location="cpu")
    if local["split"] != "val" or int(local["test_images_encoded"]) != 0:
        raise RuntimeError("Diagnosis must use validation-only local features")
    labels = local["labels"].long()
    style_names = list(local["style_names"])
    local_scores = local["official_local_scores"][str(args.ratio)].float()
    random_scores = local["random_local_scores"][str(args.ratio)].float()

    local_only_accuracy = accuracy(local_scores.argmax(dim=-1), labels)
    random_local_only_accuracies = [
        accuracy(scores.argmax(dim=-1), labels) for scores in random_scores
    ]
    official_local_prediction = local_scores.argmax(dim=-1)
    random_mean_scores = random_scores.mean(dim=0)
    branch_class_rows = []
    for class_index, class_name in enumerate(style_names):
        class_mask = labels == class_index
        branch_class_rows.append(
            {
                "class_name": class_name,
                "true_examples": int(class_mask.sum()),
                "official_predicted_examples": int(
                    (official_local_prediction == class_index).sum()
                ),
                "official_local_recall": accuracy(
                    official_local_prediction[class_mask],
                    labels[class_mask],
                ),
                "official_score_mean": float(local_scores[:, class_index].mean()),
                "random_score_mean": float(
                    random_mean_scores[:, class_index].mean()
                ),
                "official_minus_random_score_mean": float(
                    (
                        local_scores[:, class_index]
                        - random_mean_scores[:, class_index]
                    ).mean()
                ),
            }
        )
    class_rows = []
    bucket_rows = []
    run_rows = []
    for shots in [int(value) for value in protocol["shots"]]:
        for seed in [int(value) for value in protocol["development_seeds"]]:
            path = args.prediction_dir / f"tipf_s{shots}_seed{seed}.pt"
            prediction = torch.load(path, map_location="cpu")
            if not prediction["validation_only"]:
                raise RuntimeError(f"Non-development file in diagnosis: {path}")
            logits = prediction["val_logits"].float()
            if not torch.equal(prediction["val_labels"].long(), labels):
                raise RuntimeError(f"Label/order mismatch: {path}")
            baseline_prediction = logits.argmax(dim=-1)
            fused_prediction = (logits + args.gamma * local_scores).argmax(dim=-1)
            baseline_correct = baseline_prediction == labels
            fused_correct = fused_prediction == labels
            run_rows.append(
                {
                    "shots": shots,
                    "seed": seed,
                    "baseline_accuracy": accuracy(baseline_prediction, labels),
                    "fused_accuracy": accuracy(fused_prediction, labels),
                    "rescued_images": int((~baseline_correct & fused_correct).sum()),
                    "harmed_images": int((baseline_correct & ~fused_correct).sum()),
                }
            )
            for class_index, class_name in enumerate(style_names):
                mask = labels == class_index
                baseline_class_accuracy = accuracy(
                    baseline_prediction[mask],
                    labels[mask],
                )
                fused_class_accuracy = accuracy(
                    fused_prediction[mask],
                    labels[mask],
                )
                class_rows.append(
                    {
                        "shots": shots,
                        "seed": seed,
                        "class_name": class_name,
                        "examples": int(mask.sum()),
                        "baseline_accuracy": baseline_class_accuracy,
                        "fused_accuracy": fused_class_accuracy,
                        "delta": fused_class_accuracy - baseline_class_accuracy,
                    }
                )

            top_two = logits.topk(2, dim=-1).values
            margins = top_two[:, 0] - top_two[:, 1]
            order = torch.argsort(margins)
            for bucket, indices in enumerate(torch.tensor_split(order, 4), start=1):
                bucket_rows.append(
                    {
                        "shots": shots,
                        "seed": seed,
                        "confidence_quartile": bucket,
                        "examples": len(indices),
                        "mean_global_margin": float(margins[indices].mean()),
                        "baseline_accuracy": accuracy(
                            baseline_prediction[indices],
                            labels[indices],
                        ),
                        "fused_accuracy": accuracy(
                            fused_prediction[indices],
                            labels[indices],
                        ),
                        "delta": (
                            accuracy(fused_prediction[indices], labels[indices])
                            - accuracy(
                                baseline_prediction[indices],
                                labels[indices],
                            )
                        ),
                    }
                )

    summary = {
        "experiment_id": protocol["experiment_id"],
        "stage": "posthoc_validation_only_diagnosis",
        "ratio": args.ratio,
        "gamma": args.gamma,
        "test_images_encoded": int(local["test_images_encoded"]),
        "official_local_only_accuracy": local_only_accuracy,
        "random_local_only_accuracy_mean": statistics.mean(
            random_local_only_accuracies
        ),
        "random_local_only_accuracy_range": [
            min(random_local_only_accuracies),
            max(random_local_only_accuracies),
        ],
    }
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for name, rows in (
        ("per_run_rescue_harm.csv", run_rows),
        ("per_class.csv", class_rows),
        ("confidence_quartiles.csv", bucket_rows),
        ("local_branch_class_audit.csv", branch_class_rows),
    ):
        with (args.out_dir / name).open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    (args.out_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
