# CityIntent v1.1 blind-observation calibration — 2026-08-04

## Status

This is benchmark-construction evidence, not a leaderboard result. The earlier
48-trace native pilot exposed evaluator-side `success_conditions` to actors;
ReAct additionally received verifier-derived unfinished conditions and next
actions. Those scores are retained as a leakage diagnostic and must not be
reported as benchmark performance.

## Protocol repair

- v1.1 scenarios now use `observation_contract=intent_only_v1` and
  `expose_verifier_conditions=false`.
- Direct, ReAct, and PlanExec observations hide evaluator condition objects.
- ReAct no longer receives verifier-derived condition status or action hints.
- PlanExec sees only public events observable at episode start, not future
  public events.
- Evidence labels normalize case and separator formatting, so `check_in`,
  `check-in`, and `check in` are equivalent while semantically different
  services remain distinct.
- Run manifests now record hashes for every scenario, the scenario matrix,
  worlds, and benchmark config; resume rejects content drift.

All 16 native items continue to pass oracle and matched-negative gates. The
regression suite contains 67 passing tests.

## Blind-v1 calibration

The run completed 45/48 actor traces before sustained Yunwu TLS/DNS failures:
Claude 16/16, Qwen 16/16, and DeepSeek 13/16. Missing traces are not imputed.
Hard scores were replayed from saved actions after separator normalization.

| construct | systems observed | mean task | min | max | range |
|---|---:|---:|---:|---:|---:|
| compound long horizon | 6/6 | 0.767 | 0.650 | 1.000 | 0.350 |
| disruption recovery | 6/6 | 1.000 | 1.000 | 1.000 | 0.000 |
| memory-conditioned preference | 6/6 | 1.000 | 1.000 | 1.000 | 0.000 |
| multi-party commitment | 6/6 | 0.533 | 0.000 | 1.000 | 1.000 |
| POI/service evidence | 6/6 | 1.000 | 1.000 | 1.000 | 0.000 |
| resource/budget allocation | 6/6 | 0.750 | 0.500 | 1.000 | 0.500 |
| social coordination | 5/6 | 1.000 | 1.000 | 1.000 | 0.000 |
| time-window scheduling | 4/6 | 0.588 | 0.450 | 1.000 | 0.550 |

Four constructs discriminate and four remain ceiling. This replaces the old
conclusion that only two of eight items discriminate.

## Hardened-template diagnostics

The four ceiling templates were revised. A Claude 8-trace and Qwen 2-trace v2
diagnostic found two evaluator-design artifacts before the cross-model run was
continued:

- a valid library fallback was excluded from the disruption target set;
- natural service and purchase labels were narrower than the actor-visible
  intention.

Hardened v3 corrects these issues, adds a generic `purchase_at` evidence
condition, and strengthens the memory task by combining temporal memory,
current availability, and zero budget. All 16 v3 items pass two-sided gates.

## Final v4 calibration

Yunwu recovered and all 24 hardened-v3 traces completed. Combining these with
the four unchanged constructs produced a complete 48-trace, eight-item matrix.
An initial corrected item-total audit found the old time-window item negatively
correlated with the rest (`r=-0.499`): Qwen used `use_service`, while Claude and
DeepSeek used the equally valid `buy prescription` action. The verifier was
therefore measuring action-taxonomy preference.

v4 adds `obtain_at`, accepting either purchase or pickup-service evidence, and
replaces the second deadline with a narrow world-feasible arrival window. The
replacement completed 6/6 actor traces and passed the two-sided oracle gate in
both generated worlds.

Final blind-v4 results:

| construct | mean | range | corrected item-total r |
|---|---:|---:|---:|
| compound long horizon | 0.767 | 0.350 | 0.547 |
| disruption recovery | 0.500 | 1.000 | 0.898 |
| memory-conditioned preference | 0.833 | 1.000 | 0.476 |
| multi-party commitment | 0.533 | 1.000 | 0.541 |
| POI/service evidence | 0.500 | 1.000 | 0.626 |
| resource/budget allocation | 0.750 | 0.500 | 0.923 |
| social coordination | 0.792 | 0.625 | 0.839 |
| time-window scheduling | 0.667 | 0.500 | 0.550 |

Coverage is 48/48. All eight items discriminate, none is at ceiling or floor,
and all corrected item-total correlations are positive. The automated
promotion gate accepts 8/8 as a calibration seed pool using range >= 0.15,
corrected item-total correlation >= 0.20, mean task in [0.20, 0.90], full
six-system coverage, and the two-sided oracle gate. This is not yet the
144-item release benchmark.

## Cross-variant hardening (v5-v6)

The single-world v4 promotion was then challenged on the paired generated
world (`v1`). That replication exposed template overfitting that the seed
matrix alone could not reveal: the memory item returned to an all-system
ceiling and the POI item had negative corrected item-total correlation
(`r=-0.431`). Both failures were treated as generator defects, not as results
to average away.

v5 changed POI completion from a fixed named-place shortcut to service-at-
location evidence with a path-derived deadline. v6 added an explicit `recall`
action and `recall_memory` condition. Under `memory_access_contract=
recall_required_v1`, private preference memories are absent from the initial
observation and become actor-visible only after recall. This creates a genuine
closed-loop distinction: ReAct can use the retrieved value, while a fixed
PlanExec trajectory can request it but cannot retrospectively revise its plan.

The final v6 audit contains two independent 48-trace matrices (seed `v0` and
replication `v1`), each covering three models, two policies, and eight
constructs. Scores were replayed from actions under the current verifier.

