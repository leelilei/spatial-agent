#!/usr/bin/env python3
"""Real-image P/U diagnostic without adjudicated missing-positive labels.

Official WikiChurches boxes are treated as reliable positives (P). Candidate
regions outside official boxes are treated as unlabeled (U), never as verified
positives or negatives. The probe compares:

* PN: treat U as negative;
* Ignore: omit U and train on official positives/reliable cross-label negatives;
* nnPU: train a non-negative PU logistic head on P and U.

Evaluation uses held-out official positives and hierarchy-incompatible official
boxes. It measures preservation of known-label discrimination, not recovery of
true missing boxes. Because U was selected by a frozen model, SCAR is not
assumed and the nnPU results are explicitly sensitivity diagnostics.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import random
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image, ImageOps
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TOGA_ROOT = Path(
    os.environ.get("TOGA_ROOT", str(PROJECT_ROOT / "vendor" / "TOGA"))
)
sys.path.insert(0, str(TOGA_ROOT))
import clip as openai_clip  # noqa: E402


PROMPTS = (
    "a close-up photo of a {label} on a church",
    "an architectural {label}",
    "a church showing a {label}",
)


def choose_device(requested: str) -> torch.device:
    if requested != "auto":
        return torch.device(requested)
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def normalize_label(label: str) -> str:
    return " ".join(label.lower().replace("-", " ").split())


def ancestor_sets(meta: list[dict[str, object]]) -> dict[str, set[str]]:
    memo: dict[int, set[int]] = {}

    def visit(index: int) -> set[int]:
        if index in memo:
            return memo[index]
        result = {index}
        for parent in meta[index]["parents"]:
            result |= visit(int(parent))
        memo[index] = result
        return result

    return {
        normalize_label(str(item["name"])): {
            normalize_label(str(meta[parent]["name"]))
            for parent in visit(index)
        }
        for index, item in enumerate(meta)
    }


def compatible(a: str, b: str, ancestors: dict[str, set[str]]) -> bool:
    a_norm, b_norm = normalize_label(a), normalize_label(b)
    return (
        a_norm == b_norm
        or b_norm in ancestors.get(a_norm, set())
        or a_norm in ancestors.get(b_norm, set())
    )


def crop_region(
    image: Image.Image,
    region: dict[str, object],
    context: float,
) -> Image.Image:
    width, height = image.size
    left = float(region["left"])
    top = float(region["top"])
    box_width = float(region["width"])
    box_height = float(region["height"])
    x1 = max(0.0, left - box_width * context)
    y1 = max(0.0, top - box_height * context)
    x2 = min(1.0, left + box_width * (1.0 + context))
    y2 = min(1.0, top + box_height * (1.0 + context))
    if x2 <= x1 or y2 <= y1:
        raise ValueError(f"Degenerate crop: {region}")
    return image.crop(
        (
            round(x1 * width),
            round(y1 * height),
            round(x2 * width),
            round(y2 * height),
        )
    )


def encode_regions(
    records: list[dict[str, object]],
    image_dir: Path,
    model: torch.nn.Module,
    preprocess: object,
    device: torch.device,
    batch_size: int,
    context: float,
) -> np.ndarray:
    images: dict[str, Image.Image] = {}
    crops: list[Image.Image] = []
    for record in records:
        filename = str(record["image_filename"])
        if filename not in images:
            images[filename] = ImageOps.exif_transpose(
                Image.open(image_dir / filename)
            ).convert("RGB")
        crops.append(crop_region(images[filename], record, context))

    batches: list[torch.Tensor] = []
    with torch.inference_mode():
        for start in range(0, len(crops), batch_size):
            batch = torch.stack(
                [
                    preprocess(image)
                    for image in crops[start : start + batch_size]
                ]
            ).to(device)
            encoded = model.encode_image(batch)
            encoded = encoded / encoded.norm(dim=-1, keepdim=True)
            batches.append(encoded.float().cpu())
    return torch.cat(batches).numpy()


def encode_label_features(
    model: torch.nn.Module,
    labels: list[str],
    device: torch.device,
) -> np.ndarray:
    encoded_labels: list[torch.Tensor] = []
    with torch.inference_mode():
        for label in labels:
            tokens = openai_clip.tokenize(
                [prompt.format(label=label.lower()) for prompt in PROMPTS]
            ).to(device)
            encoded = model.encode_text(tokens)
            encoded = encoded / encoded.norm(dim=-1, keepdim=True)
            mean = encoded.mean(dim=0)
            encoded_labels.append((mean / mean.norm()).float().cpu())
    return torch.stack(encoded_labels).numpy()


def build_selection_covariates(
    records: list[dict[str, object]],
    features: np.ndarray,
    label_features: np.ndarray,
    label_index: dict[str, int],
) -> np.ndarray:
    covariates: list[list[float]] = []
    for record, feature in zip(records, features):
        width = max(float(record["width"]), 1e-6)
        height = max(float(record["height"]), 1e-6)
        center_x = float(record["left"]) + width / 2
        center_y = float(record["top"]) + height / 2
        target = label_features[label_index[str(record["label"])]]
        covariates.append(
            [
                float(feature @ target),
                float(np.log(width * height)),
                float(np.log(width / height)),
                center_x,
                center_y,
            ]
        )
    return np.asarray(covariates, dtype=np.float64)


def propensity_weights(
    covariates: np.ndarray,
    positives: list[int],
    unlabeled: list[int],
    floor: float,
    seed: int,
) -> tuple[np.ndarray, np.ndarray]:
    indices = positives + unlabeled
    labels = np.asarray([1] * len(positives) + [0] * len(unlabeled))
    train_x = covariates[indices]
    mean = train_x.mean(axis=0)
    scale = train_x.std(axis=0)
    scale[scale < 1e-8] = 1.0
    standardized = (train_x - mean) / scale
    classifier = LogisticRegression(
        C=0.25,
        class_weight="balanced",
        max_iter=2000,
        random_state=seed,
    )
    classifier.fit(standardized, labels)
    positive_standardized = (covariates[positives] - mean) / scale
    raw_propensity = classifier.predict_proba(positive_standardized)[:, 1]
    clipped = np.clip(raw_propensity, floor, 0.95)
    weights = 1.0 / clipped
    weights = weights / weights.mean()
    return weights.astype(np.float32), raw_propensity


def fit_supervised(
    features: np.ndarray,
    positives: list[int],
    negatives: list[int],
    seed: int,
) -> LogisticRegression:
    indices = positives + negatives
    labels = np.asarray([1] * len(positives) + [0] * len(negatives))
    classifier = LogisticRegression(
        C=1.0,
        class_weight="balanced",
        max_iter=2000,
        random_state=seed,
    )
    classifier.fit(features[indices], labels)
    return classifier


def fit_nnpu(
    features: np.ndarray,
    positives: list[int],
    unlabeled: list[int],
    class_prior: float,
    seed: int,
    epochs: int,
    learning_rate: float,
    weight_decay: float,
    device: torch.device,
    positive_weights: np.ndarray | None = None,
    unlabeled_weights: np.ndarray | None = None,
) -> torch.nn.Linear:
    torch.manual_seed(seed)
    positive_x = torch.from_numpy(features[positives]).float().to(device)
    unlabeled_x = torch.from_numpy(features[unlabeled]).float().to(device)
    if positive_weights is None:
        positive_weight_tensor = torch.ones(
            len(positives), dtype=torch.float32, device=device
        )
    else:
        positive_weight_tensor = torch.from_numpy(
            positive_weights
        ).float().to(device)
    positive_weight_tensor = (
        positive_weight_tensor / positive_weight_tensor.mean()
    )
    if unlabeled_weights is None:
        unlabeled_weight_tensor = torch.ones(
            len(unlabeled), dtype=torch.float32, device=device
        )
    else:
        unlabeled_weight_tensor = torch.from_numpy(
            unlabeled_weights
        ).float().to(device)
    unlabeled_weight_tensor = (
        unlabeled_weight_tensor / unlabeled_weight_tensor.mean()
    )
    head = torch.nn.Linear(features.shape[1], 1).to(device)
    torch.nn.init.zeros_(head.weight)
    torch.nn.init.zeros_(head.bias)
    optimizer = torch.optim.AdamW(
        head.parameters(),
        lr=learning_rate,
        weight_decay=weight_decay,
    )

    for _ in range(epochs):
        positive_logits = head(positive_x).squeeze(1)
        unlabeled_logits = head(unlabeled_x).squeeze(1)
        positive_risk = class_prior * (
            positive_weight_tensor * F.softplus(-positive_logits)
        ).mean()
        negative_risk = (
            (
                unlabeled_weight_tensor * F.softplus(unlabeled_logits)
            ).mean()
            - class_prior
            * (
                positive_weight_tensor * F.softplus(positive_logits)
            ).mean()
        )
        if negative_risk.detach().item() < 0:
            risk = -negative_risk
        else:
            risk = positive_risk + negative_risk
        optimizer.zero_grad(set_to_none=True)
        risk.backward()
        optimizer.step()
    return head.cpu()


def predict_scores(
    model: LogisticRegression | torch.nn.Linear,
    features: np.ndarray,
    indices: list[int],
) -> np.ndarray:
    if isinstance(model, LogisticRegression):
        return model.predict_proba(features[indices])[:, 1]
    with torch.inference_mode():
        logits = model(torch.from_numpy(features[indices]).float()).squeeze(1)
        return torch.sigmoid(logits).numpy()


def bootstrap_mean_ci(
    values: list[float],
    seed: int,
    replicates: int = 5000,
) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    array = np.asarray(values, dtype=float)
    sampled = rng.integers(0, len(array), size=(replicates, len(array)))
    means = array[sampled].mean(axis=1)
    return float(np.quantile(means, 0.025)), float(np.quantile(means, 0.975))


def label_means(
    rows: list[dict[str, object]],
    labels: list[str],
    field: str,
) -> list[float]:
    return [
        float(
            np.mean(
                [
                    float(row[field])
                    for row in rows
                    if row["label"] == label
                ]
            )
        )
        for label in labels
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--parts", type=Path, required=True)
    parser.add_argument("--official-boxes", type=Path, required=True)
    parser.add_argument("--unlabeled-candidates", type=Path, required=True)
    parser.add_argument("--image-dir", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--model", default="ViT-B/16")
    parser.add_argument("--device", default="auto")
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--context", type=float, default=0.1)
    parser.add_argument("--min-positive-count", type=int, default=8)
    parser.add_argument("--min-unlabeled-count", type=int, default=12)
    parser.add_argument("--repeats", type=int, default=30)
    parser.add_argument("--eval-positive-images", type=int, default=2)
    parser.add_argument("--eval-negative-images", type=int, default=5)
    parser.add_argument("--seed", type=int, default=20260726)
    parser.add_argument(
        "--class-priors",
        type=float,
        nargs="+",
        default=[0.10, 0.25, 0.50],
    )
    parser.add_argument("--nnpu-epochs", type=int, default=250)
    parser.add_argument("--nnpu-lr", type=float, default=0.05)
    parser.add_argument("--nnpu-weight-decay", type=float, default=1e-4)
    parser.add_argument("--selection-prior", type=float, default=0.25)
    parser.add_argument(
        "--propensity-floors",
        type=float,
        nargs="+",
        default=[0.10, 0.20],
    )
    args = parser.parse_args()

    if any(prior <= 0 or prior >= 1 for prior in args.class_priors):
        raise ValueError("Every class prior must lie strictly between 0 and 1")
    if args.selection_prior <= 0 or args.selection_prior >= 1:
        raise ValueError("Selection-aware class prior must be in (0, 1)")
    if any(floor <= 0 or floor >= 1 for floor in args.propensity_floors):
        raise ValueError("Every propensity floor must lie in (0, 1)")

    manifest_rows = list(csv.DictReader(args.manifest.open()))
    filenames = sorted({row["image_filename"] for row in manifest_rows})
    filename_set = set(filenames)
    payload = json.loads(args.parts.read_text())
    ancestors = ancestor_sets(payload["meta"])

    official = [
        {**row, "source": "official"}
        for row in csv.DictReader(args.official_boxes.open())
        if row["image_filename"] in filename_set
    ]
    unlabeled = [
        {**row, "source": "unlabeled"}
        for row in csv.DictReader(args.unlabeled_candidates.open())
        if row["image_filename"] in filename_set
    ]
    records = official + unlabeled
    for index, record in enumerate(records):
        record["feature_index"] = index

    positive_counts = Counter(str(row["label"]) for row in official)
    unlabeled_counts = Counter(str(row["label"]) for row in unlabeled)
    labels = sorted(
        label
        for label, count in positive_counts.items()
        if count >= args.min_positive_count
        and unlabeled_counts[label] >= args.min_unlabeled_count
    )
    if not labels:
        raise ValueError("No label satisfies the P/U count thresholds")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    device = choose_device(args.device)
    print(
        f"device={device} model={args.model} official={len(official)} "
        f"unlabeled={len(unlabeled)} labels={len(labels)}",
        flush=True,
    )
    model, preprocess = openai_clip.load(args.model, device=device)
    model.eval()
    features = encode_regions(
        records,
        args.image_dir,
        model,
        preprocess,
        device,
        args.batch_size,
        args.context,
    )
    record_labels = sorted({str(record["label"]) for record in records})
    label_feature_array = encode_label_features(
        model, record_labels, device
    )
    selection_covariates = build_selection_covariates(
        records,
        features,
        label_feature_array,
        {label: index for index, label in enumerate(record_labels)},
    )

    methods = ["PN", "Ignore"] + [
        f"nnPU(pi={prior:.2f})" for prior in args.class_priors
    ] + [
        (
            f"SA-nnPU(pi={args.selection_prior:.2f},"
            f"e>={floor:.2f})"
        )
        for floor in args.propensity_floors
    ]
    results: list[dict[str, object]] = []

    for label in labels:
        label_positive_rows = [
            row for row in official if row["label"] == label
        ]
        positive_images = sorted(
            {str(row["image_filename"]) for row in label_positive_rows}
        )
        nonpositive_images = sorted(filename_set - set(positive_images))
        if len(positive_images) <= args.eval_positive_images:
            continue

        for repeat in range(args.repeats):
            split_seed = (
                args.seed + repeat * 1009 + sum(map(ord, normalize_label(label)))
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
                and not compatible(label, str(row["label"]), ancestors)
            ]
            eval_negative = [
                int(row["feature_index"])
                for row in official
                if row["image_filename"] in eval_images
                and not compatible(label, str(row["label"]), ancestors)
            ]
            train_unlabeled = [
                int(row["feature_index"])
                for row in unlabeled
                if row["label"] == label
                and row["image_filename"] not in eval_images
            ]
            if (
                len(train_positive) < 4
                or len(eval_positive) < 2
                or len(train_negative) < 8
                or len(eval_negative) < 5
                or len(train_unlabeled) < 8
            ):
                continue

            rng.shuffle(train_negative)
            negative_cap = min(
                len(train_negative),
                max(24, 6 * len(train_positive)),
            )
            train_negative = train_negative[:negative_cap]
            eval_indices = eval_positive + eval_negative
            eval_y = np.asarray(
                [1] * len(eval_positive) + [0] * len(eval_negative)
            )

            fitted: dict[str, LogisticRegression | torch.nn.Linear] = {
                "PN": fit_supervised(
                    features,
                    train_positive,
                    train_negative + train_unlabeled,
                    split_seed,
                ),
                "Ignore": fit_supervised(
                    features,
                    train_positive,
                    train_negative,
                    split_seed,
                ),
            }
            for prior in args.class_priors:
                fitted[f"nnPU(pi={prior:.2f})"] = fit_nnpu(
                    features,
                    train_positive,
                    train_unlabeled,
                    prior,
                    split_seed,
                    args.nnpu_epochs,
                    args.nnpu_lr,
                    args.nnpu_weight_decay,
                    device,
                )
            diagnostics: dict[str, dict[str, float]] = {
                method: {
                    "propensity_floor": float("nan"),
                    "propensity_min": float("nan"),
                    "propensity_median": float("nan"),
                    "propensity_max": float("nan"),
                    "positive_weight_ess": float("nan"),
                }
                for method in fitted
            }
            for floor in args.propensity_floors:
                weights, raw_propensity = propensity_weights(
                    selection_covariates,
                    train_positive,
                    train_unlabeled,
                    floor,
                    split_seed,
                )
                method = (
                    f"SA-nnPU(pi={args.selection_prior:.2f},"
                    f"e>={floor:.2f})"
                )
                fitted[method] = fit_nnpu(
                    features,
                    train_positive,
                    train_unlabeled,
                    args.selection_prior,
                    split_seed,
                    args.nnpu_epochs,
                    args.nnpu_lr,
                    args.nnpu_weight_decay,
                    device,
                    positive_weights=weights,
                )
                diagnostics[method] = {
                    "propensity_floor": floor,
                    "propensity_min": float(raw_propensity.min()),
                    "propensity_median": float(
                        np.median(raw_propensity)
                    ),
                    "propensity_max": float(raw_propensity.max()),
                    "positive_weight_ess": float(
                        weights.sum() ** 2 / (weights**2).sum()
                    ),
                }

            for method, fitted_model in fitted.items():
                eval_scores = predict_scores(
                    fitted_model, features, eval_indices
                )
                unlabeled_scores = predict_scores(
                    fitted_model, features, train_unlabeled
                )
                reliable_negative_scores = predict_scores(
                    fitted_model, features, train_negative
                )
                threshold = float(
                    np.quantile(reliable_negative_scores, 0.95)
                )
                results.append(
                    {
                        "label": label,
                        "repeat": repeat,
                        "method": method,
                        "split_seed": split_seed,
                        "positive_count": positive_counts[label],
                        "unlabeled_count": unlabeled_counts[label],
                        "train_positive": len(train_positive),
                        "train_reliable_negative": len(train_negative),
                        "train_unlabeled": len(train_unlabeled),
                        "eval_positive": len(eval_positive),
                        "eval_reliable_negative": len(eval_negative),
                        "roc_auc": roc_auc_score(eval_y, eval_scores),
                        "average_precision": average_precision_score(
                            eval_y, eval_scores
                        ),
                        "eval_positive_mean_score": float(
                            eval_scores[: len(eval_positive)].mean()
                        ),
                        "unlabeled_mean_score": float(
                            unlabeled_scores.mean()
                        ),
                        "unlabeled_above_rn95_rate": float(
                            (unlabeled_scores > threshold).mean()
                        ),
                        **diagnostics[method],
                    }
                )
        completed = sum(1 for row in results if row["label"] == label)
        print(
            f"{label}: P={positive_counts[label]} U={unlabeled_counts[label]} "
            f"result_rows={completed}",
            flush=True,
        )

    if not results:
        raise RuntimeError("No complete P/U split was produced")

    result_path = args.out_dir / "per_split_results.csv"
    with result_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(results[0]))
        writer.writeheader()
        writer.writerows(results)

    completed_labels = sorted({str(row["label"]) for row in results})
    report = [
        "# Real P/U diagnostic without adjudication",
        "",
        "## Protocol boundary",
        "",
        "- P: official WikiChurches element boxes;",
        "- U: real candidate regions outside official boxes;",
        "- reliable N: hierarchy-incompatible official boxes;",
        "- evaluation: held-out official P versus held-out reliable N;",
        "- Oracle: unavailable because both annotation CSV files are empty;",
        "- nnPU is a prior-sensitivity diagnostic; candidate selection violates "
        "the usual SCAR assumption.",
        "- SA-nnPU uses a propensity proxy fitted from target similarity, "
        "box area/aspect, and position; deterministic top-k selection means "
        "the true propensity is not identified.",
        "",
        f"- Frozen encoder: OpenAI CLIP `{args.model}`",
        f"- Images: {len(filenames)}",
        f"- Official boxes: {len(official)}",
        f"- Unlabeled candidate boxes: {len(unlabeled)}",
        f"- Labels: {len(completed_labels)}",
        f"- Repeats: {args.repeats} / label",
        f"- Primary PU prior: 0.25; sensitivity priors: "
        f"{', '.join(f'{value:.2f}' for value in args.class_priors)}",
        f"- Selection-aware prior: {args.selection_prior:.2f}; "
        f"propensity floors: "
        f"{', '.join(f'{value:.2f}' for value in args.propensity_floors)}",
        "",
        "## Held-out known-label performance",
        "",
        "| Method | ROC-AUC | 95% CI | AP | 95% CI | "
        "P score | U score | U > RN95 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for method in methods:
        method_rows = [
            row for row in results if row["method"] == method
        ]
        auc_by_label = label_means(
            method_rows, completed_labels, "roc_auc"
        )
        ap_by_label = label_means(
            method_rows, completed_labels, "average_precision"
        )
        auc_ci = bootstrap_mean_ci(auc_by_label, args.seed)
        ap_ci = bootstrap_mean_ci(ap_by_label, args.seed + 1)
        report.append(
            f"| {method} | {np.mean(auc_by_label):.3f} | "
            f"{auc_ci[0]:.3f}–{auc_ci[1]:.3f} | "
            f"{np.mean(ap_by_label):.3f} | "
            f"{ap_ci[0]:.3f}–{ap_ci[1]:.3f} | "
            f"{np.mean(label_means(method_rows, completed_labels, 'eval_positive_mean_score')):.3f} | "
            f"{np.mean(label_means(method_rows, completed_labels, 'unlabeled_mean_score')):.3f} | "
            f"{np.mean(label_means(method_rows, completed_labels, 'unlabeled_above_rn95_rate')):.3f} |"
        )

    report.extend(
        [
            "",
            "## Selection-proxy diagnostics",
            "",
            "| Method | raw e min | raw e median | raw e max | positive ESS |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    selection_methods = [
        method for method in methods if method.startswith("SA-nnPU")
    ]
    for method in selection_methods:
        method_rows = [
            row for row in results if row["method"] == method
        ]
        report.append(
            f"| {method} | "
            f"{np.mean([float(row['propensity_min']) for row in method_rows]):.3f} | "
            f"{np.mean([float(row['propensity_median']) for row in method_rows]):.3f} | "
            f"{np.mean([float(row['propensity_max']) for row in method_rows]):.3f} | "
            f"{np.mean([float(row['positive_weight_ess']) for row in method_rows]):.2f} |"
        )

    report.extend(
        [
            "",
            "## Paired differences",
            "",
            "| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    primary_method = f"nnPU(pi={args.selection_prior:.2f})"
    indexed = {
        (str(row["label"]), int(row["repeat"]), str(row["method"])): row
        for row in results
    }
    comparisons = [
        (primary_method, "PN"),
        (primary_method, "Ignore"),
    ]
    for selection_method in selection_methods:
        comparisons.extend(
            [
                (selection_method, primary_method),
                (selection_method, "PN"),
                (selection_method, "Ignore"),
            ]
        )
    for left_method, right_method in comparisons:
        auc_deltas: list[float] = []
        ap_deltas: list[float] = []
        for label in completed_labels:
            label_auc: list[float] = []
            label_ap: list[float] = []
            for repeat in range(args.repeats):
                left = indexed.get((label, repeat, left_method))
                right = indexed.get((label, repeat, right_method))
                if left is None or right is None:
                    continue
                label_auc.append(
                    float(left["roc_auc"]) - float(right["roc_auc"])
                )
                label_ap.append(
                    float(left["average_precision"])
                    - float(right["average_precision"])
                )
            if label_auc:
                auc_deltas.append(float(np.mean(label_auc)))
                ap_deltas.append(float(np.mean(label_ap)))
        auc_ci = bootstrap_mean_ci(auc_deltas, args.seed + 2)
        ap_ci = bootstrap_mean_ci(ap_deltas, args.seed + 3)
        report.append(
            f"| {left_method} − {right_method} | "
            f"{np.mean(auc_deltas):+.3f} | "
            f"{auc_ci[0]:+.3f}–{auc_ci[1]:+.3f} | "
            f"{np.mean(ap_deltas):+.3f} | "
            f"{ap_ci[0]:+.3f}–{ap_ci[1]:+.3f} |"
        )

    report.extend(
        [
            "",
            "## Interpretation limit",
            "",
            "`U > RN95` is a recovery-candidate rate, not precision: U has no "
            "human truth. The held-out metrics only test known official labels. "
            "SA-nnPU uses an annotation-selection proxy, not an identified "
            "causal propensity. "
            "This experiment can reject an unstable P/U formulation, but it "
            "cannot estimate the real missing-positive rate or an Oracle gap.",
        ]
    )
    (args.out_dir / "real_pu_report.md").write_text(
        "\n".join(report) + "\n"
    )


if __name__ == "__main__":
    main()
