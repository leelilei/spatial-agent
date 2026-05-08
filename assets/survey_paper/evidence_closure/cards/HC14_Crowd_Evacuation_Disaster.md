# HC14 Closure Card - Crowd Evacuation Disaster

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `HC14`

Paper: Yang et al. 2026, *When agents learn to think: Large language model-enhanced agent-based modeling for crowd evacuation in disaster scenarios*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_core/15_HC14_Crowd_Evacuation_Disaster.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_core/15_HC14_Crowd_Evacuation_Disaster.fulltext.md`
- Markdown dossier: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/HC14_When_agents_learn_to_think_Large_language_model_enhanced_agent_based_modeling_fo.md`
- Extraction status: `pdfplumber`, `17` pages, `status: ok`, DOI `10.1016/j.ress.2025.112056`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `anchor_core` | Keep. The paper is a large-scale LLM-enhanced ABM for regional disaster evacuation. |
| `environment_side_representation` | `graph_based` | Keep. The simulation uses a GIS-derived road network with road segments, speed limits, width-based constraints, shelters, exits, and route planning. |
| `agent_accessible_representation` | `L3` | Keep. Agents receive prompt-level current location, surroundings, hazard conditions, nearby communications, road status, decision history, and stage-specific options. |
| `behavioral_scale` | `mixed` | Keep. The paper reports individual decisions, route revision, assistance, information dissemination, road usage, congestion, and casualty-related outcomes. |
| `evidence_status` | `observed_effect` | Keep. The paper compares LLM-enhanced ABM against conventional ABM and reports emergent communication, rerouting, road usage, and evacuation outcomes. |

## Evidence Notes

HC14 is a graph/place-level evacuation simulation. The movement system covers pedestrian and vehicular evacuation, and the road network is constructed from GIS data. The Arahama case study reconstructs roads from pre-disaster satellite imagery, assigns speed limits based on road width, defines a vertical shelter and inland exits, and models pedestrian/vehicle movement and congestion.

The agent-facing representation is prompt-mediated and local. Each agent has attributes such as age, gender, current location, vehicle ownership, and family structure. Dynamic information includes current time, hazard conditions, nearby communications, road status, crowd movement, local emotion, and memory of past decisions. Agents perceive crowd movement and emotion within a 25 m radius and conversations within a 5 m radius. Stage-specific prompts include evacuation options, road conditions, shelter arrival status, and occupancy.

This supports `graph_based / L3`. The road network is spatially explicit, but the LLM agent is not shown receiving raw geometry, pixels, coordinates as continuous embodied sensors, global network centrality, or Space Syntax-style integration/choice metrics. It reasons over local road status, route options, destination choices, communications, and memory.

Observed-effect status is supported by the comparison with a conventional ABM. The LLM-enhanced ABM can simulate delayed departure, assistance to others, detours around congestion, social information diffusion, and more realistic road usage. The conventional ABM keeps nearest-shelter/shortest-path assumptions and lacks communication, assistance, or plan revision. This is valid evacuation-behavior evidence, not a controlled test of global spatial configuration.

## Page/Section Anchors

Use these anchors for manuscript support:

- Abstract and Section 1, pages 1-2: LLM agents with personality traits, environmental observations, decision histories, communication, and pedestrian/vehicle evacuation.
- Figure 2 and Section 2, pages 2-3: framework with prompt generation, LLM request, and moving system; GIS road network for spatial realism.
- Section 2.1.2, pages 5-6: user prompt structure with personality, surroundings, memories, current location, hazard information, crowd behavior/emotion, nearby conversations, and road conditions.
- Section 2.3, pages 7-8: evacuation environment, fastest-path routing, detours under congestion, pedestrian/vehicle movement, road width/speed limits, and group evacuation.
- Section 3, pages 8-10: Arahama case study, vertical shelter, inland exits, pre-disaster road network, population generation, tsunami timeline, and snapshots.
- Section 3.2-3.3, pages 10-12: dynamic decision-making, assistance, social information diffusion, road-usage comparison, and adaptive rerouting.

## Claim Boundary

Allowed manuscript use:

- HC14 is a strong anchor example of LLM agents operating over a GIS road network with local hazard, communication, road-status, and memory prompts.
- It supports `graph_based / L3 / observed_effect` for adaptive evacuation behavior.
- It can be used to show how LLM-enhanced ABM adds communication, assistance, and route revision to conventional evacuation simulation.

Disallowed manuscript use:

- Do not code HC14 as `L4`; global network metrics are not shown as direct agent inputs.
- Do not code HC14 as `L5`; the paper does not expose first-person visual/geometric embodied streams to the LLM.
- Do not claim it validates Space Syntax measures or causal layout effects.
- Do not overstate casualty/road-usage alignment as proof of general spatial intelligence beyond the tsunami-evacuation setup.

## Follow-Up

No acquisition action is needed. Current coding can remain `anchor_core / graph_based / L3 / mixed / observed_effect`.
