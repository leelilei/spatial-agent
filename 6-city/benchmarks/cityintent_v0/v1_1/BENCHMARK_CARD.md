# CityIntent v1.1 benchmark card

Status: candidate under construction; not leaderboard-ready.

CityIntent evaluates whether an urban agent can turn a private intention into
an executable, evidence-backed outcome under spatial, temporal, resource,
social, and information constraints. The unit of evaluation is a typed action
trace executed against a graph city and a deterministic verifier.

## Intended use

- Compare agent policies, scaffolds, and model backbones under one action and
  observation protocol.
- Diagnose failures in replanning, evidence production, constraint handling,
  memory-conditioned choice, and social coordination.
- Support controlled research; it is not a deployment safety certification.

## Data and splits

The target release contains five topology-distinct worlds and 144 accepted
items: examples (24), development (36), public test (36), and private test
(48). The current generated items remain candidates until all acceptance gates
pass. Private assets are organizer-only and are excluded from public packages.

## Evaluation

The official ranking metric is macro verified task completion, averaged first
within construct-world cells and then across cells. Constraint satisfaction,
trace feasibility, intention consistency, social appropriateness, efficiency,
and cost are reported alongside it. Model-judge scores are secondary only.
Submissions contain actions and telemetry, never accepted self-reported scores.

## Known limitations

- Worlds are synthetic graph environments, not calibrated replicas of real
  cities.
- The construct taxonomy is intentionally multidimensional.
- The candidate pool inherits templates from v1.0-rc1 and currently contains
  substantial baseline ceiling and floor effects.
- Social behavior is represented through a constrained interaction protocol
  and does not capture the full ambiguity of human social life.
- Difficulty labels are provisional until empirical calibration.

## Governance

Score-changing changes require a new semantic version and complete rescoring.
Public and private manifests are hashed. Private identifiers, seeds, scenarios,
oracle keys, and scoring keys must not appear in the public archive. See
`release_spec.json` for the full freeze gate.
