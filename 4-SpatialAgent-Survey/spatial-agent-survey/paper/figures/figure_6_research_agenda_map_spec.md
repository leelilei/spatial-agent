# Figure 6. Research Agenda as an Evidence Ladder

Draft status: agenda figure spec for Section 7.

## Purpose

Organize future work around the gap identified by the evidence map. The figure should help Sections 6 and 7 move from the current diagnosis to evidence requirements without overstating current results.

## Current Diagnosis Block

- `L3` concentrated: `18 / 34` rows.
- `L4` sparse: `1 / 34` rows and bridge-only.
- evidence status: `15` designed affordance only / `19` observed effect.
- backend richness does not determine agent input.

## Agenda Stages

| axis | question | evidence requirement |
|---|---|---|
| Representation | What spatial structure is exposed to agents? | Explicit `L2`, `L3`, `L4`, or `L5` interface specification. |
| Mechanism | Does the spatial input change decisions, movement, or interaction? | Controlled ablations or matched layouts; compare `L1/L2` vs `L3`, `L3` vs `L4`, and `L3/L4` vs `L5` where appropriate. |
| Emergence | Do individual effects scale to group-level patterns? | Multi-agent measures such as movement, co-presence, encounter, clustering, route concentration, or role formation. |
| Generalization | Do effects hold across layouts, tasks, populations, models, and seeds? | Matched layout families and cross-condition replication. |
| Applications | Where is spatially grounded social simulation useful? | Application claims tied to representation level, behavioral scale, and evidence status. |

## Evidence Ladder Overlay

- `spatial affordance`
- `spatial sensitivity`
- `spatial mediation`
- `replicated mechanism`

## Caption

Figure 6. Research agenda as an evidence ladder derived from the evidence map. The current diagnosis is a spatially active but representation-limited literature: `L3` is dense, `L4` is sparse and bridge-only, and observed effects are heterogeneous. Future work should move from explicit representation contracts to mechanism tests, emergent social measures, generalization checks, and application-specific validation. Each step should preserve the survey's claim discipline: future-work directions are not current evidence unless the system exposes the relevant spatial structure and reports observed spatial-behavior associations.

## Claim Boundary

The figure supports `agenda` claims. It should not be used as evidence that richer spatial representation already improves LLM-agent social simulation. It should show what would be required to move from spatial affordance toward sensitivity, mediation, and replicated mechanism.
