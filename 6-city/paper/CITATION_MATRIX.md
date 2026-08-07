# CityIntent Citation Matrix

Last updated: 2026-08-06

This matrix defines the 25-paper core set for the first manuscript draft. The
full verified library remains in `references.bib`; papers outside this core set
should be added only when they support a specific claim.

## Introduction

| Manuscript claim | Citation keys | Use |
|---|---|---|
| Generative agents combine memory, reflection, planning, and situated action. | `park2023generativeagents`; `vezhnevets2023generativeagentbased` | Establish the agent architecture lineage without claiming CityIntent invented situated agents. |
| Urban LLM research already covers broad urban tasks, spatiotemporal reasoning, and embodied city QA. | `feng2024citybench`; `lai2025ustbench`; `zhao2025cityeqa` | Define the existing urban benchmark landscape. |
| Recent systems simulate urban behavior at individual and population scales. | `bougie2025citysim`; `liu2025gatsim`; `piao2025agentsociety`; `li2026genworld` | Motivate the need to validate execution, not merely generate plausible behavior. |
| Plausible narratives and aggregate resemblance are insufficient evidence of realistic mechanisms. | `santos2026whenplausiblenot`; `larooij2025validationcentralchallenge`; `zhao2026mechanismplausibilitygenerative` | Ground the central problem statement and bound the paper's claims. |

## Related Work

| Subsection | Citation keys | Comparison boundary |
|---|---|---|
| Social agents and private goals | `zhou2024sotopia`; `pham2026liveculturebench`; `park2023generativeagents` | SOTOPIA supplies private social goals and interaction evaluation; LiveCultureBench adds dynamic town-scale social simulation. CityIntent must differentiate through environment-owned physical state and typed transition evidence. |
| Urban generative-agent simulation | `bougie2025citysim`; `liu2025gatsim`; `piao2025agentsociety`; `li2026genworld`; `chopra2024limitsagencyagent` | Existing work covers urban behavior generation and scale. CityIntent occupies controlled high-agency, micro-scale mechanism diagnosis rather than population realism. |
| Mobility realism and route execution | `anonymous2026mobisimbench`; `santos2026whenplausiblenot`; `song2026mobilitybench`; `mao2025deliverybench` | Separate macro/micro mobility realism, route-query feasibility, and delivery economics from continuous private-intention episodes. The anonymous MobiSim entry is draft-only until de-anonymized. |
| Executable agent benchmarks | `shao2024chinatravel`; `cheng2026doagentsknow`; `yao2024bench`; `trivedi2024appworld`; `zhou2023webarena`; `hui2026sttarena`; `chen2026trip` | Credit state-based evaluation, feasibility awareness, repeated reliability, dynamic disruptions, and replanning precedents outside the resident-in-city setting. |
| Validation methodology | `larooij2025validationcentralchallenge`; `zhao2026mechanismplausibilitygenerative` | State explicitly that agent-level execution validity does not establish human behavioral realism, macro urban validity, or causal explanation. |

## Methods

| Method choice | Citation keys | Supported design decision |
|---|---|---|
| Private intentions and role-conditioned observations | `zhou2024sotopia`; `pham2026liveculturebench` | Use asymmetric information and private goals while preventing privileged world-state leakage. |
| Environment-owned state transitions | `trivedi2024appworld`; `zhou2023webarena`; `song2026mobilitybench` | Score outcomes from executable state and deterministic replay rather than self-reported completion. |
| Dynamic invalidation and post-disruption recovery | `hui2026sttarena`; `chen2026trip`; `cheng2026doagentsknow` | Measure detection, replanning, and verification after a previously valid plan becomes invalid. |
| Constraint composition | `shao2024chinatravel`; `mao2025deliverybench` | Combine spatial, temporal, resource, and economic constraints rather than testing isolated route correctness. |
| Repeated-trial reliability | `yao2024bench` | Report reliability across repeated runs in addition to mean task success. |

## Discussion And Limitations

| Required statement | Citation keys |
|---|---|
| CityIntent evaluates execution-mechanism validity in a controlled benchmark, not whether simulated residents reproduce human mobility distributions. | `santos2026whenplausiblenot`; `anonymous2026mobisimbench` |
| Micro-level evidence must not be promoted into claims about emergent urban or social mechanisms. | `larooij2025validationcentralchallenge`; `zhao2026mechanismplausibilitygenerative` |
| The high-agency design trades population scale for trace-level diagnosis. | `chopra2024limitsagencyagent`; `li2026genworld` |

## Citation Rules

1. Cite direct competitors before general surveys when making novelty or coverage claims.
2. Do not describe CityIntent as the first city-agent, mobility, feasibility, private-goal, or disruption/replanning benchmark.
3. Use `anonymous2026mobisimbench` only in internal drafts until the final author list is public.
4. Describe arXiv-only works as preprints unless a verified proceedings or journal record is added.
5. Keep the contribution phrasing narrow: a shared typed-evidence protocol for testing whether private intentions survive authoritative urban state transitions in continuous episodes.
