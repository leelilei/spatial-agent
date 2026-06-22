# PROV-text-norm strong attribution run

Date: 2026-06-22 night / 2026-06-23 early

Question: if provenance is carried only in utterance text, can an explicit attribution norm
repair the PROV-text-free failure without hidden metadata or broadcast?

Config:

```text
python sim/run_society_sweep.py \
  --memory provtextnorm \
  --runs 3 \
  --seed 301 \
  --agent-count 25 \
  --rounds 10 \
  --turns 2 \
  --meetings 1 \
  --workers 4 \
  --model gpt-5.4-mini \
  --scenario repair_drive \
  --out-dir sim/runs/provtext_norm_r10_n3
```

Completed rows:

```text
seed 301: 25 current, 0 stale, 0 unknown
seed 302: 25 current, 0 stale, 0 unknown
seed 303: 25 current, 0 stale, 0 unknown

total:    75/75 current = 100%; 0 stale; 0 unknown
```

Retention audit:

```text
run_000: source/version-like markers in 200/240 utterances; 25/25 agents version>=1
run_001: source/version-like markers in 221/240 utterances; 25/25 agents version>=1
run_002: source/version-like markers in 189/240 utterances; 25/25 agents version>=1
```

Interpretation:

This is a strong positive mechanism result, but not a natural-human dialogue result. The
current norm is deliberately protocolized: agents are instructed to say phrases like
`Official round 1 update`. The run should be treated as a strong attribution-norm upper
bound for text-only provenance, not as evidence that ordinary human-like conversation
naturally preserves provenance.

Paper-facing conclusion:

PROV-text-free shows that default LLM dialogue drops provenance. PROV-text-norm shows that
if a society adopts an explicit attribution norm, provenance can propagate through text and
repair held truth without broadcast. The next realistic experiment should weaken the norm
into natural attribution language and test whether gains survive.
