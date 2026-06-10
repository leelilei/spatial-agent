# SMGA Diagnostic Benchmark v0

This benchmark is the first controlled diagnostic benchmark for the v4.6 SMGA plan.

Current contents:

```text
seeds/seed_0001/
```

`seed_0001` is a hand-authored Experiment 0 seed. It is designed to validate schema, parsing, scorer behavior, and memory-module wiring before generating larger seed batches.

Validate all seeds:

```bash
python3 validate_seed.py
```

Validate a specific seed:

```bash
python3 validate_seed.py seeds/seed_0001
```

Score example normalized probe responses:

```bash
python3 probe_success_scorer.py \
  seeds/seed_0001 \
  examples/seed_0001_probe_responses.json
```
