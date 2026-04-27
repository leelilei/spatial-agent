# Phase 1 Widened Core Execution Memo

Date: 2026-04-27

Purpose: execute the previously documented Core boundary widening for the corpus-size and representation-balance problem, without overwriting the strict `anchor_core` baseline.

## Starting Point

Strict stable baseline:

- `17` paper-level `anchor_core` items
- `19` system/configuration rows
- representation mix: `L1 = 1 / L2 = 0 / L3 = 15 / L4 = 0 / L5 = 3`

Problem:

- `17` paper-level Core items is small for the intended evidence map.
- `L2`, `L4`, and `L5` are too thin for a useful distributional discussion.
- `L1` is also sparse, but forcing `L1` upward would mostly admit systems where space is too weak to matter.

## Working Decision

Use a widened Core structure:

- `anchor_core`: the strict multi-agent or population-level spatial-social nucleus.
- `bridge_core`: spatially and socially meaningful bridge cases that are weaker on full population-level social simulation but still belong inside the main evidence map under the widened scope.

Do not collapse the two layers. Claims based mainly on `bridge_core` must be marked as widened-core or bridge-level evidence.

## Admission Rules for This Execution Pass

A paper can enter `bridge_core` if it satisfies all of the following:

1. It involves LLM/VLM/generative agents.
2. The environment is spatially recognizable, including physical, virtual, embodied, metaverse, social-VR, or explicitly structured digital environments.
3. The study object is socially situated in at least one of these ways:
   - multi-agent social simulation
   - socially situated human-agent or avatar-agent interaction
   - online or virtual-community collective behavior
   - embodied cooperation or conflict in an explicit spatial world
4. The spatial representation can be coded from the agent-facing evidence, not only from backend implementation richness.

## Representation Rule Adjustments

### L1

Do not deliberately inflate `L1`. A sparse `L1` slice is acceptable because `L1` means location labels without relation or descriptive structure.

### L2

Widened `bridge_core` can admit `L2` cases when the agent receives semantic or scene-level spatial descriptions in a socially meaningful environment, even if the system is human-agent, avatar-agent, NPC, or training-oriented rather than full social simulation.

This is the main repair path for the `L2 = 0` problem.

### L4

Use the revised rule from the coding manual:

- `L4` is agent-facing global abstract spatial structure.
- It includes classic configurational indicators such as `integration`, `depth`, `control`, or `choice`, but is not limited to those names.
- It may also include whole-network position, global connectivity, centrality, accessibility, community structure, or route-structure summaries if these are exposed to agents as part of their operating state.

Important constraint:

- Researcher-side social-network analysis does not count as `L4` unless the global structure is actually agent-facing.

### L5

Widened `bridge_core` can admit embodied or geometry-rich systems when agents directly receive raw visual observations, coordinates, depth, collision, physical constraints, or other geometry-bearing inputs, even if the paper is a cooperation benchmark or single-agent built-environment simulator.

These rows must not be used as equal evidence for social emergence unless the paper reports social/group behavior.

## Reclassification Outcome

### Promote Now

These cases can enter `bridge_core` under the widened rule with existing local evidence:

| ID | Decision | Repr | Reason |
|---|---|---|---|
| `HC01` | promote to `bridge_core` | `L5` | Strong built-environment spatial interface with observed navigation behavior; weak on multi-agent social behavior, so bridge only. |
| `BK06` | promote to `bridge_core` | `L5` | Rich embodied simulator with social-world and human-AI collaboration affordances; bridge because the paper is platform-like. |
| `BK07` | promote to `bridge_core` | `L3_or_L4_recheck` | LLM social-network simulation in a structured digital environment; needs final check on whether global network structure is agent-facing. |
| `BK08` | promote to `bridge_core` | `L3_or_L4_recheck` | Online-community collective behavior with profiles, follows, replies, and histories; needs final check on whether global community/network state is agent-facing. |
| `R3-03` | promote to `bridge_core` | `L3` | Urban mobility population adaptation in a shared transport system; bridge because interpersonal social interaction is weak. |
| `R3-05` | promote to `bridge_core` | `L5` | Embodied multi-agent cooperation with raw sensory observations; bridge because it is primarily a cooperation benchmark. |

