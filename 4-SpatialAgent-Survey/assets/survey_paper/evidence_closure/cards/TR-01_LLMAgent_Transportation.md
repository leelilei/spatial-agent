# TR-01 Closure Card - LLM-Agent Transportation Modeling

Status: `C3 closed_card_done`

Date: 2026-05-02

Evidence row: `TR-01`

Paper: Liu, Yang, and Yin 2025, *Toward LLM-agent-based modeling of transportation systems: A conceptual framework*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_adjacent/16_TR-01_LLMAgent_Transportation_2025.pdf`
- DOI: `10.1016/j.ait.2025.100001`
- Journal: *Artificial Intelligence for Transportation*

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `bridge_core` | Keep. The paper is a transportation-modeling framework and proof of concept, not a strict LLM multi-agent social-simulation anchor case. |
| `environment_side_representation` | `graph_based` | Keep. The environment is a transportation network / dynamic traffic assignment simulator. |
| `agent_accessible_representation` | `L3` | Keep. Agents receive POIs, candidate routes, structured travel alternatives, route choices, travel times, and feedback, but no global configurational summaries are shown as agent-facing input. |
| `behavioral_scale` | `mixed` | Keep. The behavior is activity/travel demand generation and mobility adaptation, not interpersonal social interaction. |
| `evidence_status` | `observed_effect` | Keep. The proof of concept reports generated activities, structured travel-plan formatting, and learning from travel outcomes over repeated days. |

## Evidence Notes

The paper proposes an LLM-agent-based framework for transportation systems in which LLM agents represent human travelers. The framework includes profile, perception, decision-making, and action modules. The perception module is explicitly agent-facing: it allows agents to query and extract information from the physical environment, including points of interest, candidate routes, structured numerical data, and feedback on past travel outcomes. The decision-making module integrates profile attributes, memory, and perceived environmental data into natural-language prompts.

The proof-of-concept simulation uses ten GPT-4o household agents in a four-zone miniature transportation network. Agents generate activities, construct tours, specify origin/destination, departure time, route selection, and update travel memory using outcomes such as expected arrival time, actual arrival time, and total travel time. This is stronger than a backend-only transportation simulator because transportation information enters the agent decision loop.

However, the reviewed full text does not show that agents receive global abstract network/configurational measures such as accessibility rank, centrality, betweenness, impedance summaries, reachable-opportunity counts, or network-wide route-structure summaries. The available evidence supports local route/travel-option and feedback exposure. Therefore the row is coded as `L3`, with a note that it is an `L3-L4` boundary case for future transportation-network coding.

## Page/Section Anchors

- Abstract, page 1: structured profiles, memory systems, perception, decision-making, and action modules.
- Section 3.1, page 4: physical environment as dynamic transportation network simulator.
- Section 3.2, pages 4-5: profile, perception, decision-making, and action modules.
- Section 3.3, page 6: activity generation, tour-level decisions, final itinerary construction, and feedback.
- Section 5.1, pages 10-11: four-zone network, route options, household agents, and memory systems.
- Section 5.2, pages 11-13: activity generation, formatting, and learning from travel outcomes.

## Claim Boundary

Allowed manuscript use:

- Use `TR-01` as bridge evidence that transportation modeling has begun to expose environment and route information to LLM agents.
- Use it to refine the gap from "LLM agents lack spatial input" to "few systems expose global configurational structure as a controlled agent-facing variable."
- Use it as an example of an `L3-L4` boundary case that strengthens the need for precise coding.

Disallowed manuscript use:

- Do not code it as `L4` unless additional evidence shows agent-facing accessibility, centrality, impedance, reachable-opportunity, or other global network summaries.
- Do not use it as strict anchor evidence for physical-layout Space Syntax mediation.
- Do not claim it tests social behavior effects of configurational space.

## Follow-Up

If later versions or supplementary materials reveal agent-facing accessibility scores, centrality measures, impedance summaries, or global route-structure descriptors, reconsider the row as `L4` under a transportation-network bridge qualifier.
