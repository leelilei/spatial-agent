# CityIntent v1.1 — Wave-4 public six-system calibration (2026-08-06)

Status: **calibration failed the promotion gate. 1 of 8 templates accepted.**
Registry stays at 24 templates / 72 public instances. Release accepted count stays **0/144**.

## What ran

144 actor traces, complete coverage, no missing cells:

- 3 public worlds (v0/v1/v2) × 3 models × 2 policies × 8 constructs
- Models: `claude-sonnet-4-5-20250929`, `qwen3-235b-a22b-instruct-2507`, `deepseek-v4-flash`
- Policies: `api_llm_react_tool_policy`, `api_llm_plan_and_execute`
- Provider: Apilio (single provider, but three vendor families — matches Wave-3's design)
- Runner: `v1_1/native_pilot/run_wave4_public_calibration_resilient.sh`

## Promotion gate result

`audit_cross_variant_promotion.py` accepted **1/8 templates, 3/24 items**.

| Construct | v0 mean / r | v1 mean / r | v2 mean / r | Decision |
|---|---|---|---|---|
| `multi_party_commitment` | 0.865 / +0.707 | 0.865 / +0.295 | 0.729 / +0.876 | ✅ **accepted** |
| `compound_long_horizon` | 0.834 / +0.473 | 0.723 / **−0.260** | 0.889 / +0.920 | ❌ v1 item gate |
| `disruption_recovery` | 0.667 / +0.655 | 0.500 / +0.250 | 0.833 / **−0.311** | ❌ v2 item gate |
| `time_window_scheduling` | 0.885 / **−0.262** | 0.885 / **+0.180** | 0.771 / +0.890 | ❌ v0+v1 item gate |
| `social_coordination_copresence` | **0.923** / +0.779 | 0.756 / **−0.036** | 0.756 / +0.874 | ❌ v0+v1 item gate |
| `poi_availability_service_evidence` | 0.792 / +0.509 | 0.833 / **+0.036** | **0.948** / +0.700 | ❌ v1+v2 item gate |
| `memory_conditioned_preference` | **1.000** / — | **1.000** / — | **1.000** / — | ❌ all three, ceiling |
| `resource_budget_allocation` | **1.000** / — | **1.000** / — | **1.000** / — | ❌ all three, ceiling |

Gate thresholds: `mean_task ∈ [0.20, 0.90]`, `range ≥ 0.15`, `corrected_item_total_correlation ≥ 0.20`, no ceiling/floor, 6 systems observed.

Only `multi_party_commitment` (the sequential two-party relay) clears all three worlds.

## Root cause: the whole wave is too easy

This is one problem with two surface presentations, not eight separate defects.

| | system mean | system spread |
|---|---|---|
| Wave-3 v0 / v1 / v2 | 0.607 / 0.563 / 0.563 | 0.747 / 0.827 / 0.753 |
| **Wave-4 v0 / v1 / v2** | **0.871 / 0.820 / 0.866** | **0.365 / 0.284 / 0.393** |

Wave-4 sits **0.21–0.30 higher** than Wave-3 with **roughly half the system spread**. Corrected item-total correlation needs total-score variance to be stable; when six systems compress near ceiling, a single atypical score flips the sign of `r`. That is exactly what the table shows — `comp`, `disr`, `soci`, `time` each pass in some worlds and fail in others, with `r` ranging from −0.311 to +0.920 for the *same mechanism*. Those are not four per-item defects; they are four projections of insufficient variance.

Wave-3's `r` values for comparison: 0.397–0.990 (v0), 0.764–0.986 (v1). Healthy, because its systems spanned 0.126–0.953.

### The two hard ceilings are a design defect I introduced

`memory_conditioned_preference` and `resource_budget_allocation` scored **1.000 with zero range in all three worlds**. Reading the traces shows why: the `private_intention` states the answer.

- `memo`: the memory seed literally says `tagged reliable`, and the intention says "the location named by the reliable source." That is a label lookup, not arbitration. All three models produce the identical trace: `recall | recall | move->library | dwell | finish`.
- `reso`: the intention names both the market *and* the gym, *and* pre-warns that spending at the decoy "leaves too little for the training." The decoy is never a temptation. DeepSeek reaches the answer in six actions.

These are the same two mechanisms I flagged at offline construction as having weak novelty (no new evidence type; only generic `no_feasibility_violation`). The offline audit caught the smell; calibration confirmed it empirically. Weak mechanism → ceiling.

By contrast, the items that discriminate demand execution discipline rather than reading: `disr` (range 1.000) requires waiting for a recovery that cannot be shortcut; `mult` (range 0.813, the sole accepted template) requires carrying evidence between two timed meetings in order.

### One earlier hypothesis was wrong

At v0 I suspected `time`'s negative `r` (−0.262) was a Wave-1-style confound between payment and timing. It was not. v1 gave +0.180 with the same mechanism — the sign did not replicate. It was a single data point: qwen PlanExec at 0.312 against five systems at 1.000, and qwen PlanExec is not the weakest system overall. Noise from near-ceiling compression, not structure.

## What this does not change

- Offline construction gates all still pass: 24/24 oracle at 1.0 with zero violations, matched-negative headroom 0.50–1.00, 24/24 structurally distinct against base/wave1/wave2/wave3, 88 tests green, all prior waves re-verified.
- The generator is deterministic and reproducible.
- The `service_after_recovery` evaluator semantic added for this wave is sound and tested.

The failure is in item *difficulty calibration*, not in construction, evaluation, or tooling.

## What comes next

Wave-4 needs hardening before it can be re-calibrated. Two tiers:

1. **Redesign** `memo` and `reso` so the intention states the *goal* without naming the answer. For `memo`, reliability must be inferable from source type (verified bulletin vs unverified chat) rather than an explicit `tagged reliable` label. For `reso`, remove the pre-warning so the decoy is a genuine tradeoff.
2. **Raise global difficulty** for the remaining five rejected mechanisms so system spread recovers toward Wave-3's ~0.75. Per-item tweaks will not stabilise `r` while the whole wave sits at 0.87 mean.

Re-calibration costs another 144 traces and needs fresh authorization.

## Artifacts

- calibration status: `v1_1/native_pilot/expansion_wave4/calibration_status.json`
- promotion manifest: `v1_1/native_pilot/expansion_wave4/public_cross_variant_promotion_manifest.json`
- per-world analyses: `results/cityintent_v1_1_candidate/native_wave4_public_v{0,1,2}_analysis_48_2026-08-06/`
- trace archives: `results/cityintent_v1_1_candidate/native_wave4_public_v{0,1,2}_apilio_2x8x1_2026-08-06_{claude,qwen,deepseek}/`
- runner: `v1_1/native_pilot/run_wave4_public_calibration_resilient.sh`
- offline construction note: `docs/experiments/cityintent_v1_1_wave4_offline_construction_2026-08-06.md`
