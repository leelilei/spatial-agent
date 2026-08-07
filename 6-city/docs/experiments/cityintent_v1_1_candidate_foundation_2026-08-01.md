# CityIntent v1.1 true-benchmark foundation — 2026-08-01

## Outcome

CityIntent now has a reproducible benchmark-construction pipeline, but it is
correctly labelled a candidate rather than a released benchmark. The pipeline
generated five topology-distinct worlds and 144 split-fixed candidate items,
then used calibration evidence to reject the shortcut of treating generated
scale as accepted benchmark scale.

## Candidate matrix

- Worlds: 5 (3 public, 2 organizer-only).
- Topologies: dense grid, radial transit, sparse polycentric,
  bottleneck crossing, and mixed irregular.
- Items: 144 candidates.
- Splits: examples 24, development 36, public test 36, private test 48.
- Constructs: 8, exactly 18 candidates each.
- Provisional difficulty: easy/medium/hard, 48 each.
- Structural validation: pass, including 788 critical-location reachability
  checks and complete metric/architecture coverage.

## Calibration run

Command:

```bash
python tools/run_baseline_traces.py \
  --benchmark-config v1_1/benchmark_config.json \
  --agents utility_planner,llm_direct_actor,reactive_replanner,memory_reflection \
  --results-dir ../../../results/cityintent_v1_1_candidate/baseline_4x144_2026-08-01
```

All 576 expected traces completed. Mean task completion was 0.700 for the
direct-actor proxy and 0.886 for each of the three planner variants. The item
audit found:

- 87 candidates at all-baseline ceiling;
- 7 candidates at all-baseline floor;
- 101 candidates with provisional task-score range below 0.15.

These results are acceptance blockers, not paper results. Every item also
requires deterministic oracle and mechanism-matched negative-control evidence.
Migrating the 15 existing hand-authored oracle templates produced evidence for
71 instances: only 31 remained oracle-winnable on the changed topologies, and
18 of 32 instances with an available matched negative retained headroom >=
0.15. Eight candidates pass all currently implemented automated item gates.
They are still not labelled accepted until the remaining release-level gates
and calibration protocol are complete; consequently `accepted_count` remains
0. The 40 oracle failures are direct evidence that a new topology cannot be
treated as a harmless name substitution.

## Infrastructure added

- deterministic world and scenario generators with provenance and hashes;
- fixed split manifest and private-asset leakage audit;
- organizer-only paths protected from normal git inclusion;
- strict JSONL submission schema;
- evaluator-side action replay that rejects self-reported metrics;
- macro construct-world scoring;
- leak-checked public candidate archive containing 96 public items;
- clean-extraction regeneration and validation test.

## Decision

Do not run more large model matrices on the current 144 candidates. First
replace or reparameterize non-discriminating items and implement item-level
oracles and matched negative controls. The benchmark reaches publishable scale
only after 144 items pass those gates; generated count alone is insufficient.
