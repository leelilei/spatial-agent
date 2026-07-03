# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.795 | 0.823 | 0.006 | 0.632 | 0.163 | 0.75 | 0.703 | 0.787 |
| gatsim_official_planner | 0.66 | 0.83 | 0.0 | 0.42 | 0.24 | 0.787 | 0.325 | 0.562 |
| generative_agents_official_planner | 0.6 | 0.635 | 0.075 | 0.363 | 0.237 | 0.675 | 0.307 | 0.547 |
| sotopia_official_llm_agent | 0.505 | 1.0 | 0.0 | 0.275 | 0.23 | 0.488 | 0.268 | 0.385 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
