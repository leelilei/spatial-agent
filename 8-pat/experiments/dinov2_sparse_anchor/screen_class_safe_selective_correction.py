#!/usr/bin/env python3
"""Nested-OOF class-safe selective correction for PAT-H-260729-011."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import defaultdict
from pathlib import Path

import numpy as np
from sklearn.svm import SVC

from sparse_anchor_utils import balanced_accuracy, class_recall, l2_normalize


CLASSES = 200
K_VALUES = (3, 5)
MARGIN_QUANTILES = (0.1, 0.2, 0.3, 0.4)
PURITY_THRESHOLDS = (0.6, 0.8, 1.0)
MIN_PAIR_WINS = 2
MAX_PAIR_HARMS = 0
MIN_INNER_NET_GAIN = 2


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def top_margin(scores: np.ndarray) -> np.ndarray:
    top2 = np.partition(np.asarray(scores), -2, axis=1)[:, -2:]
    return top2.max(axis=1) - top2.min(axis=1)


def prototype_predictions(
    train_x: np.ndarray,
    train_y: np.ndarray,
    eval_x: np.ndarray,
    classes: int = CLASSES,
) -> np.ndarray:
    prototypes = np.stack(
        [train_x[train_y == label].mean(axis=0) for label in range(classes)]
    )
    prototypes = l2_normalize(prototypes)
    return (eval_x @ prototypes.T).argmax(axis=1)


def knn_predictions_and_purity(
    train_x: np.ndarray,
    train_y: np.ndarray,
    eval_x: np.ndarray,
    k: int,
    classes: int = CLASSES,
) -> tuple[np.ndarray, np.ndarray]:
    similarities = np.asarray(eval_x) @ np.asarray(train_x).T
    nearest = np.argpartition(-similarities, kth=k - 1, axis=1)[:, :k]
    predictions = np.empty(len(eval_x), dtype=np.int64)
    purity = np.empty(len(eval_x), dtype=np.float64)
    for row, neighbor_indices in enumerate(nearest):
        order = neighbor_indices[np.argsort(-similarities[row, neighbor_indices])]
        labels = train_y[order]
        counts = np.bincount(labels, minlength=classes)
        best_count = counts.max()
        tied = np.flatnonzero(counts == best_count)
        if len(tied) == 1:
            prediction = int(tied[0])
        else:
            similarity_sums = np.asarray(
                [similarities[row, order[labels == label]].sum() for label in tied]
            )
            prediction = int(tied[np.argmax(similarity_sums)])
        predictions[row] = prediction
        purity[row] = best_count / k
    return predictions, purity


def component_predictions(
    train_x: np.ndarray,
    train_y: np.ndarray,
    eval_x: np.ndarray,
    classes: int = CLASSES,
) -> dict[str, np.ndarray]:
    rbf = SVC(C=3.0, kernel="rbf", gamma="scale").fit(train_x, train_y)
    decision = rbf.decision_function(eval_x)
    result = {
        "rbf_prediction": rbf.predict(eval_x).astype(np.int64),
        "rbf_margin": top_margin(decision),
        "prototype_prediction": prototype_predictions(
            train_x, train_y, eval_x, classes=classes
        ),
    }
    for k in K_VALUES:
        prediction, purity = knn_predictions_and_purity(
            train_x, train_y, eval_x, k=k, classes=classes
        )
        result[f"knn_{k}_prediction"] = prediction
        result[f"knn_{k}_purity"] = purity
    return result


def pair_statistics(
    base: np.ndarray,
    candidate: np.ndarray,
    labels: np.ndarray,
    eligible: np.ndarray,
) -> dict[tuple[int, int], dict[str, int]]:
    stats: dict[tuple[int, int], dict[str, int]] = defaultdict(
        lambda: {"actions": 0, "wins": 0, "harms": 0, "neutral": 0}
    )
    for index in np.flatnonzero(eligible):
        key = (int(base[index]), int(candidate[index]))
        base_correct = bool(base[index] == labels[index])
        candidate_correct = bool(candidate[index] == labels[index])
        stats[key]["actions"] += 1
        if candidate_correct and not base_correct:
            stats[key]["wins"] += 1
        elif base_correct and not candidate_correct:
            stats[key]["harms"] += 1
        else:
            stats[key]["neutral"] += 1
    return dict(stats)


def accepted_pairs(
    stats: dict[tuple[int, int], dict[str, int]],
) -> set[tuple[int, int]]:
    return {
        pair
        for pair, values in stats.items()
        if values["wins"] >= MIN_PAIR_WINS
        and values["harms"] <= MAX_PAIR_HARMS
    }


def pair_mask(
    base: np.ndarray,
    candidate: np.ndarray,
    pairs: set[tuple[int, int]],
) -> np.ndarray:
    return np.asarray(
        [(int(left), int(right)) in pairs for left, right in zip(base, candidate)],
        dtype=np.bool_,
    )


def correction_counts(
    labels: np.ndarray,
    baseline: np.ndarray,
    corrected: np.ndarray,
) -> dict[str, int]:
    changed = baseline != corrected
    base_correct = baseline == labels
    corrected_correct = corrected == labels
    return {
        "actions": int(changed.sum()),
        "wins": int(np.sum(changed & corrected_correct & ~base_correct)),
        "harms": int(np.sum(changed & base_correct & ~corrected_correct)),
        "neutral": int(np.sum(changed & (base_correct == corrected_correct))),
    }


def evaluate_configuration(
    labels: np.ndarray,
    base: np.ndarray,
    margin: np.ndarray,
    prototype: np.ndarray,
    knn: np.ndarray,
    purity: np.ndarray,
    margin_quantile: float,
    purity_threshold: float,
    classes: int = CLASSES,
) -> dict:
    cutoff = float(np.quantile(margin, margin_quantile))
    candidate = prototype
    eligible = (
        (prototype == knn)
        & (prototype != base)
        & (margin <= cutoff)
        & (purity >= purity_threshold)
    )
    stats = pair_statistics(base, candidate, labels, eligible)
    pairs = accepted_pairs(stats)
    selected = eligible & pair_mask(base, candidate, pairs)
    corrected = base.copy()
    corrected[selected] = candidate[selected]
    counts = correction_counts(labels, base, corrected)
    base_recall = class_recall(labels, base, classes=classes)
    corrected_recall = class_recall(labels, corrected, classes=classes)
    delta = corrected_recall - base_recall
    return {
        "margin_cutoff": cutoff,
        "accepted_pairs": pairs,
        "pair_statistics": stats,
        "corrected": corrected,
        "counts": counts,
        "net_gain": counts["wins"] - counts["harms"],
        "positive_classes": int(np.sum(delta > 0)),
        "negative_classes": int(np.sum(delta < 0)),
    }


def choose_policy(
    labels: np.ndarray,
    components: dict[str, np.ndarray],
    classes: int = CLASSES,
) -> dict | None:
    candidates = []
    for k, margin_quantile, purity_threshold in itertools.product(
        K_VALUES, MARGIN_QUANTILES, PURITY_THRESHOLDS
    ):
        result = evaluate_configuration(
            labels=labels,
            base=components["rbf_prediction"],
            margin=components["rbf_margin"],
            prototype=components["prototype_prediction"],
            knn=components[f"knn_{k}_prediction"],
            purity=components[f"knn_{k}_purity"],
            margin_quantile=margin_quantile,
            purity_threshold=purity_threshold,
            classes=classes,
        )
        result.update(
            {
                "k": k,
                "margin_quantile": margin_quantile,
                "purity_threshold": purity_threshold,
            }
        )
        if (
            result["net_gain"] >= MIN_INNER_NET_GAIN
            and result["negative_classes"] == 0
        ):
            candidates.append(result)
    if not candidates:
        return None
    return max(
        candidates,
        key=lambda item: (
            item["net_gain"],
            item["counts"]["wins"],
            -item["counts"]["actions"],
            -item["margin_quantile"],
            item["purity_threshold"],
            -item["k"],
        ),
    )


def apply_policy(
    components: dict[str, np.ndarray], policy: dict | None
) -> tuple[np.ndarray, np.ndarray]:
    base = components["rbf_prediction"]
    if policy is None:
        return base.copy(), np.zeros(len(base), dtype=np.bool_)
    k = policy["k"]
    prototype = components["prototype_prediction"]
    eligible = (
        (prototype == components[f"knn_{k}_prediction"])
        & (prototype != base)
        & (components["rbf_margin"] <= policy["margin_cutoff"])
        & (components[f"knn_{k}_purity"] >= policy["purity_threshold"])
    )
    selected = eligible & pair_mask(base, prototype, policy["accepted_pairs"])
    corrected = base.copy()
    corrected[selected] = prototype[selected]
    return corrected, selected


def serializable_policy(policy: dict | None) -> dict | None:
    if policy is None:
        return None
    return {
        "k": policy["k"],
        "margin_quantile": policy["margin_quantile"],
        "margin_cutoff": policy["margin_cutoff"],
        "purity_threshold": policy["purity_threshold"],
        "accepted_pairs": [list(pair) for pair in sorted(policy["accepted_pairs"])],
        "inner_counts": policy["counts"],
        "inner_net_gain": policy["net_gain"],
        "inner_positive_classes": policy["positive_classes"],
        "inner_negative_classes": policy["negative_classes"],
    }


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--feature-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    args.output_dir.mkdir(parents=True, exist_ok=True)
    labels = np.load(args.feature_dir / "labels.npy")
    folds = np.load(args.feature_dir / "folds.npy")
    image_ids = np.load(args.feature_dir / "image_ids.npy")
    features = l2_normalize(np.load(args.feature_dir / "cls.npy", mmap_mode="r"))

    baseline = np.full(len(labels), -1, dtype=np.int64)
    corrected = np.full(len(labels), -1, dtype=np.int64)
    changed = np.zeros(len(labels), dtype=np.bool_)
    fold_details = []

    for outer_fold in sorted(np.unique(folds)):
        outer_train = np.flatnonzero(folds != outer_fold)
        outer_eval = np.flatnonzero(folds == outer_fold)
        inner_components = {
            "rbf_prediction": np.full(len(outer_train), -1, dtype=np.int64),
            "rbf_margin": np.full(len(outer_train), np.nan, dtype=np.float64),
            "prototype_prediction": np.full(len(outer_train), -1, dtype=np.int64),
        }
        for k in K_VALUES:
            inner_components[f"knn_{k}_prediction"] = np.full(
                len(outer_train), -1, dtype=np.int64
            )
            inner_components[f"knn_{k}_purity"] = np.full(
                len(outer_train), np.nan, dtype=np.float64
            )

        for inner_fold in sorted(np.unique(folds[outer_train])):
            local_eval = np.flatnonzero(folds[outer_train] == inner_fold)
            inner_eval = outer_train[local_eval]
            inner_train = outer_train[folds[outer_train] != inner_fold]
            values = component_predictions(
                features[inner_train], labels[inner_train], features[inner_eval]
            )
            for name, value in values.items():
                inner_components[name][local_eval] = value

        if np.any(inner_components["rbf_prediction"] < 0):
            raise RuntimeError("inner OOF predictions are incomplete")
        policy = choose_policy(labels[outer_train], inner_components)
        outer_components = component_predictions(
            features[outer_train], labels[outer_train], features[outer_eval]
        )
        fold_corrected, fold_changed = apply_policy(outer_components, policy)
        baseline[outer_eval] = outer_components["rbf_prediction"]
        corrected[outer_eval] = fold_corrected
        changed[outer_eval] = fold_changed
        outer_counts = correction_counts(
            labels[outer_eval], baseline[outer_eval], corrected[outer_eval]
        )
        fold_details.append(
            {
                "outer_fold": int(outer_fold),
                "selected_policy": serializable_policy(policy),
                "outer_baseline_balanced_accuracy": balanced_accuracy(
                    labels[outer_eval], baseline[outer_eval]
                ),
                "outer_corrected_balanced_accuracy": balanced_accuracy(
                    labels[outer_eval], corrected[outer_eval]
                ),
                "outer_counts": outer_counts,
            }
        )
        print(
            f"completed outer fold {outer_fold}: actions={outer_counts['actions']} "
            f"wins={outer_counts['wins']} harms={outer_counts['harms']}",
            flush=True,
        )

    if np.any(baseline < 0) or np.any(corrected < 0):
        raise RuntimeError("outer OOF predictions are incomplete")
    baseline_ba = balanced_accuracy(labels, baseline)
    corrected_ba = balanced_accuracy(labels, corrected)
    counts = correction_counts(labels, baseline, corrected)
    baseline_recall = class_recall(labels, baseline)
    corrected_recall = class_recall(labels, corrected)
    class_delta = corrected_recall - baseline_recall
    gain_pp = 100.0 * (corrected_ba - baseline_ba)
    negative_class_count = int(np.sum(class_delta < 0))
    worst_class_delta = float(class_delta.min())
    gates = {
        "gain_at_least_0_50pp": bool(gain_pp >= 0.5 - 1e-12),
        "negative_class_count_at_most_0": bool(negative_class_count == 0),
        "worst_class_recall_drop_at_least_0": bool(worst_class_delta >= 0.0),
    }
    summary = {
        "experiment_id": protocol["experiment_id"],
        "baseline_balanced_accuracy": baseline_ba,
        "corrected_balanced_accuracy": corrected_ba,
        "gain_pp": gain_pp,
        "correction_counts": counts,
        "positive_class_count": int(np.sum(class_delta > 0)),
        "negative_class_count": negative_class_count,
        "negative_class_rate": negative_class_count / CLASSES,
        "worst_class_recall_delta": worst_class_delta,
        "gates": gates,
        "screen_success": bool(all(gates.values())),
        "fold_details": fold_details,
        "official_test_images_decoded_or_encoded": 0,
        "protocol_sha256": sha256(args.protocol),
    }
    np.savez_compressed(
        args.output_dir / "class_safe_selective_correction_predictions.npz",
        labels=labels,
        folds=folds,
        image_ids=image_ids,
        baseline_predictions=baseline,
        corrected_predictions=corrected,
        changed=changed,
        baseline_class_recall=baseline_recall,
        corrected_class_recall=corrected_recall,
        class_recall_delta=class_delta,
    )
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
