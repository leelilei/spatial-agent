# When Truth Loses Its Source - Figure Plan

> Working title: *When Truth Loses Its Source: Provenance-Aware Memory for Socially Distributed Agents*.
> Figure-first Results plan. Each Results subsection should map to one figure or
> one table. Numbers live in `../RESULTS.md`.

## Main Figures

### Fig 1 - Setup / Method Schematic

Rendered: `figures/fig1_setup.png`

**Message:** The social fidelity probe separates three objects that are usually conflated:
what agents hear, what agents say, and what agents later hold.

**Content:** 25 agents on a contact graph; one ground-truthed update is injected
at a source; agents meet over rounds; logs measure SAY; final or per-round
interviews measure HOLD as current / stale / unknown.

**Caption direction:** The method instruments a social transmission channel
rather than a single-agent QA task.

### Fig 2 - Speech Is Not Belief

Rendered: `figures/fig2_speech_belief.png`.

**Message:** Source intervention changes SAY without repairing HOLD.

**Encoding:** paired bars for baseline, source, broadcast:

- SAY-current ratio from meeting streams.
- HOLD-current rate from interviews.

Source should show the gap: utterances move toward current truth while held
belief stays near baseline. Broadcast should show both SAY and HOLD high.

**Caption direction:** This is the centerpiece. It establishes the operational
speech-belief dissociation before the paper turns to decay, failed levers, and
mechanism.

### Fig 3 - Long-Horizon Fidelity Decay

Rendered: `figures/fig3_decay.png` and data in `figures/fig2_trajectory.csv`.

**Message:** Truth can appear transiently and still lose. In baseline, held
current truth rises early, peaks around round 6, and then decays toward a low
steady state by round 30. A persistent source also decays/converges toward
baseline; only broadcast sustains current belief.

**Encoding:** trajectory line plot over rounds for baseline, source, and
broadcast. Y axis = held-current percentage. Use this as the phenomenon figure,
not the older final-state-only bar.

**Caption direction:** The r5 result is not the whole story; it is near an early
transient peak. Long-run social transmission continues to erode held truth.

### Fig 4 - Failed Natural Levers

Rendered: `figures/fig4_failed_levers.png`.

**Message:** Capability, connectivity, and memory architecture do not restore
held truth.

**Encoding:** small multiples or grouped bars with 95% CIs:

- Capability: mini -> gpt-5.4 -> gpt-5.5. Claim: modest improvement, not cure.
- Connectivity: meetings 1/2/3. Claim: roughly neutral, not repair.
- Memory: GA vs smga3g. Claim: no robust rescue; M2 was an outlier.

**Caption direction:** The figure should avoid the old "connectivity amplifies"
language. The result is negative but sober: intuitive levers fail to make held
truth dominate.

### Fig 5 - Entrenchment, Not Recency

Rendered: `figures/fig5_mechanism.png`.

**Message:** Timing and breadth decide whether truth becomes entrenched.

**Encoding:** held-current rate for baseline, source, late all-agent broadcast,
early all-agent broadcast, and every-round broadcast.

**Caption direction:** A late all-agent broadcast fails, while a single early
all-agent broadcast succeeds. This refutes a simple recency account and supports
path-dependent entrenchment.

## Additional Main-Text Figures And Tables

### Fig 6 - Robustness And Measurement Validation

Rendered: `figures/fig6_robustness.png`.

**Message:** The dissociation is not a single-scenario or thin-persona artifact.

**Encoding:** replicate the baseline/source/broadcast contrast across
repair_drive, book_club, carpool, and thick-persona variants.

### Table 1 - Evidence Ledger

**Message:** One compact table should carry the full evidence chain:
M4/G1/P1-rec/P2/P3/P3b/M5.

**Content:** question, contrast, result, and claim for the core evidence blocks.

### Table S2 - Metric Validation

**Message:** The current/stale verdict is not a keyword artifact.

**Content:** keyword vs semantic judge agreement on M4. Highlight that the
headline current counts are reproduced under semantic judging.

### Table S4 - HEARD -> SAID -> HELD Mechanism

Drafted in `results_tables.md`.

**Message:** The mechanism is not that agents never hear the correction. The
important gap is between social utterance and later held answer.

## Results Draft Order

1. Fig 1: instrument and measurements.
2. Fig 2: speech-belief dissociation.
3. Fig 3: long-horizon decay.
4. Fig 4: failed levers.
5. Fig 5: entrenchment mechanism.
6. Fig 6 / Table 1: robustness, measurement validation, and evidence ledger.

## Cure & Architecture Figures/Tables (provenance + APM; C1-C17b)

Extends the diagnosis figures with the cure and the APM architecture. Most cure
figures are already rendered (`figures/fig_cure_*`); the APM block (C14-C17b) is new.

### Table 2 - Architecture Comparison (headline cure table)
Partially rendered: `figures/fig_cure_table_horizon.png`.
**Message:** only provenance integration lifts HELD truth.
**Content:** HELD-current for Raw / GA / GA-curr / Mem0 / A-MEM / MemBank / PROV / **APM**.
**Data:** C5 + **C15 (add APM row + auditability %)**. STATUS: needs APM row.

### Table 3 - Generality + Capability
**Message:** the cure is not a single-scenario / fact-type / topology / model artifact.
**Content:** PROV vs GA across 3 scenarios (C8), numeric fact (C9), topologies (C10),
and **mini + DeepSeek n=8 (C14)**. STATUS: data complete; assemble (add C14 column).

### Fig 7 - Cure: PROV vs GA
Rendered: `figures/fig_cure_prov.png`, `fig_cure_fair_prov.png`. Held-current lift +
closes the dissociation (source GA dead vs PROV alive). STATUS: ok.

### Fig 8 - APM Adversarial Robustness (APM's reason to exist) [NEW]
**Message:** under a forged-claim liar, PROV is hijacked (stale 43/75) while APM holds
(stale 0/75). Without an adversary APM ≈ PROV; with one, only APM stands.
**Data:** C16. STATUS: data complete; **render new**.

### Fig 9 - APM Communication-Sufficiency Curve [NEW]
**Message:** the 100% ceiling is a comms-model artifact; under realistic sparse comms
APM settles to a sub-100% equilibrium, and stale stays ≡ 0 at every sparsity.
**Encoding:** x = mention prob {0.1,0.15,0.2,0.25,0.3,0.5,(0.8)}; y = held-current
(rising) + stale (flat 0); reference idealized mention→1 ≈ 100% (C5/C7).
**Data:** C17 (n=8 @0.1) + C17b sweep (11 pts, mention 0->0.8). STATUS: **data COMPLETE; render png** (curve drafted as widget).

### Supplement (cure/APM)
PROV horizon r5/r10/r20 (C5) + sparse equilibrium (C7: `fig_sparse_comms_equilibrium`);
lossy-channel stress (C5-stress: `fig_prov_lossy_stress`); APM auditability + K=2
deadlock (C15); n / CI / seed reproducibility tables.

## Render queue (what is actually missing)
1. **Fig 8 — APM adversarial (C16): READY to render.**
2. **Fig 9 — APM comms curve (C17b): data COMPLETE (11 pts); render png.**
3. Table 2 — add APM row (C15). 4. Table 3 — add C14 cross-model column.
(Diagnosis Figs 1-6 + PROV cure figs already rendered.)
