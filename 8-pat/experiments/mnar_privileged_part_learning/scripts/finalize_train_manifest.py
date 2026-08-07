#!/usr/bin/env python3
"""Freeze train selection mechanisms after CLIP features are available."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path

import numpy as np


EXPERIMENT_ID = "PAT-C-260728-001"
MECHANISMS = ("MCAR", "MAR_X", "MNAR_Z", "SI_HARD")
SEEDS = (1307, 2607, 5207)


def stable_uint64(*items: object) -> int:
    payload = "\x1f".join(str(item) for item in items)
    return int.from_bytes(hashlib.sha256(payload.encode()).digest()[:8], "big")


def zscore(values: np.ndarray) -> np.ndarray:
    std = float(values.std())
    return (values - float(values.mean())) / max(std, 1e-8)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def weighted_sample(
    row_indices: np.ndarray,
    log_weights: np.ndarray,
    count: int,
    seed: int,
) -> set[int]:
    rng = np.random.default_rng(seed)
    # Efraimidis-Spirakis exponential-race form: smallest -log(U)/w wins.
    weights = np.exp(log_weights - np.max(log_weights))
    keys = -np.log(np.clip(rng.random(len(row_indices)), 1e-12, 1.0)) / np.clip(
        weights, 1e-12, None
    )
    order = np.lexsort((row_indices, keys))
    return set(int(value) for value in row_indices[order[:count]])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-manifest", type=Path, required=True)
    parser.add_argument("--features", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = [
        json.loads(line)
        for line in args.base_manifest.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    arrays = np.load(args.features)
    global_features = arrays["global_features"].astype(np.float32)
    if len(rows) != len(global_features):
        raise RuntimeError("Manifest/feature row mismatch.")

    grouped: dict[int, list[int]] = defaultdict(list)
    for row in rows:
        grouped[int(row["class_index"])].append(int(row["row_index"]))

    prototypicality = np.zeros(len(rows), dtype=np.float32)
    visibility = np.zeros(len(rows), dtype=np.float32)
    for class_rows in grouped.values():
        indices = np.asarray(class_rows, dtype=np.int64)
        centroid = global_features[indices].mean(axis=0)
        prototypicality[indices] = -np.square(
            global_features[indices] - centroid
        ).sum(axis=1)
        areas = np.asarray(
            [rows[index]["mask_area_fraction"] for index in indices], dtype=np.float32
        )
        counts = np.asarray(
            [rows[index]["visible_part_count"] for index in indices], dtype=np.float32
        )
        visibility[indices] = 0.5 * zscore(np.log(areas + 1e-6)) + 0.5 * zscore(
            counts
        )

    selected: dict[tuple[str, int], set[int]] = {}
    for mechanism in MECHANISMS:
        for seed in SEEDS:
            chosen: set[int] = set()
            for class_index, class_rows in sorted(grouped.items()):
                indices = np.asarray(class_rows, dtype=np.int64)
                count = min(
                    len(indices),
                    max(4, math.floor(0.2 * len(indices) + 0.5)),
                )
                local_proto = zscore(prototypicality[indices])
                local_visibility = zscore(visibility[indices])
                stream_seed = stable_uint64(
                    EXPERIMENT_ID, mechanism, seed, class_index
                )
                if mechanism == "MCAR":
                    picked = weighted_sample(
                        indices, np.zeros(len(indices)), count, stream_seed
                    )
                elif mechanism == "MAR_X":
                    picked = weighted_sample(
                        indices, 2.0 * local_proto, count, stream_seed
                    )
                elif mechanism == "MNAR_Z":
                    picked = weighted_sample(
                        indices, 2.0 * local_visibility, count, stream_seed
                    )
                else:
                    combined = 0.5 * local_proto + 0.5 * local_visibility
                    order = np.lexsort((indices, -combined))
                    picked = set(int(value) for value in indices[order[:count]])
                chosen.update(picked)
            selected[(mechanism, seed)] = chosen

    for row in rows:
        index = int(row["row_index"])
        row["global_prototypicality"] = float(prototypicality[index])
        row["mask_visibility_score"] = float(visibility[index])
        row["part_annotation_selected"] = {
            mechanism: {
                str(seed): index in selected[(mechanism, seed)] for seed in SEEDS
            }
            for mechanism in MECHANISMS
        }

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "train_manifest_frozen.jsonl"
    with output.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")
    counts = {
        mechanism: {
            str(seed): len(selected[(mechanism, seed)]) for seed in SEEDS
        }
        for mechanism in MECHANISMS
    }
    summary = {
        "experiment_id": EXPERIMENT_ID,
        "manifest_sha256": sha256_file(output),
        "base_manifest_sha256": sha256_file(args.base_manifest),
        "feature_file_sha256": sha256_file(args.features),
        "rows": len(rows),
        "selection_counts": counts,
        "test_images_decoded_or_encoded": 0,
    }
    (args.output_dir / "train_manifest_frozen_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