| construct | v0 mean | v0 range | v0 r | v1 mean | v1 range | v1 r |
|---|---:|---:|---:|---:|---:|---:|
| compound long horizon | 0.767 | 0.350 | 0.570 | 0.708 | 0.350 | 0.472 |
| disruption recovery | 0.500 | 1.000 | 0.934 | 0.667 | 1.000 | 0.376 |
| memory-conditioned preference | 0.500 | 1.000 | 0.934 | 0.500 | 1.000 | 0.945 |
| multi-party commitment | 0.533 | 1.000 | 0.506 | 0.583 | 1.000 | 0.540 |
| POI/service evidence | 0.667 | 0.500 | 0.723 | 0.833 | 1.000 | 0.437 |
| resource/budget allocation | 0.750 | 0.500 | 0.949 | 0.583 | 1.000 | 0.775 |
| social coordination | 0.792 | 0.625 | 0.809 | 0.688 | 0.625 | 0.956 |
| time-window scheduling | 0.667 | 0.500 | 0.574 | 0.583 | 0.500 | 0.365 |

Both matrices have 48/48 coverage, 8/8 discriminating items, zero observed
ceilings/floors, and positive corrected item-total correlation for every item.
The weakest correlation is 0.365, above the preregistered calibration cutoff
of 0.20. The cross-variant promotion gate requires every construct to pass the
full item gate in both worlds; it accepts 8/8 templates and 16/16 instances as
the calibration template pool. The release-accepted count remains zero until
the planned 144-item expansion independently passes these gates.

## Expansion wave 1

The hardened templates were next instantiated once in each of all five city
topologies, yielding an oracle-first pool of 40 candidates (8 constructs x 5
worlds). All 40 pass schema/cross-reference validation, 130 reachability
checks, oracle task and feasibility at 1.0, and matched-negative headroom of at
least 0.15. The two private-world instances per construct were not exposed to
actor models; they remain oracle-only so model-driven item tuning does not
leak into held-out worlds.

The one new public-world instance per construct (`v2`) was calibrated through
Yunwu with Claude Sonnet 4.5, DeepSeek v4 Flash, and Qwen3-235B, using ReAct and
PlanExec. All 48/48 traces completed. Seven constructs pass the empirical item
gate in all three public worlds, contributing 21/21 accepted public
calibration instances. The time-window template is rejected because its v2
corrected item-total correlation is negative (`r=-0.202`).

Trace inspection locates the confound. The v2 destination is a paid cafe:
three failing systems dwell before purchasing, so their window presence is
invalid; the successful systems pay first. The item therefore rewards paid-
venue action ordering rather than isolating temporal scheduling. The verifier
is behaving as specified, and its score is not relaxed. A replacement time
template must remove this venue-protocol dependency and undergo a fresh model
run.

## Time-window v7 replacement

The rejected item was replaced without overwriting the historical v6 scenario
ids or hashes. Time v7 uses a free destination and a future public appointment
update: the agent must complete an initial prescription deadline, wait until
the update becomes observable, and then reach the announced venue during a
narrow window. The initial PlanExec observation cannot see the future event;
ReAct may condition later actions on it. This isolates closed-loop temporal
information use instead of paid-venue action ordering.

All three replacement scenarios pass schema, reachability, oracle completion
and feasibility, and matched-negative gates. The 18/18 Yunwu actor traces
completed and were substituted into three complete 48-trace matrices.

| public variant | mean task | range | corrected item-total r | decision |
|---|---:|---:|---:|---|
| v0 / metro radial | 0.573 | 1.000 | 0.798 | accepted |
| v1 / suburb polycentric | 0.646 | 0.563 | 0.831 | accepted |
| v2 / harbor grid | 0.812 | 0.563 | 0.761 | accepted |

The final three-public-world gate now accepts 8/8 templates and 24/24 public
calibration instances. Every item has six-system coverage and nonzero range;
none is at ceiling or floor. This closes the template-calibration phase but
does not change the formal release count, which remains 0/144.

## Artifacts

- `v1_1/native_pilot/analyze_blind_pilot.py`
- `v1_1/native_pilot/run_blind_multimodel_resilient.sh`
- `v1_1/native_pilot/run_hardened_v2_smoke_resilient.sh`
- `results/cityintent_v1_1_candidate/native_pilot_blind_v1_analysis_partial_rescored_2026-08-04/`
- `results/cityintent_v1_1_candidate/native_pilot_hardened_v2_smoke_2x4x1_2026-08-04_{claude,qwen}/`
- `results/cityintent_v1_1_candidate/native_pilot_blind_v4_composite_48_2026-08-04/`
- `results/cityintent_v1_1_candidate/native_pilot_blind_v4_analysis_48_2026-08-04/`
- `v1_1/native_pilot/calibration_promotion_manifest_v4.json`
- `results/cityintent_v1_1_candidate/native_pilot_blind_v6_seed_analysis_48_2026-08-04/`
- `results/cityintent_v1_1_candidate/native_pilot_blind_v6_replication_analysis_48_2026-08-04/`
- `v1_1/native_pilot/audit_cross_variant_promotion.py`
- `v1_1/native_pilot/calibration_cross_variant_promotion_manifest_v6.json`
- `v1_1/native_pilot/generate_expansion_wave1.py`
- `v1_1/native_pilot/expansion_wave1/acceptance_report.json`
- `v1_1/native_pilot/expansion_wave1/public_cross_variant_promotion_manifest.json`
- `results/cityintent_v1_1_candidate/native_expansion_wave1_public_v2_analysis_48_2026-08-04/`
- `v1_1/native_pilot/generate_time_v7_matrix.py`
- `v1_1/native_pilot/time_v7/public_matrix/acceptance_report.json`
- `v1_1/native_pilot/time_v7/public_matrix/public_cross_variant_promotion_manifest.json`
- `results/cityintent_v1_1_candidate/native_time_v7_public_v{0,1,2}_analysis_48_2026-08-04/`
