# HC11 Closure Card - Environment-Aware VR Role-Play

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `HC11`

Paper: Li et al. 2025, *Exploring Large Language Model-Driven Agents for Environment-Aware Spatial Interactions and Conversations in Virtual Reality Role-Play Scenarios*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_adjacent/17_HC11_Environment_Aware_VR_Roleplay_2025.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_adjacent/17_HC11_Environment_Aware_VR_Roleplay_2025.fulltext.md`
- Source note: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/HC11.source.md`
- Extraction status: `39` pages, `status: ok`, `text_char_count: 117089`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `bridge_core` | Keep. The work studies human-agent VR role-play rather than population-level or multi-agent social simulation. |
| `environment_side_representation` | `3D_engine` | Keep. The prototype is implemented in Unity/VR with objects, characters, spots, animations, and NavMesh movement. |
| `agent_accessible_representation` | `L2` | Keep. The agent receives a structured text prompt schema about scene entities and interactions; coordinate-bearing fields exist, but the LLM interface is still scene/object text rather than embodied perception or global topology. |
| `behavioral_scale` | `interaction` | Keep. The evidence concerns dyadic or small-group role-play interactions. |
| `evidence_status` | `designed_affordance_only` | Keep. The user study evaluates feasibility and experience, but it does not isolate spatial representation as a causal factor. |

## Evidence Notes

The paper defines a prompt schema for VR role-play agents with five major components: system context, objects, characters, spots, and communication. The schema provides object names, descriptions, grabbability, container relations, positions and directions; character state includes position, direction, and hand state; spots encode action-relevant positions and directions; communication logs capture user actions and dialogue.

The prototype runs as a customizable Unity plugin. The environment and interaction layer translate player movement, pointing, grabbing, releasing, and conversation into textual context for the LLM. Agent responses can call functions for movements, object interactions, and dialogue, which Unity validates before animation execution. The paper also reports five VR role-play scenarios and a study with 14 participants.

The conservative `L2` decision is important. Although the context prompt can include x/y/z positions and object directions, the paper's own framing emphasizes text prompts as a way to convey VR environment and interaction cues. The LLM does not receive raw egocentric RGB/depth, meshes, point clouds, or a global layout/topology representation. It is therefore a strong bridge example of scene-aware interaction, not an anchor example of embodied geometry.

## Page/Section Anchors

- Figure 1 and Section 3.1, pages 1-3: prompt-schema architecture with system context, objects, characters, spots, and communication.
- Section 3.2-3.3, pages 3-4: Unity plugin, object metadata, function calls, validation, and agent interaction flow.
- Section 3.5-3.6, pages 4-6: role-play scenarios and object/spot interaction examples.
- Methodology and results, pages 6-8: 14-participant study and findings on localization/reasoning.
- Appendix C-D, pages 12-39: prompt examples with positions, directions, object lists, character lists, and player movement/action logs.

## Claim Boundary

Allowed manuscript use:

- Use `HC11` as a bridge example of LLM agents receiving structured VR scene and interaction context through text prompts.
- Use it to show that current VR role-play systems can expose local object, character, spot, and action cues to LLM agents.
- Use it as evidence for `3D_engine / L2` bridge coverage.

Disallowed manuscript use:

- Do not claim `HC11` is population social simulation.
- Do not code it as `L5`; coordinates inside a text schema are not equivalent to embodied sensory access.
- Do not claim it demonstrates Space Syntax, global configurational reasoning, or spatial-structure causal effects.

## Follow-Up

No acquisition action is needed. Current coding can remain `bridge_core / 3D_engine / L2 / interaction / designed_affordance_only`.
