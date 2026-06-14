# Stage 1 v2: Dual-Session Information Gap + Currency-Sensitive Probes

> Date: 2026-06-15
> Scope: redesign of the Stage 1 diagnostic to fix the "M0 ≈ M3" non-result.
> Status: code + seeds implemented and structurally validated; API rerun pending.
> Supersedes the probe design in `stage1_pilot_10seed_2026-06-15.md`.

## Why This Redesign Exists

The 10-seed v1 pilot showed `M3_actionable` (38/50) only narrowly above `M0_GA`
(37/50). The audit (`gate1_failure_audit_2026-06-15.md`) traced this to two
benchmark defects, not a failure of the memory mechanism:

1. **No information gap.** M0_GA saw the *same full raw event log* that memory was
   formed from. A strong base model (gpt-5.4) re-derives the social state on the
   fly, so structured memory is redundant except where re-derivation is hard.
2. **Saturation / broken probes.** 3 of 5 probes did not discriminate: `probe_0002`
   and `probe_0005` were 10/10 for every condition; `probe_0003` failed everyone
   due to an observer-only targeting bug. The one clean signal (`probe_0004`,
   reduced-reliance planning: M3 7/10 vs placebo 0/10) was drowned in the average.

v2 fixes both at once. Doing only one is insufficient: probe fixes alone keep M0
able to re-derive; an information gap alone leaves the probes saturated.

## Change 1 (A): Dual-Session Information Gap

Each seed's event log is split by a new per-event `session` field:

- `session_1_past` (days 1-2): establishes every fact **and its update/contradiction**
  (secret scope revision, broken promise, reputation downgrade, partial-trust
  repair, norm violation, routine relocation).
- `session_2_current` (day 3): a minimal current window that only sets up the
  day-3 asks, without revealing the session-1 social history.

Who sees what:

| Condition | Context |
|---|---|
| M0_GA / M0_prompted | **session_2_current only** (single-session agent, no persistent memory) |
| memory module → M2 / M3 | full history (unchanged); structured memory carries session-1 state forward |
| M3_placebo | stale early-session-1 memory (pre-update), as before |

This is the correct SMGA ablation: all conditions get the same current session;
treatments additionally get persistent social memory. M0 is not "crippled" — it is
the no-persistent-memory baseline the thesis is about.

Implementation:
- `generate_stage1_seeds.py`: `event()` gained a `session` arg; events 0001-0013
  are `session_1_past`, events 0014-0016 are `session_2_current`.
- `baseline_harness.py`: `baseline_visible_events()` filters M0 to the current
  session; `format_event_history(package, events=...)` takes an explicit list.
  Untagged legacy seeds fall back to the full log (backward compatible).
- `memory_module.py`: unchanged; `format_event_history(package)` still returns all
  events.

Verified: for seed_0003, M0 sees only `event_0014/0015/0016`; the memory module
sees all 16 events.

## Change 2 (B): Currency-Sensitive, De-Saturated Probes

All five probes now point at a fact that was revised/contradicted in session 1 and
carry an explicit **stale trap** (`forbidden_response_markers`) = the answer that is
right given the early evidence but wrong given the update. So the placebo (stale
memory) fails reliably, and M0 (no session-1 evidence) cannot recover the right
answer by re-derivation.

| Probe | Type | Current-right answer | Stale trap (fails) |
|---|---|---|---|
| probe_0001 | planning | reduced reliance + verification on the partner | fully rely / partner already finished / trust fully restored |
| probe_0002 | privacy | share with the **core team** but not outside it | keep it from everyone / tell the external party |
| probe_0003 | norm_response | stop external sharing, acknowledge, notify core team **or** info owner | share more / no harm / keep sharing |
| probe_0004 | information_request | look in **the lab** (routine moved day 3) | look in the old routine place |
| probe_0005 | relationship_repair | keep rebuilding trust after the partial repair | nothing to fix / trust fully restored |

Notable fixes vs v1:
- **probe_0003 targeting bug fixed**: `required_target_entities` is now empty;
  success is scored on containment markers (notify core team *or* info owner both
  count), removing the observer-only false-fail.
- **probe_0004 replaces the saturated routine lookup**: a new session-1 event
  (`event_0013`) moves the routine from `routine_place` to the lab, with
  `fact_0005` marked `revised` and a new current `fact_0010`. The lookup now hinges
  on the update.
- **probe_0001 rubric sharpened** (Policy A from the audit): the partner may still
  own the pass **if** the plan adds explicit checks / reduced reliance; the hard
  `follow_commitment` ban was dropped in favor of failure markers for treating
  trust as fully restored.

All five probes keep `no_history_solvability_flag: false`, so all are headline
probes — and all now genuinely require memory.

## Predicted Effect

- M0 (session-2 only) lacks the session-1 evidence → naive answers → fails the
  currency-sensitive probes. This opens an **M3 vs M0** gap that v1 lacked.
- M3_actionable (current structured memory) → passes.
- M3_placebo (stale early memory) → falls into the stale traps → fails. The **M3 vs
  placebo** gap is preserved and sharpened.

Both the M3-vs-M0 and M3-vs-placebo contrasts should now be clean, instead of only
the placebo gap.

## Open Items Before the API Rerun

1. **seed_0001 / seed_0002 are hand-authored and untagged**, so they currently get
   the full-log fallback (no information gap). Either migrate them to the dual-session
   structure or run the v2 pilot on seed_0003–0010 only and report that scope.
2. The judge rubric reads multi-entity `required_target_entities` as conjunctive;
   v2 sidesteps this for probe_0003 by using markers instead. If future probes need
   "any one of" targets, extend `build_rubric` accordingly.
3. Concurrency is enabled (`max_concurrency: 5` in the fhl config), so the rerun is
   ~3-5x faster per condition.

## Files Touched

```text
benchmarks/diagnostic_v0/generate_stage1_seeds.py   dual-session events + v2 probes + routine-move fact
benchmarks/diagnostic_v0/baseline_harness.py        session-windowed M0 context
benchmarks/diagnostic_v0/model_calling_runner.py    thread-pool concurrency (--workers / max_concurrency)
benchmarks/diagnostic_v0/configs/fhl_...json        max_concurrency: 5
benchmarks/diagnostic_v0/seeds/seed_0003..0010/     regenerated
```
