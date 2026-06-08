# Pilot Taxonomy Validation

This memo records the minimum Phase 0 validation for the `L0-L5` taxonomy.

## Goal

Confirm that three known systems can be coded consistently on:

- `environment_side_representation`
- `agent_accessible_representation`
- `behavioral_scale`
- `evidence_status`

The pilot is not meant to prove that the taxonomy is final. It is meant to show that the
taxonomy is operational enough to enter Phase 1 without relying on ad hoc judgments.

## Pilot Systems

### 1. Generative Agents

- `environment_side_representation`: `text-only`
- `agent_accessible_representation`: `L2`
- `behavioral_scale`: `interaction`
- `evidence_status`: `designed_affordance_only`

Reasoning:

- The environment is implemented as named places and textual observations rather than an explicit geometric or graph input to the agent.
- Agents receive semantically rich place descriptions and daily-schedule context, but not structural metrics or full topology.
- The paper demonstrates believable social interaction, but it does not isolate space as a tested causal factor.

Phase 0 lesson:

- `semantic scene description` should not be over-coded as `L3`.
- Social behavior can be substantial even when the spatial representation stays below structural adjacency.

### 2. Project Sid

- `environment_side_representation`: `text-only`
- `agent_accessible_representation`: `L1`
- `behavioral_scale`: `emergent_social_structure`
- `evidence_status`: `observed_effect`

Reasoning:

- The simulated world is rich, but the agent-facing representation in the paper is place- and event-centric rather than structurally explicit.
- The paper reports role differentiation, rule formation, and cultural transmission, so macro social effects are observed rather than merely hypothesized.
- Because agent input is not reported as explicit topology or configuration metrics, the system should not be promoted to `L3-L5`.

Phase 0 lesson:

- Large 3D or sandbox worlds do not imply high `agent_accessible_representation`.
- The taxonomy must code what agents receive, not what the engine renders.

### 3. SARAH

- `environment_side_representation`: `3D_engine`
- `agent_accessible_representation`: `L3`
- `behavioral_scale`: `local_action`
- `evidence_status`: `observed_effect`

Reasoning:

- The backend world is explicitly 3D and tracks user trajectory.
- The model conditions on user-relative spatial information and dyadic audio, but the paper does not show that the agent receives a full geometry/state description equivalent to `L5`.
- Spatial awareness is tested directly through motion quality and responsiveness, so the effect is observed.

Phase 0 lesson:

- A 3D engine plus trajectory input is still not automatically `L5`.
- `L5` should be reserved for systems where the agent itself operates on full geometry, coordinates, view constraints, or equivalent continuous physical state.

## Comparison With Oh et al. (2025)

Oh et al. define *spatial awareness levels* as experimental interaction conditions that vary how much the LLM reflects the user's space during conversation.

Our `L0-L5` taxonomy is different:

- Oh et al. describe an intervention strength in a user study.
- `L0-L5` describes the structural explicitness of the agent-accessible spatial information.
- Oh et al. is about whether the agent acknowledges and uses spatial context.
- `L0-L5` is about what kind of spatial representation is actually available to the agent.

Bridge:

- Oh et al. helps justify why spatial awareness matters for social outcomes.
- `L0-L5` helps compare heterogeneous systems on a common representational axis.

## Phase 0 Conclusion

The pilot supports three practical rules:

1. Code the agent-facing representation, not the rendering backend.
2. Separate `semantic spatial description` from `adjacency / co-presence` and from `full geometry`.
3. Keep `evidence_status` tied to what was actually tested, not what the system appears capable of.

Result:

- The taxonomy is usable enough to proceed into Phase 1.
- Borderline cases should be documented in later `adjudication_memo.md`, not silently forced upward.
