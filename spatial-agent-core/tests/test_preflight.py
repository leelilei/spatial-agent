from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from analysis.spatial_behavioral import assess_convergence, compute_run_level_alignment
from analysis.preflight import (
    build_task_collections,
    normalize_offline_responses,
    resolve_preflight_paths,
    score_and_report_preflight,
    write_jsonl,
    write_task_bundle,
)
from space.graph import load_layout_graph
from space.metrics import compute_space_metrics
from world.engine import PilotSimulationEngine
import yaml


def test_space_metrics_include_core_columns():
    graph = load_layout_graph(PROJECT_ROOT / "configs/layouts/plaza.yaml")
    frame = compute_space_metrics(graph)
    expected = {"node_id", "integration", "mean_depth", "control_value", "openness"}
    assert expected.issubset(frame.columns)
    assert len(frame) >= 10


def test_pilot_engine_produces_alignment_metrics():
    graph = load_layout_graph(PROJECT_ROOT / "configs/layouts/plaza.yaml")
    metrics = compute_space_metrics(graph)
    engine = PilotSimulationEngine(graph, metrics, num_agents=8, num_rounds=80, seed=7, condition="C4")
    visits, events = engine.run()

    summary = compute_run_level_alignment(visits, events, metrics, min_location_visits=3)
    assert "tar_h1_run" in summary
    assert "bsr_h2_run" in summary
    assert summary["num_visited_locations"] > 0


def test_convergence_assessment_recommends_round_budget():
    synthetic = [
        {"window_index": 0, "window_start": 1, "window_end": 20, "density": 0.20, "clustering": 0.12, "degree_gini": 0.30, "mean_interaction_strength": 1.0},
        {"window_index": 1, "window_start": 21, "window_end": 40, "density": 0.35, "clustering": 0.20, "degree_gini": 0.28, "mean_interaction_strength": 1.5},
        {"window_index": 2, "window_start": 41, "window_end": 60, "density": 0.36, "clustering": 0.21, "degree_gini": 0.27, "mean_interaction_strength": 1.52},
        {"window_index": 3, "window_start": 61, "window_end": 80, "density": 0.361, "clustering": 0.211, "degree_gini": 0.271, "mean_interaction_strength": 1.53},
        {"window_index": 4, "window_start": 81, "window_end": 100, "density": 0.362, "clustering": 0.211, "degree_gini": 0.272, "mean_interaction_strength": 1.531},
        {"window_index": 5, "window_start": 101, "window_end": 120, "density": 0.362, "clustering": 0.212, "degree_gini": 0.272, "mean_interaction_strength": 1.532},
        {"window_index": 6, "window_start": 121, "window_end": 140, "density": 0.363, "clustering": 0.212, "degree_gini": 0.272, "mean_interaction_strength": 1.532},
    ]
    import pandas as pd

    result = assess_convergence(
        pd.DataFrame(synthetic),
        window_size=20,
        delta_threshold=0.2,
        min_stable_windows=3,
        holdout_rounds=40,
    )
    assert result["recommended_rounds"] in {200, 300}


