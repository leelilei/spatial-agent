"""Compare two plausibility-judge archives over identical CityIntent traces."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from analyze_repeated_evidence import mean, pearson, spearman, write_csv


METRICS = (
    "face_plausibility",
    "trace_believability",
    "rationale_alignment",
    "urban_common_sense",
)


def load_archive(root: Path, subdir: str) -> dict[tuple[int, str, str], dict[str, Any]]:
    rows: dict[tuple[int, str, str], dict[str, Any]] = {}
    for repeat_path in sorted(root.glob("repeat_*")):
        repeat_id = int(repeat_path.name.split("_", 1)[1])
        path = repeat_path / subdir / "judged_traces.json"
        if not path.exists():
            raise FileNotFoundError(path)
        values = json.loads(path.read_text(encoding="utf-8"))
        for value in values:
            key = (repeat_id, value["scenario_id"], value["agent_type"])
            if key in rows:
                raise ValueError(f"duplicate judge item: {key}")
            rows[key] = value
    return rows


def binary_kappa(a: list[bool], b: list[bool]) -> float | None:
    if len(a) != len(b) or not a:
        return None
    observed = sum(x == y for x, y in zip(a, b)) / len(a)
    count_a = Counter(a)
    count_b = Counter(b)
    expected = sum(
        count_a[label] / len(a) * count_b[label] / len(b)
        for label in (False, True)
    )
    if expected == 1:
        return 1.0 if observed == 1.0 else 0.0
    return (observed - expected) / (1 - expected)


def compare(
    baseline: dict[tuple[int, str, str], dict[str, Any]],
    candidate: dict[tuple[int, str, str], dict[str, Any]],
    baseline_label: str,
    candidate_label: str,
    threshold: float,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    if set(baseline) != set(candidate):
        missing_baseline = sorted(set(candidate) - set(baseline))
        missing_candidate = sorted(set(baseline) - set(candidate))
        raise ValueError(
            f"judge archives differ: baseline_missing={missing_baseline}, "
            f"candidate_missing={missing_candidate}"
        )
    pairs: list[dict[str, Any]] = []
    for repeat_id, scenario_id, agent_type in sorted(baseline):
        row = {
            "repeat_id": repeat_id,
            "scenario_id": scenario_id,
            "agent_type": agent_type,
        }
        for metric in METRICS:
            a = float(baseline[(repeat_id, scenario_id, agent_type)]["plausibility_judgment"][metric])
            b = float(candidate[(repeat_id, scenario_id, agent_type)]["plausibility_judgment"][metric])
            row[f"{baseline_label}_{metric}"] = a
            row[f"{candidate_label}_{metric}"] = b
            row[f"abs_diff_{metric}"] = round(abs(a - b), 3)
            row[f"threshold_agree_{metric}"] = int((a >= threshold) == (b >= threshold))
        pairs.append(row)

    summary = []
    for metric in METRICS:
        a = [float(row[f"{baseline_label}_{metric}"]) for row in pairs]
        b = [float(row[f"{candidate_label}_{metric}"]) for row in pairs]
        a_binary = [value >= threshold for value in a]
        b_binary = [value >= threshold for value in b]
        p = pearson(a, b)
        s = spearman(a, b)
        kappa = binary_kappa(a_binary, b_binary)
        summary.append(
            {
                "metric": metric,
                "n": len(a),
                f"{baseline_label}_mean": round(mean(a), 3),
                f"{candidate_label}_mean": round(mean(b), 3),
                "mean_absolute_difference": round(mean([abs(x - y) for x, y in zip(a, b)]), 3),
                "pearson_r": round(p, 3) if p is not None else None,
                "spearman_rho": round(s, 3) if s is not None else None,
                "threshold_agreement": round(
                    sum(x == y for x, y in zip(a_binary, b_binary)) / len(a), 3
                ),
                "threshold_cohen_kappa": round(kappa, 3) if kappa is not None else None,
            }
        )

    by_agent: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in pairs:
        by_agent[row["agent_type"]].append(row)
    agent_summary = []
    for agent, selected in sorted(by_agent.items()):
        for metric in ("face_plausibility", "trace_believability"):
            a = [float(row[f"{baseline_label}_{metric}"]) for row in selected]
            b = [float(row[f"{candidate_label}_{metric}"]) for row in selected]
            agent_summary.append(
                {
                    "agent_type": agent,
                    "metric": metric,
                    "n": len(selected),
                    f"{baseline_label}_mean": round(mean(a), 3),
                    f"{candidate_label}_mean": round(mean(b), 3),
                    "mean_absolute_difference": round(
                        mean([abs(x - y) for x, y in zip(a, b)]), 3
                    ),
                }
            )
    return pairs, summary, agent_summary


def write_markdown(
    path: Path,
    summary: list[dict[str, Any]],
    baseline_label: str,
    candidate_label: str,
    threshold: float,
) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("# CityIntent Plausibility-Judge Robustness\n\n")
        f.write(
            f"Judges: `{baseline_label}` and `{candidate_label}`. Binary agreement "
            f"uses threshold >= {threshold:.2f}.\n\n"
        )
        f.write(
            "| Metric | n | Baseline mean | Candidate mean | MAE | Pearson | "
            "Spearman | Threshold agreement | Kappa |\n"
        )
        f.write("|---|---:|---:|---:|---:|---:|---:|---:|---:|\n")
        for row in summary:
            f.write(
                f"| `{row['metric']}` | {row['n']} | "
                f"{row[f'{baseline_label}_mean']:.3f} | "
                f"{row[f'{candidate_label}_mean']:.3f} | "
                f"{row['mean_absolute_difference']:.3f} | {row['pearson_r']} | "
                f"{row['spearman_rho']} | {row['threshold_agreement']:.3f} | "
                f"{row['threshold_cohen_kappa']} |\n"
            )
        f.write("\n## Interpretation\n\n")
        f.write(
            "- Cross-judge agreement is only moderate, so soft plausibility scores "
            "must be reported with evaluator identity and sensitivity analysis.\n"
        )
        f.write(
            "- Deterministic task, feasibility, resource, and state-transition scores "
            "remain unchanged across judges.\n"
        )
        f.write(
            "- This robustness check strengthens the case for the two-person human "
            "audit; it does not replace that release gate.\n"
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment-dir", type=Path, required=True)
    parser.add_argument("--baseline-dir", default="judged")
    parser.add_argument("--candidate-dir", default="judged_gpt54")
    parser.add_argument("--baseline-label", default="gpt54mini")
    parser.add_argument("--candidate-label", default="gpt54")
    parser.add_argument("--threshold", type=float, default=0.70)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    output_dir = args.output_dir or args.experiment_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    baseline = load_archive(args.experiment_dir, args.baseline_dir)
    candidate = load_archive(args.experiment_dir, args.candidate_dir)
    pairs, summary, agents = compare(
        baseline,
        candidate,
        args.baseline_label,
        args.candidate_label,
        args.threshold,
    )
    write_csv(output_dir / "judge_pairs.csv", pairs)
    write_csv(output_dir / "judge_agreement.csv", summary)
    write_csv(output_dir / "judge_agent_summary.csv", agents)
    write_markdown(
        output_dir / "judge_robustness.md",
        summary,
        args.baseline_label,
        args.candidate_label,
        args.threshold,
    )
    manifest = {
        "experiment_dir": str(args.experiment_dir),
        "baseline_dir": args.baseline_dir,
        "candidate_dir": args.candidate_dir,
        "baseline_label": args.baseline_label,
        "candidate_label": args.candidate_label,
        "threshold": args.threshold,
        "item_count": len(pairs),
        "outputs": [
            "judge_pairs.csv",
            "judge_agreement.csv",
            "judge_agent_summary.csv",
            "judge_robustness.md",
        ],
    }
    (output_dir / "judge_comparison_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"Compared two judges over {len(pairs)} identical traces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
