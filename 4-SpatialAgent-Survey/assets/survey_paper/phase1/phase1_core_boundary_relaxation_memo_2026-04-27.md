# Phase 1 Core Boundary Relaxation Memo

Date: 2026-04-27

Purpose: assess whether the current `Core` boundary is too strict for the project's new target of roughly `30` paper-level Core items with somewhat richer `L1/L2/L4` coverage.

## Bottom line

Yes. If the target is a stable `Core` corpus closer to `30` paper-level items, the current boundary is too strict.

However, the problem is **not** mainly that the `L1-L5` taxonomy is wrong.

The main problem is that the present `Core` admission rule is so conservative that many spatial-social bridge systems were pushed into `Adjacent`, especially:

- social VR / role-play systems
- metaverse or avatar interaction systems
- digital community / online social-platform simulations
- embodied cooperation systems
- general social-world platforms with rich spatial interfaces but weaker paper-level social-system evidence

So the recommended move is:

1. keep the basic `L1-L5` idea as a coding taxonomy
2. relax the `Core` boundary
3. revise `L4` slightly so it is not limited almost entirely to classic Space Syntax metric names

## Why the current boundary now looks too strict

Current stable status:

- `17` paper-level `Core` items
- `19` system/configuration rows

Current representation mix:

- `L1 = 1`
- `L2 = 0`
- `L3 = 15`
- `L4 = 0`
- `L5 = 3`

This creates two different problems:

### A. Corpus-size problem

`17` paper-level items is workable for a conservative scoping review, but it is still small if the manuscript wants:

- stable distributional claims
- non-trivial comparison across multiple representation slices
- a richer evidence map than "mostly L3 plus a few L5"

### B. Boundary-shape problem

Several papers already screened as `Adjacent` are spatially strong enough to matter, but they were excluded because the old rule required too tight a combination of:

- explicit LLM multi-agent social simulation
- nontrivial spatial environment
- social/group behavior as the primary reported evidence object

That rule is coherent for a strict nucleus, but too narrow for a `Core ≈ 30` target.

## What should stay strict

### 1. Do not inflate `L1` just for symmetry

`L1` is naturally a weak spatial condition.

If we deliberately try to make `L1` large, we will admit systems where space barely matters.

So a sparse `L1` slice is not itself a defect.

### 2. Do not collapse `L1-L5` into one broad `L3`

The current taxonomy still does important work:

- it prevents backend richness from being mistaken for agent-facing spatial structure
- it keeps `L5` from being overclaimed
- it preserves the distinction between local relational structure and global structural summaries

So the right move is not to abandon the taxonomy, but to stop forcing the strict `Core` boundary to carry the whole burden.

## What should be relaxed

### Relaxation A. Widen the social-behavior gate

Old strict idea:

- retain only papers where multi-agent social simulation is already the central evidence object

Recommended wider idea:

- retain papers where a socially populated spatial environment is central and the paper studies either:
  - multi-agent social simulation
  - situated human-agent or avatar-agent interaction in a socially meaningful spatial scene
  - virtual-community or online-community collective behavior
  - embodied cooperation or conflict in an explicit spatial world

This would pull in `L2`-heavy bridge cases that are currently stuck in `Adjacent`.

### Relaxation B. Widen the environment-family gate

Old strict idea:

- prefer towns, cities, buildings, transport networks, crowd spaces, and embodied worlds

Recommended wider idea:

- also count:
  - social VR scenes
  - metaverse interaction spaces
  - online communities with explicit structured interaction environments
  - avatar-populated virtual worlds

This is the cleanest way to increase corpus size without pretending the old strict boundary was already broad enough.

### Relaxation C. Widen the interaction-structure gate

Old strict idea:

- single-agent or single-user systems usually stay `Adjacent`

Recommended wider idea:

- allow admission when the system is not a full society simulator, but the spatial scene is socially populated and the study object is still socially situated interaction rather than pure navigation or pure task completion

This would allow some role-play, NPC, onboarding, and training systems to become bridge-core evidence rather than stay outside.

## What should change in `L4`

The current `L4` rule is probably too narrow because it is tied almost entirely to classic configurational metric names like:

- `integration`
- `depth`
- `control`
- `choice`

Recommended revised `L4` definition:

- agent receives **global abstract spatial structure** that is richer than local adjacency but still less than full geometry
- examples:
  - global topology summaries
  - graph-centrality or accessibility summaries
  - whole-layout structural descriptors
  - route-structure or connectivity summaries that reflect the overall configuration rather than only local next-step options

Under this revision:

- `L3` remains local relational structure
- `L4` becomes global abstract structure
- `L5` remains direct geometry, coordinates, visual field, or physical constraints

This is a better middle layer than the current almost-empty metric-name rule.

## Immediate promotion pool if the boundary is widened

The following papers become reasonable candidates for an expanded `Core` or `Bridge Core` layer:

- `HC01` TravelAgent
- `HC11` VR role-play spatial interactions
- `BK02` When LLMs Recognize Your Space
- `BK03` Context-Aware Onboarding Agent for Metaverse
- `BK04` Voice-Controlled Dialogue System for NPC Interaction
- `BK05` Forum-theatre VR training interaction
- `BK06` TongSIM
- `BK07` S^3 social-network simulation system
- `BK08` online community collective behavior
- `R3-03` Cognitive Agents in Urban Mobility
- `R3-05` CoELA

That list alone can move the paper-level count from roughly `17` to roughly `28`.

With a few more narrow additions such as:

- `INDOORWORLD`
- `BOOKWORLD`
- one or two social-VR / metaverse bridge cases

the corpus can plausibly move into the `30+` range.

## Expected representation effect of widening

### `L2`

This is the main beneficiary.

Likely gain:

- `HC11`
- `BK02`
- `BK03`
- `BK04`
- `BK05`

So `L2` can become a meaningful bridge slice rather than remain zero.

### `L4`

This will improve only if the `L4` rule itself is revised.

Boundary widening alone is not enough.

### `L1`

This may remain small, and that is acceptable.

Trying to force many `L1` papers into Core would mostly weaken the survey.

## Recommended structural solution

Do **not** keep a single undifferentiated `Core` if the boundary is widened.

Instead use a two-layer structure:

- `Anchor Core`
  - the current strict multi-agent spatial-social nucleus
- `Bridge Core`
  - socially situated spatial systems that are weaker on population-level social simulation, but still relevant enough to belong inside the main evidence map under the widened scope

This allows:

- corpus size closer to `30`
- richer `L2`
- potentially richer `L4` after taxonomy revision
- cleaner claim discipline than simply mixing all promoted items into one flat bag

## Recommendation

If the project really wants `Core ≈ 30`, then the answer is:

- **yes, the current boundary is too strict**
- **no, the right response is not blind broad search**
- **the right response is a documented scope widening plus a modest `L4` taxonomy revision**

## Next operational step

1. revise the corpus boundary from strict `Core` to `Anchor Core + Bridge Core`
2. revise `L4` from metric-name-specific configurational input to global abstract structural input
3. re-adjudicate current `Adjacent` and reserve cases under the widened rule before doing more search
4. only then run another narrow search to top up any still-thin slices
