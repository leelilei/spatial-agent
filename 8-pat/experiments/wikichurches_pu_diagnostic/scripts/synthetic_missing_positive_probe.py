#!/usr/bin/env python3
"""Controlled PN/Ignore/Oracle probe on frozen-CLIP official-box features.

For sufficiently frequent leaf labels, a fraction of official positives is
artificially hidden. PN relabels them as negatives, Ignore omits them, and
Oracle retains their positive labels. All methods share the same frozen CLIP
features and logistic-regression classifier.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import torch
from PIL import Image, ImageOps
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "vendor" / "TOGA"))
import clip as openai_clip  # noqa: E402


def choose_device(requested: str) -> torch.device:
    if requested != "auto":
        return torch.device(requested)
    if torch.backends.mps.is_available():
        return torch.device("mps")
    if torch.cuda.is_available():
        return torch.device("cuda")
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
            result |= visit(parent)
        memo[index] = result
        return result

    return {
        normalize_label(item["name"]): {
            normalize_label(meta[parent]["name"]) for parent in visit(index)
        }
        for index, item in enumerate(meta)
    }


def compatible(a: str, b: str, ancestors: dict[str, set[str]]) -> bool:
    a, b = normalize_label(a), normalize_label(b)
    return a == b or b in ancestors.get(a, set()) or a in ancestors.get(b, set())


def crop(
    image: Image.Image,
    element: dict[str, float],
    context: float,
) -> Image.Image:
    width, height = image.size
    x1, y1 = element["left"], element["top"]
    x2 = x1 + element["width"]
    y2 = y1 + element["height"]
    dx, dy = element["width"] * context, element["height"] * context
    return image.crop(
        (
            round(max(0, x1 - dx) * width),
            round(max(0, y1 - dy) * height),
            round(min(1, x2 + dx) * width),
            round(min(1, y2 + dy) * height),
        )
    )


def bootstrap_mean_ci(
    values: list[float],
    seed: int,
    replicates: int = 5000,
) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    array = np.asarray(values)
    indices = rng.integers(0, len(array), size=(replicates, len(array)))
    means = array[indices].mean(axis=1)
    return float(np.quantile(means, 0.025)), float(np.quantile(means, 0.975))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--parts", type=Path, required=True)
    parser.add_argument("--image-dir", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--model", default="ViT-B/32")
    parser.add_argument("--device", default="auto")
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--min-label-count", type=int, default=8)
    parser.add_argument("--missing-rate", type=float, default=0.25)
    parser.add_argument("--repeats", type=int, default=100)
    parser.add_argument("--seed", type=int, default=20260725)
    args = parser.parse_args()

    rows = list(csv.DictReader(args.manifest.open()))
    filenames = {row["image_filename"] for row in rows}
    payload = json.loads(args.parts.read_text())
    meta = payload["meta"]
    annotations = payload["annotations"]
    ancestors = ancestor_sets(meta)
    args.out_dir.mkdir(parents=True, exist_ok=True)

    records: list[dict[str, object]] = []
    crops: list[Image.Image] = []
    for filename in sorted(filenames):
        image = ImageOps.exif_transpose(
            Image.open(args.image_dir / filename)
        ).convert("RGB")
        for group in annotations[filename]["bbox_groups"]:
            for element in group["elements"]:
                label = meta[element["label"]]["name"]
                records.append({"image_filename": filename, "label": label})
                crops.append(crop(image, element, context=0.1))

    device = choose_device(args.device)
    print(f"device={device} model={args.model}", flush=True)
    model, preprocess = openai_clip.load(args.model, device=device)
    model.eval()
    feature_batches: list[torch.Tensor] = []
    with torch.inference_mode():
        for start in range(0, len(crops), args.batch_size):
            batch = torch.stack(
                [preprocess(image) for image in crops[start : start + args.batch_size]]
            ).to(device)
            features = model.encode_image(batch)
            features = features / features.norm(dim=-1, keepdim=True)
            feature_batches.append(features.cpu())
    features = torch.cat(feature_batches).float().numpy()

    counts = Counter(str(record["label"]) for record in records)
    labels = sorted(
        label for label, count in counts.items() if count >= args.min_label_count
    )
    all_results: list[dict[str, object]] = []
    methods = ("PN", "Ignore", "Oracle")

    for label in labels:
        positive_indices = [
            index for index, record in enumerate(records)
            if record["label"] == label
        ]
        negative_indices = [
            index for index, record in enumerate(records)
            if not compatible(label, str(record["label"]), ancestors)
        ]
        for repeat in range(args.repeats):
            rng = random.Random(args.seed + repeat * 1009 + sum(map(ord, label)))
            positives = positive_indices[:]
            negatives = negative_indices[:]
            rng.shuffle(positives)
            rng.shuffle(negatives)

            contam_n = max(1, round(len(positives) * args.missing_rate))
            eval_pos_n = max(2, round(len(positives) * args.missing_rate))
            if contam_n + eval_pos_n >= len(positives):
                contam_n, eval_pos_n = 1, 2
            contaminated = positives[:contam_n]
            eval_pos = positives[contam_n : contam_n + eval_pos_n]
            train_pos = positives[contam_n + eval_pos_n :]
            if len(train_pos) < 3:
                continue

            train_neg_n = min(len(negatives) // 2, max(12, 4 * len(train_pos)))
            eval_neg_n = min(
                len(negatives) - train_neg_n,
                max(10, 5 * len(eval_pos)),
            )
            train_neg = negatives[:train_neg_n]
            eval_neg = negatives[train_neg_n : train_neg_n + eval_neg_n]
            eval_indices = eval_pos + eval_neg
            eval_y = np.asarray([1] * len(eval_pos) + [0] * len(eval_neg))

            for method in methods:
                method_pos = train_pos[:]
                method_neg = train_neg[:]
                if method == "PN":
                    method_neg += contaminated
                elif method == "Oracle":
                    method_pos += contaminated

                train_indices = method_pos + method_neg
                train_y = np.asarray(
                    [1] * len(method_pos) + [0] * len(method_neg)
                )
                classifier = LogisticRegression(
                    C=1.0,
                    class_weight="balanced",
                    max_iter=1000,
                    random_state=args.seed + repeat,
                )
                classifier.fit(features[train_indices], train_y)
                scores = classifier.predict_proba(features[eval_indices])[:, 1]
                all_results.append(
                    {
                        "label": label,
                        "repeat": repeat,
                        "method": method,
                        "positive_count": len(positive_indices),
                        "train_positive": len(method_pos),
                        "train_negative": len(method_neg),
                        "contaminated_positive": len(contaminated),
                        "eval_positive": len(eval_pos),
                        "eval_negative": len(eval_neg),
                        "roc_auc": roc_auc_score(eval_y, scores),
                        "average_precision": average_precision_score(eval_y, scores),
                        "eval_positive_mean_score": float(
                            scores[: len(eval_pos)].mean()
                        ),
                    }
                )
        print(f"{label}: n={len(positive_indices)}", flush=True)

    result_path = args.out_dir / "per_split_results.csv"
    with result_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(all_results[0]))
        writer.writeheader()
        writer.writerows(all_results)

    grouped: dict[tuple[str, int], dict[str, dict[str, object]]] = {}
    for result in all_results:
        grouped.setdefault((str(result["label"]), int(result["repeat"])), {})[
            str(result["method"])
        ] = result
    complete_groups = [group for group in grouped.values() if len(group) == 3]

    report = [
        "# Controlled missing-positive linear probe",
        "",
        f"- Frozen encoder：OpenAI CLIP `{args.model}`",
        f"- 图像：{len(filenames)}；官方框：{len(records)}",
        f"- 标签：{len(labels)}（每标签至少 {args.min_label_count} 个正框）",
        f"- 人工缺失率：{100 * args.missing_rate:.0f}%",
        f"- 重复：{args.repeats} / 标签",
        "- 置信区间：先在每个标签内对重复取均值，再对 9 个标签做 paired bootstrap",
        "",
        "| 方法 | ROC-AUC | 95% CI | AP | 95% CI | 正例均分 |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for method in methods:
        method_rows = [
            row for row in all_results if row["method"] == method
        ]
        aucs = [float(row["roc_auc"]) for row in method_rows]
        aps = [float(row["average_precision"]) for row in method_rows]
        scores = [float(row["eval_positive_mean_score"]) for row in method_rows]
        label_auc_means = [
            float(
                np.mean(
                    [
                        float(row["roc_auc"])
                        for row in method_rows
                        if row["label"] == label
                    ]
                )
            )
            for label in labels
        ]
        label_ap_means = [
            float(
                np.mean(
                    [
                        float(row["average_precision"])
                        for row in method_rows
                        if row["label"] == label
                    ]
                )
            )
            for label in labels
        ]
        auc_ci = bootstrap_mean_ci(label_auc_means, args.seed)
        ap_ci = bootstrap_mean_ci(label_ap_means, args.seed + 1)
        report.append(
            f"| {method} | {np.mean(aucs):.3f} | "
            f"{auc_ci[0]:.3f}–{auc_ci[1]:.3f} | "
            f"{np.mean(aps):.3f} | {ap_ci[0]:.3f}–{ap_ci[1]:.3f} | "
            f"{np.mean(scores):.3f} |"
        )

    report.extend(
        [
            "",
            "## Paired differences",
            "",
            "| 对比 | ΔROC-AUC | 95% CI | ΔAP | 95% CI |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for left, right in (("PN", "Ignore"), ("Oracle", "Ignore"), ("Oracle", "PN")):
        auc_delta_all = [
            (
                str(group[left]["label"]),
                float(group[left]["roc_auc"]) - float(group[right]["roc_auc"]),
            )
            for group in complete_groups
        ]
        ap_delta_all = [
            (
                str(group[left]["label"]),
                float(group[left]["average_precision"])
                - float(group[right]["average_precision"]),
            )
            for group in complete_groups
        ]
        auc_delta = [
            float(np.mean([value for item_label, value in auc_delta_all if item_label == label]))
            for label in labels
        ]
        ap_delta = [
            float(np.mean([value for item_label, value in ap_delta_all if item_label == label]))
            for label in labels
        ]
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
            "该实验仅隔离“把已知正框错标为负例”的损害。它不估计真实漏标率，"
            "也不等价于在完整 TOGA 图教师中实现 PU 风险。",
        ]
    )
    (args.out_dir / "synthetic_probe_report.md").write_text(
        "\n".join(report) + "\n"
    )


if __name__ == "__main__":
    main()
