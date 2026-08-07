# CityIntent v1.1 native multi-model calibration — 2026-08-03

## Purpose

Test whether an oracle-first scenario pipeline can produce fair native v1.1
items, and whether those items discriminate real model-policy systems before
expanding to the 144-item release target.

This is a one-run calibration pilot. It is not a leaderboard result and no
inferential significance claims are made.

> Superseded protocol warning (2026-08-04): actor observations in this run
> exposed evaluator-side success conditions, and ReAct received additional
> verifier-derived hints. Retain this run only as a leakage diagnostic. Use
> `cityintent_v1_1_blind_observation_calibration_2026-08-04.md` for the repaired
> intent-only calibration.

## Design

- Eight construct families, one public item per construct in the model matrix.
- Three Yunwu actor backbones: Claude Sonnet 4.5, Qwen3 235B A22B Instruct,
  and DeepSeek v4 Flash.
- Two shared policies: ReAct tool policy and Plan-and-Execute.
- FHL gpt-5.4-mini as the secondary soft plausibility judge.
- Deterministic verifier metrics remain primary.

Before model execution, a 16-item native pilot pool (two items per construct)
passed the two-sided gate: oracle task completion 1.0, feasibility 1.0, zero
violations, and matched-negative headroom at least 0.15.

## Completion

- Yunwu actor traces: 48/48.
- FHL judgments: 48/48.
- Provider interruptions: multiple Yunwu TLS/DNS failures; all completed
  episodes were preserved and missing episodes resumed without overwrite.

## Aggregate deterministic results

| model | policy | task | feasibility | constraint |
|---|---|---:|---:|---:|
| Claude | PlanExec | 1.000 | 1.000 | 1.000 |
| Claude | ReAct | 0.956 | 1.000 | 1.000 |
| DeepSeek | PlanExec | 0.919 | 0.975 | 0.875 |
| DeepSeek | ReAct | 1.000 | 1.000 | 1.000 |
| Qwen | PlanExec | 1.000 | 1.000 | 1.000 |
| Qwen | ReAct | 1.000 | 0.940 | 0.750 |

The Qwen ReAct cell demonstrates why task completion cannot stand alone: it
finishes every task while only half of traces are fully feasible and its mean
constraint satisfaction is 0.75.

## Soft-judge diagnostics and cost

| model | policy | trace believability | face-to-belief gap | calls | total tokens |
|---|---|---:|---:|---:|---:|
| Claude | PlanExec | 0.776 | 0.129 | 8 | 38,743 |
| Claude | ReAct | 0.919 | 0.036 | 51 | 283,809 |
| DeepSeek | PlanExec | 0.909 | 0.045 | 8 | 49,505 |
| DeepSeek | ReAct | 0.829 | 0.113 | 55 | 304,033 |
| Qwen | PlanExec | 0.795 | 0.115 | 8 | 35,672 |
| Qwen | ReAct | 0.729 | 0.140 | 64 | 332,033 |

ReAct uses roughly 6–9 times the tokens of PlanExec in this pilot. Soft judge
scores remain diagnostic and are not mixed into the official task score.

## Item decision

Across all six real model-policy systems:

- compound long-horizon range: 0.35;
- social coordination range: 0.65;
- the other six items: range 0.00 and all-system task ceiling;
- no item is at all-system floor.

The pilot therefore validates the oracle-first infrastructure but rejects six
of eight templates as leaderboard items in their current form. They may remain
examples or mechanism checks. The next accepted-pool generator must combine
their core constructs with deadlines, budgets, evidence requirements, or
multi-stage commitments while regenerating oracle and matched negative traces.

## Reproducible artifacts

- `v1_1/native_pilot/generate_native_pilot.py`
- `v1_1/native_pilot/verify_native_pilot.py`
- `v1_1/native_pilot/run_multimodel_pilot_resilient.sh`
- `v1_1/native_pilot/analyze_multimodel_pilot.py`
- `results/cityintent_v1_1_candidate/native_pilot_multimodel_analysis_2026-08-03/`
