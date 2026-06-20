# Social Fidelity Probe - Figure Plan

> Working title: *Speech is not belief: Social fidelity decay in LLM agent societies*.
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
