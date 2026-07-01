# Thaw — Results

## Experiment ledger

| date | id | question | configuration | result | status |
|---|---|---|---|---|---|
| 2026-06-30 | A0 | Does Telephone's old late-broadcast failure reproduce? | 25a, m2, r5, t3, seed41, last round index=4, all-agent broadcast, forget=0 | **No. 25/25 current.** Audit found old `r5_broadcast` logs had zero injections. Telephone P1-rec retracted. | closed; premise invalid |
| 2026-06-30 | H1a | Does a narrow persistent source create a useful frozen baseline without explicit old-fact initialization? | 10a, m2, r5, t2, seed41, source inject r1-r4, forget=0 | 4 current / 0 stale / 6 unknown; only 1 stale utterance. This is propagation shortage, not a frozen wrong attractor. | rejected as H1 baseline |
| 2026-06-30 | H1b | Can explicit stale initialization create a real frozen incumbent? | 8a, m2, r6, t2, seed41; old fact initially observed by all; source correction r3-r5; forget=0 | **2 current / 6 stale.** Social rehearsal: 4 current vs 65 stale utterances. Valid frozen pilot regime. | gate passed |
| 2026-06-30 | H1c | Does memory decay thaw H1b? | same as H1b; forget={0.5,0.8} | Both give 3 current / 5 stale vs 2/6 control. Stale rehearsal falls 65→61→55; at r5, 11→11→4. **Weak candidate signal, n=1.** | de-risk only; needs seeds |

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
