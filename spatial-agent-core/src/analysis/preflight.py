"""v7 预实验任务、评分与报告辅助模块。"""

from __future__ import annotations

import json
import math
import re
import shutil
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd


TASK_FAMILIES = [
    "comprehension",
    "behavioral_inference",
    "prompt_position",
    "reverse_inference_audit",
    "lexical_norming",
    "coding_pilot_llm",
]

CHOICE_TASK_FAMILIES = {
    "comprehension",
    "behavioral_inference",
    "prompt_position",
    "reverse_inference_audit",
}


@dataclass(frozen=True)
class PreflightPaths:
    root: Path
    tasks: Path
    raw: Path
    scored: Path
    reports: Path
    metrics: Path
    mic: Path
    convergence: Path


def resolve_preflight_paths(project_root: Path, config: dict[str, Any]) -> PreflightPaths:
    output_root = project_root / config["experiment"]["output_dir"]
    io_cfg = config["io"]
    return PreflightPaths(
        root=output_root,
        tasks=project_root / io_cfg["tasks_dir"],
        raw=project_root / io_cfg["raw_dir"],
        scored=project_root / io_cfg["scored_dir"],
        reports=project_root / io_cfg["reports_dir"],
        metrics=output_root / "metrics",
        mic=output_root / "mic",
        convergence=output_root / "convergence",
    )


def ensure_preflight_dirs(paths: PreflightPaths) -> None:
    for path in [
        paths.root,
        paths.tasks,
        paths.raw,
        paths.scored,
        paths.reports,
        paths.metrics,
        paths.mic,
        paths.convergence,
    ]:
        path.mkdir(parents=True, exist_ok=True)


def build_task_collections(
    metrics_frame: pd.DataFrame,
    *,
    prompt_positions: list[str],
    lexical_dimensions: list[str],
    lexical_labels: list[str],
    coding_subset_cfg: dict[str, Any],
) -> dict[str, list[dict[str, Any]]]:
    task_bundle = {family: [] for family in TASK_FAMILIES}
    indexed = metrics_frame.set_index("node_id")

    ordered_integration = metrics_frame.sort_values("integration", ascending=False)["node_id"].tolist()
    ordered_depth = metrics_frame.sort_values("mean_depth", ascending=False)["node_id"].tolist()

    comprehension_tasks = []
    for index, (left, right) in enumerate(zip(ordered_integration[:3], reversed(ordered_integration[-3:]))):
        comprehension_tasks.append(
            make_choice_task(
                task_family="comprehension",
                task_id=f"comp_{index+1:02d}_{left}_vs_{right}",
                question=f"在 {left} 和 {right} 之间，哪个位置更像全局枢纽？",
                options=[left, right],
                expected_answer=left,
                metadata={"evidence_metric": "integration"},
            )
        )

    behavioral_tasks = []
    for index, (left, right) in enumerate(zip(ordered_depth[:3], reversed(ordered_depth[-3:]))):
        behavioral_tasks.append(
            make_choice_task(
                task_family="behavioral_inference",
                task_id=f"beh_{index+1:02d}_{left}_vs_{right}",
                question=f"若角色想低调交流秘密，在 {left} 和 {right} 之间更适合去哪？",
                options=[left, right],
                expected_answer=left,
                metadata={"evidence_metric": "mean_depth"},
            )
        )

    prompt_tasks: list[dict[str, Any]] = []
    for base_task in [*comprehension_tasks, *behavioral_tasks]:
        for position in prompt_positions:
            prompt_tasks.append(
                {
                    **base_task,
                    "task_id": f"{base_task['task_id']}__{position}",
                    "task_family": "prompt_position",
                    "metadata": {
                        **base_task["metadata"],
                        "prompt_position": position,
                        "base_task_family": base_task["task_family"],
                    },
                }
            )

    reverse_tasks = []
    for _, row in metrics_frame.iterrows():
        description_stub = build_affordance_description(row.to_dict())
        for metric_name in ["integration", "mean_depth", "control_value"]:
            reverse_tasks.append(
                make_choice_task(
                    task_family="reverse_inference_audit",
                    task_id=f"rev_{row['node_id']}_{metric_name}",
                    question=f"这段描述更像在暗示该地点的 {metric_name} 处于 high、mid 还是 low？",
                    options=["high", "mid", "low"],
                    expected_answer=quantile_label(float(indexed.loc[row["node_id"], metric_name]), metrics_frame[metric_name]),
                    metadata={
                        "location": row["node_id"],
                        "metric_dimension": metric_name,
                        "description_stub": description_stub,
                    },
                )
            )

    lexical_tasks = []
    for label in lexical_labels:
        lexical_tasks.append(
            {
                "task_id": f"lex_{slugify(label)}",
                "task_family": "lexical_norming",
                "prompt_payload": {
                    "label": label,
                    "dimensions": lexical_dimensions,
                    "instruction": "请对该标签在每个维度上按 1-7 打分，并返回 JSON。",
                },
                "expected_answer": None,
                "metadata": {"label": label},
            }
        )

    coding_tasks = []
    for sample in coding_subset_cfg.get("samples", []):
        coding_tasks.append(
            {
                "task_id": f"coding_{sample['id']}",
                "task_family": "coding_pilot_llm",
                "prompt_payload": {
                    "behavior_text": sample["behavior_text"],
                    "labels": coding_subset_cfg["labels"],
                    "instruction": "请按指定标签对这条行为进行编码，并返回 JSON。",
                },
                "expected_answer": None,
                "metadata": {"sample_id": sample["id"]},
            }
        )

    task_bundle["comprehension"] = comprehension_tasks
    task_bundle["behavioral_inference"] = behavioral_tasks
    task_bundle["prompt_position"] = prompt_tasks
    task_bundle["reverse_inference_audit"] = reverse_tasks
    task_bundle["lexical_norming"] = lexical_tasks
    task_bundle["coding_pilot_llm"] = coding_tasks
    return task_bundle


