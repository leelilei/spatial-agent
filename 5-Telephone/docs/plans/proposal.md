# Telephone — Research Proposal v2

> Supersedes `proposal_v1.md` as the current result-aware proposal. v1 was a pre-result
> framing document centered on phase boundaries and minimal correction. v2 folds in the
> M0-M4, G1, P1-rec, P2, P3, and P3b results. Numbers live in `../../RESULTS.md`;
> the stable synthesis lives in `../project/conclusions.md`.

## Speech is not belief: Fidelity decay in LLM agent societies

Current working title.

## One-Line Claim

When LLM agents pass a ground-truthed update through conversation, the society can learn
to *say* the truth without coming to *hold* the truth. This speech-belief dissociation is
driven by path-dependent entrenchment: the version established early and broadly wins.

## Abstract Sketch

LLM agent systems are increasingly built as societies: agents talk, share state, and rely
on one another's memories. Prior work celebrates that information spreads through such
societies, but rarely asks whether what spreads remains true. We study this missing axis:
the fidelity of socially transmitted information.

Using a controlled 25-agent society, we inject a known update to an event's time/place and
measure what agents hear, say, and finally hold. Across three scenarios, agent societies
exhibit a telephone effect: the current truth reaches the conversation stream but fails to
become the collective belief. Scaling model capability helps modestly but does not solve
the failure; increasing connectivity does not solve it; memory architecture swaps do not
robustly solve it; and a persistent authoritative source changes what agents say without
significantly changing what they believe. Only direct broadcast to every agent succeeds,
which functions as an overwrite-style positive control rather than a realistic social
cure.

The mechanism is not recency. A late broadcast to every agent immediately before probing
fails, while a single early broadcast to every agent succeeds as well as continuous
broadcast. The society's belief is therefore path-dependent: truth must be established
early and broadly before the incumbent stale version entrenches. We call this phenomenon
speech-belief dissociation in LLM agent societies and position it as the communication-time
social analog of model collapse.

## What We Have Found

### F1. Agent societies exhibit fidelity decay, not just information spread

The core empirical object is a ground-truthed update: an event changes from an old
time/place to a new one. The question is not whether agents mention the update, but whether
the society ultimately holds the current truth. In the original repair-drive scenario,
baseline truth recall is low: roughly 3/25 agents hold the current truth under the standard
GA-memory, mini-model, meetings=2, rounds=5 setting.

The parent 3-SMGA results first revealed the failure mode: agents who "received" the update
often heard a stale-dominant stream, detail drift, or version splitting. Telephone turns
that observation into the paper's object of study.

### F2. Scaling helps modestly but does not solve social truth-decay

Early M0 suggested truth preservation was almost flat across model capability. The powered
P3 rerun refines this:

```text
model       current/25 [95% CI]   n
mini        4.6  [3.0,  6.2]      8
gpt-5.4     8.6  [6.2, 11.0]      5
gpt-5.5     7.6  [5.2, 10.0]      5
```

So the honest claim is not "capability does nothing." Capability gives a modest bump. But
even strong models leave most of the society off the current truth. Scaling is therefore
not a cure for social truth-decay.

### F3. Connectivity does not solve the failure

M1 initially suggested that higher connectivity amplified corruption, driven by one
dramatic gpt-5.4 cell. P3 and P3b retract that stronger claim. On mini, meetings=1/2/3 are
roughly flat. On gpt-5.4, the connectivity-amplification result does not replicate:
Sat:Sun dominance stays around 1.0 rather than exploding.

The current claim is therefore:

**Connectivity is roughly neutral. More communication does not restore truth, but we no
longer claim it reliably amplifies corruption.**

### F4. Memory changes speech more reliably than belief

Memory architecture was tested as a possible repair. A currency-resolving memory looked
promising in a small M2 run, but the apparent rescue did not replicate in M3. The durable
signal was subtler and more interesting: memory can shift conversation streams toward the
current value without significantly lifting final truth recall.

This becomes part of the main mechanism: changes to what agents retrieve or utter need not
become changes to collective held belief.

### F5. Authoritative re-broadcast fails, while brute broadcast succeeds

M4 tested three conditions on repair_drive:

```text
condition   current/25 [95% CI]
baseline     3.0 [0.7, 5.3]
source       3.8 [2.4, 5.2]   ns vs baseline
broadcast   24.8 [24.2, 25.4] significant
```

The source condition is the realistic intervention: one authoritative source repeatedly
announces the truth. It visibly flips what agents say, but it does not significantly move
what they hold. Broadcast works only by injecting the update into every agent, bypassing
the society's ordinary communication dynamics.

This is the paper's central empirical contrast.

### F6. Speech-belief dissociation generalizes across scenarios

G1 replicated the M4 pattern on two additional scenarios: book club and carpool.

```text
scenario       baseline   source       broadcast
repair_drive    3.0        3.8 ns       24.8 sig
book_club       9.6       12.8 ns       24.8 sig
carpool         3.2        4.0 ns       25.0 sig
```

In all three scenarios, a persistent source fails to restore held belief despite changing
what agents say, while broadcast succeeds. This clears the first generality attack against
the dissociation spine: it is not a single-prompt artifact.

### F7. The mechanism is entrenchment, not recency

P1-rec distinguishes recency from path-dependence:

```text
condition                         current/25
baseline                           3.0
r1_broadcast, all agents once      24.8
r5_broadcast, all agents once       3.3
every-round broadcast              24.8
```

