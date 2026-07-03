# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.725 | 0.863 | 0.045 | 0.445 | 0.28 | 0.7 | 0.72 | 0.605 |
| gatsim_official_planner | 0.468 | 0.875 | 0.021 | 0.263 | 0.205 | 0.613 | 0.652 | 0.367 |
| generative_agents_official_planner | 0.79 | 0.95 | 0.0 | 0.375 | 0.415 | 0.838 | 0.46 | 0.652 |
| sotopia_official_llm_agent | 0.792 | 0.896 | 0.04 | 0.33 | 0.463 | 0.675 | 0.46 | 0.54 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