def make_choice_task(
    *,
    task_family: str,
    task_id: str,
    question: str,
    options: list[str],
    expected_answer: str,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "task_id": task_id,
        "task_family": task_family,
        "prompt_payload": {
            "question": question,
            "options": options,
            "instruction": "请只返回 JSON，并在 answer 字段中填写一个候选项。",
        },
        "expected_answer": {"answer": expected_answer},
        "metadata": metadata or {},
    }


def build_affordance_description(row: dict[str, Any]) -> str:
    publicness = float(row.get("publicness", 0.0))
    privacy = float(row.get("privacy", 0.0))
    guardedness = float(row.get("guardedness", 0.0))
    label = str(row.get("node_id", "unknown"))

    descriptors: list[str] = []
    if publicness >= 0.7:
        descriptors.append("常被看作适合偶遇、短暂停留和随意交谈")
    elif privacy >= 0.7:
        descriptors.append("常被看作适合安静停留、低声交流和避免被打扰")
    else:
        descriptors.append("常被看作适合短暂停留和观察周围动态")

    if guardedness >= 0.7:
        descriptors.append("也容易让人联想到筛查来往者或维持秩序")
    elif guardedness <= 0.25:
        descriptors.append("整体氛围偏放松，不强调警戒或盘查")

    return f"{label}：这里{ '，'.join(descriptors) }。"


def write_task_bundle(
    tasks_dir: Path,
    task_bundle: dict[str, list[dict[str, Any]]],
    *,
    lexical_dimensions: list[str],
) -> None:
    tasks_dir.mkdir(parents=True, exist_ok=True)
    for family, rows in task_bundle.items():
        write_jsonl(tasks_dir / f"{family}_tasks.jsonl", rows)

    lexical_rows = [{"label": task["metadata"]["label"], **{dim: "" for dim in lexical_dimensions}} for task in task_bundle["lexical_norming"]]
    pd.DataFrame(lexical_rows).to_csv(tasks_dir / "lexical_norming_sheet.csv", index=False)


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def load_tasks(tasks_dir: Path) -> dict[str, dict[str, Any]]:
    tasks: dict[str, dict[str, Any]] = {}
    for family in TASK_FAMILIES:
        for row in read_jsonl(tasks_dir / f"{family}_tasks.jsonl"):
            tasks[row["task_id"]] = row
    return tasks


