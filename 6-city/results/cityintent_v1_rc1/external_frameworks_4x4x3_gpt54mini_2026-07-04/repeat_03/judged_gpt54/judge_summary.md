# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.833 | 0.767 | 0.076 | 0.66 | 0.172 | 0.662 | 0.815 | 0.795 |
| gatsim_official_planner | 0.625 | 0.896 | 0.0 | 0.427 | 0.198 | 0.613 | 0.395 | 0.568 |
| generative_agents_official_planner | 0.782 | 0.698 | 0.123 | 0.62 | 0.163 | 0.675 | 0.36 | 0.76 |
| sotopia_official_llm_agent | 0.755 | 0.875 | 0.105 | 0.482 | 0.273 | 0.613 | 0.47 | 0.588 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
