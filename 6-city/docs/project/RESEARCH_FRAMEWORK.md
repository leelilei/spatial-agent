# CityAgency (6-city) — Research Framework

> Canonical one-page synthesis of what this project is, what exists, and the goal.
> Created 2026-07-04. Update when the direction, construct, or gate status changes.
> Companion docs: `direction_verdict_2026-07-04.md` (why the direction holds),
> `../plans/cityagency_v1_release_candidate_spec.md` (the frozen construct + gate).

## 0. One-line

**Plausible Plans, Impossible Traces** — a benchmark measuring whether an urban
agent can turn a *plausible-sounding private plan* into an *environment-verifiable
execution trace*. Main line = **urban benchmark** (unchanged).

## 1. The problem / the open cell

LLM city agents narrate fluent plans (plausible) but do not necessarily realize
them in the city world (verified). CityAgency measures the two **separately**.

Neighbors each own one axis; none owns the exact cell (first-hand check 2026-07-04):

| Others do | What's missing |
|---|---|
| Urban knowledge / spatiotemporal reasoning / planning-judgment benchmarks (CityBench, USTBench, UrbanPlanBench) | No individual resident actually *executing* a private intention |
| Population-scale aggregate simulation (GenWorld, AgentSociety, OpenCity) | Trades individual agency for scale; no per-agent outcome verification |
| Single-request route/travel planning (MobilityBench, Trip+) | Not a full multi-step private-goal episode; Trip+ scores with an LLM-judge |
| Spatio-temporal tool-use disruption (STT-Arena) | Tool calls, no city movement / social layer / resident goals |

**Our cell (open):** city resident + private intentions + movement/feasibility +
**environment-owned outcome evidence** + graded replanning + social co-presence.

## 2. The construct (what makes it distinctive)

**Evidence Contract** — refuse fluent rationale, arrival, self-report, or
LLM-judge as outcome evidence; accept only environment-confirmed state change.

| Claim | Required accepted evidence | Rejected proxy |
|---|---|---|
| Entered a place | `entry` at an open location | arrival / pass-through |
| Bought an item | typed `purchase` after entry | visiting the shop |
| Used a service | typed `service` after entry, by deadline | entering / waiting |
| Met another agent | accepted `interaction` naming counterpart, place, time window | own presence / dwell |
| Replanned | changed *feasible* route/strategy after observed disruption | new rationale, unchanged execution |

Conditions split into three roles → three primary metrics:
- `outcome` → **task_completion** (did it actually get done)
- `constraint` → constraint_satisfaction (budget / deadline / avoidance)
- `process` → replanning_success / process_success

Legacy weighted `goal_completion` is kept only as a **contrast**, not the answer.
The **divergence** between task_completion and goal_completion is the finding.

## 3. What has been built

**Runnable benchmark (v0 → v0.2 → v0.3 → v1-rc1)**
- toy city + scenarios + validator; typed executor + evidence-contract verifier
- 4 official framework adapters (external_frameworks 4-way / 4×4×3 / 4×4×1)
- pressure/disruption scenarios; repeated-reliability harness
- archive standard per run (run_config / runs / manifest / summaries / traces)

**The real finding (the benchmark's ammunition)**
- rc1: `task_completion` **systematically diverges** from legacy goal — SOTOPIA
  agents message throughout but **no framework produces an environment-accepted
  meeting interaction**. This is the plausible↔verified gap, measured.
- The 72-trace social-outcome family turns that anecdote into a repeated effect:
  GATSim completes 15/21 required co-presence outcomes, AgentSociety 4/21,
  Generative Agents 2/21, and the SOTOPIA-style `LLMAgent` adapter 0/21 despite
  61.1% fully feasible traces.

**Validation pipeline**
- blinded audit packet + RUBRIC + sealed key; 16 items awaiting human annotation
  (`annotation/cityintent_v1_rc1_blind_validation_2026-07-02/`)

**Literature base**
- archive (incl. 2026-07-04 neighbors STT-Arena / Trip+ / GenWorld), reference
  index, per-paper notes, direction verdict

**Discipline**
- RESULTS.md ledger (synced, 16 rows); "log every run" rule now covers 6-city

## 4. The goal

**Claim A (the big claim):** across multiple *official* agent frameworks there is
a **measurable, reproducible gap** — models produce plausible plans yet
systematically fail environment-verified outcomes — plus a failure taxonomy.

**Deliverable:** a **frozen v1 benchmark + paper**, framed leading with the
*evidence-contract construct* and the *gap finding*, NOT "the first urban benchmark".

## 5. Status & the one hard gate

| Stage | Status |
|---|---|
| Direction confirmed (cell open, benchmark viable) | ✅ |
| Evidence contract + runnable pipeline + first finding | ✅ |
| **Human-validation gate (verifier ≈ human judgment) → freeze v1** | ⏳ **current blocker** |
| Related-work tight positioning vs new neighbors | ⬜ |
| Scale up / more frameworks / write paper | ⬜ |

**Why the gate matters:** without human audit the gap finding has no arbiter — a
skeptic reduces it to "your verifier is just defined too strictly." The audit
anchors task_completion to human judgment (construct validity). Cost is small
(16 items × 2 annotators); model labels cannot satisfy the gate (circular).

**Immediate next action:** complete blinded `annotator_a` + a second annotator,
then compute agreement / Cohen's kappa vs the deterministic verifier → freeze v1.
