# CityAgency Reference Expansion Audit

Date: 2026-07-03

## Inventory

- Verified unique references: 45
- Archived PDF/fulltext/note packages: 44
- Verified references awaiting a retrievable PDF: 1
- Version duplicates not counted as new papers: 1, the published GATSim article

The pending paper is *Generative Agents in Agent-Based Modeling: Overview,
Validation, and Emerging Challenges* (IEEE Transactions on Artificial
Intelligence, 2025). Its metadata and relevance are verified, but both the
publisher endpoint and the available author-copy endpoint reject automated PDF
retrieval. It must not be reported as locally archived until a valid PDF exists.

## New Archived References

| Group | Paper | Decision | Why it changes CityAgency |
|---|---|---|---|
| Direct competitor | LiveCultureBench | must-cite | Already combines a graph-based small city, resident daily goals, supporting agents, norm scoring, and verifier uncertainty. |
| Direct competitor | MobilityBench | must-cite | Already provides deterministic replay and process diagnostics for real route-planning agents. |
| Direct competitor | DeliveryBench | must-cite | Already tests long-horizon embodied city execution under time, cost, battery, and interaction constraints. |
| Scale boundary | GenWorld | cite | Shows empirically grounded LLM-agent simulation at 196,608-resident scale through offline policy compilation. |
| Scale boundary | On the Limits of Agency in ABMs | cite | Makes the individual-expressiveness versus population-scale trade-off explicit. |
| Mobility method | TrajGenAgent | cite | Separates activity-chain planning from deterministic spatiotemporal grounding and adds individual anomaly checks. |
| Mobility method | AgentMob | cite | Grounds next-location prediction in analytical tools, but does not provide post-action execution evidence. |
| Urban application | Multi-Stakeholder Urban Planning | maybe | Evaluates discursive stakeholder agency rather than physical resident execution. |
| Validation foundation | Validation Is the Central Challenge | must-cite | Shows that generative ABMs often rely on validation weakly linked to their claimed mechanisms. |
| Validation foundation | Mechanism Plausibility | must-cite | Separates agent-level evidence from ABM-level explanatory claims and exposes frequent category errors. |

## Positioning Change

The old gap statement, "no compact city benchmark combines private goals,
social context, and constrained action," is no longer defensible.

The revised gap is:

> CityAgency compares heterogeneous urban-agent frameworks through one shared,
> typed evidence protocol. It measures whether plausible plans and completion
> claims survive authoritative spatial, temporal, resource, and social state
> transitions across a continuous episode.

This is an agent-level execution-mechanism contribution. Human behavioral realism,
population mobility realism, and macro urban validity remain separate empirical
claims that require separate data and validation.

## Immediate Consequences

1. Treat LiveCultureBench and DeliveryBench as direct competitors in the main table.
2. Retain plan plausibility, but make unsupported completion claims and typed state evidence central outcomes.
3. Compare actual agent architectures through adapters, not only foundation models behind one custom policy.
4. Publish the human construct-validity audit and disagreement statistics.
5. Avoid claiming that CityAgency proves agents are human-like or that agent-level success validates a city-scale ABM.
