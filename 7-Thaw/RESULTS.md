# Thaw — Results

## Experiment ledger

| date | id | question | configuration | result | status |
|---|---|---|---|---|---|
| 2026-06-30 | A0 | Does Telephone's old late-broadcast failure reproduce? | 25a, m2, r5, t3, seed41, last round index=4, all-agent broadcast, forget=0 | **No. 25/25 current.** Audit found old `r5_broadcast` logs had zero injections. Telephone P1-rec retracted. | closed; premise invalid |
| 2026-06-30 | H1a | Does a narrow persistent source create a useful frozen baseline without explicit old-fact initialization? | 10a, m2, r5, t2, seed41, source inject r1-r4, forget=0 | 4 current / 0 stale / 6 unknown; only 1 stale utterance. This is propagation shortage, not a frozen wrong attractor. | rejected as H1 baseline |
| 2026-06-30 | H1b | Can explicit stale initialization create a real frozen incumbent? | 8a, m2, r6, t2, seed41; old fact initially observed by all; source correction r3-r5; forget=0 | **2 current / 6 stale.** Social rehearsal: 4 current vs 65 stale utterances. Valid frozen pilot regime. | gate passed |
| 2026-06-30 | H1c | Does memory decay thaw H1b? | same as H1b; forget={0.5,0.8} | Both give 3 current / 5 stale vs 2/6 control. Stale rehearsal falls 65→61→55; at r5, 11→11→4. **Weak candidate signal, n=1.** | de-risk only; needs seeds |
| 2026-07-01 | H1c-ext | Does the n=1 thaw signal replicate at adequate power? | same as H1b/H1c; forget={0,0.5,0.8}, seeds 42-46 (n=5 each, 40 agents/cell) | **No.** Held-current: 40%→22.5%→40% (non-monotone, dip at 0.5, not a rise). Stale rehearsal utterances flat: 73.0→75.75→72.6. Neither go/no-go criterion met. `forget_0.5/seed42` social_rehearsal.json extraction failed (empty trajectory; currency_interview unaffected) — noted, not load-bearing for the verdict. | **NO-GO — H1 (monotone thaw) rejected** |

## Audit finding that changed the project

Telephone P1-rec compared an early all-agent broadcast against a purported final-round all-agent
broadcast. Raw `round_*.json` logs show that the latter condition injected into zero agents in all
five runs. With the correct zero-based last-round index (`4` for a five-round simulation), the
same all-agent update yields 25/25 current. Thaw therefore cannot study recovery from that claimed
failure; the treatment already works without forgetting.

See `../5-Telephone/docs/project/p1_rec_audit_2026-06-30.md`.

## Revised H1 pilot

The valid pilot deliberately creates the state Thaw needs:

1. Before round 0, every agent observes the old plan (Saturday / front porch).
2. Agents discuss it for three rounds, producing active social rehearsal.
3. At rounds 3, 4, and 5, only the authoritative source receives the new plan
   (Sunday / community center); everyone else must learn socially.
4. GA-accessible memories decay by `forget_rate`; newly heard evidence starts at full strength.

### Seed 41 de-risk result

| forget rate | held current | held stale | current utterances | stale utterances | r5 current/stale utterances |
|---:|---:|---:|---:|---:|---:|
| 0.0 | 2/8 | 6/8 | 4 | 65 | 1 / 11 |
| 0.5 | 3/8 | 5/8 | 5 | 61 | 3 / 11 |
| 0.8 | 3/8 | 5/8 | 5 | 55 | 3 / 4 |

Interpretation: high decay visibly suppresses late stale rehearsal, consistent with the proposed
decay-vs-rehearsal competition, but the endpoint gain is only one agent and could easily be seed
noise. There is no evidence yet for a phase transition, a robust thaw, or an inverted-U optimum.

## Go / no-go rule

Run matched seeds for rates `{0, 0.5, 0.8}`. Continue only if forgetting produces both:

- a repeatable reduction in stale rehearsal; and
- a repeatable increase in held-current beyond schedule variance.

If rehearsal falls but held-current does not move, forgetting is only communication friction and
Thaw should stop. If both move, add intermediate rates and trajectory interviews to locate a
Frozen → Thawed → Amnesic boundary.

## Verdict (2026-07-01): H1 (monotone thaw) rejected, seeds 42-46, n=5/cell

The seed-41 de-risk signal (held-current rising 25%→37.5%→37.5% as forget rate rises) does not
replicate at n=5:

| forget rate | held current | current rate | per-seed current (42,43,44,45,46) |
|---:|---:|---:|---|
| 0.0 | 16/40 | 40.0% | 2,4,2,6,2 |
| 0.5 | 9/40 | 22.5% | 2,2,2,2,1 |
| 0.8 | 16/40 | 40.0% | 3,3,3,2,5 |

Rehearsal-utterance totals are flat across rates (mean current/stale utterances per run:
0.0 → 4.8/73.0; 0.5 → 3.5/75.75 [n=4, one run's rehearsal extraction failed]; 0.8 → 5.6/72.6) — no
reduction in stale rehearsal with higher forgetting, and held-current dips (not rises) at 0.5
before returning to the forget=0 baseline at 0.8. Both go/no-go criteria fail. The seed-41 result
was noise, exactly what the go/no-go rule was designed to catch.

**Conclusion: simple per-round accessibility decay does not thaw a frozen incumbent.** Forgetting
at these rates is at best neutral, not a re-correction mechanism, on this scenario/config. H1 in
its current (monotone, single-mechanism) form is closed as a negative result. The non-monotone dip
at 0.5 is noted but not investigated further — group variance there is suspiciously low (per-seed
current stuck near 2) which could be a real secondary effect or an artifact of this particular
scenario/seed range, but chasing it now would be underpowered speculation, not a finding.

**Not yet ruled out** (open for a future pass, not committed): forgetting-at-the-communication-
layer rather than the individual-belief layer; combining forgetting with a second lever (sparse
comms, provenance/APM per kickoff H3); non-monotone/inverted-U sweeps at finer resolution with
higher n. None of these are scheduled — see project memory for status.
