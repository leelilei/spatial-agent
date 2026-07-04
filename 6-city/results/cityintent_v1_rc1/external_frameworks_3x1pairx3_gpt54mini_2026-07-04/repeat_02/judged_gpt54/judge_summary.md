# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.825 | 0.812 | 0.037 | 0.675 | 0.15 | 0.75 | 0.8 | 0.825 |
| gatsim_official_planner | 0.815 | 1.0 | 0.0 | 0.66 | 0.155 | 1.0 | 0.52 | 0.76 |
| generative_agents_official_planner | 0.85 | 0.715 | 0.15 | 0.765 | 0.085 | 0.75 | 0.54 | 0.83 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
