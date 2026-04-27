# Phase 1 Targeted Widened P0 Full-Text Recheck

Date: 2026-04-27

CSV companion:

- `assets/survey_paper/phase1/phase1_targeted_widened_p0_fulltext_recheck_2026-04-27.csv`

Purpose: adjudicate the four P0 rows from `phase1_targeted_widened_fulltext_queue_2026-04-27.csv`.

## Summary

All four P0 rows are relevant, but duplicate checking shows that `TW-04` is already represented by the existing `R3-02` GATSim row. The net new rows are therefore `3`, not `4`.

| ID | Decision | Layer | Repr | Evidence | Main contribution |
|---|---|---|---|---|---|
| `TW-04` | duplicate existing `R3-02` | `bridge_core` | `L3` | `observed_effect` | urban mobility/population bridge |
| `TW-09` | promote now | `bridge_core` | `L2` | `designed_affordance_only` | social-VR L2 bridge |
| `TW-11` | promote with caveat | `bridge_core` | `L2` | `observed_effect` | VR game NPC/player interaction bridge |
| `TW-13` | promote now | `bridge_core` | `L5` | `observed_effect` | VR NPC orientation and navigation bridge |

Expected distribution effect after duplicate check:

- widened-Core rows: `31 -> 34`
- `L2`: `5 -> 7`
- `L3`: unchanged at `18` because `TW-04` duplicates existing `R3-02`
- `L5`: `6 -> 7`
- `L4`: unchanged at `1`

This improves corpus size and the L2/L5 slices, but it does not materially change the L4 conclusion.

## TW-04: GATSim / Urban Mobility

Decision: `duplicate_existing`; keep the existing `R3-02` row as `bridge_core / L3 / observed_effect`.

Rationale:

- The paper reports a generative-agent framework for urban mobility in a stylized transportation network.
- It includes agent heterogeneity, daily schedules, spatial-temporal memory, individualized perceptions, route learning, incident response, and validation against micro- and macro-level mobility data.
- The social dimension is population-level mobility adaptation rather than interpersonal social interaction, so it belongs in `bridge_core`, not `anchor_core`.

Representation:

- Code as `L3`, not `L4`.
- The evidence supports route/network and spatial-temporal context, but not agent-facing global centrality, accessibility, or configurational metrics.
- Do not add a new row, because `R3-02` GATSim is already present in the widened evidence map.

Claim use:

- Can support widened-Core statements about LLM agents in urban/population mobility environments.
- Should not be used for claims about dialogue, cooperation, conflict, or social emergence.

## TW-09: ELLMA-T / Social VR

Decision: `promote_now` as `bridge_core / L2 / designed_affordance_only`.

Rationale:

- The paper reports an embodied GPT-4 conversational agent in VRChat for English learning, with role-play scenarios and qualitative user interviews.
- It is spatially situated in virtual worlds such as cafe, outdoor, and supermarket scenes.
- The agent receives/generates scene descriptions and role-play context, but the paper does not clearly show direct raw geometry, coordinates, pathfinding, or global topology as agent-facing input.

Representation:

- Code as `L2`.
- Do not code as `L5` just because the system runs in VR.

Evidence:

- The paper has human evaluation, but for our spatial-behavior question it mainly demonstrates a designed social-VR affordance rather than a tested spatial effect.

Claim use:

- Useful for strengthening the recovered L2 bridge slice.
- Not usable as evidence that spatial configuration affects behavior.

## TW-11: Dialogs With GenAI NPCs / VR Game

Decision: `promote_now_with_caveat` as `bridge_core / L2 / observed_effect`.

Rationale:

- The paper reports a user study of speech interaction with GenAI NPCs in a VR adventure-puzzle game.
- This is a spatially situated player-NPC interaction case, so it fits the widened bridge rule.
- It is not full population-level social simulation, so it remains `bridge_core`.

Representation:

- Code as `L2` with a representation-gap note.
- The spatial input appears to be mostly scene/NPC situatedness rather than raw geometry.
- The paper's own reported user feedback points to limited spatial understanding: players wanted NPCs to better account for positions in rooms, objects, and character locations.

Evidence:

- Code as `observed_effect` for observed player-NPC interaction outcomes and reported usability/immersion effects.
- Do not use it as evidence that rich spatial representation was successfully implemented.

Claim use:

- Useful as a bridge case showing that spatially situated GenAI NPC interactions are now being empirically studied.
- Also useful as a limitation example for agent-facing spatial awareness.

## TW-13: Next-Gen Orientation / Generative AI NPCs in VR

Decision: `promote_now` as `bridge_core / L5 / observed_effect`.

Rationale:

- The paper reports TUMSphere, a VR campus orientation system with generative AI NPCs.
- The system uses Unreal Engine 5, Convai, knowledge bases, spatially situated NPC guides, and navigation tasks.
- The evaluation reports `N = 24`, mixed-methods data, and full navigation task completion.

Representation:

- Code as `L5`, with caveat.
- Spatial action is implemented through the 3D engine, NavMesh walkable areas, NPC escort behavior, and object/location position references.
- The system does not provide Space Syntax or L4-style configurational metrics, so do not code as `L4`.

Evidence:

- Code as `observed_effect`, because the user study reports navigation and orientation outcomes in the VR environment.

Claim use:

- Useful for strengthening the L5 bridge slice.
- Do not use as social-emergence evidence; it is a human-agent orientation/navigation interaction case.

## Implications

The P0 queue confirms that the targeted widened screen was worthwhile:

- it likely adds `3` non-duplicate bridge rows;
- it strengthens the recovered `L2` and `L5` slices;
- it provides more VR/NPC/socially situated interaction evidence;
- it does not solve L4.

The updated claim should be:

> Widening the bridge layer can bring the corpus to roughly `34` rows after P0 duplicate control and recovers more social-VR and NPC evidence, but agent-facing global abstract structure remains nearly absent outside a single digital-network bridge case.

## Next Step

Before updating the main widened evidence map:

1. Add non-duplicate P0 rows `TW-09`, `TW-11`, and `TW-13` to a provisional evidence-map update.
2. Keep `TW-04` as supporting evidence for existing `R3-02`, not a new row.
3. Only then decide whether the P1 queue is needed.
