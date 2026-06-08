# BK07 Closure Card - S3 Social-Network Simulation

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `BK07`

Paper: *S^3: Social-network Simulation System with Large Language Model-Empowered Agents*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_adjacent/10_BK07_S3_Social_Network_Simulation.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_adjacent/10_BK07_S3_Social_Network_Simulation.fulltext.md`
- Extraction status: `18` pages, `status: ok`, `text_char_count: 60720`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `bridge_core` | Keep. It is a widened digital-social simulation case rather than physical or navigable spatial simulation. |
| `environment_side_representation` | `graph_based` | Keep. The environment is an online social network with directed following relations, posts, and propagation links. |
| `agent_accessible_representation` | `L3` | Keep. Agents observe posts from followees, profiles, demographics, memory, and received messages; global graph metrics are not shown as agent-facing decision inputs. |
| `behavioral_scale` | `emergent_social_structure` | Keep. The paper simulates information, emotion, and attitude propagation across a social network. |
| `evidence_status` | `observed_effect` | Keep. The paper reports individual- and population-level evaluation against real social-network data and baselines. |

## Evidence Notes

S3 constructs a social-network simulation environment from real-world social-media data. Users are nodes in a directed graph; following relations shape who receives messages. LLM-empowered agents simulate emotion, attitude, content generation, reposting/posting, and inactivity. The system updates memory pools and propagates messages through followers over time.

The widened bridge inclusion is justified because the operative environment is a graph-structured digital social environment. The row remains `L3`, not `L4`, because the LLM prompts use user profiles, demographics, historical posts, current emotion/attitude state, received messages, and memory. The paper describes network structure and uses population-level graph outcomes, but does not show the agent receiving global centrality, community structure, shortest paths, network-wide statistics, or full topology as decision features.

Observed-effect status is supported by reported prediction tasks and population-level simulations of information propagation, emotion propagation, and attitude propagation, including comparisons to baseline models.

## Page/Section Anchors

- Abstract and Introduction, pages 1-2: LLM-empowered social-network simulation and population-level propagation.
- Section 3.2, pages 5-6: social network environment, real data, user connections, and demographics.
- Section 3.3-3.4, pages 6-10: emotion, attitude, content generation, and population-level propagation.
- Section 4.2, pages 11-13: directed graph construction, followee/follower message propagation, memory pool, and LLM-based behavior simulation.
- Results sections, pages 8-11: information, emotion, and attitude propagation comparisons.

## Claim Boundary

Allowed manuscript use:

- Use `BK07` as bridge evidence that LLM agents can operate inside a digital social graph.
- Use it to distinguish local feed/followee exposure from agent-facing global graph representation.
- Use it as `graph_based / L3 / observed_effect`.

Disallowed manuscript use:

- Do not code it as `L4`; graph analytics are environment/researcher side, not clearly agent-facing.
- Do not treat it as physical spatial simulation.
- Do not claim Space Syntax or built-environment effects.

## Follow-Up

No acquisition action is needed. Current coding can remain `bridge_core / graph_based / L3 / emergent_social_structure / observed_effect`.
