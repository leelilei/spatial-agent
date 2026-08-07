#!/usr/bin/env python3
"""Rank box-external regions for manual review with frozen CLIP.

This is a prioritization diagnostic, not ground truth and not evidence of
missing positives by itself.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import sys
from collections import Counter
from pathlib import Path

import torch
from PIL import Image, ImageDraw, ImageFont, ImageOps

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


def overlap_fraction(
    box: tuple[float, float, float, float],
    official: tuple[float, float, float, float],
) -> float:
    x1, y1, x2, y2 = box
    ox1, oy1, ox2, oy2 = official
    intersection = max(0.0, min(x2, ox2) - max(x1, ox1)) * max(
        0.0, min(y2, oy2) - max(y1, oy1)
    )
    area = max(1e-12, (x2 - x1) * (y2 - y1))
    return intersection / area


def grid_boxes() -> list[tuple[float, float, float, float]]:
    specs = [
        (0.12, 1.0, 6),
        (0.20, 1.0, 6),
        (0.32, 1.0, 5),
        (0.22, 0.5, 5),
        (0.22, 2.0, 5),
    ]
    boxes: list[tuple[float, float, float, float]] = []
    for scale, aspect, grid in specs:
        width = min(0.9, scale * math.sqrt(aspect))
        height = min(0.9, scale / math.sqrt(aspect))
        for yi in range(grid):
            cy = height / 2 + yi * (1 - height) / max(1, grid - 1)
            for xi in range(grid):
                cx = width / 2 + xi * (1 - width) / max(1, grid - 1)
                boxes.append(
                    (
                        cx - width / 2,
                        cy - height / 2,
                        cx + width / 2,
                        cy + height / 2,
                    )
                )
    return boxes


def poisson_inclusion_probabilities(
    scores: torch.Tensor,
    expected_count: float,
    temperature: float,
    minimum_probability: float,
    maximum_probability: float,
) -> torch.Tensor:
    """Construct independent Bernoulli probabilities with a fixed expected size."""
    count = len(scores)
    if not 0 < minimum_probability < maximum_probability < 1:
        raise ValueError("Probability bounds must satisfy 0 < min < max < 1")
    if not count * minimum_probability < expected_count < count * maximum_probability:
        raise ValueError(
            "Expected sample count is incompatible with probability bounds"
        )
    weights = torch.exp((scores - scores.max()) / temperature).double()

    def probabilities(scale: float) -> torch.Tensor:
        return torch.clamp(
            minimum_probability + scale * weights,
            max=maximum_probability,
        )

    low, high = 0.0, 1.0
    while float(probabilities(high).sum()) < expected_count:
        high *= 2
    for _ in range(80):
        middle = (low + high) / 2
        if float(probabilities(middle).sum()) < expected_count:
            low = middle
        else:
            high = middle
    result = probabilities(high)
    if abs(float(result.sum()) - expected_count) > 1e-6:
        raise RuntimeError("Failed to calibrate Bernoulli inclusion probabilities")
    return result.float()


def crop_box(
    image: Image.Image,
    box: tuple[float, float, float, float],
    context: float = 0.0,
) -> Image.Image:
    width, height = image.size
    x1, y1, x2, y2 = box
    dx, dy = (x2 - x1) * context, (y2 - y1) * context
    return image.crop(
        (
            round(max(0, x1 - dx) * width),
            round(max(0, y1 - dy) * height),
            round(min(1, x2 + dx) * width),
            round(min(1, y2 + dy) * height),
        )
    )


def encode_images(
    model: torch.nn.Module,
    preprocess,
    images: list[Image.Image],
    device: torch.device,
    batch_size: int,
) -> torch.Tensor:
    features: list[torch.Tensor] = []
    with torch.inference_mode():
        for start in range(0, len(images), batch_size):
            batch = torch.stack(
                [preprocess(image) for image in images[start : start + batch_size]]
            ).to(device)
            encoded = model.encode_image(batch)
            encoded = encoded / encoded.norm(dim=-1, keepdim=True)
            features.append(encoded.cpu())
    return torch.cat(features)


def encode_labels(
    model: torch.nn.Module,
    tokenizer,
    labels: list[str],
    device: torch.device,
) -> torch.Tensor:
    per_label: list[torch.Tensor] = []
    with torch.inference_mode():
        for label in labels:
            tokens = tokenizer(
                [prompt.format(label=label.lower()) for prompt in PROMPTS]
            ).to(device)
            encoded = model.encode_text(tokens)
            encoded = encoded / encoded.norm(dim=-1, keepdim=True)
            mean = encoded.mean(dim=0)
            per_label.append((mean / mean.norm()).cpu())
    return torch.stack(per_label)


def choose_device(requested: str) -> torch.device:
    if requested != "auto":
        return torch.device(requested)
    if torch.backends.mps.is_available():
        return torch.device("mps")
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--parts", type=Path, required=True)
    parser.add_argument("--image-dir", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--model", default="ViT-B/32")
    parser.add_argument("--device", default="auto")
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--max-official-overlap", type=float, default=0.05)
    parser.add_argument("--full-pool-csv", type=Path)
    parser.add_argument("--sampling-seed", type=int, default=20260726)
    parser.add_argument("--expected-samples-per-group", type=float, default=3.0)
    parser.add_argument("--sampling-temperature", type=float, default=0.05)
    parser.add_argument("--minimum-inclusion-probability", type=float, default=0.01)
    parser.add_argument("--maximum-inclusion-probability", type=float, default=0.80)
    args = parser.parse_args()

    device = choose_device(args.device)
    print(f"device={device} model={args.model} pretrained=openai", flush=True)
    model, preprocess = openai_clip.load(args.model, device=device)
    model.eval()
    tokenizer = openai_clip.tokenize

    rows = list(csv.DictReader(args.manifest.open()))
    payload = json.loads(args.parts.read_text())
    meta = payload["meta"]
    official_payload = payload["annotations"]
    selected_filenames = {row["image_filename"] for row in rows}
    global_labels = sorted(
        {
            meta[element["label"]]["name"]
            for filename in selected_filenames
            for group in official_payload[filename]["bbox_groups"]
            for element in group["elements"]
        }
    )
    global_label_index = {
        label: index for index, label in enumerate(global_labels)
    }
    global_text_features = encode_labels(
        model,
        tokenizer,
        global_labels,
        device,
    )
    args.out_dir.mkdir(parents=True, exist_ok=True)
    overlay_dir = args.out_dir / "candidate_overlays"
    overlay_dir.mkdir(parents=True, exist_ok=True)
    candidate_grid = grid_boxes()
    output_rows: list[dict[str, object]] = []
    full_pool_rows: list[dict[str, object]] = []
    image_has_above_positive = Counter()
    font = ImageFont.load_default(size=18)
    sampling_generator = torch.Generator().manual_seed(args.sampling_seed)

    for image_index, row in enumerate(rows, start=1):
        filename = row["image_filename"]
        image = ImageOps.exif_transpose(
            Image.open(args.image_dir / filename)
        ).convert("RGB")
        official_by_label: dict[str, list[tuple[float, float, float, float]]] = {}
        all_official: list[tuple[float, float, float, float]] = []
        for group in official_payload[filename]["bbox_groups"]:
            for element in group["elements"]:
                label = meta[element["label"]]["name"]
                box = (
                    element["left"],
                    element["top"],
                    element["left"] + element["width"],
                    element["top"] + element["height"],
                )
                official_by_label.setdefault(label, []).append(box)
                all_official.append(box)

        external_grid = [
            box
            for box in candidate_grid
            if max(overlap_fraction(box, official) for official in all_official)
            <= args.max_official_overlap
        ]
        labels = sorted(official_by_label)
        text_features = encode_labels(model, tokenizer, labels, device)
        candidate_features = encode_images(
            model,
            preprocess,
            [crop_box(image, box) for box in external_grid],
            device,
            args.batch_size,
        )
        scores = candidate_features @ text_features.T
        global_scores = candidate_features @ global_text_features.T

        positive_scores: dict[str, float] = {}
        for label_index, label in enumerate(labels):
            positive_features = encode_images(
                model,
                preprocess,
                [crop_box(image, box, context=0.1) for box in official_by_label[label]],
                device,
                args.batch_size,
            )
            positive_scores[label] = float(
                torch.median(positive_features @ text_features[label_index])
            )

        overlay = image.copy()
        draw = ImageDraw.Draw(overlay)
        width, height = image.size
        overlay_rank = 0
        for label_index, label in enumerate(labels):
            label_scores = scores[:, label_index]
            inclusion_probabilities = poisson_inclusion_probabilities(
                label_scores,
                args.expected_samples_per_group,
                args.sampling_temperature,
                args.minimum_inclusion_probability,
                args.maximum_inclusion_probability,
            )
            sampled = torch.rand(
                len(external_grid), generator=sampling_generator
            ) < inclusion_probabilities
            full_ranks = torch.argsort(
                torch.argsort(label_scores, descending=True)
            ) + 1
            correct_global_index = global_label_index[label]
            for candidate_index, box in enumerate(external_grid):
                score = float(label_scores[candidate_index])
                candidate_global_scores = global_scores[candidate_index]
                global_rank = 1 + int(
                    (
                        candidate_global_scores
                        > candidate_global_scores[correct_global_index]
                    )
                    .sum()
                    .item()
                )
                other_scores = torch.cat(
                    (
                        candidate_global_scores[:correct_global_index],
                        candidate_global_scores[correct_global_index + 1 :],
                    )
                )
                specificity_margin = score - float(other_scores.max())
                full_pool_rows.append(
                    {
                        "audit_id": row["audit_id"],
                        "image_filename": filename,
                        "assigned_style": row["assigned_style"],
                        "sample_type": row["sample_type"],
                        "label": label,
                        "full_rank": int(full_ranks[candidate_index]),
                        "candidate_score": score,
                        "official_median_score": positive_scores[label],
                        "score_margin": score - positive_scores[label],
                        "global_label_rank": global_rank,
                        "global_specificity_margin": specificity_margin,
                        "sampling_probability": float(
                            inclusion_probabilities[candidate_index]
                        ),
                        "sampled": int(sampled[candidate_index]),
                        "sampling_seed": args.sampling_seed,
                        "left": box[0],
                        "top": box[1],
                        "width": box[2] - box[0],
                        "height": box[3] - box[1],
                    }
                )
            top_values, top_indices = torch.topk(
                scores[:, label_index],
                k=min(args.top_k, len(external_grid)),
            )
            above = False
            for rank, (score, candidate_index) in enumerate(
                zip(top_values.tolist(), top_indices.tolist()),
                start=1,
            ):
                box = external_grid[candidate_index]
                margin = score - positive_scores[label]
                correct_global_index = global_label_index[label]
                candidate_global_scores = global_scores[candidate_index]
                global_rank = 1 + int(
                    (candidate_global_scores > candidate_global_scores[correct_global_index])
                    .sum()
                    .item()
                )
                other_scores = torch.cat(
                    (
                        candidate_global_scores[:correct_global_index],
                        candidate_global_scores[correct_global_index + 1 :],
                    )
                )
                specificity_margin = score - float(other_scores.max())
                above = above or margin >= 0
                output_rows.append(
                    {
                        "audit_id": row["audit_id"],
                        "image_filename": filename,
                        "assigned_style": row["assigned_style"],
                        "sample_type": row["sample_type"],
                        "label": label,
                        "rank": rank,
                        "candidate_score": score,
                        "official_median_score": positive_scores[label],
                        "score_margin": margin,
                        "global_label_rank": global_rank,
                        "global_specificity_margin": specificity_margin,
                        "left": box[0],
                        "top": box[1],
                        "width": box[2] - box[0],
                        "height": box[3] - box[1],
                    }
                )
                if rank == 1 and overlay_rank < 6:
                    x1, y1 = round(box[0] * width), round(box[1] * height)
                    x2, y2 = round(box[2] * width), round(box[3] * height)
                    color = (30, 210, 110) if margin >= 0 else (255, 175, 40)
                    draw.rectangle((x1, y1, x2, y2), outline=color, width=4)
                    caption = f"{label} {margin:+.3f}"
                    draw.text(
                        (x1 + 3, y1 + 3),
                        caption,
                        fill=color,
                        stroke_fill=(0, 0, 0),
                        stroke_width=2,
                        font=font,
                    )
                    overlay_rank += 1
            image_has_above_positive[label] += int(above)

        overlay.save(
            overlay_dir / f"{row['audit_id']}_candidates.jpg",
            quality=93,
        )
        print(
            f"[{image_index:02d}/{len(rows)}] {filename}: "
            f"{len(labels)} labels, {len(external_grid)} external windows",
            flush=True,
        )

    with (args.out_dir / "outside_box_candidates.csv").open(
        "w", newline=""
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output_rows[0]))
        writer.writeheader()
        writer.writerows(output_rows)
    if args.full_pool_csv is not None:
        args.full_pool_csv.parent.mkdir(parents=True, exist_ok=True)
        with args.full_pool_csv.open("w", newline="") as handle:
            writer = csv.DictWriter(
                handle, fieldnames=list(full_pool_rows[0])
            )
            writer.writeheader()
            writer.writerows(full_pool_rows)
        print(
            f"full_pool={len(full_pool_rows)} "
            f"sampled={sum(int(row['sampled']) for row in full_pool_rows)} "
            f"expected={args.expected_samples_per_group * len({(row['audit_id'], row['label']) for row in full_pool_rows}):.1f}",
            flush=True,
        )

    top_rows = sorted(
        output_rows,
        key=lambda row: (
            float(row["score_margin"]) >= 0,
            int(row["global_label_rank"]) <= 5,
            float(row["global_specificity_margin"]),
            float(row["score_margin"]),
        ),
        reverse=True,
    )
    positive_margin = sum(float(row["score_margin"]) >= 0 for row in output_rows)
    specific_candidates = sum(
        float(row["score_margin"]) >= 0
        and int(row["global_label_rank"]) <= 5
        for row in output_rows
    )
    report = [
        "# Frozen-CLIP 框外候选诊断",
        "",
        f"- 模型：`{args.model}` / `openai`",
        f"- 设备：`{device}`",
        f"- 图像：{len(rows)}",
        f"- 候选记录：{len(output_rows)}",
        (
            "- 框外候选分数不低于同图同标签官方框中位数："
            f"{positive_margin}/{len(output_rows)} "
            f"({100 * positive_margin / len(output_rows):.1f}%)"
        ),
        (
            "- 同时满足上述条件且该标签在 69 个审计标签中 rank ≤ 5："
            f"{specific_candidates}/{len(output_rows)} "
            f"({100 * specific_candidates / len(output_rows):.1f}%)"
        ),
        "",
        "该比例只用于安排人工复核顺序，不能解释为漏标率或模型精度。",
        "",
        "## 最高优先级候选",
        "",
        "| audit_id | 标签 | pos margin | global rank | specificity |",
        "|---|---|---:|---:|---:|",
    ]
    for item in top_rows[:30]:
        report.append(
            f"| {item['audit_id']} | {item['label']} | "
            f"{float(item['score_margin']):+.3f} | "
            f"{item['global_label_rank']} | "
            f"{float(item['global_specificity_margin']):+.3f} |"
        )
    (args.out_dir / "triage_report.md").write_text("\n".join(report) + "\n")


if __name__ == "__main__":
    main()
