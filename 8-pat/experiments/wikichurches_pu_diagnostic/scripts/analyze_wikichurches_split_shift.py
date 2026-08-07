#!/usr/bin/env python3
"""Analyze style-conditioned train/validation representation shift."""

from __future__ import annotations

import argparse
import csv
import json
import statistics
from pathlib import Path

import torch


def class_recalls(
    predictions: torch.Tensor,
    labels: torch.Tensor,
    class_count: int,
) -> list[float]:
    return [
        100.0
        * float(
            (
                predictions[labels == class_index]
                == labels[labels == class_index]
            )
            .float()
            .mean()
        )
        for class_index in range(class_count)
    ]


def church_id_from_name(name: str) -> str:
    church_id, separator, suffix = Path(name).name.rpartition("_wd")
    if not separator or not church_id or not suffix.endswith(".jpg"):
        raise ValueError(f"Unexpected WikiChurches filename: {name}")
    return church_id


def aggregate_by_church(
    features: torch.Tensor,
    labels: torch.Tensor,
    names: list[str],
    normalize: bool = True,
) -> tuple[torch.Tensor, torch.Tensor, list[str]]:
    by_church: dict[str, list[int]] = {}
    for index, name in enumerate(names):
        by_church.setdefault(church_id_from_name(name), []).append(index)
    aggregated_features = []
    aggregated_labels = []
    church_ids = []
    for church_id in sorted(by_church):
        indices = torch.tensor(by_church[church_id], dtype=torch.long)
        church_labels = labels[indices]
        if len(torch.unique(church_labels)) != 1:
            raise RuntimeError(f"Church {church_id} has multiple style labels")
        feature = features[indices].mean(dim=0)
        if normalize:
            feature = feature / feature.norm().clamp_min(1e-12)
        aggregated_features.append(feature)
        aggregated_labels.append(church_labels[0])
        church_ids.append(church_id)
    return (
        torch.stack(aggregated_features),
        torch.stack(aggregated_labels),
        church_ids,
    )


def balanced_accuracy(
    predictions: torch.Tensor,
    labels: torch.Tensor,
    class_count: int,
) -> float:
    return statistics.mean(class_recalls(predictions, labels, class_count))


def prototype_predictions(
    train_features: torch.Tensor,
    train_labels: torch.Tensor,
    query_features: torch.Tensor,
    class_count: int,
) -> torch.Tensor:
    prototypes = []
    for class_index in range(class_count):
        prototype = train_features[train_labels == class_index].mean(dim=0)
        prototypes.append(prototype / prototype.norm().clamp_min(1e-12))
    prototypes = torch.stack(prototypes)
    query = query_features / query_features.norm(
        dim=-1,
        keepdim=True,
    ).clamp_min(1e-12)
    return (query @ prototypes.T).argmax(dim=-1)


def leave_one_out_prototype_predictions(
    features: torch.Tensor,
    labels: torch.Tensor,
    class_count: int,
) -> torch.Tensor:
    predictions = []
    for index in range(len(features)):
        mask = torch.ones(len(features), dtype=torch.bool)
        mask[index] = False
        prediction = prototype_predictions(
            features[mask],
            labels[mask],
            features[index : index + 1],
            class_count,
        )
        predictions.append(prediction[0])
    return torch.stack(predictions)


def deserialize_head(document: dict[str, object]) -> dict[str, torch.Tensor]:
    return {
        key: torch.tensor(value, dtype=torch.float32)
        for key, value in document.items()
    }


def apply_head(features: torch.Tensor, head: dict[str, torch.Tensor]) -> torch.Tensor:
    standardized = (
        features.float() - head["feature_mean"]
    ) / head["feature_scale"]
    logits = standardized @ head["weights"] + head["intercept"]
    return logits - logits.mean(dim=-1, keepdim=True)


