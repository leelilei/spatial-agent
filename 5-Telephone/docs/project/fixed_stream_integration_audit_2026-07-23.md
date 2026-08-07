# Fixed-stream integration audit (2026-07-23)

## Decision

The bounded mechanism experiment passes. When every agent receives the same frozen event stream,
PROV produces substantially more current HELD answers than GA. This establishes listener-side
integration as a causal intervention point under matched received evidence. It does **not** show
that integration is the only mechanism, nor that natural dialogue preserves provenance metadata.

## Design

- Source streams: the eight completed `prov_fair/prov` runs, schedule seeds 41--48.
- Society: 25 agents, five rounds, `gpt-5.4-mini`.
- Independent unit: one schedule seed / realized society stream, not an individual agent.
- Frozen input: for each seed, both replay conditions receive the identical per-agent sequence of
  text observations and structured provenance metadata.
- Manipulation: fresh GA and PROV memories represent, consolidate, retrieve, and answer from that
  same evidence. No new society dialogue is generated during replay.
- Outcome: final current / stale / unknown HELD interview, using the existing interview prompt and
  marker scoring.
- Statistics: seed-level rates, paired PROV-minus-GA differences, 95% t intervals across eight
  seeds, plus an exact two-sided sign test over the paired directions.

### Reconstruction audit

The replay tool reconstructs the provenance payload on every utterance from the original round
logs, respecting the simulator order: all encounters are generated from the state at the start of
the round, observations are then committed, and the authoritative injection occurs last. For every
seed and every agent, the reconstructed final version/value matches the original PROV memory
snapshot exactly. Provenance reached 10--19 of 25 agents across streams, so the test is not an
all-agent overwrite.

## Results

| Condition | Current | Stale | Unknown | Pooled counts |
|---|---:|---:|---:|---:|
| GA | 32.0% [28.0, 36.0] | 7.5% [1.2, 13.8] | 60.5% [52.6, 68.4] | 64 / 15 / 121 |
| PROV | 60.5% [52.8, 68.2] | 5.0% [0.7, 9.3] | 34.5% [27.1, 41.9] | 121 / 10 / 69 |

Paired current-rate differences by seed were `+36, +28, +40, +32, +12, +24, +28, +28`
percentage points. The mean paired lift is **+28.5 points [21.5, 35.5]**. PROV is higher in
8/8 seeds; exact two-sided sign-test `p = 0.0078125`. For the net current-minus-stale outcome, the
paired lift is **+31.0 points [25.1, 36.9]**.

The main change is not a large stale-to-current conversion. PROV reduces unknown answers
(60.5% to 34.5%) by preserving a directly retrievable current version. The lowest-coverage stream
(seed 45; 10/25 provenance receivers) has the smallest lift (+12 points), preserving the honest
boundary that communication reach still limits the ceiling.

## Valid interpretation

Use:

> In a matched-event replay over eight independent society streams, holding every agent's received
> observations fixed, provenance-aware integration raised HELD-current from 32.0% to 60.5%
> (paired difference +28.5 percentage points, 95% CI [21.5, 35.5]; PROV higher in 8/8 seeds).
> Listener-side integration is therefore causally consequential, rather than merely correlated
> with the different conversations produced by the two architectures.

Do not use:

- "Integration is the only cause of the dissociation."
- "This replay proves natural dialogue carries provenance."
- "The input is architecture-neutral." The frozen streams are realized PROV-run conversations and
  include structured provenance metadata; the diagnostic conditions on that metadata being
  available and isolates what listeners do with it.

## Reliability and exclusions

- Provider failures are never scored as unknown. A condition is accepted only with 25/25 completed
  agent replays; per-agent checkpoints make retries resumable.
- One early FHL attempt for seed 43 was discarded after a provider failure, then rerun completely.
- A four-agent DeepSeek transport pilot was stopped for latency and was never aggregated.
- The first two completed seeds used the original world-level replay loop; the remaining seeds used
  the checkpointed per-agent loop. Under a fixed stream the memories are conditionally independent,
  and both loops apply the same per-round observe/consolidate/retrieve/interview operations.

## Artifacts

- Runner: `sim/fixed_stream_integration_eval.py`
- Shared replay utility: `sim/replay_eval.py`
- Accepted outputs: `sim/runs/fixed_stream_integration_2026-07-23/`
- Aggregate: `sim/runs/fixed_stream_integration_2026-07-23/aggregate.json`
- Compact seed table: `sim/runs/fixed_stream_integration_2026-07-23/per_seed_summary.csv`
- Per-seed manifests, frozen streams, interviews, memory snapshots, and results are retained under
  `seed_41/` through `seed_48/`.
