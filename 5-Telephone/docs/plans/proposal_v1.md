# Telephone — Research Proposal v1

> Supersedes `proposal_v0.md` (kept for history). v1 folds in the literature review
> (`../../telephone-research.md`): the **attractor / phase-boundary** reframe (iterated
> learning), an **elevated C4** (social analog of verifier-guided collapse-escape), a
> **version-diversity** metric axis, and explicit **positioning vs the close 2025–2026
> neighbors**. Numbers → `../../RESULTS.md`; story → `../../paper/narrative.md`.

---

## 0. One-line pitch

**When LLM agents pass information to each other, the truth does not survive intact: a
society converges to a *truth attractor* or a *corruption attractor*, separated by a
predictable phase boundary — and a minimal correction can flip it back.**

Abstract hook: *agent-to-agent transmission is a lossy channel — the inference-time,
social analog of "model collapse" — and we give its governing laws and its cure.*

---

## 1. Phenomenon and evidence

GA-lineage work celebrates that information **spreads** (Park et al., 2023, Isabella's
party) and measures **reach**. **Nobody measures fidelity — is what spread still true?**

Direct evidence it is not (parent project, `../../../3-SMGA/sim/RESULTS.md`, S5L-diag): an
injected update (an event's day/place, Saturday→Sunday) was NOT faithfully relayed —
- the **superseded value persisted and out-competed the update** (seed 41: 18 of 22
  "reached" agents were Saturday-dominant in their own stream),
- **details drifted** ("community center" → "community shed"),
- **versions split** across sub-groups.

Crucially, this is not random noise. As iterated-learning experiments show (Kirby et al.,
2008, *PNAS*; Bartlett, 1932), serial transmission **contracts information toward an
attractor** — often a simpler, more "learnable," stale form. Our corrupted consensus is
exactly such an attractor. That reframing (attractor, not noise) is the spine of v1.

---

## 2. Why now + the competitive landscape

**Timeliness.** (i) Multi-agent LLM pipelines are shipping everywhere; if agent-to-agent
transmission silently corrupts information, that is an unmeasured systemic failure mode.
(ii) "Model collapse" (Shumailov et al., 2024, *Nature*) named training-time recursive
degradation; the **communication-time, social analog is missing** — we name and measure
it. (iii) AI echo chambers are a live policy concern.

**The neighborhood is filling — and that is both validation and a clock.** Two 2026
preprints sit in our exact area but stop short of our framing:
- **Becker et al., 2026 — Misinformation propagation in benign multi-agent systems**
  (MINT dataset): misinformation persists in benign MAD; group composition & protocol
  matter. Endpoint = task correctness in *debate*.
- **Jamshidi et al., 2026 — Hallucination Cascade**: in 3-agent chains, hallucination ↓
  but **factual accuracy also ↓** (0.789→0.769). Endpoint = claim-level accuracy in a
  *sequential cascade*.

Neither does **society-scale fidelity-decay-vs-hops, version-share/diversity dynamics, a
truth↔corruption phase boundary, or a minimal corrective intervention**. That gap is our
contribution. The clock means: **plant a flag fast (a clean M0 decay curve), and lean on
measurement rigor + society-scale dynamics as the moat.**

---

## 3. Research questions (attractor-framed)

- **RQ1 (existence & shape).** Does a ground-truthed update degrade with transmission
  distance? What is the **fidelity-decay curve** (vs hops/rounds/distance-from-source) —
  monotone, threshold, or stabilizing at a corrupted attractor?
- **RQ2 (governing laws & phase boundary).** What governs convergence to a **truth
  attractor** vs a **corruption attractor**? Sweep connectivity, model capability (incl.
  **heterogeneous populations**), message redundancy/framing, authority, and memory
  architecture; locate the **phase boundary** in (connectivity × capability).
- **RQ3 (what corrupts, and how diverse).** What does the society converge on — truth, a
  single dominant corruption, or fragmented versions? Report **truth-share AND version-
  diversity** (a low-diversity, high-consensus error is its own failure; cf. "Self-
  Consuming Models Go MAD", Alemohammad et al., 2023). Corruption taxonomy:
  stale-persistence / detail-drift / fabrication / loss.
- **RQ4 (correction).** Can a **minimal** intervention — authoritative re-broadcast,
  provenance-aware retrieval, or a currency-resolving memory — flip the society across the
  phase boundary toward truth? What is the smallest fix that works?

---

## 4. Central claims (sexy, falsifiable, attractor-framed)

- **C1 — lossy transmission.** Fidelity decays measurably with transmission distance;
  **reach ≠ fidelity** (a "reached" agent can hold a corrupted version). [Falsifier:
  fidelity flat in hops / equals reach.]
- **C2 — laws & phase boundary.** Decay worsens monotonically as capability/redundancy/
  authority drop; there is a **phase boundary in (connectivity × capability)** separating
  truth-convergence from corruption-convergence. [Falsifier: no systematic dependence;
  convergence random.] *(Neighbor to beat: Kim et al., 2025, "Science of Scaling Agent
  Systems" — they find performance phase behavior, error amplification 17.2× vs 4.4×; we
  recast the boundary as truth↔corruption dynamics, not performance.)*
- **C3 — structured corruption + diversity collapse.** Corruption is dominated by a small
  taxonomy with regime-predictable frequencies, AND the society often suffers **diversity
  collapse** (converging confidently on one stale attractor). [Falsifier: corruption
  idiosyncratic; diversity unrelated to regime.]
- **C4 — correctable (the social analog of verifier-guided collapse-escape).** A minimal
  intervention provably shifts the society across the boundary toward truth. C4 is
  theoretically anchored: Yi et al. (2025) show an external **verifier halts model collapse
  but converges to the verifier's "knowledge center"** — our **authoritative re-broadcast**
  is the social-channel isomorph; **currency-resolving memory** mirrors temporal
  conflict-resolution memory (APEX-MEM, Banerjee et al., 2026); and memory can also
  **amplify** error (Xiong et al., 2025), so the intervention design is non-trivial.
  [Falsifier: no minimal intervention helps; corruption irreducible.]

Headline = **C1 + C2** (existence + laws/phase boundary). **C4** is the second leg and is
where memory re-enters honestly — not "structured memory wins," but "here is the minimal
cure for a now-quantified failure, and it is the social version of a known collapse-escape
result."

---

## 5. Related-work positioning (must-cite-and-beat)

| Cluster | Anchor works | What they give us | How we go beyond |
|---|---|---|---|
| Agent societies | Park 2023 (Generative Agents); Vezhnevets 2023 (Concordia); Yan 2025 (comm-centric survey) | the instrument + the "reach as success" canon | measure **fidelity**, the axis they skip |
| MAS failure / scaling | Cemri 2025 (MAST, failure taxonomy); **Kim 2025 (scaling laws, phase behavior)** | taxonomy method; that laws/boundaries are findable | recast endpoint from **performance** to **truth↔corruption dynamics** |
| Transmission chains | Bartlett 1932; **Kirby 2008 (PNAS)**; Mesoudi & Whiten 2008; Ren 2020 (neural iterated learning) | the attractor paradigm + scientific lineage | run it in an **LLM society**, with fidelity not structure-emergence |
| LLM collective dynamics | **Ashery 2025 (Science Adv): conventions, collective bias, minority tipping** | attractors & tipping in LLM populations | apply to **truth vs corruption** attractors + correction |
| Model collapse | Shumailov 2024 (Nature); Alemohammad 2023 (MAD); Seddik 2024 (thresholds); **Yi 2025 (verifier escape)** | the framing + threshold + **correction theory** | the **communication-time, social** analog; C4 |
| Misinformation | Vosoughi 2018 (Science: false>true reach); Del Vicario 2016 (PNAS: echo chambers); Hu 2025 (LLM rumor sim); **Becker 2026 (benign MAS)**; **Jamshidi 2026 (hallucination cascade)** | reach≠truth; closest contemporaneous baselines | **decay-vs-hops + version-share/diversity + attractor + minimal correction**, society-scale, trace-level |
| Memory / correction | Lewis 2020 (RAG); Shinn 2023 (Reflexion); Xiong 2025 (memory error-propagation); **Banerjee 2026 (APEX-MEM)**; Xu 2025 (A-MEM) | C4 intervention templates | memory as a **phase-transition knob inside a society** |

One-sentence niche: **the first society-scale, quantitative characterization of information
*fidelity* (not reach) in LLM-agent societies — framed via the transmission-chain attractor
paradigm and as social/inference-time model collapse — with governing laws, a phase
boundary, and a minimal corrective intervention.**

---

## 6. Method

### 6.1 Instrument
Controllable society sim reused from 3-SMGA (`sim/`): pluggable per-agent memory, seeded
schedule with tunable connectivity, **provenance-tagged** injectable ground-truthed update,
proven transport. A measurement instrument, not a benchmark.

### 6.2 Conditions (independent variables)
connectivity (meetings/round) · horizon (rounds) · turns/encounter · model capability
(mini ↔ strong, **and heterogeneous mixed populations**) · update redundancy/framing ·
authoritative re-broadcast (on/off, frequency) · memory architecture (raw / GA-reflection /
currency-resolving) as the C4 knob.

### 6.3 Metrics — FROZEN before M1, designed to avoid the 3-SMGA traps
- **Multi-dimensional fidelity** (LLM-judge on a pre-registered rubric, human-audited on a
  sample): proposition-correctness · detail-faithfulness · currency-correctness ·
  version-consistency · provenance-traceability. NOT surface-keyword match (kills the
  keyword-circularity that confounded SMGA).
- **"Reached" defined by provenance** (the agent's stream carries the injected update's
  tag), independent of the answer keyword.
- **Decay-vs-hops**: fidelity vs graph distance from source.
- **Version-share AND diversity**: truth-share vs each corruption-share over time, plus a
  diversity index (catch low-diversity high-consensus errors).
- **Corruption taxonomy counts**: stale-persistence / drift / fabrication / loss
  (trace-level, MAST-style auditable labels).
- **Variance-first**: every headline multi-seed with effect size + CI; the sim's chaotic
  stochasticity (a 3-SMGA finding) is a *measured property* (robustness of convergence),
  not a nuisance.

### 6.4 Experiment arc (each row → ledger)
- **M0** — one regime: establish the decay curve exists and is quantifiable (the flag).
- **M1** — connectivity × capability sweep (incl. heterogeneous): the phase boundary (C2).
- **M2** — corruption taxonomy + diversity over regimes (C3).
- **M3** — interventions (authority / provenance-retrieval / currency-memory): the cure (C4).
- **≥2–3 structurally different update scenarios** (time / place / person-attribute;
  non-Chinese) before any big claim — generality, not a prompt-specific artifact.

---

## 7. What "solid" means (rigor commitments)

1. **Pre-registered** fidelity rubric + provenance-based "reached" + taxonomy in
   `docs/plans/metrics.md` BEFORE M1; human-audit the judge, report agreement.
2. **Power & reproducibility**: multi-seed, effect size + CI; full transcript/seed/model-
   version/prompt logging (the field's #1 reproducibility gap).
3. **No keyword circularity, no underpowered nulls, no hype** (carried-over 准绳).
4. **Trace-level**, not final-answer-only (our edge vs Becker/Jamshidi).
5. **Every run recorded** in the ledger — including failures.

---

## 8. Target venues (tiered)

- **Primary (LLM-agents):** COLM (ideal), or NeurIPS / ICLR (main, or Datasets & Benchmarks
  if we ship the testbed + scenarios + judge).
- **NLP alt:** ACL / EMNLP (computational social science / agents).
- **Big-splash (only if C1+C2 land clean & model-general):** Nature Machine Intelligence /
  Nature Human Behaviour / PNAS — "social model collapse" with governing laws is their kind
  of crisp, quotable result. (Neighbors already publish here: Ashery 2025 in *Science
  Advances*; Vosoughi 2018 in *Science*.)
- **Fast flag:** a NeurIPS/ICLR agent/CSS workshop with M0+M1, then extend to main track.

Decision rule: land C1+C2 with CIs → clean & general → aim interdisciplinary; else
COLM/NeurIPS with testbed + taxonomy + correction.

---

## 9. Target field / framing

Lead with **LLM multi-agent systems / safety-of-agents** (most defensible, most timely:
a failure mode of shipped pipelines), borrow the **transmission-chain** paradigm for
methodological credibility, and use the **model-collapse** contrast as the hook (stated as
analogy, not established term).

---

## 10. Risks & mitigations

- **R1 "obvious that weak models garble."** → Find the *laws* and *phase boundary*; test
  **strong & heterogeneous** populations — if strong agents also distort past a
  connectivity threshold, that is non-obvious and important.
- **R2 judge/metric circularity (the SMGA wound).** → Pre-registered multi-dim rubric,
  provenance-based "reached", human calibration, report judge agreement.
- **R3 chaotic variance.** → measured property; multi-seed + CI; reported as robustness.
- **R4 generality.** → ≥2–3 structurally different scenarios (non-Chinese).
- **R5 "the sim is just our artifact."** → cross-model, cross-scenario, and connect
  quantitatively to the human transmission-chain literature.
- **R6 (new) competitive scoop.** → the space is filling (Becker/Jamshidi 2026); move fast
  on M0+M1 and differentiate on society-scale dynamics + rigor, not on "MAS makes errors."

---

## 11. Why tractable for us (reuse)
Already have: the society-sim instrument, embedding retrieval (model2vec), proven
transport, and — most valuably — the reproducibility/variance/controlled-replay rigor
hard-won in 3-SMGA. SMGA's memory variants become C4 intervention conditions. We are
repurposing a battle-tested rig toward a better-posed question.

---

## 12. Immediate next steps (no experiments until 1–2 done)
1. `docs/plans/metrics.md` — pre-registration (multi-dim fidelity rubric, provenance-based
   "reached", corruption taxonomy, diversity index).
2. Prune SMGA-specific cheats from `sim/memories.py`; keep raw + GA-reflection substrates;
   build provenance-tagged injection.
3. **M0 flag**: one regime, establish the decay curve + first attractor evidence. Then this
   becomes proposal v2 with real numbers.
