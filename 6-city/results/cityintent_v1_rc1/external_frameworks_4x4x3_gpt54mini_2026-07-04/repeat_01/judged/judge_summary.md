# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.853 | 0.823 | 0.058 | 0.61 | 0.242 | 0.75 | 0.843 | 0.797 |
| gatsim_official_planner | 0.625 | 0.83 | 0.079 | 0.24 | 0.385 | 0.787 | 0.5 | 0.435 |
| generative_agents_official_planner | 0.573 | 0.635 | 0.148 | 0.342 | 0.23 | 0.675 | 0.277 | 0.518 |
| sotopia_official_llm_agent | 0.728 | 1.0 | 0.0 | 0.225 | 0.502 | 0.488 | 0.407 | 0.49 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
