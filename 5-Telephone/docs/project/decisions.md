# Decisions

## 2026-06-20 Adopt the research project standard

### Background

Telephone was created quickly from the 3-SMGA society-simulation work. Its experiment
ledger and paper notes grew faster than its project structure. The repository already has
a shared `0-Tools/research-standard/` convention for research projects.

### Decision

Telephone now follows that standard:

- current proposal lives at `docs/plans/proposal.md`;
- historical proposal drafts live in `docs/plans/archive/`;
- task tracking lives in `docs/guides/todolist.md`;
- structured project state lives in `docs/guides/project.yaml`;
- reference indexing lives in `docs/project/reference_sources.md`;
- reference artifacts live under `assets/papers/`.

### Rationale

This keeps the project dashboard-friendly and avoids version sprawl as the paper moves
from experiments into reference collection and drafting.

## 2026-06-20 Treat reference collection as the next active workstream

### Background

The current paper spine is stable enough to collect references around specific claims:
fidelity decay, speech-belief dissociation, path-dependent entrenchment, failed natural
levers, and judge-validated measurement.

### Decision

Reference work should proceed from `assets/papers/metadata/reference-report.md`, but only
promote papers into `paper/references.md` when they support a concrete sentence in the
paper.

### Rationale

The project needs a tight, claim-driven bibliography rather than a broad adjacent-paper
dump. This also follows the source policy in `docs/project/reference_sources.md`.


---

## 2026-06-21 — Cure direction, metric grounding, and process

**Context.** Human flagged the paper risked being "a finding without a result" (no
improvement → hard to publish), and pushed for a real architecture-level fix.

- **D1 — Pursue a CURE, not diagnosis-only.** The paper must show an intervention that
  improves held-belief fidelity *without* the trivial overwrite (broadcast). Aligns with the
  big-Claim-A 准绳.
- **D2 — The cure is PROV (provenance-aware integration).** Mechanism-matched to the
  entrenchment diagnosis: integrate heard claims by provenance (source + origin/version),
  not frequency; hold the latest authoritative version stickily; foreground it when speaking.
  This is the LISTENER-side lever smga3g lacked (smga3g moved SAY not HELD).
  - **C1 de-risk PASS** (mini, repair_drive, n=5): HOLD 18→58%.
  - **C2 validation** (n=8): PROV 40% [28–53] vs GA 22% [13–30]; **closes the dissociation**
    (source GA 21 vs PROV 51); unknown 68%→28%; **r30 sustains ~55% vs GA→6%**. First
    non-overwrite cure.
- **D3 — Next main result = architecture comparison table** (ED2D-style): PROV vs recognized
  NON-OVERWRITE baselines across scenarios. Rows = {raw/RAG, GA, currency/smga3g, A-MEM,
  MemoryBank, PROV, broadcast=ceiling}; cols = {repair_drive, book_club, carpool};
  metric = HOLD%. **Prerequisite: generalize PROV provenance to per-claim origin-round tags**
  (else "you handed PROV the answer" is fatal). SOTOPIA is the WRONG substrate (social-
  intelligence eval, not fact propagation); right axis = memory architectures; optional
  cross-framework replication = AutoGen/Concordia (NOT SOTOPIA), deferred until cure is solid.
- **D4 — Metric grounding.** `current/stale/unknown` is grounded in FEVER (3-way verdict),
  knowledge editing (efficacy vs locality), and the continued-influence effect. Add a
  dispersion/consensus entropy as a 2nd metric. Refs added to references.bib. See
  `paper/measurement_grounding.md`.
- **D5 — Process: pause LaTeX, write sections as Markdown first.** Local LaTeX build is
  blocked by the AAAI-2027 `newtx` dependency (no admin to install; tlmgr usermode declined).
  Since experiments are still evolving, write/iterate each paper section in `paper/*.md` and
  assemble into LaTeX once experiments are done. (A metric-grounding paragraph + the new bib
  entries were already added to `latex/main.tex`/`references.bib`; left in place, harmless.)

---

## 2026-06-22 — Novelty/competition check + experiment-coverage decision

**Trigger.** Lit search for related architectures + prior work. Found the closest concurrent
neighbor and reassessed whether our experimental coverage is sufficient.

