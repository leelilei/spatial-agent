#!/usr/bin/env python3
"""Conservative positive expansion without treating remaining U as negatives.

For each image-disjoint split, an ensemble is trained only on official
positives and hierarchy-incompatible reliable negatives. A sampled candidate
is added as a low-weight positive only when it clears a training-only threshold
in at least four of five ensemble members. All other candidates abstain.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))
import real_pu_no_adjudication_probe as shared  # noqa: E402
import stochastic_ipw_pu_probe as stochastic  # noqa: E402


def load_feature_cache(
    path: Path,
    unique_records: list[dict[str, object]],
    model: str,
    context: float,
) -> np.ndarray:
    payload = json.dumps(
        {
            "context": context,
            "model": model,
            "regions": [
                stochastic.region_key(row, str(row["source"]))
                for row in unique_records
            ],
        },
        ensure_ascii=True,
        separators=(",", ":"),
    )
    fingerprint = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    with np.load(path, allow_pickle=False) as cached:
        cached_fingerprint = str(cached["fingerprint"].item())
        features = np.asarray(cached["features"], dtype=np.float32)
    if cached_fingerprint != fingerprint:
        raise ValueError("Feature cache fingerprint mismatch")
    if features.shape[0] != len(unique_records):
        raise ValueError("Feature cache row count mismatch")
    print(
        f"feature_source=cache feature_shape={features.shape} "
        f"fingerprint={fingerprint[:12]}",
        flush=True,
    )
    return features


def fit_weighted_expansion(
    features: np.ndarray,
    official_positives: list[int],
    pseudo_positives: list[int],
    reliable_negatives: list[int],
    pseudo_weight: float,
    seed: int,
) -> LogisticRegression:
    indices = official_positives + pseudo_positives + reliable_negatives
    labels = np.asarray(
        [1] * (len(official_positives) + len(pseudo_positives))
        + [0] * len(reliable_negatives)
    )
    raw_weights = np.asarray(
        [1.0] * len(official_positives)
        + [pseudo_weight] * len(pseudo_positives)
        + [1.0] * len(reliable_negatives),
        dtype=float,
    )
    positive_total = raw_weights[labels == 1].sum()
    negative_total = raw_weights[labels == 0].sum()
    raw_weights[labels == 1] *= 0.5 / positive_total
    raw_weights[labels == 0] *= 0.5 / negative_total
    raw_weights *= len(raw_weights)
    classifier = LogisticRegression(
        C=1.0,
        max_iter=2000,
        random_state=seed,
    )
    classifier.fit(
        features[indices],
        labels,
        sample_weight=raw_weights,
    )
    return classifier


def select_pseudo_positives(
    features: np.ndarray,
    positives: list[int],
    reliable_negatives: list[int],
    candidates: list[int],
    seed: int,
    ensemble_size: int,
    required_votes: int,
    calibration_fraction: float,
    positive_quantile: float,
) -> tuple[list[int], dict[str, float]]:
    if not candidates:
        return [], {
            "candidate_count": 0.0,
            "selected_count": 0.0,
            "threshold_mean": float("nan"),
            "vote_mean": float("nan"),
            "selected_score_mean": float("nan"),
        }
    candidate_scores = np.empty(
        (ensemble_size, len(candidates)), dtype=float
    )
    thresholds = np.empty(ensemble_size, dtype=float)
    for member in range(ensemble_size):
        rng = np.random.default_rng(seed + 104729 * (member + 1))
        boot_positive = rng.choice(
            positives, size=len(positives), replace=True
        ).tolist()
        shuffled_negative = np.asarray(reliable_negatives, dtype=int)
        rng.shuffle(shuffled_negative)
        calibration_count = max(
            5,
            int(math.ceil(len(shuffled_negative) * calibration_fraction)),
        )
        calibration_count = min(
            calibration_count, len(shuffled_negative) - 4
        )
        calibration_negative = shuffled_negative[:calibration_count].tolist()
        fit_negative = shuffled_negative[calibration_count:].tolist()
        model = shared.fit_supervised(
            features,
            boot_positive,
            fit_negative,
            seed + member,
        )
        calibration_scores = shared.predict_scores(
            model, features, calibration_negative
        )
        positive_scores = shared.predict_scores(
            model, features, positives
        )
        thresholds[member] = max(
            float(np.max(calibration_scores)),
            float(np.quantile(positive_scores, positive_quantile)),
        )
        candidate_scores[member] = shared.predict_scores(
            model, features, candidates
        )
    votes = (candidate_scores >= thresholds[:, None]).sum(axis=0)
    selected_positions = np.flatnonzero(votes >= required_votes)
    selected = [candidates[index] for index in selected_positions]
    selected_score_mean = (
        float(candidate_scores[:, selected_positions].mean())
        if len(selected_positions)
        else float("nan")
    )
    return selected, {
        "candidate_count": float(len(candidates)),
        "selected_count": float(len(selected)),
        "threshold_mean": float(thresholds.mean()),
        "vote_mean": float(votes.mean()),
        "selected_score_mean": selected_score_mean,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--parts", type=Path, required=True)
    parser.add_argument("--official-boxes", type=Path, required=True)
    parser.add_argument("--candidate-pool", type=Path, required=True)
    parser.add_argument("--feature-cache", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--model", default="ViT-B/16")
    parser.add_argument("--context", type=float, default=0.1)
    parser.add_argument("--min-positive-count", type=int, default=8)
    parser.add_argument("--min-sampled-count", type=int, default=8)
    parser.add_argument("--repeats", type=int, default=30)
    parser.add_argument("--eval-positive-images", type=int, default=2)
    parser.add_argument("--eval-negative-images", type=int, default=5)
    parser.add_argument("--seed", type=int, default=20260726)
    parser.add_argument("--ensemble-size", type=int, default=5)
    parser.add_argument("--required-votes", type=int, default=4)
    parser.add_argument("--calibration-fraction", type=float, default=0.25)
    parser.add_argument("--positive-quantile", type=float, default=0.25)
    parser.add_argument("--pseudo-weight", type=float, default=0.25)
    args = parser.parse_args()

    if not 1 <= args.required_votes <= args.ensemble_size:
        raise ValueError("required-votes must be within ensemble size")
    if not 0 < args.calibration_fraction < 0.5:
        raise ValueError("calibration-fraction must be in (0, 0.5)")
    if not 0 <= args.positive_quantile <= 1:
        raise ValueError("positive-quantile must be in [0, 1]")
    if not 0 < args.pseudo_weight <= 1:
        raise ValueError("pseudo-weight must be in (0, 1]")

    filenames = {
        row["image_filename"]
        for row in csv.DictReader(args.manifest.open())
    }
    ancestors = shared.ancestor_sets(
        json.loads(args.parts.read_text())["meta"]
    )
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
    if not pool or "sampled" not in pool[0]:
        raise ValueError("Candidate pool lacks sampled indicator")
    unique_records = stochastic.assign_feature_indices(official, pool)
    features = load_feature_cache(
        args.feature_cache, unique_records, args.model, args.context
    )

    positive_counts = Counter(str(row["label"]) for row in official)
    sampled_counts = Counter(
        str(row["label"]) for row in pool if int(row["sampled"]) == 1
    )
    labels = sorted(
        label
        for label, count in positive_counts.items()
        if count >= args.min_positive_count
        and sampled_counts[label] >= args.min_sampled_count
    )
    if not labels:
        raise ValueError("No label satisfies P/U thresholds")
    print(
        f"official={len(official)} pool_rows={len(pool)} "
        f"sampled={sum(int(row['sampled']) for row in pool)} "
        f"labels={len(labels)}",
        flush=True,
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
            sampled_candidates = list(
                dict.fromkeys(
                    int(row["feature_index"])
                    for row in pool
                    if row["label"] == label
                    and row["image_filename"] not in eval_images
                    and int(row["sampled"]) == 1
                )
            )
            if (
                len(train_positive) < 4
                or len(eval_positive) < 2
                or len(train_negative) < 8
                or len(eval_negative) < 5
            ):
                continue
            rng.shuffle(train_negative)
            train_negative = train_negative[
                : min(
                    len(train_negative),
                    max(24, 6 * len(train_positive)),
                )
            ]
            ignore_model = shared.fit_supervised(
                features,
                train_positive,
                train_negative,
                split_seed,
            )
            selected, diagnostics = select_pseudo_positives(
                features,
                train_positive,
                train_negative,
                sampled_candidates,
                split_seed,
                args.ensemble_size,
                args.required_votes,
                args.calibration_fraction,
                args.positive_quantile,
            )
            expansion_model = (
                fit_weighted_expansion(
                    features,
                    train_positive,
                    selected,
                    train_negative,
                    args.pseudo_weight,
                    split_seed,
                )
                if selected
                else ignore_model
            )
            eval_indices = eval_positive + eval_negative
            eval_y = np.asarray(
                [1] * len(eval_positive) + [0] * len(eval_negative)
            )
            for method, model in (
                ("Ignore", ignore_model),
                ("PositiveExpansion", expansion_model),
            ):
                scores = shared.predict_scores(
                    model, features, eval_indices
                )
                results.append(
                    {
                        "label": label,
                        "repeat": repeat,
                        "method": method,
                        "split_seed": split_seed,
                        "positive_count": positive_counts[label],
                        "sampled_count_total": sampled_counts[label],
                        "train_positive": len(train_positive),
                        "train_reliable_negative": len(train_negative),
                        "train_candidate": int(
                            diagnostics["candidate_count"]
                        ),
                        "selected_pseudo_positive": int(
                            diagnostics["selected_count"]
                        ),
                        "selection_rate": (
                            diagnostics["selected_count"]
                            / diagnostics["candidate_count"]
                            if diagnostics["candidate_count"]
                            else 0.0
                        ),
                        "threshold_mean": diagnostics["threshold_mean"],
                        "vote_mean": diagnostics["vote_mean"],
                        "selected_score_mean": diagnostics[
                            "selected_score_mean"
                        ],
                        "pseudo_weight": args.pseudo_weight,
                        "eval_positive": len(eval_positive),
                        "eval_reliable_negative": len(eval_negative),
                        "roc_auc": roc_auc_score(eval_y, scores),
                        "average_precision": average_precision_score(
                            eval_y, scores
                        ),
                        "eval_positive_mean_score": float(
                            scores[: len(eval_positive)].mean()
                        ),
                    }
                )
        label_rows = [
            row
            for row in results
            if row["label"] == label
            and row["method"] == "PositiveExpansion"
        ]
        print(
            f"{label}: splits={len(label_rows)} "
            f"selected_mean={np.mean([int(row['selected_pseudo_positive']) for row in label_rows]):.2f} "
            f"selection_rate={np.mean([float(row['selection_rate']) for row in label_rows]):.3f}",
            flush=True,
        )

    if not results:
        raise RuntimeError("No complete positive-expansion split")
    args.out_dir.mkdir(parents=True, exist_ok=True)
    with (args.out_dir / "per_split_results.csv").open(
        "w", newline=""
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(results[0]))
        writer.writeheader()
        writer.writerows(results)
    summary = {
        "rows": len(results),
        "labels": len({str(row["label"]) for row in results}),
        "repeats": args.repeats,
        "ensemble_size": args.ensemble_size,
        "required_votes": args.required_votes,
        "calibration_fraction": args.calibration_fraction,
        "positive_quantile": args.positive_quantile,
        "pseudo_weight": args.pseudo_weight,
        "selected_mean": float(
            np.mean(
                [
                    int(row["selected_pseudo_positive"])
                    for row in results
                    if row["method"] == "PositiveExpansion"
                ]
            )
        ),
        "selection_rate_mean": float(
            np.mean(
                [
                    float(row["selection_rate"])
                    for row in results
                    if row["method"] == "PositiveExpansion"
                ]
            )
        ),
    }
    (args.out_dir / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
