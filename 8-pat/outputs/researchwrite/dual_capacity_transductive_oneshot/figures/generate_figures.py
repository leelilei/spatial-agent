#!/usr/bin/env python3
"""Generate the DCTPR manuscript figures from archived data and training images."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps


plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans", "Liberation Sans"]
plt.rcParams["svg.fonttype"] = "none"


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "source_data"
CUB_PATH = SOURCE / "cub_matched_summary.json"
DOGS_PATH = SOURCE / "dogs_matched_summary.json"
STRESS_PATH = SOURCE / "cub_prior_stress_summary.json"
SOURCE_IMAGES = HERE / "source_images"
PROJECT_ROOT = HERE.parents[3]
DOGS_FEATURE_ROOT = (
    PROJECT_ROOT
    / "raw"
    / "experiments"
    / "2026.07.29_StanfordDogs_DCTPR_PAT-K-260729-006"
    / "features"
)

DIAGNOSTIC_SETTINGS = {
    "temperature": 0.05,
    "sinkhorn_iterations": 100,
    "refinement_steps": 3,
    "support_query_mix": 0.5,
}

TRAINING_EXAMPLES = [
    {
        "panel": "a",
        "dataset": "CUB-200-2011",
        "class_name": "Nashville warbler",
        "path": SOURCE_IMAGES / "cub" / "3_nashville_warbler.jpg",
        "source_locator": "anjunhu/naively_captioned_CUB2002011_train, row 3",
        "split_verification": "training-only mirror: 5,994 official-training images",
    },
    {
        "panel": "a",
        "dataset": "CUB-200-2011",
        "class_name": "Tennessee warbler",
        "path": SOURCE_IMAGES / "cub" / "5_tennessee_warbler.jpg",
        "source_locator": "anjunhu/naively_captioned_CUB2002011_train, row 5",
        "split_verification": "training-only mirror: 5,994 official-training images",
    },
    {
        "panel": "a",
        "dataset": "CUB-200-2011",
        "class_name": "Myrtle warbler",
        "path": SOURCE_IMAGES / "cub" / "3002_myrtle_warbler.jpg",
        "source_locator": "anjunhu/naively_captioned_CUB2002011_train, row 3002",
        "split_verification": "training-only mirror: 5,994 official-training images",
    },
    {
        "panel": "b",
        "dataset": "Stanford Dogs",
        "class_name": "Norfolk terrier",
        "path": SOURCE_IMAGES / "dogs" / "n02094114_2923.jpg",
        "source_locator": (
            "Images/n02094114-Norfolk_terrier/n02094114_2923.jpg"
        ),
        "split_verification": "listed in the official Stanford Dogs train_list.mat",
    },
    {
        "panel": "b",
        "dataset": "Stanford Dogs",
        "class_name": "Norwich terrier",
        "path": SOURCE_IMAGES / "dogs" / "n02094258_3435.jpg",
        "source_locator": (
            "Images/n02094258-Norwich_terrier/n02094258_3435.jpg"
        ),
        "split_verification": "listed in the official Stanford Dogs train_list.mat",
    },
    {
        "panel": "b",
        "dataset": "Stanford Dogs",
        "class_name": "Cairn terrier",
        "path": SOURCE_IMAGES / "dogs" / "n02096177_164.jpg",
        "source_locator": "Images/n02096177-cairn/n02096177_164.jpg",
        "split_verification": "listed in the official Stanford Dogs train_list.mat",
    },
]


COLORS = {
    "DCTPR": "#D55E3A",
    "strong": "#252525",
    "BL_SINKHORN": "#4C78A8",
    "LAPLACIANSHOT": "#8F9AA3",
    "MAP_RAW": "#6F6F6F",
    "SIGNED_PT_MAP": "#A0A0A0",
    "BL_NCC": "#717171",
    "TIM_ADM": "#252525",
    "DCTPR_ORACLE": "#2E8B70",
}

LABELS = {
    "BL_SINKHORN": "Balanced assignment",
    "LAPLACIANSHOT": "LaplacianShot",
    "MAP_RAW": "MAP-RAW",
    "SIGNED_PT_MAP": "Signed PT-MAP",
    "TIM_ADM": "TIM-ADM",
    "DCTPR": "DCTPR",
}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def mean_methods(summary: dict) -> dict[str, dict[str, float]]:
    methods = summary["episodes"][0]["aggregate"].keys()
    result = {}
    for method in methods:
        result[method] = {
            "accuracy": float(
                np.mean(
                    [episode["aggregate"][method]["mean"] for episode in summary["episodes"]]
                )
            ),
            "runtime_ms": float(
                1000
                * np.mean(
                    [
                        episode["aggregate"][method]["mean_runtime_seconds"]
                        for episode in summary["episodes"]
                    ]
                )
            ),
        }
    return result


def save_bundle(fig: mpl.figure.Figure, stem: str) -> None:
    fig.savefig(HERE / f"{stem}.pdf", dpi=600, bbox_inches="tight")
    fig.savefig(HERE / f"{stem}.svg", dpi=600, bbox_inches="tight")
    fig.savefig(HERE / f"{stem}.tiff", dpi=600, bbox_inches="tight")
    fig.savefig(HERE / f"{stem}.png", dpi=300, bbox_inches="tight")


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    SOURCE.mkdir(exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def plot_training_examples() -> None:
    """Assemble a compact plate of verified official-training images."""
    fig, axes = plt.subplots(1, 6, figsize=(7.05, 1.45))
    provenance_rows = []
    for ax, example in zip(axes, TRAINING_EXAMPLES):
        path = example["path"]
        if not path.is_file():
            raise FileNotFoundError(f"Missing source image: {path}")
        with Image.open(path) as raw:
            image = ImageOps.fit(
                raw.convert("RGB"),
                (800, 600),
                method=Image.Resampling.LANCZOS,
                centering=(0.5, 0.5),
            )
        ax.imshow(image)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(example["class_name"], fontsize=5.8, fontweight="normal", pad=2)
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_color("#B7B7B7")
            spine.set_linewidth(0.45)
        provenance_rows.append(
            {
                "panel": example["panel"],
                "dataset": example["dataset"],
                "class_name": example["class_name"],
                "source_locator": example["source_locator"],
                "split_verification": example["split_verification"],
                "sha256": sha256(path),
                "processing": (
                    "center crop to 4:3; no brightness, contrast, color, or "
                    "local-content adjustment"
                ),
            }
        )

    fig.subplots_adjust(left=0.012, right=0.995, bottom=0.03, top=0.76, wspace=0.08)
    fig.text(0.012, 0.95, "a", fontsize=8, fontweight="bold", va="top")
    fig.text(
        0.035,
        0.95,
        "CUB-200-2011 official training",
        fontsize=7,
        fontweight="bold",
        va="top",
    )
    fig.text(0.51, 0.95, "b", fontsize=8, fontweight="bold", va="top")
    fig.text(
        0.533,
        0.95,
        "Stanford Dogs official training",
        fontsize=7,
        fontweight="bold",
        va="top",
    )
    save_bundle(fig, "fig_training_examples")
    write_csv(
        SOURCE / "fig_training_examples_provenance.csv",
        [
            "panel",
            "dataset",
            "class_name",
            "source_locator",
            "split_verification",
            "sha256",
            "processing",
        ],
        provenance_rows,
    )
    plt.close(fig)


def plot_pareto(cub: dict, dogs: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(7.05, 2.55), sharex=True)
    methods = [
        "LAPLACIANSHOT",
        "BL_SINKHORN",
        "DCTPR",
        "TIM_ADM",
        "MAP_RAW",
        "SIGNED_PT_MAP",
    ]
    offsets = {
        "CUB": {
            "LAPLACIANSHOT": (3, 5),
            "BL_SINKHORN": (3, -11),
            "DCTPR": (4, -14),
            "TIM_ADM": (4, 5),
            "MAP_RAW": (4, -12),
            "SIGNED_PT_MAP": (-55, 4),
        },
        "Dogs": {
            "LAPLACIANSHOT": (3, 5),
            "BL_SINKHORN": (3, 5),
            "DCTPR": (4, 5),
            "TIM_ADM": (4, -12),
            "MAP_RAW": (4, 5),
            "SIGNED_PT_MAP": (-57, -12),
        },
    }

    rows = []
    for ax, (dataset, values) in zip(axes, [("CUB", cub), ("Dogs", dogs)]):
        baseline = 100 * values["BL_NCC"]["accuracy"]
        ax.axhline(baseline, color="#9A9A9A", linestyle=(0, (3, 2)), linewidth=0.8)
        ax.axvline(
            50,
            color="#8A6D3B",
            linestyle=(0, (5, 2, 1, 2)),
            linewidth=0.85,
            zorder=1,
        )
        ax.text(
            2.15,
            baseline + 0.12,
            f"BL-NCC {baseline:.2f}% (0 ms)",
            color="#686868",
            fontsize=6.2,
            va="bottom",
        )
        for method in methods:
            x = values[method]["runtime_ms"]
            y = 100 * values[method]["accuracy"]
            color = COLORS["DCTPR"] if method == "DCTPR" else COLORS.get(method, "#777777")
            size = 52 if method == "DCTPR" else 29
            marker = "*" if method == "DCTPR" else "o"
            zorder = 5 if method == "DCTPR" else 3
            ax.scatter(
                x,
                y,
                s=size,
                marker=marker,
                color=color,
                edgecolor="white",
                linewidth=0.45,
                zorder=zorder,
            )
            dx, dy = offsets[dataset][method]
            ax.annotate(
                LABELS[method],
                (x, y),
                xytext=(dx, dy),
                textcoords="offset points",
                fontsize=6.1,
                color=color,
                fontweight="bold" if method == "DCTPR" else "normal",
            )
            rows.append(
                {
                    "dataset": dataset,
                    "method": LABELS[method],
                    "accuracy_percent": f"{y:.6f}",
                    "runtime_ms": f"{x:.6f}",
                }
            )
        ax.set_xscale("log")
        ax.set_xlim(1.5, 2600)
        ax.grid(axis="y", color="#E5E5E5", linewidth=0.55)
        ax.set_title("CUB, 200-way" if dataset == "CUB" else "Stanford Dogs, 120-way")
        ax.set_xlabel("Task-head runtime per rotation (ms, log scale)")
        ax.set_ylim((64.8, 77.2) if dataset == "CUB" else (63.0, 72.2))
        ax.annotate(
            "50-ms budget",
            xy=(50, 1.0),
            xycoords=("data", "axes fraction"),
            xytext=(0, -4),
            textcoords="offset points",
            ha="center",
            va="top",
            fontsize=6.1,
            color="#8A6D3B",
        )
        ax.text(
            0.02,
            0.97,
            "higher accuracy\nlower runtime",
            transform=ax.transAxes,
            ha="left",
            va="top",
            fontsize=6.2,
            color="#555555",
        )
        strong_method = "TIM_ADM" if dataset == "CUB" else "MAP_RAW"
        speedup = values[strong_method]["runtime_ms"] / values["DCTPR"]["runtime_ms"]
        arrow_y = 75.45 if dataset == "CUB" else 71.45
        ax.annotate(
            "",
            xy=(values[strong_method]["runtime_ms"], arrow_y),
            xytext=(values["DCTPR"]["runtime_ms"], arrow_y),
            arrowprops={"arrowstyle": "<->", "color": COLORS["DCTPR"], "lw": 0.9},
        )
        ax.text(
            np.sqrt(
                values[strong_method]["runtime_ms"] * values["DCTPR"]["runtime_ms"]
            ),
            arrow_y + 0.13,
            f"{speedup:.1f}x faster",
            color=COLORS["DCTPR"],
            fontsize=6.1,
            fontweight="bold",
            ha="center",
            va="bottom",
        )
    axes[0].set_ylabel("Balanced accuracy (%)")
    axes[0].text(-0.15, 1.08, "a", transform=axes[0].transAxes, fontweight="bold", fontsize=8)
    axes[1].text(-0.15, 1.08, "b", transform=axes[1].transAxes, fontweight="bold", fontsize=8)
    fig.subplots_adjust(wspace=0.21)
    save_bundle(fig, "fig2_accuracy_efficiency")
    write_csv(
        SOURCE / "fig2_accuracy_efficiency.csv",
        ["dataset", "method", "accuracy_percent", "runtime_ms"],
        rows,
    )
    plt.close(fig)


def l2_normalize(array: np.ndarray) -> np.ndarray:
    values = np.asarray(array, dtype=np.float64)
    return values / np.maximum(np.linalg.norm(values, axis=1, keepdims=True), 1e-12)


def support_rotations(
    labels: np.ndarray, image_ids: np.ndarray
) -> list[tuple[np.ndarray, np.ndarray]]:
    """Match the archived protocol: each image is support exactly once."""
    ordered_by_class = []
    for label in np.unique(labels):
        indices = np.flatnonzero(labels == label)
        ordered_by_class.append(indices[np.argsort(image_ids[indices].astype(str))])
    class_sizes = {len(indices) for indices in ordered_by_class}
    if len(class_sizes) != 1:
        raise ValueError(f"Expected balanced episodes, found class sizes {class_sizes}")

    rotations = []
    for rotation in range(class_sizes.pop()):
        support = np.asarray([indices[rotation] for indices in ordered_by_class])
        query_mask = np.ones(len(labels), dtype=bool)
        query_mask[support] = False
        rotations.append((support, np.flatnonzero(query_mask)))
    return rotations


def balanced_sinkhorn(
    logits: np.ndarray, examples_per_class: int, iterations: int
) -> np.ndarray:
    shifted = logits - logits.max(axis=1, keepdims=True)
    assignment = np.exp(np.clip(shifted, -60.0, 0.0)) + 1e-12
    target_columns = np.full(logits.shape[1], float(examples_per_class))
    for _ in range(iterations):
        assignment /= np.maximum(assignment.sum(axis=1, keepdims=True), 1e-12)
        assignment *= target_columns / np.maximum(assignment.sum(axis=0), 1e-12)
    return assignment / np.maximum(assignment.sum(axis=1, keepdims=True), 1e-12)


def refinement_diagnostic_rows() -> tuple[list[dict], dict[str, str]]:
    """Recompute the frozen Dogs DCTPR trajectory for offline diagnostics."""
    cached_csv = SOURCE / "fig_mechanism_diagnostics.csv"
    cached_metadata = SOURCE / "fig_mechanism_diagnostics_metadata.json"
    if not DOGS_FEATURE_ROOT.is_dir():
        if not cached_csv.is_file() or not cached_metadata.is_file():
            raise FileNotFoundError(
                "Dogs feature arrays and cached mechanism source data are both missing"
            )
        with cached_csv.open("r", encoding="utf-8") as handle:
            rows = []
            for row in csv.DictReader(handle):
                rows.append(
                    {
                        "dataset": row["dataset"],
                        "episode": int(row["episode"]),
                        "rotation": int(row["rotation"]),
                        "refinement_step": int(row["refinement_step"]),
                        "prototype_cosine_error": float(
                            row["prototype_cosine_error"]
                        ),
                        "balanced_assignment_accuracy": float(
                            row["balanced_assignment_accuracy"]
                        ),
                    }
                )
        metadata = load_json(cached_metadata)
        return rows, metadata.get("source_sha256", {})

    rows = []
    source_hashes = {}
    for episode in (1, 2, 3):
        b_dir = DOGS_FEATURE_ROOT / f"b_episode_{episode}"
        l_dir = DOGS_FEATURE_ROOT / f"l_episode_{episode}"
        for path in (
            b_dir / "cls.npy",
            l_dir / "cls.npy",
            b_dir / "labels.npy",
            b_dir / "image_ids.npy",
        ):
            if not path.is_file():
                raise FileNotFoundError(f"Missing diagnostic source: {path}")
            source_hashes[str(path.relative_to(PROJECT_ROOT))] = sha256(path)

        b = l2_normalize(np.load(b_dir / "cls.npy", mmap_mode="r"))
        l = l2_normalize(np.load(l_dir / "cls.npy", mmap_mode="r"))
        labels = np.load(b_dir / "labels.npy")
        image_ids = np.load(b_dir / "image_ids.npy")
        if not np.array_equal(labels, np.load(l_dir / "labels.npy")):
            raise RuntimeError(f"B/L label mismatch in Dogs episode {episode}")
        if not np.array_equal(image_ids, np.load(l_dir / "image_ids.npy")):
            raise RuntimeError(f"B/L image-id mismatch in Dogs episode {episode}")
        features = l2_normalize(np.concatenate([b, l], axis=1))

        for rotation, (support, query) in enumerate(
            support_rotations(labels, image_ids)
        ):
            support_labels = labels[support]
            query_labels = labels[query]
            support_x = features[support]
            query_x = features[query]
            examples_per_class = len(query) // len(support)
            true_query_centers = np.stack(
                [
                    l2_normalize(
                        query_x[query_labels == label].mean(axis=0, keepdims=True)
                    )[0]
                    for label in support_labels
                ]
            )

            prototypes = support_x.copy()
            for step in range(DIAGNOSTIC_SETTINGS["refinement_steps"] + 1):
                assignment = balanced_sinkhorn(
                    (query_x @ prototypes.T) / DIAGNOSTIC_SETTINGS["temperature"],
                    examples_per_class,
                    DIAGNOSTIC_SETTINGS["sinkhorn_iterations"],
                )
                predictions = support_labels[assignment.argmax(axis=1)]
                rows.append(
                    {
                        "dataset": "Stanford Dogs official training",
                        "episode": episode,
                        "rotation": rotation,
                        "refinement_step": step,
                        "prototype_cosine_error": float(
                            np.mean(
                                1.0
                                - np.sum(
                                    prototypes * true_query_centers,
                                    axis=1,
                                )
                            )
                        ),
                        "balanced_assignment_accuracy": float(
                            np.mean(predictions == query_labels)
                        ),
                    }
                )
                if step == DIAGNOSTIC_SETTINGS["refinement_steps"]:
                    continue
                query_centers = (assignment.T @ query_x) / np.maximum(
                    assignment.sum(axis=0)[:, None], 1e-12
                )
                mix = DIAGNOSTIC_SETTINGS["support_query_mix"]
                prototypes = l2_normalize(
                    (1.0 - mix) * support_x + mix * query_centers
                )
    return rows, source_hashes


def plot_mechanism_diagnostics(dogs_reference: dict) -> None:
    rows, source_hashes = refinement_diagnostic_rows()
    steps = np.arange(DIAGNOSTIC_SETTINGS["refinement_steps"] + 1)
    error = np.asarray(
        [
            [
                row["prototype_cosine_error"]
                for row in rows
                if row["episode"] == episode and row["rotation"] == rotation
            ]
            for episode in (1, 2, 3)
            for rotation in range(10)
        ]
    )
    accuracy = 100.0 * np.asarray(
        [
            [
                row["balanced_assignment_accuracy"]
                for row in rows
                if row["episode"] == episode and row["rotation"] == rotation
            ]
            for episode in (1, 2, 3)
            for rotation in range(10)
        ]
    )
    expected_start = 100.0 * dogs_reference["BL_SINKHORN"]["accuracy"]
    expected_end = 100.0 * dogs_reference["DCTPR"]["accuracy"]
    if not np.isclose(accuracy[:, 0].mean(), expected_start, atol=1e-8):
        raise RuntimeError("Diagnostic T=0 does not reproduce BL-Sinkhorn")
    if not np.isclose(accuracy[:, -1].mean(), expected_end, atol=1e-8):
        raise RuntimeError("Diagnostic T=3 does not reproduce DCTPR")

    fig, axes = plt.subplots(1, 2, figsize=(7.05, 2.25))
    panels = (
        (
            axes[0],
            error,
            "Prototype cosine error",
            "Prototypes approach query class centers",
            f"{100.0 * (1.0 - error[:, -1].mean() / error[:, 0].mean()):.1f}% lower",
        ),
        (
            axes[1],
            accuracy,
            "Balanced assignment accuracy (%)",
            "Assignments become more accurate",
            f"+{accuracy[:, -1].mean() - accuracy[:, 0].mean():.2f} pp",
        ),
    )
    for ax, values, ylabel, title, endpoint_label in panels:
        mean = values.mean(axis=0)
        rotation_sd = values.std(axis=0, ddof=1)
        ax.fill_between(
            steps,
            mean - rotation_sd,
            mean + rotation_sd,
            color="#E8B6A6",
            alpha=0.45,
            linewidth=0,
        )
        ax.plot(
            steps,
            mean,
            color=COLORS["DCTPR"],
            marker="o",
            markersize=4.2,
            linewidth=1.7,
        )
        ax.set_xticks(steps)
        ax.set_xlabel("Refinement step")
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.grid(axis="y", color="#E5E5E5", linewidth=0.55)
        ax.annotate(
            endpoint_label,
            xy=(steps[-1], mean[-1]),
            xytext=(-4, 14),
            textcoords="offset points",
            ha="right",
            va="bottom",
            fontsize=6.4,
            color=COLORS["DCTPR"],
            fontweight="bold",
            arrowprops={"arrowstyle": "-", "color": COLORS["DCTPR"], "lw": 0.7},
        )
        ax.text(
            0.02,
            0.04,
            "mean +/- SD, n = 30 rotations",
            transform=ax.transAxes,
            fontsize=5.9,
            color="#666666",
        )
    axes[0].text(-0.15, 1.08, "a", transform=axes[0].transAxes, fontweight="bold", fontsize=8)
    axes[1].text(-0.15, 1.08, "b", transform=axes[1].transAxes, fontweight="bold", fontsize=8)
    fig.subplots_adjust(wspace=0.28)
    save_bundle(fig, "fig_mechanism_diagnostics")
    write_csv(
        SOURCE / "fig_mechanism_diagnostics.csv",
        [
            "dataset",
            "episode",
            "rotation",
            "refinement_step",
            "prototype_cosine_error",
            "balanced_assignment_accuracy",
        ],
        rows,
    )
    metadata = {
        "status": "OFFLINE_MECHANISM_DIAGNOSTIC",
        "dataset": "Stanford Dogs official-training episodes 1--3",
        "episodes": 3,
        "support_rotations": 30,
        "classes_per_episode": 120,
        "settings": DIAGNOSTIC_SETTINGS,
        "metric_definitions": {
            "prototype_cosine_error": (
                "mean over classes of one minus cosine similarity between the "
                "current prototype and the true query-class center"
            ),
            "balanced_assignment_accuracy": (
                "fraction of query images whose maximum-mass balanced assignment "
                "matches the query label"
            ),
        },
        "query_label_boundary": (
            "Query labels are used only offline to compute diagnostic true class "
            "centers and score assignments; they are never passed to DCTPR."
        ),
        "replicate_note": (
            "Rotations share images; standard-deviation bands describe rotation-level "
            "trajectory variability and are not independent-sample inference."
        ),
        "endpoint_validation_percent": {
            "computed_step_0": float(accuracy[:, 0].mean()),
            "archived_bl_sinkhorn": expected_start,
            "computed_step_3": float(accuracy[:, -1].mean()),
            "archived_dctpr": expected_end,
        },
        "source_sha256": source_hashes,
    }
    (SOURCE / "fig_mechanism_diagnostics_metadata.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    plt.close(fig)


def per_rotation_gains(summary: dict, dataset: str) -> list[dict]:
    rows = []
    for episode in summary["episodes"]:
        for rotation in episode["rotations"]:
            metrics = rotation["metrics"]
            rows.append(
                {
                    "dataset": dataset,
                    "episode": int(episode["episode"]),
                    "rotation": int(rotation["rotation"]),
                    "gain_pp": 100 * (metrics["DCTPR"] - metrics["BL_NCC"]),
                }
            )
    return rows


def stress_means(stress: dict) -> dict[str, dict[str, float]]:
    grouped: dict[str, dict[str, list[float]]] = {}
    for result in stress["results"]:
        regime = result["regime"]
        grouped.setdefault(regime, {})
        for method in ["BL_NCC", "TIM_ADM", "DCTPR_UNIFORM", "DCTPR_ORACLE"]:
            grouped[regime].setdefault(method, []).append(
                result["aggregate"][method]["macro_balanced_accuracy"]
            )
    return {
        regime: {method: float(np.mean(values)) for method, values in methods.items()}
        for regime, methods in grouped.items()
    }


def plot_robustness(cub_summary: dict, dogs_summary: dict, stress: dict) -> None:
    fig, (ax_gain, ax_stress) = plt.subplots(
        1, 2, figsize=(7.05, 2.65), gridspec_kw={"width_ratios": [1.15, 1]}
    )

    gains = per_rotation_gains(cub_summary, "CUB") + per_rotation_gains(
        dogs_summary, "Dogs"
    )
    labels = ["CUB E1", "CUB E2", "CUB E3", "Dogs E1", "Dogs E2", "Dogs E3"]
    gain_rows = []
    rng = np.random.default_rng(20260729)
    for pos, label in enumerate(labels):
        dataset, episode_text = label.split()
        episode = int(episode_text[1:])
        vals = np.array(
            [
                row["gain_pp"]
                for row in gains
                if row["dataset"] == dataset and row["episode"] == episode
            ]
        )
        jitter = rng.uniform(-0.12, 0.12, size=len(vals))
        color = "#4C78A8" if dataset == "CUB" else "#6D8F72"
        ax_gain.scatter(
            np.full(len(vals), pos) + jitter,
            vals,
            s=13,
            alpha=0.62,
            color=color,
            edgecolor="none",
        )
        ax_gain.plot(
            [pos - 0.22, pos + 0.22],
            [vals.mean(), vals.mean()],
            color=COLORS["DCTPR"],
            linewidth=2.0,
            solid_capstyle="round",
        )
        for row in [r for r in gains if r["dataset"] == dataset and r["episode"] == episode]:
            gain_rows.append(row)
    ax_gain.axhline(0, color="#777777", linewidth=0.7)
    ax_gain.set_xticks(range(len(labels)), labels, rotation=22, ha="right")
    ax_gain.set_ylabel("DCTPR gain over BL-NCC (pp)")
    ax_gain.set_title("Gain is positive in every rotation")
    ax_gain.grid(axis="y", color="#E5E5E5", linewidth=0.55)
    cub_means = mean_methods(cub_summary)
    prior = stress_means(stress)
    regimes = ["Balanced", "Mild 3/9", "Severe 1--9"]
    x = np.arange(3)
    series = {
        "BL-NCC": [
            cub_means["BL_NCC"]["accuracy"],
            prior["MILD_3_9"]["BL_NCC"],
            prior["SEVERE_1_9"]["BL_NCC"],
        ],
        "TIM-ADM": [
            cub_means["TIM_ADM"]["accuracy"],
            prior["MILD_3_9"]["TIM_ADM"],
            prior["SEVERE_1_9"]["TIM_ADM"],
        ],
        "DCTPR, uniform": [
            cub_means["DCTPR"]["accuracy"],
            prior["MILD_3_9"]["DCTPR_UNIFORM"],
            prior["SEVERE_1_9"]["DCTPR_UNIFORM"],
        ],
        "DCTPR, oracle": [
            cub_means["DCTPR"]["accuracy"],
            prior["MILD_3_9"]["DCTPR_ORACLE"],
            prior["SEVERE_1_9"]["DCTPR_ORACLE"],
        ],
    }
    style = {
        "BL-NCC": ("#777777", "o", "-"),
        "TIM-ADM": ("#252525", "s", "-"),
        "DCTPR, uniform": (COLORS["DCTPR"], "*", "-"),
        "DCTPR, oracle": (COLORS["DCTPR_ORACLE"], "^", "--"),
    }
    stress_rows = []
    for label, values in series.items():
        color, marker, linestyle = style[label]
        values_pct = 100 * np.array(values)
        ax_stress.plot(
            x,
            values_pct,
            color=color,
            marker=marker,
            markersize=6 if marker == "*" else 4.2,
            linewidth=1.35,
            linestyle=linestyle,
            label=label,
        )
        for regime, value in zip(regimes, values_pct):
            stress_rows.append(
                {
                    "regime": regime,
                    "method": label,
                    "macro_balanced_accuracy_percent": f"{value:.6f}",
                }
            )
    ax_stress.set_xticks(x, regimes)
    ax_stress.set_ylabel("Macro balanced accuracy (%)")
    ax_stress.set_title("Uniform-prior gain collapses under imbalance")
    ax_stress.set_ylim(66.5, 77.2)
    ax_stress.grid(axis="y", color="#E5E5E5", linewidth=0.55)
    ax_stress.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.18),
        ncol=2,
        fontsize=6.0,
        handlelength=2.2,
        columnspacing=1.4,
    )
    ax_stress.text(
        0.98,
        0.03,
        "oracle counts are diagnostic only",
        transform=ax_stress.transAxes,
        ha="right",
        va="bottom",
        fontsize=5.9,
        color="#2E8B70",
    )

    ax_gain.text(-0.14, 1.08, "a", transform=ax_gain.transAxes, fontweight="bold", fontsize=8)
    ax_stress.text(-0.14, 1.08, "b", transform=ax_stress.transAxes, fontweight="bold", fontsize=8)
    fig.subplots_adjust(wspace=0.23)
    save_bundle(fig, "fig3_stability_prior")
    write_csv(
        SOURCE / "fig3_rotation_gains.csv",
        ["dataset", "episode", "rotation", "gain_pp"],
        gain_rows,
    )
    write_csv(
        SOURCE / "fig3_prior_stress.csv",
        ["regime", "method", "macro_balanced_accuracy_percent"],
        stress_rows,
    )
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
            "font.size": 7,
            "axes.titlesize": 8,
            "axes.titleweight": "bold",
            "axes.labelsize": 7,
            "xtick.labelsize": 6.2,
            "ytick.labelsize": 6.2,
            "axes.spines.right": False,
            "axes.spines.top": False,
            "axes.linewidth": 0.75,
            "legend.frameon": False,
            "pdf.fonttype": 42,
            "svg.fonttype": "none",
        }
    )
    cub_summary = load_json(CUB_PATH)
    dogs_summary = load_json(DOGS_PATH)
    stress = load_json(STRESS_PATH)
    plot_training_examples()
    plot_pareto(mean_methods(cub_summary), mean_methods(dogs_summary))
    plot_mechanism_diagnostics(mean_methods(dogs_summary))
    plot_robustness(cub_summary, dogs_summary, stress)


if __name__ == "__main__":
    main()
