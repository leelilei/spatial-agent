# CityIntent v1.1 Wave-3 semantic review package — 2026-08-05

## Scope

Wave-3 contains 24 public calibration candidates: one proposed mechanism per
construct in each of the three public worlds. The candidates pass the offline
oracle and matched-negative checks, and the structural audit finds a delta for
all 24 candidates against the corresponding Wave-2 payloads.

This document began as a review package and now records the final public
calibration decision. The machine-readable review record is:

`benchmarks/cityintent_v0/v1_1/native_pilot/expansion_wave3/semantic_review.json`

## Preliminary findings

The strongest candidate distinctions are route-closure recovery, irreversible
reservation, registry-evidence chaining, two-step memory recall, and the gated
medication-pickup chain. Social coordination and multi-party commitment include
explicit public update events whose ordering semantics are enforced by the
evaluator.

## Governance status

- Wave-3 final public actor matrix: 144 traces complete.
- Private-world actors: not run.
- Calibration registry: 24 templates / 72 public instances.
- Release accepted count: 0/144.
- Promotion status: `public_calibration_promoted_not_release`.

All eight Wave-3 templates and all 24 public instances pass the cross-world
promotion gate. This does not authorize release or private-world actor runs.

## Public actor smoke attempt

The social and multi-party event-ordering contracts were made executable in
the evaluator and the offline gate was rerun successfully at 24/24. A minimal
public-only smoke was then attempted on one social scenario with two policies
and the three planned Yunwu models.

The initial Yunwu attempt was interrupted by four connection failures. After
the endpoint recovered, the same resume-safe runner completed all six planned
traces: two policies over Claude, Qwen, and DeepSeek.

All three ReAct traces completed the task; all three Plan-and-Execute traces
failed after committing to a stale or incorrect venue before the public
update. Task completion is therefore 0.5 overall with a 1.0 policy range. This
is promising mechanism-level discrimination, but a one-scenario smoke is not
promotion evidence. The next gate is six-system public calibration across all
three worlds. The runner is:

`benchmarks/cityintent_v0/v1_1/native_pilot/run_wave3_public_smoke_resilient.sh`

## Public v0 six-system calibration

The first full public-world batch completed 48 traces: eight constructs, two
policies, and three models. Existing Yunwu Claude and Qwen traces were retained
without rerunning. Yunwu completed six DeepSeek traces before its account quota
was exhausted; Apilio supplied only the ten missing DeepSeek trace keys. The
deterministic merge reported no duplicates.

All eight final v0 items have six-system coverage and discriminate. No item is
at ceiling or floor. Mean task completion ranges from 0.500 to 0.847, observed
system ranges from 0.500 to 1.000, and corrected item-total correlations from
0.397 to 0.990. Thus 8/8 pass the numerical item thresholds.

## Public v1 six-system calibration

The v1 Apilio batch completed 48/48 traces. Initial analysis identified local
failures in compound corrected correlation, resource evidence labeling and
correlation, and an overly easy time window. Hardening was restricted to those
three items; the remaining 30 traces were retained.

The final v1 archive has 48 unique traces and 8/8 items pass. Mean task
completion spans 0.458–0.704, observed ranges 0.588–1.000, and corrected
item-total correlations 0.764–0.987. The resource item now requires an
irreversible reservation after a public 10:10 price update, replacing the
previous service-label confound with an executable resource-state transition.

## Public v2 and cross-world closure

The v2 Apilio batch completed 48/48 traces. The resource mechanism was then
made consistent across all three worlds: the public update reveals the
reservation location, the reservation token is a core outcome, and training
and return remain downstream obligations. Only the three resource items were
rerun for this final contract.

The final v2 items pass with mean task completion 0.333–0.833, ranges
0.500–1.000, and corrected correlations 0.411–0.988. The final cross-world
audit accepts 8/8 Wave-3 templates and 24/24 public instances. The calibration
registry is updated to 24 templates and 72 public instances. Release accepted
count remains 0/144.
