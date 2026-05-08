# HC04 Closure Card - Affordable Generative Agents

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `HC04`

Paper: Yu et al. 2024, *Affordable Generative Agents*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_core/02_Affordable_Generative_Agents_Yu2024.pdf`
- Markdown dossier: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/HC04_Affordable_Generative_Agents.md`
- Extraction status in dossier: `pypdf`, `29` pages, `status: ok`, `text_char_count: 94543`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `anchor_core` | Keep. The paper directly extends LLM generative-agent social simulation and tests multi-agent town settings. |
| `environment_side_representation` | `2D_grid` for the social-simulation row | Keep with caveat. The paper also includes VirtualHome, but the multi-agent social evidence used here is the Generative Agents town setting. |
| `agent_accessible_representation` | `L3` | Keep. The relevant social-simulation setting uses Perceive/Act over surrounding objects, locations, and inter-agent interaction, not global configurational metrics or direct geometry. |
| `behavioral_scale` | `mixed` | Keep. The paper covers agent-environment activities and inter-agent dialogue/social relationships. |
| `evidence_status` | `designed_affordance_only` for spatial-effect claims | Keep. The paper reports social outcomes and cost/performance comparisons, but not matched spatial-representation or layout effects. |

## Evidence Notes

The paper's main contribution is cost reduction for believable LLM-agent interaction. It optimizes two interaction modes: agent-environment interaction through a Lifestyle Policy and inter-agent interaction through Social Memory. This is relevant to social simulation, but it is not a new spatial representation method.

For the multi-agent social-simulation evidence, the paper evaluates on the Generative Agents environment. It explicitly describes the simulated town, daily schedules, natural-language interaction, sprites/emojis, perception of surrounding game objects, and an Act module that selects locations and objects of interaction. This supports `L3`: local environment/object/location interaction is available to agents.

The paper also evaluates VirtualHome, a 3D domestic environment with objects, item states, and programmatic actions. That part is useful as an embodied/household task comparison, but it should not upgrade this Core social-simulation row to `L5`. The social multi-agent evidence used by this review comes from the Generative Agents town environment, not from a multi-agent VirtualHome social setting.

The paper reports information diffusion, party awareness, mayoral-candidacy awareness, and relationship evolution. These are valid social-simulation outcomes. However, they are not spatial-effect outcomes because the study does not manipulate spatial representation, local versus global layout information, or spatial configuration under matched controls.

## Page/Section Anchors

Use these anchors for manuscript support:

- Section 3, pages 3-5: method framing around agent-environment and inter-agent interaction.
- Section 4.1, page 6: evaluation environments, including Generative Agents town and VirtualHome.
- Section 4.3, pages 7-8: evaluation protocol, including relationship evolution and behavioral assessment.
- Section 5.1, pages 7-10: Generative Agents results, information diffusion, relationship evolution.
- Appendix E, pages 26-27: VirtualHome implementation; use only as a caveat, not as the main social-simulation coding basis.

## Claim Boundary

Allowed manuscript use:

- AGA supports the claim that current LLM-agent social simulation often uses local town/object/social interaction scaffolds inherited from Generative Agents.
- It can be used as a cost/performance extension of Generative Agents with multi-agent social behavior measurements.
- It supports the point that observed social outcomes can exist without controlled spatial-representation evidence.

Disallowed manuscript use:

- Do not treat AGA as introducing configurational spatial input.
- Do not use its VirtualHome component to reclassify the social-simulation row as `L5`.
- Do not claim AGA demonstrates that spatial configuration shapes social behavior.
- Do not treat information diffusion or relationship evolution as spatial mediation.

## Follow-Up

No acquisition action is needed. If the evidence table is later revised, consider adding a note that the row intentionally codes the Generative Agents social-simulation setting rather than the separate VirtualHome household-task setting.

