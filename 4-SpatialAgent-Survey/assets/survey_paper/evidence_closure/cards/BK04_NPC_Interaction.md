# BK04 Closure Card - Voice-Controlled NPC Interaction

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `BK04`

Paper: *A Voice-Controlled Dialogue System for NPC Interaction using Large Language Models*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_adjacent/07_BK04_NPC_Interaction.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_adjacent/07_BK04_NPC_Interaction.fulltext.md`
- Extraction status: `10` pages, `status: ok`, `text_char_count: 34654`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `bridge_core` | Keep. The system is a single-user game/NPC interaction prototype. |
| `environment_side_representation` | `3D_engine` | Keep. The prototype is built in Unity as a narrative game environment with NPCs and first-person interaction. |
| `agent_accessible_representation` | `L2` | Keep. The LLM maps free-form speech to predefined dialogue options and receives textual dialogue state, not spatial structure. |
| `behavioral_scale` | `interaction` | Keep. The empirical unit is player-to-NPC dialogue. |
| `evidence_status` | `designed_affordance_only` | Keep. The user study evaluates voice-interface experience, not a spatial-behavior effect. |

## Evidence Notes

The paper implements a Unity prototype for narrative-driven gameplay. The LLM is used as a mapper from player speech input to one of several predefined dialogue options in a structured dialogue graph. Whisper and translation components support voice input, while Unity handles game mechanics, visuals, characters, controls, and dialogue progression.

The user study includes 14 participants and compares voice-controlled interaction with a point-and-click interface. The study reports player perceptions of immersion, freedom, joy, voice-interface confidence, and mapping accuracy. These outcomes support the paper as a useful bridge case for LLM-enabled NPC dialogue, but not for spatially rich agent simulation.

The row should stay `L2`. The game is visually and spatially situated, but the LLM-facing state is the current NPC dialogue and available dialogue options. The paper does not show object coordinates, navigation topology, global layout, embodied perception, or spatial memory as agent input.

## Page/Section Anchors

- Abstract and Introduction, pages 1-2: voice-controlled interface, Unity prototype, LLM mapping, and user study with 14 participants.
- Method section, pages 2-4: structured dialogue graph, Unity implementation, speech capture, transcription, translation, and mapping to dialogue options.
- User Study, pages 4-6: procedure, questionnaires, and participants.
- Results and Discussion, pages 6-8: immersion, freedom, mapping accuracy, latency, and voice-interface limitations.

## Claim Boundary

Allowed manuscript use:

- Use `BK04` as a bridge example of LLM-supported NPC interaction in a Unity game.
- Use it to illustrate that many VR/game LLM-NPC systems remain dialogue-interface systems despite 3D presentation.

Disallowed manuscript use:

- Do not claim the LLM agent is spatially aware beyond the narrative scene.
- Do not use this as evidence for `L3`, `L4`, or `L5`.
- Do not treat the user-study outcomes as spatial-representation effects.

## Follow-Up

No acquisition action is needed. Current coding can remain `bridge_core / 3D_engine / L2 / interaction / designed_affordance_only`.
