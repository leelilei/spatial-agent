# Phase 1 Proxy Abstract Recheck

Date: 2026-04-28

Companion table:

- `assets/survey_paper/phase1/phase1_proxy_abstract_recheck_2026-04-28.csv`

Purpose: recheck the `28` rows whose abstracts were backfilled by proxy summary on `2026-04-28`, to determine whether any current screening or widened-Core decisions need to be reopened.

## Summary

Rechecked rows:

- `26` original candidate-pool rows
- `2` fresh L4-tilt rows
- `28` total proxy-backfilled rows

Outcome:

- `27` rows: `no_change`
- `1` row: upgraded from exclusion to background/adjacent relevance
- `0` rows: upgraded into active full-text recheck
- `0` rows: changed widened-Core, shortlist, or optimistic counts

## Main Finding

The backfilled abstracts do not justify a broad screening redo.

They do justify a narrow audit trail:

- almost all proxy-filled rows remain correctly excluded;
- one fresh L4 review article was previously marked `abstract_missing_exclude` only because the abstract was unavailable and should now be retained as `background_or_adjacent`;
- no proxy-backfilled row becomes a new widened-Core admission candidate.

## Candidate Pool Result

All `26` proxy-backfilled original-pool rows remain excluded.

Why:

- several are clearly outside scope even after abstract recovery, including ecology, geology, generic ML, or proceedings records;
- several are spatial-language, urban-form, or human-behavior papers that remain useful only as very broad background, not as target corpus rows worth reopening in the current workflow;
- none introduces a missed LLM-agent spatial-social system, a bridge-level VR/NPC case, or a clean L4 candidate.

Operational consequence:

- do not reopen the original `417`-record screening flow;
- do not expand the active shortlist from this proxy-backfilled subset.

## Fresh L4 Result

### FT-L4-078

`LLMs and generative agent-based models for complex systems research`

Decision:

- upgrade from `abstract_missing_exclude` to `abstract_background_or_adjacent`

Why:

- the abstract confirms real methodological relevance to LLM-plus-generative-ABM research;
- but the paper is still a review/methods overview rather than a primary spatial-social target system.

Use:

- retain as background or low-priority boundary material;
- do not move into widened-Core or active P1 recheck.

### FT-L4-111

`Retrieval-Augmented Generation (RAG)`

Decision:

- remain excluded

Why:

- the abstract confirms a general RAG methods paper, not a spatial-social LLM-agent system.

## Net Impact

Stable widened-Core remains:

- `35` rows
- `33` papers
- `L4` stable admitted rows remain `1`

Conclusion:

- yes, the proxy-filled subset was worth rechecking;
- no, it does not trigger a broad rescreen;
- the correct follow-up is to keep the recheck as an audit supplement and continue using the current widened-Core table as the stable corpus.
