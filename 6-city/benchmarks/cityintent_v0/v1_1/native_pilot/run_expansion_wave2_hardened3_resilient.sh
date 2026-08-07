#!/bin/bash
# Resume-safe Yunwu calibration for the targeted Wave-2 hardening items.
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
    v1) echo ci11w2_reso_harbor_grid_v1_v1 ;;
    v2) echo ci11w2_comp_harbor_grid_v1_v2,ci11w2_time_harbor_grid_v1_v2 ;;
    *) echo "unknown variant: $1" >&2; return 1 ;;
  esac
}

run_model() {
  variant="$1"
  name="$2"
  config="$3"
  scenarios="$(scenarios_for_variant "$variant")" || return 1
  if [ "$variant" = "v1" ]; then
    hardening_tag=hardened4
  else
    hardening_tag=hardened3
  fi
  output="$RESULT_ROOT/native_wave2_public_${variant}_${hardening_tag}_2xtargetx1_${RUN_DATE}_${name}"
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
