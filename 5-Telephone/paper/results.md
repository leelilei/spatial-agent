# Results Draft v0

> Figure-first draft. This is prose scaffolding for the paper, not final
> camera-ready text. Keep numbers synchronized with `../RESULTS.md` and
> `results_tables.md`.

## 1. Measuring Social Fidelity In An Agent Society

We study a controlled social transmission task in which a fact changes from a
stale value to a current value. A source agent receives the update, agents meet
over multiple rounds, and the society is later probed for the current answer.
The design separates three measurements: what agents hear, what agents say
during interaction, and what agents later hold when interviewed.

This distinction is essential. A social system can appear to transmit the
current fact in its conversation stream while failing to preserve that fact as a
later answer. We therefore evaluate social fidelity, not merely reach.

Figure 1 summarizes the instrument.

## 2. Current Truth Appears Transiently And Then Decays

In the baseline condition, the current update does not become a stable collective
belief. The long-horizon M5 run shows that held-current truth can rise early,
peaking near 28% around round 6, and then decay to roughly 6% by round 29. Thus,
the common r5 snapshot is close to an early transient peak rather than a stable
truth-preserving state.

A persistent authoritative source delays the decay but does not prevent it:
source runs peak near 36% and fall to about 4% by the end of the long horizon.
By contrast, direct broadcast to every agent keeps held-current belief near
ceiling, remaining around 92% at the final round. This establishes the core
phenomenon: ordinary social transmission can make truth visible without making
it durable.

Figure 2 shows this trajectory.

## 3. Intuitive Natural Levers Do Not Repair Held Truth

We next tested whether the failure is removed by obvious improvements to the
agent society.

Scaling model capability helps modestly but does not solve the problem. In the
powered capability rerun, held-current recall rises from 4.6/25 for the mini
model to 8.6/25 for gpt-5.4 and 7.6/25 for gpt-5.5. This is an improvement, but
most agents still do not hold the current truth.

Increasing connectivity also fails to repair the society. An early small run
suggested that higher connectivity might amplify corruption, but that result did
not replicate. The current claim is narrower and more defensible: connectivity
is roughly neutral and non-curative.

Changing memory architecture likewise fails as a robust repair. The smga3g
memory variant appeared promising in an underpowered run, but the rescue did not
replicate. Memory can affect what agents say, but in our tested setting it does
not reliably make the society hold the updated fact.

Figure 3 summarizes these failed natural levers.

## 4. Speech And Belief Dissociate

The central experiment compares three conditions: baseline, persistent source,
and broadcast. In baseline, agents receive the update through ordinary social
transmission. In source, the original source repeatedly re-announces the current
truth. In broadcast, every agent receives the current truth every round.

The source intervention is the crucial test. It makes the current truth much
more prominent in what agents say, but final held-current belief remains near
baseline: 3.0/25 in baseline and 3.8/25 under source, a non-significant
difference. Broadcast, by contrast, raises held-current belief to 24.8/25.

This demonstrates an operational speech-belief dissociation. The issue is not
that agents never encounter or utter the correction. They can say it. The
failure is that the uttered truth does not become the answer agents later give
when probed.

Figure 4 visualizes the SAY/HOLD gap.

## 5. The Mechanism Is Entrenchment, Not Recency

One natural explanation is recency: perhaps agents simply answer with the most
recent value they encountered. P1-rec rules this out. A late all-agent broadcast
immediately before probing should succeed under a recency account, but it does
not: held-current belief remains near baseline at 3.3/25. Conversely, a single
early all-agent broadcast succeeds at 24.8/25, matching continuous broadcast.

The mechanism is therefore path-dependent entrenchment. The value established
early and broadly becomes the one later conversation reinforces. Late or narrow
correction can enter speech without dislodging the incumbent held state.

Figure 5 shows the timing contrast.

## 6. Robustness And Measurement Checks

The dissociation is not limited to the original repair-drive scenario. G1
replicates the source-fails / broadcast-works pattern across book_club and
carpool. The absolute baseline difficulty varies by scenario, but the
intervention pattern remains: source does not approach broadcast.

The result is also not a thin-persona artifact. G2 repeats the core
baseline/source/broadcast comparison with richer personas. Baseline and source
remain near each other, while broadcast remains near ceiling.

Finally, the headline metric is not a keyword artifact. P2 rescored all M4
interview answers with a semantic judge. Keyword and judge scoring agree at
99-100%, and the headline current counts are unchanged: baseline 3.0, source
3.8, broadcast 24.8.

Together, these checks support the paper's main claim: social fidelity decay is
not merely a weak-model, single-scenario, thin-persona, or keyword-scoring
artifact.

## Result Summary

LLM-agent societies can transmit the current truth in speech while failing to
retain it as later held belief. Natural levers do not repair this failure.
Direct broadcast works only by bypassing the social channel. The governing
mechanism is not recency but early/broad entrenchment.