Count effect: `17 -> 23` paper-level widened Core items.

### Promote After Quick Recheck

These cases are likely `bridge_core`, but should not be counted as stable until the source basis is checked or the existing source note is accepted as sufficient:

| ID | Decision | Repr | Reason |
|---|---|---|---|
| `HC11` | quick recheck, then likely promote | `L2` | Social VR role-play case; currently abstract-level evidence only. |
| `BK02` | quick recheck, then likely promote | `L2` | Spatially aware human-agent interaction; strong for L2 bridge evidence but not population simulation. |
| `BK03` | quick recheck, then likely promote | `L2` | Metaverse onboarding with spatiotemporal context; bridge if source confirms spatially situated interaction. |
| `BK04` | quick recheck, then likely promote | `L2` | Unity/NPC interaction with explicit spatial scene; bridge, not anchor. |
| `BK05` | quick recheck, then likely promote | `L2` | Social VR/forum-theatre training scene with virtual agents; bridge, not anchor. |

Count effect if all survive: `17 -> 28` paper-level widened Core items.

### Reserve

| ID | Decision | Repr | Reason |
|---|---|---|---|
| `LD01` | reserve only | `L2` | Avatar chatbot case is spatially/socially adjacent but weaker than the main bridge candidates. |

## Projected Representation Mix

If the six `promote_now` bridge cases enter:

- paper-level widened Core: `23`
- row-level widened Core: approximately `25`
- representation effect:
  - `L5` gains `HC01`, `BK06`, and `R3-05`
  - `L3` gains `R3-03`
  - `L4` may gain `BK07` and/or `BK08` only after agent-facing structure recheck

If the five quick-recheck cases also enter:

- paper-level widened Core: `28`
- row-level widened Core: approximately `30`
- `L2` becomes a real bridge slice with about `5` rows

If `BK07` and `BK08` remain `L3` after recheck:

- `L4` remains a strict negative finding even under widened Core.

If either exposes agent-facing global network/community structure:

- `L4` becomes a small bridge slice, not an anchor-core finding.

## Operational Consequence

Do not run a new broad search yet.

Next actions:

1. Create a bridge-core coding draft for the 12 local candidates.
2. Recheck `BK07` and `BK08` specifically for agent-facing global structure.
3. Recheck `HC11`, `BK02`, and `BK03` source basis because they are currently not locally archived as PDFs.
4. After local reclassification stabilizes, decide whether external top-up with `INDOORWORLD` and `BOOKWORLD` is still needed.

## Execution Update

The first recheck pass is now complete.

Follow-up files:

- `assets/survey_paper/phase1/phase1_widened_core_recheck_results_2026-04-27.md`
- `assets/survey_paper/phase1/phase1_widened_core_evidence_map_2026-04-27.csv`
- `assets/survey_paper/phase1/phase1_widened_core_evidence_map_2026-04-27.md`

Final local widened-Core status:

- accepted bridge-core rows: `11`
- reserve rows: `1` (`LD01`)
- widened-Core rows: `30`
- widened-Core paper-level items: `28`

Final representation status after local widening:

- `L1 = 1`
- `L2 = 5`
- `L3 = 18`
- `L4 = 0`
- `L5 = 6`

Important result:

- `BK07` and `BK08` are both `bridge_core`, but both remain `L3`.
- The local widening pass does not recover `L4`; it strengthens the interpretation of `L4 = 0` as an agent-facing representation gap.

Later robustness update:

- `phase1_targeted_l4_robustness_search_2026-04-27.md` identified `L4R-01` Network formation and dynamics among multi-LLMs as a valid widened-bridge `L4` row.
- After admitting `L4R-01`, widened Core becomes `31` rows and `29` paper-level items.
- Updated representation distribution: `L1 = 1 / L2 = 5 / L3 = 18 / L4 = 1 / L5 = 6`.
- Claim discipline: `L4` exists only in the widened digital-network bridge layer, not in strict `anchor_core`.
