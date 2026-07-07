# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.782 | 0.673 | 0.164 | 0.492 | 0.29 | 0.417 | 0.7 | 0.712 |
| gatsim_official_planner | 0.798 | 0.843 | 0.063 | 0.617 | 0.182 | 0.65 | 0.455 | 0.723 |
| generative_agents_official_planner | 0.592 | 0.723 | 0.087 | 0.388 | 0.203 | 0.333 | 0.292 | 0.53 |
| sotopia_official_llm_agent | 0.723 | 0.919 | 0.012 | 0.373 | 0.35 | 0.35 | 0.458 | 0.672 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