def test_preflight_analyze_generates_decision_report(tmp_path):
    with (PROJECT_ROOT / "configs/experiments/preflight_v7.yaml").open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)

    config["experiment"]["output_dir"] = str(tmp_path / "results/preflight")
    config["io"]["tasks_dir"] = str(tmp_path / "results/preflight/tasks")
    config["io"]["raw_dir"] = str(tmp_path / "results/preflight/raw")
    config["io"]["scored_dir"] = str(tmp_path / "results/preflight/scored")
    config["io"]["reports_dir"] = str(tmp_path / "results/preflight/reports")

    graph = load_layout_graph(PROJECT_ROOT / "configs/layouts/plaza.yaml")
    metrics = compute_space_metrics(graph)
    tasks = build_task_collections(
        metrics,
        prompt_positions=config["llm_gate"]["prompt_positions"],
        lexical_dimensions=config["lexical_norming"]["dimensions"],
        lexical_labels=config["lexical_norming"]["candidate_labels"],
        coding_subset_cfg=config["coding_pilot_llm_subset"],
    )
    paths = resolve_preflight_paths(PROJECT_ROOT, config)
    write_task_bundle(paths.tasks, tasks, lexical_dimensions=config["lexical_norming"]["dimensions"])

    paths.metrics.mkdir(parents=True, exist_ok=True)
    paths.convergence.mkdir(parents=True, exist_ok=True)
    paths.mic.mkdir(parents=True, exist_ok=True)
    (paths.metrics / "quality_report.json").write_text(
        '{"metric_correlation":{"openness":{"connectivity":0.82}}}',
        encoding="utf-8",
    )
    (paths.convergence / "stability_report.json").write_text(
        '{"recommended_rounds":300,"converged":false}',
        encoding="utf-8",
    )
    (paths.mic / "mic_variance_report.csv").write_text(
        "window_start,window_end,dv,comparison,icc_seed,variance_reduction\n1,50,tar_h1_run,C6m-C1,0.12,0.4\n",
        encoding="utf-8",
    )

    raw_rows = {
        "comprehension": [
            {"task_id": tasks["comprehension"][0]["task_id"], "task_family": "comprehension", "model": "primary", "parsed_answer": {"answer": tasks["comprehension"][0]["expected_answer"]["answer"]}, "raw_text": "", "success": True},
        ],
        "behavioral_inference": [
            {"task_id": tasks["behavioral_inference"][0]["task_id"], "task_family": "behavioral_inference", "model": "primary", "parsed_answer": {"answer": tasks["behavioral_inference"][0]["expected_answer"]["answer"]}, "raw_text": "", "success": True},
        ],
        "prompt_position": [
            {"task_id": task["task_id"], "task_family": "prompt_position", "model": "primary", "parsed_answer": {"answer": task["expected_answer"]["answer"]}, "raw_text": "", "success": True}
            for task in tasks["prompt_position"]
        ],
        "reverse_inference_audit": [
            {"task_id": task["task_id"], "task_family": "reverse_inference_audit", "model": "primary", "parsed_answer": {"answer": task["expected_answer"]["answer"]}, "raw_text": "", "success": True}
            for task in tasks["reverse_inference_audit"][:3]
        ],
        "lexical_norming": [
            {"task_id": tasks["lexical_norming"][0]["task_id"], "task_family": "lexical_norming", "model": "primary", "parsed_answer": {"publicness": 6, "privacy": 2, "danger": 3, "valence": 4, "brightness": 5}, "raw_text": "", "success": True},
        ],
        "coding_pilot_llm": [
            {"task_id": tasks["coding_pilot_llm"][0]["task_id"], "task_family": "coding_pilot_llm", "model": "primary", "parsed_answer": {"behavior_type": "social", "interaction_intensity": "high", "information_sensitivity": "low", "gatekeeping": "absent"}, "raw_text": "", "success": True},
        ],
    }
    for family, rows in raw_rows.items():
        write_jsonl(paths.raw / family / "primary" / "responses.jsonl", rows)

    result = score_and_report_preflight(paths, config)
    assert result["decisions"]["metric_selection"]["chosen_h2_metric"] == "mean_depth"
    assert (paths.reports / "preflight_summary.md").exists()
    assert (paths.scored / "prompt_position" / "summary.json").exists()


def test_run_offline_import_normalizes_flat_files(tmp_path):
    responses_dir = tmp_path / "imports"
    responses_dir.mkdir()
    flat_path = responses_dir / "comprehension.jsonl"
    write_jsonl(
        flat_path,
        [
            {
                "task_id": "comp_01",
                "parsed_answer": {"answer": "plaza_center"},
                "success": True,
            }
        ],
    )
    raw_dir = tmp_path / "raw"
    imported = normalize_offline_responses(responses_dir, raw_dir)
    assert imported
    normalized = list((raw_dir / "comprehension" / "offline_import").glob("responses.jsonl"))
    assert normalized
