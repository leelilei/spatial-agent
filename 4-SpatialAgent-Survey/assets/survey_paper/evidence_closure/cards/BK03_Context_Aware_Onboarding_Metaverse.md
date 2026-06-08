# BK03 Closure Card - Context-Aware Onboarding Agent for Metaverse

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `BK03`

Paper: Lee et al. 2024, *A Context-Aware Onboarding Agent for Metaverse Powered by Large Language Models*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_adjacent/19_BK03_Context_Aware_Onboarding_Metaverse_2024.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_adjacent/19_BK03_Context_Aware_Onboarding_Metaverse_2024.fulltext.md`
- Source note: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/BK03.source.md`
- Extraction status: `18` pages, `status: ok`, `text_char_count: 85934`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `bridge_core` | Keep. PICAN is a single-user onboarding assistant in a metaverse environment. |
| `environment_side_representation` | `3D_engine` | Keep. The system operates in a virtual/metaverse world with avatar movement, objects, places, and activities. |
| `agent_accessible_representation` | `L2` | Keep. The agent uses logged current location, visible objects, recent dialogue, recent actions, and exploration history; it is context-aware but not topology- or geometry-driven. |
| `behavioral_scale` | `interaction` | Keep. The task is user-NPC onboarding interaction. |
| `evidence_status` | `observed_effect` | Keep. The paper reports an ablation study and a user study showing effects of context usage. |

## Evidence Notes

PICAN is an LLM-based pipeline for an onboarding AI NPC in a metaverse setting. The formative study identifies two key context types: short-term spatiotemporal context and long-term exploration context. Short-term context includes user location, recent dialogue, and recent actions; long-term context includes visited locations, performed actions, and past experience history.

The implemented pipeline continuously logs user location, actions, visited locations, performed actions, and conversation history. It resolves references to objects, locations, and interactions using spatial, dialogic, and action context, then uses exploration history to customize suggestions and explanations. The system was evaluated through an ablation study with 20 evaluators and a user study with 21 participants.

The representation remains `L2`. Spatial context is used for reference resolution and localized assistance, but the LLM is not shown to receive a structured city graph, global navigation network, topological centrality, coordinates as a decision geometry, first-person sensory streams, or explicit metric maps. The bridge value is in context-aware assistance, not in spatial simulation scale.

## Page/Section Anchors

- Abstract and Introduction, pages 1-2: short-term spatiotemporal context, long-term exploration context, ablation study, and user study.
- Section 3, pages 3-6: formative study and requirements for spatial, dialogic, action, and exploration context.
- Section 4.1-4.3, pages 6-8: PICAN logging, reference resolution, and long-term exploration response generation.
- Section 5, pages 9-11: ablation study showing usefulness and immersion effects.
- Section 6, pages 11-15: user study and participant feedback on spatial and long-term context.

## Claim Boundary

Allowed manuscript use:

- Use `BK03` as a bridge example of context-aware LLM assistance in a virtual world.
- Use it to support observed-effect claims for short-term spatial/dialogic/action context in onboarding responses.
- Use it as `3D_engine / L2`, not as a high-level spatial simulation case.

Disallowed manuscript use:

- Do not claim PICAN simulates emergent social structure.
- Do not code it as `L3`, `L4`, or `L5` without new evidence showing agent-facing topology, metric maps, or embodied sensory streams.
- Do not treat user-location awareness as proof of configurational spatial reasoning.

## Follow-Up

No acquisition action is needed. Current coding can remain `bridge_core / 3D_engine / L2 / interaction / observed_effect`.
