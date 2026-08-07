#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OUT="$ROOT/paper/dai2026/dai2026_anonymous_artifact.zip"
STAGE="$(mktemp -d)"
ART="$STAGE/telephone_dai2026_artifact"
trap 'rm -rf "$STAGE"' EXIT

mkdir -p "$ART"

copy_path() {
  local rel="$1"
  local src="$ROOT/$rel"
  local dst="$ART/$rel"
  if [[ -d "$src" ]]; then
    mkdir -p "$dst"
    rsync -a --exclude '__pycache__' --exclude '*.pyc' "$src/" "$dst/"
  else
    mkdir -p "$(dirname "$dst")"
    cp "$src" "$dst"
  fi
}

code_paths=(
  sim/society.py
  sim/memories.py
  sim/llm.py
  sim/run_society_sweep.py
  sim/pool_runs.py
  sim/judge_rescore.py
  sim/replay_eval.py
  sim/fixed_stream_integration_eval.py
  sim/matched_policy_ablation.py
  sim/requirements.txt
)

doc_paths=(
  RESULTS.md
  docs/project/data_index.md
  docs/project/code_data_audit_2026-07-06.md
  docs/project/fixed_stream_integration_audit_2026-07-23.md
  docs/project/matched_policy_ablation_audit_2026-07-23.md
  paper/dai2026/main.tex
  paper/dai2026/references.bib
  paper/dai2026/figures
)

run_paths=(
  sim/runs/m4_rebroadcast
  sim/runs/prov_fair/prov
  sim/runs/fixed_stream_integration_2026-07-23
  sim/runs/matched_policy_ablation_2026-07-23
  sim/runs/table_repair
  sim/runs/table_3scenario
  sim/runs/dues
  sim/runs/topology
  sim/runs/p3_power
  sim/runs/g2_persona
  sim/runs/provtext_llm_only_r10_n5
  sim/runs/provtext_norm_r10_n3
  sim/runs/cap_c16_mini_adversary
  sim/runs/cap_c17_mini_sparse_r10
  sim/runs/cap_c17_mini_sparse_r10_ext
  sim/runs/cap_deepseek_prov_vs_ga_pilot
  sim/runs/cap_deepseek_prov_vs_ga_n8ext
  sim/runs/cap_deepseek_prov_n8fill
  sim/runs/cap_deepseek_prov_seed44
)

for rel in "${code_paths[@]}" "${doc_paths[@]}" "${run_paths[@]}"; do
  copy_path "$rel"
done

cp "$ROOT/paper/dai2026/ARTIFACT_README.md" "$ART/README.md"

# Remove local absolute paths from text-like files in the staged copy.
while IFS= read -r -d '' file; do
  perl -pi -e 's#\Q'"$ROOT"'\E#<REPO_ROOT>#g; s#/Users/[^/[:space:]"]+#<USER_HOME>#g' "$file"
done < <(find "$ART" -type f \( -name '*.json' -o -name '*.md' -o -name '*.py' -o -name '*.tex' -o -name '*.bib' -o -name '*.txt' \) -print0)

# Fail closed on identity paths or common live-secret representations.
if rg -n '/Users/|Bearer[[:space:]]+[A-Za-z0-9._-]{20,}|"api[_-]?key"[[:space:]]*:[[:space:]]*"[^"]+"' "$ART"; then
  echo "artifact privacy scan failed" >&2
  exit 1
fi

(
  cd "$ART"
  find . -type f ! -name SHA256SUMS -print0 \
    | sort -z \
    | xargs -0 shasum -a 256 > SHA256SUMS
)

rm -f "$OUT"
(
  cd "$STAGE"
  zip -qry "$OUT" "$(basename "$ART")"
)

echo "$OUT"
