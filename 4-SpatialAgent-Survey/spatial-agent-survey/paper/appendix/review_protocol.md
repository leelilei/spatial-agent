# Review Protocol

Draft status: protocol summary aligned to the 2026-05-01 closure baseline.

This appendix records the review protocol used to read the evidence map. It is a drafting scaffold for the manuscript appendix, not a new screening round.

## Review Type and Aim

This paper is framed as a scoping review. The goal is to map how LLM-agent systems expose space at the agent interface, what social-behavior scales they study, and what evidence status their reported results can support. The protocol is descriptive and gap-oriented rather than an effect-size synthesis.

## Corpus Roles

The review distinguishes three corpus roles:

- `Core`: systems used for the main evidence map.
- `Adjacent`: spatial reasoning, embodied, or boundary work used for feasibility and scope discussion.
- `Foundational`: Space Syntax, physical-space, and prior simulation work used for theoretical framing and transferable hypotheses.

Within the stable widened Core, rows are further separated into:

- `anchor_core`: the strict nucleus for the cleanest descriptive and gap claims.
- `bridge_core`: socially and spatially relevant bridge cases that extend the map without carrying the same evidential weight as the strict nucleus.

`HC01` is retained only as Adjacent / boundary / feasibility evidence. `TW-02` is retained only as a scope-boundary comparison and does not enter the stable widened-Core evidence map.

## Unit of Analysis

The screening stage operates at the paper level. The evidence map operates at the `system / environment configuration` level. This is why the stable widened-Core baseline contains `33` paper-level sources but `35` coded rows. Split-row families such as `Concordia` and `SimWorld` expose more than one agent-facing spatial interface and must not be collapsed into a single coding decision.

## Coding Fields

The main coded fields are:

- `core_layer`
- `admission_status`
- `corpus_tier`
- `shortlist_id`
- `system_name`
- `system_family`
- `paper_refs`
- `environment_side_representation`
- `agent_accessible_representation`
- `representation_gap_note`
- `behavioral_scale`
- `behavior_type`
- `evidence_status`
- `spatial_behavior_coupling`
- `evaluation_method`
- `space_syntax_construct`
- `local_artifact_path`
- `source_basis`

The central coding rule is that `agent_accessible_representation` codes what the agent can actually consume, not what the simulator, renderer, GIS backend, or analyst can compute.

## Spatial Representation Taxonomy

The review uses an agent-facing `L0-L5` taxonomy:

- `L0`: no spatial information.
- `L1`: place labels or action-space labels without explicit spatial relations.
- `L2`: semantic or descriptive place information without explicit topology.
- `L3`: local relational structure, including adjacency, co-presence, nearby agents, local movement options, feeds, or local graph exposure.
- `L4`: agent-facing global abstract structure beyond local next-step relations, including configurational or network-level structure when it is provided to agents.
- `L5`: geometry, coordinates, visual field, embodiment, or physical constraints directly consumed by the agent.

`3D_engine` does not automatically imply `L5`. Researcher-side centrality, community, or network analysis does not imply `L4` unless the global structure is part of the agent-facing input.

## Evidence Status Rules

Rows are coded conservatively:

- `designed_affordance_only`: space is part of the system design or interaction affordance, but the paper does not report a separated spatial-behavior relation.
- `observed_effect`: the paper reports some spatial-behavior association, difference, or outcome in the system. This does not by itself establish a strong causal mechanism.
- `hypothesized_but_not_tested`: the spatial-behavior link is proposed rather than evaluated.

When a row contains both design claims and observed outcomes, the manuscript should use the weaker applicable claim unless the spatial-behavior relation is directly reported.

## Current Stable Baseline

As of the 2026-05-02 closure baseline:

- strict baseline: `17` paper-level `anchor_core` sources and `19` coded rows;
- stable widened Core: `33` paper-level sources and `35` coded rows;
- row layers: `anchor_core = 19`, `bridge_core = 16`;
- representation distribution: `L1 = 1`, `L2 = 8`, `L3 = 19`, `L4 = 1`, `L5 = 6`;
- evidence status: `observed_effect = 20`, `designed_affordance_only = 15`;
- `L4` appears only in one widened digital-network `bridge_core` row and remains absent from the strict `anchor_core`.

The authoritative row-level appendix asset for this baseline is `appendix_evidence_table.csv`.