def squared_centroid_distance(
    features: torch.Tensor,
    domain: torch.Tensor,
) -> float:
    left = features[domain == 0].mean(dim=0)
    right = features[domain == 1].mean(dim=0)
    return float((left - right).square().sum())


def shift_statistics(
    train_features: torch.Tensor,
    train_labels: torch.Tensor,
    val_features: torch.Tensor,
    val_labels: torch.Tensor,
    style_names: list[str],
    permutation_count: int,
    seed: int,
) -> tuple[list[dict[str, object]], dict[str, float]]:
    class_count = len(style_names)
    rows = []
    observed_by_style = []
    pooled_by_style = []
    domain_by_style = []
    generator = torch.Generator().manual_seed(seed)
    for class_index, class_name in enumerate(style_names):
        train = train_features[train_labels == class_index].float()
        val = val_features[val_labels == class_index].float()
        pooled = torch.cat((train, val))
        domain = torch.cat(
            (
                torch.zeros(len(train), dtype=torch.long),
                torch.ones(len(val), dtype=torch.long),
            )
        )
        observed = squared_centroid_distance(pooled, domain)
        train_centroid = train.mean(dim=0)
        within_rms = float(
            ((train - train_centroid).square().sum(dim=-1).mean()).sqrt()
        )
        effect = observed**0.5 / max(within_rms, 1e-12)
        exceed = 0
        for _ in range(permutation_count):
            permutation = torch.randperm(len(pooled), generator=generator)
            permuted_domain = domain[permutation]
            statistic = squared_centroid_distance(pooled, permuted_domain)
            exceed += statistic >= observed
        p_value = (exceed + 1) / (permutation_count + 1)
        rows.append(
            {
                "style": class_name,
                "train_count": len(train),
                "validation_count": len(val),
                "squared_centroid_distance": observed,
                "train_within_rms_radius": within_rms,
                "normalized_shift_effect": effect,
                "permutation_p": p_value,
            }
        )
        observed_by_style.append(observed)
        pooled_by_style.append(pooled)
        domain_by_style.append(domain)

    observed_overall = statistics.mean(observed_by_style)
    exceed_overall = 0
    for _ in range(permutation_count):
        statistics_by_style = []
        for pooled, domain in zip(
            pooled_by_style,
            domain_by_style,
            strict=True,
        ):
            permutation = torch.randperm(len(pooled), generator=generator)
            statistics_by_style.append(
                squared_centroid_distance(pooled, domain[permutation])
            )
        exceed_overall += statistics.mean(statistics_by_style) >= observed_overall
    overall = {
        "equal_style_mean_squared_centroid_distance": observed_overall,
        "stratified_permutation_p": (
            exceed_overall + 1
        ) / (permutation_count + 1),
    }
    return rows, overall


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--global-features", type=Path, required=True)
    parser.add_argument("--local-train", type=Path, required=True)
    parser.add_argument("--local-val", type=Path, required=True)
    parser.add_argument("--residual-frozen-config", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    global_data = torch.load(args.global_features, map_location="cpu")
    local_train = torch.load(args.local_train, map_location="cpu")
    local_val = torch.load(args.local_val, map_location="cpu")
    frozen = json.loads(
        args.residual_frozen_config.read_text(encoding="utf-8")
    )
    if global_data["experiment_id"] != protocol["experiment_id"]:
        raise RuntimeError("Global feature experiment mismatch")
    if (
        local_train["split"] != "train_loco_calibration"
        or local_val["split"] != "val"
    ):
        raise RuntimeError("Invalid local artifacts")
    test_count = (
        int(global_data["test_images_encoded"])
        + int(local_train["test_images_encoded"])
        + int(local_val["test_images_encoded"])
    )
    if test_count != 0:
        raise RuntimeError("Test image found in diagnostic inputs")

    style_names = list(global_data["style_names"])
    class_count = len(style_names)
    permutation_count = int(protocol["permutation"]["count"])
    seed = int(protocol["permutation"]["seed"])
    ratio_key = "0.01"

    global_all_train, global_all_train_labels, all_train_church_ids = (
        aggregate_by_church(
        global_data["train_features"].float(),
        global_data["train_labels"].long(),
        list(global_data["train_names"]),
        )
    )
    global_val, global_val_labels, val_church_ids = aggregate_by_church(
        global_data["val_features"].float(),
        global_data["val_labels"].long(),
        list(global_data["val_names"]),
    )
    if set(all_train_church_ids) & set(val_church_ids):
        raise RuntimeError("Train/validation church overlap")
    box_church_ids = list(local_train["church_ids"])
    box_church_set = set(box_church_ids)
    if len(box_church_set) != len(box_church_ids):
        raise RuntimeError("Duplicate church in local train calibration")
    all_train_index = {
        church_id: index
        for index, church_id in enumerate(all_train_church_ids)
    }
    missing_box_churches = box_church_set - set(all_train_index)
    if missing_box_churches:
        raise RuntimeError(
            f"Box churches absent from canonical train: "
            f"{sorted(missing_box_churches)[:5]}"
        )
    box_indices = torch.tensor(
        [all_train_index[church_id] for church_id in sorted(box_church_set)],
        dtype=torch.long,
    )
    global_train = global_all_train[box_indices]
    global_train_labels = global_all_train_labels[box_indices]
    global_train_prediction = leave_one_out_prototype_predictions(
        global_train,
        global_train_labels,
        class_count,
    )
    global_val_prediction = prototype_predictions(
        global_train,
        global_train_labels,
        global_val,
        class_count,
    )
    global_train_recalls = class_recalls(
        global_train_prediction,
        global_train_labels,
        class_count,
    )
    global_val_recalls = class_recalls(
        global_val_prediction,
        global_val_labels,
        class_count,
    )

    (
        local_train_features,
        local_train_labels,
        local_train_church_ids,
    ) = aggregate_by_church(
        local_train["official_calibration_scores"][ratio_key].float(),
        local_train["labels"].long(),
        list(local_train["image_names"]),
        normalize=False,
    )
    (
        local_val_features,
        local_val_labels,
        local_val_church_ids,
    ) = aggregate_by_church(
        local_val["official_local_scores"][ratio_key].float(),
        local_val["labels"].long(),
        list(local_val["image_names"]),
        normalize=False,
    )
    if set(local_train_church_ids) != box_church_set:
        raise RuntimeError("Local/global box-bearing church mismatch")
    if set(local_train_church_ids) & set(local_val_church_ids):
        raise RuntimeError("Local train/validation church overlap")
    official_head = deserialize_head(frozen["official_head"])
    local_val_logits = apply_head(local_val_features, official_head)
    local_val_prediction = local_val_logits.argmax(dim=-1)
    local_train_ba = float(
        frozen["head_cv_selection"]["oof_balanced_accuracy"]
    )
    local_train_recalls = [
        float(
            frozen["head_cv_selection"][f"oof_recall_{style_name}"]
        )
        for style_name in style_names
    ]
    local_val_recalls = class_recalls(
        local_val_prediction,
        local_val_labels,
        class_count,
    )
    local_val_ba = balanced_accuracy(
        local_val_prediction,
        local_val_labels,
        class_count,
    )

    local_mean = local_train_features.mean(dim=0)
    local_scale = local_train_features.std(
        dim=0,
        correction=0,
    ).clamp_min(0.02)
    local_train_standardized = (
        local_train_features - local_mean
    ) / local_scale
    local_val_standardized = (
        local_val_features - local_mean
    ) / local_scale

    global_shift_rows, global_overall = shift_statistics(
        global_train,
        global_train_labels,
        global_val,
        global_val_labels,
        style_names,
        permutation_count,
        seed,
    )
    global_all_shift_rows, global_all_overall = shift_statistics(
        global_all_train,
        global_all_train_labels,
        global_val,
        global_val_labels,
        style_names,
        permutation_count,
        seed + 10,
    )
    local_shift_rows, local_overall = shift_statistics(
        local_train_standardized,
        local_train_labels,
        local_val_standardized,
        local_val_labels,
        style_names,
        permutation_count,
        seed + 1,
    )
    transfer_rows = []
    for index, style_name in enumerate(style_names):
        transfer_rows.append(
            {
                "representation": "global_clip",
                "style": style_name,
                "train_recall": global_train_recalls[index],
                "validation_recall": global_val_recalls[index],
                "recall_drop": (
                    global_train_recalls[index] - global_val_recalls[index]
                ),
            }
        )
        transfer_rows.append(
            {
                "representation": "local_residual_head",
                "style": style_name,
                "train_recall": local_train_recalls[index],
                "validation_recall": local_val_recalls[index],
                "recall_drop": (
                    local_train_recalls[index] - local_val_recalls[index]
                ),
            }
        )
    transfer_summary = {
        "global_train_balanced_accuracy": balanced_accuracy(
            global_train_prediction,
            global_train_labels,
            class_count,
        ),
        "global_validation_balanced_accuracy": balanced_accuracy(
            global_val_prediction,
            global_val_labels,
            class_count,
        ),
        "local_train_oof_balanced_accuracy": local_train_ba,
        "local_validation_balanced_accuracy": local_val_ba,
    }
    transfer_summary["global_balanced_accuracy_drop"] = (
        transfer_summary["global_train_balanced_accuracy"]
        - transfer_summary["global_validation_balanced_accuracy"]
    )
    transfer_summary["local_balanced_accuracy_drop"] = (
        transfer_summary["local_train_oof_balanced_accuracy"]
        - transfer_summary["local_validation_balanced_accuracy"]
    )
    global_all_train_prediction = leave_one_out_prototype_predictions(
        global_all_train,
        global_all_train_labels,
        class_count,
    )
    global_all_val_prediction = prototype_predictions(
        global_all_train,
        global_all_train_labels,
        global_val,
        class_count,
    )
    transfer_summary["global_all_train_balanced_accuracy"] = (
        balanced_accuracy(
            global_all_train_prediction,
            global_all_train_labels,
            class_count,
        )
    )
    transfer_summary["global_all_train_to_validation_balanced_accuracy"] = (
        balanced_accuracy(
            global_all_val_prediction,
            global_val_labels,
            class_count,
        )
    )
    gothic_index = style_names.index("Gothic")
    gothic_local_recall_drop = (
        local_train_recalls[gothic_index] - local_val_recalls[gothic_index]
    )
    ranked_local_styles = sorted(
        local_shift_rows,
        key=lambda row: float(row["normalized_shift_effect"]),
        reverse=True,
    )
    gothic_shift_rank = next(
        index
        for index, row in enumerate(ranked_local_styles, start=1)
        if row["style"] == "Gothic"
    )
    rule = protocol["diagnostic_support_rule"]
    conditions = {
        "global_stratified_permutation": {
            "observed": global_overall["stratified_permutation_p"],
            "required_at_most": float(
                rule["global_stratified_permutation_p_at_most"]
            ),
            "pass": global_overall["stratified_permutation_p"]
            <= float(rule["global_stratified_permutation_p_at_most"]),
        },
        "local_stratified_permutation": {
            "observed": local_overall["stratified_permutation_p"],
            "required_at_most": float(
                rule["local_stratified_permutation_p_at_most"]
            ),
            "pass": local_overall["stratified_permutation_p"]
            <= float(rule["local_stratified_permutation_p_at_most"]),
        },
        "local_balanced_accuracy_drop": {
            "observed": transfer_summary["local_balanced_accuracy_drop"],
            "required_at_least": float(
                rule["local_balanced_accuracy_drop_at_least"]
            ),
            "pass": transfer_summary["local_balanced_accuracy_drop"]
            >= float(rule["local_balanced_accuracy_drop_at_least"]),
        },
        "gothic_local_recall_drop": {
            "observed": gothic_local_recall_drop,
            "required_at_least": float(
                rule["gothic_local_recall_drop_at_least"]
            ),
            "pass": gothic_local_recall_drop
            >= float(rule["gothic_local_recall_drop_at_least"]),
        },
        "gothic_local_shift_effect_rank": {
            "observed": gothic_shift_rank,
            "required_at_most": int(
                rule["gothic_local_shift_effect_rank_at_most"]
            ),
            "pass": gothic_shift_rank
            <= int(rule["gothic_local_shift_effect_rank_at_most"]),
        },
    }
    decision = {
        "experiment_id": protocol["experiment_id"],
        "decision": (
            "SPLIT_SHIFT_SUPPORTED"
            if all(condition["pass"] for condition in conditions.values())
            else "SPLIT_SHIFT_NOT_FULLY_SUPPORTED"
        ),
        "conditions": conditions,
        "global_shift": global_overall,
        "global_all_train_control_shift": global_all_overall,
        "local_shift": local_overall,
        "transfer": transfer_summary,
        "gothic_local_recall_drop": gothic_local_recall_drop,
        "gothic_local_shift_effect_rank": gothic_shift_rank,
        "test_images_encoded": test_count,
    }

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for name, rows in (
        ("global_box_subset_shift_by_style.csv", global_shift_rows),
        ("global_all_train_control_shift_by_style.csv", global_all_shift_rows),
        ("local_shift_by_style.csv", local_shift_rows),
        ("transfer_by_style.csv", transfer_rows),
    ):
        with (args.out_dir / name).open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    (args.out_dir / "decision.json").write_text(
        json.dumps(decision, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# WikiChurches train–validation split-shift diagnostic",
        "",
        f"Decision: **{decision['decision']}**. Test images encoded: "
        f"**{test_count}**.",
        "",
        "| Representation | Train BA | Validation BA | Drop | Stratified p |",
        "|---|---:|---:|---:|---:|",
        f"| Global CLIP, box subset | "
        f"{transfer_summary['global_train_balanced_accuracy']:.2f} | "
        f"{transfer_summary['global_validation_balanced_accuracy']:.2f} | "
        f"{transfer_summary['global_balanced_accuracy_drop']:+.2f} | "
        f"{global_overall['stratified_permutation_p']:.5f} |",
        f"| Global CLIP, all-train control | "
        f"{transfer_summary['global_all_train_balanced_accuracy']:.2f} | "
        f"{transfer_summary['global_all_train_to_validation_balanced_accuracy']:.2f} | "
        f"{transfer_summary['global_all_train_balanced_accuracy'] - transfer_summary['global_all_train_to_validation_balanced_accuracy']:+.2f} | "
        f"{global_all_overall['stratified_permutation_p']:.5f} |",
        f"| Local residual | {local_train_ba:.2f} | {local_val_ba:.2f} | "
        f"{transfer_summary['local_balanced_accuracy_drop']:+.2f} | "
        f"{local_overall['stratified_permutation_p']:.5f} |",
        "",
        "## Local shift by style",
        "",
        "| Style | Train n | Val n | Normalized shift | Permutation p |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in local_shift_rows:
        lines.append(
            f"| {row['style']} | {row['train_count']} | "
            f"{row['validation_count']} | "
            f"{row['normalized_shift_effect']:.3f} | "
            f"{row['permutation_p']:.5f} |"
        )
    lines.extend(["", "## Gate", ""])
    for name, condition in conditions.items():
        lines.append(
            f"- {name}: {'PASS' if condition['pass'] else 'FAIL'} "
            f"({json.dumps(condition, sort_keys=True)})"
        )
    (args.out_dir / "README.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(decision, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
