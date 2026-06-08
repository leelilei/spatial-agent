# BK01 Closure Card - AgentSociety

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `BK01`

Paper: Piao et al. 2025, *AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_core/07_AgentSociety_Piao2025.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_core/07_AgentSociety_Piao2025.fulltext.md`
- Markdown dossier: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/BK01_AgentSociety_Large_Scale_Simulation_of_LLM_Driven_Generative_Agents_Advances_Und.md`
- Extraction status: `pdfplumber`, `45` pages, `status: ok`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `anchor_core` | Keep. AgentSociety is a large-scale LLM-driven social simulator with mobility, social, and economic behavior modules. |
| `environment_side_representation` | `graph_based` | Keep. The societal environment includes urban road networks, AOIs, POIs, transport modes, social networks, and economic structures. |
| `agent_accessible_representation` | `L3` | Keep. Agents use location-bearing memory, POIs, AOIs, routes/travel plans, distance-based place selection, and environmental feedback; no global configurational metrics are shown as agent inputs. |
| `behavioral_scale` | `emergent_social_structure` | Keep. The paper reports large-scale social/economic/mobility experiments including polarization, inflammatory-message spread, UBI, and hurricane mobility. |
| `evidence_status` | `observed_effect` for social-simulation outcomes; `designed_affordance_only` for spatial-representation claims | Keep row as conservative unless the table later separates these two evidence dimensions. |

## Evidence Notes

AgentSociety is a broad simulator rather than a paper about spatial representation alone. It includes a realistic societal environment divided into urban, social, and economic spaces. Urban space includes road networks, AOIs, POIs, walking, driving, public transit, taxis, routes, positions, speeds, travel plans, and feedback about time and cost. Social space includes online/offline social networks and moderation. Economic space includes accounts, firms, banks, government, employment, consumption, taxation, and indicators such as GDP.

The agent-level spatial interface is place- and mobility-oriented. The mobility module converts needs into intention extraction, POI type selection, radius decision, and gravity-model place selection. The memory system stores stream-memory nodes with time, location, and event description. After an action, the agent receives event feedback such as whether it reached the correct location under environmental factors like weather. This supports `L3`: a structured local/place/travel interface with feedback and memory.

The paper also contains observed outcomes. It runs social experiments on polarization, inflammatory messages, UBI, and Hurricane Dorian mobility. The hurricane experiment uses SafeGraph POIs/mobility and CBG demographic data, involves 1000 agents, incorporates real-time weather, and compares activity-level spatial distributions plus daily outflow trends against real data. These outcomes support AgentSociety as a validated large-scale social simulator.

The conservative evidence-status boundary remains important. The reported experiments validate broad simulator behavior and social/mobility responses, but the paper does not isolate spatial representation as an experimental factor. It does not show that different spatial encodings, graph metrics, or layout configurations cause the observed social outcomes. Therefore, for claims specifically about spatial-representation effects, the row should remain `designed_affordance_only`; if the evidence table later separates system-outcome evidence from spatial-effect evidence, AgentSociety can be marked as observed-effect for overall simulation outcomes.

## Page/Section Anchors

Use these anchors for manuscript support:

- Section 2, pages 3-4: AgentSociety overview and its three components: LLM-driven agents, realistic societal environment, and large-scale simulation engine.
- Section 3.3, page 9: mobility behavior, need-plan-behavior sequence, POI type selection, radius decision, and gravity-model place selection.
- Section 3.6, pages 12-13: memory system, time/location/event-description memory nodes, event feedback, and environmental-event processing.
- Section 4, pages 14-16: realistic societal environment with urban, social, and economic spaces.
- Section 4.2, page 15: road networks, AOIs, POIs, multimodal mobility, routes, OpenStreetMap/SafeGraph data, agent-position initialization, travel plans, and monitoring APIs.
- Section 7.5, pages 33-35: Hurricane Dorian mobility experiment, SafeGraph/CBG data, 1000 agents, real-time weather, activity-level spatial distributions, and simulated versus real daily outflow patterns.

## Claim Boundary

Allowed manuscript use:

- AgentSociety is an anchor example of a large-scale LLM social simulator with explicit urban, social, and economic environment layers.
- It supports `graph_based / L3` because agents interact with POIs, AOIs, travel plans, distance-based place selection, location-bearing memory, and environmental feedback.
- It can be used to show that realistic societal simulators increasingly require structured urban environments for mobility and social/economic behavior closure.

Disallowed manuscript use:

- Do not claim AgentSociety directly demonstrates Space Syntax or global spatial-configuration effects.
- Do not code it as `L4`; global road/AOI/POI structures exist environment-side, but global network metrics are not shown as agent-facing decision inputs.
- Do not code it as `L5`; there is no first-person visual/geometric embodiment evidence.
- Do not treat the hurricane/UBI/social-network experiments as causal tests of spatial representation unless the manuscript explicitly frames them as overall simulator-validation evidence.

## Follow-Up

No acquisition action is needed. Current representation coding can remain `anchor_core / graph_based / L3`. Keep `evidence_status` conservative as `designed_affordance_only` for spatial-representation claims, while noting observed simulator-level outcomes in prose.
