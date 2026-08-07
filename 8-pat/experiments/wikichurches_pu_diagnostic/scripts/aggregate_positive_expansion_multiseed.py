#!/usr/bin/env python3
"""Aggregate conservative positive expansion across sampler seeds and labels."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

import numpy as np

BASELINE_METHODS = (
    "PN-sampled",
    "Ignore",
    "nnPU-sampled",
    "IPW-nnPU",
    "FullPool-nnPU",
)
METHODS = BASELINE_METHODS + ("PositiveExpansion",)
METRICS = ("roc_auc", "average_precision")


def hierarchical_ci(
    matrix: np.ndarray,
    rng: np.random.Generator,
    replicates: int,
) -> tuple[float, float]:
    draws = np.empty(replicates, dtype=float)
    for index in range(replicates):
        seed_indices = rng.integers(0, matrix.shape[0], matrix.shape[0])
        label_indices = rng.integers(0, matrix.shape[1], matrix.shape[1])
        draws[index] = matrix[np.ix_(seed_indices, label_indices)].mean()
    return tuple(np.quantile(draws, (0.025, 0.975)).tolist())


def cell_matrix(
    rows: list[dict[str, object]],
    seeds: list[int],
    labels: list[str],
    method: str,
    field: str,
) -> np.ndarray:
    buckets: defaultdict[tuple[int, str], list[float]] = defaultdict(list)
    for row in rows:
        if row["method"] == method:
            buckets[(int(row["sampler_seed"]), str(row["label"]))].append(
                float(row[field])
            )
    result = np.empty((len(seeds), len(labels)), dtype=float)
    for i, seed in enumerate(seeds):
        for j, label in enumerate(labels):
            values = buckets[(seed, label)]
            if len(values) != 30:
                raise ValueError(
                    f"Expected 30 rows for {seed}/{label}/{method}, "
                    f"found {len(values)}"
                )
            result[i, j] = np.mean(values)
    return result


def fmt_ci(interval: tuple[float, float], signed: bool = False) -> str:
    spec = "+.3f" if signed else ".3f"
    return f"{interval[0]:{spec}}–{interval[1]:{spec}}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline-results", type=Path, required=True)
    parser.add_argument("--positive-run-root", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--seeds", type=int, nargs="+", required=True)
    parser.add_argument("--bootstrap-replicates", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=20260726)
    args = parser.parse_args()

    baseline_rows = list(csv.DictReader(args.baseline_results.open()))
    positive_rows: list[dict[str, object]] = []
    for seed in args.seeds:
        path = (
            args.positive_run_root
            / f"seed{seed}"
            / "per_split_results.csv"
        )
        positive_rows.extend(
            {**row, "sampler_seed": seed}
            for row in csv.DictReader(path.open())
        )
    labels = sorted({str(row["label"]) for row in positive_rows})

    baseline_ignore = {
        (
            int(row["sampler_seed"]),
            str(row["label"]),
            int(row["repeat"]),
        ): row
        for row in baseline_rows
        if row["method"] == "Ignore"
    }
    positive_ignore = {
        (
            int(row["sampler_seed"]),
            str(row["label"]),
            int(row["repeat"]),
        ): row
        for row in positive_rows
        if row["method"] == "Ignore"
    }
    if set(baseline_ignore) != set(positive_ignore):
        raise ValueError("Positive-expansion splits do not match baseline")
    max_ignore_difference = max(
        abs(
            float(baseline_ignore[key][metric])
            - float(positive_ignore[key][metric])
        )
        for key in baseline_ignore
        for metric in METRICS
    )
    if max_ignore_difference > 1e-12:
        raise ValueError(
            f"Ignore reproduction mismatch: {max_ignore_difference}"
        )

    expansion_rows = [
        row for row in positive_rows if row["method"] == "PositiveExpansion"
    ]
    combined_rows = baseline_rows + expansion_rows
    matrices = {
        (method, metric): cell_matrix(
            combined_rows, args.seeds, labels, method, metric
        )
        for method in METHODS
        for metric in METRICS
    }
    rng = np.random.default_rng(args.seed)
    report = [
        "# Conservative positive-expansion multi-seed diagnostic",
        "",
        f"- Sampler seeds: {len(args.seeds)}",
        f"- Labels: {len(labels)}",
        "- Image-split repeats: 30",
        f"- Baseline rows: {len(baseline_rows)}",
        f"- PositiveExpansion rows: {len(expansion_rows)}",
        f"- Combined rows: {len(combined_rows)}",
        f"- Reproduced Ignore max absolute difference: "
        f"{max_ignore_difference:.3g}",
        "",
        "## Held-out known-label performance",
        "",
        "| Method | ROC-AUC | hierarchical 95% CI | AP | hierarchical 95% CI |",
        "|---|---:|---:|---:|---:|",
    ]
    for method in METHODS:
        auc = matrices[(method, "roc_auc")]
        ap = matrices[(method, "average_precision")]
        report.append(
            f"| {method} | {auc.mean():.3f} | "
            f"{fmt_ci(hierarchical_ci(auc, rng, args.bootstrap_replicates))} | "
            f"{ap.mean():.3f} | "
            f"{fmt_ci(hierarchical_ci(ap, rng, args.bootstrap_replicates))} |"
        )

    report.extend(
        [
            "",
            "## Frozen-gate contrasts",
            "",
            "| Contrast | ΔROC-AUC | hierarchical 95% CI | ΔAP | hierarchical 95% CI |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for right in ("Ignore", "PN-sampled", "IPW-nnPU", "FullPool-nnPU"):
        auc_delta = (
            matrices[("PositiveExpansion", "roc_auc")]
            - matrices[(right, "roc_auc")]
        )
        ap_delta = (
            matrices[("PositiveExpansion", "average_precision")]
            - matrices[(right, "average_precision")]
        )
        report.append(
            f"| PositiveExpansion − {right} | {auc_delta.mean():+.3f} | "
            f"{fmt_ci(hierarchical_ci(auc_delta, rng, args.bootstrap_replicates), True)} | "
            f"{ap_delta.mean():+.3f} | "
            f"{fmt_ci(hierarchical_ci(ap_delta, rng, args.bootstrap_replicates), True)} |"
        )

    expansion_auc = matrices[("PositiveExpansion", "roc_auc")]
    ignore_auc = matrices[("Ignore", "roc_auc")]
    expansion_ap = matrices[("PositiveExpansion", "average_precision")]
    ignore_ap = matrices[("Ignore", "average_precision")]
    auc_delta = expansion_auc - ignore_auc
    ap_delta = expansion_ap - ignore_ap
    per_label_auc = auc_delta.mean(axis=0)
    per_seed_auc = auc_delta.mean(axis=1)
    selection_by_cell: defaultdict[tuple[int, str], list[float]] = defaultdict(
        list
    )
    for row in expansion_rows:
        selection_by_cell[
            (int(row["sampler_seed"]), str(row["label"]))
        ].append(float(row["selected_pseudo_positive"]))
    selected_matrix = np.asarray(
        [
            [
                np.mean(selection_by_cell[(seed, label)])
                for label in labels
            ]
            for seed in args.seeds
        ]
    )
    covered_labels = int((selected_matrix.mean(axis=0) > 0).sum())
    auc_ci = hierarchical_ci(
        auc_delta, rng, args.bootstrap_replicates
    )
    ap_ci = hierarchical_ci(ap_delta, rng, args.bootstrap_replicates)
    gate_pass = (
        auc_delta.mean() >= 0.01
        and ap_delta.mean() >= 0.01
        and auc_ci[0] > 0
        and ap_ci[0] > 0
        and covered_labels >= 4
        and np.all(per_seed_auc > 0)
    )
    report.extend(
        [
            "",
            "## Per-label diagnostics",
            "",
            "| Label | selected / split | ΔAUC vs Ignore | ΔAP vs Ignore |",
            "|---|---:|---:|---:|",
        ]
    )
    for index, label in enumerate(labels):
        report.append(
            f"| {label} | {selected_matrix[:, index].mean():.2f} | "
            f"{per_label_auc[index]:+.3f} | "
            f"{ap_delta[:, index].mean():+.3f} |"
        )
    report.extend(
        [
            "",
            "## Per-sampler-seed diagnostics",
            "",
            "| Sampler seed | selected / split | ΔAUC vs Ignore | "
            "ΔAP vs Ignore |",
            "|---:|---:|---:|---:|",
        ]
    )
    for index, seed in enumerate(args.seeds):
        report.append(
            f"| {seed} | {selected_matrix[index].mean():.2f} | "
            f"{per_seed_auc[index]:+.3f} | "
            f"{ap_delta[index].mean():+.3f} |"
        )
    report.extend(
        [
            "",
            "## Frozen Go gate",
            "",
            f"- Mean selected pseudo-positives / split: "
            f"{selected_matrix.mean():.2f}",
            f"- Labels with any mean expansion: {covered_labels}/{len(labels)}",
            f"- Labels with positive AUC delta: "
            f"{int((per_label_auc > 0).sum())}/{len(labels)}",
            f"- Sampler seeds with positive AUC delta: "
            f"{int((per_seed_auc > 0).sum())}/{len(args.seeds)}",
            f"- Required: ΔAUC and ΔAP ≥ +0.01, both lower CIs > 0, "
            f"coverage ≥ 4 labels, AUC positive in every sampler seed.",
            f"- Decision: **{'GO' if gate_pass else 'NO-GO'}**.",
            "",
            "U not selected as pseudo-positive receives zero loss. This "
            "experiment evaluates preservation of held-out official labels; "
            "it does not establish missing-positive truth.",
        ]
    )
    args.out_dir.mkdir(parents=True, exist_ok=True)
    with (args.out_dir / "combined_results.csv").open(
        "w", newline=""
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=sorted(
                {field for row in combined_rows for field in row}
            ),
        )
        writer.writeheader()
        writer.writerows(combined_rows)
    (args.out_dir / "positive_expansion_report.md").write_text(
        "\n".join(report) + "\n"
    )
    print(
        f"combined_rows={len(combined_rows)} "
        f"ignore_max_diff={max_ignore_difference:.3g} "
        f"decision={'GO' if gate_pass else 'NO-GO'}",
        flush=True,
    )


if __name__ == "__main__":
    main()
