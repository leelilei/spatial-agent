# Table 2. Review Protocol Summary

Draft status: main-text table aligned to the 2026-05-01 closure baseline.

| Protocol element | Main-text summary | Appendix / source |
|---|---|---|
| Review type | Scoping review and structured evidence map, not an effect-size synthesis. | `paper/appendix/review_protocol.md` |
| Review aim | Map how LLM-agent systems expose space at the agent interface, what social-behavior scales they study, and what evidence status their results can support. | `paper/appendix/review_protocol.md` |
| Bibliographic screening | Phase 1 screening separates records into `Core`, `Adjacent`, `Foundational`, and `Excluded`; PRISMA-ScR reporting uses bibliographic counts. | `results/logs/prisma_summary.json` |
| Corpus roles | `Core` supports the main evidence map; `Adjacent` supports feasibility and boundary discussion; `Foundational` supports theory and transferable hypotheses. | `paper/appendix/review_protocol.md`; `docs/plans/claim_matrix.md` |
| Core layers | Stable widened Core distinguishes `anchor_core` from `bridge_core`; bridge rows extend coverage but do not carry the same evidential weight as the strict anchor nucleus. | `paper/appendix/review_protocol.md`; `docs/plans/claim_matrix.md` |
| Unit of analysis | Screening is paper-level; evidence-map coding is at the `system / environment configuration` level. Split-row families such as `Concordia` and `SimWorld` explain why `32` paper-level sources produce `34` coded rows. | `paper/appendix/review_protocol.md`; `paper/appendix/appendix_evidence_table.csv` |
| Spatial coding rule | Code what the agent can consume, not what the simulator stores, renders, or what the analyst computes after the fact. | `paper/appendix/review_protocol.md`; `paper/appendix/taxonomy_change_log.md` |
| Representation taxonomy | `L0` no spatial input; `L1` labels; `L2` semantic scene descriptions; `L3` local relations; `L4` global abstract structure; `L5` geometry or embodiment consumed by the agent. | `paper/figures/figure_3_l0_l5_taxonomy.svg`; `paper/appendix/review_protocol.md` |
| Evidence status | `designed_affordance_only` supports architecture/affordance claims; `observed_effect` supports limited reported-association claims; neither alone establishes strong causal mechanism. | `paper/appendix/review_protocol.md`; `docs/plans/claim_matrix.md` |
| Boundary handling | `HC01` is Adjacent / boundary / feasibility evidence. `TW-02` is a scope-boundary comparison. Neither enters the stable widened-Core evidence map. `BK02` remains source-note-only bridge evidence until full text is acquired or the row is downgraded. | `paper/appendix/adjudication_memo.md`; `assets/survey_paper/phase1/phase1_tw02_scope_decision_2026-04-28.md`; `assets/survey_paper/evidence_closure/global_consistency_check_2026-05-01.md` |
| Current stable baseline | Strict anchor baseline: `17` paper-level sources and `19` rows. Stable widened Core: `32` paper-level sources and `34` rows, with `19` `anchor_core` rows and `15` `bridge_core` rows. The 2026-05-01 closure check leaves only `BK02` unresolved as source-note-only bridge evidence. | `paper/appendix/appendix_evidence_table.csv`; `paper/tables/table_3_core_evidence_map.md`; `assets/survey_paper/evidence_closure/global_consistency_check_2026-05-01.md` |

Caption: Table 2 summarizes the review protocol needed to read the evidence map. The key distinction is between bibliographic screening counts and row-level evidence-map counts. The latter use `system / environment configuration` as the unit of analysis and code agent-accessible spatial representation rather than backend richness.
