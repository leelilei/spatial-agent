# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.9 | 0.812 | 0.107 | 0.81 | 0.09 | 0.75 | 0.945 | 0.875 |
| gatsim_official_planner | 0.75 | 1.0 | 0.0 | 0.34 | 0.41 | 1.0 | 0.5 | 0.64 |
| generative_agents_official_planner | 0.845 | 0.715 | 0.145 | 0.65 | 0.195 | 0.75 | 0.365 | 0.81 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
