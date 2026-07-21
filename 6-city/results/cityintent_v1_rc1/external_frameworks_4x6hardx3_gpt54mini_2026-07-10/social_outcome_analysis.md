# CityIntent Social-Outcome Family Analysis

Repeated runs per scenario-adapter cell: 3.

| Adapter | Accepted outcomes | Outcome rate | Full social traces | Social pass^k | Full task | Fully feasible | Joint success | Legal but ineffective | Plausible but unverified |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| AgentSociety | 4/27 | 0.148 | 0.000 | 0.000 | 0.000 | 0.278 | 0.000 | 0.278 | 0.611 |
| GATSim | 21/27 | 0.778 | 0.667 | 0.667 | 0.667 | 0.833 | 0.667 | 0.167 | 0.222 |
| Generative Agents | 3/27 | 0.111 | 0.056 | 0.000 | 0.056 | 0.278 | 0.000 | 0.278 | 0.667 |
| SOTOPIA | 0/27 | 0.000 | 0.000 | 0.000 | 0.000 | 0.167 | 0.000 | 0.167 | 0.611 |

## Evidence-Gap Diagnostics

| Adapter | Message without meeting | Interact attempt without success | Target entry without meeting | Mean task | Mean feasibility | Mean face plausibility |
|---|---:|---:|---:|---:|---:|---:|
| AgentSociety | 0.167 | 0.500 | 0.722 | 0.314 | 0.813 | 0.729 |
| GATSim | 0.000 | 0.333 | 0.333 | 0.750 | 0.905 | 0.724 |
| Generative Agents | 0.111 | 0.222 | 0.833 | 0.410 | 0.771 | 0.721 |
| SOTOPIA | 0.389 | 0.000 | 0.278 | 0.158 | 0.850 | 0.677 |

`Social pass^k` is the fraction of scenario cells where every repeat accepts all required co-presence outcomes.
