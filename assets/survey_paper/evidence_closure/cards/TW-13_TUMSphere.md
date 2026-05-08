# TW-13 Closure Card - TUMSphere

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `TW-13`

Paper: Berrezueta-Guzman and Wagner 2026, *Next-Gen Orientation: Supporting International Students with Generative AI NPCs in VR*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_adjacent/14_TW-13_TUMSphere_Next_Gen_Orientation_2026.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_adjacent/14_TW-13_TUMSphere_Next_Gen_Orientation_2026.fulltext.md`
- Source note: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/TW-13.source.md`
- Extraction status: `21` pages, `status: ok`, `text_char_count: 95634`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `bridge_core` | Keep. TUMSphere is a VR campus-orientation and education system, not population social simulation. |
| `environment_side_representation` | `3D_engine` | Keep. The system is built in Unreal Engine 5 with a virtual campus, VR locomotion, object interaction, NPCs, and NavMesh. |
| `agent_accessible_representation` | `L5` | Keep cautiously. NPCs are connected to object/location awareness, proximity-based interaction, Actions API, spatial navigation, and NavMesh escort behavior in a 3D VR campus. |
| `behavioral_scale` | `interaction` | Keep. The behavior is student-NPC guidance, information retrieval, navigation, and role-play. |
| `evidence_status` | `observed_effect` | Keep. The mixed-methods user study reports usability, task success, latency, and participant preferences. |

## Evidence Notes

TUMSphere recreates a campus environment in Unreal Engine 5 with classrooms, laboratories, corridors, common areas, buildings, landscaping, locomotion, teleportation, object interaction, spatial navigation cues, and NPC guides. It integrates LLM-powered NPCs via Convai, including speech recognition, LLM dialogue, TTS, lip sync, facial animation, conversation history, RAG/knowledge-bank grounding, and Ready Player Me avatars.

The `L5` coding is justified by the environmental-awareness and navigation layer. The paper describes registering campus objects and locations with NPCs, assigning descriptive names and position references, using Convai's Actions API, enforcing proximity-based interaction through VR controller positions relative to NPCs, and using Unreal Engine's NavMesh to let NPCs guide students physically through the campus. Task B required participants to follow an NPC as it navigated the NavMesh to the library, with 100% completion.

The coding should remain cautious. The LLM dialogue layer itself is not shown to compute global spatial metrics or reason over Space Syntax. The L5 claim rests on embodied action in a 3D engine with object/location awareness and navigation behaviors, not on global configurational reasoning.

## Page/Section Anchors

- Abstract, page 1: embodied NPCs, real-time speech, context-aware dialogue, autonomous spatial navigation, and user study with 24 participants.
- Section 3.1, pages 4-6: TUMSphere virtual campus, VR locomotion, object interaction, spatial navigation, and educational objectives.
- Section 3.2-3.3, pages 6-8: LLM integration, Unreal Engine, Convai, speech, TTS, animation, and interaction pipeline.
- Section 4.4.2, page 11: environmental awareness, object registration, position references, interaction radius, Actions API, and NavMesh navigation.
- Section 5-6, pages 14-18: user study, task success, latency, usability, and participant preference for embodied navigation.
- Section 7.3 and 9.3, pages 18-19: embodiment, spatial agency, and future environmental awareness/persistence.

## Claim Boundary

Allowed manuscript use:

- Use `TW-13` as a strong bridge example of LLM NPCs coupled to spatial navigation and object/location awareness in a VR campus.
- Use it to discuss how LLM NPCs can become guides rather than only conversational kiosks when linked to NavMesh and game-engine actions.
- Use it as observed-effect evidence for VR orientation task completion and user preference for embodied guidance.

Disallowed manuscript use:

- Do not treat it as emergent social simulation.
- Do not claim Space Syntax or global configurational metrics.
- Do not imply the LLM alone has full geometric perception; the spatial agency comes from integration with Unreal/Convai object and navigation systems.

## Follow-Up

No acquisition action is needed. Current coding can remain `bridge_core / 3D_engine / L5 / interaction / observed_effect`.
