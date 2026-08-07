#!/usr/bin/env python3
"""Paired WikiChurches official-box versus matched-random information probe.

The script uses only the canonical train+val splits. Test filenames are loaded
solely to assert exclusion and are never opened or encoded.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

import numpy as np
import torch
from PIL import Image, ImageOps


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TOGA_ROOT = Path(
    os.environ.get("TOGA_ROOT", str(PROJECT_ROOT / "vendor" / "TOGA"))
)
sys.path.insert(0, str(TOGA_ROOT))
import clip as openai_clip  # noqa: E402


STYLE_ID_TO_NAME = {
    "Q46261": "Romanesque",
    "Q176483": "Gothic",
    "Q236122": "Renaissance",
    "Q840829": "Baroque",
}
STYLE_NAMES = tuple(STYLE_ID_TO_NAME.values())
STYLE_TO_INDEX = {name: index for index, name in enumerate(STYLE_NAMES)}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parts", type=Path, required=True)
    parser.add_argument("--image-dir", type=Path, required=True)
    parser.add_argument("--labels-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--max-images", type=int)
    return parser.parse_args()


def choose_device(requested: str) -> torch.device:
    if requested != "auto":
        return torch.device(requested)
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def read_split(path: Path) -> dict[str, str]:
    rows: dict[str, str] = {}
    with path.open(encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            fields = line.split()
            if len(fields) != 2:
                raise ValueError(f"{path}:{line_number}: expected filename style_id")
            filename, style_id = fields
            if style_id not in STYLE_ID_TO_NAME:
                raise ValueError(f"Unsupported style ID: {style_id}")
            if filename in rows:
                raise ValueError(f"Duplicate split filename: {filename}")
            rows[filename] = style_id
    return rows


def church_id(filename: str) -> str:
    identifier, separator, suffix = filename.rpartition("_wd")
    if not separator or not identifier or not suffix.endswith(".jpg"):
        raise ValueError(f"Unexpected filename: {filename}")
    return identifier


def normalize_rows(array: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(array, axis=1, keepdims=True)
    return array / np.clip(norms, 1e-12, None)


def overlap_fraction(
    candidate: tuple[float, float, float, float],
    official: tuple[float, float, float, float],
) -> float:
    x1, y1, x2, y2 = candidate
    ox1, oy1, ox2, oy2 = official
    intersection = max(0.0, min(x2, ox2) - max(x1, ox1)) * max(
        0.0, min(y2, oy2) - max(y1, oy1)
    )
    area = max(1e-12, (x2 - x1) * (y2 - y1))
    return intersection / area


def matched_random_boxes(
    official_box: tuple[float, float, float, float],
    all_official: list[tuple[float, float, float, float]],
    count: int,
    candidate_draws: int,
    rng: random.Random,
) -> list[tuple[tuple[float, float, float, float], float]]:
    x1, y1, x2, y2 = official_box
    width = x2 - x1
    height = y2 - y1
    if not 0 < width <= 1 or not 0 < height <= 1:
        raise ValueError(f"Invalid official box: {official_box}")
    candidates = {}
    for _ in range(candidate_draws):
        left = rng.uniform(0.0, max(0.0, 1.0 - width))
        top = rng.uniform(0.0, max(0.0, 1.0 - height))
        box = (left, top, left + width, top + height)
        key = tuple(round(value, 8) for value in box)
        if key in candidates:
            continue
        maximum_overlap = max(
            overlap_fraction(box, other) for other in all_official
        )
        candidates[key] = (box, maximum_overlap)
    ranked = sorted(
        candidates.values(),
        key=lambda item: item[1],
    )
    if len(ranked) < count:
        raise RuntimeError("Unable to generate enough unique random controls")
    return ranked[:count]


def crop_with_context(
    image: Image.Image,
    box: tuple[float, float, float, float],
    context: float,
) -> Image.Image:
    width, height = image.size
    x1, y1, x2, y2 = box
    dx = (x2 - x1) * context
    dy = (y2 - y1) * context
    left = max(0, min(width - 1, round((x1 - dx) * width)))
    top = max(0, min(height - 1, round((y1 - dy) * height)))
    right = max(left + 1, min(width, round((x2 + dx) * width)))
    bottom = max(top + 1, min(height, round((y2 + dy) * height)))
    return image.crop((left, top, right, bottom))


def encode_regions(
    model: torch.nn.Module,
    preprocess,
    records: list[dict[str, object]],
    image_dir: Path,
    device: torch.device,
    batch_size: int,
    context: float,
) -> np.ndarray:
    features: list[np.ndarray] = []
    image_cache: dict[str, Image.Image] = {}
    with torch.inference_mode():
        for start in range(0, len(records), batch_size):
            batch_records = records[start : start + batch_size]
            tensors = []
            for record in batch_records:
                filename = str(record["image_filename"])
                if filename not in image_cache:
                    image_cache[filename] = ImageOps.exif_transpose(
                        Image.open(image_dir / filename)
                    ).convert("RGB")
                box = tuple(float(record[key]) for key in ("left", "top", "right", "bottom"))
                tensors.append(
                    preprocess(
                        crop_with_context(image_cache[filename], box, context)
                    )
                )
            batch = torch.stack(tensors).to(device)
            encoded = model.encode_image(batch)
            encoded = encoded / encoded.norm(dim=-1, keepdim=True)
            features.append(encoded.float().cpu().numpy())
            print(
                f"encoded={min(start + batch_size, len(records))}/{len(records)}",
                flush=True,
            )
    return np.concatenate(features, axis=0)


def encode_style_text(
    model: torch.nn.Module,
    prompts: list[str],
    device: torch.device,
) -> np.ndarray:
    outputs = []
    with torch.inference_mode():
        for style in STYLE_NAMES:
            tokens = openai_clip.tokenize(
                [template.format(style=style.lower()) for template in prompts]
            ).to(device)
            encoded = model.encode_text(tokens)
            encoded = encoded / encoded.norm(dim=-1, keepdim=True)
            mean = encoded.mean(dim=0)
            mean = mean / mean.norm()
            outputs.append(mean.float().cpu().numpy())
    return np.stack(outputs)


def class_margin(scores: np.ndarray, target: int) -> float:
    incorrect = np.delete(scores, target)
    return float(scores[target] - incorrect.max())


def percentile_interval(values: np.ndarray) -> tuple[float, float]:
    return float(np.percentile(values, 2.5)), float(np.percentile(values, 97.5))


def balanced_accuracy(labels: np.ndarray, predictions: np.ndarray) -> float:
    recalls = []
    for label in range(len(STYLE_NAMES)):
        mask = labels == label
        if mask.any():
            recalls.append(float((predictions[mask] == label).mean()))
    return float(np.mean(recalls))


def stratified_folds(
    labels: np.ndarray,
    folds: int,
    rng: random.Random,
) -> list[np.ndarray]:
    assignments: list[list[int]] = [[] for _ in range(folds)]
    for label in range(len(STYLE_NAMES)):
        indices = np.flatnonzero(labels == label).tolist()
        rng.shuffle(indices)
        for position, index in enumerate(indices):
            assignments[position % folds].append(index)
    return [np.array(sorted(items), dtype=int) for items in assignments]


def prototype_predictions(
    train_features: np.ndarray,
    train_labels: np.ndarray,
    test_features: np.ndarray,
) -> np.ndarray:
    prototypes = []
    for label in range(len(STYLE_NAMES)):
        class_features = train_features[train_labels == label]
        if len(class_features) == 0:
            raise RuntimeError(f"Training fold lacks class {label}")
        prototype = class_features.mean(axis=0, keepdims=True)
        prototypes.append(normalize_rows(prototype)[0])
    return np.argmax(test_features @ np.stack(prototypes).T, axis=1)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    args = parse_args()
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    args.out_dir.mkdir(parents=True, exist_ok=True)
    audit_dir = args.out_dir / "audit"
    audit_dir.mkdir(exist_ok=True)

    parts_document = json.loads(args.parts.read_text(encoding="utf-8"))
    annotations = parts_document["annotations"]
    split_maps = {
        split: read_split(args.labels_dir / f"wc4_{split}.txt")
        for split in ("train", "val", "test")
    }
    development = {**split_maps["train"], **split_maps["val"]}
    selected_names = sorted(set(annotations) & set(development))
    if args.max_images is not None:
        selected_names = selected_names[: args.max_images]
    test_overlap = set(selected_names) & set(split_maps["test"])
    if test_overlap:
        raise RuntimeError(f"Forbidden test images selected: {sorted(test_overlap)}")
    selected_churches = [church_id(name) for name in selected_names]
    if len(selected_churches) != len(set(selected_churches)):
        raise RuntimeError("Annotated development images are not church-disjoint")
    missing_images = [
        filename for filename in selected_names if not (args.image_dir / filename).is_file()
    ]
    if missing_images:
        raise FileNotFoundError(f"Missing images: {missing_images[:5]}")

    random_seed = int(protocol["random_seed"])
    random_per_box = int(protocol["random_controls_per_box"])
    candidate_draws = int(protocol["random_candidate_draws_per_box"])
    target_overlap = float(protocol["target_max_overlap_with_any_official_box"])
    random_generator = random.Random(random_seed)
    region_records: list[dict[str, object]] = []
    box_metadata: list[dict[str, object]] = []
    style_image_counts = Counter()
    style_box_counts = Counter()

    for filename in selected_names:
        style_id = development[filename]
        style_name = STYLE_ID_TO_NAME[style_id]
        style_index = STYLE_TO_INDEX[style_name]
        style_image_counts[style_name] += 1
        official_boxes = []
        for group in annotations[filename]["bbox_groups"]:
            for element in group["elements"]:
                official_boxes.append(
                    (
                        float(element["left"]),
                        float(element["top"]),
                        float(element["left"] + element["width"]),
                        float(element["top"] + element["height"]),
                        int(element["label"]),
                    )
                )
        spatial_boxes = [box[:4] for box in official_boxes]
        for box_index, official in enumerate(official_boxes):
            official_box = official[:4]
            box_id = f"{filename}__box{box_index:03d}"
            official_record_index = len(region_records)
            region_records.append(
                {
                    "box_id": box_id,
                    "region_type": "official",
                    "control_index": -1,
                    "image_filename": filename,
                    "church_id": church_id(filename),
                    "style_id": style_id,
                    "style_name": style_name,
                    "style_index": style_index,
                    "component_label_id": official[4],
                    "left": official_box[0],
                    "top": official_box[1],
                    "right": official_box[2],
                    "bottom": official_box[3],
                    "max_official_overlap": 1.0,
                }
            )
            controls = matched_random_boxes(
                official_box,
                spatial_boxes,
                random_per_box,
                candidate_draws,
                random_generator,
            )
            control_indices = []
            for control_index, (control, maximum_overlap) in enumerate(controls):
                control_indices.append(len(region_records))
                region_records.append(
                    {
                        "box_id": box_id,
                        "region_type": "random",
                        "control_index": control_index,
                        "image_filename": filename,
                        "church_id": church_id(filename),
                        "style_id": style_id,
                        "style_name": style_name,
                        "style_index": style_index,
                        "component_label_id": official[4],
                        "left": control[0],
                        "top": control[1],
                        "right": control[2],
                        "bottom": control[3],
                        "max_official_overlap": maximum_overlap,
                    }
                )
            box_metadata.append(
                {
                    "box_id": box_id,
                    "image_filename": filename,
                    "church_id": church_id(filename),
                    "style_name": style_name,
                    "style_index": style_index,
                    "official_record_index": official_record_index,
                    "control_record_indices": control_indices,
                }
            )
            style_box_counts[style_name] += 1

    expected_records = len(box_metadata) * (1 + random_per_box)
    if len(region_records) != expected_records:
        raise RuntimeError("Region record cardinality mismatch")
    write_csv(args.out_dir / "region_manifest.csv", region_records)
    print(
        f"development_images={len(selected_names)} boxes={len(box_metadata)} "
        f"region_crops={len(region_records)} test_images_encoded=0",
        flush=True,
    )

    device = choose_device(args.device)
    model, preprocess = openai_clip.load(protocol["model"], device=device)
    model.eval()
    text_features = encode_style_text(
        model,
        list(protocol["style_prompts"]),
        device,
    )
    region_features = encode_regions(
        model,
        preprocess,
        region_records,
        args.image_dir,
        device,
        args.batch_size,
        float(protocol["crop_context"]),
    )
    if region_features.shape[0] != len(region_records):
        raise RuntimeError("Feature cardinality mismatch")
    if not np.isfinite(region_features).all():
        raise RuntimeError("Non-finite region features")
    np.savez_compressed(
        args.out_dir / "region_features.npz",
        features=region_features,
        text_features=text_features,
    )

    region_scores = region_features @ text_features.T
    per_box_rows = []
    image_box_rows: dict[str, list[dict[str, object]]] = defaultdict(list)
    for metadata in box_metadata:
        target = int(metadata["style_index"])
        official_index = int(metadata["official_record_index"])
        control_indices = list(metadata["control_record_indices"])
        official_margin = class_margin(region_scores[official_index], target)
        random_margins = [
            class_margin(region_scores[index], target) for index in control_indices
        ]
        overlaps = [
            float(region_records[index]["max_official_overlap"])
            for index in control_indices
        ]
        row = {
            "box_id": metadata["box_id"],
            "image_filename": metadata["image_filename"],
            "church_id": metadata["church_id"],
            "style_name": metadata["style_name"],
            "official_margin": official_margin,
            "random_margin_mean": float(np.mean(random_margins)),
            "paired_margin_delta": official_margin - float(np.mean(random_margins)),
            "official_zero_shot_correct": int(
                np.argmax(region_scores[official_index]) == target
            ),
            "random_zero_shot_correct_mean": float(
                np.mean(
                    [int(np.argmax(region_scores[index]) == target) for index in control_indices]
                )
            ),
            "max_control_overlap": max(overlaps),
            "controls_above_target_overlap": sum(
                overlap > target_overlap for overlap in overlaps
            ),
        }
        per_box_rows.append(row)
        image_box_rows[str(metadata["image_filename"])].append(row)
    write_csv(args.out_dir / "per_box_results.csv", per_box_rows)

    official_by_image = {}
    random_by_image: dict[str, list[np.ndarray]] = {}
    per_image_rows = []
    for filename in selected_names:
        matching_metadata = [
            item for item in box_metadata if item["image_filename"] == filename
        ]
        official_indices = [
            int(item["official_record_index"]) for item in matching_metadata
        ]
        official_feature = normalize_rows(
            region_features[official_indices].mean(axis=0, keepdims=True)
        )[0]
        random_features = []
        for control_set in range(random_per_box):
            control_indices = [
                int(item["control_record_indices"][control_set])
                for item in matching_metadata
            ]
            random_features.append(
                normalize_rows(
                    region_features[control_indices].mean(axis=0, keepdims=True)
                )[0]
            )
        official_by_image[filename] = official_feature
        random_by_image[filename] = random_features
        rows = image_box_rows[filename]
        style_name = str(rows[0]["style_name"])
        target = STYLE_TO_INDEX[style_name]
        official_scores = official_feature @ text_features.T
        random_score_sets = [
            feature @ text_features.T for feature in random_features
        ]
        random_margins = [
            class_margin(scores, target) for scores in random_score_sets
        ]
        per_image_rows.append(
            {
                "image_filename": filename,
                "church_id": church_id(filename),
                "style_name": style_name,
                "box_count": len(rows),
                "official_margin_mean_over_boxes": float(
                    np.mean([float(row["official_margin"]) for row in rows])
                ),
                "random_margin_mean_over_boxes": float(
                    np.mean([float(row["random_margin_mean"]) for row in rows])
                ),
                "paired_margin_delta": float(
                    np.mean([float(row["paired_margin_delta"]) for row in rows])
                ),
                "official_aggregate_margin": class_margin(official_scores, target),
                "random_aggregate_margin": float(np.mean(random_margins)),
                "aggregate_margin_delta": class_margin(official_scores, target)
                - float(np.mean(random_margins)),
                "official_aggregate_zero_shot_correct": int(
                    np.argmax(official_scores) == target
                ),
                "random_aggregate_zero_shot_correct_mean": float(
                    np.mean(
                        [
                            int(np.argmax(scores) == target)
                            for scores in random_score_sets
                        ]
                    )
                ),
            }
        )
    write_csv(args.out_dir / "per_image_results.csv", per_image_rows)

    image_deltas = np.array(
        [float(row["paired_margin_delta"]) for row in per_image_rows]
    )
    bootstrap_rng = np.random.default_rng(int(protocol["paired_bootstrap_seed"]))
    bootstrap_repetitions = int(protocol["paired_bootstrap_repetitions"])
    bootstrap_means = np.empty(bootstrap_repetitions)
    for repetition in range(bootstrap_repetitions):
        indices = bootstrap_rng.integers(0, len(image_deltas), len(image_deltas))
        bootstrap_means[repetition] = image_deltas[indices].mean()
    margin_ci = percentile_interval(bootstrap_means)

    filenames = [str(row["image_filename"]) for row in per_image_rows]
    labels = np.array(
        [STYLE_TO_INDEX[str(row["style_name"])] for row in per_image_rows],
        dtype=int,
    )
    official_image_features = np.stack([official_by_image[name] for name in filenames])
    random_image_feature_sets = [
        np.stack([random_by_image[name][control_set] for name in filenames])
        for control_set in range(random_per_box)
    ]
    cv = protocol["prototype_cv"]
    cv_rows = []
    paired_cv_deltas = []
    for repeat in range(int(cv["repeats"])):
        rng = random.Random(int(cv["seed"]) + repeat)
        folds = stratified_folds(labels, int(cv["folds"]), rng)
        for fold_index, test_indices in enumerate(folds):
            train_mask = np.ones(len(labels), dtype=bool)
            train_mask[test_indices] = False
            train_indices = np.flatnonzero(train_mask)
            official_predictions = prototype_predictions(
                official_image_features[train_indices],
                labels[train_indices],
                official_image_features[test_indices],
            )
            official_accuracy = float(
                (official_predictions == labels[test_indices]).mean()
            )
            official_balanced = balanced_accuracy(
                labels[test_indices], official_predictions
            )
            cv_rows.append(
                {
                    "repeat": repeat,
                    "fold": fold_index,
                    "branch": "official",
                    "control_set": -1,
                    "train_images": len(train_indices),
                    "test_images": len(test_indices),
                    "accuracy": official_accuracy,
                    "balanced_accuracy": official_balanced,
                }
            )
            random_balanced_values = []
            for control_set, features in enumerate(random_image_feature_sets):
                predictions = prototype_predictions(
                    features[train_indices],
                    labels[train_indices],
                    features[test_indices],
                )
                accuracy = float((predictions == labels[test_indices]).mean())
                balanced = balanced_accuracy(labels[test_indices], predictions)
                random_balanced_values.append(balanced)
                cv_rows.append(
                    {
                        "repeat": repeat,
                        "fold": fold_index,
                        "branch": "random",
                        "control_set": control_set,
                        "train_images": len(train_indices),
                        "test_images": len(test_indices),
                        "accuracy": accuracy,
                        "balanced_accuracy": balanced,
                    }
                )
            paired_cv_deltas.append(
                official_balanced - float(np.mean(random_balanced_values))
            )
    write_csv(args.out_dir / "prototype_cv_results.csv", cv_rows)

    per_style_deltas = {}
    for style_name in STYLE_NAMES:
        values = [
            float(row["paired_margin_delta"])
            for row in per_image_rows
            if row["style_name"] == style_name
        ]
        per_style_deltas[style_name] = {
            "images": len(values),
            "mean_paired_margin_delta": float(np.mean(values)),
        }
    positive_style_directions = sum(
        item["mean_paired_margin_delta"] > 0
        for item in per_style_deltas.values()
    )
    official_cv = [
        float(row["balanced_accuracy"])
        for row in cv_rows
        if row["branch"] == "official"
    ]
    random_cv = [
        float(row["balanced_accuracy"])
        for row in cv_rows
        if row["branch"] == "random"
    ]
    prototype_delta_pp = 100 * (float(np.mean(official_cv)) - float(np.mean(random_cv)))
    rule = protocol["go_rule"]
    checks = {
        "mean_margin_delta": float(image_deltas.mean())
        > float(rule["mean_image_level_margin_delta_greater_than"]),
        "bootstrap_ci_lower": margin_ci[0]
        > float(rule["paired_bootstrap_95ci_lower_greater_than"]),
        "positive_style_directions": positive_style_directions
        >= int(rule["positive_style_directions_at_least"]),
        "prototype_balanced_accuracy_delta": prototype_delta_pp
        >= float(rule["prototype_balanced_accuracy_delta_pp_at_least"]),
    }
    decision = "GO" if all(checks.values()) else "NO-GO"
    overlap_violations = sum(
        int(row["controls_above_target_overlap"]) for row in per_box_rows
    )
    summary = {
        "experiment_id": protocol["experiment_id"],
        "decision": decision,
        "checks": checks,
        "go_rule": rule,
        "data": {
            "development_images": len(selected_names),
            "development_churches": len(set(selected_churches)),
            "official_boxes": len(box_metadata),
            "random_controls": len(box_metadata) * random_per_box,
            "test_images_encoded": 0,
            "style_image_counts": dict(style_image_counts),
            "style_box_counts": dict(style_box_counts),
            "control_overlap_violations": overlap_violations,
        },
        "margin_probe": {
            "mean_image_level_paired_delta": float(image_deltas.mean()),
            "sd_image_level_paired_delta": float(image_deltas.std(ddof=1)),
            "paired_bootstrap_95ci": list(margin_ci),
            "positive_style_directions": positive_style_directions,
            "per_style": per_style_deltas,
        },
        "prototype_cv": {
            "official_mean_balanced_accuracy": float(np.mean(official_cv)),
            "random_mean_balanced_accuracy": float(np.mean(random_cv)),
            "paired_delta_percentage_points": prototype_delta_pp,
            "paired_fold_delta_sd_percentage_points": 100
            * float(np.std(paired_cv_deltas, ddof=1)),
        },
        "integrity": {
            "parts_sha256": sha256(args.parts),
            "protocol_sha256": sha256(args.protocol),
            "model": protocol["model"],
            "device": str(device),
        },
        "interpretation_boundary": protocol["interpretation_boundary"],
    }
    (args.out_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# WikiChurches Box-vs-Random regional-information probe",
        "",
        f"Predeclared decision: **{decision}**.",
        "",
        "Only canonical train+val annotated images were encoded. Test images "
        "were used only as a filename exclusion set; encoded test images: 0.",
        "",
        "## Data",
        "",
        f"- Images/churches: {len(selected_names)}/{len(set(selected_churches))}",
        f"- Official boxes: {len(box_metadata)}",
        f"- Matched random controls: {len(box_metadata) * random_per_box}",
        f"- Controls above target official-overlap threshold: {overlap_violations}",
        "",
        "## Primary paired result",
        "",
        f"- Mean image-level margin delta: {image_deltas.mean():+.5f}",
        f"- Paired bootstrap 95% CI: [{margin_ci[0]:+.5f}, {margin_ci[1]:+.5f}]",
        f"- Positive style directions: {positive_style_directions}/4",
        "",
        "| Style | Images | Mean paired margin Δ |",
        "|---|---:|---:|",
    ]
    for style_name in STYLE_NAMES:
        item = per_style_deltas[style_name]
        lines.append(
            f"| {style_name} | {item['images']} | "
            f"{item['mean_paired_margin_delta']:+.5f} |"
        )
    lines.extend(
        [
            "",
            "## Church-disjoint prototype CV",
            "",
            f"- Official-box balanced accuracy: {np.mean(official_cv) * 100:.2f}%",
            f"- Random-region balanced accuracy: {np.mean(random_cv) * 100:.2f}%",
            f"- Paired delta: {prototype_delta_pp:+.2f} percentage points",
            "",
            "## Decision checks",
            "",
        ]
    )
    for name, passed in checks.items():
        lines.append(f"- {name}: {'PASS' if passed else 'FAIL'}")
    lines.extend(
        [
            "",
            "This probe tests whether selected official regions carry more "
            "style information than area/aspect-matched same-image controls. "
            "It is not an end-to-end few-shot result and does not establish "
            "that unannotated regions are negatives.",
        ]
    )
    (args.out_dir / "README.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
