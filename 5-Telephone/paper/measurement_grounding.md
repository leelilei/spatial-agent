# Measurement & Cure — Grounding (with references)

> Written 2026-06-21. Captures the "why these metrics / why provenance" discussion so the
> rationale + citations survive for when we assemble the paper. Bib keys refer to
> `latex/references.bib`; triage in `references.md`.

## 1. Why a `current / stale / unknown` verdict (the fidelity metric)

The task is a fact whose truth value **changed** (event rescheduled A→B). We probe each agent
and classify its held answer into three classes. This taxonomy is **not ad hoc** — it mirrors
recognized evaluation structures:

| Our class | What it captures | Public-standard analog | Ref |
|---|---|---|---|
| **current** | holds the new (correct) value | edit **efficacy** (new value takes hold); SUPPORTED | knowledge editing `meng2022rome,meng2023memit`; fact-verification `thorne2018fever` |
| **stale** | holds the old, **superseded** value | **specificity/locality** failure (old value not displaced); **continued-influence effect** | `meng2023memit`; misinformation `lewandowsky2012misinformation,thorson2016belief` |
| **unknown** | holds neither (lost / can't say) | NOT-ENOUGH-INFO; retention failure (exposure ≠ retention) | `thorne2018fever` |

**Why the 3-way split is load-bearing (not just correct/incorrect):** distinguishing **stale
(active corruption)** from **unknown (information loss)** is essential because the two respond
differently to interventions — e.g. capability converts *loss* into *confident corruption*
(M0). A binary correct/incorrect score would hide this, which is the project's most
non-obvious finding.

**Validation:** a semantic LLM judge reproduces the keyword verdict (P2, 99–100% agreement),
so the categories are not a keyword artifact.

## 2. Other public-standard metrics (could add / map to)

Ranked by value-to-add:
1. **Semantic LLM-judge verdict** — done (P2). Keep + foreground. (`manakul2023selfcheckgpt`,
   `farquhar2024detecting` for the broader practice.)
2. **Dispersion / consensus entropy** over the society's held values → quantifies *which
   attractor* and how converged; connects truth-decay to **diversity collapse** in
   self-consuming/model-collapse systems (`alemohammad2024selfconsuming`,
   `shumailov2023curse`). *Cheap to add; recommended as a second metric.*
3. **Knowledge-editing suite** (efficacy / generalization / **locality** / portability) —
   map current→efficacy, stale-persistence→locality failure (`meng2022rome,meng2023memit`).
4. **Transmission-chain fidelity** — reproduction accuracy / source→final mutual information,
   from iterated-learning (`kirby2008cumulative`).
5. **TruthfulQA / SelfCheckGPT** — single-agent truthfulness/consistency; cite as background.

## 3. Why **provenance** is the cure (PROV)

Three independent justifications — it is a principled, mechanism-matched cure, not a random
architecture:

1. **It negates the diagnosed mechanism.** Decay = *frequency/majority* integration → the
   stale incumbent wins (entrenchment). PROV integrates by *provenance* (source + origin
   round), so the latest authoritative version wins regardless of how often the stale one is
   repeated.
2. **It is normatively correct for a *changing* fact.** The correct belief about an updated
   fact is the **most recent authoritative version**; frequency is the *wrong* cue (an old
   value repeated often is still old). The integration rule must be time/version-aware.
3. **It is a classic idea, re-applied.** Justification/source tracking is the basis of
   **truth-maintenance systems** (`doyle1979truth`) and **belief revision** (AGM,
   `alchourron1985logic`); conflict resolution by "latest version" is standard **data/temporal
   provenance**; and weighting by **source credibility** (vs naive averaging) is the lever in
   social-learning/opinion-dynamics models (`degroot1974reaching`). PROV is the social-channel
   instance.

**Why it is a *fair* cure (not broadcast in disguise):** PROV does **not** overwrite agents.
The current value must still be HEARD via conversation; an agent that never hears it stays
stale/unknown. PROV only changes how an agent **integrates and relays** what it locally hears.

**Fairness caveat (must fix before the comparison table):** the de-risk PROV encodes
provenance via scenario value-markers (it is told *which* value is the latest). The paper
version must **generalize** to per-claim **origin-round/version tags** carried as conversation
metadata, so PROV is not "handed the answer" relative to the baselines.

**Evidence so far:** C1 de-risk (HOLD 18→58%, n=5) and C2 (n=8: 40 vs GA 22; closes the
speech–belief dissociation — source GA 21 vs PROV 51; r30: PROV sustains ~55% vs GA→6%). See
RESULTS.md C1/C2 and `figures/fig_cure_prov.png`.

## New references added (2026-06-21)
`thorne2018fever` (FEVER, NAACL'18) · `meng2022rome` (ROME, NeurIPS'22) ·
`meng2023memit` (MEMIT, ICLR'23) · `lewandowsky2012misinformation` (continued-influence) ·
`alchourron1985logic` (AGM belief revision) · `doyle1979truth` (TMS) ·
`degroot1974reaching` (consensus/opinion dynamics).
Added to `latex/references.bib` (verified venues/years; pages where known).
