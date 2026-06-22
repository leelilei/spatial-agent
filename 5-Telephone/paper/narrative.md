# When Truth Loses Its Source - Paper Narrative

> Working title: *When Truth Loses Its Source: Provenance-Aware Memory for Socially Distributed Agents*.
> This is the current writing spine. Numbers live in `../RESULTS.md`; the
> figure plan lives in `figures.md`; citation triage lives in `references.md`.
> Intro-specific framing notes live in `introduction.md`.
> Section-first writing plan lives in `sections/README.md`; stabilize each major
> Markdown block before migrating prose into LaTeX.

## One-Sentence Thesis

When LLM agents pass a ground-truthed update through conversation, the society
can learn to *say* the truth without coming to *hold* the truth. This
speech-belief dissociation is driven by path-dependent entrenchment: once a
current fact loses its source/version, the version established early and broadly
wins.

## What Changed From The Original Plan

The project started as a search for a clean phase boundary and a minimal repair
mechanism. The current evidence changes that framing.

- We no longer claim a connectivity/capability phase boundary. Capability helps
  modestly but does not solve the failure; connectivity is roughly neutral.
- We no longer claim connectivity amplifies corruption. The dramatic early cell
  was an underpowered outlier and did not replicate in P3b.
- We no longer claim memory is a cure. The M2 smga3g rescue did not replicate.
- We no longer claim an authoritative source repairs the society. M4 shows that
  a persistent source changes speech but not held belief.
- We now center the paper on a sharper result: speech and belief dissociate in
  LLM-agent societies, and the mechanism is early/broad entrenchment.

## Why This Is Worth Doing

Generative-agent work shows that information can spread through an agent
society. That is not the same as showing that the spread is faithful. A rumor,
correction, schedule change, policy update, or evidence item can reach the
conversation stream while failing to become the society's later answer.

The social fidelity probe therefore moves the unit of evaluation from an
individual model's answer to a social process: what happens when agents
repeatedly hear, relay, compress, and retrieve a changing fact?

## Core Contributions

1. **Measurement shift:** a social fidelity probe separates what agents hear,
   what they say, and what they later hold.
2. **Main phenomenon:** authority can move speech without repairing held belief;
   the society can say the truth without holding it.
3. **Mechanism and boundaries:** natural levers fail to repair held truth, while
   early and broad entrenchment explains when truth persists.

## Result Spine

### R1. Speech and belief dissociate

M4 is the centerpiece. Under a persistent authoritative source, agents
increasingly utter the current value, but final interviews remain near baseline.
Broadcast to every agent every round makes both speech and held belief current.

This creates the paper's clean contrast:

| Condition | What agents hear / say | What agents hold | Interpretation |
|---|---|---|---|
| Baseline | Current update appears but competes with stale history | Low current belief | Ordinary social transmission loses fidelity |
| Source | Current truth is repeatedly uttered by authority | Still low current belief | Speech moves without belief repair |
| Broadcast | Every agent receives the current truth directly | High current belief | Overwrite-style positive control |

The result should be described operationally. We do not claim access to literal
mental states. "Held belief" means the answer an agent gives when later probed
about the current fact.

### R2. Social fidelity decays over time

In the core task, an event changes from a stale value to a current value. Agents
then meet over several rounds and are interviewed at the end. The basic failure
is that the current value reaches the conversation stream but does not reliably
become the society's held answer.

M5 sharpens this into a long-horizon story. In baseline runs, current truth can
rise early, peaking near round 6, then decays toward a low steady state by round
30. The r5 snapshot therefore slightly overstates long-run truth retention. The
important object is not just end-state corruption but the trajectory: truth can
appear transiently and still lose.

### R3. Natural levers do not solve the failure

The negative result is now more precise than the original plan:

| Lever | Current conclusion | Paper wording |
|---|---|---|
| Capability | Helps modestly but leaves most agents off the current truth | Scaling is not a cure |
| Connectivity | Roughly neutral after P3b; does not restore truth | More communication is not repair |
| Memory | smga3g rescue did not replicate | Memory architecture is not a robust cure |
| Authoritative source | Changes speech but not held belief | Authority can make agents say truth without making them hold it |
| Broadcast to all | Works | Positive control / overwrite, not a social cure |

This matters because each lever is an intuitive repair story. The paper's claim
is not that agents are incapable of outputting the truth. They can. The problem
is that normal social communication does not reliably install the truth as later
held belief.

### R4. The mechanism is entrenchment, not recency

P1-rec distinguishes two stories:

- If recency drove belief, a late all-agent broadcast immediately before the
  probe should work.
- If repetition drove belief, a single early all-agent broadcast should fail.

The opposite happens. A single early broadcast succeeds; a late broadcast fails.
So the governing factor is whether the truth becomes the early, broad version
that later conversation reinforces. The stale value begins with incumbent
advantage; narrow or late correction can be uttered without taking over the
society's held state.

### R5. Generality and measurement checks are in place

G1 replicates the baseline/source/broadcast pattern across repair_drive,
book_club, and carpool. G2 shows that thicker personas do not remove the
dissociation. P2 shows that the headline current/stale verdict is not a keyword
artifact: semantic judge and keyword scoring agree on the M4 headline.

## Related Work Spine

The related work should not become a broad survey. It should serve four
paragraphs.

1. **Agent societies and communicative agents.** Generative Agents, CAMEL,
   AutoGen, SOTOPIA, and related systems establish the setting: agents talk,
   remember, coordinate, and simulate social environments. This work asks a
   missing reliability question inside that setting.
2. **Misinformation, rumor, and reach vs fidelity.** Rumor and fake-news work
   distinguishes spread from truth. LLM-agent rumor simulations are close
   neighbors, but they typically measure propagation or vulnerability; this work
   measures held-fact fidelity after a truth change.
3. **Factuality, hallucination, and measurement.** TruthfulQA, SelfCheckGPT,
   semantic entropy, RAGTruth, calibration, and internal-state work justify
   treating truthfulness as a semantic behavioral target rather than surface
   fluency.
4. **Memory, correction, and recursive degradation.** Memory systems explain why
   exposure is not retention; correction and belief-echo work explain why stale
   information can persist; model-collapse work provides an analogy for
   recursive degradation, but we must state that this is communication-time
   degradation, not training-time collapse.

## Claim Boundaries

- Do not say "more connectivity worsens corruption" as a stable result. Say it
  does not repair truth and appears roughly neutral in the powered rerun.
- Do not say "source correction fails because agents never hear it." M4 shows
  the opposite: source changes what agents say.
- Do not say "memory never matters." Say the tested memory swap does not
  robustly restore held truth; memory can affect speech and remains a possible
  mitigation direction.
- Do not say "broadcast is a practical cure." It is an upper bound and positive
  control because it bypasses the social channel.
- Do not treat the model-collapse analogy as identity. The shared structure is
  recursive reuse degrading fidelity; the mechanism is different.

## Draft Order

1. Abstract from the one-sentence thesis.
2. Introduction around the missing axis: spread is not fidelity.
3. Methods around Inject -> Propagate -> Measure; HEARD/SAY/HOLD.
4. Main result: speech-belief dissociation.
5. Long-horizon social fidelity decay.
6. Failed natural levers.
7. Mechanism: early and broad entrenchment.
8. Robustness and measurement validation.
9. Related work using `references.md`.
10. Discussion around engineering implications, memory/correction limits, and
   communication-time collapse as analogy.
