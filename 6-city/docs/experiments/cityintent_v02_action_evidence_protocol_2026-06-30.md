# CityIntent v0.2 Action-Evidence Protocol Pilot

Date: 2026-06-30

## Research Question

Can an urban LLM agent execute a plausible plan as a legal, continuous, and
verifiable trace, rather than receiving credit for merely arriving at or
passing through a location?

## Protocol Change

CityIntent v0.2 separates five claims that v0.1 conflated:

1. `move`: arrive outside a graph location.
2. `enter`: enter an open place and create entry evidence.
3. `buy`: purchase a named item and deduct the place cost.
4. `use_service`: complete a named service and deduct the place cost.
5. `dwell`: remain inside; paid places require prior purchase/service evidence.

Every scored condition now stores its supporting evidence. Starting at home no
longer counts as evidence for a later `return_home` condition with
`ignore_start=true`.

## Verification

- Four protocol unit tests pass: arrival is not entry, pass-through is not
  entry, purchase requires entry and charges once, closed entry/unpaid dwell
  are rejected, and ignored start state is not return evidence.
- The deterministic utility baseline completes 10 of 12 scenarios with full
  feasibility and full goal completion.
- The two remaining failures are the commute scenarios where a multi-edge
  `move` crosses an event that appears mid-route. This exposes the next
  environment issue: movement needs an interruptible decision boundary.

## Real-Model Framework Pilot

Configuration: `gpt-5.4-mini`, temperature 0, one run, one
`budget_errand_chain` scenario, four adapters pinned to verified official
decision-layer sources. These are adapted official decision layers, not native
full-framework backends.

| Adapter | Goal | Trace feasibility | Calls | Tokens | Diagnostic outcome |
|---|---:|---:|---:|---:|---|
| GATSim | 1.00 | 1.00 | 1 | 8,986 | Entered, bought medicine, used meal service, and re-entered home |
| SOTOPIA | 0.55 | 0.60 | 6 | 39,757 | Tried to buy before entry, missed meal and return-home evidence |
| Generative Agents | 0.55 | 1.00 | 1 | 6,723 | Legal trace, but did not execute meal or return-home completion |
| AgentSociety | 0.50 | 0.80 | 4 | 27,395 | Tried to buy before entry; completed meal but not medicine or return home |

All token counts came from provider usage fields. The archive contains raw
traces, JSONL, metric tables, condition evidence, per-call telemetry, aggregate
telemetry, and a sanitized run manifest.

## Interpretation

This pilot validates the measurement object, not an architecture ranking. All
four outputs are surface-plausible, but the verifier separates successful task
execution, legal-but-incomplete behavior, and invalid state transitions. The
large call/token differences also show why performance must be reported with
cost and latency.

A preliminary development run was overwritten while correcting the evidence
filter and is excluded. The runner now refuses to overwrite an existing trace
archive unless `--overwrite` is explicit.

## Next Experiment

1. Make route traversal interruptible at newly observed events.
2. Run four diagnostic scenarios across the four adapters with at least three
   repeats per cell.
3. Report mean, standard deviation, completion evidence type, invalid state
   transitions, calls, tokens, and latency.
4. Treat architecture comparisons as exploratory until the repeated table and
   human audit are complete.

Archive:
`results/cityintent_v02/four_framework_action_evidence_smoke_gpt54mini_2026-06-30/`
