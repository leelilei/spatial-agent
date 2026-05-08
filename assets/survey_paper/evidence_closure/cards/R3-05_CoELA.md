# R3-05 Closure Card - CoELA

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `R3-05`

Paper: Zhang et al. 2024, *Building Cooperative Embodied Agents Modularly with Large Language Models*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_round3_candidates/R3-05_CoELA_2024.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_round3_candidates/R3-05_CoELA_2024.fulltext.md`
- Source note: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/R3-05.source.md`
- Extraction status: `29` pages, `status: ok`, `text_char_count: 84497`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `bridge_core` | Keep. CoELA is primarily a cooperative embodied-agent benchmark/framework rather than a broad social-simulation study. |
| `environment_side_representation` | `3D_engine` | Keep. The evaluated environments include TDW-MAT and Communicative Watch-And-Help/VirtualHome-Social. |
| `agent_accessible_representation` | `L5` | Keep. Agents receive egocentric RGB-D, position/rotation, object states, local maps, and messages in embodied 3D tasks. |
| `behavioral_scale` | `interaction` | Keep. The focus is two-agent cooperation and human-agent collaboration. |
| `evidence_status` | `observed_effect` | Keep. The paper reports quantitative benchmark results, ablations, qualitative analyses, and a human-agent user study. |

## Evidence Notes

CoELA addresses decentralized multi-agent cooperation with raw sensory observations, costly communication, partial observation, and long-horizon multi-objective embodied tasks. The architecture includes perception, memory, communication, planning, and execution modules.

The `L5` evidence is strong. TDW-MAT provides egocentric RGB-D observations, agent position and rotation, messages, navigation controls, interaction actions, and object/container manipulation. The perception module builds 3D point clouds and local occupancy or semantic maps from RGB-D. C-WAH supports symbolic and visual observations; in visual mode agents receive egocentric RGB/depth plus agent position and messages.

Observed-effect status is supported by results on TDW-MAT and C-WAH, efficiency improvements when cooperating with CoELA, ablations of communication/memory/planning modules, and a human-agent study showing trust and cooperation differences. The paper itself notes a limitation: CoELA does not fully exploit all 3D spatial information in current LLM reasoning, so manuscript claims should separate embodied access from proven spatial reasoning.

## Page/Section Anchors

- Abstract and Introduction, pages 1-4: decentralized control, raw sensory observations, costly communication, and embodied cooperation.
- Section 4, pages 4-6: CoELA architecture with perception, memory, communication, planning, and execution.
- Section 5, pages 6-10: TDW-MAT and C-WAH environments, metrics, baselines, and results.
- Section 5.3.2, pages 10-11: human-agent collaboration user study and trust/cooperation findings.
- Appendix A-B, pages 17-22: observation spaces, RGB-D, semantic maps, object states, agent position, action spaces, and messages.
- Limitations, page 11: limited use of 3D spatial information by current LLMs.

## Claim Boundary

Allowed manuscript use:

- Use `R3-05` as a strong `3D_engine / L5` bridge example for embodied cooperative agents.
- Use it to show that multimodal embodied access and natural-language communication can be combined in multi-agent tasks.
- Use it as observed-effect evidence for cooperation benchmark outcomes.

Disallowed manuscript use:

- Do not present CoELA as population-scale social simulation.
- Do not claim it demonstrates built-environment or Space Syntax effects.
- Do not conflate embodied sensory access with fully solved 3D spatial reasoning; the authors identify this as a limitation.

## Follow-Up

No acquisition action is needed. Current coding can remain `bridge_core / 3D_engine / L5 / interaction / observed_effect`.
