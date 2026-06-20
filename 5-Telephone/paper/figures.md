# Telephone — Figure plan (figure-first Results)

> Working title: *Speech is not belief: Fidelity decay in LLM agent societies*.
> Lock this list BEFORE drafting Results prose; each Results paragraph = caption for one figure.
> Status legend: ✅ data in hand · 🟡 needs a small re-extraction from existing run logs ·
> 🔴 needs a (small) new run. Numbers live in `../RESULTS.md`.

---

## Main figures (target: 4 main + 1–2 supp)

### Fig 1 — Setup / method schematic  ✅ [rendered: figures/fig1_setup.png]
- **Message:** how the instrument works, in one picture.
- **Content:** N=25 agents on a contact graph → a ground-truthed update is injected at one
  source ("repair drive moved Saturday→Sunday") → K rounds of pairwise meetings (each agent
  reads/relays via GA-reflection memory) → at the end we *interview* every agent ("when/where
  is it now?") and score held belief = current / stale / unknown.
- **Why:** establishes the two distinct measurements the whole paper hinges on — what agents
  SAY in meetings vs what the society HOLDS at interview.

### Fig 2 — The phenomenon: fidelity decay over a long horizon (DECAY CURVE)  ✅  [rendered: figures/fig2_decay.png]
- **Message:** a true update does NOT survive propagation; the stale version wins.
- **Encoding:** stacked bar (or area) of held-belief composition {current, stale, unknown}
  for the baseline condition; truth (current) is a thin sliver (~12–14%), stale/unknown
  dominate. Optionally overlay the receiver Sat:Sun provenance split as a second bar.
- **Data:** baseline interviews (M4 thin + G2 thick agree). ✅ for final-state.
- **NOTE / honesty:** we interview only at the END (r5), so this is a *final-state* bar, not a
  decay-vs-round *trajectory*. A trajectory (current-rate vs round) would be more striking →
  see "Gap" below (Fig 2-alt, 🔴 small re-run with per-round interviews).

### Fig 3 — Failed levers  ✅ [rendered: figures/fig3_failed_levers.png]
- **DATA NOTE:** capability gives a MODEST bump (mini 19% → gpt-5.4 35% → gpt-5.5 30%, error bars separated) but stays ≤35% ≪ broadcast cure 99%; connectivity flat/n.s. (20/19/14); memory n.s. (ga 17% vs smga3g 24%, smga3g std huge — the M2 56% outlier). Dashed line = broadcast cure (99%).
- **Message:** capability, connectivity, and memory all FAIL to restore truth.
- **Encoding:** 3 small panels (or one grouped bar), y = held current-rate with 95% CI,
  baseline reference line:
  - (a) **Capability** (M0/P3): mini → gpt-5.4 → gpt-5.5, flat ~16→20→21%.
  - (b) **Connectivity** (M1/P3b): meetings 1/2/3, flat (~neutral; the retracted 10× is gone).
  - (c) **Memory** (M2/M3): ga vs smga3g, Δ ns.
- **Data:** M0/P3, P3b, M3 aggregates. ✅ (CIs from per-run rates).

### Fig 4 — ★ The dissociation: speech ≠ belief (money figure)  ✅ [rendered: figures/fig4_dissociation.png]
- **DATA NOTE:** SAID = FINAL-round current-utterance % (not cumulative). source SAY 54→75% but HELD 12→15% (the gap); broadcast 99/99 (no gap).
- **Message:** interventions change what agents SAY, not what the society HOLDS.
- **Encoding:** for each condition {baseline, authoritative source, broadcast}, two paired
  bars: (i) SAID-current ratio (from meeting event streams) vs (ii) HELD-current rate (from
  interview). Source: SAID jumps (Sun:Sat ~25:5) while HELD stays flat ≈ baseline. Broadcast:
  both high. Baseline: both low.
- **Data:** M4 + G1 (3 scenarios) + G2 (thick). ✅ This is the paper's centerpiece.

### Fig 5 — The mechanism: entrenchment / timing  ✅ [rendered: figures/fig5_mechanism.png]
- **DATA NOTE:** baseline 12% / source 15% / broadcast-LATE(r5) 9% / broadcast-EARLY(r1) 100%. Late or narrow fails; only early+broad wins (recency refuted).
- **Message:** WHEN+HOW BROAD the truth lands decides everything; recency does NOT.
- **Encoding:** held current-rate vs injection timing — r1-broadcast (early, all) = 25/25 vs
  r5-broadcast (late, all) = 0/25; contrast with source (every round, narrow) ≈ baseline. A
  small "phase" cartoon: early+broad → truth attractor; late or narrow → corruption attractor.
- **Data:** P1-rec + M4. ✅

## Supplementary / robustness

### Fig S1 — Generality across scenarios + persona depth  ✅ [rendered: figures/figS1_generality.png]
- **DATA NOTE:** broadcast ~99% everywhere; source never approaches the cure. (book_club baseline/source are higher — 38/51% — but still ≪ broadcast; pattern qualitatively holds.)
- **Message:** the dissociation is not a single-scenario or thin-persona artifact.
- **Encoding:** small-multiples of Fig 4's source-vs-baseline contrast across
  {repair_drive, book_club, carpool} (G1) and {thin, thick} persona (G2): source ≈ baseline,
  broadcast ≫, everywhere.
- **Data:** G1 + G2. ✅

### Fig/Table S2 — Metric validation  ✅
- **Message:** the current/stale verdict is not a keyword artifact.
- **Content:** keyword vs LLM-judge agreement (99–100%); judge current-rate = keyword exactly.
- **Data:** P2. ✅ (likely a TABLE, not a figure.)

### Tables (appendix)
- **T1:** full lever sweep numbers (M0/M1 grid) with n and CIs.
- **T2:** per-condition/per-scenario current/stale/unknown counts (M4/G1/G2).

---

## The one gap worth a decision
**Decay trajectory (Fig 2-alt):** we currently interview only at r5, so we can show the
end-state corruption attractor but not a *current-rate-vs-round* decay curve. A decay curve
would be a stronger Fig 2 / possible hero. Cost: one small re-run (baseline, n=5) that
interviews after every round. **Decision: add per-round interview + run Fig-2 trajectory, or
ship final-state bars?** (Recommend: yes, cheap and it's the most intuitive "telephone" image.)

## Draft order for Results prose (around these figures)
1. Setup (Fig 1) → 2. Phenomenon/decay (Fig 2) → 3. Failed levers (Fig 3) →
4. ★ Dissociation (Fig 4) → 5. Mechanism/entrenchment (Fig 5) → 6. Robustness (S1) +
metric validation (S2).
