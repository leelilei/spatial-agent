# Phase 1 Representation Adjudication Memo

Date: 2026-04-23

Purpose: close the remaining representation-level ambiguities in the `Core 15` seed table before first-pass coding.

## Final decisions

- `HC03` Concordia: keep in `Core`, but do not force one flat `L` level at paper level; split by configuration before final coding
- `HC06` Project Sid: adjudicate to `3D_engine / L5`
- `HC10` Real world community oriented HD social simulation: adjudicate to `3D_engine / L3`
- `HC12` SimWorld: keep in `Core`, but split by interface before final coding; `L5` is present in at least one interface
- `BK01` AgentSociety: adjudicate conservatively to `graph_based / L3`

## Taxonomy effect

No taxonomy change is required.

The existing manual already supports these outcomes:

- treat `agent-accessible representation` separately from backend environment richness
- avoid promoting a system to `L5` only because the backend is 3D
- split when interface differences are real and behavior-relevant

## Case notes

### HC03 Concordia

Field in dispute:

- whether Concordia can be coded as one paper-level `L` value

Evidence used:

- the framework explicitly spans `physical`, `social`, and `digital` environments
- the `Game Master` mediates environment updates and player-specific observations
- appendix material describes GM components with player-facing state exposure such as location labels, for example a location component exposing where a player is

Decision:

- keep `environment_side_representation = mixed_pending_split`
- set `agent_accessible_representation = mixed_L3_to_L5_split_required`
- do not first-pass code this as one flat row

Reason:

Concordia is a framework family rather than one stable environment-interface pairing. The extracted evidence is enough to show that paper-level flattening would collapse materially different representations into one label.

### HC06 Project Sid

Field in dispute:

- whether the agent-facing representation is truly `L5` or only a richer backend with text summaries

Evidence used:

- the paper's appendix/config pages include coordinate-bearing location memories for villages, such as settlements located around specific `x, y, z` positions
- configuration examples include `spawn_location` with explicit coordinates
- the main architecture figure also distinguishes environment detail as an agent input stream rather than a purely human-viewing backend

Decision:

- keep `environment_side_representation = 3D_engine`
- set `agent_accessible_representation = L5`

Reason:

This is direct agent-facing coordinate information. That crosses the manual's threshold for `L5`, even if the paper is not primarily about spatial causality.

### HC10 Real world community oriented HD social simulation

Field in dispute:

- whether the GIS/BIM/Unreal stack should push the system to `L5`

Evidence used:

- the method section lists ten observations split into environment-based and agent-based observations
- the exposed fields are time and categorical agent state, including current action, last action, location, last location, phone usage, and age
- available actions are bounded by location classes such as home, workplace, school, supermarket, and public area

Decision:

- keep `environment_side_representation = 3D_engine`
- set `agent_accessible_representation = L3`

Reason:

The backend community model is visually and physically rich, but the agent-facing state remains categorical and local rather than geometric. This is exactly the type of backend-versus-interface gap that the coding manual warns against.

### HC12 SimWorld

Field in dispute:

- whether SimWorld should be given one flat `L5` label at paper level

Evidence used:

- the simulator exposes a gym-like agent interface
- the observation stack shown in the system overview includes visual observations, scene graphs, GPS, and history
- the agent section describes a diverse observation space plus an action planner bridging low-level control and high-level reasoning
- UnrealCV+ supports data querying and fine-grained environment control

Decision:

- keep `environment_side_representation = 3D_engine`
- set `agent_accessible_representation = L5_present_but_split_required`
- require interface-level splitting before final coding

Reason:

SimWorld clearly contains `L5` interfaces, but not every supported observation mode is identical. A single paper-level row would hide meaningful variation between visual, structured, and abstract observation channels.

### BK01 AgentSociety

Field in dispute:

- whether there is enough evidence to move from `unknown` to a stable conservative representation label

Evidence used:

- the mobility module uses explicit place selection and distance-sensitive movement logic
- stream memory nodes are described with `time`, `location`, and `event description`
- the societal environment uses urban road networks, AOI/POI structures, and realistic positional feedback
- interview responses are generated from internal state plus surrounding environmental context

Decision:

- keep `environment_side_representation = graph_based`
- set `agent_accessible_representation = L3`

Reason:

There is now enough method evidence to say that agents receive explicit location-bearing state. However, the currently extracted evidence still does not show direct coordinate or geometry feeds at the agent interface, so `L5` would be too strong.

## Operational consequence

After this memo, the former five-paper representation queue separates into:

- `3` rows ready for conservative first-pass coding: `HC06`, `HC10`, `BK01`
- `2` rows that should be split before final coding: `HC03`, `HC12`

This means the `Core 15` now operationally looks like:

- `10` rows ready for first-pass coding
- `2` rows split-required
- `3` rows acquisition-blocked at memo time

## 2026-04-27 addendum

Later full-text work changed that operational state:

- `HC01` was archived and adjudicated as Adjacent/boundary evidence rather than stable Core social-behavior evidence
- `HC13` and `HC14` were archived as valid PDFs and adjudicated conservatively as stable Core items

So the live state after the 2026-04-27 updates is:

- `16` Core system/configuration rows are now materialized in the first-pass table
- `HC13` and `HC14` are no longer waiting for row materialization
- no remaining Core PDF-acquisition blocker

## 2026-04-27 Round 3 integration addendum

Targeted Round 3 work subsequently added three more stable Core rows:

- `R3-01` MineLand
- `R3-02` GATSim
- `R3-04` LLM-driven epidemic-economic dynamics

So the live state after Round 3 integration is:

- `19` Core system/configuration rows are now materialized in the first-pass table
- the former `L5 + observed_effect` gap is now closed
- no further broad or narrow expansion is currently required before synthesis
