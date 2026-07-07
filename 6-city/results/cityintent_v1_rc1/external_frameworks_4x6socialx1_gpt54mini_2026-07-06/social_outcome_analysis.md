# CityIntent Social-Outcome Family Analysis

Repeated runs per scenario-adapter cell: 3.

| Adapter | Accepted outcomes | Outcome rate | Full social traces | Social pass^k | Full task | Fully feasible | Joint success | Legal but ineffective | Plausible but unverified |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| AgentSociety | 4/21 | 0.190 | 0.222 | 0.167 | 0.222 | 0.278 | 0.167 | 0.111 | 0.778 |
| GATSim | 15/21 | 0.714 | 0.667 | 0.667 | 0.667 | 0.500 | 0.500 | 0.000 | 0.278 |
| Generative Agents | 2/21 | 0.095 | 0.111 | 0.000 | 0.056 | 0.056 | 0.000 | 0.056 | 0.667 |
| SOTOPIA | 0/21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.611 | 0.000 | 0.611 | 0.889 |

## Evidence-Gap Diagnostics

| Adapter | Message without meeting | Interact attempt without success | Target entry without meeting | Mean task | Mean feasibility | Mean face plausibility |
|---|---:|---:|---:|---:|---:|---:|
| AgentSociety | 0.333 | 0.333 | 0.611 | 0.325 | 0.615 | 0.903 |
| GATSim | 0.000 | 0.333 | 0.333 | 0.667 | 0.819 | 0.776 |
| Generative Agents | 0.333 | 0.056 | 0.722 | 0.220 | 0.666 | 0.772 |
| SOTOPIA | 0.611 | 0.056 | 0.111 | 0.103 | 0.913 | 0.813 |

`Social pass^k` is the fraction of scenario cells where every repeat accepts all required co-presence outcomes.
