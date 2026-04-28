# Evidence Map

Draft status: scaffold aligned to the widened-Core baseline dated 2026-04-28.

This section maps how current LLM-agent systems represent space at the agent interface, what kinds of social behavior they study, and what kind of evidence they actually provide. It does not argue that configurational spatial structure has already been robustly shown to shape LLM-agent social behavior. Instead, it establishes the current coverage, the current absences, and the current evidential limits of the coded corpus.

[Figure 2 about here: PRISMA-ScR flowchart]

[Table 2 about here: review protocol summary]

[Figure 3 about here: L0-L5 taxonomy]

[Table 3 about here: widened-Core evidence map]

[Table 4 about here: environment-side vs agent-accessible examples]

## 3.1 Review Protocol Summary

We frame this paper as a scoping review rather than as an effect-validation study. The goal of the evidence map is therefore descriptive and gap-oriented: to show which kinds of agent-accessible spatial representation currently appear in the literature, which kinds of social behavior are studied alongside them, and what kinds of claims the available evidence can safely support. Full protocol details, coding rules, and adjudication materials belong in Appendix A; this section should keep only the protocol elements needed to read the evidence map.

The review operates with three corpus roles. `Core` papers form the main coded corpus for the evidence map. `Adjacent` papers provide feasibility and boundary evidence about whether current models may be able to process richer spatial inputs. `Foundational` papers provide Space Syntax theory, physical-space empirical findings, and transferable hypotheses, but they do not count as direct evidence about LLM-agent social behavior. Within the current widened-Core operating rule, the main coded corpus is further separated into `anchor_core` and `bridge_core`. The `anchor_core` layer is the strict nucleus, while the `bridge_core` layer retains socially and spatially meaningful bridge cases inside the widened scope without treating them as equal in evidential weight to the strict nucleus.

At the screening stage, papers are judged bibliographically, but at the evidence-map stage the unit of analysis is the `system / environment configuration` rather than the paper as a whole. This matters because several families expose more than one agent-facing spatial interface, and some systems require split rows to avoid collapsing text-mediated and geometry-bearing configurations into a single coding decision. The split treatment of SimWorld is one example of why this system-level unit is necessary.

As of 2026-04-28, the strict baseline contains `17` paper-level `anchor_core` items and `19` coded rows. The stable widened Core contains `32` papers and `34` coded rows, made up of `19` `anchor_core` rows and `15` `bridge_core` rows. `HC01` is kept as Adjacent/boundary evidence rather than counted in the stable widened Core, and `TW-02` is intentionally excluded from the stable widened Core and retained only as a scope-boundary contrast case. Before prose freeze, the final PRISMA-ScR counts and flow figure should be synchronized with the latest screening exports and appendix assets.

Drafting note:

- Keep the protocol summary short here.
- Point readers to Appendix A for the full review protocol, adjudication memo, and taxonomy change log.
- Do not let this subsection turn into a methods chapter; its job is to orient Figure 2 and Table 2.

## 3.2 Spatial Representation Taxonomy: L0-L5

The evidence map uses an agent-facing taxonomy of spatial representation. The key distinction is between `environment-side representation` and `agent-accessible representation`. A system may run on a 3D engine, GIS substrate, or graph backend while still exposing only sparse textual location labels or local relational summaries to the agent. For that reason, the taxonomy below codes what the agent actually receives, not what the environment internally stores.

At the low end, `L0` indicates no spatial information, `L1` indicates place labels without explicit spatial relations, and `L2` indicates semantic or descriptive place information without explicit topology. `L3` captures local relational structure such as adjacency, co-presence, nearby agents, or limited movement options. `L4` is reserved for agent-facing global abstract structure that summarizes the broader environment beyond only local next-step relations. This includes classic configurational indicators such as `integration`, `depth`, `control`, or `choice`, but it is not limited to those labels. `L5` requires direct geometry, coordinates, embodiment, visual field, or physical constraints in a form that the agent actually consumes.

This distinction prevents two recurrent coding mistakes. First, a rendered 3D world should not automatically be treated as `L5`. Second, a system with graph-level analysis performed only by the researcher should not automatically be treated as `L4` unless that global structure is available at the agent interface. In other words, the taxonomy is not a ranking of technological sophistication; it is a measure of structural explicitness in the agent-facing spatial input.

Figure 3 should visualize this taxonomy with the agent-facing rule made explicit. The caption should also state that `L4` remains an underexplored design space rather than a mature, densely populated layer in the present literature.

Drafting note:

- Keep the full decision tree in Appendix A or the coding manual, not in the main body.
- Reuse the visual language from the exemplar guide, but keep the text here precise and brief.
- Mention that the widened-Core update broadened `L4` to global abstract agent-facing structure, not metric-name matching only.

## 3.3 Main Evidence Map

The widened-Core evidence map shows a literature that is still concentrated in local and mid-structure representations rather than in explicit configurational inputs. Across the stable widened Core, the coded distribution is `L1 = 1`, `L2 = 8`, `L3 = 18`, `L4 = 1`, and `L5 = 6`, for a total of `34` rows. By layer, the strict nucleus remains heavily concentrated in `L3`, with `15` of `19` `anchor_core` rows coded at that level, `3` rows reaching `L5`, and no `anchor_core` rows reaching `L2` or `L4`. The bridge layer broadens the map by adding `8` `L2` rows, `3` additional `L5` rows, and the only admitted `L4` row.

The evidence-status distribution is slightly more favorable than in the earlier strict slice but still far from decisive. The stable widened Core contains `19` `observed_effect` rows and `15` `designed_affordance_only` rows. This means the literature is no longer dominated only by untested design claims, yet the observed-effect material is still unevenly distributed across representation levels and core layers. In particular, the widened bridge layer contributes important recovery in thin slices, but those recovered slices should not be described as if they reflect a settled field-level consensus.

