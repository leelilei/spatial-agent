# HC02 Closure Card - Generative Agents

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `HC02`

Paper: Park et al. 2023, *Generative Agents: Interactive Simulacra of Human Behavior*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_core/01_Generative_Agents_Park2023.pdf`
- Markdown dossier: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/HC02_Generative_Agents_Interactive_Simulacra_of_Human_Behavior.md`
- Extraction status in dossier: `pypdf`, `22` pages, `status: ok`, `text_char_count: 130433`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `anchor_core` | Keep. This is a canonical LLM multi-agent social-simulation system with a spatial sandbox. |
| `environment_side_representation` | `2D_grid` | Keep. Smallville is a sprite-based sandbox town with areas, buildings, subareas, and objects. |
| `agent_accessible_representation` | `L3` | Keep. Agents receive local area/object/co-presence information and navigate to selected locations, but do not receive global configurational metrics or direct geometry. |
| `behavioral_scale` | `emergent_social_structure` | Keep. The paper reports information diffusion, relationship memory, and coordination among agents. |
| `evidence_status` | `designed_affordance_only` for spatial-effect claims | Keep. The paper reports social emergence, but it does not run matched spatial-representation/layout comparisons. It should not be used as evidence that spatial configuration affects social behavior. |

## Evidence Notes

The system instantiates `25` agents in the Smallville sandbox. The environment includes named areas such as houses, cafe, stores, park, school, dorm, and objects within subareas. This supports a spatially explicit environment-side code.

The LLM-facing interface is text-mediated. Agents output natural-language action descriptions, and the system translates selected actions into movement and object-state updates in the sandbox. The sandbox server maintains agent locations, current actions, interacted objects, and sends nearby agents/objects within a preset visual range to each agent. This supports `L3` local relational representation: local area, nearby objects, local co-presence, and movement targets.

The paper describes an environment tree: areas and objects are represented hierarchically, and agents maintain individual subgraphs that update as they navigate. The model selects suitable areas/subareas from this stored tree, after which game path algorithms animate movement. This is stronger than labels or pure semantic scene description, but it is still not `L4`: there is no agent-facing integration, depth, control, choice, global accessibility, or whole-layout position metric.

The paper reports emergent social behaviors, including information diffusion, relationship memory, and coordination around a party. These are valid social-simulation outcomes. However, they are not controlled spatial-effect evidence because the paper does not manipulate spatial representation levels or layout structure while holding social conditions fixed.

## Page/Section Anchors

Use these anchors for manuscript support:

- Section 3.1-3.2, pages 5-6: Smallville interaction, local awareness, environmental interaction, movement through places, object-state changes.
- Figure 2, page 5/6 area in extraction: town areas, subareas, and objects as a tree-like world description.
- Section 3.4, page 6 onward: emergent social behaviors.
- Section 5.1, page 12: sandbox server, JSON state, nearby agents/objects, environment tree, and text conversion.
- Section 7.1, page 15: descriptive emergent social behavior evaluation.

## Claim Boundary

Allowed manuscript use:

- Generative Agents is a strong anchor example of LLM agents situated in a spatial sandbox.
- It supports the claim that current systems can use local spatial context, co-presence, movement, and places as interaction scaffolds.
- It supports the evidence-map point that spatial worlds are common, but often agent-facing structure remains local/text-mediated.

Disallowed manuscript use:

- Do not claim this paper demonstrates configuration-mediated social behavior.
- Do not treat Smallville's environment tree as `L4`; the tree is used for area/object selection, not global configurational reasoning.
- Do not treat the emergent party or relationship formation as a spatial effect without controls.

## Follow-Up

No immediate acquisition action is needed. If the evidence table is later revised, `source_basis` can be upgraded from `local_pdf_and_reading_note` to `local_pdf_fulltext_closure_card`.

