# CityAgency Worklog - 2026-06-27

## Scope

This worklog archives the CityAgency discussion and repository changes completed on
2026-06-27. It records the evaluation decision, literature-note completion, reference
comparison, validation status, and next research steps.

## Research Decisions

### Completion Must Be Proven By World State

An agent's statement that a task is complete is not completion evidence. CityAgency
should translate each scenario goal into deterministic predicates over the event log and
authoritative world state, such as:

- a purchase event occurred while the agent was at an open POI;
- money decreased by the correct amount and the item entered inventory;
- two agents were co-present for the required interval before a meeting counted;
- the agent reached the required destination before the deadline;
- every movement followed valid edges and consumed sufficient time.

This motivates a proof-carrying-trace design: the rollout must contain enough state-changing
evidence for a verifier to establish completion. LLM or human judges evaluate soft qualities
such as believability, but do not determine hard completion.

### Goal Completion Is Not Plan Adherence

CityAgency should primarily evaluate whether the agent achieves its underlying goal, not
whether it mechanically follows its initial plan. Replanning is evidence of agency when it
responds to a real change and preserves the original intention. The benchmark therefore keeps
separate measures for goal completion, plan deviation, replanning validity, and unjustified
abandonment.

### The Defensible Gap Is A Combined Proof Obligation

The project should not claim the first city-agent benchmark, first mobility-realism benchmark,
or first feasibility benchmark. Existing work separately evaluates urban capability, social
goal pursuit, empirical mobility realism, and executable final state. CityAgency targets the
missing combined question:

> Can an agent turn a plausible private plan into a continuous, environment-valid urban trace
> whose completion is supported by state-changing evidence?

For urban research, this is a micro-validity check before synthetic agents are used to support
claims about transport, activities, accessibility, disaster response, or policy behavior.

## Literature Archive And Notes

The local archive was audited and refreshed with the standard PDF-to-fulltext tool using the
bundled Codex PDF runtime.

| Artifact | Count | Status |
|---|---:|---|
| PDF papers | 34 | present; all have valid PDF signatures |
| Fulltext Markdown | 34 | complete; conversion failures: 0 |
| Per-paper notes | 34 | complete; missing/orphan notes: 0 |
| Note-local PDF/fulltext references | 68 | all resolve |

At the start of the session, 22 papers had notes. Twelve first-pass notes were added:

- four social and human-behavior references;
- two mobility-realism references;
- six agent-execution and feasibility references.

The note generator now indexes all 34 papers and is additive by default. It creates missing
notes and refreshes the index without overwriting manually edited notes. A deliberate full
regeneration requires `--force`.

Primary indexes:

- `assets/papers/metadata/fulltext_summary.md`
- `assets/papers/notes/INDEX.md`
- `assets/papers/notes/NOTE_PIPELINE.md`

The current notes are first-pass research notes, not substitutes for close reading. The 17
`must-cite` papers should be promoted to `reviewed` or `deep_read` before final related-work
claims and numerical citations are written.

## Reference Benchmark Comparison

Two comparison documents were created:

- `docs/project/cityagency-reference-benchmark-comparison-2026-06-27.md`
- `docs/project/cityagency-reference-benchmark-comparison-2026-06-27.zh-CN.md`

They compare 19 central references across four groups:

1. urban mobility realism and city simulation;
2. urban LLM and embodied-city benchmarks;
3. social and human-behavior agent benchmarks;
4. agent execution, feasibility, and state validation.

The comparison records, for each reference:

- benchmark objective;
- tested agent architecture or system;
- tested foundation models;
- human baseline or evaluator;
- test method;
- metrics;
- main reported conclusion;
- significance for urban research;
- boundary relative to CityAgency.

The architecture/model audit exposes an important design requirement for our main experiment.
Many urban and social benchmarks primarily compare foundation models under one agent wrapper.
CityAgency should run two controlled axes:

1. hold the architecture fixed and compare foundation models;
2. hold the foundation model fixed and compare agent architectures.

The Chinese comparison ends with a CityAgency (ours) row under the same framework. It records
the current Utility Planner, Direct Actor, Plan-then-Act, and Reactive Replanner baselines; the
scenario method; proposed metrics; preliminary findings; and the intended urban-research value.

## Archive Checks

The two explicitly requested papers are present at all three levels:

| Paper | PDF | Fulltext | Note |
|---|---|---|---|
| CityBench | yes | yes | yes |
| AgentSociety | yes | yes | yes |

The English reference comparison has 38 local paper links, all valid. The Chinese comparison
has 19 note links, all valid. Markdown diff checks report no whitespace errors.

## Current Experimental Signal

The existing 12-scenario, four-architecture experiment remains preliminary but supports the
paper's core diagnostic direction:

| Agent | Goal completion | Trace feasibility | Trace believability |
|---|---:|---:|---:|
| API LLM Direct Actor | 0.832 | 0.873 | 0.500 |
| API LLM Plan-then-Act | 0.918 | 0.906 | 0.784 |
| API LLM Reactive Replanner | 0.913 | 0.822 | 0.718 |
| Utility Planner | 0.850 | 0.750 | 0.508 |

Plan-then-Act is strongest in this small setup. Direct Actor shows the clearest gap between
apparently successful outcomes and believable full traces. These results are not yet sufficient
for the final paper claim because model coverage, architecture coverage, human baselines, and
empirical urban data remain limited.

## Tooling Notes

- `0-Tools/research-standard/convert_pdfs_to_fulltext.py` remains the canonical PDF conversion
  tool.
- The system Python lacks `pdfplumber` and `pypdf`; the bundled Codex workspace Python was used
  successfully.
- The project-level compliance checker separately reports missing research-standard guide files:
  `docs/guides/todolist.md`, a roadmap/project file, a project map/project file, and
  `docs/project/decisions.md`. This did not affect the paper archive but remains cleanup work.

## Next Steps

1. Deep-read the 17 `must-cite` references and replace first-pass claims with page-backed notes.
2. Convert each CityAgency scenario goal into explicit verifier predicates and evidence requirements.
3. Add `false_completion_claim` and evidence coverage to the deterministic evaluator.
4. Run the two controlled experiment axes: fixed architecture across models and fixed model across
   architectures.
5. Add a small human trajectory or human decision baseline before making human-likeness claims.
6. Use the completed comparison to revise the proposal's related-work and contribution sections.

