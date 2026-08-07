# CityIntent v1.1 mechanism expansion roadmap — 2026-08-05

## Current evidence

The audited public calibration registry combines three independent mechanism
sources:

- base/time-v7: 8 mechanism templates, 24 public instances;
- Wave-2: 8 mechanism templates, 24 public instances.
- Wave-3: 8 mechanism templates, 24 public instances.

All 24 templates and 72 instances pass their source promotion gates. This is
calibration evidence only. The release accepted count remains 0/144.

## Construction gap

The release specification requires at least 18 accepted items per construct.
The fixed 144-item split layout allocates 12 public and 6 private items per
construct. The controlled expansion design therefore targets four independent
public mechanism templates per construct, each instantiated in the three public
worlds, plus three of those mechanisms transferred to each private world.

| quantity per construct | current | target | gap |
|---|---:|---:|---:|
| independent public mechanism templates | 3 | 4 | 1 |
| public calibration instances | 9 | 12 | 3 |
| private instances | 0 accepted | 6 | 6 |

## Next waves

Wave-4 must add one genuinely new mechanism for every construct family. Each
wave is generated from a versioned mechanism-specific builder,
instantiated in all three public worlds, and independently checked for schema,
reachability, oracle completion, matched-negative headroom, and public leakage.
Only after six-system public calibration and cross-world item gates pass may a
template be added to the registry.

Private instances remain organizer-only. They may receive deterministic oracle
and negative-control checks during construction, but private-world actors must
not run until a complete public mechanism set and the release governance gates
are ready.

The registry builder is:

`benchmarks/cityintent_v0/v1_1/build_calibration_registry.py`

It rejects scenario hash drift, duplicate payloads, non-public calibration
items, incomplete source manifests, and any attempt to count calibration
evidence as release acceptance.

## Wave-3 closure status (2026-08-06)

Wave-3 candidate generation is implemented at
`benchmarks/cityintent_v0/v1_1/native_pilot/generate_expansion_wave3.py`.
It emits 8 mechanism contracts × 3 public worlds (24 scenarios) with
machine-readable state transitions, required evidence, and negative-failure
definitions. The offline verifier passes 24/24 oracle traces and 24/24
matched negatives. A separate Wave-2/Wave-3 signature audit finds structural
deltas for 24/24 public candidates across events, success conditions, memory
contracts, or action evidence. The full benchmark test suite passes 74 tests.

Public calibration is complete across all three worlds: 144 final six-system
traces cover 24 items, with targeted reruns restricted to changed items. The
strict cross-world gate accepts 8/8 templates and 24/24 public instances. The
registry is updated to 24 templates / 72 public instances.

Private-world actors have not been run. Wave-3 remains calibration evidence,
not release acceptance; release accepted count stays 0/144. Wave-4 is the only
remaining public mechanism expansion before private transfer planning.

## Wave-4 design kickoff (2026-08-06)

The versioned design contract is
`benchmarks/cityintent_v0/v1_1/native_pilot/wave4_mechanism_design.json`.
It defines eight unique mechanisms and state transitions, each with explicit
novelty claims against Base, Wave-2, and Wave-3, required action/evaluator
evidence, and a matched-negative failure mode. The static design audit passes
8/8 constructs with no duplicate mechanism or transition.

Four evidence semantics are implemented with positive and negative tests:
dwell within a bounded window, ordered service/evidence chains, handoff
evidence, and ordered interaction chains. Scenario generation is now unblocked;
actor runs remain disabled until the 24-scenario oracle pool passes.

## Wave-4 offline construction complete (2026-08-06)

The 24-scenario oracle pool now exists and passes, so the generation gate is
closed. `generate_expansion_wave4.py` emits 8 mechanisms × 3 public worlds with
0 rejections; oracle task/feasibility are 1.0 with zero violations on all 24,
and matched-negative headroom spans 0.50–1.00. Distinctness is audited against
base, wave1, wave2 and wave3 together — a stronger check than the Wave-3
pairwise audit — and accepts 24/24. The suite passes 88 tests and every prior
wave re-verifies unchanged.

Two novelty caveats are recorded in
`expansion_wave4/offline_construction_status.json`: the memory mechanism adds no
new evidence type (its novelty is memory-seed content), and the resource
mechanism's only previously-unused condition type is the generic
`no_feasibility_violation`.

## Wave-4 calibration failed promotion (2026-08-06)

The 144-trace public calibration ran to completion on Apilio (Claude Sonnet 4.5 /
Qwen3-235B / DeepSeek-v4-flash × ReAct + PlanExec), with full coverage and no
missing cells. The cross-variant promotion gate accepted **1 of 8 templates**
(`multi_party_commitment`, 3/24 items).

The wave is too easy: system mean 0.87 versus Wave-3's 0.58, with system spread
0.28–0.39 versus Wave-3's 0.75–0.83. Compressed near ceiling, corrected
item-total correlation becomes unstable, so `comp`/`disr`/`soci`/`time` pass in
some worlds and fail in others (`r` from −0.311 to +0.920 for the same
mechanism). `memory_conditioned_preference` and `resource_budget_allocation` are
hard ceilings in all three worlds because their `private_intention` states the
answer rather than the goal — the same two mechanisms this roadmap's offline
audit had already flagged for weak novelty.

Registry stays at **24 templates / 72 public instances**; release accepted stays
**0/144**. The public construction gap is not closed.

Hardening plan before re-calibration:
1. Redesign `memo` (reliability inferable from source type, not an explicit
   `tagged reliable` label) and `reso` (drop the pre-warning so the decoy is a
   real tradeoff).
2. Raise global difficulty for the five variance-limited mechanisms so system
   spread recovers toward Wave-3's ~0.75.

Re-calibration is another 144 traces and needs fresh authorization. Details:
`docs/experiments/cityintent_v1_1_wave4_public_calibration_2026-08-06.md`.
