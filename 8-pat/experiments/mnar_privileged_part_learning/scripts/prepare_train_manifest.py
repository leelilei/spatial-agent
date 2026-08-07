#!/usr/bin/env python3
"""Create the train-only PartImageNet pilot manifest and 14x14 part targets.

This program is deliberately incapable of opening val.json or test.json.  It
must run before any validation image is decoded.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import shutil
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import torch
from pycocotools.coco import COCO
from torchvision.transforms import InterpolationMode
from torchvision.transforms import functional as TF


EXPERIMENT_ID = "PAT-C-260728-001"
PARTS = ("Head", "Body", "Foot", "Tail")


def stable_digest(*items: object) -> str:
    payload = "\x1f".join(str(item) for item in items)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_part(category: dict) -> str | None:
    name = str(category.get("name", "")).strip().lower()
    for part in PARTS:
        if name == part.lower() or name.endswith(part.lower()):
            return part
    return None


def repair_four_point_polygons(dataset: dict) -> dict:
    repaired = copy.deepcopy(dataset)
    for ann in repaired["annotations"]:
        if ann.get("area", 0) <= 0 or ann.get("iscrowd", 0) == 1:
            continue
        segments = ann.get("segmentation", [])
        if not isinstance(segments, list):
            continue
        for index, polygon in enumerate(segments):
            if len(polygon) == 4:
                x1, y1, width, height = ann["bbox"]
                x2, y2 = x1 + width, y1 + height
                segments[index] = [x1, y1, x1, y2, x2, y2, x2, y1]
    return repaired


def mask_to_clip_grid(mask: np.ndarray) -> torch.Tensor:
    tensor = torch.from_numpy(mask.astype(np.float32, copy=False))[None, ...]
    tensor = TF.resize(
        tensor,
        224,
        interpolation=InterpolationMode.NEAREST,
        antialias=False,
    )
    tensor = TF.center_crop(tensor, [224, 224])
    return torch.nn.functional.interpolate(
        tensor[None, ...], size=(14, 14), mode="area"
    )[0, 0]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "--archive",
        type=Path,
        help="Optional official ZIP; extract only the selected train images.",
    )
    parser.add_argument("--class-count", type=int, default=20)
    parser.add_argument("--max-per-class", type=int, default=80)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    annotation_path = args.dataset_root / "train.json"
    image_root = args.dataset_root / "train"
    if annotation_path.name != "train.json":
        raise RuntimeError("Only train.json is permitted at this stage.")
    if not annotation_path.is_file():
        raise FileNotFoundError(annotation_path)
    if not args.archive and not image_root.is_dir():
        raise FileNotFoundError(image_root)

    raw = json.loads(annotation_path.read_text(encoding="utf-8"))
    coco = COCO()
    coco.dataset = repair_four_point_polygons(raw)
    coco.createIndex()

    quadruped_category_ids = {
        category_id
        for category_id, category in coco.cats.items()
        if str(category.get("supercategory", "")).strip().lower() == "quadruped"
    }
    part_by_category = {
        category_id: canonical_part(category)
        for category_id, category in coco.cats.items()
        if category_id in quadruped_category_ids
    }
    missing_parts = [
        category_id
        for category_id, part in part_by_category.items()
        if part is None
    ]
    if missing_parts:
        raise RuntimeError(f"Unrecognized Quadruped categories: {missing_parts}")

    candidates: list[dict] = []
    for image_id, image in coco.imgs.items():
        anns = [
            ann
            for ann in coco.imgToAnns.get(image_id, [])
            if ann.get("area", 0) > 0
            and ann.get("iscrowd", 0) != 1
            and ann["category_id"] in quadruped_category_ids
        ]
        if not anns:
            continue
        file_name = str(image["file_name"])
        synset = Path(file_name).name.split("_", 1)[0]
        candidates.append(
            {
                "image_id": int(image_id),
                "file_name": file_name,
                "synset": synset,
                "width": int(image["width"]),
                "height": int(image["height"]),
            }
        )

    counts = Counter(item["synset"] for item in candidates)
    selected_classes = [
        synset
        for synset, _ in sorted(
            counts.items(), key=lambda pair: (-pair[1], pair[0])
        )[: args.class_count]
    ]
    class_index = {synset: index for index, synset in enumerate(selected_classes)}
    grouped: dict[str, list[dict]] = defaultdict(list)
    for item in candidates:
        if item["synset"] in class_index:
            grouped[item["synset"]].append(item)

    selected: list[dict] = []
    for synset in selected_classes:
        ordered = sorted(
            grouped[synset],
            key=lambda item: stable_digest(
                EXPERIMENT_ID, "train-cap", item["image_id"]
            ),
        )
        selected.extend(ordered[: args.max_per_class])
    selected.sort(key=lambda item: (class_index[item["synset"]], item["image_id"]))

    if args.archive:
        image_root.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(args.archive) as archive:
            for item in selected:
                relative = Path(item["file_name"])
                if relative.is_absolute() or ".." in relative.parts:
                    raise RuntimeError(f"Unsafe archive path: {relative}")
                destination = image_root / relative
                if destination.is_file():
                    continue
                destination.parent.mkdir(parents=True, exist_ok=True)
                member = f"PartImageNet/images/train/{relative.as_posix()}"
                with archive.open(member) as source, destination.open("wb") as target:
                    shutil.copyfileobj(source, target)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    masks = np.zeros((len(selected), len(PARTS), 14, 14), dtype=np.float16)
    area_fraction = np.zeros(len(selected), dtype=np.float32)
    visible_count = np.zeros(len(selected), dtype=np.int8)
    rows: list[dict] = []

    for row_index, item in enumerate(selected):
        native_masks = {
            part: np.zeros((item["height"], item["width"]), dtype=np.uint8)
            for part in PARTS
        }
        for ann in coco.imgToAnns[item["image_id"]]:
            if (
                ann.get("area", 0) <= 0
                or ann.get("iscrowd", 0) == 1
                or ann["category_id"] not in quadruped_category_ids
            ):
                continue
            part = part_by_category[ann["category_id"]]
            native_masks[part] |= coco.annToMask(ann).astype(np.uint8)

        union = np.zeros_like(next(iter(native_masks.values())))
        for part_index, part in enumerate(PARTS):
            union |= native_masks[part]
            masks[row_index, part_index] = (
                mask_to_clip_grid(native_masks[part]).numpy().astype(np.float16)
            )
        area_fraction[row_index] = float(union.mean())
        visible_count[row_index] = sum(mask.any() for mask in native_masks.values())

        image_path = image_root / item["file_name"]
        if not image_path.is_file():
            raise FileNotFoundError(image_path)
        fold_key = stable_digest(EXPERIMENT_ID, item["image_id"], 1307)
        rows.append(
            {
                "row_index": row_index,
                "image_id": item["image_id"],
                "split": "train",
                "file_name": item["file_name"],
                "relative_path": str(Path("train") / item["file_name"]),
                "synset": item["synset"],
                "class_index": class_index[item["synset"]],
                "width": item["width"],
                "height": item["height"],
                "fold_sort_key": fold_key,
                "mask_area_fraction": float(area_fraction[row_index]),
                "visible_part_count": int(visible_count[row_index]),
            }
        )

    for synset in selected_classes:
        class_rows = [row for row in rows if row["synset"] == synset]
        class_rows.sort(key=lambda row: row["fold_sort_key"])
        for rank, row in enumerate(class_rows):
            row["fold"] = rank % 5
            del row["fold_sort_key"]

    manifest_path = args.output_dir / "train_manifest_base.jsonl"
    with manifest_path.open("w", encoding="utf-8") as handle:
        for row in sorted(rows, key=lambda value: value["row_index"]):
            handle.write(json.dumps(row, sort_keys=True) + "\n")
    np.savez_compressed(
        args.output_dir / "train_part_targets.npz",
        masks=masks,
        mask_area_fraction=area_fraction,
        visible_part_count=visible_count,
        parts=np.asarray(PARTS),
    )
    summary = {
        "experiment_id": EXPERIMENT_ID,
        "source_annotation": str(annotation_path),
        "source_annotation_sha256": sha256_file(annotation_path),
        "supercategory": "Quadruped",
        "selected_classes": selected_classes,
        "source_counts": {key: counts[key] for key in selected_classes},
        "retained_counts": dict(
            sorted(Counter(row["synset"] for row in rows).items())
        ),
        "images": len(rows),
        "part_names": PARTS,
        "manifest_sha256": sha256_file(manifest_path),
        "test_images_decoded": 0,
    }
    summary_path = args.output_dir / "train_manifest_base_summary.json"
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
