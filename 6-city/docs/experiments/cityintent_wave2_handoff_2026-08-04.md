# CityIntent Wave-2 handoff — 2026-08-04 23:42 CST

## Objective

Continue turning CityIntent v1.1 Wave 2 into a real benchmark. The immediate
task is to close three localized public-world calibration failures without
rerunning the 21 unchanged items or exposing private evaluation worlds to actor
models.

Workspace: `/Users/mac/Documents/6-Research/6-city`

## Safe checkpoint

- No Wave-2 actor process is running.
- The base public matrix is complete: v0/v1/v2 each have 48/48 traces, for
  144/144 total traces across Claude Sonnet 4.5, DeepSeek v4 Flash, Qwen3-235B,
  ReAct, and PlanExec.
- All 24 current generated scenarios pass oracle and matched-negative gates.
- The full test suite passes: `68 passed`.
- Private-world actors have not been run.
- Yunwu has shown intermittent DNS, TLS, HTTP/2, and 120-second timeout errors.
  All runner scripts are resume-safe; run models serially.

## Completed empirical results

### v0 final

Analysis:
`results/cityintent_v1_1_candidate/native_wave2_public_v0_hardened2_analysis_48_2026-08-04/analysis.json`

All 8/8 items passed the single-world gate. Item mean/range/corrected-r:

| construct | mean | range | r |
|---|---:|---:|---:|
| compound | 0.847 | 0.529 | 0.708 |
| disruption | 0.500 | 1.000 | 0.942 |
| memory | 0.428 | 1.000 | 0.975 |
| multi | 0.271 | 0.875 | 0.515 |
| POI | 0.500 | 1.000 | 0.942 |
| resource | 0.875 | 0.375 | 0.728 |
| social | 0.500 | 0.750 | 0.784 |
| time | 0.750 | 0.500 | 0.954 |

### v1 final before targeted hardening

Analysis:
`results/cityintent_v1_1_candidate/native_wave2_public_v1_analysis_48_2026-08-04/analysis.json`

Coverage is 48/48 with no ceiling/floor. Seven items pass the strict item gate.
The only failure is `ci11w2_reso_harbor_grid_v1_v1`: mean 0.875, range 0.375,
corrected r 0.034. Its six task scores were 1.000 for both Claude systems and
both DeepSeek systems, and 0.625 for both Qwen systems.

### v2 final before targeted hardening

Analysis:
`results/cityintent_v1_1_candidate/native_wave2_public_v2_analysis_48_2026-08-04/analysis.json`

Coverage is 48/48 with no ceiling/floor. Six items pass the strict item gate.
Failures:

- `ci11w2_comp_harbor_grid_v1_v2`: mean 0.912, range 0.529, r 0.443;
  five systems scored 1.000 and Qwen PlanExec scored 0.471.
- `ci11w2_time_harbor_grid_v1_v2`: mean 0.917, range 0.500, r 0.387;
  five systems scored 1.000 and Claude PlanExec scored 0.500.

The first cross-world audit accepted 5/8 templates and 15/24 instances. It is
archived, intentionally not final, at:
`benchmarks/cityintent_v0/v1_1/native_pilot/expansion_wave2/public_cross_variant_promotion_manifest_pre_hardening.json`.

## Current generator state

Generator:
`benchmarks/cityintent_v0/v1_1/native_pilot/generate_expansion_wave2.py`

Manifest version is `cityintent-native-expansion-wave2-1.0.2`.

Only three items differ from the archived base matrix:

1. v1 resource, hardened4:
   - supplies outcome weight 0.15;
   - training outcome weight 0.15;
   - return-home outcome weight 0.30;
   - avoid optional cafes outcome weight 0.20;
   - budget constraint weight 0.20.
   - The intention explicitly forbids entering either optional cafe as an
     action-budget detour.
2. v2 compound, hardened3:
   - medicine/message/meeting/return weights are 0.15/0.15/0.40/0.15;
   - legal-trace constraint remains 0.15.
3. v2 time, hardened3:
   - first/second window weights are 0.28/0.52;
   - legal-trace constraint remains 0.20.

The other 21 scenarios were checked against archived run manifests using the
runner's canonical JSON hash function: 0 mismatches.

Current offline verification:

```text
{"all_passed": true, "pass_count": 24, "scenario_count": 24}
68 passed in 1.02s
```

## Historical targeted calibration

Hardened3 v1-resource results are retained as calibration evidence but must not
be merged into the final hardened4 composite:

- Claude: ReAct 1.000, PlanExec 1.000, complete 2/2.
- Qwen: ReAct 1.000, PlanExec 0.500, complete 2/2.
- DeepSeek: ReAct 1.000, PlanExec missing, interrupted 1/2.

This proved the no-detour outcome repairs policy alignment, but the implied
mean was 0.917, still above the 0.90 upper bound. Hardened4 therefore lowers
the same observed Qwen PlanExec behavior to 0.375; expected item mean is 0.896.

The current hardened4 Claude directory is an empty interrupted checkpoint:
`results/cityintent_v1_1_candidate/native_wave2_public_v1_hardened4_2xtargetx1_2026-08-04_claude/`
(0/2, no `traces.json`). The runner can safely start it again without
`--resume` and will rewrite the stale interrupted manifest.

## Exact continuation procedure

### 1. Confirm no duplicate process

```bash
pgrep -af 'run_expansion_wave2_hardened3_resilient|run_baseline_traces.py.*hardened[34]' || true
```

### 2. Resume the 18 targeted traces

The script name says hardened3 for historical reasons. Its current behavior is
correct: v1 writes to `hardened4`, v2 writes to `hardened3`.

