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
