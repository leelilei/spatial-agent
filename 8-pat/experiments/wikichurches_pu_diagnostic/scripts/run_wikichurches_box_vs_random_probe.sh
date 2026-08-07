#!/usr/bin/env bash
set -Eeuo pipefail

TOGA_DIR="${TOGA_DIR:-/root/workspace/TOGA}"
DATASET_DIR="${DATASET_DIR:-/root/workspace/datasets/wikichurches}"
PARTS_FILE="${PARTS_FILE:-/root/workspace/building_parts.json}"
PROTOCOL_FILE="${PROTOCOL_FILE:-/root/workspace/wikichurches_box_vs_random_protocol.json}"
PROBE_SCRIPT="${PROBE_SCRIPT:-/root/workspace/wikichurches_box_vs_random_probe.py}"
OUT_DIR="${OUT_DIR:-/root/workspace/results/wikichurches_box_vs_random_20260727}"
PY_BIN="${PY_BIN:-/usr/local/miniconda3/envs/py312/bin/python}"
RUN_TIMEOUT_SECONDS="${RUN_TIMEOUT_SECONDS:-1200}"
BATCH_SIZE="${BATCH_SIZE:-64}"
MAX_IMAGES="${MAX_IMAGES:-}"
export TOGA_ROOT="$TOGA_DIR"

mkdir -p "$OUT_DIR/audit"
date -Is > "$OUT_DIR/audit/start_time.txt"
"$PY_BIN" --version > "$OUT_DIR/audit/python_version.txt" 2>&1
nvidia-smi -q > "$OUT_DIR/audit/nvidia_smi_q.txt"
sha256sum \
  "$PARTS_FILE" \
  "$PROTOCOL_FILE" \
  "$PROBE_SCRIPT" \
  "$TOGA_DIR/clip/clip.py" \
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

command=(
  timeout "$RUN_TIMEOUT_SECONDS" "$PY_BIN" "$PROBE_SCRIPT"
  --parts "$PARTS_FILE"
  --image-dir "$DATASET_DIR/images"
  --labels-dir "$DATASET_DIR/labels"
  --protocol "$PROTOCOL_FILE"
  --out-dir "$OUT_DIR"
  --device cuda
  --batch-size "$BATCH_SIZE"
)
if [[ -n "$MAX_IMAGES" ]]; then
  command+=(--max-images "$MAX_IMAGES")
fi

set +e
"${command[@]}" > "$OUT_DIR/run.log" 2>&1
run_status=$?
set -e
date -Is > "$OUT_DIR/audit/end_time.txt"
printf "%s\n" "$run_status" > "$OUT_DIR/audit/exit_code.txt"
if [[ "$run_status" -ne 0 || ! -s "$OUT_DIR/summary.json" ]]; then
  echo "Probe failed with exit code $run_status" >&2
  exit 1
fi

tar -C "$(dirname "$OUT_DIR")" -czf "${OUT_DIR}.tar.gz" "$(basename "$OUT_DIR")"
sha256sum "${OUT_DIR}.tar.gz" > "${OUT_DIR}.tar.gz.sha256"