def normalize_offline_responses(
    responses_dir: Path,
    canonical_raw_dir: Path,
    *,
    default_model: str = "offline_import",
) -> list[Path]:
    if not responses_dir.exists():
        raise FileNotFoundError(f"Responses dir does not exist: {responses_dir}")

    imported_paths: list[Path] = []
    for family in TASK_FAMILIES:
        canonical_candidates = sorted(responses_dir.glob(f"{family}/*/responses.jsonl"))
        if canonical_candidates:
            for source_path in canonical_candidates:
                model = source_path.parent.name
                imported_paths.append(
                    normalize_response_file(
                        source_path,
                        canonical_raw_dir / family / model / "responses.jsonl",
                        family=family,
                        model=model,
                    )
                )
            continue

        flat_path = responses_dir / f"{family}.jsonl"
        if flat_path.exists():
            imported_paths.append(
                normalize_response_file(
                    flat_path,
                    canonical_raw_dir / family / default_model / "responses.jsonl",
                    family=family,
                    model=default_model,
                )
            )

    lexical_csv = responses_dir / "lexical_norming_sheet.csv"
    if lexical_csv.exists():
        target = canonical_raw_dir / "lexical_norming" / default_model / "manual_scores.csv"
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(lexical_csv, target)
        imported_paths.append(target)

    return imported_paths


def normalize_response_file(
    source_path: Path,
    target_path: Path,
    *,
    family: str,
    model: str,
) -> Path:
    rows = read_jsonl(source_path)
    normalized_rows = []
    for row in rows:
        normalized_rows.append(
            {
                "task_id": row["task_id"],
                "task_family": row.get("task_family", family),
                "model": row.get("model", model),
                "raw_text": row.get("raw_text", ""),
                "parsed_answer": row.get("parsed_answer"),
                "success": bool(row.get("success", row.get("parsed_answer") is not None or row.get("raw_text"))),
                "latency_ms": row.get("latency_ms"),
                "cache_hit": row.get("cache_hit"),
                "error": row.get("error"),
            }
        )
    write_jsonl(target_path, normalized_rows)
    return target_path


def load_all_responses(raw_dir: Path) -> dict[str, list[dict[str, Any]]]:
    family_rows: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for path in raw_dir.glob("*/*/responses.jsonl"):
        for row in read_jsonl(path):
            family = row.get("task_family") or path.parent.parent.name
            family_rows[family].append(row)
    return family_rows


def score_and_report_preflight(
    paths: PreflightPaths,
    config: dict[str, Any],
) -> dict[str, Any]:
    ensure_preflight_dirs(paths)
    tasks = load_tasks(paths.tasks)
    responses_by_family = load_all_responses(paths.raw)

    family_summaries: dict[str, Any] = {}
    for family in TASK_FAMILIES:
        rows = score_family(
            family,
            tasks,
            responses_by_family.get(family, []),
            lexical_csv_paths=list(paths.raw.glob("lexical_norming/*/manual_scores.csv")),
        )
        family_summaries[family] = write_scored_outputs(paths.scored, family, rows)

    decisions = build_decisions(paths, config, family_summaries)
    write_reports(paths.reports, decisions, family_summaries)
    return {
        "family_summaries": family_summaries,
        "decisions": decisions,
    }


def score_family(
    family: str,
    tasks: dict[str, dict[str, Any]],
    responses: list[dict[str, Any]],
    *,
    lexical_csv_paths: list[Path] | None = None,
) -> list[dict[str, Any]]:
    if family == "lexical_norming":
        return score_lexical_norming(tasks, responses, lexical_csv_paths or [])
    if family == "coding_pilot_llm":
        return score_coding_pilot(tasks, responses)

    rows = []
    for response in responses:
        task = tasks.get(response["task_id"])
        if task is None:
            continue
        predicted = extract_prediction(task, response)
        expected = task["expected_answer"]["answer"]
        row = {
            "task_id": task["task_id"],
            "task_family": family,
            "model": response.get("model", "unknown"),
            "success": bool(response.get("success", False)),
            "expected_answer": expected,
            "predicted_answer": predicted,
            "correct": predicted == expected,
            **task["metadata"],
        }
        rows.append(row)
    return rows


def score_lexical_norming(
    tasks: dict[str, dict[str, Any]],
    responses: list[dict[str, Any]],
    csv_paths: list[Path],
) -> list[dict[str, Any]]:
    rows = []
    for response in responses:
        task = tasks.get(response["task_id"])
        if task is None:
            continue
        parsed = extract_structured_answer(response)
        if not isinstance(parsed, dict):
            continue
        row = {
            "task_id": task["task_id"],
            "task_family": "lexical_norming",
            "model": response.get("model", "unknown"),
            "label": task["metadata"]["label"],
            "success": bool(response.get("success", False)),
        }
        for key, value in parsed.items():
            row[key] = value
        rows.append(row)

    for csv_path in csv_paths:
        frame = pd.read_csv(csv_path)
        model = csv_path.parent.name
        for _, record in frame.iterrows():
            row = {
                "task_id": f"lex_{slugify(str(record['label']))}",
                "task_family": "lexical_norming",
                "model": model,
                "label": str(record["label"]),
                "success": True,
            }
            for column in frame.columns:
                if column == "label":
                    continue
                value = record[column]
                row[column] = None if pd.isna(value) or value == "" else float(value)
            rows.append(row)
    return rows


