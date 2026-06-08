# HC07 Closure Card - OASIS

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `HC07`

Paper: Yang et al. 2024, *OASIS: Open Agent Social Interaction Simulations with One Million Agents*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_core/06_OASIS_Yang2024.pdf`
- Markdown dossier: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/HC07_OASIS_Open_Agent_Social_Interaction_Simulations_with_One_Million_Agents.md`
- Extraction status in dossier: `pypdf`, `37` pages, `status: ok`, `text_char_count: 106548`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `anchor_core` | Keep. OASIS is a large-scale LLM-agent social simulation of platform interaction dynamics. |
| `environment_side_representation` | `graph_based` | Keep. The platform environment uses social relationships, posts, comments, recommendations, traces, and dynamically updated relation networks. |
| `agent_accessible_representation` | `L3` | Keep. Agents receive recommended posts, user relations, feeds, and local interaction opportunities; there is no evidence that agents receive global network centrality, community structure, or full graph metrics. |
| `behavioral_scale` | `emergent_social_structure` | Keep. The paper studies information spreading, polarization, herd effects, misinformation spread, and newly formed relations. |
| `evidence_status` | `observed_effect` | Keep. The paper reports platform-level and group-scale outcome patterns, though not controlled spatial/configurational mediation. |

## Evidence Notes

OASIS simulates social media platforms such as X and Reddit. The environment server maintains users, posts, comments, relations, traces, and recommendations. Relation tables include follow and mutual relationships, and the database updates over time as agents post, comment, like, dislike, follow, and unfollow.

The agent-facing representation is local-relational and feed-mediated. In simulation, the environment and recommender system send agent information, posts, and user relations to agents; agents receive recommended posts and act on them. This is `L3`: local graph/feed exposure and interaction opportunities. It should not be coded as `L4` because the paper does not show that agents receive global abstract network measures such as centrality, community labels, structural holes, degree rankings as decision features, or whole-network summaries.

The observed-effect coding is supported by reported simulations of information propagation, group polarization, herd effects, scale effects, misinformation spreading, and newly established follow relations. These are observed social-platform outcomes in a graph-based digital environment. The claim should remain limited: OASIS reports platform/social-network dynamics, not Space Syntax-style spatial mediation.

## Page/Section Anchors

Use these anchors for manuscript support:

- Section 2.1, pages 3-4: workflow, environment server, RecSys, and agent actions.
- Figure 2, page 4: environment server sends posts and user relations; RecSys recommends posts; agents generate actions.
- Section 2.2-2.4, pages 4-6: environment database, recommendation system, agent module, and time engine.
- Section 3, pages 6-12: information propagation, polarization, herd effect, scale effects, misinformation spreading.
- Appendix method details, pages 22-25: user action prompts and environment-server database structure.

## Claim Boundary

Allowed manuscript use:

- OASIS is a strong example of graph-based digital social simulation with local/feed-mediated agent exposure.
- It supports `L3` local-relational coding in a digital social platform.
- It supports limited `observed_effect` claims for reported platform-level social outcomes.

Disallowed manuscript use:

- Do not code OASIS as `L4`; global social-network analysis and emergent relation graphs are researcher-side outputs unless shown as agent inputs.
- Do not treat recommendation exposure as Space Syntax configuration.
- Do not claim the paper proves spatial configuration shapes LLM-agent social behavior.
- Do not mix OASIS graph-platform effects with physical-space or geometry claims.

## Follow-Up

No acquisition action is needed. Current coding can remain `graph_based / L3 / observed_effect`.

