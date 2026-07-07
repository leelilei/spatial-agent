# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.922 | 0.655 | 0.286 | 0.518 | 0.403 | 0.433 | 0.962 | 0.823 |
| gatsim_official_planner | 0.767 | 0.785 | 0.12 | 0.283 | 0.483 | 0.65 | 0.682 | 0.445 |
| generative_agents_official_planner | 0.742 | 0.602 | 0.194 | 0.385 | 0.357 | 0.308 | 0.505 | 0.512 |
| sotopia_official_llm_agent | 0.79 | 0.896 | 0.051 | 0.385 | 0.405 | 0.4 | 0.595 | 0.603 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
