# Global Consistency Check

Date: 2026-05-01

Scope: manuscript-facing evidence-map assets after the evidence-closure card batch.

Primary source: `spatial-agent-survey/paper/appendix/appendix_evidence_table.csv`

Closure audit: `assets/survey_paper/evidence_closure/closure_audit_2026-05-01.md`

## Result

The manuscript-facing evidence map is internally consistent with the `2026-05-01 closure baseline`.

- Stable widened Core: `34` coded rows from `32` paper-level sources.
- Row layers: `anchor_core = 19`, `bridge_core = 15`.
- Closure cards: `33 / 34` rows are `C3 closed_card_done`.
- Remaining unresolved row: `BK02` remains `C0 acquire_or_downgrade` because it is source-note-only and lacks a local full text.
- Manuscript status lines should refer to the `2026-05-01 closure baseline`, not the earlier `2026-04-28 stable widened-Core baseline`.

## Verified Counts

| Check | Verified value |
|---|---:|
| coded rows | `34` |
| paper-level sources | `32` |
| `anchor_core` rows | `19` |
| `bridge_core` rows | `15` |
| `L1` rows | `1` |
| `L2` rows | `8` |
| `L3` rows | `18` |
| `L4` rows | `1` |
| `L5` rows | `6` |
| `observed_effect` rows | `19` |
| `designed_affordance_only` rows | `15` |
| `2D_grid` backends | `5` |
| `text-only` backends | `4` |
| `3D_engine` backends | `16` |
| `graph_based` backends | `9` |

## Claim Boundaries

- `L4` is absent from the strict `anchor_core`.
- The only admitted `L4` row is `L4R-01`, a widened digital-network `bridge_core` case.
- The correct `L4` claim is scarcity or underexploration, not absence across the full widened Core and not field-wide validation.
- `L5` rows are `HC06`, `HC12A`, `R3-01`, `BK06`, `R3-05`, and `TW-13`.
- Anchor `L5` rows can support embodied or geometry-bearing interface mapping, but they still do not establish general configurational mediation.
- Bridge `L5` rows require qualifiers: `BK06` is platform-like, `R3-05` is an embodied cooperation benchmark, and `TW-13` is a VR guidance/navigation system.
- `BK07` and `BK08` remain `graph_based / L3`; researcher-side network analysis does not make them `L4`.
- `HC11` remains `3D_engine / L2`; coordinate-like fields are treated as structured text-schema evidence rather than embodied geometry.
- `BK02` should not be used for strong manuscript claims until full text is acquired or the row is downgraded.

## Manuscript Writing Rules

- Use `anchor_core` for the strictest descriptive and gap claims.
- Use `bridge_core` to broaden design-space mapping, but keep bridge qualifiers visible.
- State observed effects as reported associations or outcomes, not as robust causal mechanisms.
- Do not convert backend richness into agent-facing representation level.
- Do not treat `3D_engine` as automatic `L5`.
- Do not treat graph metrics as `L4` unless the global structure is agent-facing.
- Preserve the distinction between bibliographic screening counts and row-level evidence-map counts.

## Checked Manuscript Assets

- `spatial-agent-survey/paper/sections/03_evidence_map.md`
- `spatial-agent-survey/paper/sections/04_feasibility.md`
- `spatial-agent-survey/paper/sections/05_social_simulation.md`
- `spatial-agent-survey/paper/sections/06_evaluation_dimensions.md`
- `spatial-agent-survey/paper/sections/07_research_agenda.md`
- `spatial-agent-survey/paper/appendix/review_protocol.md`
- `spatial-agent-survey/paper/tables/table_2_review_protocol_summary.md`
- `spatial-agent-survey/paper/tables/table_3_core_evidence_map.md`
- `spatial-agent-survey/paper/tables/table_6_space_syntax_proposition_transfer.md`
- `spatial-agent-survey/paper/tables/table_7_evaluation_dimensions.md`
- `spatial-agent-survey/paper/figures/figure_1_corpus_evidence_roles_spec.md`
- `spatial-agent-survey/paper/figures/figure_2_prisma_scr_flow_spec.md`
- `spatial-agent-survey/paper/figures/figure_3_l0_l5_taxonomy_spec.md`
- `spatial-agent-survey/paper/figures/figure_4_representation_distribution_spec.md`

## Next Work

- Resolve `BK02` through institutional access, author copy, downgrade, or exclusion before final manuscript freeze.
- Use this memo as the claim-boundary checkpoint when revising Sections 3, 5, 6, and 7.
- Resume paragraph-level drafting only with closure cards and this consistency memo as source of truth.
