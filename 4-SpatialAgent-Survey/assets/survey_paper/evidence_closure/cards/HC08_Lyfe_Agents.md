# HC08 Closure Card - Lyfe Agents

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `HC08`

Paper: Zhao et al. 2023, *Lyfe Agents: Generative agents for low-cost real-time social interactions*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_core/09_HC08_Lyfe_Agents.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_core/09_HC08_Lyfe_Agents.fulltext.md`
- Markdown dossier: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/HC08_Lyfe_Agents_Generative_agents_for_low_cost_real_time_social_interactions.md`
- Extraction status: `pdfplumber`, `31` pages, `status: ok`, `text_char_count: 90354`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `anchor_core` | Keep. This is a multi-agent social interaction system in a custom 3D virtual world. |
| `environment_side_representation` | `3D_engine` | Keep. LyfeGame is built in Unity, with a 3D small-town environment, landmarks, virtual bodies, collision-free navigation, and proximity-mediated interaction. |
| `agent_accessible_representation` | `L3` | Keep. Agents receive language/observation streams, landmark/destination choices, arrival/vicinity feedback, and proximity-conditioned dialogue; the paper does not show raw geometry, pixel-space vision, coordinates, or global layout metrics being consumed by the LLM. |
| `behavioral_scale` | `interaction` | Keep. The main reported behavior is situated social interaction, information exchange, collaboration, and preference influence among a limited number of agents. |
| `evidence_status` | `designed_affordance_only` for spatial-effect claims | Keep. The paper reports social-scenario outcomes and architecture ablations, but it does not isolate spatial representation or layout as the causal factor. |

## Evidence Notes

Lyfe Agents is a stable anchor-core case because agents inhabit LyfeGame, a custom Unity-based 3D virtual environment. The SakuraMachi setting includes named landmarks such as a hotel, library, convenience store, and flower shop, and agents can navigate toward those landmarks with virtual bodies controlled by their artificial brains.

The strongest spatial evidence is local and interactional. Agents receive observations while living in the environment, especially conversations from nearby agents and human players. Dialogue is vicinity-based: an agent can only receive conversations from others in its vicinity, and the agent can talk so that nearby agents and users receive the utterance. Agents can also choose `move`, advancing toward a selected destination in the environment.

Appendix B confirms that the Unity side supports richer 3D capabilities, including vision, spatial awareness, body movement, object interaction, and collision-free navigation. However, for Lyfe Agents specifically, the system uses these capabilities mainly to support navigation, arrival feedback, and whether other agents are in the vicinity. The paper's own limitation section says interactions still rely heavily on natural language and that pixel-space vision and simulated robotic bodies have not yet been incorporated.

This is why the row remains `L3`, not `L5`. The environment is a 3D engine, but the agent-accessible representation is a prompt-mediated/local-observation interface: named locations, vicinity, group conversation state, and high-level move/talk actions. There is no evidence of direct coordinate streams, depth, egocentric image input, metric geometry, or global configurational layout measures entering the LLM decision loop.

The social-behavior evidence is real but not spatial-effect evidence. The paper evaluates murder mystery, activity fair, and patient-help scenarios. Agents exchange information, update opinions, form groups, meet near locations, and influence preferences through conversations. Ablations test option-action selection, self-monitoring, and Summarize-and-Forget memory. These support the social-interaction anchor role, but the ablations are architectural rather than spatial/layout manipulations.

## Page/Section Anchors

Use these anchors for manuscript support:

- Abstract and Figure 1, page 1: LyfeGame 3D virtual environment and multi-agent collaboration in a murder-mystery scenario.
- Section 3, pages 4-5: custom LyfeGame/Unity environment, SakuraMachi landmarks, virtual bodies, observations, vicinity-based conversation, and move/talk actions.
- Section 4, pages 5-9: murder mystery, information exchange, opinion change, activity fair, and patient-help scenario evaluations.
- Section 6, pages 9-10: limitation that interactions rely heavily on natural language and that pixel-space vision/simulated robotic bodies are not yet incorporated.
- Appendix B, pages 16-17: LyfeGame architecture, Unity and Python brain wrapper, collision-free navigation, arrival/vicinity feedback, move/talk action set, spontaneous navigation, group formation, and meeting near locations.
- Appendix E, pages 20-21: architecture ablations for option-action, self-monitoring, and memory.

## Claim Boundary

Allowed manuscript use:

- Lyfe Agents is a strong anchor example of real-time multi-agent social interaction in a 3D virtual environment.
- It supports the claim that current LLM agents can use local place, proximity, movement destination, and co-present conversation as social-interaction scaffolds.
- It is useful for showing why environment-side richness and agent-accessible representation must be coded separately.

Disallowed manuscript use:

- Do not code Lyfe Agents as `L5`; Unity supports richer embodied capabilities, but the paper does not show those capabilities entering the LLM as raw geometry, images, coordinates, or embodied sensor streams.
- Do not claim the paper demonstrates spatial-configuration effects on social behavior.
- Do not treat murder mystery success or activity-fair influence as evidence that layout or spatial representation caused the outcome.
- Do not mix the Unity backend with agent-facing Space Syntax or global configurational metrics.

## Follow-Up

No acquisition action is needed. Current coding can remain `anchor_core / 3D_engine / L3 / interaction / designed_affordance_only`. If the evidence table later separates social-outcome evidence from spatial-effect evidence, note that Lyfe Agents reports observed social-scenario outcomes but only designed affordances for spatial-representation claims.
