# Matched-policy integration ablation audit (2026-07-23)

## Decision

The strict selector ablation passes. On the same normalized candidate store, changing only the
conflict-resolution policy from mention frequency to maximum event version raises current
post-replay answers by 9.0 percentage points. The direction is positive in all eight independent
society streams.

This is a narrower result than the earlier GA-versus-PROV fixed-stream replay. It supports a
causal statement about the selector policy itself. It does not show that natural dialogue
supplies correct versions, and it does not identify the relative contribution of every component
in the complete GA and PROV pipelines.

## Design

- Source material: frozen per-agent streams reconstructed from the eight completed PROV societies,
  schedule seeds 41--48.
- Independent unit: one realized society stream / schedule seed.
- Sample: eight seeds, 25 agents per seed, 200 paired agent streams.
- Common pipeline in both conditions:
  - identical ordered event stream;
  - identical typed candidate records;
  - identical candidate store and no-op consolidation;
  - identical one-record retrieval budget;
  - identical context format;
  - identical interview system prompt and `gpt-5.4-mini` model;
  - identical current/stale/unknown marker scorer.
- Sole manipulation:
  - `frequency`: select the value with the largest number of candidate mentions, breaking a tie
    by latest arrival;
  - `version_max`: select the candidate with the largest event version, breaking a tie by latest
    arrival.

## Candidate normalization

The controlled task defines Saturday/front porch as version 0 and Sunday/community center as
version 1. Events carrying reconstructed provenance retain their explicit version. Text-only
events are added only when they unambiguously mention one of the two registered values; their
version is an analysis annotation from the controlled task definition. Text mentioning both
values without structured provenance is excluded as ambiguous.

Across all streams:

| Event disposition | Count |
|---|---:|
| Total received events | 5,412 |
| Explicit structured provenance candidates | 494 |
| Unambiguous text-annotated candidates | 556 |
| Ambiguous text excluded | 40 |
| Irrelevant text excluded | 4,322 |

This normalization makes the policy contrast isomorphic but is intentionally an oracle-coded
mechanism assay. It must not be described as an end-to-end natural-language provenance system.

## Results

| Selector | Current answers | Seed-level 95% CI |
|---|---:|---:|
| Mention frequency | 62.5% | 52.7--72.3% |
| Maximum version | 71.5% | 64.3--78.8% |
| Paired difference | +9.0 points | +4.4--+13.6 |

Per-seed differences were `+4, +8, +4, +8, +4, +20, +12, +12` percentage points.
Maximum-version selection was higher in 8/8 seeds; the exact two-sided sign-test result is
`p = 0.0078125`.

The 400 common-prompt LLM interviews exactly matched the selected symbolic state, so the
behavioral and state-level tables are identical. No provider failure was scored as unknown.

## Valid manuscript wording

Use:

> A strict matched-policy ablation retained the same candidate records, consolidation, retrieval
> budget, context format, and interview, changing only the conflict selector. Maximum-version
> selection yielded 71.5% current answers versus 62.5% for mention-frequency selection (paired
> difference +9.0 points, 95% CI 4.4--13.6; higher in 8/8 seeds; exact two-sided sign test
> p=.0078).

Also state:

> Versions assigned to unstructured claims were controlled-task annotations. The ablation tests
> the consequence of using a supplied version, not whether ordinary dialogue can infer or
> authenticate that version.

Do not use:

- "The complete PROV architecture differs from GA only in one rule."
- "The ablation proves that provenance is naturally available."
- "Version selection alone explains the full 28.5-point GA-versus-PROV replay gap."
- "The annotated streams are a deployment-ready provenance channel."

## Artifacts

- Runner: `sim/matched_policy_ablation.py`
- Aggregate: `sim/runs/matched_policy_ablation_2026-07-23/aggregate.json`
- Per-seed normalized candidates and selections:
  `sim/runs/matched_policy_ablation_2026-07-23/seed_*/prepared.json`
- Per-agent interview checkpoints:
  `sim/runs/matched_policy_ablation_2026-07-23/seed_*/checkpoints/`
