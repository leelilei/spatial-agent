# Phase 1 Widened Core Recheck Results

Date: 2026-04-27

Purpose: close the first local widened-Core recheck pass after the `anchor_core + bridge_core` boundary change.

## Result Summary

All five `quick_recheck` cases are now accepted as `bridge_core`.

`BK07` and `BK08` are accepted as `bridge_core`, but neither should be coded as `L4` under the current evidence.

Updated paper-level count:

- strict `anchor_core`: `17`
- widened Core after local bridge reclassification: `28`
- reserve not counted: `LD01`

Updated row-level count:

- strict `anchor_core`: `19`
- widened Core after local bridge reclassification: `30`

## BK07 / BK08 L4 Recheck

### BK07 S3

Decision:

- `bridge_core`
- `agent_accessible_representation = L3`

Source basis:

- local PDF: `assets/survey_paper/pdfs/phase1_adjacent/10_BK07_S3_Social_Network_Simulation.pdf`
- ar5iv/arXiv full text: `https://ar5iv.org/pdf/2307.14984.pdf`

Reasoning:

- The system constructs a directed social network from real social-media data.
- Agents perceive an informational environment through content from users they follow.
- The paper describes user profiles, memory pools, messages, follow relations, followers/followees, and propagation between source and target nodes.
- The paper discusses indegree/outdegree and influential users at the environment/model level.
- However, the recheck did not find evidence that agents receive a global abstract network summary such as centrality, community structure, global accessibility, or whole-network position as part of their prompt/state.

Conclusion:

- This is local/relational graph exposure rather than agent-facing global abstract structure.
- Code as `L3`, not `L4`.

### BK08 Online Community Collective Behaviors

Decision:

- `bridge_core`
- `agent_accessible_representation = L3`

Source basis:

- ScienceDirect open-access page: `https://www.sciencedirect.com/science/article/pii/S2543925125000154`

Reasoning:

- The study examines LLM-based autonomous agents in Chirper, an online community inhabited by AI agents.
- The page confirms profiles, posts, follows/replies/interaction networks through the article framing and abstract-level evidence.
- The reported network structures, centralization, homophily, power-law degree distributions, and small-world comparison are analysis outputs.
- The current source basis does not show that global network metrics are given to agents as agent-facing state.

Conclusion:

- The operative environment is a structured interaction graph/community.
- The global network metrics are researcher-side social network analysis.
- Code as `L3`, not `L4`.

## L2 Quick-Recheck Results

### HC11 VR Role-Play

Decision:

- `bridge_core`
- `agent_accessible_representation = L2`

Source basis:

- IEEE DOI record / public abstract: `10.1109/VR59515.2025.00025`
- ResearchGate full-text preview

Reasoning:

- The system uses a schema describing VR environments and interactions through text prompts.
- The public source identifies components such as spots, objects, characters, and communications across five role-play scenarios.
- Evaluation involves `14` participants.
- This is socially situated VR human-AI interaction, not full social simulation.

### BK02 Spatially Aware LLM Agents

Decision:

- `bridge_core`
- `agent_accessible_representation = L2`
- `evidence_status = observed_effect`

Source basis:

- PubMed/lifescience abstract page
- local note already reviewed in the earlier sanity check

Reasoning:

- The study compares spatial-awareness conditions in counseling conversations.
- Reported outcomes include copresence, trust, therapeutic alliance, and self-disclosure.
- This provides observed-effect bridge evidence for spatially aware human-agent interaction.

### BK03 PICAN Metaverse Onboarding

Decision:

- `bridge_core`
- `agent_accessible_representation = L2`
- `evidence_status = observed_effect`

Source basis:

- Yonsei/KAIST publication pages for `A Context-Aware Onboarding Agent for Metaverse Powered by Large Language Models`
- DOI: `10.1145/3643834.3661579`

Reasoning:

- The system uses short-term spatiotemporal context, including current location, recent conversation, and actions.
- It also uses long-term exploration context.
- The source reports an ablation study and user study, including improved usefulness/immersiveness and learning about virtual locations and activities.
- It is a metaverse onboarding bridge case, not population simulation.

### BK04 NPC Interaction

Decision:

- `bridge_core`
- `agent_accessible_representation = L2`

Source basis:

- local PDF: `assets/survey_paper/pdfs/phase1_adjacent/07_BK04_NPC_Interaction.pdf`
- earlier primary-source review

Reasoning:

- Unity/NPC interaction in an explicit game-world scene.
- The spatial setting is socially situated, but the study is a single user-to-NPC interface.

### BK05 Forum-Theatre VR Training

Decision:

- `bridge_core`
- `agent_accessible_representation = L2`

Source basis:

- local PDF: `assets/survey_paper/pdfs/phase1_adjacent/08_BK05_Forum_Theatre_Training.pdf`
- earlier primary-source review

Reasoning:

- VR training scene with virtual agents and mixed-initiative dialogue management.
- The setting is socially staged and spatially situated.
- Bridge only because the contribution is training interaction rather than broad social simulation.

## Distribution After This Pass

Row-level widened Core distribution:

| Representation | Count |
|---|---:|
| `L1` | 1 |
| `L2` | 5 |
| `L3` | 18 |
| `L4` | 0 |
| `L5` | 6 |
| **Total** | **30** |

Paper-level widened Core count:

| Layer | Count |
|---|---:|
| `anchor_core` | 17 |
| `bridge_core` | 11 |
| **Total counted widened Core** | **28** |

Reserve:

- `LD01` remains reserve and is not counted.

## Interpretation

The local widening pass solves the corpus-size and `L2/L5` thinness problem but does not solve `L4`.

`L4 = 0` should remain a valid gap under the current agent-facing rule. The widened boundary shows that even when social VR, online community, metaverse, NPC, and embodied cooperation cases are admitted, agent-facing global abstract spatial structure remains absent in the local corpus.

## Later L4 Robustness Update

A subsequent targeted robustness search is documented in:

- `assets/survey_paper/phase1/phase1_targeted_l4_robustness_search_2026-04-27.md`
- `assets/survey_paper/phase1/phase1_targeted_l4_robustness_candidates_2026-04-27.csv`

That search identified one additional widened-bridge `L4` case:

- `L4R-01` Network formation and dynamics among multi-LLMs

After admitting `L4R-01`, the widened-Core evidence map has:

- `31` rows
- `29` paper-level items
- `L1 = 1 / L2 = 5 / L3 = 18 / L4 = 1 / L5 = 6`

Interpretation adjustment:

- `L4` is no longer entirely absent in widened Core.
- `L4` remains absent from strict `anchor_core`.
- The only current `L4` row is a digital social-network bridge case, so it should not erase the stricter finding that physical/virtual spatial-social systems rarely expose agent-facing global abstract spatial structure.
