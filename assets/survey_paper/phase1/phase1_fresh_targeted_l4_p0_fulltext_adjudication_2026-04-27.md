# Phase 1 Fresh Targeted L4 P0 Full-Text Adjudication

Date: 2026-04-27

CSV companion:

- `assets/survey_paper/phase1/phase1_fresh_targeted_l4_p0_fulltext_adjudication_2026-04-27.csv`

Purpose: adjudicate the five `P0-L4` rows from `phase1_fresh_targeted_l4_tilt_priority_queue_2026-04-27.csv`, with one question:

> Is global abstract graph/network/topology structure actually agent-facing, or only researcher-side analysis?

## Summary

| ID | Decision | Layer | Repr | Evidence | L4 result |
|---|---|---|---|---|---|
| `FT-L4-029` | promote now | `bridge_core` | `L4` | `observed_effect` | yes, strongest fresh L4 case |
| `FT-L4-066` | reserve or bridge L3 | `bridge_core` | `L3` | `observed_effect` | no |
| `FT-L4-095` | promote now | `bridge_core` | `L3` | `observed_effect` | no |
| `FT-L4-116` | promote with caveat | `bridge_core` | `L3` | `observed_effect` | no, unless later full text shows global metrics are agent-facing |
| `FT-L4-171` | adjacent only | `adjacent` | `L4` | `observed_effect` | L4 feasibility, not Core |

Net effect if promoted after duplicate control:

- widened-Core rows: `34 -> 37` if adding `FT-L4-029`, `FT-L4-095`, and `FT-L4-116`
- `L4`: `1 -> 2` in widened Core
- `L3`: increases by `2` if `FT-L4-095` and `FT-L4-116` are added
- strict `anchor_core` L4 remains `0`

Conservative alternative:

- If we only add the unambiguous L4 row, widened Core becomes `35` rows and `L4 = 2`.
- This is the cleaner choice if we want to keep the digital-network bridge layer compact.

## FT-L4-029

Title: `Emergence of Scale-Free Networks in Social Interactions among Large Language Models`

Decision: `promote_now` as `bridge_core / L4 / observed_effect`.

Why:

- The system simulates a growing online social network with LLM agents.
- At each step, agents receive information about existing users.
- Crucially, the full text states that the agent sees each user's number of friends, i.e. degree information.
- The agent then chooses whom to connect to.
- The paper evaluates emergent network structures such as scale-free and hub-and-spoke patterns.

Coding:

- `environment_side = graph_based`
- `agent_accessible = L4`
- `evidence_status = observed_effect`
- `behavioral_scale = emergent_social_structure`

This is a valid L4 case because agent-facing degree information is a global abstract network-position signal, not merely local co-presence or researcher-side SNA.

Boundary:

- It is still `bridge_core`, not `anchor_core`, because it is a digital social-network environment rather than a physical/virtual spatial-social environment.

## FT-L4-066

Title: `Simulating Opinion Dynamics with Networks of LLM-based Agents`

Decision: `reserve_or_bridge_l3`.

Why:

- The paper studies LLM-agent opinion dynamics and reports observed opinion trajectories.
- It is useful for LLM population/opinion-dynamics evidence.
- But the implementation does not recover L4. The paper notes that its agents can interact with everyone and that more realistic network structures are future work.

Coding:

- If included: `bridge_core / L3 / observed_effect`
- Not L4.

Boundary:

- Despite the title using "networks", the agent-facing structure is closer to repeated dyadic/all-to-all interaction than to global topology.

## FT-L4-095

Title: `LLM-AIDSim: LLM-Enhanced Agent-Based Influence Diffusion Simulation in Social Networks`

Decision: `promote_now` as `bridge_core / L3 / observed_effect`.

Why:

- The paper defines a directed social network with in-neighbours and out-neighbours.
- LLM user agents respond to information and influence diffusion unfolds through network links.
- The model can use synthetic or real-world social networks.

Why not L4:

- The agent-facing evidence is based on incoming messages and active in-neighbour responses.
- The paper does not show that agents receive global graph metrics such as centrality, community labels, accessibility, or whole-network position.

Coding:

- `environment_side = graph_based`
- `agent_accessible = L3`
- `evidence_status = observed_effect`
- `behavioral_scale = emergent_social_structure`

## FT-L4-116

Title: `Understanding Online Polarization Through Human-Agent Interaction in a Synthetic LLM-Based Social Network`

Decision: `promote_now_with_caveat` as `bridge_core / L3 / observed_effect`.

Why:

- The paper studies human-agent interaction in a synthetic LLM-based social network.
- It reports a controlled experiment with 122 participants and manipulated social-network environments.
- It observes effects on emotionality, group identity salience, and expressed uncertainty.

Why not L4 yet:

- The accessible evidence shows a networked environment and experimental manipulation.
- It does not yet show that LLM agents receive global graph metrics or topology summaries.

Coding:

- `environment_side = graph_based`
- `agent_accessible = L3`
- `evidence_status = observed_effect`
- `behavioral_scale = interaction`

Keep a representation-gap note if added:

- "Network environment is central, but agent-facing global metrics are not yet verified."

## FT-L4-171

Title: `GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems`

Decision: `adjacent_only`.

Why:

- This is directly about communication topology generation for LLM-based multi-agent systems.
- It is a useful L4 feasibility case because it optimizes/generates topology.
- But it is not a spatial or socially situated environment, and the behavior is task/coordination performance rather than spatial-social behavior.

Coding:

- Use as `Adjacent / L4 feasibility`.
- Do not add to Core evidence map.

## Updated Reading Of L4

Before this P0-L4 adjudication:

- widened Core had `L4 = 1`, from `L4R-01`.
- strict `anchor_core` still had `L4 = 0`.

After this adjudication:

- `FT-L4-029` gives one additional valid widened `bridge_core / L4` row.
- widened Core can become `L4 = 2`.
- strict `anchor_core` remains `L4 = 0`.

Therefore the correct claim is now:

> Agent-facing global abstract structure is absent from strict anchor-core physical/virtual spatial-social systems, but a small number of widened digital-network bridge cases expose global network-position or topology-related information to agents.

This is stronger and more precise than the previous claim that L4 appears only once. The gap remains real, but it is now a "very sparse digital-network bridge slice" rather than a singleton.

## Recommended Evidence-Map Update

Minimal update:

1. Add `FT-L4-029` as `bridge_core / L4 / observed_effect`.
2. Keep `FT-L4-171` in Adjacent feasibility notes.
3. Hold `FT-L4-066`, `FT-L4-095`, and `FT-L4-116` until deciding whether to expand the digital-network bridge layer beyond L4 recovery.

Expanded update:

1. Add `FT-L4-029`.
2. Add `FT-L4-095` and `FT-L4-116` as `bridge_core / L3 / observed_effect`.
3. Keep `FT-L4-066` as reserve unless more network-specific evidence is needed.
4. Keep `FT-L4-171` as Adjacent.

The minimal update is cleaner for claim discipline; the expanded update is better for increasing corpus size.

