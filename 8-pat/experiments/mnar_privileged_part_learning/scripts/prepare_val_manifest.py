#!/usr/bin/env python3
"""Prepare validation rows only after train OOF hyperparameters are frozen."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import shutil
import zipfile
from pathlib import Path

import numpy as np
import torch
from pycocotools.coco import COCO
from torchvision.transforms import InterpolationMode
from torchvision.transforms import functional as TF


PARTS = ("Head", "Body", "Foot", "Tail")


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
        tensor, 224, interpolation=InterpolationMode.NEAREST, antialias=False
    )
    tensor = TF.center_crop(tensor, [224, 224])
    return torch.nn.functional.interpolate(
        tensor[None, ...], size=(14, 14), mode="area"
    )[0, 0]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--train-summary", type=Path, required=True)
    parser.add_argument("--selected-hparams", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "--archive",
        type=Path,
        help="Optional official ZIP; extract only the selected validation images.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.selected_hparams.is_file():
        raise RuntimeError("Train-only hyperparameters must be frozen first.")
    selected_hparams = json.loads(
        args.selected_hparams.read_text(encoding="utf-8")
    )
    if selected_hparams.get("validation_read_before_selection") is not False:
        raise RuntimeError("Invalid selection audit field.")
    train_summary = json.loads(args.train_summary.read_text(encoding="utf-8"))
    selected_classes = train_summary["selected_classes"]
    class_index = {
        synset: index for index, synset in enumerate(selected_classes)
    }

    annotation_path = args.dataset_root / "val.json"
    image_root = args.dataset_root / "val"
    raw = json.loads(annotation_path.read_text(encoding="utf-8"))
    coco = COCO()
    coco.dataset = repair_four_point_polygons(raw)
    coco.createIndex()
    category_ids = {
        category_id
        for category_id, category in coco.cats.items()
        if str(category.get("supercategory", "")).strip().lower() == "quadruped"
    }
    part_by_category = {
        category_id: canonical_part(coco.cats[category_id])
        for category_id in category_ids
    }
    if any(value is None for value in part_by_category.values()):
        raise RuntimeError("Unrecognized Quadruped part name in val.json.")

    selected_images = []
    for image_id, image in coco.imgs.items():
        synset = Path(str(image["file_name"])).name.split("_", 1)[0]
        if synset not in class_index:
            continue
        anns = [
            ann
            for ann in coco.imgToAnns.get(image_id, [])
            if ann.get("area", 0) > 0
            and ann.get("iscrowd", 0) != 1
            and ann["category_id"] in category_ids
        ]
        if anns:
            selected_images.append(
                {
                    "image_id": int(image_id),
                    "file_name": str(image["file_name"]),
                    "synset": synset,
                    "width": int(image["width"]),
                    "height": int(image["height"]),
                }
            )
    selected_images.sort(
        key=lambda item: (class_index[item["synset"]], item["image_id"])
    )

    if args.archive:
        image_root.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(args.archive) as archive:
            for item in selected_images:
                relative = Path(item["file_name"])
                if relative.is_absolute() or ".." in relative.parts:
                    raise RuntimeError(f"Unsafe archive path: {relative}")
                destination = image_root / relative
                if destination.is_file():
                    continue
                destination.parent.mkdir(parents=True, exist_ok=True)
                member = f"PartImageNet/images/val/{relative.as_posix()}"
                with archive.open(member) as source, destination.open("wb") as target:
                    shutil.copyfileobj(source, target)

    masks = np.zeros(
        (len(selected_images), len(PARTS), 14, 14), dtype=np.float16
    )
    rows = []
    for row_index, item in enumerate(selected_images):
        native_masks = {
            part: np.zeros((item["height"], item["width"]), dtype=np.uint8)
            for part in PARTS
        }
        for ann in coco.imgToAnns[item["image_id"]]:
            if (
                ann.get("area", 0) > 0
                and ann.get("iscrowd", 0) != 1
                and ann["category_id"] in category_ids
            ):
                native_masks[part_by_category[ann["category_id"]]] |= (
                    coco.annToMask(ann).astype(np.uint8)
                )
        for part_index, part in enumerate(PARTS):
            masks[row_index, part_index] = (
                mask_to_clip_grid(native_masks[part]).numpy().astype(np.float16)
            )
        image_path = image_root / item["file_name"]
        if not image_path.is_file():
            raise FileNotFoundError(image_path)
        rows.append(
            {
                "row_index": row_index,
                "image_id": item["image_id"],
                "split": "val",
                "file_name": item["file_name"],
                "relative_path": str(Path("val") / item["file_name"]),
                "synset": item["synset"],
                "class_index": class_index[item["synset"]],
                "width": item["width"],
                "height": item["height"],
            }
        )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest = args.output_dir / "val_manifest_frozen.jsonl"
    with manifest.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")
    np.savez_compressed(
        args.output_dir / "val_part_targets.npz",
        masks=masks,
        parts=np.asarray(PARTS),
    )
    summary = {
        "images": len(rows),
        "selected_classes": selected_classes,
        "manifest_sha256": sha256_file(manifest),
        "selected_hparams_sha256": sha256_file(args.selected_hparams),
        "validation_opened_after_train_selection": True,
        "test_images_decoded": 0,
    }
    (args.output_dir / "val_manifest_frozen_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
