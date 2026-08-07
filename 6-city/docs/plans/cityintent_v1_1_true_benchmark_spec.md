# CityIntent v1.1 — Benchmark release specification

Status: implementation target  
Supersedes: `1.0-rc1` as the next public benchmark release  
Purpose: convert the current single-world diagnostic testbed into a durable,
versioned benchmark with held-out evaluation.

## Benchmark claim

CityIntent v1.1 evaluates whether an agent can turn a private urban intention
into an executable, evidence-backed outcome under spatial, temporal, resource,
social, and information constraints. The primary score is deterministic and
outcome-based. Model-judge plausibility is a secondary diagnostic and cannot
determine the leaderboard ranking.

The release must not claim to represent all urban intelligence. It may claim
coverage of the constructs, environments, and action protocol enumerated in
this specification.

## Required scale

### Worlds

- At least 5 connected city worlds.
- Three public worlds and two evaluation-only worlds.
- Required topology archetypes: dense grid, radial transit, sparse polycentric,
  bottleneck/river crossing, and mixed-use irregular.
- Worlds must vary topology, travel times, opening hours, prices, POI density,
  and feasible substitutes—not only names.
- Evaluation-only worlds use different location identifiers and are excluded
  from the public participant package.

### Scenarios

- At least 144 accepted scenarios.
- Four disjoint splits:
  - examples: 24;
  - development: 36;
  - public test: 36;
  - private test: 48.
- At least 18 accepted items in each construct family:
  1. disruption recovery;
  2. time-window scheduling;
  3. resource and budget allocation;
  4. POI availability and service evidence;
  5. memory-conditioned preference;
  6. social coordination and co-presence;
  7. multi-party commitment management;
  8. compound long-horizon intention execution.
- Easy, medium, and hard tiers must each contain at least 25% of the accepted
  items.
- Every item records its generator version, template id, seed, world id,
  construct family, difficulty tier, and split.

## Item acceptance gate

Every generated item must pass all of the following before entering a split:

1. schema and cross-reference validation;
2. connected-world reachability;
3. deterministic oracle task completion = 1.0;
4. deterministic oracle feasibility = 1.0;
5. at least one mechanism-matched negative control with task headroom >= 0.15;
6. no answer, oracle action sequence, or private-test identifier in the public
   observation;
7. no dependency on an action unavailable to a baseline unless the item is
   explicitly tagged `action_surface_coverage` and reported separately;
8. deterministic regeneration from the archived generator version and seed.

Generation failures are retained in a rejection log; they must not be silently
discarded after observing model performance.

## Data splits and leakage policy

- Template families may cross splits, but instantiated world topology,
  parameters, identifiers, and random seeds may not.
- Public-test labels may be released after the first benchmark cycle; private
  test labels remain server-side.
- The private package contains world files, scenario files, oracle keys, and
  scoring keys. It is excluded from the public release builder.
- A split validator checks duplicate ids, duplicate normalized payload hashes,
  seed overlap, template-instance overlap, and world leakage.
- Benchmark maintainers publish hashes of private assets before accepting
  submissions.

## Evaluation protocol

### Primary leaderboard metrics

1. verified task completion;
2. constraint satisfaction;
3. trace feasibility;
4. intention consistency;
5. social appropriateness for applicable items;
6. efficiency-normalized verified completion;
7. macro-average across construct families and worlds.

The official ranking metric is the macro-average verified completion score,
first across items within each construct-world cell and then across cells. This
prevents large families or easy worlds from dominating the leaderboard.

### Secondary diagnostics

- failure taxonomy;
- replanning success;
- action and token cost;
- face plausibility;
- full-trace believability;
- face-to-trace gap;
- robustness to perturbation pairs.

Model-judge metrics are never mixed into the primary score.

### Submission contract

Each submission provides:

- one JSONL trace per requested episode;
- benchmark version and split hash;
- system/scaffold name and version;
- actor model identifier and provider;
- declared tool/action interface;
- token, call, latency, and retry telemetry;
- deterministic seeds where applicable;
- disclosure of external memory, retrieval, fine-tuning, and human input.

The evaluator rejects missing episodes, extra episodes, unknown actions,
post-deadline actions, malformed telemetry, and traces that exceed the declared
budget. It never accepts self-reported success.

## Baseline suite

The release archive must contain at least:

- two deterministic controls;
- ReAct and Plan-and-Execute paper-backed policies;
- four pinned external-framework adapters;
- four actor-model families from at least three providers;
- three repeats for stochastic systems on public test;
- one complete organizer run on the private test.

All baselines share the same observation, action, budget, termination, retry,
and scoring contract.

## Validity and reliability gate

### Human validation

- At least 72 stratified traces.
- Two independent blinded annotators.
- Completion and feasibility: exact agreement >= 0.80 and Cohen's kappa >=
  0.60.
- Evidence sufficiency >= 0.90 for each annotator.
- Every disagreement receives a documented disposition.

### Evaluator robustness

- At least two independent model judges plus the deterministic verifier.
- Spearman rank correlation >= 0.70 between model judges on secondary soft
  scores.
- Main qualitative conclusions must retain direction under each judge and
  after removing every single scenario family in turn.

### Item quality

- No unlabelled action-surface confound.
- No accepted item is at deterministic-baseline ceiling or floor across the
  full baseline suite without an explicit diagnostic role.
- Negative item-total correlations require removal, relabelling as a separate
  construct, or a pre-registered rationale.
- Reliability and discrimination are reported within construct families; a
  single unidimensional reliability coefficient is not required for this
  intentionally multidimensional benchmark.

## Reproducibility and governance

- Immutable semantic version and changelog.
- Scenario generator, seeds, schemas, validators, evaluator, and public
  baselines are released.
- A benchmark card documents intended use, exclusions, limitations, licensing,
  privacy, ethical considerations, maintenance, and deprecation.
- Public and private package manifests include SHA-256 hashes.
- Score-changing bug fixes trigger a new benchmark version and rescoring; they
  are never patched silently.
- A submission registry records evaluator version, package hash, declared
  resources, and result hash.

## Freeze rule

CityIntent v1.1 may be labelled a public benchmark only when every machine
gate in `v1_1/release_spec.json` passes, the private evaluation package exists,
the human-validation gate passes, and at least one end-to-end submission has
been scored from a clean checkout. Until then its status is
`benchmark_candidate_under_construction`.

