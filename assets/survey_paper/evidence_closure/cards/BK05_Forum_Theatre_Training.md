# BK05 Closure Card - Forum-Theatre VR Training

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `BK05`

Paper: Otofa et al., *Mixed-Initiative Dialogue Management for Human-Virtual Agents Interaction in Forum Theatre Inspired Training*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_adjacent/08_BK05_Forum_Theatre_Training.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_adjacent/08_BK05_Forum_Theatre_Training.fulltext.md`
- Extraction status: `5` pages, `status: ok`, `text_char_count: 16726`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `bridge_core` | Keep. The paper presents a VR training dialogue system, not a social-simulation framework. |
| `environment_side_representation` | `3D_engine` | Keep. The training system is implemented in a VR platform with virtual actors and replayed scenes. |
| `agent_accessible_representation` | `L2` | Keep. The LLM-driven component uses dialogue state and scripted scene context rather than spatial topology or embodied sensory streams. |
| `behavioral_scale` | `interaction` | Keep. The behavior is user-virtual-agent training dialogue and reflection. |
| `evidence_status` | `designed_affordance_only` | Keep. The paper describes system design and potential, with limited evaluation detail in the archived text. |

## Evidence Notes

The system adapts forum theatre for VR discrimination-awareness training. A user first observes a simulated discriminatory scene enacted by virtual characters, then discusses problematic behaviors with a virtual character, and can later replay or confront the same scene. The dialogue architecture combines state-based control with LLM-driven open dialogue, text-to-speech, a Unity VR environment, a VR animation manager, and scripted VR sequences.

The dialogue controller maintains dialogue history, stage goals, labels for discussed discriminatory situations, and recovery mechanisms for sensitive inputs. This supports the bridge row as an LLM-based human-agent interaction system in VR. It does not support a higher spatial coding because the LLM-facing state is dialogue/training state, not geometry or a structured spatial model.

## Page/Section Anchors

- Abstract and Section 2, pages 1-2: VR forum-theatre training purpose and discrimination-awareness scenario.
- Section 4, pages 2-4: mixed-initiative dialogue architecture, state-based control, LLM-driven open dialogue, and VR animation integration.
- Section 4.2, pages 3-4: dialogue state, scripted dialogue router, and scene replay/confrontation stages.
- Discussion, page 4: training potential and future evaluation direction.

## Claim Boundary

Allowed manuscript use:

- Use `BK05` as a bridge example of LLM dialogue management in a VR social-training environment.
- Use it to show that VR LLM-agent systems often rely on scripted training states plus open dialogue.

Disallowed manuscript use:

- Do not use it as evidence of emergent social structure or population simulation.
- Do not code it as `L3`, `L4`, or `L5`; the paper does not expose agent-facing spatial structure at those levels.
- Do not overstate evaluation strength; keep it as design evidence.

## Follow-Up

No acquisition action is needed. Current coding can remain `bridge_core / 3D_engine / L2 / interaction / designed_affordance_only`.
