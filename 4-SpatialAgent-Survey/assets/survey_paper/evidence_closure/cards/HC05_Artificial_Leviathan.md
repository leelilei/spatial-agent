# HC05 Closure Card - Artificial Leviathan

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `HC05`

Paper: Dai et al. 2024, *Artificial Leviathan: Exploring Social Evolution of LLM Agents Through the Lens of Hobbesian Social Contract Theory*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_core/04_Artificial_Leviathan_Dai2024.pdf`
- Markdown dossier: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/HC05_Artificial_Leviathan_Exploring_Social_Evolution_of_LLM_Agents_Through_the_Lens_o.md`
- Extraction status in dossier: `pypdf`, `16` pages, `status: ok`, `text_char_count: 75091`

## Coding Decision

| Field | Current decision | Closure assessment |
|---|---|---|
| `core_layer` | `anchor_core` | Keep only if the review treats abstract resource worlds as sufficient spatial environments. Otherwise this is a candidate for boundary discussion. |
| `environment_side_representation` | `text-only` | Keep. The world is a prompt-defined resource setting, not a grid, map, graph, or geometry. |
| `agent_accessible_representation` | `L3` | Revise or flag. Full-text evidence supports `L2` more than `L3`: agents receive a semantic resource-world description, agent names, resource quantities, memories, and action options, but not adjacency, local co-presence, nearby-agent state, local movement options, or topology. |
| `behavioral_scale` | `emergent_social_structure` | Keep. The paper studies conflict, concession, commonwealth formation, and social contracts. |
| `evidence_status` | `designed_affordance_only` for spatial-effect claims | Keep. The paper reports social evolution, but it does not test spatial representation or spatial configuration effects. |

## Evidence Notes

The paper instantiates agents in a resource-constrained natural world with food and arable land. Agents make choices such as farming, trading, robbing, conceding, and donating. They have traits, memories, resources, and knowledge of other agents. The experiments examine whether a society transitions from conflict to a commonwealth-like structure.

The spatial evidence is weak. The prompt includes a world description and farming land, but it does not expose locations, adjacency, distances, neighborhoods, movement, co-presence, or local perceptual range. Agents appear to be able to target other agents through action choices rather than through spatial proximity or movement. The resource environment is meaningful for social evolution, but it is not an `L3` local-relational spatial interface.

The current `L3` coding likely overstates the spatial representation. A safer coding is `L2`: semantic/resource-world description without explicit topology. An even stricter interpretation could treat the case as a weak spatial-environment boundary because the "world" is mainly a resource/game-theoretic setting. If retained in Core, the manuscript should not use it to support claims about local spatial relations.

The paper reports observed social outcomes under agent/system parameter changes, including conflict, concession, commonwealth formation, and changes in peaceful interactions. These are not observed spatial effects. The independent variables are psychological, memory, population, common-power, intelligence, and resource/system parameters rather than spatial layout or representation levels.

## Page/Section Anchors

Use these anchors for manuscript support:

- Section 3.1, page 4: natural world with food/arable land, limited transparency, initial resources.
- Section 3.3, pages 5-6: action set: farm, rob, trade, donate.
- Section 4.1 and Appendix A, pages 7 and 15: prompt includes general world description, agent/resource information, memory, and action rules.
- Section 5 and 5.1, pages 8-9: transition from state of nature to commonwealth and baseline outcome analysis.
- Section 6-7, pages 9-11: experiments manipulate agent/system parameters and report social evolution outcomes.

## Claim Boundary

Allowed manuscript use:

- Artificial Leviathan can be cited as an LLM-agent social simulation with an abstract resource-world setting.
- It supports discussion of emergent social structure in prompt-defined environments.
- It is useful as a cautionary example: social emergence can be reported without a strong spatial interface.

Disallowed manuscript use:

- Do not use this row as evidence that `L3` local spatial relations are common unless the row is recoded or explicitly qualified.
- Do not claim it exposes adjacency, co-presence, movement options, or local topology.
- Do not claim it supports spatial configuration, Space Syntax, or layout-mediated social behavior.
- Do not treat resource scarcity as spatial configuration.

## Follow-Up

Recommended table action: recode `agent_accessible_representation` from `L3` to `L2`, or move the row into a boundary/weak-spatial note if the review tightens the Core inclusion rule. This change would affect representation counts and any manuscript sentence using the `L3 = 18` baseline.

