# Phase 1 Core Gap Audit

Date: 2026-04-22

Purpose: determine whether the current `Core 15` requires another broad search round, or whether the better next step is to code the current set and only reopen search if a real structural gap appears.

## Bottom line

Do **not** start another broad expansion round now.

The current `Core 15` is already large enough to support the next stage of analysis. The main bottlenecks are now:

- evidence completeness for a small number of papers
- representation-level coding for several system papers
- checking whether the current set leaves any truly empty conceptual cells after coding

## What the current Core set already covers

### 1. Environment-family coverage is already reasonably broad

The current set is not concentrated in only one narrow genre.

- Built environment, urban replica, or city-scale cases:
  `HC01`, `HC10`, `HC13`, `HC14`, `HC15`, `BK01`
- Sandbox, game-world, or virtual social-world cases:
  `HC02`, `HC04`, `HC05`, `HC06`, `HC08`, `HC09`
- Environment-architecture anchors:
  `HC03`, `HC07`, `HC12`

This means the present Core already spans:

- built/urban physical-space questions
- sandbox and virtual-world social simulation
- reusable environment frameworks and simulator architectures

That is enough variation to move into systematic coding.

### 2. Representation-level coverage is imperfect, but not empty

The current set leans heavily toward `L3`-like representations.

- Clear or likely `L3` cases dominate:
  `HC02`, `HC04`, `HC05`, `HC07`, `HC08`, `HC09`, `HC10`, `HC13`, `HC14`, `HC15`
- Clear or likely `L5` cases exist, but are fewer:
  `HC01`, `HC06`, `HC12`
- Multi-configuration or unresolved cases:
  `HC03`, `BK01`

This is a real pattern, but it is **not yet** proof that search must continue. It only means the first coding pass should verify whether the paper-level dominance of `L3` leaves too few robust `L5` or hybrid cases for your argument.

### 3. Behavioral-scale coverage is also workable

- Emergent social structure is well represented:
  `HC02`, `HC05`, `HC06`, `HC07`, `HC09`, `HC10`, `HC15`, `BK01`
- Interaction-focused cases are fewer but present:
  `HC01`, `HC08`
- Mixed or framework cases also exist:
  `HC03`, `HC04`, `HC12`, `HC13`, `HC14`

So the current problem is not that the Core is behaviorally empty. The issue is more likely one of balance and coding precision.

## The actual gaps right now

### A. Evidence-completeness gap

This is the most immediate gap, and it is smaller than a new search round.

- `HC01` is still in Core but has no local PDF yet
- `HC13` only has a placeholder HTML file
- `HC14` only has a placeholder HTML file

So the real evidence state is closer to:

- `12` Core papers with valid local PDFs
- `3` Core papers that still need acquisition or verification

This argues for finishing acquisition before reopening search.

### B. Representation-coding gap

Several Core papers are already strong enough to keep, but still need precise coding of the environment representation:

- `HC03` Concordia
- `HC06` Project Sid
- `HC10`
- `HC12` SimWorld
- `BK01` AgentSociety

This is a coding problem, not a retrieval problem.

### C. Possible built-environment configurational gap

If there is one place where a later targeted expansion could still be justified, it is here:

- explicitly built-environment or layout-sensitive cases
- where spatial configuration is not just background context
- and where the representation layer is methodologically central

Right now the best candidates in that direction are:

- `HC01` TravelAgent
- `HC10`
- `HC15`
- provisionally `HC13` and `HC14`
- partly `BK01`

That may be enough. But if later coding shows that most of these still operate at a coarse environment level rather than a true configuration-sensitive level, then **this** would be the right place for a future targeted expansion.

## What not to do

Do not reopen broad search for:

- general LLM multi-agent surveys
- online community papers
- digital social-platform behavior papers
- generic simulator platforms
- single-agent interaction or onboarding systems

Those lines have already been screened and mostly resolved.

## Recommended next step

The right next move is:

1. code the current `Core 15`
2. verify the three incomplete papers (`HC01`, `HC13`, `HC14`)
3. then check whether any conceptual cell is truly empty

Only after that should you consider a new search round.

## Decision

Current recommendation: **hold Core expansion for now**.

Reopen targeted search only if one of the following happens:

- one or more incomplete Core papers drop out after full-text verification
- the first coding pass reveals a real empty cell
- the argument needs more explicitly configurational built-environment cases than the current set can support
