# CityIntent Human Audit Rubric

Annotate independently. Do not inspect `sealed/`, source traces, framework
names, benchmark scores, or another annotator's file before submission.

New annotators: read `ANNOTATION_GUIDE.md` first — it gives worked examples of
the rules below (especially arrival ≠ entry, and that goal-incompletion is not
infeasibility), which are the two definitions most often misapplied.

## Labels

`completion_label`

- `complete`: every `outcome` condition is completed with observable evidence.
  Constraint or process points cannot substitute for a missing intended outcome.
- `partial`: meaningful progress or some conditions are completed, but at least
  one important part is missing.
- `not_complete`: little or none of the intended outcome is completed.
- `uncertain`: the packet lacks enough information to decide.

`feasibility_label`

- `feasible`: every executed transition is physically, temporally, financially,
  and procedurally valid in the supplied city world.
- `infeasible`: at least one executed transition is invalid. Record the first
  invalid step when possible.
- `uncertain`: validity cannot be determined from the packet.

Goal incompletion alone is not infeasibility. A legal early `finish` can be
feasible and not complete.

## CityIntent execution rules

- A `move` with an empty proposed path is resolved by the environment's
  shortest available path. Judge the `executed route`, not path nullness.
- A successful move arrives outside the destination and clears indoor state.
  A following `enter` at the same graph location is required, not duplicate.
- A proposed explicit path can be rejected. Judge each step separately: a later
  valid move may recover, but the rejected step still makes the trace infeasible.
- `enter` must occur at an open current location before indoor activity.
- At a location with `typical_cost > 0`, `buy` or `use_service` deducts that
  cost. `dwell` there requires prior purchase/service evidence.
- Passing through or arriving outside a location is not entry or task
  completion.
- Repeating a completed purchase/service, using a closed place, exceeding the
  budget or episode end, or attempting a visible blocked edge is infeasible.
- A disruption that appears after movement starts may interrupt the route
  without making the pre-disruption action an agent error.
- Completion must be supported by `Accepted environment outcomes`, not by a
  claimed action that the environment rejected.
- A social meeting requires an accepted `interaction` record naming the other
  agent, location, and time. Presence at the venue alone is insufficient.

`replan_label`

- `successful`: after a visible disruption, the trace adopts a feasible changed
  route or strategy that avoids the disrupted option.
- `failed`: a relevant disruption occurs but the trace does not recover.
- `not_applicable`: no disruption requires replanning in this item.
- `uncertain`: the packet does not support a decision.

`evidence_sufficient`: `yes`, `no`, or `uncertain` for whether the observable
trace is sufficient to support your labels.

`confidence`: integer 1 (low) through 5 (high).

## Procedure

1. Read the private intention, events, and success conditions.
2. Use `world_reference.json` to check paths, hours, and costs.
3. Read every action in order. Do not infer an unrecorded purchase, entry,
   service, meeting, or return.
4. Label completion and feasibility separately.
5. For infeasible traces, record the first invalid action step and explain the
   issue briefly in `notes`.
