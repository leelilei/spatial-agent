# R3-04 Closure Card - LLM Epidemic-Economic Dynamics

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `R3-04`

Paper: Wang et al. 2026, *An LLM-Driven Multi-Agent Simulation Framework for Coupled Epidemic-Economic Dynamics*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_round3_candidates/R3-04_LLM_Epidemic_Economic_Dynamics_2026.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_round3_candidates/R3-04_LLM_Epidemic_Economic_Dynamics_2026.fulltext.md`
- Markdown dossier: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/R3-04_An_LLM_Driven_Multi_Agent_Simulation_Framework_for_Coupled_Epidemic_Economic_Dyn.md`
- Extraction status: `pdfplumber`, `24` pages, `status: ok`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `anchor_core` | Keep. The paper is a direct LLM-driven multi-agent ABM for epidemic-economic dynamics. |
| `environment_side_representation` | `2D_grid` | Keep. The environment is a rectangular 2D gridworld representing an abstract city, with proximity-based contact. |
| `agent_accessible_representation` | `L3` | Keep. Agents receive prompt-mediated position, nearby people, visible symptoms, nearest business, economic state, and available actions; no global geometry/configuration metrics are agent-facing. |
| `behavioral_scale` | `emergent_social_structure` | Keep. The reported outcomes are population-level epidemic curves, unemployment, GDP/wealth loss, WFH adaptation, lockdown effects, and economic-health trade-offs. |
| `evidence_status` | `observed_effect` | Keep. The paper reports multiple scenario outcomes, sensitivity analysis, scale checks, LLM generalization, and empirical epidemic-curve comparison. |

## Evidence Notes

R3-04 is a compact but valid anchor-core example because spatial contact is part of the ABM loop. The environment is explicitly a rectangular 2D gridworld representing an abstract city. Persons, businesses, and government entities operate in this shared environment. Disease transmission occurs through physical proximity/contact distance within the continuous 2D grid, superimposed on household and employment/economic links.

The agent-facing representation is prompt-level and local. The prompt includes current health, position, age, wealth, social class, epidemic news, nearby people within a local range, symptom visibility, nearest business distance/status/cost, shopping urgency, and available actions such as GoToWork, GoShopping, StayHome, and SeekMedicalCare. Agents perceive their immediate locality and can distinguish symptomatic individuals from healthy-appearing individuals, but not exact hidden infection state.

This supports `2D_grid / L3`. The system uses spatial position and local proximity, but the LLM agent is not given raw geometry, vision, a global map, or global graph/layout metrics. It reasons over local observations and action options inside an abstract grid-world epidemic-economic ABM.

Observed-effect status is supported. Scenarios show laissez-faire epidemic/economic collapse, dynamic lockdown flattening with economic volatility, decentralized work-from-home adaptation, and distinct health-economy trade-offs. The paper also reports population-scale consistency, LLM-backend generalization, parameter sensitivity, and comparison with empirical early COVID infection-ratio curves. These are observed system-level effects, not controlled tests of spatial configuration.

## Page/Section Anchors

Use these anchors for manuscript support:

- Abstract and Section 1, pages 1-2: LLM-driven multi-agent framework, PDA loop, health/economic trade-offs, and macro outcomes.
- Section 3.1, page 4: rectangular 2D gridworld, persons/businesses/government, hourly iterations, and proximity-based SEIR transmission.
- Section 3.2, pages 4-5: household units, employment graph, dynamic spatial contact layer, and Person/Business/Government agent action spaces.
- Section 3.3-3.4, pages 5-6: Perception-Deliberation-Action loop, partial local observability, frozen global-state snapshot, CoTA prompts, and concurrent execution.
- Section 5, pages 9-15: scenario outcomes, epidemic/economic curves, lockdown, WFH adaptation, and generalization checks.
- Appendix A, pages 19-21: prompt templates with position, nearby people, nearest business, economic state, visible symptoms, and available actions.

## Claim Boundary

Allowed manuscript use:

- R3-04 supports a simplified `2D_grid / L3` case where spatial proximity structures epidemic-economic interaction among LLM agents.
- It can be used as observed-effect evidence for emergent macro outcomes arising from local cognitive agent decisions in an abstract spatial ABM.
- It is useful for showing that spatial representation can be minimal but still behaviorally relevant when contact/proximity matters.

Disallowed manuscript use:

- Do not code R3-04 as direct geometry or embodied spatial intelligence.
- Do not claim the paper demonstrates physical built-environment layout effects.
- Do not code it as `L4`; no global grid/network metrics are shown as agent-facing inputs.
- Do not treat epidemic/economic curves as evidence of Space Syntax or architectural configuration.

## Follow-Up

No acquisition action is needed. Current coding can remain `anchor_core / 2D_grid / L3 / emergent_social_structure / observed_effect`.
