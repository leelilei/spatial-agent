#!/usr/bin/env python3
"""Hierarchically aggregate stochastic-IPW runs over sampler seeds and labels."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

import numpy as np

METHODS = (
    "PN-sampled",
    "Ignore",
    "nnPU-sampled",
    "IPW-nnPU",
    "FullPool-nnPU",
)
METRICS = ("roc_auc", "average_precision")


def load_runs(
    run_root: Path, seeds: list[int]
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for seed in seeds:
        path = run_root / f"seed{seed}" / "per_split_results.csv"
        if not path.exists():
            raise FileNotFoundError(path)
        seed_rows = [
            {**row, "sampler_seed": seed}
            for row in csv.DictReader(path.open())
        ]
        if not seed_rows:
            raise ValueError(f"No results in {path}")
        rows.extend(seed_rows)
    return rows


def cell_means(
    rows: list[dict[str, object]],
    labels: list[str],
    seeds: list[int],
    method: str,
    metric: str,
) -> np.ndarray:
    buckets: dict[tuple[int, str], list[float]] = defaultdict(list)
    for row in rows:
        if row["method"] == method:
            buckets[(int(row["sampler_seed"]), str(row["label"]))].append(
                float(row[metric])
            )
    matrix = np.empty((len(seeds), len(labels)), dtype=float)
    for i, seed in enumerate(seeds):
        for j, label in enumerate(labels):
            values = buckets.get((seed, label), [])
            if not values:
                raise ValueError(
                    f"Missing cell seed={seed} label={label} method={method}"
                )
            matrix[i, j] = np.mean(values)
    return matrix


def absolute_gap_cell_means(
    rows: list[dict[str, object]],
    labels: list[str],
    seeds: list[int],
    metric: str,
) -> np.ndarray:
    index = {
        (
            int(row["sampler_seed"]),
            str(row["label"]),
            int(row["repeat"]),
            str(row["method"]),
        ): float(row[metric])
        for row in rows
    }
    matrix = np.empty((len(seeds), len(labels)), dtype=float)
    for i, seed in enumerate(seeds):
        for j, label in enumerate(labels):
            repeats = sorted(
                {
                    int(row["repeat"])
                    for row in rows
                    if int(row["sampler_seed"]) == seed
                    and row["label"] == label
                }
            )
            deltas = []
            for repeat in repeats:
                reference = index[
                    (seed, label, repeat, "FullPool-nnPU")
                ]
                deltas.append(
                    abs(
                        index[(seed, label, repeat, "IPW-nnPU")]
                        - reference
                    )
                    - abs(
                        index[(seed, label, repeat, "nnPU-sampled")]
                        - reference
                    )
                )
            matrix[i, j] = np.mean(deltas)
    return matrix


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


def fmt_ci(interval: tuple[float, float], signed: bool = False) -> str:
    spec = "+.3f" if signed else ".3f"
    return f"{interval[0]:{spec}}–{interval[1]:{spec}}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--seeds", type=int, nargs="+", required=True)
    parser.add_argument("--bootstrap-replicates", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=20260726)
    args = parser.parse_args()

    rows = load_runs(args.run_root, args.seeds)
    labels = sorted({str(row["label"]) for row in rows})
    methods = sorted({str(row["method"]) for row in rows})
    missing_methods = set(METHODS) - set(methods)
    if missing_methods:
        raise ValueError(f"Missing methods: {sorted(missing_methods)}")

    key_counts: defaultdict[tuple[int, str, str], int] = defaultdict(int)
    for row in rows:
        key_counts[
            (
                int(row["sampler_seed"]),
                str(row["label"]),
                str(row["method"]),
            )
        ] += 1
    repeat_counts = sorted(set(key_counts.values()))
    if len(repeat_counts) != 1:
        raise ValueError(f"Unbalanced repeat counts: {repeat_counts}")
    expected_rows = (
        len(args.seeds) * len(labels) * len(METHODS) * repeat_counts[0]
    )
    if len(rows) != expected_rows:
        raise ValueError(f"Expected {expected_rows} rows, found {len(rows)}")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    with (args.out_dir / "all_results.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    rng = np.random.default_rng(args.seed)
    matrices = {
        (method, metric): cell_means(
            rows, labels, args.seeds, method, metric
        )
        for method in METHODS
        for metric in METRICS
    }
    report = [
        "# Multi-sampler-seed stochastic IPW diagnostic",
        "",
        "The fixed Bernoulli inclusion probabilities are held constant while "
        "the sampled candidate set is redrawn under eight predeclared seeds.",
        "",
        f"- Sampler seeds: {', '.join(map(str, args.seeds))}",
        f"- Seeds: {len(args.seeds)}",
        f"- Labels: {len(labels)}",
        f"- Image-split repeats: {repeat_counts[0]} per seed/label",
        f"- Result rows: {len(rows)}",
        f"- Hierarchical bootstrap replicates: {args.bootstrap_replicates}",
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
            "## Paired differences",
            "",
            "| Contrast | ΔROC-AUC | hierarchical 95% CI | ΔAP | hierarchical 95% CI |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    comparisons = (
        ("IPW-nnPU", "nnPU-sampled"),
        ("IPW-nnPU", "FullPool-nnPU"),
        ("IPW-nnPU", "Ignore"),
    )
    for left, right in comparisons:
        auc_delta = matrices[(left, "roc_auc")] - matrices[(right, "roc_auc")]
        ap_delta = (
            matrices[(left, "average_precision")]
            - matrices[(right, "average_precision")]
        )
        report.append(
            f"| {left} − {right} | {auc_delta.mean():+.3f} | "
            f"{fmt_ci(hierarchical_ci(auc_delta, rng, args.bootstrap_replicates), True)} | "
            f"{ap_delta.mean():+.3f} | "
            f"{fmt_ci(hierarchical_ci(ap_delta, rng, args.bootstrap_replicates), True)} |"
        )

    auc_gap = absolute_gap_cell_means(
        rows, labels, args.seeds, "roc_auc"
    )
    ap_gap = absolute_gap_cell_means(
        rows, labels, args.seeds, "average_precision"
    )
    report.extend(
        [
            "",
            "## FullPool approximation",
            "",
            "Negative values mean IPW is closer to the FullPool sampling-risk "
            "reference than unweighted sampled-U nnPU.",
            "",
            "| Gap contrast | Δ absolute AUC gap | hierarchical 95% CI | "
            "Δ absolute AP gap | hierarchical 95% CI |",
            "|---|---:|---:|---:|---:|",
            f"| IPW gap − unweighted gap | {auc_gap.mean():+.3f} | "
            f"{fmt_ci(hierarchical_ci(auc_gap, rng, args.bootstrap_replicates), True)} | "
            f"{ap_gap.mean():+.3f} | "
            f"{fmt_ci(hierarchical_ci(ap_gap, rng, args.bootstrap_replicates), True)} |",
            "",
            "## Per-sampler-seed IPW effects",
            "",
            "| Sampler seed | sampled rows (9 labels) | ΔAUC vs unweighted | "
            "ΔAP vs unweighted | ΔAUC vs Ignore |",
            "|---:|---:|---:|---:|---:|",
        ]
    )
    for i, seed in enumerate(args.seeds):
        seed_rows = [row for row in rows if int(row["sampler_seed"]) == seed]
        sampled_count = sum(
            {
                str(row["label"]): int(row["sampled_count_total"])
                for row in seed_rows
            }.values()
        )
        auc_unweighted = (
            matrices[("IPW-nnPU", "roc_auc")][i]
            - matrices[("nnPU-sampled", "roc_auc")][i]
        ).mean()
        ap_unweighted = (
            matrices[("IPW-nnPU", "average_precision")][i]
            - matrices[("nnPU-sampled", "average_precision")][i]
        ).mean()
        auc_ignore = (
            matrices[("IPW-nnPU", "roc_auc")][i]
            - matrices[("Ignore", "roc_auc")][i]
        ).mean()
        report.append(
            f"| {seed} | {sampled_count} | {auc_unweighted:+.3f} | "
            f"{ap_unweighted:+.3f} | {auc_ignore:+.3f} |"
        )

    report.extend(
        [
            "",
            "## Interpretation boundary",
            "",
            "This analysis tests robustness to candidate sampling only. "
            "FullPool is not an annotation Oracle, and no missing region has "
            "acquired human truth through this experiment.",
        ]
    )
    (args.out_dir / "multiseed_report.md").write_text(
        "\n".join(report) + "\n"
    )
    print(
        f"rows={len(rows)} seeds={len(args.seeds)} labels={len(labels)} "
        f"repeats={repeat_counts[0]}",
        flush=True,
    )


if __name__ == "__main__":
    main()
