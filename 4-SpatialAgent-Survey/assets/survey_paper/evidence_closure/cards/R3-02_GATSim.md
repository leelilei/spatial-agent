# R3-02 Closure Card - GATSim

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `R3-02`

Paper: Liu et al. 2025, *GATSim: Urban Mobility Simulation with Generative Agents*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_round3_candidates/R3-02_GATSim_2025.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_round3_candidates/R3-02_GATSim_2025.fulltext.md`
- Markdown dossier: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/R3-02_GATSim_Urban_Mobility_Simulation_with_Generative_Agents.md`
- Extraction status: `pdfplumber`, `56` pages, `status: ok`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `anchor_core` | Keep. GATSim is a generative-agent urban mobility simulation framework with memory, planning, reaction, and reflection. |
| `environment_side_representation` | `graph_based` | Keep. The transportation environment is formally represented as graph nodes/links, facilities, transit links, tilemaps, and bitmap visualizations. |
| `agent_accessible_representation` | `L3` | Keep. Agents use activity states, locations, travel paths, local network/trip context, spatial-temporal memory, route/mode options, and congestion experiences; no global graph metrics are shown as direct agent inputs. |
| `behavioral_scale` | `emergent_social_structure` | Keep. The main outcomes are aggregate mobility adaptation, congestion spreading, incident response, and route/mode/departure-time changes. |
| `evidence_status` | `observed_effect` | Keep. The paper reports human-agent behavioral comparison, multi-day congestion adaptation, and network-incident response. |

## Evidence Notes

GATSim is best coded as `graph_based / L3`. The simulation core uses a hierarchical transportation-network representation with graph, tilemap, and bitmap formats. The transportation network is formally `G = (V, E)`, where nodes and links represent the network, facilities such as apartments/offices/schools serve as origins/destinations, and transit lines connect to the road network through boarding/alighting links.

Agent cognition is spatial-temporal but not globally configurational. Short-term memory stores activity plans, ongoing states, travel paths, and immediate perceptions. Long-term memory stores ConceptNodes with textual content, embeddings, keywords, spatial coverage, temporal scope, importance, timestamps, and access histories. Retrieval combines keyword, semantic, and spatial-temporal relevance. This supports `L3`: place/path/local experience and memory over a graph-like mobility environment.

The paper does mention bitmap input for LLMs with image capabilities, but the evidence row should remain `L3` because the dominant agent-facing structure is network/facility/activity/travel-path context, not embodied first-person visual perception. The paper also identifies spatial reasoning limitations in LLM agents, which reinforces a conservative boundary.

Observed-effect status is supported. GATSim reports that agents adapt departure times, routes, and mode choices over multiple days as they accumulate travel experiences. In an incident experiment, agents react to link capacity reduction, shift departure times, avoid routes, overreact, and gradually recover. These are observed mobility-system effects, not Space Syntax or global metric effects.

## Page/Section Anchors

Use these anchors for manuscript support:

- Abstract and Introduction, pages 1-5: GATSim integrates transportation simulation, generative agents, memory, planning, reaction, and reflection.
- Section 3.1, pages 9-10: graph/tilemap/bitmap network representation, nodes, links, facilities, transit links, point queues, and capacity constraints.
- Section 5.1, pages 13-15: short-term/long-term memory, spatial coverage, temporal scope, spatial-temporal retrieval, and route/congestion memories.
- Section 6.1, pages 24-27: human-agent behavioral comparison and flexible reactive behavior.
- Section 6.2, pages 29-30: multi-day traffic evolution, peak spreading, congestion reduction, and route/mode/departure-time adaptation.
- Section 6.3, pages 30-33: network incident response, temporal shifting, route avoidance, over-reaction, and gradual recovery.

## Claim Boundary

Allowed manuscript use:

- GATSim is a strong anchor example of graph/place/path-level urban mobility simulation with LLM-agent memory and adaptation.
- It supports `graph_based / L3 / observed_effect` because agents reason over travel paths, facilities, congestion, route options, and spatial-temporal memories.
- It can be used to show a transition from rule-based mobility ABM toward cognitively grounded mobility agents.

Disallowed manuscript use:

- Do not code GATSim as `L4`; network topology exists environment-side, but global centrality, betweenness, integration, or whole-network metrics are not shown as agent-facing decision features.
- Do not code it as `L5`; bitmap/map visualization is not first-person embodied sensory input.
- Do not claim it validates Space Syntax constructs.
- Do not overstate the prototype scale; the reported experiment uses a stylized 13-node network and 70 synthetic individuals.

## Follow-Up

No acquisition action is needed. Current coding can remain `anchor_core / graph_based / L3 / emergent_social_structure / observed_effect`.
