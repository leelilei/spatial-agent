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

