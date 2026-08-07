#!/usr/bin/env python3
"""Freeze one-keypoint-image-per-class CUB selections for PAT-D-260728-003."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


MECHANISMS = (
    "MCAR_1",
    "MAR_X_ATYPICAL",
    "MNAR_Z_INCOMPLETE",
    "SI_POSE",
)
HEAD_PARTS = (1, 4, 5, 6, 9, 10, 14)
TAIL_PART = 13


def pose_score(row):
    points = np.asarray(row["keypoints"], dtype=np.float64)
    visible = points[:, 2] > 0
    head_visible = [index for index in HEAD_PARTS if visible[index]]
    if not visible[TAIL_PART] or not head_visible:
        return np.nan
    visible_x = points[visible, 0]
    span = float(visible_x.max() - visible_x.min())
    if span <= 1e-12:
        return np.nan
    head_x = float(points[head_visible, 0].mean())
    return (head_x - float(points[TAIL_PART, 0])) / span


def deterministic_argmin(candidates, scores, image_ids):
    order = np.lexsort((image_ids, scores))
    return int(candidates[order[0]])


def deterministic_pose_max(candidates, scores, image_ids):
    valid = np.isfinite(scores)
    if valid.any():
        eligible = np.flatnonzero(valid)
        order = np.lexsort((image_ids[eligible], -scores[eligible]))
        return int(candidates[eligible[order[0]]])
    return int(candidates[np.argmin(image_ids)])


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--base-scores", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    rows = [json.loads(line) for line in args.manifest.read_text().splitlines()]
    if any(
        row["split"] != "train" or row["source_split"] != "official_train"
        for row in rows
    ):
        raise RuntimeError("PAT-D-260728-003 may inspect official train only")
    labels = np.asarray([row["class_index"] for row in rows])
    folds = np.asarray([row["fold"] for row in rows])
    image_ids = np.asarray([row["image_id"] for row in rows])
    source = np.load(args.base_scores)
    typicality = source["typicality"].astype(np.float64)
    completeness = source["completeness"].astype(np.float64)
    pose = np.asarray([pose_score(row) for row in rows], dtype=np.float64)
    selection = {
        mechanism: np.zeros((5, len(rows)), dtype=np.bool_)
        for mechanism in MECHANISMS
    }
    seed = int(protocol["screening"]["seed"])

    for fold in range(5):
        for class_index in range(200):
            candidates = np.flatnonzero(
                (labels == class_index) & (folds != fold)
            )
            if len(candidates) != 8:
                raise RuntimeError(
                    f"Expected 8 train candidates, got {len(candidates)}"
                )
            rng = np.random.default_rng(
                seed + 10000 * fold + 100 * class_index
            )
            chosen = {
                "MCAR_1": int(rng.choice(candidates)),
                "MAR_X_ATYPICAL": deterministic_argmin(
                    candidates,
                    typicality[fold, candidates],
                    image_ids[candidates],
                ),
                "MNAR_Z_INCOMPLETE": deterministic_argmin(
                    candidates,
                    completeness[candidates],
                    image_ids[candidates],
                ),
                "SI_POSE": deterministic_pose_max(
                    candidates,
                    pose[candidates],
                    image_ids[candidates],
                ),
            }
            for mechanism, index in chosen.items():
                selection[mechanism][fold, index] = True

    for mechanism, values in selection.items():
        for fold in range(5):
            selected = values[fold]
            if selected.sum() != 200:
                raise RuntimeError(
                    f"{mechanism} fold {fold}: expected 200 selected"
                )
            per_class = np.bincount(labels[selected], minlength=200)
            if set(per_class.tolist()) != {1}:
                raise RuntimeError(
                    f"{mechanism} fold {fold}: class budget mismatch"
                )
            if np.any(selected & (folds == fold)):
                raise RuntimeError(
                    f"{mechanism} fold {fold}: selected an OOF image"
                )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "cub_severe_missingness_selections.npz"
    np.savez_compressed(
        output,
        **{f"selected_{key}": value for key, value in selection.items()},
        typicality=typicality.astype(np.float32),
        completeness=completeness.astype(np.float32),
        pose=pose.astype(np.float32),
    )
    summary = {
        "experiment_id": protocol["experiment_id"],
        "selection_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "screening_seed": seed,
        "images": len(rows),
        "official_test_images_decoded_or_encoded": 0,
        "pose_score_valid_fraction": float(np.isfinite(pose).mean()),
        "mechanisms": {},
    }
    for mechanism, values in selection.items():
        metrics = {}
        for metric_name, metric_values in (
            ("typicality", typicality),
            ("completeness", np.broadcast_to(completeness, typicality.shape)),
            ("pose", np.broadcast_to(pose, typicality.shape)),
        ):
            selected_values, unselected_values = [], []
            for fold in range(5):
                train = folds != fold
                chosen = values[fold]
                if metric_name == "typicality":
                    fold_values = metric_values[fold]
                else:
                    fold_values = metric_values[fold]
                selected_values.extend(fold_values[chosen].tolist())
                unselected_values.extend(
                    fold_values[train & ~chosen].tolist()
                )
            selected_values = np.asarray(selected_values, dtype=np.float64)
            unselected_values = np.asarray(unselected_values, dtype=np.float64)
            metrics[f"mean_{metric_name}_selected"] = float(
                np.nanmean(selected_values)
            )
            metrics[f"mean_{metric_name}_unselected"] = float(
                np.nanmean(unselected_values)
            )
            metrics[f"{metric_name}_valid_fraction_selected"] = float(
                np.isfinite(selected_values).mean()
            )
        summary["mechanisms"][mechanism] = {
            "selected_per_fold": 200,
            "selected_per_class_per_fold": 1,
            **metrics,
        }
    summary_path = (
        args.output_dir / "cub_severe_missingness_selection_summary.json"
    )
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

