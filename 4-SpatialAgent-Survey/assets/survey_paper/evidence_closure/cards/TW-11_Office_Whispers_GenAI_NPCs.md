# TW-11 Closure Card - Office Whispers GenAI NPCs

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `TW-11`

Paper: Zargham et al. 2026, *Dialogs with GenAI NPCs: Exploring Player Interactions with Speech Agents in a VR Game*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_adjacent/15_TW-11_Office_Whispers_GenAI_NPCs_2026.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_adjacent/15_TW-11_Office_Whispers_GenAI_NPCs_2026.fulltext.md`
- Source note: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/TW-11.source.md`
- Extraction status: `30` pages, `status: ok`, `text_char_count: 118691`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `bridge_core` | Keep. The paper studies a speech-based VR game with GenAI NPCs, not population simulation. |
| `environment_side_representation` | `3D_engine` | Keep. Office Whispers is a VR adventure/puzzle game with rooms, NPCs, objects, and player movement. |
| `agent_accessible_representation` | `L2` | Keep. NPCs are spatially situated, but the study highlights limited context awareness and does not show geometry/topology as agent input. |
| `behavioral_scale` | `interaction` | Keep. The behavior is player-NPC conversation and puzzle interaction. |
| `evidence_status` | `observed_effect` | Keep. The user study with 48 participants reports player experience, immersion, agency, and limitations. |

## Evidence Notes

Office Whispers is a VR adventure/puzzle game in a virtual office. Players move through rooms, interact with objects, solve puzzles, and communicate by speech with four GenAI-based NPCs occupying office roles. Conversations occur when players stand near an NPC; recognized player input and NPC responses appear in a chat box. NPCs remain stationary at designated locations.

The evidence supports `3D_engine` and `interaction`, but only `L2` agent access. The NPCs are embedded in a room-based game environment, yet the paper repeatedly reports context-awareness limitations: hallucinations, irrelevant responses, limited alignment with game events, prior actions, room/object state, and narrative progression. The paper itself calls for stronger grounding in real-time game state, environmental changes, and player action history.

Observed-effect status is justified for user experience. The study reports that players found the system immersive, novel, and agency-enhancing, while speech recognition issues, turn-taking, hallucinations, and limited context awareness disrupted play.

## Page/Section Anchors

- Abstract and Introduction, pages 2-4: VR game with GenAI NPCs and user-study framing.
- Game Design, pages 8-10: office rooms, four NPCs, puzzles, speech interaction, proximity, and object interaction.
- Study Method, pages 10-12: participant procedure and measures.
- Results and Discussion, pages 12-22: immersion, agency, novelty, speech interaction, GenAI communication, and context-awareness limitations.
- Limitations, pages 22-23: need to manipulate game state, environmental changes, and player-action history.

## Claim Boundary

Allowed manuscript use:

- Use `TW-11` as bridge evidence for LLM-based NPC interaction in a room-based VR game.
- Use it as an observed-effect user-study case for immersion and agency.
- Use it to support the survey's caution that 3D presentation often exceeds agent-facing spatial grounding.

Disallowed manuscript use:

- Do not code it as `L5`; no raw embodied perception is shown for NPC decision making.
- Do not claim robust object/location reasoning; participants raised the opposite concern.
- Do not treat it as emergent multi-agent social simulation.

## Follow-Up

No acquisition action is needed. Current coding can remain `bridge_core / 3D_engine / L2 / interaction / observed_effect`.
