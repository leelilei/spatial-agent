# R3-01 Closure Card - MineLand

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `R3-01`

Paper: Yu et al. 2024, *MineLand: Simulating Large-Scale Multi-Agent Interactions with Limited Multimodal Senses and Physical Needs*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_round3_candidates/R3-01_MineLand_2024.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_round3_candidates/R3-01_MineLand_2024.fulltext.md`
- Markdown dossier: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/R3-01_MineLand_Simulating_Large_Scale_Multi_Agent_Interactions_with_Limited_Multimodal.md`
- Extraction status: `pdfplumber`, `33` pages, `status: ok`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `anchor_core` | Keep. MineLand is a large-scale multi-agent simulator for embodied Minecraft agents with cooperation, competition, communication, and social experiments. |
| `environment_side_representation` | `3D_engine` | Keep. The system is built on Minecraft and exposes block-based 3D open-world environments, physical needs, inventory, objects, and multi-agent interaction. |
| `agent_accessible_representation` | `L5` | Keep. Agents receive first-person RGB video plus tactile/block, auditory, event, and limited-sense observations; the paper also evaluates vision versus no-vision settings. |
| `behavioral_scale` | `mixed` | Keep. The paper includes task execution, resource gathering, cooperation, competition, communication, conformity, personality traits, and large-scale multi-agent behavior. |
| `evidence_status` | `observed_effect` | Keep. The paper reports performance comparisons, cooperation differences, vision ablation, personality/conformity experiments, and scalability experiments. |

## Evidence Notes

MineLand is one of the clearest anchor-core `L5` cases. The simulator provides tactile information about blocks surrounding the agent, auditory information, and first-person RGB video. The authors explicitly describe these as raw perceptual information and impose human-like limitations on visual and auditory perception, including distance attenuation, environmental obstruction, and directional constraints.

The agent-accessible interface is therefore embodied and multimodal, not merely symbolic. Agents interact with a Minecraft world using low-level actions such as walking, running, jumping, and object interaction, plus high-level code-based actions. They also have physical needs such as oxygen, hunger, health, inventory, equipment, and satiety, which ground behavior in survival and daily-life rhythms.

The spatial/social coupling is also explicit. Communication is distance-constrained through chat, auditory information, and body language; messages can interrupt ongoing long-horizon action execution. Cooperation and competition tasks show different planning and communication costs. Appendix experiments show conformity and personality-trait effects with more than 10 agents and up to 48 agents.

Observed-effect status is supported by multiple tests. The vision-enhanced MineLand condition outperforms the no-vision condition in the ocean-finding task, with higher success rate and shorter completion time. Cooperation/personality conditions affect whether agents collaborate. Large-scale experiments show the simulator can support 64 or more agents, and specific social experiments report conformity and cooperation tendencies.

## Page/Section Anchors

Use these anchors for manuscript support:

- Abstract and Introduction, pages 1-3: large-scale Minecraft simulator with limited multimodal senses and physical needs.
- Section 2.2, page 4: tactile/block, auditory, and first-person RGB video observations as raw perceptual information.
- Section 2.3, page 4: physical needs such as oxygen and hunger.
- Section 2.4-2.5, pages 4-5: low/high-level action space, distance-constrained communication, auditory/body-language/text communication, and interrupt mechanism.
- Section 5.2, pages 8-9: cooperation/competition and personality effects in multi-agent tasks.
- Appendix H, pages 22-23: vision versus no-vision comparison for finding the ocean.
- Appendix O, pages 27-28: conformity and personality-trait experiments with multi-agent groups.

## Claim Boundary

Allowed manuscript use:

- MineLand is a strong `L5` example of embodied, first-person, multimodal, limited-sense agent access in a 3D game world.
- It supports observed-effect claims for vision, limited senses, communication, cooperation, personality, and social-experiment outcomes.
- It is useful for contrasting embodied spatial/social agent platforms with text-only or graph/place-level social simulations.

Disallowed manuscript use:

- Do not treat MineLand as evidence for Space Syntax or global configurational reasoning.
- Do not claim agents receive global layout metrics or complete world maps; limited perception is central to the design.
- Do not generalize Minecraft/block-world findings directly to real built environments without noting the simulator boundary.
- Do not collapse its embodied sensory interface into `L3` simply because high-level code actions are also supported.

## Follow-Up

No acquisition action is needed. Current coding can remain `anchor_core / 3D_engine / L5 / mixed / observed_effect`.
