# HC09 Closure Card - Spontaneous Emergence

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `HC09`

Paper: Takata et al. 2024, *Spontaneous Emergence of Agent Individuality Through Social Interactions in Large Language Model-Based Communities*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_core/10_HC09_Spontaneous_Emergence.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_core/10_HC09_Spontaneous_Emergence.fulltext.md`
- Markdown dossier: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/HC09_Spontaneous_Emergence_of_Agent_Individuality_Through_Social_Interactions_in_Larg.md`
- Extraction status: `pdfplumber`, `21` pages, `status: ok`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `anchor_core` | Keep. The paper is a direct LLM-agent social simulation with multi-agent communication, movement, and emergent group behavior. |
| `environment_side_representation` | `2D_grid` | Keep. The environment is explicitly a `50 x 50` two-dimensional grid with periodic boundary conditions. |
| `agent_accessible_representation` | `L3` | Keep. Agents receive their own coordinates, nearby messages, memories, and movement options; the interface is local-position/local-neighborhood rather than global configurational metrics. |
| `behavioral_scale` | `emergent_social_structure` | Keep. The reported outcomes include social norms, cooperation, hashtags, hallucination propagation, emotional synchronization, and personality differentiation. |
| `evidence_status` | `observed_effect` | Keep. The paper manipulates message propagation range and reports resulting differences in movement, hashtag lifespan, message diversity, hallucination count, and personality-type differentiation. |

## Evidence Notes

This is one of the cleanest anchor-core examples for local spatial mediation. The simulation places 10 initially homogeneous LLM agents in a `50 x 50` 2D grid. Agents can send messages to nearby agents, store situational memories, and choose movement commands from `x+1`, `x-1`, `y+1`, `y-1`, or `stay`.

The agent-facing representation is spatial but not geometric in the strong embodied sense. Prompts include the agent's current state, agent ID, own coordinates, prior memory, and messages received from agents within message reach. The paper also says received messages are restricted by Chebyshev distance in the default setup. This supports `L3`: local position, neighborhood exposure, movement, and co-presence-like communication. It does not support `L4` or `L5`, because agents are not given global graph metrics, visibility fields, whole-layout descriptors, raw images, depth, egocentric perception, or Space Syntax measures.

The observed-effect status is stronger than many other anchor cases. The authors explicitly vary the spatial scale of message exchange and report how this changes behavior and communication. The `stay` behavior is rare when agents cannot exchange messages, more frequent when exchange is possible, and lower again under overly wide broadcast-like ranges. Hashtag lifespan, message similarity/diversity, hallucination count, and MBTI-type differentiation also vary across communication ranges.

The manuscript should still keep the claim bounded. The paper demonstrates spatial-neighborhood effects inside a simplified 2D grid communication model. It does not demonstrate physical built-environment configuration, navigation through real geometry, or Space Syntax-style global integration/choice effects.

## Page/Section Anchors

Use these anchors for manuscript support:

- Section 2.1, page 3: `50 x 50` 2D grid, periodic boundary, random initial positions, free movement, and messaging.
- Section 2.2, pages 3-4: three agent actions, prompts, own coordinates, nearby messages, and Chebyshev-distance message reception.
- Section 2.3, pages 4-5: simulation step, recorded coordinates, generated messages, memory, and movement command conversion.
- Section 3.5, pages 12-14: spatial scale/message propagation range experiment and results for movement, hashtags, message diversity, hallucination, and MBTI differentiation.
- Section 4, pages 14-15: discussion that spatial positioning and interactions led to differentiated behavior, memories, messages, and shared narratives.

## Claim Boundary

Allowed manuscript use:

- HC09 is a strong anchor example of local-neighborhood spatial mediation in an LLM-agent society.
- It supports `2D_grid / L3 / observed_effect` because spatial position and communication range are part of the agent loop and are varied experimentally.
- It can be used to show that even simple local spatial constraints can shape communication, movement, and emergent social differentiation.

Disallowed manuscript use:

- Do not treat HC09 as evidence for 3D embodied spatial intelligence.
- Do not claim it uses or validates Space Syntax measures.
- Do not code it as `L4`; the paper analyzes spatial clusters and ranges, but global configurational metrics are not shown as agent inputs.
- Do not generalize the observed effects beyond the simplified grid/local-message setting.

## Follow-Up

No acquisition action is needed. Current coding can remain `anchor_core / 2D_grid / L3 / emergent_social_structure / observed_effect`.
