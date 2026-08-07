#!/usr/bin/env python3
"""Create train-only leave-one-church-out local calibration scores."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

import torch

from wikichurches_positive_anchor_features import (
    STYLE_ID_TO_NAME,
    STYLE_NAMES,
    STYLE_TO_INDEX,
    encode_images,
    expanded_box,
    farthest_point_indices,
    openai_clip,
    pool_box_tokens,
    read_split,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--region-manifest", type=Path, required=True)
    parser.add_argument("--image-dir", type=Path, required=True)
    parser.add_argument("--labels-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--out-file", type=Path, required=True)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--batch-size", type=int, default=8)
    return parser.parse_args()


def select_bank(
    records_by_style: dict[int, list[dict[str, object]]],
    excluded_church: str,
    anchors_per_style: int,
) -> tuple[torch.Tensor, dict[str, int]]:
    per_style = []
    available = {}
    for style in range(len(STYLE_NAMES)):
        records = [
            record
            for record in records_by_style[style]
            if record["church_id"] != excluded_church
        ]
        available[STYLE_NAMES[style]] = len(records)
        if len(records) < anchors_per_style:
            raise RuntimeError(
                f"Only {len(records)} {STYLE_NAMES[style]} regions remain "
                f"after excluding church {excluded_church}"
            )
        features = torch.stack([record["feature"] for record in records])
        selected = farthest_point_indices(features, anchors_per_style)
        per_style.append(features[selected])
    return torch.stack(per_style), available


def score_query(
    query_tokens: torch.Tensor,
    bank: torch.Tensor,
    ratios: list[float],
) -> dict[str, torch.Tensor]:
    similarities = torch.einsum("pd,cad->pca", query_tokens, bank)
    per_patch = similarities.max(dim=-1).values
    output = {}
    for ratio in ratios:
        count = max(1, int(round(len(query_tokens) * ratio)))
        output[str(ratio)] = per_patch.topk(count, dim=0).values.mean(dim=0)
    return output


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    resolution = int(protocol["resolution"])
    expected_grid = int(protocol["patch_grid"])
    context = float(protocol["box_context"])
    anchors_per_style = int(protocol["anchors_per_style"])
    ratios = [float(value) for value in protocol["topk_patch_ratios"]]
    device = torch.device(args.device)

    train_rows = read_split(args.labels_dir / "wc4_train.txt")
    train_style = {filename: style_id for filename, style_id in train_rows}
    manifest_rows = list(
        csv.DictReader(args.region_manifest.open(encoding="utf-8"))
    )
    official_rows = [
        row
        for row in manifest_rows
        if row["region_type"] == "official"
        and row["image_filename"] in train_style
    ]
    query_names = sorted({row["image_filename"] for row in official_rows})
    if not query_names:
        raise RuntimeError("No train images with official boxes")
    church_by_image = {}
    for row in official_rows:
        previous = church_by_image.setdefault(
            row["image_filename"],
            row["church_id"],
        )
        if previous != row["church_id"]:
            raise RuntimeError("Image maps to more than one church")

    model, _ = openai_clip.load(
        protocol.get("model", "ViT-B/16"),
        device=device,
    )
    model.eval()
    query_tokens, grid = encode_images(
        query_names,
        args.image_dir,
        model,
        resolution,
        args.batch_size,
        device,
    )
    if grid != expected_grid:
        raise RuntimeError(f"Expected {expected_grid} grid, got {grid}")
    filename_to_index = {
        filename: index for index, filename in enumerate(query_names)
    }

    official_records: dict[int, list[dict[str, object]]] = defaultdict(list)
    random_records: dict[
        int, dict[int, list[dict[str, object]]]
    ] = defaultdict(lambda: defaultdict(list))
    for row in manifest_rows:
        filename = row["image_filename"]
        if filename not in filename_to_index:
            continue
        style = STYLE_TO_INDEX[row["style_name"]]
        feature = pool_box_tokens(
            query_tokens[filename_to_index[filename]],
            grid,
            expanded_box(row, context),
        )
        record = {
            "church_id": row["church_id"],
            "box_id": row["box_id"],
            "feature": feature,
        }
        if row["region_type"] == "official":
            official_records[style].append(record)
        else:
            random_records[int(row["control_index"])][style].append(record)

    control_indices = sorted(random_records)
    expected_controls = int(protocol["random_control_banks"])
    if control_indices != list(range(expected_controls)):
        raise RuntimeError(
            f"Expected random controls 0..{expected_controls - 1}, "
            f"got {control_indices}"
        )
    official_scores = {str(ratio): [] for ratio in ratios}
    random_scores = {
        str(ratio): [[] for _ in control_indices] for ratio in ratios
    }
    minimum_available = {
        "official": {style: 10**9 for style in STYLE_NAMES},
        "random": {
            str(control): {style: 10**9 for style in STYLE_NAMES}
            for control in control_indices
        },
    }
    for query_index, filename in enumerate(query_names):
        excluded_church = church_by_image[filename]
        official_bank, available = select_bank(
            official_records,
            excluded_church,
            anchors_per_style,
        )
        for style, count in available.items():
            minimum_available["official"][style] = min(
                minimum_available["official"][style],
                count,
            )
        scores = score_query(query_tokens[query_index], official_bank, ratios)
        for ratio in ratios:
            official_scores[str(ratio)].append(scores[str(ratio)])

        for control in control_indices:
            random_bank, available = select_bank(
                random_records[control],
                excluded_church,
                anchors_per_style,
            )
            for style, count in available.items():
                minimum_available["random"][str(control)][style] = min(
                    minimum_available["random"][str(control)][style],
                    count,
                )
            scores = score_query(query_tokens[query_index], random_bank, ratios)
            for ratio in ratios:
                random_scores[str(ratio)][control].append(scores[str(ratio)])
        print(
            f"loco_scored={query_index + 1}/{len(query_names)}",
            flush=True,
        )

    official_scores = {
        key: torch.stack(values) for key, values in official_scores.items()
    }
    random_scores = {
        key: torch.stack(
            [torch.stack(control_values) for control_values in values]
        )
        for key, values in random_scores.items()
    }
    labels = torch.tensor(
        [
            STYLE_TO_INDEX[STYLE_ID_TO_NAME[train_style[filename]]]
            for filename in query_names
        ],
        dtype=torch.long,
    )
    output = {
        "experiment_id": protocol["experiment_id"],
        "split": "train_loco_calibration",
        "resolution": resolution,
        "grid": grid,
        "style_names": STYLE_NAMES,
        "image_names": query_names,
        "church_ids": [church_by_image[name] for name in query_names],
        "labels": labels,
        "topk_patch_ratios": ratios,
        "official_calibration_scores": official_scores,
        "random_calibration_scores": random_scores,
        "minimum_available_after_church_exclusion": minimum_available,
        "test_images_encoded": 0,
    }
    args.out_file.parent.mkdir(parents=True, exist_ok=True)
    torch.save(output, args.out_file)
    summary = {
        "experiment_id": protocol["experiment_id"],
        "split": output["split"],
        "query_images": len(query_names),
        "query_churches": len(set(output["church_ids"])),
        "style_counts": dict(
            Counter(STYLE_NAMES[int(label)] for label in labels)
        ),
        "resolution": resolution,
        "grid": grid,
        "anchors_per_style": anchors_per_style,
        "random_control_banks": expected_controls,
        "minimum_available_after_church_exclusion": minimum_available,
        "test_images_encoded": 0,
    }
    args.out_file.with_suffix(".json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
