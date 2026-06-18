# SMGA

Structured Memory for Generative Agents.

SMGA is an independent research project split out from SpatialAgent. North star:
**LLM game agents** — believable multi-agent social *simulation* (Generative Agents
lineage). Memory is the lever, not the goal.

## Working Principles (准绳)

These govern how we work. They override convenience.

1. **Aim for a big claim.** The target claim is **A**: *improved structured social
   memory (SMGA v2) makes a society of agents more coherent over a long horizon.*
   We do not retreat to a smaller, safer claim because the big one is hard. Small
   claims do not produce good work. If the evidence is not there yet, we build the
   evidence — we do not shrink the claim to fit what we already have.
2. **Solve problems; do not abandon them.** When an experiment exposes a problem
   (high variance, a retrieval ceiling, weak diffusion, a confound), the problem is
   an *obstacle on the path to Claim A* — something to fix — not a reason to change
   direction or lower the bar. "Switching tracks to avoid the hard part" is failure;
   "naming the obstacle and removing it" is the job. We may sequence problems, but
   we do not drop them.
3. **No underpowered nulls, no hype.** A result counts only with adequate power
   (variance controlled, effect size + CI) and honest scope. We neither overclaim
   nor settle for "n=1 looked good."

**Current focus (2026-06-18): the society simulation (`sim/`).** The short-context,
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
n=1 run, 4 agents; `sim/run_society_sweep.py` now provides the scaling/multi-run
harness, and this claim is now being stress-tested in 25-agent pilots.) The
companion eval-benchmark project lives at `../3-SMGA-EVAL`.

**Latest society result (2026-06-18): powered 5-seed main result + low-variance
instrument.** Stack upgraded (embedding retrieval; anchored consolidation; connectivity
`meetings_per_round`). On the full society (25 agents, meetings=2, r5, 5 seeds, paired),
the RAW result does **not** support Claim A: current GA 17% vs SMGA 25% (Δ+2/25, 95% CI
includes 0), and SMGA stale (34%) is far worse than GA (9%) — a changed central fact
strands a web of dependent side-commitments on the old value. We also found the sim is
**chaotically stochastic** (temp-0 gives no reproducibility), so claims need replication
+ power. We built a low-variance instrument — `replay_eval.py`, which replays a FIXED
event stream into each memory — and, crucially, conditioned the metric on agents who
**received** the update (isolating memory coherence from diffusion). Under that correct
metric, **SMGA v2 keeps 48% of informed agents on the current truth vs GA's 31%
(+17pp)** — the first low-variance evidence FOR Claim A's core (GA wins only by
forgetting: 57% unknown). An entity-centric **v3** (event registry as single source of
truth + late binding + a deterministic guard against incidental-mention clobbering) now
**replicates across 5 independent fixed event logs**: receiver-conditioned current-rate
**v3 69% vs v2 35% vs GA 25%**, with v3 also the LOWEST stale (15%). Paired per-log
(n=5): **v3−GA +43pp (95% CI [+25,+61], significant)**, v3−v2 +35pp (significant), while
v2−GA is only +8pp (ns) — so the win is localized to the entity-registry design, not
"structured memory" in general. And in the **LIVE sim** (memory feeds back into
behaviour, so a good relay re-transmits the update), the gap is even larger: v3 puts
**67% of the whole society** on the current truth vs GA's 14% (n=5 seeds; v3−GA +53pp,
95% CI [+30,+75], significant). It wins on BOTH **relay** (reaches 19.6/25 agents vs
GA's 9.6 — a forgetful GA agent is a broken relay) and **retention** (86% of receivers
stay current vs 38%). This is the first powered evidence for Claim A's core: structured
currency memory >> the GA baseline. (Honest caveat: at n=5 the live raw v3−v2 gap +39pp
is ns due to v2 variance; the v3>v2 localization rests on the fixed-log S5i where it is
significant, plus the consistently v3-favoring relay/receiver metrics.) Other caveats:
single scenario, mini model, scenario-specific registry anchor. See `sim/RESULTS.md`
(numbers) and `paper/narrative.md` (story). 

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

The living paper narrative / thesis (concept-level: why the claim matters, key
distinctions like exchange-vs-retention, honest boundaries) is:

- `paper/narrative.md`  ← read for the *story*; `sim/RESULTS.md` for the *numbers*

The current direction + investigation log (read this first) is:

- `docs/project/findings_capability_axis_2026-06-15.md`

Supporting result/design notes from the 2026-06-15 investigation:

- `docs/project/society_sweep_tooling_2026-06-16.md` (multi-run society sim tooling)
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