If recency governed belief, the round-5 broadcast should work. It does not. If continuous
repetition were required, round-1 broadcast should fail. It does not. The clean conclusion:
the decisive factor is whether the truth is established early and broadly enough to become
the version reinforced by later conversation.

The stale value is the incumbent belief from round 0. A late or narrow correction can be
uttered without becoming the collective belief.

### F8. The headline metric is not a keyword artifact

P2 re-scored 375 M4 interview answers with an LLM judge. Keyword and judge agreement was
99-100%, and the judge reproduced the headline current counts exactly:

```text
condition   keyword current/run   judge current/run
baseline    3.0                   3.0
source      3.8                   3.8
broadcast   24.8                  24.8
```

The current/stale verdict is therefore not merely a surface keyword artifact. A fuller
provenance-based fidelity rubric remains useful, but the headline dissociation survives
semantic judging.

## Revised Central Claims

### C1. Fidelity is distinct from reach

An update can enter the society's conversation stream without becoming the society's held
truth. Measuring spread alone misses the failure.

### C2. Natural levers do not solve the failure

Model scaling helps modestly but leaves truth recall low. Connectivity does not restore
truth. Memory architecture changes do not robustly rescue belief. A persistent authority
changes speech but not held belief.

### C3. Speech and belief dissociate in LLM agent societies

The strongest result is not merely that agents forget. It is that interventions can make
the society say the truth while the final held belief remains unchanged.

### C4. The mechanism is path-dependent entrenchment

The version established early and broadly wins. A late correction, even broadcast to all
agents immediately before the probe, is no better than baseline. Truth must win the early
population-level competition, not merely be uttered later.

## What We Retract or Downgrade From v1

- **Phase-boundary as the center:** downgraded. We have a robust failure phenomenon and
  governing evidence, but current connectivity results do not support a clean
  connectivity-capability phase boundary.
- **Connectivity amplifies corruption:** retracted. P3b did not replicate it. Connectivity
  is currently best described as roughly neutral and not curative.
- **Minimal correction flips the society:** retracted. Realistic source re-broadcast fails.
  Broadcast succeeds only as an overwrite-style positive control.
- **Memory as cure:** retracted. The M2 apparent cure did not replicate.

## Contribution Framing

1. **A measurement shift:** from information reach to information fidelity in LLM-agent
   societies.
2. **A phenomenon:** social fidelity decay, or a telephone effect, in agent-to-agent
   transmission.
3. **A mechanism:** speech-belief dissociation caused by path-dependent entrenchment.
4. **A negative intervention result:** natural fixes fail; brute overwrite works.
5. **A rigor story:** three scenarios, semantic judge validation, powered reruns, and
   explicit retractions of non-replicated early claims.

## Related Work Positioning

### Agent societies

Generative Agents and related society simulators show that information can spread. Our
contribution is to ask whether the spread preserves the original truth. This makes the
work a fidelity study, not another emergence demo.

### Transmission chains and rumor dynamics

Human serial reproduction and iterated learning show that repeated transmission contracts
information toward attractors. Telephone imports that lens into LLM-agent societies, with
trace-level measurement of heard, said, and held versions.

### Model collapse

Model collapse studies degradation through recursive training or self-consumption.
Telephone studies the communication-time analog: degradation through inference-time social
exchange. The novel twist is speech-belief dissociation: the surface signal can be fixed
while held belief remains collapsed.

### Misinformation and collective belief

Misinformation work often focuses on reach, cascades, or final task accuracy. Our result
focuses on the gap between utterance and held belief, and on the timing/breadth conditions
under which correction fails.

### Memory and correction

Memory systems can alter retrieval and utterance, but our results show that better
retrieval is not automatically better collective belief. This is the bridge from memory
systems to social epistemics.

See `../../paper/references.md` for the working reference library.

## Method Summary

- 25-agent society simulation.
- Pluggable memory conditions.
- Controlled event-update scenarios.
- Three surface-different scenarios: repair_drive, book_club, carpool.
- Conditions: baseline, persistent source re-broadcast, broadcast-to-all, timing-specific
  broadcast, model-capability sweeps, connectivity sweeps, memory variants.
- Metrics: final held answer, conversation utterance ratios, event-stream evidence ratios,
  keyword and semantic-judge verdicts, confidence intervals over seeds.

## Paper Skeleton

1. **Introduction:** LLM agents increasingly share state socially; spread is not fidelity.
2. **Setup:** controlled update propagation in a simulated agent society.
3. **Existence:** baseline fidelity decay and stale/unknown convergence.
4. **Failed levers:** capability, connectivity, memory, authority.
5. **Speech-belief dissociation:** source changes speech but not belief; broadcast positive
   control.
6. **Mechanism:** early/broad entrenchment, not recency.
7. **Generality and validation:** three scenarios, semantic judge, powered reruns.
8. **Discussion:** implications for multi-agent systems, collective epistemics, and social
   model collapse.

## Remaining Work Before Submission

- Update `paper/narrative.md` so it no longer carries old connectivity-amplification and
  minimal-cure framing.
- Produce a mechanism figure: `HEARD -> SAID -> HELD` over rounds/conditions.
- Add a compact table of all headline conditions and confidence intervals.
- Extend judge/provenance scoring beyond M4 if needed for the final paper.
- Decide whether to add one more scenario or reserve it for revision.

## Current Bottom Line

The paper is no longer about discovering a clean phase boundary or a minimal cure. It is
about a sharper phenomenon:

**LLM-agent societies can be made to say the truth without coming to believe it, because
collective belief is path-dependent and entrenched by early, broad social evidence.**
