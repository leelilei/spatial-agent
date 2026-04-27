# Phase 1 Targeted Widened Screen Round

Date: 2026-04-27

Purpose: increase the screened surface after the widened-Core decision without launching a new broad search or flattening `anchor_core` and `bridge_core`.

## Inputs

This round combines two sources:

1. Existing-pool rescreen:
   - source: `assets/survey_paper/phase1/phase1_abstract_rereview_round1_2026-04-13.csv`
   - output: `assets/survey_paper/phase1/phase1_existing_pool_widened_rescreen_candidates_2026-04-27.csv`
2. External targeted screen:
   - output: `assets/survey_paper/phase1/phase1_targeted_widened_screen_candidates_2026-04-27.csv`

## Search/Rescreen Families

The round used six target families:

| Family | Purpose |
|---|---|
| `social_vr_metaverse_avatar` | recover L2/L5 bridge cases in VR, metaverse, avatar-agent, and role-play settings |
| `online_community_network` | recover digital-community and social-network bridge cases |
| `game_npc_social_world` | recover NPC, game, sandbox, and virtual-world social interaction cases |
| `urban_mobility_crowd_built` | recover urban, crowd, evacuation, and built-environment cases |
| `embodied_3d_cooperation` | recover 3D embodied cooperation or collaboration cases |
| `l4_graph_topology` | specifically target agent-facing global abstract structure: graph, centrality, community, topology, accessibility |

## Existing-Pool Rescreen Outcome

The existing-pool rescreen found `84` candidate rows for manual recheck:

- `77` high-priority keyword matches
- `7` medium-priority keyword matches

Important caveat:

Many of these will remain `Adjacent` or `Foundational`. The rescreen is deliberately broad because its goal is not immediate admission, but to ensure the widened boundary does not miss plausible bridge cases already present in the local pool.

The most useful existing-pool categories are:

- LLM/game/sandbox systems that may have been excluded under the old narrow Core rule;
- urban/crowd/built-environment items that may support bridge or foundational contrast;
- graph/topology items that may help L4 boundary checking;
- VR/NPC/avatar items, if any are present in the old pool.

The least useful categories are:

- generic spatial-reasoning benchmarks without social behavior;
- classical Space Syntax or ABM papers without LLM agents;
- geospatial reasoning systems without multi-agent or social interaction.

## External Targeted Screen Outcome

The external targeted screen added `15` rows:

| Decision bucket | Count |
|---|---:|
| `already_admitted` | 4 |
| `already_in_local_queue` | 2 |
| `fulltext_recheck` | 4 |
| `reserve_recheck` | 3 |
| `reserve_or_adjacent` | 1 |
| `exclude_or_foundational` | 1 |
| **Total** | **15** |

Target-family distribution:

| Target family | Count |
|---|---:|
| `social_vr_metaverse_avatar` | 7 |
| `urban_mobility_crowd_built` | 4 |
| `game_npc_social_world` | 2 |
| `l4_graph_topology` | 2 |
| **Total** | **15** |

## Combined Screen Surface

This round increases the screened surface by:

- `84` existing-pool rescreen rows;
- `15` external targeted rows;
- `99` total rows requiring either quick exclusion or targeted full-text recheck.

This meets the intended target of expanding the screened surface by roughly `80-120` items without doing a new broad search.

## Immediate Full-Text Recheck Queue

Prioritize these external targeted rows:

| ID | Title | Reason |
|---|---|---|
| `TW-04` | Generative agents for urban mobility: A cognitive framework for realistic travel behavior simulation | possible urban/mobility bridge row; may improve L3/L4 boundary evidence |
| `TW-09` | ELLMA-T: an Embodied LLM-agent for Supporting English Language Learning in Social VR | possible social-VR L2/L5 bridge row |
| `TW-11` | Dialogs with GenAI NPCs: Exploring Player Interactions with Speech Agents in a VR Game | promising NPC/VR social interaction bridge case |
| `TW-13` | Next-Gen orientation: supporting international students with generative AI NPCs in VR | promising VR/NPC/campus-orientation bridge case |

Secondary reserve recheck:

| ID | Title | Reason |
|---|---|---|
| `TW-02` | CiteAgent / citation-network simulations | possible L4 but farther from spatial-social target |
| `TW-10` | Conversing with AI agents in VR | likely social VR but spatial input may be weak |
| `TW-12` | Virtual Tutoring System with LLM-Guided NPCs | possible NPC bridge, but educational setting may be weakly social-spatial |

Do not duplicate work:

- `TW-05` and `TW-06` correspond to local `HC13` and `HC14`.
- `TW-01`, `TW-03`, `TW-07`, and `TW-08` are already admitted or counted in the widened evidence map.

## Expected Yield

Conservative expectation:

- full-text recheck queue: `4` primary + `3` reserve;
- likely new widened-Core rows: `2-4`;
- possible final widened-Core size after this round: `33-35` rows.

Optimistic expectation:

- if the VR/NPC cases expose agent-facing spatial context clearly, widened Core may reach `35-37` rows;
- L2 may increase from `5` to `7-8`;
- L5 may increase by `1-2` if embodied VR geometry is directly agent-facing;
- L4 is unlikely to increase substantially unless `TW-02` or `TW-04` exposes agent-facing global network/route structure.

## Decision

Do not run a new broad screen.

Proceed with:

1. quick manual triage of the `84` existing-pool rescreen rows;
2. full-text recheck of `TW-04`, `TW-09`, `TW-11`, and `TW-13`;
3. reserve recheck of `TW-02`, `TW-10`, and `TW-12` only if primary yield is low;
4. update the widened evidence map only after full-text support is checked.

