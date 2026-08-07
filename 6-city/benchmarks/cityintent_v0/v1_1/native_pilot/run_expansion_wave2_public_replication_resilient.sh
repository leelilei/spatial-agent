#!/bin/bash
# Resume-safe Yunwu replication of Wave-2 mechanisms in public world variants v1/v2.
set -u

V0_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
PILOT_ROOT="$V0_ROOT/v1_1/native_pilot"
RESULT_ROOT="$V0_ROOT/../../results/cityintent_v1_1_candidate"
CITYINTENT_PYTHON="${CITYINTENT_PYTHON:-python}"
RUNNER="$V0_ROOT/tools/run_baseline_traces.py"
BENCHMARK="$PILOT_ROOT/expansion_wave2/benchmark_config.json"
AGENTS=api_llm_react_tool_policy,api_llm_plan_and_execute
RUN_DATE=2026-08-04

[ -n "${DEEPSEEK_API_KEY:-}" ] || { echo "DEEPSEEK_API_KEY MISSING"; exit 1; }

scenarios_for_variant() {
  case "$1" in
    v1)
      echo ci11w2_comp_suburb_polycentric_v1_v1,ci11w2_disr_metro_radial_v1_v1,ci11w2_memo_suburb_polycentric_v1_v1,ci11w2_mult_metro_radial_v1_v1,ci11w2_poi__metro_radial_v1_v1,ci11w2_reso_harbor_grid_v1_v1,ci11w2_soci_harbor_grid_v1_v1,ci11w2_time_suburb_polycentric_v1_v1
      ;;
    v2)
      echo ci11w2_comp_harbor_grid_v1_v2,ci11w2_disr_suburb_polycentric_v1_v2,ci11w2_memo_harbor_grid_v1_v2,ci11w2_mult_suburb_polycentric_v1_v2,ci11w2_poi__suburb_polycentric_v1_v2,ci11w2_reso_metro_radial_v1_v2,ci11w2_soci_metro_radial_v1_v2,ci11w2_time_harbor_grid_v1_v2
      ;;
    *)
      echo "unknown variant: $1" >&2
      return 1
      ;;
  esac
}

run_model() {
  variant="$1"
  name="$2"
  config="$3"
  scenarios="$(scenarios_for_variant "$variant")" || return 1
  run_tag="native_wave2_public_${variant}_2x8x1_${RUN_DATE}"
  output="$RESULT_ROOT/${run_tag}_${name}"

  for attempt in $(seq 1 100); do
    if [ -f "$output/run_manifest.json" ] && [ "$(jq -r '.status' "$output/run_manifest.json")" = "complete" ]; then
      echo "$variant $name COMPLETE"
      return 0
    fi
    echo "$variant $name attempt $attempt"
    if [ -f "$output/traces.json" ]; then
      "$CITYINTENT_PYTHON" "$RUNNER" \
        --benchmark-config "$BENCHMARK" \
        --agents "$AGENTS" \
        --llm-config "$config" \
        --scenario-ids "$scenarios" \
        --results-dir "$output" \
        --resume \
        && true
    else
      "$CITYINTENT_PYTHON" "$RUNNER" \
        --benchmark-config "$BENCHMARK" \
        --agents "$AGENTS" \
        --llm-config "$config" \
        --scenario-ids "$scenarios" \
        --results-dir "$output" \
        && true
    fi
    # Yunwu occasionally rejects several consecutive TLS handshakes. Back off
    # enough to avoid turning a transient provider incident into a failed run.
    sleep 30
  done
  echo "$variant $name INCOMPLETE"
  return 1
}

for variant in v1 v2; do
  run_model "$variant" claude "$V0_ROOT/configs/yunwu_claude_sonnet45_20250929.json" || exit 1
  run_model "$variant" qwen "$V0_ROOT/configs/yunwu_qwen3_235b_a22b_instruct_2507.json" || exit 1
  run_model "$variant" deepseek "$V0_ROOT/configs/yunwu_deepseek_v4flash.json" || exit 1
done
