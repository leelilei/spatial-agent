# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.903 | 0.673 | 0.249 | 0.525 | 0.378 | 0.417 | 0.928 | 0.755 |
| gatsim_official_planner | 0.767 | 0.843 | 0.057 | 0.362 | 0.405 | 0.65 | 0.655 | 0.455 |
| generative_agents_official_planner | 0.728 | 0.723 | 0.131 | 0.263 | 0.465 | 0.333 | 0.607 | 0.473 |
| sotopia_official_llm_agent | 0.797 | 0.919 | 0.036 | 0.437 | 0.36 | 0.35 | 0.745 | 0.62 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
