# SMGA

Structured Memory for Generative Agents.

SMGA is an independent research project split out from SpatialAgent.

**Working claim (updated 2026-06-15):** structured social memory is a
**capability-amplification** mechanism — affordance-bearing memory lets a weak/cheap
planner match a strong one on social-planning decisions, while plain memory degrades
as the model weakens. Diagnostic evidence: on gpt-5.4-mini, plain memory drops to 57%
while M3 (structured affordance memory) holds at 98%; the M3-vs-plain gap roughly
doubles vs gpt-5.4. The original "structured format / currency improves accuracy"
framing did NOT survive testing on a frontier model (all such effects are null on
gpt-5.4; structure moved only cost, and cost is out of scope). See
`docs/project/findings_capability_axis_2026-06-15.md`.

The implementation-oriented proposal is:

- `docs/plans/proposal.md`

The full defensive research blueprint is:

- `docs/plans/archive/SMGA-proposal-v4.4.md`

The current direction + investigation log (read this first) is:

- `docs/project/findings_capability_axis_2026-06-15.md`

Supporting result/design notes from the 2026-06-15 investigation:

- `docs/project/stage1_v2_final_2026-06-15.md` (clean 10-seed v2 result)
- `docs/project/stage2_main_40seed_2026-06-15.md` (40-seed run; M0 headline superseded — uses strawman GA)
- `docs/project/probe0001_structure_confound_audit_2026-06-15.md` (format is not the driver)
- `docs/project/structure_at_scale_design_2026-06-15.md` (structure = cost, not accuracy)
- `docs/project/stage2b_horizon_sweep_plan_2026-06-15.md` (1M-context-aware plan; deprioritized)

The earlier Experiment 0 failure-analysis note is:

- `docs/project/experiment0_probe_0002_diagnostic.md`

The current Experiment 0 judge snapshot is:

- `docs/project/experiment0_judge_snapshot_2026-06-14.md`

The current Stage 1 10-seed pilot report is:

- `docs/project/stage1_pilot_10seed_2026-06-15.md`

The current Gate 1 failure audit is:

- `docs/project/gate1_failure_audit_2026-06-15.md`

The earlier Stage 1 alpha pilot report is:

- `docs/project/stage1_pilot_alpha_2026-06-15.md`

The current implementation-facing memory schema is:

- `docs/project/smga_memory_schema_v0.1.md`

The current diagnostic scenario-package schema is:

- `docs/project/smga_scenario_package_schema_v0.1.md`

The current normalized probe response schema is:

- `docs/project/normalized_probe_response_schema_v0.1.md`

The current model-calling and baseline-run guide is:

- `benchmarks/diagnostic_v0/README.md`

## Project Layout

```text
.
├── docs/
│   ├── guides/
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
- `docs/guides/`: active todo lists and execution guides
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
