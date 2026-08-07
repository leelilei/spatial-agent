# CityIntent v1.1 — Wave-4 offline construction (2026-08-06)

Status: **offline construction complete; public six-system calibration not yet run.**
Release accepted count remains **0/144**. Registry remains 24 templates / 72 public instances.

## What Wave-4 closes

Wave-4 supplies the **fourth** independent public mechanism for each of the eight
construct families, which is the last item in the public construction gap
recorded in `docs/plans/cityintent_v1_1_mechanism_expansion_roadmap_2026-08-05.md`.
After its calibration passes, each construct reaches 4 mechanisms × 3 public
worlds = 12 public instances.

## Mechanisms

Generated from the versioned design contract
`v1_1/native_pilot/wave4_mechanism_design.json` by
`v1_1/native_pilot/generate_expansion_wave4.py`.

| Construct | Wave-4 mechanism | State transition |
|---|---|---|
| disruption_recovery | `temporary_service_outage_with_timed_recovery_choice` | service goes down, later recovers; naive arrival lands inside the outage |
| time_window_scheduling | `minimum_duration_inside_nested_window` | broad arrival window contains a narrow interval needing a minimum accumulated dwell |
| resource_budget_allocation | `two_stage_inventory_commitment` | the first purchase decides whether the downstream service stays affordable |
| poi_availability_service_evidence | `referral_then_provider_service_chain` | a referral service unlocks a second provider service elsewhere |
| memory_conditioned_preference | `source_reliability_memory_arbitration` | two recalled memories conflict; the reliable-tagged source wins over the newer one |
| social_coordination_copresence | `message_acknowledgement_then_handoff` | acknowledgement authorises a timed physical handoff, not a generic meeting |
| multi_party_commitment | `sequential_two_party_relay` | evidence from the first timed meeting is carried into a second partner's meeting |
| compound_long_horizon | `credential_unlock_purchase_service_return_chain` | credential unlocks a labeled purchase, which unlocks a timed service before return |

Unlike Wave-3, these items are built directly on `pilot.base_scenario` rather than
by mutating a prior wave, because every mechanism introduces a state transition
with no Wave-2/Wave-3 counterpart. All timings are derived per world from actual
`shortest_path` legs, since travel varies sharply across the three public worlds
(e.g. market→gym is 11 min in metro_radial and 31 min in suburb_polycentric).

## Gates passed

| Gate | Result |
|---|---|
| generation | 24/24 candidates, 0 rejections, deterministic from generator + seed |
| oracle task completion | 24/24 at 1.0 |
| oracle trace feasibility | 24/24 at 1.0, zero violations |
| matched-negative headroom | 24/24, range **0.50–1.00** (threshold 0.15) |
| structural distinctness | 24/24 distinct from **all** prior pools (base, wave1, wave2, wave3) |
| blind observation contract | 24/24 `intent_only_v1`, `expose_verifier_conditions: false` |
| test suite | **88 passed** (was 79) |
| prior-wave regression | base 16, wave1 40, wave2 24, wave3 24, time_v7 24 — all still pass |

## New evaluator semantics

Seven of the eight mechanisms reuse evidence semantics implemented at the Wave-4
design kickoff. One was genuinely missing and was added:

- **`service_after_recovery`** — service evidence counts only when the action
  *completes* at or after a recovery instant, and no later than an optional
  deadline. Implemented in `tools/run_baseline_traces.py` with scoring, evidence
  listing, and a deterministic-planner branch that waits outside the venue
  (waiting inside a paid venue would itself be a violation).

## Negative-control audit, and one repair

Every matched negative was replayed condition-by-condition to confirm it fails
for its **mechanism** reason rather than an incidental one. This found a real
defect:

- `memory_conditioned_preference`'s negative bought coffee at a paid unreliable
  venue with a zero budget, so it failed on `budget_negative` — a money failure
  masquerading as an arbitration failure. Repaired by moving the unreliable
  source to a free venue and having the negative **recall both sources** and
  still arbitrate wrongly. The negative now fails only on
  `reliable_source_choice` / `study_session` / `reject_unreliable` and passes
  `recall_both_sources`, which is the sharp form of the test.

For `disruption_recovery` and `resource_budget_allocation` the violation *is* the
mechanism (`closed_location` from committing before recovery; `budget_negative`
from spending the claim on the decoy), so those were left as designed.

## Honest novelty caveats

The distinctness audit is structural, and it records two weaker claims rather
than hiding them:

- **`memory_conditioned_preference` introduces no new evidence type.** Its
  condition vocabulary matches prior memory items; novelty rests entirely on
  memory-seed content (reliable/unreliable source tagging) plus the arbitration
  rule.
- **`resource_budget_allocation`'s only previously-unused condition type is the
  generic `no_feasibility_violation`.** Its mechanism novelty rests on the
  affordability-breaking decoy parameterisation, not on new evidence semantics.

Both are genuine mechanisms, but they are distinct at the parameter/content
level rather than the evidence-type level. A reviewer is entitled to weigh those
two differently from the other six.

One design-contract wording correction: the time-window mechanism said
"uninterrupted duration", but `dwell_within_window` **sums** overlapping dwell
intervals. The contract now says "accumulated", because the evaluator is the
source of truth.

## Artifacts

- generator: `v1_1/native_pilot/generate_expansion_wave4.py`
- design contract: `v1_1/native_pilot/wave4_mechanism_design.json`
- candidates: `v1_1/native_pilot/expansion_wave4/scenarios/` (24)
- oracle/negative plans: `v1_1/native_pilot/expansion_wave4/oracle_negative_plans.json`
- acceptance report: `v1_1/native_pilot/expansion_wave4/acceptance_report.json`
- distinctness audit: `v1_1/native_pilot/expansion_wave4/distinctness_audit.json`
- distinctness tool: `v1_1/native_pilot/audit_wave4_distinctness.py`
- rejection log: `v1_1/native_pilot/expansion_wave4/rejection_log.json` (empty)
- status: `v1_1/native_pilot/expansion_wave4/offline_construction_status.json`
- tests: `tests/test_wave4_generation.py`, `tests/test_wave4_evaluator_conditions.py`

## What remains

Public six-system calibration (3 models × 2 policies × 8 constructs × 3 worlds =
144 actor traces) has **not** been run — it needs a paid provider and explicit
authorization. Until it passes the cross-world promotion gate, Wave-4 is
candidate evidence only: the registry stays at 24 templates / 72 public
instances and the release accepted count stays 0/144.

Private-world actors remain unrun by design.
