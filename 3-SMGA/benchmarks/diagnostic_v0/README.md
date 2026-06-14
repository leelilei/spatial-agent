# SMGA Diagnostic Benchmark v0

This benchmark is the first controlled diagnostic benchmark for the v4.6 SMGA plan.

Current contents:

```text
seeds/seed_0001/ ... seeds/seed_0010/
```

`seed_0001` and `seed_0002` are hand-authored Experiment 0 seeds. They are
designed to validate schema, parsing, scorer behavior, and memory-module wiring
before generating larger seed batches. `seed_0003` through `seed_0010` are
template-generated Stage 1 diagnostic seeds created by
`generate_stage1_seeds.py`.

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

Generate the Stage 1 diagnostic seed expansion:

```bash
python3 generate_stage1_seeds.py --start 3 --end 10
```

Prepare baseline prompt bundles and scorer-readable response templates:

```bash
python3 baseline_harness.py seeds/seed_0001 --condition all
```

## Model Providers

The model runner reads provider settings from JSON files in `configs/`.

Current provider configs:

- `configs/baseline_model_config.example.json`: OpenAI-compatible Chat Completions template.
- `configs/fhl_responses_gpt54_config.example.json`: tested `fhl` Responses API config using `gpt-5.4`.
- `configs/fhl_responses_minimal_config.example.json`: `fhl` Responses API config using `gpt-5.4-mini`; useful for comparison, but `seed_0001` showed intermittent 502s on this model.

Set provider keys in the shell before running real model calls:

```bash
export FHL_API_KEY="..."
```

or:

```bash
export OPENAI_API_KEY="..."
```

Do not commit real API keys. For a persistent local shell setting, put the export line in `~/.zshrc`.

The tested `fhl` path uses:

```json
{
  "provider": "fhl",
  "model": "gpt-5.4",
  "wire_api": "responses",
  "base_url": "https://www.fhl.mom",
  "transport": "curl",
  "responses_input_mode": "string",
  "omit_temperature": true,
  "json_mode": false,
  "disable_response_storage": true
}
```

`transport: "curl"` is intentional: direct Python `urllib` calls produced intermittent 502s through the `fhl`/Cloudflare path, while curl transport succeeded. The config also includes conservative retry/backoff settings.

## Running Baselines

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

Run a prompt bundle through the `fhl` Responses API after setting `FHL_API_KEY` or `OPENAI_API_KEY`:

```bash
python3 model_calling_runner.py \
  tmp/smga_baseline_harness/seed_0001_M0_GA_prompts.jsonl \
  --config configs/fhl_responses_gpt54_config.example.json \
  --response-template tmp/smga_baseline_harness/seed_0001_M0_GA_responses.template.json \
  --output-dir tmp/fhl_gpt54_baseline
```

Run a single probe when debugging or filling a failed call:

```bash
python3 model_calling_runner.py \
  tmp/smga_baseline_harness/seed_0001_M0_GA_prompts.jsonl \
  --config configs/fhl_responses_gpt54_config.example.json \
  --probe-id probe_0002 \
  --raw-output tmp/smga_baseline_harness/repair_seed_0001_M0_GA_probe_0002_raw_outputs.jsonl
```

When filling a failed call, merge the repaired raw record into the existing
condition raw output / response draft before rerunning the judge. Passing
`--response-template` with `--probe-id` creates a draft with only that selected
probe filled.

Print non-secret resolved config:

```bash
python3 model_calling_runner.py \
  tmp/smga_baseline_harness/seed_0001_M0_GA_prompts.jsonl \
  --config configs/fhl_responses_gpt54_config.example.json \
  --print-config
```

Print the first non-secret provider payload:

```bash
python3 model_calling_runner.py \
  tmp/smga_baseline_harness/seed_0001_M0_GA_prompts.jsonl \
  --config configs/fhl_responses_gpt54_config.example.json \
  --print-first-payload
```

Normalize an `M0_GA` raw response draft into scorer-readable fields:

```bash
python3 response_normalizer.py \
  seeds/seed_0001 \
  tmp/fhl_gpt54_baseline/seed_0001_M0_GA_responses.raw_draft.json
```

Score normalized `M0_GA` responses:

```bash
python3 probe_success_scorer.py \
  seeds/seed_0001 \
  tmp/fhl_gpt54_baseline/seed_0001_M0_GA_responses.normalized.json
```

Score example normalized probe responses:

```bash
python3 probe_success_scorer.py \
  seeds/seed_0001 \
  examples/seed_0001_probe_responses.json
```

## Current Baseline Result

First real `M0_GA` run:

```text
provider: fhl
model: gpt-5.4
seed: seed_0001
condition: M0_GA
score: 4/5 headline probes passed (80.0%)
failed probe: probe_0004
failure reason: not enough required response markers
```

