#!/usr/bin/env python3
"""Known-inclusion-probability PU diagnostic on stochastic candidate samples.

The candidate pool must contain independent Bernoulli inclusion probabilities
and sampled indicators. The experiment compares unweighted sampled-U nnPU,
self-normalized inverse-probability-weighted nnPU, and nnPU trained on the full
candidate census. FullPool is a sampling-risk reference, not label Oracle.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import random
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import torch
from sklearn.metrics import average_precision_score, roc_auc_score

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))
import real_pu_no_adjudication_probe as shared  # noqa: E402


def region_key(row: dict[str, object], source: str) -> tuple[object, ...]:
    if source == "official":
        return (
            source,
            row["image_filename"],
            row.get("group_index", ""),
            row.get("element_index", ""),
            row["left"],
            row["top"],
            row["width"],
            row["height"],
        )
    return (
        source,
        row["image_filename"],
        round(float(row["left"]), 10),
        round(float(row["top"]), 10),
        round(float(row["width"]), 10),
        round(float(row["height"]), 10),
    )


def assign_feature_indices(
    official: list[dict[str, object]],
    pool: list[dict[str, object]],
) -> list[dict[str, object]]:
    unique_records: list[dict[str, object]] = []
    index_by_key: dict[tuple[object, ...], int] = {}
    for rows, source in ((official, "official"), (pool, "pool")):
        for row in rows:
            key = region_key(row, source)
            if key not in index_by_key:
                index_by_key[key] = len(unique_records)
                unique_records.append(row)
            row["feature_index"] = index_by_key[key]
    return unique_records


def bootstrap_mean_ci(
    values: list[float],
    seed: int,
    replicates: int = 5000,
) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    array = np.asarray(values, dtype=float)
    draws = array[
        rng.integers(0, len(array), size=(replicates, len(array)))
    ].mean(axis=1)
    return float(np.quantile(draws, 0.025)), float(np.quantile(draws, 0.975))


def method_label_means(
    rows: list[dict[str, object]],
    labels: list[str],
    method: str,
    field: str,
) -> list[float]:
    return [
        float(
            np.mean(
                [
                    float(row[field])
                    for row in rows
                    if row["method"] == method and row["label"] == label
                ]
            )
        )
        for label in labels
    ]


def paired_label_deltas(
    rows: list[dict[str, object]],
    labels: list[str],
    repeats: int,
    left: str,
    right: str,
    field: str,
) -> list[float]:
    index = {
        (str(row["label"]), int(row["repeat"]), str(row["method"])): row
        for row in rows
    }
    deltas: list[float] = []
    for label in labels:
        repeat_deltas: list[float] = []
        for repeat in range(repeats):
            left_row = index.get((label, repeat, left))
            right_row = index.get((label, repeat, right))
            if left_row is None or right_row is None:
                continue
            repeat_deltas.append(
                float(left_row[field]) - float(right_row[field])
            )
        if repeat_deltas:
            deltas.append(float(np.mean(repeat_deltas)))
    return deltas


def paired_absolute_gap_delta(
    rows: list[dict[str, object]],
    labels: list[str],
    repeats: int,
    left: str,
    right: str,
    reference: str,
    field: str,
) -> list[float]:
    index = {
        (str(row["label"]), int(row["repeat"]), str(row["method"])): row
        for row in rows
    }
    deltas: list[float] = []
    for label in labels:
        repeat_deltas: list[float] = []
        for repeat in range(repeats):
            left_row = index.get((label, repeat, left))
            right_row = index.get((label, repeat, right))
            reference_row = index.get((label, repeat, reference))
            if left_row is None or right_row is None or reference_row is None:
                continue
            target = float(reference_row[field])
            repeat_deltas.append(
                abs(float(left_row[field]) - target)
                - abs(float(right_row[field]) - target)
            )
        if repeat_deltas:
            deltas.append(float(np.mean(repeat_deltas)))
    return deltas


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--parts", type=Path, required=True)
    parser.add_argument("--official-boxes", type=Path, required=True)
    parser.add_argument("--candidate-pool", type=Path, required=True)
    parser.add_argument("--image-dir", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument(
        "--feature-cache",
        type=Path,
        help="Validated .npz cache shared across candidate resamples.",
    )
    parser.add_argument("--model", default="ViT-B/16")
    parser.add_argument("--device", default="auto")
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--context", type=float, default=0.1)
    parser.add_argument("--min-positive-count", type=int, default=8)
    parser.add_argument("--min-sampled-count", type=int, default=8)
    parser.add_argument("--min-train-sampled", type=int, default=1)
    parser.add_argument("--repeats", type=int, default=30)
    parser.add_argument("--eval-positive-images", type=int, default=2)
    parser.add_argument("--eval-negative-images", type=int, default=5)
    parser.add_argument("--class-prior", type=float, default=0.25)
    parser.add_argument("--seed", type=int, default=20260726)
    parser.add_argument("--nnpu-epochs", type=int, default=250)
    parser.add_argument("--nnpu-lr", type=float, default=0.05)
    parser.add_argument("--nnpu-weight-decay", type=float, default=1e-4)
    args = parser.parse_args()

    if args.class_prior <= 0 or args.class_prior >= 1:
        raise ValueError("class-prior must be in (0, 1)")

    filenames = {
        row["image_filename"]
        for row in csv.DictReader(args.manifest.open())
    }
    payload = json.loads(args.parts.read_text())
    ancestors = shared.ancestor_sets(payload["meta"])
    official = [
        {**row, "source": "official"}
        for row in csv.DictReader(args.official_boxes.open())
        if row["image_filename"] in filenames
    ]
    pool = [
        {**row, "source": "pool"}
        for row in csv.DictReader(args.candidate_pool.open())
        if row["image_filename"] in filenames
    ]
    if not pool or "sampling_probability" not in pool[0] or "sampled" not in pool[0]:
        raise ValueError("Candidate pool lacks probability/sample columns")
    probabilities = np.asarray(
        [float(row["sampling_probability"]) for row in pool]
    )
    if np.any(probabilities <= 0) or np.any(probabilities >= 1):
        raise ValueError("Known inclusion probabilities must be in (0, 1)")

    unique_records = assign_feature_indices(official, pool)
    positive_counts = Counter(str(row["label"]) for row in official)
    sampled_counts = Counter(
        str(row["label"]) for row in pool if int(row["sampled"]) == 1
    )
    pool_counts = Counter(str(row["label"]) for row in pool)
    labels = sorted(
        label
        for label, count in positive_counts.items()
        if count >= args.min_positive_count
        and sampled_counts[label] >= args.min_sampled_count
    )
    if not labels:
        raise ValueError("No label satisfies positive/sampled thresholds")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    device = shared.choose_device(args.device)
    print(
        f"device={device} model={args.model} official={len(official)} "
        f"pool_rows={len(pool)} unique_regions={len(unique_records)} "
        f"sampled={sum(int(row['sampled']) for row in pool)} "
        f"labels={len(labels)}",
        flush=True,
    )
    cache_payload = json.dumps(
        {
            "context": args.context,
            "model": args.model,
            "regions": [
                region_key(row, str(row["source"]))
                for row in unique_records
            ],
        },
        ensure_ascii=True,
        separators=(",", ":"),
    )
    cache_fingerprint = hashlib.sha256(
        cache_payload.encode("utf-8")
    ).hexdigest()
    features: np.ndarray
    feature_source = "encoded"
    if args.feature_cache is not None and args.feature_cache.exists():
        with np.load(args.feature_cache, allow_pickle=False) as cached:
            cached_fingerprint = str(cached["fingerprint"].item())
            features = np.asarray(cached["features"], dtype=np.float32)
        if cached_fingerprint != cache_fingerprint:
            raise ValueError(
                "Feature cache fingerprint does not match the region census"
            )
        if features.shape[0] != len(unique_records):
            raise ValueError("Feature cache row count is invalid")
        feature_source = "cache"
    else:
        toga_root = Path(
            os.environ.get("TOGA_ROOT", str(PROJECT_ROOT / "vendor" / "TOGA"))
        )
        sys.path.insert(0, str(toga_root))
        import clip as openai_clip  # noqa: E402

        model, preprocess = openai_clip.load(args.model, device=device)
        model.eval()
        features = shared.encode_regions(
            unique_records,
            args.image_dir,
            model,
            preprocess,
            device,
            args.batch_size,
            args.context,
        ).astype(np.float32, copy=False)
        if args.feature_cache is not None:
            args.feature_cache.parent.mkdir(parents=True, exist_ok=True)
            np.savez_compressed(
                args.feature_cache,
                features=features,
                fingerprint=np.asarray(cache_fingerprint),
            )
    print(
        f"feature_source={feature_source} feature_shape={features.shape} "
        f"fingerprint={cache_fingerprint[:12]}",
        flush=True,
    )

    methods = (
        "PN-sampled",
        "Ignore",
        "nnPU-sampled",
        "IPW-nnPU",
        "FullPool-nnPU",
    )
    results: list[dict[str, object]] = []

    for label in labels:
        positive_images = sorted(
            {
                str(row["image_filename"])
                for row in official
                if row["label"] == label
            }
        )
        nonpositive_images = sorted(filenames - set(positive_images))
        for repeat in range(args.repeats):
            split_seed = (
                args.seed
                + repeat * 1009
                + sum(map(ord, shared.normalize_label(label)))
            )
            rng = random.Random(split_seed)
            shuffled_positive = positive_images[:]
            shuffled_nonpositive = nonpositive_images[:]
            rng.shuffle(shuffled_positive)
            rng.shuffle(shuffled_nonpositive)
            eval_images = set(
                shuffled_positive[: args.eval_positive_images]
                + shuffled_nonpositive[: args.eval_negative_images]
            )

            train_positive = [
                int(row["feature_index"])
                for row in official
                if row["label"] == label
                and row["image_filename"] not in eval_images
            ]
            eval_positive = [
                int(row["feature_index"])
                for row in official
                if row["label"] == label
                and row["image_filename"] in eval_images
            ]
            train_negative = [
                int(row["feature_index"])
                for row in official
                if row["image_filename"] not in eval_images
                and not shared.compatible(
                    label, str(row["label"]), ancestors
                )
            ]
            eval_negative = [
                int(row["feature_index"])
                for row in official
                if row["image_filename"] in eval_images
                and not shared.compatible(
                    label, str(row["label"]), ancestors
                )
            ]
            sampled_rows = [
                row
                for row in pool
                if row["label"] == label
                and row["image_filename"] not in eval_images
                and int(row["sampled"]) == 1
            ]
            full_rows = [
                row
                for row in pool
                if row["label"] == label
                and row["image_filename"] not in eval_images
            ]
            train_sampled = [
                int(row["feature_index"]) for row in sampled_rows
            ]
            train_full = [int(row["feature_index"]) for row in full_rows]
            if (
                len(train_positive) < 4
                or len(eval_positive) < 2
                or len(train_negative) < 8
                or len(eval_negative) < 5
                or len(train_sampled) < args.min_train_sampled
                or len(train_full) < 50
            ):
                continue

            rng.shuffle(train_negative)
            train_negative = train_negative[
                : min(
                    len(train_negative),
                    max(24, 6 * len(train_positive)),
                )
            ]
            inclusion = np.asarray(
                [
                    float(row["sampling_probability"])
                    for row in sampled_rows
                ],
                dtype=np.float32,
            )
            ipw = 1.0 / inclusion
            ipw = ipw / ipw.mean()
            ipw_ess = float(ipw.sum() ** 2 / (ipw**2).sum())

            fitted: dict[str, object] = {
                "PN-sampled": shared.fit_supervised(
                    features,
                    train_positive,
                    train_negative + train_sampled,
                    split_seed,
                ),
                "Ignore": shared.fit_supervised(
                    features,
                    train_positive,
                    train_negative,
                    split_seed,
                ),
                "nnPU-sampled": shared.fit_nnpu(
                    features,
                    train_positive,
                    train_sampled,
                    args.class_prior,
                    split_seed,
                    args.nnpu_epochs,
                    args.nnpu_lr,
                    args.nnpu_weight_decay,
                    device,
                ),
                "IPW-nnPU": shared.fit_nnpu(
                    features,
                    train_positive,
                    train_sampled,
                    args.class_prior,
                    split_seed,
                    args.nnpu_epochs,
                    args.nnpu_lr,
                    args.nnpu_weight_decay,
                    device,
                    unlabeled_weights=ipw,
                ),
                "FullPool-nnPU": shared.fit_nnpu(
                    features,
                    train_positive,
                    train_full,
                    args.class_prior,
                    split_seed,
                    args.nnpu_epochs,
                    args.nnpu_lr,
                    args.nnpu_weight_decay,
                    device,
                ),
            }

            eval_indices = eval_positive + eval_negative
            eval_y = np.asarray(
                [1] * len(eval_positive) + [0] * len(eval_negative)
            )
            for method, fitted_model in fitted.items():
                eval_scores = shared.predict_scores(
                    fitted_model, features, eval_indices
                )
                full_scores = shared.predict_scores(
                    fitted_model, features, train_full
                )
                results.append(
                    {
                        "label": label,
                        "repeat": repeat,
                        "method": method,
                        "split_seed": split_seed,
                        "positive_count": positive_counts[label],
                        "sampled_count_total": sampled_counts[label],
                        "pool_count_total": pool_counts[label],
                        "train_positive": len(train_positive),
                        "train_reliable_negative": len(train_negative),
                        "train_sampled": len(train_sampled),
                        "train_full_pool": len(train_full),
                        "eval_positive": len(eval_positive),
                        "eval_reliable_negative": len(eval_negative),
                        "sampling_probability_min": float(
                            inclusion.min()
                        ),
                        "sampling_probability_median": float(
                            np.median(inclusion)
                        ),
                        "sampling_probability_max": float(
                            inclusion.max()
                        ),
                        "ipw_ess": ipw_ess,
                        "roc_auc": roc_auc_score(eval_y, eval_scores),
                        "average_precision": average_precision_score(
                            eval_y, eval_scores
                        ),
                        "eval_positive_mean_score": float(
                            eval_scores[: len(eval_positive)].mean()
                        ),
                        "full_pool_mean_score": float(full_scores.mean()),
                    }
                )
        completed = sum(
            1 for row in results if row["label"] == label
        )
        print(
            f"{label}: P={positive_counts[label]} "
            f"sampled={sampled_counts[label]} pool={pool_counts[label]} "
            f"result_rows={completed}",
            flush=True,
        )

    if not results:
        raise RuntimeError("No complete stochastic P/U split")
    with (args.out_dir / "per_split_results.csv").open(
        "w", newline=""
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(results[0]))
        writer.writeheader()
        writer.writerows(results)

    completed_labels = sorted({str(row["label"]) for row in results})
    report = [
        "# Stochastic known-inclusion-probability P/U diagnostic",
        "",
        "## Boundary",
        "",
        "- U is sampled with recorded independent Bernoulli probability q;",
        "- IPW uses self-normalized 1/q on the sampled-U negative risk;",
        "- FullPool-nnPU uses the candidate census as sampling-risk reference;",
        "- FullPool is not label Oracle and U still has no human truth.",
        "",
        f"- Encoder: `{args.model}`",
        f"- Images: {len(filenames)}",
        f"- Official boxes: {len(official)}",
        f"- Candidate pool rows: {len(pool)}",
        f"- Unique encoded regions: {len(unique_records)}",
        f"- Sampled rows: {sum(int(row['sampled']) for row in pool)}",
        f"- Labels: {len(completed_labels)}",
        f"- Repeats: {args.repeats} / label",
        f"- Class prior: {args.class_prior:.2f}",
        "",
        "## Held-out known-label performance",
        "",
        "| Method | ROC-AUC | 95% CI | AP | 95% CI | P score | pool score |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for method in methods:
        aucs = method_label_means(
            results, completed_labels, method, "roc_auc"
        )
        aps = method_label_means(
            results, completed_labels, method, "average_precision"
        )
        auc_ci = bootstrap_mean_ci(aucs, args.seed)
        ap_ci = bootstrap_mean_ci(aps, args.seed + 1)
        report.append(
            f"| {method} | {np.mean(aucs):.3f} | "
            f"{auc_ci[0]:.3f}–{auc_ci[1]:.3f} | "
            f"{np.mean(aps):.3f} | "
            f"{ap_ci[0]:.3f}–{ap_ci[1]:.3f} | "
            f"{np.mean(method_label_means(results, completed_labels, method, 'eval_positive_mean_score')):.3f} | "
            f"{np.mean(method_label_means(results, completed_labels, method, 'full_pool_mean_score')):.3f} |"
        )

    report.extend(
        [
            "",
            "## Sampling diagnostics",
            "",
            f"- q min/median/max over split samples: "
            f"{np.mean([float(row['sampling_probability_min']) for row in results]):.3f}/"
            f"{np.mean([float(row['sampling_probability_median']) for row in results]):.3f}/"
            f"{np.mean([float(row['sampling_probability_max']) for row in results]):.3f}",
            f"- IPW ESS mean: "
            f"{np.mean([float(row['ipw_ess']) for row in results]):.2f}",
            "",
            "## Paired differences",
            "",
            "| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    comparisons = (
        ("IPW-nnPU", "nnPU-sampled"),
        ("IPW-nnPU", "FullPool-nnPU"),
        ("nnPU-sampled", "FullPool-nnPU"),
        ("IPW-nnPU", "Ignore"),
    )
    for left, right in comparisons:
        auc_delta = paired_label_deltas(
            results,
            completed_labels,
            args.repeats,
            left,
            right,
            "roc_auc",
        )
        ap_delta = paired_label_deltas(
            results,
            completed_labels,
            args.repeats,
            left,
            right,
            "average_precision",
        )
        auc_ci = bootstrap_mean_ci(auc_delta, args.seed + 2)
        ap_ci = bootstrap_mean_ci(ap_delta, args.seed + 3)
        report.append(
            f"| {left} − {right} | {np.mean(auc_delta):+.3f} | "
            f"{auc_ci[0]:+.3f}–{auc_ci[1]:+.3f} | "
            f"{np.mean(ap_delta):+.3f} | "
            f"{ap_ci[0]:+.3f}–{ap_ci[1]:+.3f} |"
        )

    report.extend(
        [
            "",
            "## FullPool approximation",
            "",
            "Negative values mean IPW is closer to FullPool than unweighted "
            "sampled-U nnPU.",
            "",
            "| Gap contrast | Δ absolute AUC gap | 95% CI | "
            "Δ absolute AP gap | 95% CI |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    auc_gap = paired_absolute_gap_delta(
        results,
        completed_labels,
        args.repeats,
        "IPW-nnPU",
        "nnPU-sampled",
        "FullPool-nnPU",
        "roc_auc",
    )
    ap_gap = paired_absolute_gap_delta(
        results,
        completed_labels,
        args.repeats,
        "IPW-nnPU",
        "nnPU-sampled",
        "FullPool-nnPU",
        "average_precision",
    )
    auc_gap_ci = bootstrap_mean_ci(auc_gap, args.seed + 4)
    ap_gap_ci = bootstrap_mean_ci(ap_gap, args.seed + 5)
    report.append(
        f"| IPW gap − unweighted gap | {np.mean(auc_gap):+.3f} | "
        f"{auc_gap_ci[0]:+.3f}–{auc_gap_ci[1]:+.3f} | "
        f"{np.mean(ap_gap):+.3f} | "
        f"{ap_gap_ci[0]:+.3f}–{ap_gap_ci[1]:+.3f} |"
    )
    report.extend(
        [
            "",
            "This experiment identifies candidate-sampling correction only. "
            "It does not identify annotation propensity, missing-positive "
            "precision, or Oracle performance.",
        ]
    )
    (args.out_dir / "stochastic_ipw_report.md").write_text(
        "\n".join(report) + "\n"
    )


if __name__ == "__main__":
    main()
