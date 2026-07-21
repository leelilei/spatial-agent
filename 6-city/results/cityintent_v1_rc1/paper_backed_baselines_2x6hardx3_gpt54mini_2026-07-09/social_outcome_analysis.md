# CityIntent Social-Outcome Family Analysis

Repeated runs per scenario-adapter cell: 3.

| Adapter | Accepted outcomes | Outcome rate | Full social traces | Social pass^k | Full task | Fully feasible | Joint success | Legal but ineffective | Plausible but unverified |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 10/27 | 0.370 | 0.222 | 0.167 | 0.167 | 0.389 | 0.167 | 0.222 | 0.778 |
| api_llm_react_tool_policy | 21/27 | 0.778 | 0.667 | 0.500 | 0.333 | 0.500 | 0.167 | 0.167 | 0.333 |

## Evidence-Gap Diagnostics

| Adapter | Message without meeting | Interact attempt without success | Target entry without meeting | Mean task | Mean feasibility | Mean face plausibility |
|---|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.111 | 0.722 | 0.778 | 0.534 | 0.909 | 0.889 |
| api_llm_react_tool_policy | 0.056 | 0.278 | 0.333 | 0.726 | 0.908 | 0.819 |

`Social pass^k` is the fraction of scenario cells where every repeat accepts all required co-presence outcomes.