The `probe_0004` failure is interpretable: the model selected a broadly correct planning direction, but did not explicitly include enough planning-grounding markers such as `verify` or `less rely`.

## Full Pipeline & Automated Runs (memory → conditions → judge)

The end-to-end Experiment 0 pipeline. Every model-calling step goes through
`model_calling_runner.py` (the only transport that reliably reaches the `fhl`
provider — see Model Providers above).

### API key handling

Real runs need the provider key in the environment. The key must NOT be written
into any committed file; it lives only in the shell environment:

```bash
export FHL_API_KEY="sk-..."   # one-off in the current shell
```

For a persistent setting, add that `export` line to `~/.zshrc`.

Note for automated/assistant runs: a non-interactive shell does not auto-source
`~/.zshrc`, so scripts are invoked with the key loaded explicitly from it:

```bash
eval "$(grep -E '^[[:space:]]*export[[:space:]]+FHL_API_KEY=' ~/.zshrc)"
python3 <script> ...   # the key is now in the env for this command only
```

This keeps the secret in the user's `~/.zshrc` and out of the repo while letting
the runner / judge / memory module call the API directly.

### Components

- `memory_module.py` — Module A. A model reads only the entity catalog + event
  history (condition-blind, no probes/gold) and forms `StructuredSocialMemory`
  objects, validated against the schema.
- `treatment_harness.py` — serializes the shared memory set two ways:
  `M2_memory_only` (plain-text notes) and `M3_actionable` (structured objects +
  optional planning-affordance hints, respecting `currency_status`). It also
  builds `M3_placebo`, an interface-matched stale-memory control constructed
  from the early log before current-update events.
- `judge_scorer.py` — condition-blind LLM-judge. Builds one judge prompt per
  probe (probe + plain-language rubric from the locked success/failure conditions
  + the agent's answer) and returns per-probe pass + rationale. Replaces brittle
  keyword/affordance matching for headline scoring.
- `probe_success_scorer.py` (v0.2) — keyword scorer kept as a fast mechanical
  check; affordance acceptability now uses a candidate set, forbidden affordance
  uses the dominant label only.

### Run order (per seed)

```bash
SEED=seeds/seed_0001
CFG=configs/fhl_responses_gpt54_config.example.json

# 0. validate the seed
python3 validate_seed.py $SEED

# 1. baselines: build prompts, run, judge
python3 baseline_harness.py $SEED --condition all --output-dir tmp/smga_baseline_harness
python3 model_calling_runner.py tmp/smga_baseline_harness/<seed>_M0_GA_prompts.jsonl --config $CFG \
  --response-template tmp/smga_baseline_harness/<seed>_M0_GA_responses.template.json --output-dir tmp/smga_baseline_harness
python3 judge_scorer.py $SEED tmp/smga_baseline_harness/<seed>_M0_GA_responses.raw_draft.json --config $CFG

# 2. memory formation (Module A)
python3 memory_module.py $SEED --config $CFG --output-dir tmp/smga_memory

# 3. treatment: build M2/M3 prompts, run, judge
python3 treatment_harness.py $SEED tmp/smga_memory/<seed>_memory_artifact.json
python3 model_calling_runner.py tmp/smga_treatment/<seed>_M3_placebo_prompts.jsonl --config $CFG \
  --response-template tmp/smga_treatment/<seed>_M3_placebo_responses.template.json --output-dir tmp/smga_treatment
python3 judge_scorer.py $SEED tmp/smga_treatment/<seed>_M3_placebo_responses.raw_draft.json --config $CFG
python3 model_calling_runner.py tmp/smga_treatment/<seed>_M3_actionable_prompts.jsonl --config $CFG \
  --response-template tmp/smga_treatment/<seed>_M3_actionable_responses.template.json --output-dir tmp/smga_treatment
python3 judge_scorer.py $SEED tmp/smga_treatment/<seed>_M3_actionable_responses.raw_draft.json --config $CFG
```

For resume-friendly Stage 1 execution across a seed range:

```bash
python3 run_stage1_pilot.py --start 1 --end 10
```

### Result snapshot (LLM-judge, 10 seeds x 5 probes)

```text
condition         pass/total   rate
M0_GA              37/50       74%
M0_prompted        35/50       70%
M2_memory_only     33/50       66%
M3_placebo         28/50       56%
M3_actionable      38/50       76%
```

Headline diagnostic: `M3_actionable` is strongest, but narrowly above `M0_GA`.
The clearer mechanism signal is the gap over the interface-matched stale
placebo (38/50 vs 28/50), especially on reduced-reliance planning
(`probe_0004`: 7/10 vs 0/10). See
`docs/project/stage1_pilot_10seed_2026-06-15.md`.
