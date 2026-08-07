#!/usr/bin/env bash
set -euo pipefail

# Byte-identical transport mirror; the assembled archive must match the
# CaltechDATA-published byte count and MD5 below before it is accepted.
url="https://hf-mirror.com/datasets/XiN0919/FGVC/resolve/main/CUB_200_2011.tgz?download=true"
output="${1:-/root/workspace/datasets/cub_200_2011/CUB_200_2011.tgz}"
run_dir="${2:-/root/workspace/mnar_privileged_part_learning/runs/PAT-D-260728-001}"
total_bytes=1150585339
workers=24
expected_md5="97eceeb196236b17998738112f37df78"

chunk_dir="${output}.parts"
mkdir -p "$(dirname "$output")" "$run_dir" "$chunk_dir"

chunk_size=$(( (total_bytes + workers - 1) / workers ))
pids=()

for ((i=0; i<workers; i++)); do
  start=$((i * chunk_size))
  end=$((start + chunk_size - 1))
  if ((end >= total_bytes)); then
    end=$((total_bytes - 1))
  fi
  expected=$((end - start + 1))
  part=$(printf "%s/part-%03d" "$chunk_dir" "$i")
  if [[ -f "$part" ]] && [[ $(stat -c %s "$part") -eq $expected ]]; then
    continue
  fi
  (
    touch "$part"
    attempt=0
    while [[ $(stat -c %s "$part") -lt $expected ]]; do
      attempt=$((attempt + 1))
      [[ "$attempt" -le 100 ]]
      actual=$(stat -c %s "$part")
      request_start=$((start + actual))
      remainder="${part}.remainder"
      rm -f "$remainder"
      curl --fail --location --connect-timeout 20 --max-time 120 \
        --range "${request_start}-${end}" --output "$remainder" "$url" || true
      received=$(stat -c %s "$remainder" 2>/dev/null || printf 0)
      [[ "$received" -gt 0 ]]
      cat "$remainder" >> "$part"
      rm -f "$remainder"
      current=$(stat -c %s "$part")
      [[ "$current" -le "$expected" ]]
    done
    [[ $(stat -c %s "$part") -eq "$expected" ]]
  ) >"${run_dir}/download-part-$(printf "%03d" "$i").log" 2>&1 &
  pids+=("$!")
done

failure=0
for pid in "${pids[@]}"; do
  if ! wait "$pid"; then
    failure=1
  fi
done
[[ "$failure" -eq 0 ]]

assembled="${output}.assembling"
: > "$assembled"
for ((i=0; i<workers; i++)); do
  part=$(printf "%s/part-%03d" "$chunk_dir" "$i")
  cat "$part" >> "$assembled"
done
[[ $(stat -c %s "$assembled") -eq $total_bytes ]]

actual_md5=$(md5sum "$assembled" | awk '{print $1}')
[[ "$actual_md5" == "$expected_md5" ]]
tar -tzf "$assembled" >/dev/null
mv "$assembled" "$output"
printf "%s  %s\n" "$actual_md5" "$output" > "${run_dir}/CUB_200_2011.md5"
printf "DOWNLOAD_VERIFIED bytes=%s md5=%s\n" "$total_bytes" "$actual_md5"
