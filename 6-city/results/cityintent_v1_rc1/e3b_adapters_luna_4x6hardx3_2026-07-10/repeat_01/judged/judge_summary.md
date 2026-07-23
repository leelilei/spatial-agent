# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.85 | 0.943 | 0.008 | 0.523 | 0.327 | 0.708 | 0.767 | 0.653 |
| gatsim_official_planner | 0.81 | 0.926 | 0.037 | 0.425 | 0.385 | 0.817 | 0.668 | 0.56 |
| generative_agents_official_planner | 0.652 | 0.907 | 0.008 | 0.355 | 0.297 | 0.667 | 0.385 | 0.487 |
| sotopia_official_llm_agent | 0.817 | 0.931 | 0.027 | 0.43 | 0.387 | 0.642 | 0.572 | 0.61 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