def score_coding_pilot(tasks: dict[str, dict[str, Any]], responses: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for response in responses:
        task = tasks.get(response["task_id"])
        if task is None:
            continue
        parsed = extract_structured_answer(response)
        row = {
            "task_id": task["task_id"],
            "task_family": "coding_pilot_llm",
            "model": response.get("model", "unknown"),
            "success": bool(response.get("success", False)),
            **task["metadata"],
        }
        if isinstance(parsed, dict):
            row.update(parsed)
        rows.append(row)
    return rows


def write_scored_outputs(scored_dir: Path, family: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    family_dir = scored_dir / family
    family_dir.mkdir(parents=True, exist_ok=True)

    details_path = family_dir / "details.csv"
    summary_path = family_dir / "summary.json"

    if rows:
        pd.DataFrame(rows).to_csv(details_path, index=False)
    else:
        pd.DataFrame().to_csv(details_path, index=False)

    summary = summarize_family(family, rows)
    with summary_path.open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, ensure_ascii=False, indent=2)
    return summary


def summarize_family(family: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    if family in CHOICE_TASK_FAMILIES:
        if not rows:
            return {"family": family, "status": "missing", "n": 0}
        frame = pd.DataFrame(rows)
        summary: dict[str, Any] = {
            "family": family,
            "status": "ok",
            "n": int(len(frame)),
            "models": {},
        }
        for model, model_frame in frame.groupby("model"):
            model_summary = {
                "accuracy": float(model_frame["correct"].mean()),
                "n": int(len(model_frame)),
            }
            if family == "prompt_position" and "prompt_position" in model_frame.columns:
                position_stats = []
                for position, position_frame in model_frame.groupby("prompt_position"):
                    position_stats.append(
                        {
                            "prompt_position": position,
                            "accuracy": float(position_frame["correct"].mean()),
                            "n": int(len(position_frame)),
                        }
                    )
                model_summary["positions"] = position_stats
            if family == "reverse_inference_audit" and "metric_dimension" in model_frame.columns:
                leak_stats = []
                for dimension, dimension_frame in model_frame.groupby("metric_dimension"):
                    leak_stats.append(
                        {
                            "metric_dimension": dimension,
                            "leak_rate": float(dimension_frame["correct"].mean()),
                            "n": int(len(dimension_frame)),
                        }
                    )
                model_summary["dimensions"] = leak_stats
            summary["models"][model] = model_summary
        return summary

    if family == "lexical_norming":
        if not rows:
            return {"family": family, "status": "missing", "n": 0}
        frame = pd.DataFrame(rows)
        numeric_cols = [column for column in frame.columns if column not in {"task_id", "task_family", "model", "label", "success"}]
        grouped = frame.groupby("label")[numeric_cols].mean(numeric_only=True).reset_index()
        if not grouped.empty:
            grouped["public_private_gap"] = (grouped["publicness"] - grouped["privacy"]).abs()
            grouped["nuisance_spread"] = grouped[["danger", "valence", "brightness"]].std(axis=1, ddof=0).fillna(0.0)
            grouped = grouped.sort_values(["public_private_gap", "nuisance_spread"], ascending=[False, True])
        return {
            "family": family,
            "status": "ok",
            "n": int(len(frame)),
            "ranked_labels": grouped.to_dict(orient="records"),
        }

    if family == "coding_pilot_llm":
        if not rows:
            return {"family": family, "status": "missing", "n": 0}
        frame = pd.DataFrame(rows)
        return {
            "family": family,
            "status": "ok",
            "n": int(len(frame)),
            "models": {
                model: {"n": int(len(model_frame)), "success_rate": float(model_frame["success"].mean())}
                for model, model_frame in frame.groupby("model")
            },
        }

    return {"family": family, "status": "missing", "n": 0}


def build_decisions(
    paths: PreflightPaths,
    config: dict[str, Any],
    family_summaries: dict[str, Any],
) -> dict[str, Any]:
    metrics_quality = load_json(paths.metrics / "quality_report.json")
    stability_report = load_json(paths.convergence / "stability_report.json")
    mic_report_path = paths.mic / "mic_variance_report.csv"
    mic_frame = pd.read_csv(mic_report_path) if mic_report_path.exists() else pd.DataFrame()

    correlation_threshold = config["metrics"]["h2_metric_correlation_threshold"]
    openness_connectivity = abs(
        float(metrics_quality.get("metric_correlation", {}).get("openness", {}).get("connectivity", 0.0))
    )
    chosen_h2_metric = "mean_depth" if openness_connectivity > correlation_threshold else "openness"

    primary_alias = pick_decision_model_alias(family_summaries)
    gate_summary = {
        "comprehension": family_summaries["comprehension"].get("models", {}).get(primary_alias),
        "behavioral_inference": family_summaries["behavioral_inference"].get("models", {}).get(primary_alias),
    }
    passes_gate = None
    if gate_summary["comprehension"] and gate_summary["behavioral_inference"]:
        passes_gate = (
            gate_summary["comprehension"]["accuracy"] >= config["thresholds"]["comprehension_accuracy"]
            and gate_summary["behavioral_inference"]["accuracy"] >= config["thresholds"]["behavioral_inference_accuracy"]
        )

    prompt_choice = choose_prompt_position(
        family_summaries["prompt_position"].get("models", {}).get(primary_alias),
        prompt_order=config["llm_gate"]["prompt_positions"],
    )
    reverse_summary = summarize_reverse_audit_decision(
        family_summaries["reverse_inference_audit"].get("models", {}).get(primary_alias),
        cutoff=config["thresholds"]["reverse_inference_leak_cutoff"],
        scored_details_path=paths.scored / "reverse_inference_audit" / "details.csv",
    )
    lexical_choice = summarize_lexical_decision(
        family_summaries["lexical_norming"],
        primary_gap_min=config["thresholds"]["lexical_primary_gap_min"],
        nuisance_spread_max=config["thresholds"]["lexical_nuisance_spread_max"],
    )
    mic_decision = summarize_mic_decision(mic_frame)

    return {
        "metric_selection": {
            "chosen_h2_metric": chosen_h2_metric,
            "openness_connectivity_correlation": openness_connectivity,
            "threshold": correlation_threshold,
        },
        "llm_gate": {
            "primary_model_alias": primary_alias,
            "comprehension": gate_summary["comprehension"],
            "behavioral_inference": gate_summary["behavioral_inference"],
            "passes_gate": passes_gate,
        },
        "prompt_position": prompt_choice,
        "reverse_inference_audit": reverse_summary,
        "lexical_norming": lexical_choice,
        "mic_pilot": mic_decision,
        "convergence_pilot": stability_report,
    }


def pick_decision_model_alias(family_summaries: dict[str, Any]) -> str:
    for preferred in ["primary", "gpt54", "robustness"]:
        for family in ["comprehension", "behavioral_inference", "prompt_position", "reverse_inference_audit"]:
            models = family_summaries.get(family, {}).get("models", {})
            if preferred in models:
                return preferred
    for family in ["comprehension", "behavioral_inference", "prompt_position", "reverse_inference_audit"]:
        models = family_summaries.get(family, {}).get("models", {})
        if models:
            return next(iter(models))
    return "primary"


def choose_prompt_position(model_summary: dict[str, Any] | None, *, prompt_order: list[str]) -> dict[str, Any]:
    if not model_summary or "positions" not in model_summary:
        return {"status": "missing", "recommended_position": None}
    ranked = sorted(
        model_summary["positions"],
        key=lambda row: (-row["accuracy"], prompt_order.index(row["prompt_position"]) if row["prompt_position"] in prompt_order else math.inf),
    )
    best = ranked[0]
    return {
        "status": "ok",
        "recommended_position": best["prompt_position"],
        "positions": ranked,
    }


def summarize_reverse_audit_decision(
    model_summary: dict[str, Any] | None,
    *,
    cutoff: float,
    scored_details_path: Path,
) -> dict[str, Any]:
    if not model_summary:
        return {"status": "missing", "descriptions_to_rewrite": []}

    flagged_locations: list[str] = []
    if scored_details_path.exists():
        frame = pd.read_csv(scored_details_path)
        if not frame.empty:
            grouped = (
                frame.groupby(["location", "metric_dimension"], as_index=False)["correct"]
                .mean()
                .rename(columns={"correct": "leak_rate"})
            )
            flagged_locations = sorted(grouped.loc[grouped["leak_rate"] > cutoff, "location"].unique().tolist())

    return {
        "status": "ok",
        "cutoff": cutoff,
        "dimensions": model_summary.get("dimensions", []),
        "descriptions_to_rewrite": flagged_locations,
    }


def summarize_lexical_decision(
    lexical_summary: dict[str, Any],
    *,
    primary_gap_min: float,
    nuisance_spread_max: float,
) -> dict[str, Any]:
    if lexical_summary.get("status") != "ok":
        return {"status": "missing", "recommended_labels": []}

    ranked_labels = lexical_summary.get("ranked_labels", [])
    recommended = [
        row["label"]
        for row in ranked_labels
        if row.get("public_private_gap", 0.0) >= primary_gap_min
        and row.get("nuisance_spread", math.inf) <= nuisance_spread_max
    ]
    return {
        "status": "ok",
        "recommended_labels": recommended,
        "ranked_labels": ranked_labels,
    }


def summarize_mic_decision(mic_frame: pd.DataFrame) -> dict[str, Any]:
    if mic_frame.empty:
        return {"status": "missing", "windows_with_icc": []}
    windows_with_icc = (
        mic_frame.loc[mic_frame["icc_seed"] >= 0.1, ["window_start", "window_end", "dv", "comparison", "icc_seed"]]
        .sort_values(["window_start", "dv", "comparison"])
        .to_dict(orient="records")
    )
    return {
        "status": "ok",
        "windows_with_icc": windows_with_icc,
        "best_variance_reduction": mic_frame.sort_values("variance_reduction", ascending=False).head(5).to_dict(orient="records"),
    }


def write_reports(reports_dir: Path, decisions: dict[str, Any], family_summaries: dict[str, Any]) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    with (reports_dir / "preflight_decisions.json").open("w", encoding="utf-8") as handle:
        json.dump(decisions, handle, ensure_ascii=False, indent=2)

    lines = [
        "# Preflight Summary",
        "",
        "## Gate Checks",
        f"- H2 metric choice: `{decisions['metric_selection']['chosen_h2_metric']}`",
        f"- Primary LLM gate passed: `{decisions['llm_gate']['passes_gate']}`",
        f"- Recommended prompt position: `{decisions['prompt_position'].get('recommended_position')}`",
        "",
        "## Reverse-Inference Audit",
        f"- Descriptions to rewrite: {', '.join(decisions['reverse_inference_audit'].get('descriptions_to_rewrite', [])) or 'none'}",
        "",
        "## Lexical Norming",
        f"- Recommended labels: {', '.join(decisions['lexical_norming'].get('recommended_labels', [])) or 'none'}",
        "",
        "## MIC + Convergence",
        f"- MIC windows with ICC >= 0.1: `{len(decisions['mic_pilot'].get('windows_with_icc', []))}`",
        f"- Recommended rounds: `{decisions['convergence_pilot'].get('recommended_rounds')}`",
        "",
        "## Family Status",
    ]
    for family, summary in family_summaries.items():
        lines.append(f"- `{family}`: `{summary.get('status', 'missing')}`, n=`{summary.get('n', 0)}`")
    with (reports_dir / "preflight_summary.md").open("w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def extract_prediction(task: dict[str, Any], response: dict[str, Any]) -> str | None:
    parsed = extract_structured_answer(response)
    if isinstance(parsed, dict) and "answer" in parsed:
        return normalize_answer(str(parsed["answer"]))
    if isinstance(parsed, str):
        return normalize_answer(parsed)

    raw_text = str(response.get("raw_text", ""))
    options = task["prompt_payload"].get("options", [])
    normalized_options = {normalize_answer(option): option for option in options}
    normalized_text = normalize_answer(raw_text)
    if normalized_text in normalized_options:
        return normalized_text
    for option in normalized_options:
        if option and option in normalized_text:
            return option
    return None


def extract_structured_answer(response: dict[str, Any]) -> Any:
    if response.get("parsed_answer") is not None:
        return response["parsed_answer"]

    raw_text = str(response.get("raw_text", "")).strip()
    if not raw_text:
        return None

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        pass

    match = re.search(r"\{.*\}", raw_text, re.S)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            return None
    return raw_text


def normalize_answer(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())


def quantile_label(value: float, series: pd.Series) -> str:
    rank = float((series <= value).mean())
    if rank >= 2 / 3:
        return "high"
    if rank <= 1 / 3:
        return "low"
    return "mid"


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.strip().lower()).strip("_")
