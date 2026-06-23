# Architecture: APM vs GA-reflection

> Section-first draft. Argues the memory-architecture contribution as a peer-level
> alternative to Generative-Agents reflection, not a patch on it.

## The section's job in the paper

Make the memory contribution legible as an **architecture**, not a trick: show that GA
(reflection-style) memory and APM (provenance-style) memory share the same pipeline skeleton
and differ at exactly one layer — **integration** — and that this single difference is what
produces (GA) vs repairs (APM) social fidelity decay.

## The claim it must prove

1. GA-reflection and APM are **peer-level memory architectures** (drop-in, same interface),
   not a base + variant. (Empirically already true: the C5 table evaluates PROV as one memory
   condition among recognized architectures, same harness, and it is the only one that lifts
   held truth.)
2. The **only** architectural difference that matters is the integration rule: GA integrates by
   **frequency + recency** (DeGroot-style opinion synthesis); APM integrates by **provenance
   chain** (AGM / Doyle truth-maintenance-style belief revision).
3. APM is **interpretable by construction**: a held belief carries an auditable justification
   (source, version, origin round, independent provenance paths), which black-box memories
   (GA, Mem0, A-MEM, MemBank) cannot produce.

## Shared skeleton — difference is the INTEGRATE layer

```
            hears a claim
                 |
        +--------v---------+
        |   STORE          |
        +--------+---------+
        |   RETRIEVE       |
        +--------+---------+
        |  INTEGRATE       |  <-- the ONLY architecturally decisive difference
        +--------+---------+      (this layer decides held belief)
        |   SPEAK          |
        +------------------+
```

### GA (Generative Agents / reflection)

```
STORE      each observation = natural-language record (text, timestamp); no source/version
RETRIEVE   score = recency + importance + relevance
INTEGRATE  REFLECTION: synthesize/abstract over retrieved memories
             implicit rule = frequency + recency  ->  the most-heard / most-recent wins
SPEAK      utter the currently synthesized belief
```
Root cause of decay: integration counts how often / how recently a value was heard. The stale
value has the larger population base, so the stale value wins -> telephone decay.

### APM (Auditable Provenance Memory)

```
STORE      each claim = (value, source, version, origin_round, provenance_path)
RETRIEVE   score carries provenance (source credibility / version / path independence)
INTEGRATE  provenance-chain belief revision (TMS-style):
             (1) latest version that traces to an authoritative origin wins (not frequency)
             (2) chain-corroboration: count INDEPENDENT provenance paths to origin,
                 NOT the frequency of the surface value  [this is the fix for the C6 failure]
             (3) conflict / insufficient evidence -> downgrade to unknown / low-confidence (abstain)
SPEAK      utter belief + its restatable justification (from whom, which version, how many paths)
```
A large stale population cannot win: it does not trace to the latest authoritative origin. Every
belief is auditable: we can answer "why does the society hold this, and which hop corrupted it?"

## Per-layer comparison

| layer | GA (reflection) | APM (provenance) |
|---|---|---|
| storage unit | text observation stream (no source) | event with `(source, version, origin, path)` |
| integration rule | frequency + recency synthesis | latest authoritative version; **chain-corroboration (independent paths)** |
| conflict handling | implicit; majority / most-recent wins | explicit; insufficient evidence -> **abstain / downgrade** |
| who wins | the high-base stale value | the value that traces to authoritative origin |
| anti-spoofing | none (claiming high frequency hijacks) | yes (requires traceable / multi-path verification) |
| interpretability | black box; cannot say "why" | white box; belief = value + auditable justification chain |
| theoretical lineage | DeGroot-style opinion synthesis | AGM / Doyle TMS-style belief revision |
| failure mode | telephone decay (stale value entrenches) | (to verify) may flood to 100% under idealized comms -> must be evaluated under realistic friction |

## One-line positioning

```
GA-reflection : integrate belief by HEARD FREQUENCY        -> stale value wins -> decay
APM           : revise belief by PROVENANCE CHAIN + audit  -> true value wins  -> explainable
                = replace reflection's "frequency synthesis" with "provenance-traced revision"
```

## Failure modes / reviewer objections this section must answer

- **"You did not invent provenance."** Correct; the contribution is (a) the SAY/HELD dissociation
  diagnosis, (b) provenance as a *decentralized social-memory* integration rule evaluated head-to-head
  against recognized memories, and (c) auditability as a measured property — not the idea of provenance.
- **"APM is just GA with an extra field."** No: the integration paradigm changes from opinion
  synthesis (DeGroot) to belief revision (TMS). Empirically it is the only memory condition that
  moves held truth (C5).
- **"Generality is narrower than reflection."** True and stated: reflection is content-agnostic;
  APM is general over *sourced/versioned facts* (a broad but bounded class). We claim a peer-level
  architecture, not universal superiority; APM and reflection can compose (provenance-aware reflection).
- **"Does APM saturate to 100% like PROV did (C5 horizon)?"** This is the make-or-break check.
  The 100% was a COMMUNICATION-model artifact (every-utterance broadcast + lossless + sticky;
  diagnosed in C7), not a property of provenance integration. Under realistic friction (sparse
  comms / forgetting / ongoing noise / adversary) APM must settle to a stable, explainable
  sub-100% equilibrium that is clearly above GA. We pre-register this as the C15 success/failure
  criterion: if APM only beats GA by flooding to 100%, that is reported as a negative result.

## Evidence currently in hand

- C5 architecture table: PROV is the only memory (vs Raw / Mem0 / A-MEM / GA / GA-curr / MemBank)
  that lifts held truth -> peer-level, drop-in, and wins.
- C8/C9/C10: generalizes across scenarios, numeric fact-type, topologies.
- C14: the integration rule's advantage survives a model-family change (DeepSeek-V4-Flash):
  PROV 70.7% vs GA 17.3% held-current @ r5.
- C7: the 100% ceiling is a comms-model artifact; sparse comms yields a real equilibrium ~2x GA.

## Open questions before migration to LaTeX

- APM as written is the *target* architecture; the integration features (chain-corroboration,
  abstain, anti-spoofing) are NOT yet implemented or validated. They are the C15+ workstream.
- Need to confirm the sim stores the **provenance path** (not just version) required for
  chain-corroboration (`memories.py` / `society.py` audit).
- Saturation pre-registration (above) must run BEFORE claiming APM is a deployable/interpretable
  architecture, to avoid repeating the PROV-v2 (C6) overreach.
