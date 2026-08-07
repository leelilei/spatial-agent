#!/usr/bin/env python3
"""Score an adjudicated audit against official boxes.

The adjudicated CSV uses the same schema as annotation_template.csv. Only rows
with certainty=certain enter the primary analysis.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
from collections import defaultdict
from pathlib import Path


STYLE_POPULATION = {
    "Romanesque": 54,
    "Gothic": 49,
    "Renaissance": 22,
    "Baroque": 17,
}


def iou(a: dict[str, float], b: dict[str, float]) -> float:
    ax2, ay2 = a["left"] + a["width"], a["top"] + a["height"]
    bx2, by2 = b["left"] + b["width"], b["top"] + b["height"]
    ix1, iy1 = max(a["left"], b["left"]), max(a["top"], b["top"])
    ix2, iy2 = min(ax2, bx2), min(ay2, by2)
    intersection = max(0.0, ix2 - ix1) * max(0.0, iy2 - iy1)
    union = a["width"] * a["height"] + b["width"] * b["height"] - intersection
    return intersection / union if union > 0 else 0.0


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

    output: dict[str, set[str]] = {}
    for index, item in enumerate(meta):
        output[normalize_label(item["name"])] = {
            normalize_label(meta[parent]["name"]) for parent in visit(index)
        }
    return output


def labels_compatible(a: str, b: str, ancestors: dict[str, set[str]]) -> bool:
    a, b = normalize_label(a), normalize_label(b)
    if a == b:
        return True
    return b in ancestors.get(a, set()) or a in ancestors.get(b, set())


def load_adjudicated(path: Path) -> dict[str, list[dict[str, object]]]:
    by_image: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in csv.DictReader(path.open()):
        if row["certainty"].strip().lower() != "certain":
            continue
        coords: dict[str, float] = {}
        for key in ("left", "top", "width", "height"):
            try:
                coords[key] = float(row[key])
            except ValueError as exc:
                raise ValueError(f"{row['audit_id']}: invalid {key}") from exc
        if (
            coords["left"] < 0
            or coords["top"] < 0
            or coords["width"] <= 0
            or coords["height"] <= 0
            or coords["left"] + coords["width"] > 1.0001
            or coords["top"] + coords["height"] > 1.0001
        ):
            raise ValueError(f"{row['audit_id']}: box outside normalized image")
        by_image[row["image_filename"]].append(
            {
                **row,
                **coords,
                "feature_label": row["feature_label"].strip(),
            }
        )
    if not by_image:
        raise ValueError("No certainty=certain boxes found in adjudicated CSV")
    return by_image


def estimate(image_stats: list[dict[str, object]]) -> dict[str, float]:
    official = sum(float(row["weight"]) * int(row["official"]) for row in image_stats)
    complete = sum(float(row["weight"]) * int(row["complete"]) for row in image_stats)
    matched = sum(float(row["weight"]) * int(row["matched"]) for row in image_stats)
    missing = max(0.0, complete - matched)
    return {
        "weighted_official": official,
        "weighted_complete": complete,
        "weighted_matched": matched,
        "original_recall": matched / complete if complete else float("nan"),
        "missing_positive_rate": missing / complete if complete else float("nan"),
    }


def bootstrap_ci(
    image_stats: list[dict[str, object]],
    seed: int,
    replicates: int,
) -> dict[str, list[float]]:
    rng = random.Random(seed)
    by_style: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in image_stats:
        by_style[str(row["style"])].append(row)
    values: dict[str, list[float]] = defaultdict(list)
    for _ in range(replicates):
        sample: list[dict[str, object]] = []
        for rows in by_style.values():
            sample.extend(rng.choices(rows, k=len(rows)))
        result = estimate(sample)
        for key in ("original_recall", "missing_positive_rate"):
            values[key].append(result[key])
    output: dict[str, list[float]] = {}
    for key, samples in values.items():
        ordered = sorted(value for value in samples if value == value)
        output[key] = [
            ordered[int(0.025 * (len(ordered) - 1))],
            ordered[int(0.975 * (len(ordered) - 1))],
        ]
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parts", type=Path, required=True)
    parser.add_argument("--selection", type=Path, required=True)
    parser.add_argument("--adjudicated", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--iou", type=float, default=0.5)
    parser.add_argument("--seed", type=int, default=20260725)
    parser.add_argument("--bootstrap", type=int, default=5000)
    args = parser.parse_args()

    payload = json.loads(args.parts.read_text())
    meta = payload["meta"]
    official_payload = payload["annotations"]
    ancestors = ancestor_sets(meta)
    complete_by_image = load_adjudicated(args.adjudicated)
    selection = list(csv.DictReader(args.selection.open()))
    selection_by_filename = {row["image_filename"]: row for row in selection}
    args.out_dir.mkdir(parents=True, exist_ok=True)

    match_rows: list[dict[str, object]] = []
    image_stats: list[dict[str, object]] = []
    for filename, complete_boxes in complete_by_image.items():
        if filename not in selection_by_filename:
            raise ValueError(f"{filename} is absent from selection")
        selected = selection_by_filename[filename]
        if selected["sample_type"] != "core":
            continue
        official_boxes: list[dict[str, object]] = []
        for group in official_payload[filename]["bbox_groups"]:
            for element in group["elements"]:
                official_boxes.append(
                    {
                        **element,
                        "feature_label": meta[element["label"]]["name"],
                    }
                )

        candidates: list[tuple[float, int, int]] = []
        for official_index, official_box in enumerate(official_boxes):
            for complete_index, complete_box in enumerate(complete_boxes):
                overlap = iou(official_box, complete_box)
                if overlap >= args.iou and labels_compatible(
                    str(official_box["feature_label"]),
                    str(complete_box["feature_label"]),
                    ancestors,
                ):
                    candidates.append((overlap, official_index, complete_index))
        used_official: set[int] = set()
        used_complete: set[int] = set()
        for overlap, official_index, complete_index in sorted(
            candidates, reverse=True
        ):
            if official_index in used_official or complete_index in used_complete:
                continue
            used_official.add(official_index)
            used_complete.add(complete_index)
            match_rows.append(
                {
                    "image_filename": filename,
                    "official_label": official_boxes[official_index]["feature_label"],
                    "complete_label": complete_boxes[complete_index]["feature_label"],
                    "iou": overlap,
                }
            )

        style = selected["assigned_style"]
        core_n = sum(
            row["sample_type"] == "core" and row["assigned_style"] == style
            for row in selection
        )
        image_stats.append(
            {
                "image_filename": filename,
                "style": style,
                "weight": STYLE_POPULATION[style] / core_n,
                "official": len(official_boxes),
                "complete": len(complete_boxes),
                "matched": len(used_complete),
                "new": len(complete_boxes) - len(used_complete),
            }
        )

    if len(image_stats) != 40:
        raise ValueError(
            f"Primary analysis requires all 40 core images; found {len(image_stats)}"
        )

    result = estimate(image_stats)
    result["bootstrap_95_ci"] = bootstrap_ci(
        image_stats, args.seed, args.bootstrap
    )
    result["iou_threshold"] = args.iou
    result["core_images"] = len(image_stats)

    with (args.out_dir / "image_level_results.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(image_stats[0]))
        writer.writeheader()
        writer.writerows(image_stats)
    with (args.out_dir / "matched_boxes.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["image_filename", "official_label", "complete_label", "iou"],
        )
        writer.writeheader()
        writer.writerows(match_rows)
    (args.out_dir / "audit_metrics.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    )

    recall_ci = result["bootstrap_95_ci"]["original_recall"]
    missing_ci = result["bootstrap_95_ci"]["missing_positive_rate"]
    report = [
        "# WikiChurches 漏标审计结果",
        "",
        f"- Core 图像：{len(image_stats)}",
        f"- IoU 匹配阈值：{args.iou}",
        (
            f"- 原始标注召回率：{100 * result['original_recall']:.1f}% "
            f"(bootstrap 95% CI {100 * recall_ci[0]:.1f}–"
            f"{100 * recall_ci[1]:.1f}%)"
        ),
        (
            f"- Missing Positive Rate："
            f"{100 * result['missing_positive_rate']:.1f}% "
            f"(bootstrap 95% CI {100 * missing_ci[0]:.1f}–"
            f"{100 * missing_ci[1]:.1f}%)"
        ),
        "",
        "Stress 样本不进入上述总体比例估计，应另行报告失败模式。",
    ]
    (args.out_dir / "audit_results.md").write_text("\n".join(report) + "\n")


if __name__ == "__main__":
    main()

