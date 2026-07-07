# CityIntent Social-Outcome Family Analysis

Repeated runs per scenario-adapter cell: 3.

| Adapter | Accepted outcomes | Outcome rate | Full social traces | Social pass^k | Full task | Fully feasible | Joint success | Legal but ineffective | Plausible but unverified |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 18/21 | 0.857 | 0.833 | 0.833 | 0.833 | 0.722 | 0.667 | 0.056 | 0.167 |
| api_llm_react_tool_policy | 21/21 | 1.000 | 1.000 | 1.000 | 1.000 | 0.833 | 0.833 | 0.000 | 0.000 |

## Evidence-Gap Diagnostics

| Adapter | Message without meeting | Interact attempt without success | Target entry without meeting | Mean task | Mean feasibility | Mean face plausibility |
|---|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.000 | 0.167 | 0.167 | 0.917 | 0.957 | 0.910 |
| api_llm_react_tool_policy | 0.000 | 0.000 | 0.000 | 1.000 | 0.958 | 0.876 |

`Social pass^k` is the fraction of scenario cells where every repeat accepts all required co-presence outcomes.
