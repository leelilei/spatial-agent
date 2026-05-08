# TW-09 Closure Card - ELLMA-T Social VR

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `TW-09`

Paper: Pan et al. 2024/2025, *ELLMA-T: An Embodied LLM-Agent for Supporting English Language Learning in Social VR*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_adjacent/12_TW-09_ELLMA-T_Social_VR_2024.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_adjacent/12_TW-09_ELLMA-T_Social_VR_2024.fulltext.md`
- Source note: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/TW-09.source.md`
- Extraction status: `20` pages, `status: ok`, `text_char_count: 101293`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `bridge_core` | Keep. ELLMA-T is an educational social-VR interaction system, not social simulation. |
| `environment_side_representation` | `3D_engine` | Keep. The system is implemented in VRChat with embodied avatars and virtual worlds. |
| `agent_accessible_representation` | `L2` | Keep. The agent uses role-play scenario descriptions and conversational context, not object-level geometry or spatial topology. |
| `behavioral_scale` | `interaction` | Keep. The study concerns learner-agent conversation and role-play. |
| `evidence_status` | `designed_affordance_only` | Keep. The qualitative study reports user experience; it does not establish spatial representation as an isolated effect. |

## Evidence Notes

ELLMA-T is a GPT-4-based embodied conversational agent in VRChat designed to support English language learning. It assesses language level, generates role-play scenarios, conducts turn-taking role-play conversations, and provides feedback. The system uses VRChat, Unity/VRChat OSC integration, Quest 3 interaction, speech, avatar embodiment, and different virtual worlds such as indoor cafes and outdoor city settings.

The spatial role is primarily contextual. ELLMA-T can describe a scene, outline surroundings and significant objects, and place the learner-agent interaction in a corresponding VR environment. Participants reported value from contextualized learning, 3D interactivity, avatars, and immersive settings. However, the paper does not show the agent receiving live object coordinates, navigation graphs, raw visual observations, or direct geometry.

The row should therefore remain `L2`: a scene/contextual prompt and social-VR embodiment bridge case.

## Page/Section Anchors

- Abstract and Figure 1, pages 1-2: GPT-4 tutor in VRChat, role-play, and qualitative interviews with 12 participants.
- Section 3.2, pages 4-5: workflow, language assessment, role-play scenario generation, and feedback.
- Section 3.3, pages 5-6: VRChat, Quest 3, Unity/OSC, prompts, memory, and system architecture.
- Section 5, pages 8-12: participant perceptions of agent embodiment, situated learning, and contextualized role-play.
- Appendix A, pages 18-20: prompt templates for role-play and feedback.

## Claim Boundary

Allowed manuscript use:

- Use `TW-09` as a bridge example of LLM-agent interaction in social VR for education.
- Use it to discuss contextualized role-play and embodied presence.

Disallowed manuscript use:

- Do not treat it as a social simulation or multi-agent environment.
- Do not code it as `L5`; the agent does not receive raw embodied spatial observations.
- Do not overclaim object/location awareness beyond scenario and role-play context.

## Follow-Up

No acquisition action is needed. Current coding can remain `bridge_core / 3D_engine / L2 / interaction / designed_affordance_only`.
