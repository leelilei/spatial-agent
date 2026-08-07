# CityIntent v1.1 Wave-2 mechanism expansion — 2026-08-04

## Scope

Wave 2 adds one genuinely different mechanism per construct rather than
creating name- or world-only clones. Each mechanism is instantiated in all
three public worlds, producing 24 candidates. Private evaluation worlds remain
actor-model blind.

| construct | Wave-2 mechanism |
|---|---|
| disruption recovery | future destination relocation |
| time-window scheduling | ordered dual free-venue windows |
| resource/budget allocation | joint money and action-budget allocation |
| POI/service evidence | future service-registry update |
| memory-conditioned preference | environment-cued conditional memory |
| social coordination | confirmed meeting with future relocation |
| multi-party commitment | overlap requiring explicit renegotiation |
| compound long horizon | purchase, meeting, and return-home chain |

## Offline acceptance

The first generator attempt retained 23 items and passed 16/23 oracle gates.
Failures exposed a no-detour disruption edge, a closed bookstore, a one-minute
social oracle timing error, and a resource negative control with no headroom.
The rejection summary is retained under `expansion_wave2/rejection_logs/`.

After parameter repair, the 24-item matrix passes schema validation, 81
reachability checks, 24/24 oracle completion and feasibility, and 24/24
matched-negative headroom gates. The regression suite contains 68 tests.

## v0 empirical calibration

The first public-world matrix completed 48/48 Yunwu traces over Claude Sonnet
4.5, DeepSeek v4 Flash, and Qwen3-235B, each with ReAct and PlanExec. The first
model run correctly rejected four mechanisms: disruption and POI were at
ceiling, multi had corrected `r=0.157`, and resource was dominated by action-
label mismatch.

Two targeted hardening rounds were run only on changed families. Historical
traces remain archived. The final v0 matrix is:

| construct | mean | range | corrected item-total r | decision |
|---|---:|---:|---:|---|
| compound long horizon | 0.847 | 0.529 | 0.708 | accepted |
| disruption recovery | 0.500 | 1.000 | 0.942 | accepted |
| memory-conditioned preference | 0.428 | 1.000 | 0.975 | accepted |
| multi-party commitment | 0.271 | 0.875 | 0.515 | accepted |
| POI/service evidence | 0.500 | 1.000 | 0.942 | accepted |
| resource/budget allocation | 0.875 | 0.375 | 0.728 | accepted |
| social coordination | 0.500 | 0.750 | 0.784 | accepted |
| time-window scheduling | 0.750 | 0.500 | 0.954 | accepted |

Coverage is 48/48; all eight items discriminate, none is at ceiling/floor,
and the automated single-world gate accepts 8/8. This is seed evidence only.
The mechanisms were then replicated in public variants v1 and v2.

## v1/v2 replication checkpoint

The public replication completed 96/96 additional Yunwu traces. Together with
v0, Wave 2 now has 144/144 traces over three public worlds, three models, and
two policies. No private-world actor run was performed.

| world variant | traces | complete items | ceiling/floor |
|---|---:|---:|---:|
| v0 | 48/48 | 8/8 | 0/0 |
| v1 | 48/48 | 8/8 | 0/0 |
| v2 | 48/48 | 8/8 | 0/0 |

The first strict three-world audit accepted five of eight templates and 15/24
instances. Three localized failures remained:

| construct | failing instance | mean | range | corrected r | reason |
|---|---|---:|---:|---:|---|
| resource/budget | v1 harbor | 0.875 | 0.375 | 0.034 | weak item-total alignment |
| compound long horizon | v2 harbor | 0.912 | 0.529 | 0.443 | slightly too easy |
| time-window scheduling | v2 harbor | 0.917 | 0.500 | 0.387 | slightly too easy |

Disruption, memory, multi-party, POI, and social templates independently pass
in all three worlds. The pre-hardening audit is archived as
`public_cross_variant_promotion_manifest_pre_hardening.json`.

## Targeted hardening closure

The handoff's 18 targeted traces completed without rerunning the 21 unchanged
items: six v1-resource traces and twelve v2 compound/time traces. Deterministic
first-source merging rebuilt both 48-trace composites. The first post-handoff
audit still exposed three correlation failures: v1 resource (r=0.171), v2
time (r=-0.037), and the previously borderline v2 multi item (r=0.198).

Generator 1.0.3 therefore applies a final localized scoring repair. It raises
the weight of the indispensable training outcome in v1 resource, balances the
two ordered windows in v2 time, and gives explicit Casey renegotiation more
weight in v2 multi. Actor-visible intentions and world state are unchanged.
Actions were deterministically rescored. Resource and multi then passed, while
time remained low-correlation because one DeepSeek ReAct sample incorrectly
treated the direct 13-minute library-to-office route as a 34-minute detour and
abandoned at step one. A fresh six-system sample was collected for v2 time
only; the old failed sample remains archived.

Final hardened values are:

| construct/instance | mean | range | corrected r | decision |
|---|---:|---:|---:|---|
| v1 resource, harbor | 0.875 | 0.500 | 0.208 | accepted |
| v2 compound, harbor | 0.735 | 0.647 | 0.953 | accepted |
| v2 multi-party, suburb | 0.353 | 0.824 | 0.396 | accepted |
| v2 time-window, harbor | 0.666 | 0.563 | 0.866 | accepted |

The strict three-world audit now accepts 8/8 mechanism templates and 24/24
public instances. Every instance has six systems, range at least 0.15,
corrected item-total correlation at least 0.20, mean task in [0.20, 0.90], and
no ceiling/floor. All 24 scenarios still pass oracle and matched-negative
verification, and the full regression suite passes 68/68. Private-world actors
were never run. This promotes a calibration template pool; it does not create
the 144-item release benchmark, whose accepted count remains 0/144.

## Artifacts

- `benchmarks/cityintent_v0/v1_1/native_pilot/generate_expansion_wave2.py`
- `benchmarks/cityintent_v0/v1_1/native_pilot/expansion_wave2/acceptance_report.json`
- `benchmarks/cityintent_v0/v1_1/native_pilot/expansion_wave2/v0_promotion_manifest.json`
- `results/cityintent_v1_1_candidate/native_wave2_public_v0_hardened2_analysis_48_2026-08-04/`
- `results/cityintent_v1_1_candidate/native_wave2_public_v1_hardened5_rescore_analysis_48_2026-08-05/`
- `results/cityintent_v1_1_candidate/native_wave2_public_v2_hardened4_analysis_48_2026-08-05/`
- `benchmarks/cityintent_v0/v1_1/native_pilot/expansion_wave2/public_cross_variant_promotion_manifest.json`
- `benchmarks/cityintent_v0/v1_1/native_pilot/expansion_wave2/public_cross_variant_promotion_manifest_pre_hardening.json`
- `benchmarks/cityintent_v0/v1_1/manifests/calibration_template_registry.json`
- `docs/plans/cityintent_v1_1_mechanism_expansion_roadmap_2026-08-05.md`
- `docs/experiments/cityintent_wave2_handoff_2026-08-04.md`

## Next gate

Use the accepted Wave-2 public calibration templates as controlled mechanism
seeds for further expansion toward the 144-item target. New instances must
independently repeat the oracle, matched-negative, six-system difficulty,
cross-world discrimination, leakage, and provenance gates before any release
count can increase.
