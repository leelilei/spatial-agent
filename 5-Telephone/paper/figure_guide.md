# Figure Guide — main-text figures

> Walkthrough of the seven current main-text figures (rendered 2026-06-26 from the latest
> ledger by `scripts/render_latest_figs.py`). Each entry gives the figure's **purpose** (the
> question it answers in the narrative) and its **finding** (the claim it supports), with the
> backing experiment. Story arc: **diagnosis → cure → architecture**. Numbers live in
> `../RESULTS.md`.

---

## Part I — Diagnosis (the phenomenon and its mechanism)

### Fig 1 — Failed natural levers
![Failed natural levers](figures/fig_failed_levers.png)

- **Purpose.** Rule out every "obvious" fix before claiming the failure is deep: does any natural
  lever — model capability, memory architecture, persona richness, an authoritative source —
  restore the society's held truth?
- **Finding.** None do. Capability (21%), memory (18%), persona (14%) and source (15%) all sit at
  the baseline level (14%); only direct broadcast to every agent reaches 99% — and that is
  spoon-feeding, an overwrite-style upper bound, not a social repair. The failure is structural,
  not a missing knob.
- **Source.** M0–M4, G2 (mini, n=5–8), held-current %.

### Fig 2 — Speech is not belief (SAY/HOLD dissociation)
![Speech is not belief](figures/fig_say_vs_hold.png)

- **Purpose.** The sharpest claim of the paper: separately measure what agents *say* in
  conversation (SAID) and what they *hold* when later interviewed (HELD), to test whether
  utterance equals belief.
- **Finding.** An authoritative source moves SAID to 83% current while HELD stays at 15% (≈
  baseline) — a large gap. Only broadcast lifts both (99/99). Reach is not belief; a fact can be
  visible in the conversation log while failing as held state.
- **Source.** M4 (mini, n=5). Validated by an LLM judge (P2, 99–100% agreement with keywords).

### Fig 3 — Entrenchment, not recency
![Entrenchment, not recency](figures/fig_entrenchment.png)

- **Purpose.** Identify the mechanism: is the stale belief sticky because of *recency* (latest
  wins) or *entrenchment* (whatever was established early and broadly wins)?
- **Finding.** The same all-agent correction succeeds at round 1 (100%) but fails at round 5 (0%).
  Timing, not recency, decides — truth must be established before the incumbent stale belief
  entrenches. This is path-dependence.
- **Source.** P1-rec (repair_drive, mini).

---

## Part II — The cure (provenance-aware integration)

### Fig 4 — Architecture comparison
![Architecture comparison](figures/fig_architecture.png)

- **Purpose.** Locate *where* the fix lives by comparing PROV head-to-head against recognized
  memory architectures under one identical harness.
- **Finding.** Raw, Mem0, A-MEM, GA and MemBank all fail (14–25%); only PROV lifts held truth
  (57%). The decisive lever is the listener-side **integration rule** (integrate by provenance,
  not frequency), not a bigger or fancier memory.
- **Source.** C5 (repair_drive, mini, n=8), held-current %.

### Fig 5 — Capability check
![Capability check](figures/fig_capability_c14.png)

- **Purpose.** Test whether the cure is a small-model artifact by repeating it on a different
  model family (DeepSeek-V4-Flash) with full statistical weight.
- **Finding.** GA is statistically flat-and-failing across both models (mini 21.5%, DeepSeek
  15.5%), while PROV wins on both (57% / 64%) with disjoint CIs. The cure survives capability —
  in symmetry with M0's "the phenomenon survives capability."
- **Source.** C14 (25a, m2, r5, n=8). Error bars = 95% CI.

#### Generality table (cure is not a single-condition artifact)

| Axis | Condition | GA | PROV |
|---|---|---|---|
| Scenario (C8) | repair_drive | 22 | **57** |
| | book_club | 47 | **69** |
| | carpool | 18 | **59** |
| Fact type (C9) | dues $40→$60 | 28 | **59** |
| Topology (C10) | random | 22 | **93** |
| | ring | 6 | **68** |
| | smallworld | 10 | **83** |

PROV wins across scenarios, fact types and topologies; the margin grows on harder (structured,
slow) networks. held-current %, mini.

---

## Part III — The architecture (APM = Auditable Provenance Memory)

### Fig 6 — Adversarial robustness (APM's reason to exist)
![Adversarial robustness](figures/fig_apm_adversarial.png)

- **Purpose.** Without an adversary APM ≈ PROV, so APM needs a reason to exist. Introduce a liar
  that broadcasts a forged high-version stale claim (`auth=false`) and ask which architecture
  survives.
- **Finding.** The liar collapses PROV from 57% to 33% and hijacks 43/75 agents to the forgery
  (stale 57%). APM is unmoved (64%) with **zero hijack (stale 0)** — its origin-anchoring rejects
  the unauthenticated claim. Without an adversary the two are equivalent; with one, only APM
  stands. This is the deployable-architecture answer to "naive provenance is exploitable."
- **Source.** C16 (mini, r5, adversary from r2, n=3). Mechanism also unit-tested.

### Fig 7 — Communication-sufficiency curve
![Communication-sufficiency curve](figures/fig_apm_comms_curve.png)

- **Purpose.** Answer the recurring worry "does APM also flood to 100% like idealized PROV did?"
  by sweeping communication density (how often agents actually mention the fact) under realistic
  sparse comms.
- **Finding.** A smooth, fully monotonic S-curve: held-current rises from 11% (mention 0, only the
  source knows) to 87% (0.25–0.3) and saturates at 100% only at the unrealistic dense limit
  (0.5+). The 40% sparse-end value is the honest floor, not a ceiling. Crucially **stale stays 0
  at every density** — APM's safety is independent of how well truth spreads.
- **Source.** C17b (mini, r10, n=5; mention 0.1 is n=8). Shaded band = 95% CI.

---

## How the figures map to the argument

```
Diagnosis : Fig 1 (no natural fix) -> Fig 2 (say != hold) -> Fig 3 (entrenchment)
Cure      : Fig 4 (only provenance) -> Fig 5 + table (survives capability/scenario/topology)
Architecture: Fig 6 (only APM under attack) -> Fig 7 (non-saturating, stale=0)
```

One-line takeaway per part: **(I)** a ground-truthed update decays through conversation and no
natural lever fixes it because speech ≠ belief and early versions entrench; **(II)** integrating
by provenance — not frequency — is the lever that works, across models, scenarios, fact types and
topologies; **(III)** hardened as APM it stays interpretable, is the only architecture that
survives a forgery attack, and gives a realistic non-saturating equilibrium with zero confident
errors.

## Still to add
- Table 2 (architecture + APM row) and Table 3 (generality + C14 column) as formal tables in
  `results_tables.md`.
- Supplement figures: PROV horizon r5→r20 (C5), lossy/garble stress (C5-stress), judge validation
  (P2) — render via the same script when needed.
