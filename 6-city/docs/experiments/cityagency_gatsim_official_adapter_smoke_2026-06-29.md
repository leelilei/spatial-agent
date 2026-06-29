# CityAgency GATSim Official Adapter Smoke Run

Date: 2026-06-29

## Question

Can CityAgency evaluate a real external city-agent planning component rather
than only locally designed architecture proxies?

## External Provenance

- framework: GATSim
- official repository: `https://github.com/qiliuchn/gatsim`
- pinned commit: `3dc40248086cdfb1eca38d22b76b0edb5fe53ea6`
- integration level: `adapted_official_planner`
- native full backend: no
- model provider: `fhl`
- model: `gpt-5.4-mini`

The setup tool verifies the repository remote, commit, and SHA-256 hashes of
GATSim's official `generate_prompt` source plus the daily-plan and update-plan
templates. The adapter executes that official renderer and preserves GATSim's
six-field activity schema. CityAgency owns the micro-city state, typed action
execution, and deterministic scoring.

This is therefore a real integration of GATSim's official planner interface,
but it is not a claim that the complete native GATSim simulator is running.

## Scenarios

| Scenario | Goal completion | Trace feasibility | Plausibility-feasibility gap | Replanning success |
|---|---:|---:|---:|---:|
| `budget_errand_chain` | 1.0 | 1.0 | 0.0 | N/A |
| `closed_poi_replacement` | 0.75 | 0.667 | 0.333 | N/A |
| `commute_disruption` | 0.5 | 0.0 | 1.0 | 0.0 |

Aggregate results:

- plan plausibility: 1.0
- trace feasibility: 0.556
- plausibility-feasibility gap: 0.444
- impossible trace rate: 0.444
- goal completion: 0.75
- feasibility violation: 0.444
- budget consistency: 1.0

## What The Run Shows

1. The external integration works end to end.

   A real provider generated GATSim-format plans, CityAgency converted and
   executed them, and every trace records the framework, model, source commit,
   verification state, and integration boundary.

2. The benchmark catches a plan-to-trace failure hidden by fluent text.

   In `commute_disruption`, the reflection said the blocked
   `transit_hub-office` edge should be avoided, but the structured plan selected
   `shortest`. Execution crossed the blocked edge, producing a 1.0
   plausibility-feasibility gap and failed replanning.

3. Destination choice alone is not enough.

   In `closed_poi_replacement`, the selected destinations sounded reasonable,
   but the executed route passed through the closed library. The verifier
   exposed the route-level violation.

4. GATSim's explicit path field must be preserved.

   An earlier bridge discarded the official path field and let CityAgency
   silently recompute a shortest path. The adapter and executor now preserve
   and validate explicit framework-provided routes, so route failures belong to
   the tested plan rather than the bridge.

## Artifacts

- `benchmarks/cityintent_v0/external_adapters/gatsim_manifest.json`
- `benchmarks/cityintent_v0/external_adapters/gatsim_official.py`
- `benchmarks/cityintent_v0/tools/setup_external_framework.py`
- `results/cityintent_v0/gatsim_official_smoke_gpt54mini_2026-06-29/`

## Interpretation

This three-scenario smoke run is not a framework ranking. Its useful result is
that CityAgency can now distinguish an official external planner's plausible
urban narrative from the feasibility of its executed spatial trace. The next
fair comparison should run the same model and scenarios through GATSim's
adapted planner, direct action, plan-then-act, and reactive replanning policies
with repeated seeds.
