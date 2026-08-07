#!/bin/bash
# Resume-safe Wave-4 public six-system calibration across all three public worlds.
#
# 3 public variants x 3 actor models x 2 paper-backed policies x 8 constructs
#   = 144 actor traces.
#
# The API key is read from the environment only; it is never written to disk.
set -u

V0_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
PILOT_ROOT="$V0_ROOT/v1_1/native_pilot"
RESULT_ROOT="$V0_ROOT/../../results/cityintent_v1_1_candidate"
CITYINTENT_PYTHON="${CITYINTENT_PYTHON:-python}"
RUNNER="$V0_ROOT/tools/run_baseline_traces.py"
BENCHMARK="$PILOT_ROOT/expansion_wave4/benchmark_config.json"
AGENTS=api_llm_react_tool_policy,api_llm_plan_and_execute
RUN_DATE=2026-08-06

[ -n "${APILIO_API_KEY:-}" ] || { echo "APILIO_API_KEY MISSING"; exit 1; }

V0_SCENARIOS=ci11w4_comp_metro_radial_v1_v0,ci11w4_disr_harbor_grid_v1_v0,ci11w4_memo_metro_radial_v1_v0,ci11w4_mult_harbor_grid_v1_v0,ci11w4_poi__harbor_grid_v1_v0,ci11w4_reso_suburb_polycentric_v1_v0,ci11w4_soci_suburb_polycentric_v1_v0,ci11w4_time_metro_radial_v1_v0
V1_SCENARIOS=ci11w4_comp_suburb_polycentric_v1_v1,ci11w4_disr_metro_radial_v1_v1,ci11w4_memo_suburb_polycentric_v1_v1,ci11w4_mult_metro_radial_v1_v1,ci11w4_poi__metro_radial_v1_v1,ci11w4_reso_harbor_grid_v1_v1,ci11w4_soci_harbor_grid_v1_v1,ci11w4_time_suburb_polycentric_v1_v1
V2_SCENARIOS=ci11w4_comp_harbor_grid_v1_v2,ci11w4_disr_suburb_polycentric_v1_v2,ci11w4_memo_harbor_grid_v1_v2,ci11w4_mult_suburb_polycentric_v1_v2,ci11w4_poi__suburb_polycentric_v1_v2,ci11w4_reso_metro_radial_v1_v2,ci11w4_soci_metro_radial_v1_v2,ci11w4_time_harbor_grid_v1_v2

run_cell() {
  variant="$1"
  scenarios="$2"
  name="$3"
  config="$4"
  output="$RESULT_ROOT/native_wave4_public_${variant}_apilio_2x8x1_${RUN_DATE}_${name}"
  for attempt in $(seq 1 60); do
    if [ -f "$output/run_manifest.json" ] \
       && [ "$(jq -r '.status' "$output/run_manifest.json" 2>/dev/null)" = "complete" ]; then
      echo "wave4 $variant $name COMPLETE"
      return 0
    fi
    echo "wave4 $variant $name attempt $attempt"
    resume_flag=
    [ -f "$output/traces.json" ] && resume_flag=--resume
    "$CITYINTENT_PYTHON" "$RUNNER" \
      --benchmark-config "$BENCHMARK" \
      --agents "$AGENTS" \
      --llm-config "$config" \
      --scenario-ids "$scenarios" \
      --results-dir "$output" \
      $resume_flag && true
    sleep 20
  done
  echo "wave4 $variant $name INCOMPLETE"
  return 1
}

for spec in "v0:$V0_SCENARIOS" "v1:$V1_SCENARIOS" "v2:$V2_SCENARIOS"; do
  variant="${spec%%:*}"
  scenarios="${spec#*:}"
  run_cell "$variant" "$scenarios" claude   "$V0_ROOT/configs/apilio_claude_sonnet45_20250929.json"   || exit 1
  run_cell "$variant" "$scenarios" qwen     "$V0_ROOT/configs/apilio_qwen3_235b_a22b_instruct_2507.json" || exit 1
  run_cell "$variant" "$scenarios" deepseek "$V0_ROOT/configs/apilio_deepseek_v4flash.json"           || exit 1
done

echo "ALL WAVE-4 PUBLIC CELLS COMPLETE"
