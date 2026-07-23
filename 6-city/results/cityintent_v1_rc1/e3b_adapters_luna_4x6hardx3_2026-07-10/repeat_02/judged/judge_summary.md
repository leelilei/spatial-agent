# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.775 | 0.884 | 0.015 | 0.358 | 0.417 | 0.667 | 0.775 | 0.602 |
| gatsim_official_planner | 0.622 | 0.972 | 0.0 | 0.318 | 0.303 | 0.775 | 0.765 | 0.41 |
| generative_agents_official_planner | 0.717 | 0.915 | 0.03 | 0.392 | 0.325 | 0.675 | 0.527 | 0.458 |
| sotopia_official_llm_agent | 0.785 | 0.9 | 0.038 | 0.582 | 0.203 | 0.625 | 0.535 | 0.697 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
