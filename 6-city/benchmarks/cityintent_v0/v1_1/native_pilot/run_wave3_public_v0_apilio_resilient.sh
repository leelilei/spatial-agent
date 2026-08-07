#!/bin/bash
# Resume-safe Apilio calibration for Wave-3 public variant v0.
set -u

V0_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
PILOT_ROOT="$V0_ROOT/v1_1/native_pilot"
RESULT_ROOT="$V0_ROOT/../../results/cityintent_v1_1_candidate"
CITYINTENT_PYTHON="${CITYINTENT_PYTHON:-python}"
RUNNER="$V0_ROOT/tools/run_baseline_traces.py"
BENCHMARK="$PILOT_ROOT/expansion_wave3/benchmark_config.json"
AGENTS=api_llm_react_tool_policy,api_llm_plan_and_execute
SCENARIOS=ci11w3_comp_metro_radial_v1_v0,ci11w3_disr_harbor_grid_v1_v0,ci11w3_memo_metro_radial_v1_v0,ci11w3_mult_harbor_grid_v1_v0,ci11w3_poi__harbor_grid_v1_v0,ci11w3_reso_suburb_polycentric_v1_v0,ci11w3_soci_suburb_polycentric_v1_v0,ci11w3_time_metro_radial_v1_v0
RUN_DATE=2026-08-05

[ -n "${APILIO_API_KEY:-}" ] || { echo "APILIO_API_KEY MISSING"; exit 1; }

run_model() {
  name="$1"
  config="$2"
  output="$RESULT_ROOT/native_wave3_public_v0_apilio_2x8x1_${RUN_DATE}_${name}"
  for attempt in $(seq 1 100); do
    if [ -f "$output/run_manifest.json" ] && [ "$(jq -r '.status' "$output/run_manifest.json")" = "complete" ]; then
      echo "v0 apilio $name COMPLETE"
      return 0
    fi
    echo "v0 apilio $name attempt $attempt"
    resume_flag=
    [ -f "$output/traces.json" ] && resume_flag=--resume
    "$CITYINTENT_PYTHON" "$RUNNER" \
      --benchmark-config "$BENCHMARK" \
      --agents "$AGENTS" \
      --llm-config "$config" \
      --scenario-ids "$SCENARIOS" \
      --results-dir "$output" \
      $resume_flag && true
    sleep 30
  done
  echo "v0 apilio $name INCOMPLETE"
  return 1
}

run_model claude "$V0_ROOT/configs/apilio_claude_sonnet45_20250929.json" || exit 1
run_model qwen "$V0_ROOT/configs/apilio_qwen3_235b_a22b_instruct_2507.json" || exit 1
run_model deepseek "$V0_ROOT/configs/apilio_deepseek_v4flash.json" || exit 1
