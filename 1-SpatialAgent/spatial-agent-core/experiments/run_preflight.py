"""v7 预实验双模式闭环编排脚本。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import pandas as pd
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from analysis.spatial_behavioral import (  # noqa: E402
    assess_convergence,
    compute_mic_variance_report,
    compute_run_level_alignment,
    compute_windowed_network_metrics,
    compute_windowed_run_metrics,
)
from analysis.preflight import (  # noqa: E402
    build_task_collections,
    ensure_preflight_dirs,
    normalize_offline_responses,
    read_jsonl,
    resolve_preflight_paths,
    score_and_report_preflight,
    write_jsonl,
    write_task_bundle,
)
from llm.client import build_llm_client  # noqa: E402
from llm.prompts import build_preflight_messages  # noqa: E402
from space.graph import load_layout, load_layout_graph  # noqa: E402
from space.metrics import compute_space_metrics, summarize_metric_quality  # noqa: E402
from world.engine import PilotSimulationEngine  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run v7 preflight experiments.")
    parser.add_argument(
        "--config",
        default="configs/experiments/preflight_v7.yaml",
        help="Path to preflight config, relative to project root.",
    )
    parser.add_argument(
        "--stage",
        choices=["all", "metrics", "tasks", "run_offline", "run_online", "mic", "convergence", "analyze"],
        default="all",
        help="Which preflight stage to run.",
    )
    parser.add_argument(
        "--model",
        default="primary",
        help="Model alias in config.models to use for run_online.",
    )
    parser.add_argument(
        "--mode",
        choices=["offline", "online"],
        default="offline",
        help="Execution mode hint. 'all' remains offline-safe by default.",
    )
    parser.add_argument(
        "--responses-dir",
        default="",
        help="Directory for importing offline responses.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing response files for the selected stage.",
    )
    return parser.parse_args()


def load_config(config_path: str) -> dict[str, Any]:
    path = PROJECT_ROOT / config_path
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def run_metric_precheck(config: dict[str, Any]) -> None:
    output_dir = ensure_dir(resolve_preflight_paths(PROJECT_ROOT, config).metrics)
    layout_path = PROJECT_ROOT / config["experiment"]["layout_path"]
    layout = load_layout(layout_path)
    graph = load_layout_graph(layout_path)
    metrics = compute_space_metrics(graph)
    quality = summarize_metric_quality(
        metrics,
        high_control_quantile=config["metrics"]["high_control_quantile"],
    )

    metrics.to_csv(output_dir / "node_metrics.csv", index=False)
    with (output_dir / "quality_report.json").open("w", encoding="utf-8") as handle:
        json.dump(quality, handle, ensure_ascii=False, indent=2)
    with (output_dir / "layout_snapshot.json").open("w", encoding="utf-8") as handle:
        json.dump(layout, handle, ensure_ascii=False, indent=2)


def prepare_task_files(config: dict[str, Any]) -> None:
    paths = resolve_preflight_paths(PROJECT_ROOT, config)
    ensure_preflight_dirs(paths)
    layout_path = PROJECT_ROOT / config["experiment"]["layout_path"]
    graph = load_layout_graph(layout_path)
    metrics = compute_space_metrics(graph)
    task_bundle = build_task_collections(
        metrics,
        prompt_positions=config["llm_gate"]["prompt_positions"],
        lexical_dimensions=config["lexical_norming"]["dimensions"],
        lexical_labels=config["lexical_norming"]["candidate_labels"],
        coding_subset_cfg=config["coding_pilot_llm_subset"],
    )
    write_task_bundle(
        paths.tasks,
        task_bundle,
        lexical_dimensions=config["lexical_norming"]["dimensions"],
    )


def run_offline_import(config: dict[str, Any], args: argparse.Namespace) -> None:
    if not args.responses_dir:
        raise ValueError("--responses-dir is required for run_offline stage.")
    paths = resolve_preflight_paths(PROJECT_ROOT, config)
    ensure_preflight_dirs(paths)
    normalize_offline_responses(Path(args.responses_dir), paths.raw)


def run_online_tasks(config: dict[str, Any], args: argparse.Namespace) -> None:
    paths = resolve_preflight_paths(PROJECT_ROOT, config)
    ensure_preflight_dirs(paths)
    model_cfg = config["models"][args.model]
    client = build_llm_client(model_cfg, cache_dir=PROJECT_ROOT / ".cache" / "preflight_llm")

    for task_file in sorted(paths.tasks.glob("*_tasks.jsonl")):
        tasks = read_jsonl(task_file)
        if not tasks:
            continue

        family = tasks[0]["task_family"]
        output_path = paths.raw / family / args.model / "responses.jsonl"
        existing = {}
        if output_path.exists() and not args.force:
            existing = {row["task_id"]: row for row in read_jsonl(output_path)}

        response_rows = list(existing.values())
        for task in tasks:
            if task["task_id"] in existing and not args.force:
                continue

            messages = build_preflight_messages(task)
            try:
                response = client.complete(
                    model=model_cfg["model"],
                    messages=messages,
                    temperature=float(model_cfg.get("temperature", 0.0)),
                    max_tokens=int(model_cfg.get("max_tokens", 300)),
                )
                response_rows.append(
                    {
                        "task_id": task["task_id"],
                        "task_family": task["task_family"],
                        "model": args.model,
                        "raw_text": response.text,
                        "parsed_answer": None,
                        "success": True,
                        "latency_ms": response.latency_ms,
                        "cache_hit": response.cache_hit,
                        "error": None,
                    }
                )
            except Exception as exc:  # pragma: no cover - exercised with mocks / live run
                response_rows.append(
                    {
                        "task_id": task["task_id"],
                        "task_family": task["task_family"],
                        "model": args.model,
                        "raw_text": "",
                        "parsed_answer": None,
                        "success": False,
                        "latency_ms": None,
                        "cache_hit": False,
                        "error": str(exc),
                    }
                )
        deduped = {row["task_id"]: row for row in response_rows}
        write_jsonl(output_path, list(deduped.values()))


def run_mic_pilot(config: dict[str, Any]) -> None:
    pilot_cfg = config["mic_pilot"]
    output_dir = ensure_dir(resolve_preflight_paths(PROJECT_ROOT, config).mic)
    layout_path = PROJECT_ROOT / config["experiment"]["layout_path"]
    graph = load_layout_graph(layout_path)
    metrics = compute_space_metrics(graph)

    run_rows = []
    window_rows = []
    for seed in range(1, pilot_cfg["seeds"] + 1):
        for condition in pilot_cfg["conditions"]:
            engine = PilotSimulationEngine(
                graph,
                metrics,
                num_agents=pilot_cfg["num_agents"],
                num_rounds=pilot_cfg["num_rounds"],
                seed=seed,
                condition=condition,
            )
            visits, events = engine.run()
            run_metrics = compute_run_level_alignment(
                visits,
                events,
                metrics,
                min_location_visits=pilot_cfg["min_location_visits"],
            )
            run_metrics.update({"seed": seed, "condition": condition})
            run_rows.append(run_metrics)

            window_metrics = compute_windowed_run_metrics(
                visits,
                events,
                metrics,
                window_size=pilot_cfg["window_size"],
                min_location_visits=pilot_cfg["min_location_visits"],
            )
            window_metrics["seed"] = seed
            window_metrics["condition"] = condition
            window_rows.append(window_metrics)

    run_frame = pd.DataFrame(run_rows)
    window_frame = pd.concat(window_rows, ignore_index=True)
    variance_report = compute_mic_variance_report(
        window_frame,
        comparisons=[tuple(item) for item in pilot_cfg["comparisons"]],
        dvs=pilot_cfg["dvs"],
        unmatched_bootstrap=pilot_cfg["unmatched_bootstrap"],
    )

    run_frame.to_csv(output_dir / "run_level_metrics.csv", index=False)
    window_frame.to_csv(output_dir / "window_level_metrics.csv", index=False)
    variance_report.to_csv(output_dir / "mic_variance_report.csv", index=False)


def run_convergence_pilot(config: dict[str, Any]) -> None:
    pilot_cfg = config["convergence_pilot"]
    output_dir = ensure_dir(resolve_preflight_paths(PROJECT_ROOT, config).convergence)
    layout_path = PROJECT_ROOT / config["experiment"]["layout_path"]
    graph = load_layout_graph(layout_path)
    metrics = compute_space_metrics(graph)

    window_frames = []
    for seed in range(1, pilot_cfg["seeds"] + 1):
        engine = PilotSimulationEngine(
            graph,
            metrics,
            num_agents=pilot_cfg["num_agents"],
            num_rounds=pilot_cfg["num_rounds"],
            seed=seed,
            condition=pilot_cfg["condition"],
        )
        _, events = engine.run()
        social_events = events.loc[events["event_type"] == "social"].copy()
        network_window = compute_windowed_network_metrics(
            social_events,
            num_agents=pilot_cfg["num_agents"],
            num_rounds=pilot_cfg["num_rounds"],
            window_size=pilot_cfg["window_size"],
        )
        network_window["seed"] = seed
        window_frames.append(network_window)

    stacked = pd.concat(window_frames, ignore_index=True)
    summary = (
        stacked.groupby(["window_index", "window_start", "window_end"], as_index=False)[
            ["density", "clustering", "degree_gini", "mean_interaction_strength"]
        ]
        .mean()
        .sort_values("window_index")
    )
    convergence = assess_convergence(
        summary,
        window_size=pilot_cfg["window_size"],
        delta_threshold=pilot_cfg["delta_threshold"],
        min_stable_windows=pilot_cfg["min_stable_windows"],
        holdout_rounds=pilot_cfg["holdout_rounds"],
    )

    stacked.to_csv(output_dir / "window_metrics_by_seed.csv", index=False)
    convergence["window_metrics"].to_csv(output_dir / "window_metrics_summary.csv", index=False)
    report = {key: value for key, value in convergence.items() if key != "window_metrics"}
    with (output_dir / "stability_report.json").open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)


def main() -> None:
    args = parse_args()
    config = load_config(args.config)
    if args.stage == "all":
        stages = ["metrics", "tasks", "run_online", "mic", "convergence", "analyze"] if args.mode == "online" else ["metrics", "tasks", "mic", "convergence", "analyze"]
    else:
        stages = [args.stage]
    for stage in stages:
        if stage == "metrics":
            run_metric_precheck(config)
        elif stage == "tasks":
            prepare_task_files(config)
        elif stage == "run_offline":
            run_offline_import(config, args)
        elif stage == "run_online":
            run_online_tasks(config, args)
        elif stage == "mic":
            run_mic_pilot(config)
        elif stage == "convergence":
            run_convergence_pilot(config)
        elif stage == "analyze":
            score_and_report_preflight(resolve_preflight_paths(PROJECT_ROOT, config), config)


if __name__ == "__main__":
    main()
