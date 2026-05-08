# TW-12 Closure Card - Virtual Tutoring System

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `TW-12`

Paper: *A Virtual Tutoring System with Gamification, LLM-Guided NPCs, and Online Tutor Support*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_adjacent/13_TW-12_Virtual_Tutoring_System_2026.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_adjacent/13_TW-12_Virtual_Tutoring_System_2026.fulltext.md`
- Source note: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/TW-12.source.md`
- Extraction status: `31` pages, `status: ok`, `text_char_count: 89719`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `bridge_core` | Keep. The system is an educational virtual-world tutoring platform, not social simulation. |
| `environment_side_representation` | `3D_engine` | Keep. The system is built in Unity as a 3D virtual world with rooms, avatars, NPCs, quizzes, and gamification. |
| `agent_accessible_representation` | `L2` | Keep. LLM-NPCs support free-form educational dialogue in situated rooms, but no topology, coordinates, or embodied sensory stream is shown as agent input. |
| `behavioral_scale` | `interaction` | Keep. The evidence concerns learner-NPC and learner-tutor interaction. |
| `evidence_status` | `observed_effect` | Keep. Two evaluations report usage, helpfulness, interest, friendliness, learning support, and tutor intervention findings. |

## Evidence Notes

The paper presents a Unity-based virtual tutoring system with gamification, script-based NPCs, LLM-NPCs, a backend API, database, WebSocket monitoring, and tutor dashboard. The virtual world includes five consecutive rooms with panels, quizzes, scoring, and NPCs. Learners approach NPCs to trigger interactions; script NPCs expose predefined Q&A, while LLM-NPCs allow free-form dialogue via ChatGPT through the backend.

The system records learner interactions, time spent at NPCs, quiz progress, and tutor alerts. Tutors can inspect learner state, request screenshots, and provide contextual hints. The evaluations include an early experiment with 34 participants and a late experiment with 30 participants. Results show strong perceived interest and friendliness for LLM-NPCs, with gamification features also important.

The row remains `L2` because spatial context is the situated room/task structure and proximity-triggered interaction. The LLM-NPC prompt and backend are not shown to expose spatial coordinates, navigation topology, global layouts, or raw visual state to the model.

## Page/Section Anchors

- Abstract and Introduction, pages 1-4: system goals, Unity virtual world, LLM-NPCs, gamification, and tutor support.
- Section 4.2, pages 9-11: architecture, Unity environment, backend, database, OpenAI/ChatGPT proxy, and WebSocket monitoring.
- Section 5.1-5.3, pages 13-16: rooms, NPC interaction design, script NPCs, LLM-NPCs, and tutor support.
- Section 6.1, pages 17-19: early evaluation with 34 participants.
- Section 6.2, pages 19-23: late evaluation with 30 participants and tutor intervention results.

## Claim Boundary

Allowed manuscript use:

- Use `TW-12` as a bridge example of LLM-guided NPCs in a Unity educational virtual world.
- Use it as observed-effect evidence for user perception of LLM-NPCs versus script NPCs.

Disallowed manuscript use:

- Do not use it as evidence of emergent social structure.
- Do not code it as `L3` or higher unless new evidence shows agent-facing spatial representation beyond situated interaction triggers.
- Do not treat tutor-dashboard monitoring as LLM agent spatial perception.

## Follow-Up

No acquisition action is needed. Current coding can remain `bridge_core / 3D_engine / L2 / interaction / observed_effect`.
