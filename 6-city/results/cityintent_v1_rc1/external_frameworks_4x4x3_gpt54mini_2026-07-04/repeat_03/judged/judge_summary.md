# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.905 | 0.767 | 0.148 | 0.525 | 0.38 | 0.662 | 0.828 | 0.792 |
| gatsim_official_planner | 0.605 | 0.896 | 0.0 | 0.212 | 0.393 | 0.613 | 0.545 | 0.365 |
| generative_agents_official_planner | 0.805 | 0.698 | 0.166 | 0.465 | 0.34 | 0.675 | 0.523 | 0.65 |
| sotopia_official_llm_agent | 0.83 | 0.875 | 0.083 | 0.315 | 0.515 | 0.613 | 0.588 | 0.608 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
