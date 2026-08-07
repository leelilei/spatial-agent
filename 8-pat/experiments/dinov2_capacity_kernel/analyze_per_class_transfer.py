"""PAT-K-260806-010: per-class transfer and paired significance for DCTPR.

Post-hoc analysis of archived development-episode predictions. Performs no new
inference and touches no official-test artifact. See
``PAT-K-260806-010_protocol.json`` for the frozen protocol.
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.stats import binomtest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = ROOT / "outputs/researchwrite/dual_capacity_transductive_oneshot/figures/source_data"

DATASETS = {
    "cub": {
        "label": "CUB-200-2011",
        "ways": 200,
        "dir": ROOT / "raw/experiments/2026.07.29_CUB_PublishedBaselines_PAT-K-260729-004/formal",
        "strongest": "TIM_ADM",
    },
    "dogs": {
        "label": "Stanford Dogs",
        "ways": 120,
        "dir": ROOT / "raw/experiments/2026.07.29_StanfordDogs_DCTPR_PAT-K-260729-006/formal",
        "strongest": "MAP_RAW",
    },
}
EPISODES = (1, 2, 3)
BASELINE = "BL_NCC"
METHOD = "DCTPR"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def mcnemar_exact(correct_a: np.ndarray, correct_b: np.ndarray) -> dict:
    """Two-sided exact McNemar on paired binary correctness vectors."""
    only_a = int(np.sum(correct_a & ~correct_b))
    only_b = int(np.sum(~correct_a & correct_b))
    discordant = only_a + only_b
    if discordant == 0:
        return {"only_a": 0, "only_b": 0, "discordant": 0, "p_value": 1.0}
    p = binomtest(only_a, discordant, 0.5, alternative="two-sided").pvalue
    return {
        "only_a": only_a,
        "only_b": only_b,
        "discordant": discordant,
        "p_value": float(p),
    }


def load_dataset(spec: dict) -> tuple[dict[str, np.ndarray], np.ndarray, dict[str, str]]:
    """Stack per-rotation correctness across episodes.

    Returns per-method boolean arrays of shape (episodes, rotations, queries),
    the shared query-label array of shape (queries,), and file digests.
    """
    per_method: dict[str, list[np.ndarray]] = {}
    labels_ref: np.ndarray | None = None
    digests: dict[str, str] = {}

    for episode in EPISODES:
        path = spec["dir"] / f"episode_{episode}_predictions.npz"
        digests[path.name] = sha256(path)
        data = np.load(path)
        labels = data["query_labels"]
        if not all((labels[0] == labels[i]).all() for i in range(labels.shape[0])):
            raise AssertionError(f"{path}: query labels vary across rotations")
        if labels_ref is None:
            labels_ref = labels[0]
        elif not np.array_equal(labels_ref, labels[0]):
            raise AssertionError(f"{path}: query label order differs across episodes")

        for key in data.files:
            if not key.endswith("_predictions"):
                continue
            method = key[: -len("_predictions")]
            per_method.setdefault(method, []).append(data[key] == labels)

    assert labels_ref is not None
    stacked = {m: np.stack(v) for m, v in per_method.items()}
    return stacked, labels_ref, digests


def per_class_accuracy(correct: np.ndarray, labels: np.ndarray, ways: int) -> np.ndarray:
    """Mean per-class accuracy over episodes and rotations."""
    flat = correct.reshape(-1, correct.shape[-1])
    out = np.empty((flat.shape[0], ways), dtype=float)
    for cls in range(ways):
        out[:, cls] = flat[:, labels == cls].mean(axis=1)
    return out.mean(axis=0)


def analyse(name: str, spec: dict) -> tuple[dict, list[dict], list[dict]]:
    correct, labels, digests = load_dataset(spec)
    ways = spec["ways"]
    strongest = spec["strongest"]

    acc = {m: per_class_accuracy(c, labels, ways) for m, c in correct.items()}
    delta_bl = acc[METHOD] - acc[BASELINE]
    delta_strong = acc[METHOD] - acc[strongest]

    class_rows = [
        {
            "dataset": spec["label"],
            "class_id": cls,
            "bl_ncc_accuracy": round(float(acc[BASELINE][cls]), 6),
            "dctpr_accuracy": round(float(acc[METHOD][cls]), 6),
            "strongest_method": strongest,
            "strongest_accuracy": round(float(acc[strongest][cls]), 6),
            "dctpr_minus_bl_ncc_pp": round(float(delta_bl[cls] * 100), 4),
            "dctpr_minus_strongest_pp": round(float(delta_strong[cls] * 100), 4),
            "transfer": (
                "positive" if delta_bl[cls] > 0 else "negative" if delta_bl[cls] < 0 else "neutral"
            ),
        }
        for cls in range(ways)
    ]

    # Paired significance, computed within each rotation where query images are distinct.
    paired_rows: list[dict] = []
    for pair_name, other in (("vs_bl_ncc", BASELINE), ("vs_strongest", strongest)):
        for ep_idx, episode in enumerate(EPISODES):
            for rot in range(correct[METHOD].shape[1]):
                stats = mcnemar_exact(
                    correct[METHOD][ep_idx, rot], correct[other][ep_idx, rot]
                )
                paired_rows.append(
                    {
                        "dataset": spec["label"],
                        "comparison": pair_name,
                        "reference_method": other,
                        "episode": episode,
                        "rotation": rot,
                        "dctpr_only_correct": stats["only_a"],
                        "reference_only_correct": stats["only_b"],
                        "discordant": stats["discordant"],
                        "p_value": round(stats["p_value"], 8),
                        "significant_at_0.05": bool(stats["p_value"] < 0.05),
                    }
                )

    def pair_summary(pair_name: str) -> dict:
        rows = [r for r in paired_rows if r["comparison"] == pair_name]
        favours = sum(1 for r in rows if r["dctpr_only_correct"] > r["reference_only_correct"])
        sig = [r for r in rows if r["significant_at_0.05"]]
        sig_favour = sum(
            1 for r in sig if r["dctpr_only_correct"] > r["reference_only_correct"]
        )
        return {
            "rotations": len(rows),
            "rotations_favouring_dctpr": favours,
            "rotations_significant_at_0.05": len(sig),
            "significant_and_favouring_dctpr": sig_favour,
            "significant_and_favouring_reference": len(sig) - sig_favour,
            "max_p_value_among_significant": (
                round(max(r["p_value"] for r in sig), 8) if sig else None
            ),
        }

    # Error overlap against the strongest matched solver, pooled over all rotations.
    err_m = ~correct[METHOD].reshape(-1)
    err_s = ~correct[strongest].reshape(-1)
    both = int(np.sum(err_m & err_s))
    union = int(np.sum(err_m | err_s))

    negatives = [r for r in class_rows if r["transfer"] == "negative"]
    worst = min(class_rows, key=lambda r: r["dctpr_minus_bl_ncc_pp"])

    summary = {
        "dataset": spec["label"],
        "ways": ways,
        "episodes": list(EPISODES),
        "rotations_per_episode": int(correct[METHOD].shape[1]),
        "queries_per_rotation": int(correct[METHOD].shape[2]),
        "overall": {
            m: round(float(a.mean() * 100), 4) for m, a in sorted(acc.items())
        },
        "class_transfer_vs_bl_ncc": {
            "positive": sum(1 for r in class_rows if r["transfer"] == "positive"),
            "neutral": sum(1 for r in class_rows if r["transfer"] == "neutral"),
            "negative": len(negatives),
            "negative_fraction": round(len(negatives) / ways, 4),
            "mean_delta_pp": round(float(delta_bl.mean() * 100), 4),
            "median_delta_pp": round(float(np.median(delta_bl) * 100), 4),
            "worst_class_id": worst["class_id"],
            "worst_class_harm_pp": worst["dctpr_minus_bl_ncc_pp"],
            "mean_harm_among_negative_pp": (
                round(float(np.mean([r["dctpr_minus_bl_ncc_pp"] for r in negatives])), 4)
                if negatives
                else 0.0
            ),
            "classes_at_zero_accuracy_dctpr": int(np.sum(acc[METHOD] == 0)),
            "classes_at_zero_accuracy_bl_ncc": int(np.sum(acc[BASELINE] == 0)),
        },
        "class_comparison_vs_strongest": {
            "strongest_method": strongest,
            "classes_dctpr_better": int(np.sum(delta_strong > 0)),
            "classes_equal": int(np.sum(delta_strong == 0)),
            "classes_dctpr_worse": int(np.sum(delta_strong < 0)),
            "mean_delta_pp": round(float(delta_strong.mean() * 100), 4),
        },
        "paired_significance": {
            "test": "two-sided exact McNemar within a single support rotation",
            "vs_bl_ncc": pair_summary("vs_bl_ncc"),
            "vs_strongest": pair_summary("vs_strongest"),
        },
        "error_overlap_vs_strongest": {
            "strongest_method": strongest,
            "dctpr_error_rate": round(float(err_m.mean()), 6),
            "strongest_error_rate": round(float(err_s.mean()), 6),
            "joint_error_rate": round(both / err_m.size, 6),
            "jaccard": round(both / union, 6) if union else None,
            "dctpr_only_error_rate": round(float(np.sum(err_m & ~err_s) / err_m.size), 6),
            "strongest_only_error_rate": round(float(np.sum(err_s & ~err_m) / err_m.size), 6),
        },
        "input_digests": digests,
    }
    return summary, class_rows, paired_rows


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    summaries, class_rows, paired_rows = {}, [], []
    for name, spec in DATASETS.items():
        summary, classes, paired = analyse(name, spec)
        summaries[name] = summary
        class_rows.extend(classes)
        paired_rows.extend(paired)
        tr = summary["class_transfer_vs_bl_ncc"]
        print(
            f"{summary['dataset']}: DCTPR {summary['overall'][METHOD]:.2f}% "
            f"vs BL-NCC {summary['overall'][BASELINE]:.2f}% | "
            f"positive/neutral/negative classes {tr['positive']}/{tr['neutral']}/{tr['negative']} | "
            f"worst-class harm {tr['worst_class_harm_pp']:.2f}pp"
        )
        sig = summary["paired_significance"]
        print(
            f"  McNemar vs BL-NCC: {sig['vs_bl_ncc']['significant_and_favouring_dctpr']}"
            f"/{sig['vs_bl_ncc']['rotations']} rotations significant and favouring DCTPR; "
            f"vs {spec['strongest']}: "
            f"{sig['vs_strongest']['significant_and_favouring_reference']}"
            f"/{sig['vs_strongest']['rotations']} significant and favouring the reference"
        )

    payload = {
        "experiment_id": "PAT-K-260806-010",
        "analysis": "post-hoc per-class transfer and paired significance",
        "official_test_used": False,
        "protocol": "experiments/dinov2_capacity_kernel/PAT-K-260806-010_protocol.json",
        "caveats": [
            "Support rotations reuse episode images; rotation-level tests are reported "
            "individually and never pooled into one p-value.",
            "McNemar tests paired decisions within one rotation, not the cross-episode mean gap.",
            "Development episodes only; official-test per-query predictions were never archived.",
        ],
        "datasets": summaries,
    }
    (OUT / "per_class_transfer_summary.json").write_text(json.dumps(payload, indent=2) + "\n")
    write_csv(OUT / "per_class_transfer.csv", class_rows)
    write_csv(OUT / "paired_significance.csv", paired_rows)
    print(f"\nwrote 3 files to {OUT}")


if __name__ == "__main__":
    main()
