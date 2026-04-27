# Phase 1 Fresh Targeted L4 Abstract Completion

Date: 2026-04-28

Purpose: complete the abstract retrieval and abstract-level disposition pass for the fresh L4-tilt targeted screen.

## New Files

- `assets/survey_paper/phase1/phase1_fresh_targeted_l4_tilt_abstracts_2026-04-28.csv`
- `assets/survey_paper/phase1/phase1_fresh_targeted_l4_tilt_abstract_disposition_2026-04-28.csv`

## Abstract Retrieval

Source:

- OpenAlex API, queried by OpenAlex ID recovered from the raw fresh-search table.

Rows:

| Scope | Rows | Abstract available | Abstract missing |
|---|---:|---:|---:|
| All fresh L4-tilt rows | 179 | 166 | 13 |
| Non-duplicate vs original `417` pool | 164 | 151 | 13 |
| Non-duplicate vs original pool and prior targeted screen | 161 | 148 | 13 |

Interpretation:

- The fresh L4-tilt screen is no longer only title/metadata-screened.
- `166 / 179` fresh records now have reconstructed abstracts.
- The remaining `13` lack abstracts in OpenAlex and are marked explicitly as abstract-missing.

## Abstract-Level Disposition

Companion table:

- `assets/survey_paper/phase1/phase1_fresh_targeted_l4_tilt_abstract_disposition_2026-04-28.csv`

Final disposition counts:

| Abstract disposition status | Rows |
|---|---:|
| `fulltext_checked_promote` | 3 |
| `fulltext_checked_reserve` | 1 |
| `fulltext_checked_adjacent` | 1 |
| `queued_for_recheck` | 7 |
| `abstract_keep` | 15 |
| `abstract_keep_adjacent` | 16 |
| `abstract_background_or_adjacent` | 53 |
| `abstract_exclude` | 50 |
| `abstract_missing_keep_metadata` | 4 |
| `abstract_missing_exclude` | 8 |
| `duplicate_existing_pool` | 17 |
| `duplicate_prior_targeted` | 3 |
| `duplicate_or_covered` | 1 |
| **Total** | **179** |

Tier-like grouping:

| Tier-like disposition | Rows |
|---|---:|
| `bridge_core` | 9 |
| `bridge_core_candidate` | 15 |
| `bridge_core_or_adjacent` | 1 |
| `bridge_core_reserve` | 1 |
| `adjacent` | 1 |
| `adjacent_or_bridge_candidate` | 16 |
| `adjacent_or_foundational` | 57 |
| `duplicate` | 21 |
| `excluded` | 58 |
| **Total** | **179** |

## Active Queues After Abstract Completion

Already full-text checked:

- `FT-L4-029`
- `FT-L4-066`
- `FT-L4-095`
- `FT-L4-116`
- `FT-L4-171`

P1 queue remains active:

- `FT-L4-076`
- `FT-L4-108`
- `FT-L4-115`
- `FT-L4-127`
- `FT-L4-136`
- `FT-L4-137`
- `FT-L4-158`

Additional abstract-level bridge candidates:

- `FT-L4-032` Urban Generative Intelligence
- `FT-L4-068` Y Social
- `FT-L4-083` Unbounded
- `FT-L4-089` CharacterBox
- `FT-L4-101` LLM-Driven Social Influence for Cooperative Behavior
- `FT-L4-110` Lagged Stance Interactions and Counter-Spiral of Silence
- `FT-L4-123` BOOKWORLD
- `FT-L4-128` LLM Driven Agents for Simulating Echo Chamber Formation
- `FT-L4-129` Simulating Online Social Media Conversations
- `FT-L4-138` Economic Simulation for MMORPGs with Generative Agent-Based Modeling
- `FT-L4-140` Simulating conversations on social media with generative agent-based models
- `FT-L4-141` Homophily-induced emergence of biased structures in LLM-based multi-agent AI systems
- `FT-L4-153` MineNPC-Task
- `FT-L4-154` MetaProxy
- `FT-L4-178` Influence in Motion

## Corrected Methods Wording

After this pass, the methods wording can be strengthened:

> We identified `581` records after targeted supplementary screening. The original Phase 1 pool contained `417` records, of which `348` had abstracts available locally. The fresh L4-tilt search added `164` non-duplicate records relative to the original pool; `151` of these had abstracts retrieved from OpenAlex and were screened at abstract level, while `13` were screened using title/metadata because abstracts were unavailable.

Still avoid:

- `581 abstracts were screened.`

Use instead:

- `581 records were identified and screened at title/metadata level, with abstract-level screening performed where abstracts were available and full-text adjudication for prioritized candidates.`

## Current Recommendation

The abstract completion pass is sufficient for protocol accounting.

Next step:

1. Update the widened evidence map using already adjudicated rows.
2. Then decide whether P1 queue review is necessary for further L4 strengthening.