Table 3 should be the central artifact of this section. Its surrounding prose should do three jobs. First, it should identify where the corpus is actually dense: mostly `L3`, with some `L5`, and very limited `L1` or `L2` coverage in the strict nucleus. Second, it should distinguish strict and widened readings instead of collapsing them into a single field narrative. Third, it should clarify that the current literature contains more evidence about how space is included in systems than about whether configurational structure has already been validated as a driver of social behavior.

Safe synthesis sentences for this subsection:

- Most `anchor_core` systems expose agent-accessible spatial information at `L1-L3` rather than at configurational level.
- The widened-Core pass materially broadens `L2` and `L5` coverage, but that recovery is concentrated in bridge cases rather than in the strict nucleus.
- Observed spatial-behavior associations are present in the coded corpus, but they remain limited, heterogeneous, and uneven across representation levels.

Do not write here:

- that the field has already demonstrated configurational social mediation;
- that widened-Core recovery eliminates the original strict-gap interpretation;
- that `L5` or `L2` is now broadly established across the field.

## 3.4 The L4 Gap as an Underexplored Design Space

The most important result of the evidence map is not that `L4` is impossible, but that it remains extremely sparse even after widening the coded boundary. In the strict `anchor_core`, `L4` is entirely absent. In the stable widened Core, `L4` appears only once, in a single admitted digital-network bridge case: `L4R-01`, coded as `bridge_core / L4`. This is enough to show that configurational or globally abstract agent-facing structure is not logically outside the design space, but it is nowhere near enough to support a claim that the field has already operationalized it in any systematic way.

This point is where strict and widened readings must be stated side by side. The strict reading is that `L4` is absent from the anchor nucleus. The widened reading is that once the bridge layer is opened, one admitted bridge case reaches `L4`, while another upper-bound pressure case, `TW-02`, remains outside the stable widened Core because it falls beyond the accepted spatial-social bridge scope. The right interpretation is therefore neither "there is no `L4` at all" nor "the `L4` gap is solved." The right interpretation is that `L4` remains a highly underexplored design space, with only minimal admitted evidence at the widened boundary.

This subsection should also clarify why nearby cases do not automatically count as `L4`. `BK07` and `BK08`, for example, remain `L3` despite global network or community metrics appearing in the study, because those metrics appear to function as researcher-side analysis rather than as agent-facing global abstract input. This distinction matters because the survey is about what the agent can actually use, not what the analyst can compute afterward.

Safe synthesis sentences for this subsection:

- `L4` remains absent from the strict anchor core.
- Within the widened Core, `L4` appears only in a single admitted bridge case.
- Configurational agent-facing representation remains highly underexplored in current LLM-agent social simulation.

## 3.5 Environment-Side Richness vs Agent-Accessible Structure

One recurring pattern in the corpus is that environment-side richness often overstates what the agent actually receives. The widened-Core map contains `17` rows with `3D_engine` backends, `9` `graph_based` rows, `5` `2D_grid` rows, and `4` `text-only` rows. Yet these backend counts do not translate directly into higher agent-facing representation levels. Several apparently rich environments still expose only local, categorical, or prompt-mediated spatial summaries to the agent.

Table 4 should make this mismatch concrete. `Project Sid` and `MineLand` are useful positive examples because they expose geometry-bearing or embodied information at the agent interface and can therefore justify `L5`. By contrast, the real-world community-oriented HD social simulation row remains `L3` despite a GIS/BIM/Unreal backend, because the exposed observation fields remain categorical and prompt-mediated. `SimWorld` is especially useful because its split rows show how the same family can expose both a geometry-bearing interface (`HC12A`, `L5`) and a scene-graph or abstract-layout interface (`HC12B`, `L3`). `HC14` provides a further cautionary example: a GIS-derived road network does not become `L5` if the agent still receives only textual status summaries, nearby communications, and prompt-mediated route context.

This environment-versus-interface gap is analytically important for two reasons. First, it explains why "3D" should not be treated as a shortcut for "structurally rich spatial input." Second, it clarifies why the survey centers agent-accessible representation rather than visual fidelity or simulator complexity. The missing ingredient in much of the literature is not environment richness in itself, but the explicit transfer of global or geometry-level structure into the agent's decision interface in a form that can be tied to social behavior claims.

Drafting note:

- Use Table 4 here, not a long abstract explanation.
- Keep the examples concrete and row-specific.
- This subsection should set up Section 4 by showing why richer backends do not automatically answer the feasibility question.

## 3.6 Transition to the Next Sections

Taken together, the evidence map supports three conclusions that should carry forward into the rest of the paper. First, current LLM-agent social simulations are concentrated at local or mid-structure spatial interfaces, especially `L3`. Second, widened bridge cases broaden the representation landscape but do not erase the strict-gap interpretation, especially for `L4`. Third, the literature currently contains more evidence about how systems include space than about whether richer spatial structure has already been validated as a driver of social behavior.

These conclusions motivate the next three sections. Section 4 asks whether current models may be able to process richer configurational inputs if such inputs were provided. Section 5 examines how space is actually used in current social-simulation systems and where direct effect evidence remains thin. Section 6 then turns from description to evaluation by asking what would count as credible evidence for spatially mediated social behavior in future work.

Before prose freeze:

- sync this section with the final PRISMA-ScR export;
- ensure `appendix_evidence_table.csv` and any widened-Core table export match the `35`-row / `33`-paper baseline used here;
- cross-check every sentence against `docs/plans/claim_matrix.md`.
