#!/usr/bin/env python3
"""Support-only deterministic view expansion screen."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from sklearn.svm import SVC

from sparse_anchor_utils import balanced_accuracy, class_recall, l2_normalize


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def class_bootstrap_interval(delta, seed=9526, draws=20000):
    rng = np.random.default_rng(seed)
    indices = rng.integers(0, len(delta), (draws, len(delta)))
    values = delta[indices].mean(axis=1) * 100.0
    return [float(x) for x in np.quantile(values, [0.025, 0.5, 0.975])]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-feature-dir", type=Path, required=True)
    parser.add_argument("--multiview-feature-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    labels = np.load(args.base_feature_dir / "labels.npy")
    folds = np.load(args.base_feature_dir / "folds.npy")
    image_ids = np.load(args.base_feature_dir / "image_ids.npy")
    views = l2_normalize(
        np.load(args.multiview_feature_dir / "multiview_cls.npy", mmap_mode="r")
    )
    arm_views = {
        "REFERENCE": (0,),
        "SUPPORT_STRETCH_FLIP": (0, 1),
        "SUPPORT_STRETCH_CENTER": (0, 2),
        "SUPPORT_ALL4": (0, 1, 2, 3),
    }
    predictions = {
        name: np.full(len(labels), -1, dtype=np.int64) for name in arm_views
    }
    for fold in range(5):
        train = np.flatnonzero(folds != fold)
        evaluate_on = np.flatnonzero(folds == fold)
        for name, selected_views in arm_views.items():
            train_x = views[train][:, selected_views].reshape(
                len(train) * len(selected_views), -1
            )
            train_y = np.repeat(labels[train], len(selected_views))
            classifier = SVC(C=3.0, kernel="rbf", gamma="scale").fit(
                train_x, train_y
            )
            predictions[name][evaluate_on] = classifier.predict(
                views[evaluate_on, 0]
            )
        print(json.dumps({"status": "SUPPORT_EXPANSION_FOLD_COMPLETE", "fold": fold}), flush=True)
    metrics = {
        name: balanced_accuracy(labels, prediction)
        for name, prediction in predictions.items()
    }
    baseline = metrics["REFERENCE"]
    candidates = [name for name in metrics if name != "REFERENCE"]
    best_arm = max(candidates, key=metrics.__getitem__)
    gain_pp = 100.0 * (metrics[best_arm] - baseline)
    baseline_recall = class_recall(labels, predictions["REFERENCE"])
    winner_recall = class_recall(labels, predictions[best_arm])
    delta = winner_recall - baseline_recall
    summary = {
        "experiment_id": protocol["experiment_id"],
        "metrics": metrics,
        "best_arm": best_arm,
        "gain_pp_vs_reference": gain_pp,
        "screen_success": bool(gain_pp >= 0.5),
        "winner_positive_classes": int(np.sum(delta > 0)),
        "winner_negative_classes": int(np.sum(delta < 0)),
        "winner_class_bootstrap_delta_pp": class_bootstrap_interval(delta),
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
    }
    np.savez_compressed(
        args.output_dir / "support_expansion_predictions.npz",
        labels=labels,
        image_ids=image_ids,
        **{f"{name}_predictions": value for name, value in predictions.items()},
    )
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
