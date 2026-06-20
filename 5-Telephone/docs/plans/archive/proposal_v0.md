# Telephone — Research Proposal v0

> **SUPERSEDED by `proposal_v1.md`** (2026-06-19) — v1 folds in the literature review
> (attractor/phase-boundary reframe, elevated C4, diversity metric, competitive
> positioning). Kept for history.

> Status: DRAFT for discussion (2026-06-19). This is the "what are we actually writing"
> document: the phenomenon, the sexy-but-falsifiable claim, the positioning, the target
> venues, and what "solid" requires. Numbers go in `../../RESULTS.md`; story in
> `../../paper/narrative.md`.

---

## 0. One-line pitch

**When LLM agents pass information to each other, the truth does not survive intact — it
decays in a predictable, governable way. We measure the decay, find its laws, and show
what stops it.**

A sharper framing for the abstract: *agent-to-agent transmission is a lossy channel; we
characterize the loss as the inference-time, social analog of "model collapse."*

---

## 1. The phenomenon (and why we believe it is real)

Generative-Agents-lineage work celebrates that information **spreads** through an agent
society (Park et al.'s Isabella-party diffusion is the canonical success demo). The field
measures **reach** — did it spread — and treats spread as success. **Nobody measures
fidelity — is what spread still true?**

We have direct evidence it often is not. In a 25-agent society where a fact-update was
injected (an event's day/place changes Saturday→Sunday), agents did not faithfully relay
it. Instead (parent project, `../../../3-SMGA/sim/RESULTS.md`, S5L-diag):
- the **superseded value persisted and out-competed the update** (seed 41: 18 of 22
  agents who "received" the update were nonetheless Saturday-dominant in their own stream);
- **details drifted** ("community center" → "community shed");
- **versions split** across sub-groups.

The society converged not on the truth but on a **corrupted consensus**. That is the
phenomenon Telephone studies. (Methodological honesty: in 3-SMGA this same corruption was
a *confound* that defeated a memory-ranking claim. Here it is promoted from confound to
*object of study*.)

---

## 2. Why now (the timeliness hooks that make it sexy)

1. **Multi-agent LLM systems are exploding** — agent swarms, "societies of mind," LLMs
   debating/critiquing/relaying to other LLMs in production pipelines. If agent-to-agent
   transmission silently corrupts information, that is a **systemic, unmeasured failure
   mode** of the architecture everyone is now shipping.
2. **The "model collapse" anxiety** (training on AI-generated data degrades models;
   Shumailov et al., *Nature* 2024) has a missing sibling: **inference-time, social
   collapse** — degradation through agent-to-agent *communication*, not training. We name
   and measure it.
3. **AI echo chambers / synthetic-information ecosystems** are a live policy concern. A
   controllable testbed for how truth degrades among communicating AIs is timely and
   citable beyond ML.

---

## 3. Research questions

- **RQ1 (existence & shape).** Does a ground-truthed update degrade as it propagates, and
  what is the shape of the **fidelity-decay curve** (vs hops / rounds / distance-from-
  source)? Is it monotone, threshold-like, or does it stabilize at a corrupted attractor?
- **RQ2 (governing laws).** What governs the decay? We sweep: network **connectivity**,
  model **capability** (weak→strong), message **redundancy/framing**, presence of an
  **authoritative re-broadcaster**, and **agent memory architecture**.
- **RQ3 (attractors).** What does the society *converge on*? Truth, a single dominant
  corruption, or fragmented versions? Is there a **connectivity/capability phase boundary**
  between truth-convergence and corruption-convergence?
- **RQ4 (error-correction).** Can a memory architecture or a protocol act as
  **error-correction / anti-entropy** that preserves collective fidelity — and what is the
  minimal intervention that flips the society back to truth-convergence?

---

## 4. Central claims (sexy AND falsifiable, with predicted laws)

- **C1.** *Agent-to-agent transmission is lossy*: fidelity decays measurably with
  transmission distance; reach ≠ fidelity (an agent can be "reached" yet hold a corrupted
  version). [Falsifier: fidelity is flat in hops / equals reach.]
- **C2.** *The decay has governing laws*: it worsens monotonically as model capability
  drops and as redundancy/authority decrease; there is a **phase boundary** in
  (connectivity × capability) separating truth- from corruption-convergence. [Falsifier:
  no systematic dependence; convergence is random.]
- **C3.** *Corruption is structured, not random*: it is dominated by a small taxonomy —
  **stale-persistence**, **detail-drift**, **fabrication**, **loss** — with predictable
  relative frequencies by regime. [Falsifier: corruption is idiosyncratic/unclassifiable.]
- **C4.** *It is correctable*: a targeted intervention (an authoritative re-broadcast, or a
  currency-resolving memory) provably shifts the society across the phase boundary toward
  truth. [Falsifier: no intervention helps; it is irreducible.]

The headline is C1+C2 (existence + laws). C4 is where **memory re-enters as a variable**
(error-correction), recycling the SMGA work honestly — not as "structured memory wins,"
but as "here is the minimal fix for a now-quantified failure."

---

## 5. Positioning vs related work (the academic move)

We sit at a deliberate **intersection** that none of the neighbors occupy:

- **Generative Agents / multi-agent LLMs** (Park 2023; Concordia; OASIS; AgentSociety):
  they measure diffusion **reach** and emergent macro-behavior. **We measure fidelity** —
  the orthogonal axis they skip.
- **Iterated learning / transmission-chain experiments** (cognitive science; Kirby;
  Bartlett's classic "telephone"): a respected paradigm showing human cultural
  transmission compresses/regularizes information. **We run the LLM-agent version** and ask
  whether LLMs distort like humans, differently, or worse — giving us a credible,
  established methodological lineage (transmission chains) + a novel substrate (LLM
  societies).
- **Model collapse** (Shumailov 2024, *Nature*): degradation via *training* on synthetic
  data. **We are the inference-time, communicative analog** — degradation via *talking*.
  Strong, quotable contrast.
- **Misinformation / rumor propagation** (computational social science): classically
  modeled with hand-specified transmission rules. **Our transmission rule is an actual
  LLM** — so distortion is endogenous, not assumed.

The one-sentence niche: **the first systematic, quantitative characterization of
information *fidelity* (not reach) in LLM-agent societies, framed as social/inference-time
model collapse, with governing laws and a corrective intervention.**

---

## 6. Method

### 6.1 Instrument
The controllable society sim reused from 3-SMGA (`sim/`): pluggable per-agent memory,
seeded encounter schedule with tunable connectivity, an injectable ground-truthed update,
and the proven provider transport. Used as a measurement instrument, not a benchmark.

### 6.2 Conditions / independent variables
- connectivity (meetings/round), horizon (rounds), turns/encounter;
- model capability (gpt-5.4-mini ↔ gpt-5.4; mixed populations);
- message redundancy & framing of the injected update;
- authoritative re-broadcast on/off and frequency;
- memory architecture (raw stream / GA-reflection / currency-resolving) — as a C4 knob.

### 6.3 Metrics (FROZEN before first real run; designed to avoid the 3-SMGA traps)
- **Fidelity** of an agent's held/spoken version vs ground truth — scored by an LLM judge
  on a rubric, NOT by surface-keyword match (kills the keyword-circularity that confounded
  SMGA), with human-audited calibration on a sample.
- **"Reached" defined independently of the answer** (e.g., the agent's stream contains the
  update *event* via provenance tags we inject, not the answer keyword).
- **Decay-vs-hops**: fidelity as a function of graph distance from the source.
- **Version-share**: truth-share vs each corruption-share over time → convergence/attractor.
- **Corruption taxonomy counts**: stale-persistence / drift / fabrication / loss.
- **Variance-first**: every headline is multi-seed with effect size + CI; we treat the
  sim's chaotic stochasticity (a 3-SMGA finding) as a measured property, not a nuisance.

### 6.4 Experiment arc (each row goes in the ledger)
- **M0**: one regime — establish the decay curve exists and is quantifiable.
- **M1**: connectivity × capability sweep — find the phase boundary (C2).
- **M2**: corruption taxonomy over regimes (C3).
- **M3**: interventions (authority, memory) — the correction (C4).

---

## 7. What "solid" means here (rigor commitments)

1. **Pre-registered metrics**: freeze fidelity rubric + "reached" definition + taxonomy in
   `docs/plans/metrics.md` BEFORE M1; human-audit the judge on a sample.
2. **Power & reproducibility**: multi-seed, effect-size + CI on every claim; full
   transcript/seed/model-version/prompt logging (the field's #1 reproducibility gap).
3. **No keyword circularity, no underpowered nulls, no hype** (carried-over 准绳).
4. **Every run recorded** in the ledger — including failures.

---

## 8. Target venues (tiered)

- **Primary (ML/LLM-agents):** **COLM** (Conference on Language Modeling — ideal fit), or
  **NeurIPS / ICLR** (main track, or Datasets & Benchmarks if we ship the testbed).
- **Strong alternative (NLP):** **ACL / EMNLP** (computational social science / agents
  track).
- **Big-splash interdisciplinary (if C1+C2 land cleanly and generalize):** **Nature
  Machine Intelligence / Nature Human Behaviour / PNAS** — "social model collapse" is the
  kind of crisp, quotable result those venues take. Aim here only if the laws are robust.
- **Fallback / fast flag-planting:** NeurIPS/ICLR multi-agent or "agentic" workshops, then
  extend to a main-track submission.

Decision rule: land C1+C2 with CIs first → if the phase boundary is clean and
model-general, aim interdisciplinary; otherwise COLM/NeurIPS with the testbed + taxonomy +
intervention as the contribution.

---

## 9. Target field / framing choice

Primary field: **LLM multi-agent systems / AI safety-of-agents**, framed so it also speaks
to **computational social science** (transmission chains) and the **model-collapse**
literature. We lead with the engineering-relevant framing (a failure mode of multi-agent
LLM pipelines) because it is the most defensible and the most timely; we borrow the
transmission-chain paradigm for methodological credibility and the model-collapse contrast
for the hook.

---

## 10. Risks & mitigations

- **R1: "It's obvious that weak models garble things."** → Mitigate by finding the *laws*
  and the *phase boundary* (not just existence), and by testing STRONG models / mixed
  populations: if strong agents also distort past a connectivity threshold, that is
  non-obvious and important.
- **R2: Judge/metric circularity (the SMGA wound).** → Pre-registered rubric, provenance-
  based "reached," human calibration, report judge agreement.
- **R3: Chaotic variance.** → It's a measured property; multi-seed + CI; report it as a
  finding (robustness of convergence), not hide it.
- **R4: Generality (one scenario).** → ≥2–3 structurally different update scenarios
  (non-Chinese, per user); show the laws hold across them before any big claim.
- **R5: Confound with "the sim is just our artifact."** → Cross-model, cross-scenario,
  and connect quantitatively to the human transmission-chain literature where possible.

---

## 11. Why this is tractable for us (reuse)

We already have: the society-sim instrument, embedding retrieval (model2vec), the proven
transport, and — most valuably — the **reproducibility/variance/controlled-replay rigor**
hard-won in 3-SMGA, which is exactly the scarce skill this phenomenon-study rewards. The
memory variants from SMGA become C4 intervention conditions. We are not starting cold; we
are repurposing a battle-tested rig toward a better-posed question.

---

## 12. Immediate next steps (no experiments until these are done)

1. Pin down `docs/plans/metrics.md` (fidelity rubric, provenance-based "reached",
   corruption taxonomy) — the pre-registration.
2. Prune the SMGA-specific cheats from `sim/memories.py`; keep raw + GA-reflection as the
   transmission substrates; design provenance-tagged injection.
3. M0 pilot: one regime, establish the decay curve. Then this proposal becomes v1 with
   real numbers.
