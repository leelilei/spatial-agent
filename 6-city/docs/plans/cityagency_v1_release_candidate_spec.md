# CityAgency v1 Release Candidate Specification

Date: 2026-07-02

Status: `1.0-rc1`; not frozen until the human-validation gate passes.

## Construct

CityAgency tests whether an urban agent converts a plausible private plan into
an executable trace whose intended outcome is supported by authoritative world
state. It does not treat fluent rationale, arrival, or self-reported completion
as outcome evidence.

## Evidence Contract

| Claim | Required accepted evidence | Insufficient proxy |
|---|---|---|
| Entered a place | `entry` at the current open location | arrival or pass-through |
| Bought an item | typed `purchase` after entry | visiting the shop |
| Used a service | typed `service` after entry, completed by deadline if present | entering or waiting |
| Picked up a child | `child_pickup` service at school by the deadline | arrival at school |
| Met another agent | accepted `interaction` naming counterpart, location, start, and end time | own presence or dwell |
| Replanned | changed feasible route/strategy after observed disruption | a new rationale with unchanged execution |

An `interaction` is accepted only when the primary agent has entered the
location and the environment exposes the counterpart there during the allowed
window. When a scenario declares coordination as an outcome, the required
message must precede the interaction.

## Condition Roles

- `outcome`: intended result. These conditions determine `task_completion`.
- `process`: diagnostic behavior such as verified replanning or optional social
  handling. These determine `process_success`.
- `constraint`: budget, deadline, avoidance, and feasibility requirements.
  These determine `constraint_satisfaction`.

The legacy `goal_completion` remains the weighted sum over all conditions.
It is not the primary answer to whether the task was completed.

## v1 Metrics

Primary metrics are `task_completion`, `trace_feasibility`, and
`replanning_success`. Supporting metrics include `constraint_satisfaction`,
`process_success`, `impossible_trace_rate`, `city_false_continue`, budget and
travel consistency, and blinded human trace judgments.

## Human-Validation Gate

1. Sample the same scenario-adapter cells without exposing framework identity,
   verifier outputs, violations, or the sealed key.
2. Two people annotate independently using outcome completion, transition
   feasibility, disruption recovery, and evidence sufficiency labels.
3. Report exact agreement and Cohen's kappa before adjudication.
4. Compare each annotator with deterministic `task_completion`, feasibility,
   and replanning labels.
5. Resolve material disagreements by changing the verifier, packet, or rubric;
   rerun affected traces and audit items.

Model-generated labels may debug the packet but cannot satisfy this gate.

## Freeze Criteria

CityAgency v1 can be frozen only when all tests and package validation pass,
verified external adapters produce archived v1 traces, both human annotation
files are complete, agreement/calibration results are archived, and every
material audit finding has a documented disposition. Until then the status
must remain `release_candidate_pending_human_audit`.
