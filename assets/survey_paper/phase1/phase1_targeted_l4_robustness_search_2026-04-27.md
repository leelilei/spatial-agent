# Phase 1 Targeted L4 Robustness Search

Date: 2026-04-27

Purpose: run a narrow robustness search for `L4` after widened Core still had `L4 = 0`.

This pass is not a broad Core expansion. It tests whether the `L4 = 0` finding survives queries that are broader than classic Space Syntax metric names.

## L4 Rule Used

`L4` means agent-facing global abstract spatial or network structure.

Counts as `L4`:

- whole-network or whole-layout structure in the agent prompt/state
- node degree, centrality, bridge role, community label, common-neighbor count, or whole-network neighborhood information if used by the agent for action
- accessibility, connectivity, route hierarchy, or global reachability if returned to an agent as part of its operating state

Does not count as `L4`:

- researcher-side SNA after the simulation
- backend graph structure invisible to the agent
- local followee/neighbor/co-presence exposure only
- route/location context without a global structural summary

## Query Families

Searches targeted:

- `LLM agents centrality prompt social network simulation`
- `large language model agents global topology simulation`
- `generative agents centrality social network prompt`
- `LLM multi-agent community structure prompt simulation`
- `LLM agents accessibility urban simulation prompt`
- `LLM agents global map simulation prompt`

Primary sources were preferred when available.

## Main Finding

The earlier `L4 = 0` result does not fully survive the broader `global abstract structure` search.

One strong bridge-core `L4` hit was identified:

- `L4R-01` Papachristou and Yuan, *Network formation and dynamics among multi-LLMs*

This paper should be added as a `bridge_core / L4` row if the widened digital-network environment rule remains active.

## Candidate Decisions

### L4R-01 Network formation and dynamics among multi-LLMs

Primary source:

- `https://academic.oup.com/pnasnexus/article/doi/10.1093/pnasnexus/pgaf317/8361967`

Decision:

- advance to `bridge_core`
- code as `L4`

Why it qualifies:

- The paper studies multiple LLM agents making network-formation decisions.
- The environment is a social/professional network.
- The agent-facing input includes global or semi-global abstract network information.
- The paper explicitly states that LLMs receive candidate attributes such as node degrees, neighbors, common connections, and community labels in JSON format.
- In the small-world experiment, the model is provided with full network structure including nodes and neighborhoods before selecting rewiring endpoints.
- These are not only researcher-side metrics; they are part of the decision input.

Conservative coding:

- `core_layer = bridge_core`
- `environment_side_representation = graph_based`
- `agent_accessible_representation = L4`
- `behavioral_scale = emergent_social_structure`
- `evidence_status = observed_effect`
- `spatial_behavior_coupling = explicit`

Caution:

- This is a digital social-network environment, not physical or navigable space.
- It should not be mixed with `anchor_core` claims.
- It is best used to show that `L4` exists in a widened digital-network bridge layer, while still remaining absent from the stricter physical/virtual spatial-social nucleus.

### L4R-02 CiteAgent

Primary source:

- `https://www.nature.com/articles/s41599-025-06193-w`

Decision:

- reserve / boundary recheck

Why it is relevant:

- It simulates citation-network evolution with LLM-based agents.
- Agents operate over paper/author/citation attributes.
- Citation-related visibility and recommendation algorithms affect generated network structure.

Why not immediately count:

- It is a science-of-science citation network, farther from the project's spatial-social environment target than online communities or social networks.
- It should enter only if the project explicitly accepts citation/research-community networks as part of the widened digital-social bridge layer.

### L4R-03 Smart City Management

Primary source:

- `https://www.mdpi.com/2624-6511/8/1/19/xml`

Decision:

- keep `Adjacent`

Why it is relevant:

- The system exposes accessibility, service provision, connectivity, service proximity, development potential, centrality, and geospatial layers through a Digital Urban Platform API.
- This is a strong `L4 feasibility` case.

Why not Core:

- It is a decision-support system for urban management, not social simulation or socially situated interaction.
- The agents are task-processing roles, not simulated social actors.

### Already Counted Cases Rechecked

`BK07` and `BK08` remain `L3`, not `L4`.

- `BK07`: follow graph, followee message exposure, profiles, memory, and propagation are agent-facing, but no evidence shows global centrality/community summaries in agent input.
- `BK08`: centralization, homophily, power-law, and small-world structure are researcher-side SNA outputs, not agent-facing structure.

`R3-03` remains `L3`, not `L4`.

- It has geospatial transport context and adaptation, but the current source basis supports route/location/context exposure rather than global abstract configurational indicators in agent state.

## Updated Distribution If L4R-01 Is Admitted

Row-level widened Core:

| Representation | Before L4 robustness | After admitting L4R-01 |
|---|---:|---:|
| `L1` | 1 | 1 |
| `L2` | 5 | 5 |
| `L3` | 18 | 18 |
| `L4` | 0 | 1 |
| `L5` | 6 | 6 |
| **Total** | **30** | **31** |

Paper-level widened Core:

- before: `28`
- after admitting `L4R-01`: `29`

## L1 Sanity Note

No dedicated `L1` search was run.

Reason:

- `L1` means only location or area labels without semantic, topological, geometric, or global structural information.
- Deliberately searching for `L1` would mostly retrieve weak spatial cases where space is nominal rather than analytically meaningful.
- Sparse `L1` is therefore not a coverage defect in the same way that sparse `L2`, `L4`, or `L5` is.

Working interpretation:

- `L1 = 1` should be retained as a descriptive result.
- Do not inflate `L1` unless a known bridge case naturally fits.

## Recommendation

Add `L4R-01` to the widened-Core evidence map as a `bridge_core / L4` row.

Do not add `L4R-02` unless the project explicitly accepts citation-network science-of-science simulations as in-scope bridge cases.

Keep `L4R-03` as Adjacent feasibility evidence.