```bash
cd /Users/mac/Documents/6-Research/6-city
./benchmarks/cityintent_v0/v1_1/native_pilot/run_expansion_wave2_hardened3_resilient.sh
```

Expected new coverage:

- v1 hardened4: 1 scenario × 2 policies × 3 models = 6 traces.
- v2 hardened3: 2 scenarios × 2 policies × 3 models = 12 traces.
- total = 18 traces.

Do not parallelize models through Yunwu. If interrupted, rerun the same script;
it checks `run_manifest.json` and uses `--resume` when `traces.json` exists.

### 3. Rebuild v1 composite with hardened4 first

```bash
python benchmarks/cityintent_v0/v1_1/native_pilot/merge_trace_archives.py \
  --run-dir results/cityintent_v1_1_candidate/native_wave2_public_v1_hardened4_2xtargetx1_2026-08-04_claude \
  --run-dir results/cityintent_v1_1_candidate/native_wave2_public_v1_hardened4_2xtargetx1_2026-08-04_qwen \
  --run-dir results/cityintent_v1_1_candidate/native_wave2_public_v1_hardened4_2xtargetx1_2026-08-04_deepseek \
  --run-dir results/cityintent_v1_1_candidate/native_wave2_public_v1_composite_48_2026-08-04 \
  --expected-traces 48 --expected-scenarios 8 \
  --output-dir results/cityintent_v1_1_candidate/native_wave2_public_v1_hardened4_composite_48_2026-08-04

python benchmarks/cityintent_v0/v1_1/native_pilot/analyze_blind_pilot.py \
  --run-dir results/cityintent_v1_1_candidate/native_wave2_public_v1_hardened4_composite_48_2026-08-04 \
  --expected-systems 6 \
  --benchmark-config benchmarks/cityintent_v0/v1_1/native_pilot/expansion_wave2/benchmark_config.json \
  --output-dir results/cityintent_v1_1_candidate/native_wave2_public_v1_hardened4_analysis_48_2026-08-04
```

### 4. Rebuild v2 composite with hardened3 first

```bash
python benchmarks/cityintent_v0/v1_1/native_pilot/merge_trace_archives.py \
  --run-dir results/cityintent_v1_1_candidate/native_wave2_public_v2_hardened3_2xtargetx1_2026-08-04_claude \
  --run-dir results/cityintent_v1_1_candidate/native_wave2_public_v2_hardened3_2xtargetx1_2026-08-04_qwen \
  --run-dir results/cityintent_v1_1_candidate/native_wave2_public_v2_hardened3_2xtargetx1_2026-08-04_deepseek \
  --run-dir results/cityintent_v1_1_candidate/native_wave2_public_v2_composite_48_2026-08-04 \
  --expected-traces 48 --expected-scenarios 8 \
  --output-dir results/cityintent_v1_1_candidate/native_wave2_public_v2_hardened3_composite_48_2026-08-04

python benchmarks/cityintent_v0/v1_1/native_pilot/analyze_blind_pilot.py \
  --run-dir results/cityintent_v1_1_candidate/native_wave2_public_v2_hardened3_composite_48_2026-08-04 \
  --expected-systems 6 \
  --benchmark-config benchmarks/cityintent_v0/v1_1/native_pilot/expansion_wave2/benchmark_config.json \
  --output-dir results/cityintent_v1_1_candidate/native_wave2_public_v2_hardened3_analysis_48_2026-08-04
```

The merge tool uses deterministic first-source priority. The hardened run dirs
must precede the old composite.

### 5. Rerun the strict cross-world gate

```bash
python benchmarks/cityintent_v0/v1_1/native_pilot/audit_cross_variant_promotion.py \
  --analysis results/cityintent_v1_1_candidate/native_wave2_public_v0_hardened2_analysis_48_2026-08-04/analysis.json \
  --analysis results/cityintent_v1_1_candidate/native_wave2_public_v1_hardened4_analysis_48_2026-08-04/analysis.json \
  --analysis results/cityintent_v1_1_candidate/native_wave2_public_v2_hardened3_analysis_48_2026-08-04/analysis.json \
  --oracle-report benchmarks/cityintent_v0/v1_1/native_pilot/expansion_wave2/acceptance_report.json \
  --scenario-dir benchmarks/cityintent_v0/v1_1/native_pilot/expansion_wave2/scenarios \
  --output benchmarks/cityintent_v0/v1_1/native_pilot/expansion_wave2/public_cross_variant_promotion_manifest.json
```

Target result: 8/8 templates and 24/24 public instances accepted. Required per
instance thresholds are six systems, range ≥0.15, corrected item-total r ≥0.20,
and mean task in [0.20, 0.90], with no ceiling/floor.

### 6. Final verification and documentation

```bash
python -m pytest benchmarks/cityintent_v0/tests -q
```

Then update:

- `docs/experiments/cityintent_v1_1_wave2_mechanism_expansion_2026-08-04.md`
- `RESULTS.md`

Report actual hardened item values, not the expected values above. If any item
still fails, retain the failed run and perform another localized hardening; do
not weaken the global thresholds and do not rerun private-world actors.

## Important cautions

- Do not use FHL for actor runs here; the actor matrix is Yunwu. A deterministic
  verifier is used for this gate. FHL is acceptable only for a separate judge
  experiment if explicitly added later.
- Do not overwrite or delete old v0/v1/v2 or hardened3 archives.
- Do not mix a changed LLM transport or model config into a resumed run; the
  manifest correctly rejects hash drift.
- `results/.../native_wave2_public_v2_preliminary_*_47_2026-08-04` is a
  diagnostic partial archive and must not be used in promotion.
- The benchmark release accepted count remains 0/144. Passing this Wave-2 gate
  promotes calibration templates; it does not by itself create the 144-item
  release benchmark.
