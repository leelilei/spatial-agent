#!/usr/bin/env python3
"""Create a reproducible inventory of the official WikiChurches part boxes."""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from collections import Counter
from pathlib import Path


STYLE_NAMES = {
    "Q46261": "Romanesque",
    "Q176483": "Gothic",
    "Q236122": "Renaissance",
    "Q840829": "Baroque",
}


def quantile(values: list[float], q: float) -> float:
    ordered = sorted(values)
    if not ordered:
        return math.nan
    pos = (len(ordered) - 1) * q
    lo, hi = math.floor(pos), math.ceil(pos)
    if lo == hi:
        return ordered[lo]
    return ordered[lo] * (hi - pos) + ordered[hi] * (pos - lo)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parts", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    payload = json.loads(args.parts.read_text())
    meta = payload["meta"]
    annotations = payload["annotations"]
    args.out_dir.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, object]] = []
    label_counts: Counter[str] = Counter()
    style_images: Counter[str] = Counter()
    style_boxes: Counter[str] = Counter()
    group_count = 0
    multi_element_groups = 0
    images_with_repeated_leaf_label = 0
    extra_repeated_leaf_boxes = 0

    for filename, item in sorted(annotations.items()):
        style_ids = item["styles"]
        for style_id in style_ids:
            style_images[style_id] += 1

        image_areas: list[float] = []
        image_labels: list[str] = []
        box_count = 0
        for group_index, group in enumerate(item["bbox_groups"]):
            group_count += 1
            if len(group["elements"]) > 1:
                multi_element_groups += 1
            for element_index, element in enumerate(group["elements"]):
                label_name = meta[element["label"]]["name"]
                area = element["width"] * element["height"]
                image_areas.append(area)
                image_labels.append(label_name)
                label_counts[label_name] += 1
                box_count += 1
                for style_id in style_ids:
                    style_boxes[style_id] += 1
                rows.append(
                    {
                        "image_filename": filename,
                        "church_id": filename.split("_wd", 1)[0],
                        "style_ids": "|".join(style_ids),
                        "style_names": "|".join(
                            STYLE_NAMES.get(style_id, style_id)
                            for style_id in style_ids
                        ),
                        "group_index": group_index,
                        "group_label_id": group["group_label"],
                        "group_label": meta[group["group_label"]]["name"],
                        "element_index": element_index,
                        "label_id": element["label"],
                        "label": label_name,
                        "left": element["left"],
                        "top": element["top"],
                        "width": element["width"],
                        "height": element["height"],
                        "relative_area": area,
                    }
                )
        image_label_counts = Counter(image_labels)
        if any(count > 1 for count in image_label_counts.values()):
            images_with_repeated_leaf_label += 1
        extra_repeated_leaf_boxes += sum(
            max(0, count - 1) for count in image_label_counts.values()
        )

    inventory_path = args.out_dir / "official_box_inventory.csv"
    with inventory_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    areas = [float(row["relative_area"]) for row in rows]
    per_image = Counter(str(row["image_filename"]) for row in rows)
    summary = {
        "images": len(annotations),
        "groups": group_count,
        "boxes": len(rows),
        "multi_element_groups": multi_element_groups,
        "images_with_repeated_leaf_label": images_with_repeated_leaf_label,
        "extra_repeated_leaf_boxes": extra_repeated_leaf_boxes,
        "unique_image_leaf_label_pairs": len(rows) - extra_repeated_leaf_boxes,
        "style_image_counts": {
            STYLE_NAMES.get(key, key): value
            for key, value in style_images.most_common()
        },
        "style_box_memberships": {
            STYLE_NAMES.get(key, key): value
            for key, value in style_boxes.most_common()
        },
        "boxes_per_image": {
            "mean": statistics.mean(per_image.values()),
            "median": statistics.median(per_image.values()),
            "min": min(per_image.values()),
            "max": max(per_image.values()),
        },
        "relative_box_area": {
            "min": min(areas),
            "q25": quantile(areas, 0.25),
            "median": quantile(areas, 0.50),
            "q75": quantile(areas, 0.75),
            "max": max(areas),
        },
        "top_labels": label_counts.most_common(30),
    }
    (args.out_dir / "annotation_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n"
    )

    report = [
        "# WikiChurches 官方局部框清点",
        "",
        f"- 图像：{summary['images']}",
        f"- 框组：{summary['groups']}",
        f"- 元素框：{summary['boxes']}",
        f"- 多元素框组：{summary['multi_element_groups']}",
        (
            "- 同图出现重复 leaf label："
            f"{summary['images_with_repeated_leaf_label']}/{summary['images']} 图"
        ),
        (
            "- 631 个框中，仅 "
            f"{summary['extra_repeated_leaf_boxes']} 个是同图同 leaf label 的"
            "第二个或后续实例"
        ),
        (
            "- 每图框数："
            f"mean {summary['boxes_per_image']['mean']:.2f}, "
            f"median {summary['boxes_per_image']['median']:.0f}, "
            f"range {summary['boxes_per_image']['min']}–"
            f"{summary['boxes_per_image']['max']}"
        ),
        (
            "- 相对框面积："
            f"Q1 {100 * summary['relative_box_area']['q25']:.3f}%, "
            f"median {100 * summary['relative_box_area']['median']:.3f}%, "
            f"Q3 {100 * summary['relative_box_area']['q75']:.3f}%"
        ),
        "",
        "## 风格分布",
        "",
        "| 风格 | 带框图像数 | 框归属数 |",
        "|---|---:|---:|",
    ]
    for style_name, image_count in summary["style_image_counts"].items():
        report.append(
            f"| {style_name} | {image_count} | "
            f"{summary['style_box_memberships'][style_name]} |"
        )
    report.extend(
        [
            "",
            "注：少量图像有两个风格标签，因此“框归属数”可能重复计数。",
            "",
            "## 高频构件",
            "",
            "| 构件 | 框数 |",
            "|---|---:|",
        ]
    )
    report.extend(f"| {name} | {count} |" for name, count in summary["top_labels"])
    (args.out_dir / "annotation_inventory_report.md").write_text(
        "\n".join(report) + "\n"
    )


if __name__ == "__main__":
    main()
