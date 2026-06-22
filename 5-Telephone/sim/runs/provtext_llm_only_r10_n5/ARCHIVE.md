# Archive Note -- PROV-text-free real LLM run

Date: 2026-06-22

Purpose: test whether provenance can survive as ordinary natural-language attribution in
real LLM dialogue, without the hidden structured `event["prov"]` relay used by structured
PROV.

Command is preserved in `run_config.json`; stdout/stderr are preserved as `_stdout.log`
and `_stderr.log`.

## Completed Rows

`aggregate.json` and `runs.json` were reconstructed after stopping the process. They include
only runs whose `sim_summary.json` contains `currency_interview`.

```text
PROV-text-free: 3 complete runs, 16/75 current, 0/75 stale, 59/75 unknown
held-current rate: 21.3%
```

Per seed:

```text
seed 301: 5 current, 0 stale, 20 unknown
seed 302: 3 current, 0 stale, 22 unknown
seed 303: 8 current, 0 stale, 17 unknown
```

## Source/Version Retention Audit

Across the three complete runs:

```text
utterances containing source/version markers: 0/720
agents holding version>=1 in memory snapshots: 1/25 per run (only a01/Rosa)
```

Thus ordinary LLM dialogue did not spontaneously preserve the provenance phrase needed for
PROV-text propagation. The condition collapses mainly to `unknown`, not `stale`.

## Incomplete / Excluded Rows

- `provtext/run_003`: created by the runner after seed 303, but the process was manually
  stopped before any round logs were written. Excluded from aggregate.

## Interpretation

This is a negative mechanism result. It does not refute provenance-aware memory; it shows
that provenance must be preserved by the communication layer. The next target is
PROV-text-norm: explicit source/version attribution carried in natural language.
