# Phase 1 Fresh Targeted L4-Tilt Screening Memo

Date: 2026-04-27

Purpose: expand the screened candidate surface to at least `500` while tilting the new search toward L4-related evidence: graph, topology, centrality, community structure, opinion dynamics, social networks, accessibility, and global abstract structure.

## Inputs And Outputs

New files:

- `assets/survey_paper/phase1/phase1_fresh_targeted_l4_tilt_candidates_raw_2026-04-27.csv`
- `assets/survey_paper/phase1/phase1_fresh_targeted_l4_tilt_screening_2026-04-27.csv`
- `assets/survey_paper/phase1/phase1_fresh_targeted_l4_tilt_priority_queue_2026-04-27.csv`

Search source:

- OpenAlex API

Search date:

- 2026-04-27

Year window:

- 2022-2026

## Query Families

The fresh search used ten targeted query families:

| Query family | Weight |
|---|---|
| `"large language model" "social network" "centrality"` | L4-heavy |
| `"LLM agents" "network formation" "topology"` | L4-heavy |
| `"large language model" "agent-based simulation" "graph"` | L4-heavy |
| `"LLM" "opinion dynamics" "network structure"` | L4-heavy |
| `"generative agents" "social network" "community"` | L4-heavy |
| `"LLM agents" "urban mobility" "transport network"` | bridge/L3-L4 |
| `"large language model" "crowd evacuation" "building"` | bridge/L3-L5 |
| `"LLM agents" "virtual world" "NPC" "spatial"` | bridge/L2-L5 |
| `"large language model" "metaverse" "avatar" "spatial"` | bridge/L2-L5 |
| `"embodied LLM agents" "3D" "multi-agent"` | bridge/L5 |

The first five families deliberately tilt toward L4-like network/configurational structure.

## Screening Counts

OpenAlex retrieval:

- raw retrieved rows: `199`
- deduplicated fresh rows: `179`

Duplicate control:

- duplicate with original `417` candidate pool: `15`
- non-duplicate relative to original pool: `164`
- duplicate with prior targeted widened screen: `3`
- non-duplicate relative to both original pool and prior targeted screen: `161`

Updated screened-surface count:

- original candidate pool: `417`
- fresh non-duplicate targeted rows: `164`
- conservative total screened candidates: `581`

If also counting the prior external targeted rows that were not captured by OpenAlex, the total screened surface is slightly higher, but `581` is the clean conservative number.

## L4-Tilt Distribution

Priority was recalculated from the title, not from the query string, to avoid inflated L4 counts.

Across all `179` fresh deduplicated rows:

| Title-based priority | Rows |
|---|---:|
| `high` | 15 |
| `medium` | 25 |
| `low` | 139 |

Across the `161` non-duplicate fresh rows:

| Title-based priority | Rows |
|---|---:|
| `high` | 15 |
| `medium` | 24 |
| `low` | 122 |

Interpretation:

- The search achieved the target of expanding screened candidates beyond `500`.
- It also produced a real L4-tilted review set: `39` non-duplicate rows with high/medium title-level relevance to L4-like graph, network, topology, community, or adjacent bridge structure.

## Priority Full-Text Queue

Primary L4 queue:

| ID | Title | Reason |
|---|---|---|
| `FT-L4-029` | Emergence of Scale-Free Networks in Social Interactions among Large Language Models | direct LLM social interaction + network emergence |
| `FT-L4-066` | Simulating Opinion Dynamics with Networks of LLM-based Agents | LLM agents embedded in explicit networks |
| `FT-L4-095` | LLM-AIDSim: LLM-Enhanced Agent-Based Influence Diffusion Simulation in Social Networks | influence diffusion in social networks |
| `FT-L4-116` | Understanding Online Polarization Through Human-Agent Interaction in a Synthetic LLM-Based Social Network | synthetic LLM-based social network and human-agent interaction |
| `FT-L4-171` | GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems | communication topology generation for LLM multi-agent systems |

Secondary L4/boundary queue:

| ID | Title | Reason |
|---|---|---|
| `FT-L4-076` | Decoding Echo Chambers: LLM-Powered Simulations Revealing Polarization in Social Networks | echo-chamber and polarization simulation |
| `FT-L4-108` | Emergent social conventions and collective bias in LLM populations | strong LLM population emergence; network/spatial structure uncertain |
| `FT-L4-115` | LLMs Generate Structurally Realistic Social Networks but Overestimate Political Homophily | network realism; may be generation rather than agent simulation |
| `FT-L4-127` | Characterizing LLM-driven Social Network: The Chirper.ai Case | digital LLM-driven social network |
| `FT-L4-158` | Beliefs in Motion: Simulating Opinion Dynamics via LLM-Powered Community Reactions | community reactions and opinion dynamics |

Bridge backup queue:

| ID | Title | Reason |
|---|---|---|
| `FT-L4-136` | Modeling realistic human behavior using generative agents in a multimodal transport system | transport-network bridge, check duplicate risk |
| `FT-L4-137` | Implicit Behavioral Alignment of Language Agents in High-Stakes Crowd Simulations | crowd-simulation bridge |

## Claim Discipline

This search should not be described as a broad expansion. It is a targeted supplementary screen:

> We added a fresh targeted screening round, tilted toward graph/network/topology terms, to test whether the apparent scarcity of agent-facing global abstract structure was an artifact of the original search vocabulary.

Safe downstream wording:

- screened surface now exceeds `500` candidates;
- L4-targeted queries yielded a small but concrete full-text recheck queue;
- L4 remains a question for full-text adjudication, not an assumed recovered slice.

Avoid:

- saying L4 has been solved before checking whether network/global structure is agent-facing;
- counting every social-network simulation as L4;
- treating communication topology methods as spatial-social evidence unless they involve agent behavior in a socially meaningful environment.

## Next Step

Full-text recheck should start with the `P0-L4` rows:

1. `FT-L4-029`
2. `FT-L4-066`
3. `FT-L4-095`
4. `FT-L4-116`
5. `FT-L4-171`

The main adjudication question is the same for all:

> Is global abstract structure actually agent-facing, or is it only a researcher-side network metric?

