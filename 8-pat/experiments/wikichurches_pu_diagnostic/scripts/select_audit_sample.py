#!/usr/bin/env python3
"""Select a deterministic, style-balanced, diverse 50-image audit sample."""

from __future__ import annotations

import argparse
import csv
import json
import random
import statistics
from collections import Counter, defaultdict
from pathlib import Path


STYLE_NAMES = {
    "Q46261": "Romanesque",
    "Q176483": "Gothic",
    "Q236122": "Renaissance",
    "Q840829": "Baroque",
}
QUOTAS = {
    "Q46261": 15,
    "Q176483": 15,
    "Q236122": 10,
    "Q840829": 10,
}
CORE_QUOTAS = {
    "Q46261": 12,
    "Q176483": 12,
    "Q236122": 8,
    "Q840829": 8,
}


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parts", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=20260725)
    args = parser.parse_args()

    payload = json.loads(args.parts.read_text())
    meta = payload["meta"]
    annotations = payload["annotations"]
    args.out_dir.mkdir(parents=True, exist_ok=True)

    candidates: dict[str, list[dict[str, object]]] = defaultdict(list)
    for filename, item in annotations.items():
        labels: list[str] = []
        areas: list[float] = []
        for group in item["bbox_groups"]:
            for element in group["elements"]:
                labels.append(meta[element["label"]]["name"])
                areas.append(element["width"] * element["height"])
        record = {
            "image_filename": filename,
            "church_id": filename.split("_wd", 1)[0],
            "style_ids": item["styles"],
            "box_count": len(labels),
            "group_count": len(item["bbox_groups"]),
            "median_relative_area": statistics.median(areas),
            "labels": sorted(set(labels)),
        }
        for style_id in item["styles"]:
            if style_id in QUOTAS:
                candidates[style_id].append(record)

    rng = random.Random(args.seed)
    selected: list[dict[str, object]] = []
    used_files: set[str] = set()
    used_labels: Counter[str] = Counter()

    for style_id, quota in QUOTAS.items():
        pool = candidates[style_id][:]
        rng.shuffle(pool)
        core: list[dict[str, object]] = []
        for item in pool:
            if str(item["image_filename"]) in used_files:
                continue
            core.append(item)
            used_files.add(str(item["image_filename"]))
            if len(core) == CORE_QUOTAS[style_id]:
                break
        if len(core) != CORE_QUOTAS[style_id]:
            raise RuntimeError(f"Insufficient unique core images for {style_id}")
        for item in core:
            used_labels.update(item["labels"])
            selected.append(
                {
                    "sample_type": "core",
                    "assigned_style_id": style_id,
                    **item,
                }
            )

        stress: list[dict[str, object]] = []
        stress_quota = quota - CORE_QUOTAS[style_id]
        while len(stress) < stress_quota:
            available = [
                item for item in pool
                if str(item["image_filename"]) not in used_files
            ]
            if not available:
                raise RuntimeError(f"Insufficient unique images for {style_id}")

            def score(item: dict[str, object]) -> tuple[float, float, float]:
                novelty = sum(1 / (1 + used_labels[label]) for label in item["labels"])
                # Prefer both rich and tiny-feature images without making box count
                # the sole selection criterion.
                small_feature = 1 / max(float(item["median_relative_area"]), 1e-9)
                jitter = rng.random() * 1e-6
                return novelty, small_feature, float(item["box_count"]) + jitter

            pick = max(available, key=score)
            stress.append(pick)
            used_files.add(str(pick["image_filename"]))
            used_labels.update(pick["labels"])

        for item in stress:
            selected.append(
                {
                    "sample_type": "stress",
                    "assigned_style_id": style_id,
                    **item,
                }
            )

    rng.shuffle(selected)
    blinded_rows: list[dict[str, object]] = []
    sealed_rows: list[dict[str, object]] = []
    annotation_rows: list[dict[str, object]] = []
    for index, item in enumerate(selected, start=1):
        audit_id = f"WC-AUD-{index:03d}"
        blinded_rows.append(
            {
                "audit_id": audit_id,
                "image_filename": item["image_filename"],
                "assigned_style": STYLE_NAMES[item["assigned_style_id"]],
                "sample_type": item["sample_type"],
            }
        )
        sealed_rows.append(
            {
                "audit_id": audit_id,
                "image_filename": item["image_filename"],
                "church_id": item["church_id"],
                "assigned_style_id": item["assigned_style_id"],
                "assigned_style": STYLE_NAMES[item["assigned_style_id"]],
                "sample_type": item["sample_type"],
                "all_style_ids": "|".join(item["style_ids"]),
                "box_count": item["box_count"],
                "group_count": item["group_count"],
                "median_relative_area": item["median_relative_area"],
                "official_labels": "|".join(item["labels"]),
            }
        )
        annotation_rows.append(
            {
                "audit_id": audit_id,
                "image_filename": item["image_filename"],
                "sample_type": item["sample_type"],
                "annotator_id": "",
                "feature_label": "",
                "parent_label": "",
                "left": "",
                "top": "",
                "width": "",
                "height": "",
                "certainty": "",
                "visibility": "",
                "occlusion": "",
                "notes": "",
            }
        )

    write_csv(args.out_dir / "blinded_manifest.csv", blinded_rows)
    write_csv(args.out_dir / "sealed_selection.csv", sealed_rows)
    write_csv(args.out_dir / "annotation_template.csv", annotation_rows)

    counts = Counter(
        (row["assigned_style"], row["sample_type"]) for row in blinded_rows
    )
    report = [
        "# 50 图审计样本",
        "",
        f"- seed：`{args.seed}`",
        f"- 图像数：{len(selected)}",
        f"- 唯一教堂数：{len(set(row['church_id'] for row in sealed_rows))}",
        "",
        "| 风格 | Core | Stress | 合计 |",
        "|---|---:|---:|---:|",
    ]
    for name in sorted(STYLE_NAMES.values()):
        core_count = counts[(name, "core")]
        stress_count = counts[(name, "stress")]
        report.append(
            f"| {name} | {core_count} | {stress_count} | "
            f"{core_count + stress_count} |"
        )
    report.extend(
        [
            "",
            "Core 在固定风格配额内随机抽样，用于主要比例估计；Stress 从剩余图像中"
            "优先覆盖尚未覆盖的构件标签和小构件，只用于发现失败模式。"
            "原始框信息仅保存在 sealed 文件。",
        ]
    )
    (args.out_dir / "selection_report.md").write_text("\n".join(report) + "\n")


if __name__ == "__main__":
    main()
