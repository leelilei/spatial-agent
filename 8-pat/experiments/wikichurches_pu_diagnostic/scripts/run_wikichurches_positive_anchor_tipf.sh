#!/usr/bin/env bash
set -Eeuo pipefail

if [[ "$#" -ne 3 ]]; then
  echo "Usage: $0 STAGE SHOTS SEED" >&2
  exit 2
fi

stage="$1"
shots="$2"
seed="$3"
case "$stage" in
  dev)
    case "$seed" in 1|2|3) ;; *) echo "Invalid dev seed: $seed" >&2; exit 2 ;; esac
    ;;
  confirm)
    case "$seed" in 7|8|9) ;; *) echo "Invalid confirmation seed: $seed" >&2; exit 2 ;; esac
    ;;
  *) echo "Invalid stage: $stage" >&2; exit 2 ;;
esac
case "$shots" in 1|4|16) ;; *) echo "Invalid shots: $shots" >&2; exit 2 ;; esac

TOGA_DIR="${TOGA_DIR:-/root/workspace/TOGA}"
DATA_ROOT="${DATA_ROOT:-/root/workspace/datasets}"
ROOT_OUT_DIR="${ROOT_OUT_DIR:-/root/workspace/results/wikichurches_positive_anchor_20260727}"
PY_BIN="${PY_BIN:-/usr/local/miniconda3/envs/py312/bin/python}"
RUN_TIMEOUT_SECONDS="${RUN_TIMEOUT_SECONDS:-1800}"
OUT_DIR="$ROOT_OUT_DIR/${stage}_tipf"

mkdir -p "$OUT_DIR/predictions" "$OUT_DIR/json" "$OUT_DIR/logs" "$OUT_DIR/locks"
run_id="tipf_s${shots}_seed${seed}"
prediction_path="$OUT_DIR/predictions/${run_id}.pt"
json_path="$OUT_DIR/json/${run_id}.json"
log_path="$OUT_DIR/logs/${run_id}.log"
lock_dir="$OUT_DIR/locks/${run_id}.lock"

if [[ -s "$prediction_path" && -s "$json_path" ]]; then
  echo "Reusing complete run: $run_id"
  exit 0
fi
if ! mkdir "$lock_dir" 2>/dev/null; then
  echo "Run is already active: $run_id"
  exit 0
fi
cleanup() {
  rmdir "$lock_dir" 2>/dev/null || true
}
trap cleanup EXIT INT TERM

command=(
  timeout "$RUN_TIMEOUT_SECONDS" "$PY_BIN" main.py
  --config ./configs/wikichurches.yaml
  --root_path "$DATA_ROOT"
  --shots "$shots"
  --seed "$seed"
  --method tip_adapter_f
  --train_epoch 20
  --batch_size 16
  --num_workers 0
  --wandb_mode disabled
  --run_namespace "positive_anchor_${stage}_s${shots}"
  --lr 0.001
  --output_predictions "$prediction_path"
  --output_json "$json_path"
)
if [[ "$stage" == "dev" ]]; then
  command+=(--validation_only)
fi

cd "$TOGA_DIR"
echo "Starting $stage $run_id at $(date -Is)"
"${command[@]}" > "$log_path" 2>&1
if [[ ! -s "$prediction_path" || ! -s "$json_path" ]]; then
  echo "Missing output for $run_id; see $log_path" >&2
  exit 1
fi
echo "Completed $stage $run_id at $(date -Is)"
