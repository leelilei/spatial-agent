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

Load a seed and print its package summary:

```bash
python3 benchmark_loader.py seeds/seed_0001
```

Prepare baseline prompt bundles and scorer-readable response templates:

```bash
python3 baseline_harness.py seeds/seed_0001 --condition all
```

Run a baseline prompt bundle through the offline mock provider:

```bash
python3 model_calling_runner.py \
  tmp/smga_baseline_harness/seed_0001_M0_GA_prompts.jsonl \
  --provider mock \
  --response-template tmp/smga_baseline_harness/seed_0001_M0_GA_responses.template.json
```

Run a prompt bundle through OpenAI Chat Completions after setting `OPENAI_API_KEY`:

```bash
python3 model_calling_runner.py \
  tmp/smga_baseline_harness/seed_0001_M0_GA_prompts.jsonl \
  --config configs/baseline_model_config.example.json \
  --response-template tmp/smga_baseline_harness/seed_0001_M0_GA_responses.template.json
```

Normalize a raw response draft into scorer-readable fields:

```bash
python3 response_normalizer.py \
  seeds/seed_0001 \
  tmp/smga_baseline_harness/seed_0001_M0_GA_responses.raw_draft.json
```

Score example normalized probe responses:

```bash
python3 probe_success_scorer.py \
  seeds/seed_0001 \
  examples/seed_0001_probe_responses.json
```
