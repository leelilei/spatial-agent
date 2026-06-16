# SMGA

Structured Memory for Generative Agents.

SMGA is an independent research project split out from SpatialAgent. North star:
**LLM game agents** — believable multi-agent social *simulation* (Generative Agents
lineage). Memory is the lever, not the goal.

**Current focus (2026-06-16): the society simulation (`sim/`).** The short-context,
single-shot diagnostic regime (`benchmarks/diagnostic_v0/`) cannot decisively rank
memory architectures (proven across our experiments). The goal — show that an
improved social memory makes a *society* of agents more coherent over a long horizon
— requires a live multi-agent sim. `sim/society.py` is a minimal, controllable,
pluggable-memory society. First live result on a currency-stress scenario (a mid-sim
fact update — the repair drive moves to a new day/place): SMGA v2 kept **4/4** agents
on the current truth vs GA reflection **3/4** on gpt-5.4, and the gap **widens sharply
on the weak model — SMGA v2 4/4 vs GA 0/4** on gpt-5.4-mini (GA's free-text reflection
lost the updated detail for every agent). The advantage grows as the per-agent model
weakens — exactly the regime where memory architecture should matter. (Preliminary:
n=1 run, 4 agents; scaling + multi-run + more coherence dimensions is next.) The
companion eval-benchmark project lives at `../3-SMGA-EVAL`.

**Earlier working claim (diagnostic, 2026-06-15):** SMGA is **amortized / distilled
social-planning memory**. A capable model consolidates interactions once into
affordance-rich structured memory; cheap downstream planners then reuse it to decide
at near-frontier quality. Diagnostic evidence (40 seeds, strong-formed memory): a
gpt-5.4-mini planner retains 91% on M3 (structured affordance memory) vs gpt-5.4's
94% — a 97% retention — while the same mini planner drops to 65% on plain memory and
71% on GA-style reflective memory. M3 is the most capability-robust representation:
its advantage over GA-style reflection grows monotonically as you weaken formation or
planning (+10pp strong agent → +20pp weak planner → +23pp full weak agent). Best case
is "strong formation + cheap decisions" (distillation, 91% near-frontier); even a
fully weak agent keeps a clear edge (M3 72% vs reflective 49% vs plain 60% at 40
seeds). Earlier framings that did NOT survive testing: "structured format/currency
improves accuracy" (null on gpt-5.4) and cost (out of scope — prior work, and our
inspiration). See `docs/project/findings_capability_axis_2026-06-15.md`.

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