- **D1 — Closest neighbor = "From Spark to Fire" (arXiv:2603.04474, 2026).** Has a
  Lineage-Graph **provenance cure**, "Propagation as Adoption" (adoption≠repetition), and
  "consensus inertia" (=our entrenchment). **Decision: cite prominently + differentiate; do
  NOT add as a comparison-table row** (it is a CENTRALIZED governance plugin + external
  verifier, not a per-agent memory architecture; giving it the ground truth = broadcast/
  unfair, withholding it ≈ PROV). Its two mechanisms are already covered by us: provenance =
  PROV (decentralized), external-authority = our M4 source (failed) + broadcast (ceiling).
  Note + 4-point differentiation: `assets/papers/neighbors/NOTE_spark_to_fire.md`. Lead our
  contribution on: correction-fails-to-install direction, SAY/HOLD separate elicitation, PROV
  as decentralized memory architecture + head-to-head table — NOT "we invented agent
  provenance." refs.bib += xie2026spark, chhikara2025mem0.

- **D2 — Paper type: we are a SCIENCE paper (depth), not a SYSTEMS paper (breadth).**
  Spark-to-Fire runs a 6-framework × 3-topology × 3-attack × multi-defense × 3-dataset matrix
  (LangChain/MetaGPT/AutoGen/CAMEL/CrewAI/LangGraph; MATH/MMLU/UCI). **We will NOT try to match
  that matrix.** Our edge is a sharp mechanism + measurement + cure, with a head-to-head memory
  architecture comparison they do not have.

- **D3 — But our external validity is currently thin; close these gaps (priority order):**
  1. **Architecture table across all 3 scenarios** (repair_drive done; add book_club, carpool)
     — confirm PROV's win generalizes. (In progress.)
  2. **Topology robustness** — we use ONE contact model (random matching). Add chain / star(hub)
     / small-world structures and re-run GA-vs-PROV (or the table). Directly answers the
     "single-topology artifact" attack and parallels their 3-topology coverage. (Needs a
     scheduler topology option.)
  3. **Capability check on the table** — re-run key rows (GA, PROV, +1-2 baselines) at gpt-5.4
     to show PROV's win is not mini-specific. (Cheap.)
  4. **Cross-framework replication (DEFERRED)** — reproduce the dissociation on AutoGen or
     Concordia (NOT SOTOPIA). Gold-standard external validity but heavy; do only if targeting a
     top venue / if reviewers demand it.

- **D4 — Sufficiency call:** core claims (dissociation, entrenchment, PROV cure) are near-solid
  (n=8, CIs, judge, capability ladder, 7-architecture table). Breadth is the gap. Prioritize
  D3.1–D3.3 (all cheap-ish) to neutralize the "single-harness/single-topology artifact"
  critique before investing in D3.4.

---

## 2026-06-22 (late) — PROV horizon climb to 100% is a DANGER SIGNAL (idealized channel)

**Finding (C5).** Fair-PROV climbs with propagation time: r5 57% → r10 93% → r20 100% (n=8/5/4),
while GA stays ~20% and decays. All recognized memories (Raw/Mem0/A-MEM/GA/GA-currency/MemoryBank)
fail at 14–25%.

**Danger signal (human-flagged, confirmed).** The 100% (zero variance) is NOT emergent reasoning.
PROV's provenance is a **lossless, automatic, always-adopted side-channel**: every utterance auto-
carries the version tag (content-independent), the listener adopts max-version by a hard rule (no
LLM, no doubt, no garble), sticky. → a **perfect gossip/flood** that mechanically saturates a
connected network. **PROV "cures" by routing AROUND the lossy LLM relay** (the very cause of
corruption), not by reasoning better about conflicting claims. Risks: (a) "broadcast in disguise"
dismissal (though it IS decentralized 1-source propagation, not central injection); (b) unrealistic
(real provenance is garbled/distrusted); (c) GA-vs-PROV contrast partly unfair (PROV rides a clean
channel GA lacks).

**Decisions.**
- **D1 — Do NOT headline "PROV→100% solves it."** Frame 100% as an **idealized UPPER BOUND**
  (what provenance achieves if losslessly preserved) → establishes provenance as the RIGHT LEVER.
  The honest operating result is the degradation curve (below).
- **D2 — Key next experiment: lossy provenance channel.** Make provenance survive each relay only
  with prob (1−loss) (models the recency/source framing not surviving LLM retelling). Sweep loss.
  If PROV still beats GA/frequency under realistic loss → **real, non-trivial cure** (the
  INTEGRATION RULE is what matters, not the magic channel). If it collapses to GA → the cure
  depends on idealization (a crucial honest finding either way).
- **D3 — The non-trivial core is the integration rule** (prefer latest-origin vs frequency), not
  the lossless channel. The stress-test isolates it. (Literal text-embedded provenance is an
  optional further variant.)
- This upholds the 准绳: report the idealization honestly, don't over-claim, solve under realism.
