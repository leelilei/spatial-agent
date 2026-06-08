# L4R-01 Closure Card - Network Formation among Multi-LLMs

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `L4R-01`

Paper: Papachristou and Yuan 2025, *Network Formation and Dynamics Among Multi-LLMs*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_adjacent/11_L4R-01_Network_Formation_LLMs_Papachristou2025.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_adjacent/11_L4R-01_Network_Formation_LLMs_Papachristou2025.fulltext.md`
- Extraction status: `pdfplumber`, `48` pages, `status: ok`, `text_char_count: 117884`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `bridge_core` | Keep. The study is a digital social-network simulation rather than a physical or navigable spatial-social environment. |
| `environment_side_representation` | `graph_based` | Keep. The operative environment is a dynamic social/professional network with nodes, edges, candidate links, neighborhoods, and graph statistics. |
| `agent_accessible_representation` | `L4` | Keep, but only under the widened digital-network bridge rule. Network structure is part of the LLM decision input, including neighbors, node degrees, common connections, and in small-world experiments current network structure. |
| `behavioral_scale` | `emergent_social_structure` | Keep. The paper studies link formation and emergent network properties such as preferential attachment, triadic closure, homophily, community structure, and small-world effects. |
| `evidence_status` | `observed_effect` | Keep. The paper reports generated network outcomes, fitted choice-model effects, robustness checks, and a human baseline comparison. |

## Evidence Notes

The paper simulates multiple LLM agents making network-formation choices in synthetic and real-world network settings. Agents act in separate conversational threads and make link choices over candidate nodes. This qualifies as a widened digital-social bridge case, not as a physical-space or embodied simulation anchor.

The key L4 evidence is agent-facing representation. The methods section describes a query process where the LLM receives personal or network features of candidate alternatives. Those features can include node neighbors, node degrees, common connections with the query node, and community memberships, formatted as JSON. The prompt examples show profile and candidate-profile JSON blocks with neighbor lists, and the feature-representation section gives JSON-like examples for preferential attachment, triadic closure, homophily, and small-world prompts.

This is stronger than `L3` local exposure because the agent is not merely told about nearby actors or a local feed. It can receive abstract network topology and structural descriptors as explicit decision features. It is also different from analyst-side graph metrics in `BK07` or `BK08`: here the topology-relevant information is part of the input used to choose new links.

The small-world experiment is the strongest boundary case for `L4`. In that setting, the altered Watts-Strogatz process rewires edges by querying the LLM with all nodes and each node's neighbors, i.e. the current network structure. The paper also contrasts full topological information with degree-only prompts and reports different emergent structures, reinforcing that the agent-facing representation matters.

The observed-effect coding is supported by reported emergence of preferential attachment, triadic closure, homophily, community structure, and small-world-like network properties across models, temperatures, and contextual prompts. The real-world network experiments further model LLM link choices using degree, attribute similarity, and common-neighbor terms; the human-baseline survey compares LLM and human choices under matched candidate-profile inputs.

## Page/Section Anchors

Use these anchors for manuscript support:

- Abstract and Introduction, pages 1-2: study purpose, multiple LLM agents, synthetic and real-world network settings, micro-level and macro-level network properties.
- Results, pages 3-6: preferential attachment, degree distributions, triadic closure, homophily, community structure, and small-world outcomes.
- Section A.1.1, page 25: network formation process, candidate alternatives, network features, JSON-formatted input, and JSON output.
- Section A.1.2-A.1.3, pages 25-27: prompt template and feature representations for neighbors, common neighbors, homophily attributes, and small-world inputs.
- Section A.2, page 28: small-world rewiring in which the LLM receives all nodes and each node's neighbors as the current network structure.
- Section A.3, pages 29-30: real-world network experiments, candidate set construction, and structural features used in link-formation decisions.
- Human baseline, pages 17 and 31-32: matched human and LLM candidate-profile decision tasks.

## Claim Boundary

Allowed manuscript use:

- Use `L4R-01` as the single admitted widened-Core example that reaches `L4` through agent-facing global or semi-global abstract graph structure.
- Use it to support the claim that `L4` is technically possible for LLM agents when network topology is exposed as decision input.
- Use it in Table 4 and Figure 3/Figure 4 only with a clear widened-bridge qualifier.
- Use it to explain the distinction between environment-side graph structure, analyst-side graph metrics, and agent-accessible graph representation.

Disallowed manuscript use:

- Do not treat `L4R-01` as evidence that `anchor_core` physical or navigable virtual environments contain `L4` cases.
- Do not describe it as Space Syntax, configurational urban morphology, direct geometry, or embodied spatial perception.
- Do not generalize from this single bridge row to claim that L4 is common.
- Do not use its observed network outcomes as proof that physical spatial configuration affects LLM-agent social behavior.

## Follow-Up

No acquisition action is needed. The row can remain `bridge_core / graph_based / L4 / observed_effect`, with the manuscript caveat that `L4` appears only in the widened digital-network bridge layer and remains absent from the stricter anchor-core spatial-social nucleus.
