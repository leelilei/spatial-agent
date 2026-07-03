# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.927 | 0.705 | 0.23 | 0.613 | 0.315 | 0.725 | 0.91 | 0.787 |
| gatsim_official_planner | 0.445 | 1.0 | 0.0 | 0.168 | 0.278 | 0.787 | 0.215 | 0.277 |
| generative_agents_official_planner | 0.682 | 0.701 | 0.156 | 0.357 | 0.325 | 0.637 | 0.398 | 0.627 |
| sotopia_official_llm_agent | 0.743 | 0.817 | 0.108 | 0.33 | 0.413 | 0.613 | 0.527 | 0.588 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
