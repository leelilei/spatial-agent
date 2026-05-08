# R3-03 Closure Card - Cognitive Agents in Urban Mobility

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `R3-03`

Paper: Jordán et al. 2025, *Cognitive Agents in Urban Mobility: Integrating LLM Reasoning into Multi-Agent Simulations*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_round3_candidates/R3-03_Cognitive_Agents_Urban_Mobility_2025.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_round3_candidates/R3-03_Cognitive_Agents_Urban_Mobility_2025.fulltext.md`
- Extraction status: `32` pages, `status: ok`, `text_char_count: 95437`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `bridge_core` | Keep. It is an urban mobility simulation with cognitive agents; direct interpersonal social interaction is weak. |
| `environment_side_representation` | `graph_based` | Keep. SimFleet models geolocated agents, routes, transport infrastructure, stops, vehicles, and proximity/event triggers. |
| `agent_accessible_representation` | `L3` | Keep. Agents use location, route, modal options, travel outcomes, short/long-term memory, and environmental disruption feedback, not raw geometry or global topology metrics. |
| `behavioral_scale` | `mixed` | Keep. The study combines mobility routines, disruption response, and profile-level aggregate behavior. |
| `evidence_status` | `observed_effect` | Keep. The paper reports a 20-day simulation with 320 agents, disruption experiments, and memory ablations. |

## Evidence Notes

The paper integrates LLM-based cognitive agents into SimFleet, an agent-based urban mobility simulator. SimFleet includes spatially embedded customer, pedestrian, bus, taxi, electric taxi, station, and infrastructure agents. The MovableMixin supports autonomous navigation, spatial localization, and route planning; infrastructure agents are spatially positioned and can be derived from OpenStreetMap.

The experiment simulates 320 agents over 20 days, including baseline and disrupted transport conditions. A severe taxi strike deactivates 80% of taxi agents, and cognitive agents adapt through short-term memory, long-term memory, reflection, and re-planning. The ablation study compares no-memory, short-term-memory, and full-memory variants over 6,400 trips.

The row is `L3` because agents reason over structured mobility context rather than embodied geometry. They receive and remember travel plans, mode choices, outcomes, waiting times, and disruption experience. The study does not expose global network centrality, Space Syntax metrics, full route topology, visual observations, or mesh-level geometry as agent-facing inputs.

## Page/Section Anchors

- Abstract and Introduction, pages 1-4: 320 agents, 20-day simulation, disruption response, and memory-driven planning.
- Section 3, pages 8-11: SimFleet architecture, geolocated agents, navigation, infrastructure, and OSM-derived locations.
- Section 4, pages 11-16: cognitive architecture, memory, planning, reflection, and structured memory.
- Section 6.1-6.2, pages 19-24: baseline mobility behavior and taxi-strike adaptation.
- Section 6.3, pages 24-25: ablation study with 6,400 trips and memory-module effects.

## Claim Boundary

Allowed manuscript use:

- Use `R3-03` as bridge evidence that LLM reasoning and memory can operate in a structured urban mobility simulator.
- Use it for observed-effect claims about mobility adaptation under disruption.
- Use it as `graph_based / L3`, not as embodied `L5`.

Disallowed manuscript use:

- Do not treat it as strong interpersonal social simulation evidence.
- Do not code it as `L4`; global transport-network metrics are not shown as direct agent inputs.
- Do not claim observed adaptation proves spatial-configuration causality.

## Follow-Up

No acquisition action is needed. Current coding can remain `bridge_core / graph_based / L3 / mixed / observed_effect`.
