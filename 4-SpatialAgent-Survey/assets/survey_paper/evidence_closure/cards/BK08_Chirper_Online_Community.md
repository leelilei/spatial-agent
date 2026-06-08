# BK08 Closure Card - Chirper Online Community

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `BK08`

Paper: *Unveiling the Collective Behaviors of Large Language Model-Based Autonomous Agents in an Online Community: A Social Network Analysis Perspective*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_adjacent/18_BK08_Online_Community_Collective_Behaviors_2026.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_adjacent/18_BK08_Online_Community_Collective_Behaviors_2026.fulltext.md`
- Source note: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/BK08.source.md`
- Extraction status: `14` pages, `status: ok`, `text_char_count: 75934`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `bridge_core` | Keep. Chirper is an online-community bridge case, not a physical or navigable environment. |
| `environment_side_representation` | `graph_based` | Keep. The study constructs a directed like-based interaction network among agents. |
| `agent_accessible_representation` | `L3` | Keep. Agents have profiles, posts, feeds, likes/comments/follows, and histories, while SNA metrics are researcher-side. |
| `behavioral_scale` | `emergent_social_structure` | Keep. The study analyzes collective behavior, small-world structure, degree distributions, preferential attachment, and homophily. |
| `evidence_status` | `observed_effect` | Keep. The reported network contains observed agent interactions and quantitative social-network analysis. |

## Evidence Notes

The paper studies Chirper, a Twitter-like online community inhabited by LLM-based autonomous agents. The platform includes continuous feeds, posts, likes, comments, hashtags, trending conversations, profile pages, biographies, follower/following information, activity histories, and posting/liking records.

The authors construct a directed weighted network from likes, with each node representing an agent and each edge representing likes from one agent to another. The analyzed network contains 26,369 nodes and 113,236 directed edges. They then apply social-network analysis to test small-world structure, power-law degree distributions, preferential attachment, profile-based homophily, and content-based homophily.

The representation boundary is the key decision. The social graph is real and analytically important, but the paper does not show that agents receive global graph statistics, centrality, community labels, or whole-network topology as inputs. Thus it is `L3` under the widened digital-network bridge rule, unlike `L4R-01` where graph features are explicitly agent-facing.

## Page/Section Anchors

- Abstract and Introduction, pages 1-2: Chirper platform, collective behavior, and SNA framing.
- Section 4.1, pages 5-6: Chirper dataset, profiles, posts, interaction histories, and platform interface.
- Section 4.2, pages 6-7: like-based directed network construction and SNA metrics.
- Section 5.1-5.3, pages 7-11: small-world structure, degree distributions, preferential attachment, and homophily results.
- Discussion, pages 11-12: human-like collective behavior and limitations.

## Claim Boundary

Allowed manuscript use:

- Use `BK08` as bridge evidence for LLM-agent collective behavior in an online social platform.
- Use it to show the distinction between platform-level graph structure and agent-facing graph representation.
- Use it as `graph_based / L3 / observed_effect`.

Disallowed manuscript use:

- Do not code it as `L4`; SNA metrics are not shown as agent inputs.
- Do not use it as evidence of physical spatial behavior.
- Do not generalize platform interaction patterns to built-environment spatial effects.

## Follow-Up

No acquisition action is needed. Current coding can remain `bridge_core / graph_based / L3 / emergent_social_structure / observed_effect`.
