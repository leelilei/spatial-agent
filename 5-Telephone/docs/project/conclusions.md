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

---

# CAPSTONE SYNTHESIS (2026-06-22) — full arc + honest verdict

**The complete experimental arc (all archived in RESULTS.md ledger; data in data_index.md):**

1. **Phenomenon (robust social fidelity decay).** A ground-truthed update does NOT survive
   propagation; the society holds the truth at a low, decaying level. Survives capability
   (M0/P3), connectivity (M1/P3b, neutral), memory swaps (M2/M3), thick personas (G2); decays
   over a long horizon (M5, GA peaks ~r6 then -> ~6% by r30). Metric judge-validated (P2).

2. **The DISSOCIATION (sharpest claim).** Speech != belief: interventions change what agents
   SAY (final-round utterances) without changing what the society HOLDS (private interview).
   M4: an authoritative source flips SAID to current but HELD stays at baseline; only brute
   broadcast (overwrite) moves both. SAY/HOLD elicited separately.

3. **Mechanism (entrenchment, not recency).** P1-rec: an early+broad correction succeeds,
   a late one fails -> path-dependent entrenchment; frequency-based integration lets the
   incumbent (stale) value win.

4. **The CURE = PROV (provenance-aware integration).** Integrate heard claims by provenance
   (latest authoritative version) not frequency. C1 de-risk, C2 validation, C3 fair (n=8:
   57% [49-65] vs GA 22% [13-30], CIs disjoint). C5 architecture table: PROV is the ONLY
   memory that lifts held truth; all recognized memories fail (Raw14/Mem0-18/A-MEM19/GA22/
   GA-curr25/MemBank25). Generalizes: C8 (#1 across 3 scenarios), C9 (numeric fact-type),
   C10 (#1 across topologies, margin GROWS on harder nets).

5. **The CURE's honest boundaries.** C5 horizon: PROV climbs to 100% at r20 -- flagged (by the
   human) as a DANGER SIGNAL. C5-stress: robust to provenance DROP, graceful under value
   GARBLE (beats GA until severe). C6: a "smarter" PROV-v2 (corroboration + Ebbinghaus decay)
   FAILED (negative result, recorded). C7: the 100% was a COMMS-MODEL artifact (every-utterance
   broadcast); under realistic SPARSE communication + forgetting, PROV settles to a dynamic
   equilibrium (~40% at mention 0.1, still ~2x GA, clean). The 100% on connected nets is a
   universal idealized ceiling (would recur for C9/C10 at r20), NOT the headline; the honest
   cure number is the sparse-comms equilibrium, above GA.

**VERDICT (honest).**
- *Diagnosis half:* FULLY achieved and strong (publishable on its own): phenomenon +
  dissociation + mechanism, robust and judge-validated.
- *Cure half:* achieved as an EXISTENCE PROOF that provenance integration is the right lever
  (beats every recognized memory, across scenarios/fact-types/topologies) -- NOT as a
  deployable robust architecture (PROV is naive/exploitable; PROV-v2 failed; realistic level is
  ~2x GA, not 100%). This is a real positive result (resolves the "finding without a result"
  worry), made more credible by honestly-mapped boundaries.
- *The original goal* ("characterize fidelity decay + whether better architecture acts as
  error-correction" / big Claim A with a real result): SUBSTANTIALLY MET.

**Remaining before "experiments closed":**
1. ~~CAPABILITY CHECK ON THE CURE (the one real gap)~~ **DONE (C14, 2026-06-23).** Verified on a
   different model FAMILY (DeepSeek-V4-Flash via yunwu.ai) rather than gpt-5.4/5.5: PROV 70.7%
   vs GA 17.3% held-current @ r5 (n=3, per-seed ranges disjoint). The cure survives capability,
   in fact with a WIDER margin than mini (mini PROV 57/GA 22). Symmetric with M0's
   phenomenon-survives-capability result. n=8 extension (seeds 44-48) in progress for matched CIs.
2. Minor: two topology GA-baseline cells at n=2-3 (firm to n=5).
3. Positioning vs Spark-to-Fire (arXiv:2603.04474): lead on dissociation + decentralized-memory
   comparison + correction-direction, NOT on inventing provenance.

**Future (not blocking):** PROV-v3 (trust/verification for the exploit/garble limit); n-extension
of headline rows (pool_runs.py ready); star broadcast-hub topology; sparse-comms cross-scenario.
