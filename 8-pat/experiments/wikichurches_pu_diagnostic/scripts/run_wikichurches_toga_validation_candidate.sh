#!/usr/bin/env bash
set -Eeuo pipefail

if [[ "$#" -ne 3 ]]; then
  echo "Usage: $0 CANDIDATE_ID SHOTS SEED" >&2
  exit 2
fi

candidate_id="$1"
shots="$2"
seed="$3"
case "$shots" in
  1|4|16) ;;
  *) echo "Invalid shots: $shots" >&2; exit 2 ;;
esac
case "$seed" in
  1|2|3) ;;
  *) echo "Invalid development seed: $seed" >&2; exit 2 ;;
esac

TOGA_DIR="${TOGA_DIR:-/root/workspace/TOGA}"
DATA_ROOT="${DATA_ROOT:-/root/workspace/datasets}"
OUT_DIR="${OUT_DIR:-/root/workspace/results/wikichurches_toga_tuning_20260727/validation_screen}"
PY_BIN="${PY_BIN:-/usr/local/miniconda3/envs/py312/bin/python}"
CANDIDATE_FILE="${CANDIDATE_FILE:-/root/workspace/wikichurches_toga_validation_candidates.json}"
RUN_TIMEOUT_SECONDS="${RUN_TIMEOUT_SECONDS:-1800}"

mkdir -p \
  "$OUT_DIR/json" \
  "$OUT_DIR/logs" \
  "$OUT_DIR/audit/status_fragments" \
  "$OUT_DIR/audit/locks"

mapfile -t candidate_values < <(
  "$PY_BIN" - "$CANDIDATE_FILE" "$candidate_id" <<'PY'
import json
import sys

path, candidate_id = sys.argv[1:]
document = json.load(open(path, encoding="utf-8"))
try:
    candidate = document["candidates"][candidate_id]
except KeyError as error:
    raise SystemExit(f"Unknown candidate: {candidate_id}") from error
for key in (
    "lr",
    "init_delta",
    "lambda_teacher",
    "pooling_ratio",
    "dropout_rate",
    "focal_loss_gamma",
):
    print(candidate[key])
PY
)
if [[ "${#candidate_values[@]}" -ne 6 ]]; then
  echo "Failed to resolve candidate: $candidate_id" >&2
  exit 2
fi
lr="${candidate_values[0]}"
init_delta="${candidate_values[1]}"
lambda_teacher="${candidate_values[2]}"
pooling_ratio="${candidate_values[3]}"
dropout_rate="${candidate_values[4]}"
focal_loss_gamma="${candidate_values[5]}"

run_id="${candidate_id}_s${shots}_seed${seed}"
json_path="$OUT_DIR/json/${run_id}.json"
log_path="$OUT_DIR/logs/${run_id}.log"
status_path="$OUT_DIR/audit/status_fragments/${run_id}.tsv"
lock_dir="$OUT_DIR/audit/locks/${run_id}.lock"

if [[ -s "$json_path" ]]; then
  printf "%s\t%s\t%s\tREUSED\tREUSED\t0\t0\n" \
    "$candidate_id" "$shots" "$seed" > "$status_path"
  exit 0
fi
if ! mkdir "$lock_dir" 2>/dev/null; then
  echo "Candidate is already running: $run_id"
  exit 0
fi
cleanup() {
  rmdir "$lock_dir" 2>/dev/null || true
}
trap cleanup EXIT INT TERM

cd "$TOGA_DIR"
start_iso=$(date -Is)
start_s=$(date +%s)
set +e
timeout "$RUN_TIMEOUT_SECONDS" "$PY_BIN" main.py \
  --config ./configs/wikichurches.yaml \
  --root_path "$DATA_ROOT" \
  --shots "$shots" \
  --seed "$seed" \
  --method toga \
  --train_epoch 20 \
  --batch_size 16 \
  --num_workers 0 \
  --wandb_mode disabled \
  --validation_only \
  --run_namespace "tune_${candidate_id}_s${shots}" \
  --lr "$lr" \
  --init_delta "$init_delta" \
  --lambda_teacher "$lambda_teacher" \
  --pooling_ratio "$pooling_ratio" \
  --dropout_rate "$dropout_rate" \
  --focal_loss_gamma "$focal_loss_gamma" \
  --output_json "$json_path" \
  > "$log_path" 2>&1
run_status=$?
set -e
end_s=$(date +%s)
end_iso=$(date -Is)
elapsed=$((end_s - start_s))
printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\n" \
  "$candidate_id" "$shots" "$seed" \
  "$start_iso" "$end_iso" "$elapsed" "$run_status" \
  > "$status_path"

if [[ "$run_status" -ne 0 || ! -s "$json_path" ]]; then
  echo "Run failed: $run_id (exit=$run_status); see $log_path" >&2
  exit 1
fi

