#!/usr/bin/env python3
"""Build positive-only WikiChurches dense-token anchors and local logits."""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path

import torch
import torch.nn.functional as F
from PIL import Image, ImageOps
from torchvision import transforms


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
CLIP_MEAN = (0.48145466, 0.4578275, 0.40821073)
CLIP_STD = (0.26862954, 0.26130258, 0.27577711)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--region-manifest", type=Path, required=True)
    parser.add_argument("--image-dir", type=Path, required=True)
    parser.add_argument("--labels-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--split", choices=("val", "test"), required=True)
    parser.add_argument("--out-file", type=Path, required=True)
    parser.add_argument("--anchor-bank-file", type=Path)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--batch-size", type=int, default=8)
    return parser.parse_args()


def read_split(path: Path) -> list[tuple[str, str]]:
    rows = []
    seen = set()
    with path.open(encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            fields = line.split()
            if len(fields) != 2:
                raise ValueError(f"{path}:{line_number}: malformed split row")
            filename, style_id = fields
            if filename in seen or style_id not in STYLE_ID_TO_NAME:
                raise ValueError(f"{path}:{line_number}: invalid split row")
            seen.add(filename)
            rows.append((filename, style_id))
    return rows


def dense_visual_tokens(
    visual: torch.nn.Module,
    images: torch.Tensor,
) -> torch.Tensor:
    dtype = visual.conv1.weight.dtype
    x = visual.conv1(images.to(dtype))
    batch, width, grid_h, grid_w = x.shape
    x = x.reshape(batch, width, grid_h * grid_w).permute(0, 2, 1)
    class_token = visual.class_embedding.to(dtype)
    class_tokens = class_token + torch.zeros(
        batch, 1, width, dtype=dtype, device=x.device
    )
    x = torch.cat((class_tokens, x), dim=1)

    positional = visual.positional_embedding
    original_grid = int(math.sqrt(positional.shape[0] - 1))
    if original_grid * original_grid != positional.shape[0] - 1:
        raise RuntimeError("CLIP patch positional embedding is not square")
    class_position = positional[:1]
    patch_position = positional[1:].reshape(
        original_grid, original_grid, width
    )
    patch_position = patch_position.permute(2, 0, 1).unsqueeze(0).float()
    patch_position = F.interpolate(
        patch_position,
        size=(grid_h, grid_w),
        mode="bicubic",
        align_corners=False,
    )
    patch_position = patch_position.squeeze(0).permute(1, 2, 0).reshape(
        grid_h * grid_w, width
    )
    interpolated_position = torch.cat(
        (class_position.float(), patch_position),
        dim=0,
    ).to(device=x.device, dtype=dtype)
    x = x + interpolated_position
    x = visual.ln_pre(x)
    x = x.permute(1, 0, 2)
    x = visual.transformer(x)
    x = x.permute(1, 0, 2)
    x = visual.ln_post(x)
    if visual.proj is not None:
        x = x @ visual.proj
    patch_tokens = x[:, 1:, :].float()
    return patch_tokens / patch_tokens.norm(dim=-1, keepdim=True).clamp_min(1e-12)


def encode_images(
    filenames: list[str],
    image_dir: Path,
    model: torch.nn.Module,
    resolution: int,
    batch_size: int,
    device: torch.device,
) -> tuple[torch.Tensor, int]:
    transform = transforms.Compose(
        [
            transforms.Resize(
                (resolution, resolution),
                interpolation=transforms.InterpolationMode.BICUBIC,
            ),
            transforms.ToTensor(),
            transforms.Normalize(mean=CLIP_MEAN, std=CLIP_STD),
        ]
    )
    outputs = []
    with torch.inference_mode():
        for start in range(0, len(filenames), batch_size):
            batch_names = filenames[start : start + batch_size]
            images = torch.stack(
                [
                    transform(
                        ImageOps.exif_transpose(
                            Image.open(image_dir / filename)
                        ).convert("RGB")
                    )
                    for filename in batch_names
                ]
            ).to(device)
            tokens = dense_visual_tokens(model.visual, images)
            outputs.append(tokens.cpu())
            print(
                f"dense_encoded={min(start + batch_size, len(filenames))}/"
                f"{len(filenames)}",
                flush=True,
            )
    concatenated = torch.cat(outputs)
    grid = int(math.sqrt(concatenated.shape[1]))
    if grid * grid != concatenated.shape[1]:
        raise RuntimeError("Dense token count is not square")
    return concatenated, grid


def expanded_box(
    row: dict[str, str],
    context: float,
) -> tuple[float, float, float, float]:
    left = float(row["left"])
    top = float(row["top"])
    right = float(row["right"])
    bottom = float(row["bottom"])
    dx = (right - left) * context
    dy = (bottom - top) * context
    return (
        max(0.0, left - dx),
        max(0.0, top - dy),
        min(1.0, right + dx),
        min(1.0, bottom + dy),
    )


def pool_box_tokens(
    tokens: torch.Tensor,
    grid: int,
    box: tuple[float, float, float, float],
) -> torch.Tensor:
    left, top, right, bottom = box
    xs1 = torch.arange(grid, dtype=torch.float32) / grid
    ys1 = torch.arange(grid, dtype=torch.float32) / grid
    xs2 = (torch.arange(grid, dtype=torch.float32) + 1) / grid
    ys2 = (torch.arange(grid, dtype=torch.float32) + 1) / grid
    intersection_width = (
        torch.minimum(xs2, torch.tensor(right))
        - torch.maximum(xs1, torch.tensor(left))
    ).clamp_min(0)
    intersection_height = (
        torch.minimum(ys2, torch.tensor(bottom))
        - torch.maximum(ys1, torch.tensor(top))
    ).clamp_min(0)
    weights = (
        intersection_height[:, None] * intersection_width[None, :]
    ).reshape(-1)
    if float(weights.sum()) <= 0:
        raise RuntimeError(f"Box does not overlap dense grid: {box}")
    pooled = (tokens * weights[:, None]).sum(dim=0) / weights.sum()
    return pooled / pooled.norm().clamp_min(1e-12)


def farthest_point_indices(
    features: torch.Tensor,
    count: int,
) -> torch.Tensor:
    if len(features) < count:
        raise RuntimeError(
            f"Need {count} anchors but class has only {len(features)}"
        )
    features = features / features.norm(dim=-1, keepdim=True).clamp_min(1e-12)
    mean = features.mean(dim=0)
    mean = mean / mean.norm().clamp_min(1e-12)
    first = int(torch.argmin(features @ mean))
    selected = [first]
    minimum_distance = 1.0 - features @ features[first]
    for _ in range(1, count):
        minimum_distance[selected] = -1
        next_index = int(torch.argmax(minimum_distance))
        selected.append(next_index)
        distance = 1.0 - features @ features[next_index]
        minimum_distance = torch.minimum(minimum_distance, distance)
    return torch.tensor(selected, dtype=torch.long)


def build_anchor_banks(
    manifest_rows: list[dict[str, str]],
    train_tokens: torch.Tensor,
    train_filenames: list[str],
    grid: int,
    context: float,
    anchors_per_style: int,
) -> tuple[torch.Tensor, torch.Tensor, dict[str, object]]:
    filename_to_index = {
        filename: index for index, filename in enumerate(train_filenames)
    }
    official_by_style: dict[int, list[tuple[str, torch.Tensor]]] = defaultdict(list)
    random_by_set_and_style: dict[
        int, dict[int, list[tuple[str, torch.Tensor]]]
    ] = defaultdict(lambda: defaultdict(list))
    for row in manifest_rows:
        filename = row["image_filename"]
        if filename not in filename_to_index:
            continue
        style = STYLE_TO_INDEX[row["style_name"]]
        pooled = pool_box_tokens(
            train_tokens[filename_to_index[filename]],
            grid,
            expanded_box(row, context),
        )
        key = f"{row['box_id']}::{row['region_type']}::{row['control_index']}"
        if row["region_type"] == "official":
            official_by_style[style].append((key, pooled))
        else:
            control_set = int(row["control_index"])
            random_by_set_and_style[control_set][style].append((key, pooled))

    audit = {"official": {}, "random": {}}
    official_banks = []
    for style in range(len(STYLE_NAMES)):
        items = official_by_style[style]
        features = torch.stack([feature for _, feature in items])
        selected = farthest_point_indices(features, anchors_per_style)
        official_banks.append(features[selected])
        audit["official"][STYLE_NAMES[style]] = {
            "available": len(items),
            "selected_ids": [items[index][0] for index in selected.tolist()],
        }
    random_banks = []
    for control_set in sorted(random_by_set_and_style):
        per_style = []
        audit["random"][str(control_set)] = {}
        for style in range(len(STYLE_NAMES)):
            items = random_by_set_and_style[control_set][style]
            features = torch.stack([feature for _, feature in items])
            selected = farthest_point_indices(features, anchors_per_style)
            per_style.append(features[selected])
            audit["random"][str(control_set)][STYLE_NAMES[style]] = {
                "available": len(items),
                "selected_ids": [items[index][0] for index in selected.tolist()],
            }
        random_banks.append(torch.stack(per_style))
    return torch.stack(official_banks), torch.stack(random_banks), audit


def local_scores(
    query_tokens: torch.Tensor,
    bank: torch.Tensor,
    ratios: list[float],
    batch_size: int = 32,
) -> dict[str, torch.Tensor]:
    outputs = {str(ratio): [] for ratio in ratios}
    for start in range(0, len(query_tokens), batch_size):
        batch = query_tokens[start : start + batch_size]
        similarities = torch.einsum("bpd,cad->bpca", batch, bank)
        per_patch = similarities.max(dim=-1).values
        for ratio in ratios:
            count = max(1, int(round(batch.shape[1] * ratio)))
            score = per_patch.topk(count, dim=1).values.mean(dim=1)
            outputs[str(ratio)].append(score)
    return {key: torch.cat(values) for key, values in outputs.items()}


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
    query_rows = read_split(args.labels_dir / f"wc4_{args.split}.txt")
    train_names = {filename for filename, _ in train_rows}
    query_names = [filename for filename, _ in query_rows]
    if train_names & set(query_names):
        raise RuntimeError("Train/query image overlap")
    missing = [
        filename
        for filename in query_names
        if not (args.image_dir / filename).is_file()
    ]
    if missing:
        raise FileNotFoundError(f"Missing query images: {missing[:5]}")

    model, _ = openai_clip.load(protocol.get("model", "ViT-B/16"), device=device)
    model.eval()
    if args.anchor_bank_file is None:
        manifest_rows = list(
            csv.DictReader(args.region_manifest.open(encoding="utf-8"))
        )
        anchor_filenames = sorted(
            {
                row["image_filename"]
                for row in manifest_rows
                if row["image_filename"] in train_names
            }
        )
        anchor_tokens, grid = encode_images(
            anchor_filenames,
            args.image_dir,
            model,
            resolution,
            args.batch_size,
            device,
        )
        if grid != expected_grid:
            raise RuntimeError(f"Expected {expected_grid} grid, got {grid}")
        official_bank, random_banks, anchor_audit = build_anchor_banks(
            manifest_rows,
            anchor_tokens,
            anchor_filenames,
            grid,
            context,
            anchors_per_style,
        )
    else:
        saved = torch.load(args.anchor_bank_file, map_location="cpu")
        official_bank = saved["official_anchor_bank"]
        random_banks = saved["random_anchor_banks"]
        anchor_audit = saved["anchor_audit"]
        grid = int(saved["grid"])
        if grid != expected_grid:
            raise RuntimeError("Frozen anchor grid mismatch")

    query_tokens, query_grid = encode_images(
        query_names,
        args.image_dir,
        model,
        resolution,
        args.batch_size,
        device,
    )
    if query_grid != grid:
        raise RuntimeError("Anchor/query grid mismatch")
    official_scores = local_scores(query_tokens, official_bank, ratios)
    random_scores = {
        str(ratio): [] for ratio in ratios
    }
    for bank in random_banks:
        per_bank = local_scores(query_tokens, bank, ratios)
        for ratio in ratios:
            random_scores[str(ratio)].append(per_bank[str(ratio)])
    random_scores = {
        key: torch.stack(values) for key, values in random_scores.items()
    }
    labels = torch.tensor(
        [STYLE_TO_INDEX[STYLE_ID_TO_NAME[style_id]] for _, style_id in query_rows],
        dtype=torch.long,
    )
    output = {
        "experiment_id": protocol["experiment_id"],
        "split": args.split,
        "resolution": resolution,
        "grid": grid,
        "style_names": STYLE_NAMES,
        "image_names": query_names,
        "labels": labels,
        "topk_patch_ratios": ratios,
        "official_local_scores": official_scores,
        "random_local_scores": random_scores,
        "official_anchor_bank": official_bank,
        "random_anchor_banks": random_banks,
        "anchor_audit": anchor_audit,
        "test_images_encoded": len(query_names) if args.split == "test" else 0,
    }
    args.out_file.parent.mkdir(parents=True, exist_ok=True)
    torch.save(output, args.out_file)
    summary = {
        "split": args.split,
        "query_images": len(query_names),
        "test_images_encoded": output["test_images_encoded"],
        "resolution": resolution,
        "grid": grid,
        "official_bank_shape": list(official_bank.shape),
        "random_bank_shape": list(random_banks.shape),
        "style_counts": dict(
            Counter(STYLE_NAMES[int(label)] for label in labels)
        ),
    }
    args.out_file.with_suffix(".json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
