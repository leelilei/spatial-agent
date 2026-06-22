# Archive Note -- PROV-text comparator long run

Date: 2026-06-22

Purpose: attempted same-run comparison of GA, structured PROV, and PROV-text under real
LLM dialogue. The run was manually stopped after the user decided not to spend more budget
on structured PROV and to prioritize PROV-text.

Command is preserved in `run_config.json`; stdout/stderr are preserved as `_stdout.log`
and `_stderr.log`.

## Completed Rows

`aggregate.json` and `runs.json` were reconstructed after stopping the process. They include
only runs whose `sim_summary.json` contains `currency_interview`.

```text
GA:   4 complete runs, 21/100 current, 4/100 stale, 75/100 unknown
PROV: 2 complete runs, 50/50 current, 0/50 stale, 0/50 unknown
```

## Incomplete / Excluded Rows

- `ga/run_000`: failed after round 0 because the Responses API returned HTTP 403 content
  policy violation. Excluded from aggregate.
- `prov/run_002`: completed 10 conversation rounds and memory snapshots, but the run was
  stopped before a currency interview was written. Excluded from aggregate.

## Interpretation

This directory is useful as a comparator archive, not as the final PROV-text result. It
confirms the expected contrast: GA remains low/unknown-dominated, while structured PROV is
an idealized upper bound under preserved provenance.
