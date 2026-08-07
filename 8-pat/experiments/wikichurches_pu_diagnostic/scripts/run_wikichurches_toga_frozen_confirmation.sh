#!/usr/bin/env bash
set -Eeuo pipefail

TOGA_DIR="${TOGA_DIR:-/root/workspace/TOGA}"
DATA_ROOT="${DATA_ROOT:-/root/workspace/datasets}"
OUT_DIR="${OUT_DIR:-/root/workspace/results/wikichurches_toga_tuning_20260727/frozen_confirmation}"
PY_BIN="${PY_BIN:-/usr/local/miniconda3/envs/py312/bin/python}"
PAIR_RUNNER="${PAIR_RUNNER:-/root/workspace/run_wikichurches_toga_frozen_pair.sh}"
AGGREGATOR="${AGGREGATOR:-/root/workspace/aggregate_wikichurches_toga_frozen_confirmation.py}"
FROZEN_FILE="${FROZEN_FILE:-/root/workspace/wikichurches_toga_frozen_configs.json}"
PROTOCOL_FILE="${PROTOCOL_FILE:-/root/workspace/wikichurches_toga_frozen_confirmation_protocol.json}"
PARALLEL_PAIRS="${PARALLEL_PAIRS:-6}"

mkdir -p "$OUT_DIR/json" "$OUT_DIR/logs" "$OUT_DIR/audit"
date -Is > "$OUT_DIR/audit/start_time.txt"
"$PY_BIN" --version > "$OUT_DIR/audit/python_version.txt" 2>&1
nvidia-smi -q > "$OUT_DIR/audit/nvidia_smi_q.txt"
sha256sum \
  "$TOGA_DIR/main.py" \
  "$TOGA_DIR/utils.py" \
  "$TOGA_DIR/configs/wikichurches.yaml" \
  "$FROZEN_FILE" \
  "$PROTOCOL_FILE" \
  "$PAIR_RUNNER" \
  "$AGGREGATOR" \
  > "$OUT_DIR/audit/input_sha256.txt"

monitor_pid=""
cleanup() {
  if [[ -n "$monitor_pid" ]]; then
    kill "$monitor_pid" 2>/dev/null || true
  fi
}
trap cleanup EXIT INT TERM
(
  while true; do
    nvidia-smi \
      --query-gpu=timestamp,utilization.gpu,memory.used,power.draw,temperature.gpu \
      --format=csv,noheader,nounits
    sleep 2
  done
) > "$OUT_DIR/audit/gpu.csv" 2>&1 &
monitor_pid=$!

{
  for shots in 1 4 16; do
    for seed in 4 5 6; do
      printf "%s %s\n" "$shots" "$seed"
    done
  done
} | xargs -P "$PARALLEL_PAIRS" -n 2 "$PAIR_RUNNER"

{
  printf "shots\tseed\tmethod\tcandidate\tstart\tend\telapsed_seconds\texit_code\n"
  find "$OUT_DIR/audit/status_fragments" -name "*.tsv" -type f -print0 \
    | sort -z \
    | xargs -0 cat
} > "$OUT_DIR/audit/run_status.tsv"

if awk -F $'\t' 'NR > 1 && $8 != 0 {exit 1}' "$OUT_DIR/audit/run_status.tsv"; then
  :
else
  echo "At least one confirmation run failed" >&2
  exit 1
fi

date -Is > "$OUT_DIR/audit/end_time.txt"
"$PY_BIN" "$AGGREGATOR" \
  --json-dir "$OUT_DIR/json" \
  --protocol-file "$PROTOCOL_FILE" \
  --frozen-file "$FROZEN_FILE" \
  --out-dir "$OUT_DIR/aggregate"
