# Figure 3. Agent-Accessible Spatial Representation Taxonomy

Draft status: figure spec aligned to the 2026-05-01 closure baseline.

## Purpose

Explain the `L0-L5` taxonomy as an agent-facing coding rule. The figure should make the backend/interface distinction visually obvious: environment-side richness does not determine the coded level unless the information is available to the agent.

## Taxonomy Levels

| level | short label | coding rule | stable widened-Core rows |
|---|---|---|---:|
| `L0` | none | no spatial information | 0 |
| `L1` | labels | place or action-space labels without explicit relations | 1 |
| `L2` | semantic scene | semantic or descriptive place information without explicit topology | 8 |
| `L3` | local relations | adjacency, co-presence, nearby agents, local movement options, feeds, or local graph exposure | 18 |
| `L4` | global abstract structure | agent-facing global structure beyond local next-step relations, including configurational or network position information | 1 |
| `L5` | geometry / embodiment | coordinates, visual field, embodiment, physical constraints, or geometry-bearing input consumed by the agent | 6 |

## Required Visual Message

The figure should not read as a simple maturity ladder. It should show increasing structural explicitness in the agent input while preserving two cautions:

- `3D_engine` or GIS backend does not automatically imply `L5`.
- Researcher-side network analysis does not imply `L4` unless it is agent-facing.
- The single `L4` row is a digital-network bridge case, not strict anchor evidence for physical-layout Space Syntax mediation.
- `L5` rows are heterogeneous and should not be treated as one social-simulation validation category.

## Caption

Figure 3. Agent-accessible spatial representation taxonomy used in the evidence map. Levels code what the agent can consume, not what the environment stores or what the analyst computes after the simulation. The stable widened Core is concentrated at `L3`, while `L4` appears only once and only in a widened digital-network bridge case. `L5` indicates geometry-bearing or embodied input, not automatic configurational mediation. This supports the interpretation of configurational or globally abstract agent-facing structure as an underexplored design space rather than a validated field-wide layer.

## Rendering Notes

- Use a left-to-right sequence from `L0` to `L5`.
- Add a separate backend strip below the sequence showing examples such as `text-only`, `2D_grid`, `graph_based`, and `3D_engine`.
- Draw a visual warning that backend richness only counts when exposed at the agent interface.
- Include row counts on each level, but keep them visually secondary to the definitions.
