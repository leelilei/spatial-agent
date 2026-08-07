#!/usr/bin/env bash
set -Eeuo pipefail

if [[ "$#" -lt 1 || "$#" -gt 2 ]]; then
  echo "Usage: $0 STAGE [PARALLEL_JOBS]" >&2
  exit 2
fi
stage="$1"
parallel_jobs="${2:-4}"
case "$stage" in
  dev) seeds=(1 2 3) ;;
  confirm) seeds=(7 8 9) ;;
  *) echo "Invalid stage: $stage" >&2; exit 2 ;;
esac
case "$parallel_jobs" in
  ''|*[!0-9]*|0) echo "Invalid parallel job count: $parallel_jobs" >&2; exit 2 ;;
esac

RUNNER="${RUNNER:-/root/workspace/run_wikichurches_positive_anchor_tipf.sh}"
job_file="$(mktemp)"
cleanup() {
  rm -f "$job_file"
}
trap cleanup EXIT INT TERM
for shots in 1 4 16; do
  for seed in "${seeds[@]}"; do
    printf "%s %s\n" "$shots" "$seed" >> "$job_file"
  done
done

xargs -n2 -P"$parallel_jobs" bash -c \
  '"$1" "$2" "$3" "$4"' _ "$RUNNER" "$stage" < "$job_file"
