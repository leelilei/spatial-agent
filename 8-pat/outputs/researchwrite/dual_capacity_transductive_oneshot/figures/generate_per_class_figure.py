#!/usr/bin/env python3
"""Generate the per-class transfer figure from the PAT-K-260806-010 analysis.

Reads only the archived analysis outputs in ``source_data``; performs no
inference. Run ``analyze_per_class_transfer.py`` first.
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans", "Liberation Sans"]
plt.rcParams["svg.fonttype"] = "none"

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "source_data"
CLASS_CSV = SOURCE / "per_class_transfer.csv"
PAIRED_CSV = SOURCE / "paired_significance.csv"
SUMMARY_JSON = SOURCE / "per_class_transfer_summary.json"

STEM = "fig_per_class_transfer"
DATASETS = ("CUB-200-2011", "Stanford Dogs")
POS_COLOR = "#2c6fbb"
NEG_COLOR = "#c0392b"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def save_bundle(fig: mpl.figure.Figure, stem: str) -> None:
    fig.savefig(HERE / f"{stem}.pdf", dpi=600, bbox_inches="tight")
    fig.savefig(HERE / f"{stem}.svg", dpi=600, bbox_inches="tight")
    fig.savefig(HERE / f"{stem}.tiff", dpi=600, bbox_inches="tight")
    fig.savefig(HERE / f"{stem}.png", dpi=300, bbox_inches="tight")


def load_rows(path: Path) -> list[dict]:
    with path.open() as handle:
        return list(csv.DictReader(handle))


def class_deltas(rows: list[dict], dataset: str) -> np.ndarray:
    vals = [
        float(r["dctpr_minus_bl_ncc_pp"]) for r in rows if r["dataset"] == dataset
    ]
    return np.sort(np.asarray(vals))[::-1]


def paired_counts(rows: list[dict], dataset: str, comparison: str) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sel = [
        r for r in rows if r["dataset"] == dataset and r["comparison"] == comparison
    ]
    only_m = np.asarray([int(r["dctpr_only_correct"]) for r in sel])
    only_r = np.asarray([int(r["reference_only_correct"]) for r in sel])
    sig = np.asarray([r["significant_at_0.05"] == "True" for r in sel])
    return only_m, only_r, sig


def plot_panel_a(ax: plt.Axes, rows: list[dict], dataset: str) -> None:
    deltas = class_deltas(rows, dataset)
    colors = [POS_COLOR if d > 0 else NEG_COLOR if d < 0 else "#999999" for d in deltas]
    ax.bar(np.arange(deltas.size), deltas, width=1.0, color=colors, linewidth=0)
    ax.axhline(0.0, color="black", linewidth=0.8)
    n_neg = int(np.sum(deltas < 0))
    ax.set_xlabel(f"Classes, sorted by gain ({deltas.size} total)", fontsize=8)
    ax.set_ylabel("DCTPR $-$ BL-NCC (pp)", fontsize=8)
    ax.set_title(dataset, fontsize=9)
    ax.tick_params(labelsize=7)
    ax.margins(x=0.01)
    ax.annotate(
        f"{n_neg} classes degrade\nworst {deltas.min():.1f} pp",
        xy=(0.97, 0.06),
        xycoords="axes fraction",
        ha="right",
        va="bottom",
        fontsize=7,
        color=NEG_COLOR,
    )
    ax.annotate(
        f"mean {deltas.mean():+.2f} pp\nmedian {np.median(deltas):+.2f} pp",
        xy=(0.03, 0.94),
        xycoords="axes fraction",
        ha="left",
        va="top",
        fontsize=7,
    )
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)


def main() -> None:
    class_rows = load_rows(CLASS_CSV)
    paired_rows = load_rows(PAIRED_CSV)
    summary = json.loads(SUMMARY_JSON.read_text())
    refs = {
        "CUB-200-2011": "TIM-ADM",
        "Stanford Dogs": "MAP-RAW",
    }

    fig, axes = plt.subplots(2, 2, figsize=(7.2, 5.0))
    for col, dataset in enumerate(DATASETS):
        plot_panel_a(axes[0, col], class_rows, dataset)
        plot_panel_b(axes[1, col], paired_rows, dataset, refs[dataset])
    axes[0, 0].text(-0.16, 1.06, "a", transform=axes[0, 0].transAxes,
                    fontsize=11, fontweight="bold", va="bottom")
    axes[1, 0].text(-0.16, 1.06, "b", transform=axes[1, 0].transAxes,
                    fontsize=11, fontweight="bold", va="bottom")
    fig.tight_layout(h_pad=2.0, w_pad=2.2)
    save_bundle(fig, STEM)
    plt.close(fig)

    csv_path = write_figure_source_data(class_rows, paired_rows)
    meta = {
        "figure": STEM,
        "experiment_id": "PAT-K-260806-010",
        "official_test_used": False,
        "panels": {
            "a": "per-class DCTPR minus BL-NCC accuracy, sorted descending",
            "b": "per-rotation difference in exclusively-correct queries against the "
                 "strongest matched solver; red bars are significant at alpha=0.05 "
                 "under a two-sided exact McNemar test",
        },
        "caveats": summary["caveats"],
        "inputs": {
            CLASS_CSV.name: sha256(CLASS_CSV),
            PAIRED_CSV.name: sha256(PAIRED_CSV),
            SUMMARY_JSON.name: sha256(SUMMARY_JSON),
        },
        "source_data": {csv_path.name: sha256(csv_path)},
    }
    (SOURCE / f"{STEM}_metadata.json").write_text(json.dumps(meta, indent=2) + "\n")
    print(f"wrote {STEM}.{{pdf,svg,tiff,png}} and source data to {SOURCE}")


def write_figure_source_data(class_rows: list[dict], paired_rows: list[dict]) -> Path:
    """Export exactly the plotted values, in plotted order."""
    out = SOURCE / f"{STEM}.csv"
    records: list[dict] = []
    for dataset in DATASETS:
        deltas = class_deltas(class_rows, dataset)
        for rank, value in enumerate(deltas, start=1):
            records.append(
                {
                    "panel": "a",
                    "dataset": dataset,
                    "series": "dctpr_minus_bl_ncc_pp",
                    "x_sorted_rank": rank,
                    "y_value": round(float(value), 4),
                }
            )
        only_m, only_r, sig = paired_counts(paired_rows, dataset, "vs_strongest")
        order = np.argsort(only_m - only_r)
        for rank, i in enumerate(order, start=1):
            records.append(
                {
                    "panel": "b",
                    "dataset": dataset,
                    "series": "dctpr_only_minus_reference_only_correct",
                    "x_sorted_rank": rank,
                    "y_value": int(only_m[i] - only_r[i]),
                    "significant_at_0.05": bool(sig[i]),
                }
            )
    fields = ["panel", "dataset", "series", "x_sorted_rank", "y_value", "significant_at_0.05"]
    with out.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in records:
            record.setdefault("significant_at_0.05", "")
            writer.writerow(record)
    return out


def plot_panel_b(ax: plt.Axes, rows: list[dict], dataset: str, reference: str) -> None:
    only_m, only_r, sig = paired_counts(rows, dataset, "vs_strongest")
    order = np.argsort(only_m - only_r)
    idx = np.arange(only_m.size)
    diff = (only_m - only_r)[order]
    sig_o = sig[order]
    colors = [NEG_COLOR if s else "#b0b0b0" for s in sig_o]
    ax.bar(idx, diff, color=colors, width=0.8, linewidth=0)
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xlabel("Support rotations, sorted (3 episodes $\\times$ 10)", fontsize=8)
    ax.set_ylabel(f"DCTPR-only $-$ {reference}-only\ncorrect queries", fontsize=8)
    ax.set_title(f"{dataset}: paired decisions vs.\\ {reference}", fontsize=9)
    ax.tick_params(labelsize=7)
    ax.annotate(
        f"{int(np.sum(sig))} of {sig.size} rotations significant\n"
        f"(exact McNemar, $\\alpha=0.05$)",
        xy=(0.03, 0.06),
        xycoords="axes fraction",
        ha="left",
        va="bottom",
        fontsize=7,
    )
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)


if __name__ == "__main__":
    main()
