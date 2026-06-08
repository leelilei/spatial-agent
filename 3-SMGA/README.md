# SMGA

Structured Memory for Generative Agents.

SMGA is an independent research project split out from SpatialAgent. Its working claim is that long-horizon generative agents need structured, evidence-grounded, contradiction-aware social memory objects that can be exposed to planning through auditable affordances.

The implementation-oriented proposal is:

- `docs/plans/SMGA-proposal-v4.5-lite.md`

The full defensive research blueprint is:

- `docs/plans/SMGA-proposal-v4.4.md`

## Project Layout

```text
.
├── docs/
│   ├── plans/
│   └── project/
├── assets/
│   └── papers/
├── smga-core/
├── benchmarks/
├── experiments/
├── annotation/
├── results/
└── paper/
```

## Directory Roles

- `docs/plans/`: proposal versions and staged research plans
- `docs/project/`: project notes, reference-source indexes, decisions, and execution logs
- `assets/papers/`: curated SMGA reference papers, notes, and generated indexes
- `smga-core/`: implementation of SMGA memory formation and planning interfaces
- `benchmarks/`: diagnostic benchmark definitions and external benchmark adapters
- `experiments/`: runnable experiment entrypoints and ablation orchestration
- `annotation/`: human annotation protocols, schemas, and claim-evidence validation assets
- `results/`: experiment outputs and analysis artifacts
- `paper/`: paper draft, figures, tables, and bibliography

## Migration Note

The SMGA proposal files were migrated from:

```text
../1-SpatialAgent/docs/plans/
```

Shared literature assets from SpatialAgent were not copied into this project. Use `docs/project/reference_sources.md` as the initial index, and only copy selected PDFs or notes into SMGA later when they become project-specific assets.
