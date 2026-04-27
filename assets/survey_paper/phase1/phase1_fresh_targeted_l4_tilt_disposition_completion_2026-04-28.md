# Phase 1 Fresh Targeted L4-Tilt Disposition Completion

Date: 2026-04-28

Purpose: complete title/abstract-level disposition for all `179` fresh targeted L4-tilt screening rows, rather than only adjudicating the five P0-L4 full-text cases.

Companion table:

- `assets/survey_paper/phase1/phase1_fresh_targeted_l4_tilt_disposition_2026-04-28.csv`

## Source

Input table:

- `assets/survey_paper/phase1/phase1_fresh_targeted_l4_tilt_screening_2026-04-27.csv`

Input count:

- `179` deduplicated fresh OpenAlex rows

Context:

- Original Phase 1 candidate pool: `417`
- Fresh non-duplicate rows relative to original pool: `164`
- Conservative screened surface after this round: `581`

## Disposition Status Counts

| Disposition status | Rows | Meaning |
|---|---:|---|
| `fulltext_checked_promote` | 3 | P0-L4 rows already full-text adjudicated and suitable for widened Core |
| `fulltext_checked_reserve` | 1 | P0-L4 row checked but held as reserve/optional L3 bridge |
| `fulltext_checked_adjacent` | 1 | P0-L4 row checked and assigned to Adjacent |
| `queued_for_recheck` | 7 | P1-L4 or P1-Bridge queue; not screened out |
| `title_abstract_keep` | 7 | title-level keep for later abstract/full-text recheck if more rows are needed |
| `background_or_adjacent` | 33 | useful as adjacent/background or low-priority boundary material |
| `title_abstract_exclude` | 107 | excluded at title level |
| `duplicate_existing_pool` | 16 | duplicate or already covered by original candidate pool |
| `duplicate_prior_targeted` | 3 | duplicate of prior targeted widened-screen rows |
| `duplicate_or_covered` | 1 | covered by a P0-L4 adjudicated row |
| **Total** | **179** |  |

## Tier-Like Counts

| Disposition tier | Rows |
|---|---:|
| `bridge_core` | 9 |
| `bridge_core_candidate` | 7 |
| `bridge_core_or_adjacent` | 1 |
| `bridge_core_reserve` | 1 |
| `adjacent` | 1 |
| `adjacent_or_foundational` | 33 |
| `duplicate` | 20 |
| `excluded` | 107 |
| **Total** | **179** |

Interpretation:

- Not all non-P0 rows were screened out.
- The fresh screen now has a complete disposition trail.
- Only `107 / 179` were excluded at title level.
- `7` remain in the explicit P1 queue.
- `7` additional rows remain as title-level keeps.
- `33` are retained as adjacent/background or low-priority boundary material.

## Full-Text Checked Rows

Already checked:

| ID | Result |
|---|---|
| `FT-L4-029` | promote as `bridge_core / L4 / observed_effect` |
| `FT-L4-066` | reserve or optional `bridge_core / L3 / observed_effect` |
| `FT-L4-095` | promote as `bridge_core / L3 / observed_effect` |
| `FT-L4-116` | promote with caveat as `bridge_core / L3 / observed_effect` |
| `FT-L4-171` | Adjacent only, useful for L4 feasibility |

## P1 Recheck Queue

These are not screened out:

| ID | Title | Current role |
|---|---|---|
| `FT-L4-076` | Decoding Echo Chambers: LLM-Powered Simulations Revealing Polarization in Social Networks | P1-L4 |
| `FT-L4-108` | Emergent social conventions and collective bias in LLM populations | P1-L4 |
| `FT-L4-115` | LLMs Generate Structurally Realistic Social Networks but Overestimate Political Homophily | P1-L4 |
| `FT-L4-127` | Characterizing LLM-driven Social Network: The Chirper.ai Case | P1-L4 |
| `FT-L4-136` | Modeling realistic human behavior using generative agents in a multimodal transport system | P1-Bridge |
| `FT-L4-137` | Implicit Behavioral Alignment of Language Agents in High-Stakes Crowd Simulations | P1-Bridge |
| `FT-L4-158` | Beliefs in Motion: Simulating Opinion Dynamics via LLM-Powered Community Reactions | P1-L4 |

## Additional Title-Level Keeps

These are lower than P1 but retained:

| ID | Title | Reason |
|---|---|---|
| `FT-L4-060` | Multi-LLM QA with Embodied Exploration | embodied bridge candidate |
| `FT-L4-092` | SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents | adjacent/embodied benchmark candidate |
| `FT-L4-130` | SafeMind: Benchmarking and Mitigating Safety Risks in Embodied LLM Agents | adjacent/embodied benchmark candidate |
| `FT-L4-138` | Empowering Economic Simulation for Massively Multiplayer Online Games through Generative Agent-Based Modeling | possible virtual-world/social-economy bridge case |
| `FT-L4-141` | Homophily-induced emergence of biased structures in LLM-based multi-agent AI systems | possible L3/L4 social-network bridge |
| `FT-L4-162` | From Assumptions to Actions: Turning LLM Reasoning into Uncertainty-Aware Planning for Embodied Agents | embodied planning bridge/adjacent candidate |
| `FT-L4-168` | Jailbreaking Embodied LLMs via Action-level Manipulation | embodied-agent adjacent candidate |

Duplicates/covered items:

- `FT-L4-016` is covered by existing `BK07` S^3.
- `FT-L4-027` is covered by the full-text checked `FT-L4-066`.

## Exclusion Logic

Rows were excluded at title level when they appeared to be:

- general AI/LLM surveys rather than primary systems;
- education, medicine, privacy, security, wireless-network, RAG, or general graph-generation papers without a spatial/social LLM-agent system;
- modeling or forecasting work with no clear LLM agents;
- network papers where "network" referred to mobile/wireless/computer networks rather than social/spatial agent environments;
- LLM capability or benchmark papers with no social/spatial environment.

Rows were retained as background/adjacent when they had:

- relevant social-network or spatial vocabulary but no clear LLM-agent system;
- possible feasibility value;
- likely foundational or adjacent relevance but insufficient Core evidence.

## Current Recommendation

The fresh screen is now complete enough for methods/protocol accounting.

Do not continue broad searching immediately. The next methodologically clean step is:

1. update the widened evidence map with the already adjudicated minimum set;
2. decide whether to process the seven P1 recheck rows;
3. keep the remaining title-level keeps as backlog, not active blockers.

For L4, the immediate evidence-map update should at least add:

- `FT-L4-029` as `bridge_core / L4 / observed_effect`.

Optional digital-network expansion can add:

- `FT-L4-095` as `bridge_core / L3 / observed_effect`;
- `FT-L4-116` as `bridge_core / L3 / observed_effect`.

