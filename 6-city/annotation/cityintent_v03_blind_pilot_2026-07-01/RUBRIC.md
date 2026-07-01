# CityIntent Human Audit Rubric

Annotate independently. Do not inspect `sealed/`, source traces, framework
names, benchmark scores, or another annotator's file before submission.

## Labels

`completion_label`

- `complete`: all important parts of the private intention and weighted success
  conditions are completed with observable evidence.
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
