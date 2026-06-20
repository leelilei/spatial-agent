# Telephone - Deep Conclusions

> Stable synthesis after the current M0-M5 / G1-G2 / P1-P3b result set.
> Numbers live in `../../RESULTS.md`; paper writing spine lives in
> `../../paper/narrative.md`.

## The Result In One Paragraph

In a simulated society of LLM agents, we inject a ground-truthed update and let
it propagate through agent-to-agent conversation. The society does not reliably
converge on the current truth. The current value can enter the conversation
stream, and under an authoritative source agents can increasingly *say* it, but
the society's later probed answer often remains stale or unknown. The failure is
not solved by model scaling, increased connectivity, tested memory swaps, richer
personas, or a persistent source. Only direct broadcast to every agent succeeds,
which is best interpreted as an overwrite-style positive control rather than a
realistic social cure. The mechanism is path-dependent entrenchment: the version
established early and broadly wins.

## Load-Bearing Findings

1. **Fidelity decay exists.** Agent societies can transmit a changing fact in
   conversation without preserving it as later held belief.
2. **Capability is not a cure.** Stronger models improve current recall
   modestly in powered reruns, but most agents still fail to hold the current
   truth.
3. **Connectivity is not a cure.** The earlier "connectivity amplifies
   corruption" claim was an underpowered outlier and is retracted. P3b supports
   the quieter claim: connectivity is roughly neutral and does not restore truth.
4. **Memory architecture is not a robust cure.** The M2 smga3g apparent rescue
   did not replicate in M3. Memory can change what agents say without reliably
   changing what they later hold.
5. **Authoritative source fails as a held-belief repair.** A persistent source
   can flip utterances toward the current truth while final held belief stays
   near baseline.
6. **Broadcast works as a positive control.** Injecting the current truth into
   every agent succeeds because it bypasses ordinary social transmission.
7. **The mechanism is entrenchment, not recency.** Early all-agent broadcast
   succeeds; late all-agent broadcast fails. Truth must win the early population
   competition, not merely appear later.

## Why It Matters

For multi-agent LLM systems, agent-to-agent communication is a reliability risk
for time-sensitive facts. A fact can be visible in logs while still failing as
state. Systems that rely on agents to relay updates need probes for what agents
later hold, not only what they utter during interaction.

For misinformation and collective epistemics, the contribution is a controlled
machine analogue of a familiar social problem: reach is not belief, correction
is not repair, and early entrenched versions can dominate later evidence.

For the model-collapse lineage, Telephone is an analogy rather than an identity.
Training-time collapse concerns recursive generated data degrading model
distributions. Telephone concerns communication-time recursive reuse degrading
social factual fidelity. The shared lesson is that fresh grounding matters; the
mechanism here is social entrenchment and speech-belief dissociation.

## Claim Boundaries

- Do not use the old wording that connectivity makes corruption worse as a
  stable conclusion. The current conclusion is neutral/non-curative.
- Do not describe broadcast as a practical social repair. It is the upper bound.
- Do not describe source failure as lack of exposure. Source failure is sharper:
  agents can hear/say the truth without later holding it.
- Do not claim literal access to internal belief. "Held belief" is the
  operational interview answer after social transmission.
- Do not present the work as a broad social simulation claim about humans. It is
  a controlled LLM-agent phenomenon paper with human communication analogues.

## Submission-Relevant Strengths

- Three-scenario generality check via G1.
- Persona-depth robustness via G2.
- Semantic judge validation via P2.
- Powered retractions of early overclaims via P3/P3b.
- Long-horizon decay trajectory via M5.

## Remaining Work

- Promote verified references into the paper draft and `.bib`.
- Write the Results section around Fig 1-5.
- Add the headline results table and HEARD -> SAID -> HELD mechanism table to
  the paper materials.
- Decide whether one additional scenario or broader judge validation is worth
  running for reviewer defense.
