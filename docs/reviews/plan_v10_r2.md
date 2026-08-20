# Review of `plan_v10.md` - R2

**Target**: `docs/plans/plan_v10.md`  
**Review focus**: research-plan executability, preregistration clarity, condition validity, and alignment with current project assets  
**Date**: 2026-05-02  
**Recommendation**: Major Revision before implementation  
**Summary score**: 6/10 as a plan, 7/10 as a conceptual direction

---

## Overall Assessment

`plan_v10.md` has a substantially better research direction than earlier drafts. Its strongest move is to stop arguing that Space Syntax itself is "true" in LLM-agent societies, and instead frame the paper around a narrower empirical claim:

> computable spatial configuration can be converted into agent-facing input, and this input may systematically alter multi-agent social behavior.

This is a defensible and useful research gap. The condition matrix also moves the project beyond a weak "with space vs without space" comparison by separating topology-only input, implicit spatial affordance, non-spatial structured descriptions, explicit configurational descriptions, movement, and action sampling.

However, v10 is not yet a fully usable research plan. It is currently closer to a strong conceptual protocol plus an experimental wish list. The biggest problem is not the theory; it is that the key claims, experimental endpoints, condition implementations, and current code/config assets are not yet tied together tightly enough for execution or preregistration.

---

## Major Concerns

### 1. The plan is not yet executable from the current code/config state

`plan_v10.md` defines a full experimental pipeline:

- Stage 0 preflight
- Stage 1 micro-task
- Stage 2 long-run simulation
- Stage 3 mechanism and robustness
- Stage 4 human evaluation

It also states that the minimum publishable version must include all of these except some extensions.

Problem: the current implementation layer does not yet reflect this plan. The existing `spatial-agent-core/configs/experiments/exp1_spatial_vs_baseline.yaml` is still only a placeholder:

```yaml
# Exp1: 空间感知 vs 无空间感知对比
experiment:
  name: "exp1_spatial_vs_baseline"
  description: "对比 SpatialAgent 和 BaseAgent 的行为可信度"
  # TODO: 补充实验参数
```

This means the main v10 condition matrix is not yet mapped to runnable config fields, scripts, output schemas, or analysis commands.

**Why this matters**: a research plan should allow a collaborator to know exactly what to run, what files are needed, what outputs are produced, and what analysis consumes those outputs. v10 currently describes the desired experiment, but not yet the operational bridge.

**Required fix**: add an "Implementation Binding" section:

- condition name -> config key
- map name -> layout file
- run definition -> script command
- output file schema -> required fields
- metric name -> analysis function or planned script
- stage gate -> exact pass/fail criterion

Without this, v10 should not be treated as implementation-ready.

---

### 2. The primary endpoint `TAR_H1_run` is underdefined

v10 names the main endpoint as:

```text
TAR_H1_run
```

and identifies the main comparison as:

```text
C4 vs C1
```

This is directionally good, but not yet reproducible. The plan defines:

```text
BSR = 行为是否随空间变量发生系统性差异
TAR = 行为变化是否沿着预注册理论方向发生
```

This is a principle, not an operational metric.

The plan still needs to specify:

- What exactly is H1?
- Which events count as H1-relevant behavior?
- Is H1 about encounter rate, public conversation, private disclosure, information spread, or role behavior?
- Is `TAR_H1_run` computed by rule-based event parsing, LLM judging, human coding, or a hybrid?
- How are round-level or event-level signals aggregated to run-level?
- What happens when submetrics disagree?

**Why this matters**: reviewers will not accept "the behavior follows the theory" unless the theory-aligned direction is preregistered as a formula or scoring table.

**Required fix**: define `TAR_H1_run` as a concrete formula, for example:

```text
TAR_H1_run =
  z(high_integration_encounter_rate)
  + z(public_node_conversation_rate)
  + z(information_spread_reach)
  - z(private_disclosure_in_high_integration_nodes)
```

The actual formula can differ, but it must exist before experiments run.

---

### 3. The additive decomposition of `C4 - C1` is too strong

v10 writes:

```text
C4 - C1 = (C6m - C1) + (C6f - C6m) + (C4 - C6f)
```

This is attractive as a narrative, but risky as a methodological claim.

In a long-run multi-agent simulation, effects are path-dependent:

- movement changes who meets whom;
- encounters change memory;
- memory changes later goals;
- conversations change information flow;
- information flow changes the social network;
- the social network changes later movement and action opportunities.

Because of this, `C6f - C6m` and `C4 - C6f` are not clean additive components in the way the formula implies. Once early trajectories diverge, later outcomes are not operating on the same state distribution.

**Required fix**: replace the additive equation with a weaker and more defensible statement:

```text
The contrasts C6m-C1, C6f-C6m, and C4-C6f are diagnostic contrasts.
They are used to probe whether perception, movement, and sampling each contribute
to the observed system-level difference, but they are not interpreted as a strict
additive causal decomposition in nonlinear long-run simulations.
```

This preserves the value of the condition matrix while avoiding an overclaim.

---

### 4. The map plan does not match current available assets

v10 recommends:

```text
Plaza, Labyrinth, Bridge, Irregular
```

But the current `spatial-agent-core/configs/layouts/` directory contains:

```text
grid.yaml
labyrinth.yaml
plaza.yaml
```

There is no current `bridge.yaml` or `irregular.yaml`.

**Why this matters**: if the plan says the formal design uses four maps, but the repo only contains three layout files, then the experiment cannot be run as written.

**Required fix**: choose one of two paths:

1. Change the formal plan to use the currently available maps:

```text
Plaza, Labyrinth, Grid
```

2. Or add an explicit implementation task:

```text
Before Stage 2, create and validate bridge.yaml and irregular.yaml.
They must pass Stage 0 metric sanity checks and reverse-inference audit.
```

The plan should not silently rely on missing assets.

---

### 5. Stage 4 should probably not be required for the MVP

v10 says the minimum publishable version must include:

- Stage 0
- Stage 1A
- Stage 2
- Stage 3 minimum robustness
- Stage 4 pairwise human preference

This may be too heavy for a first paper. Stage 4 is valuable, but it validates perceived realism or spatial fit; it does not establish the main causal mechanism.

For a main experimental paper, the core should be:

- Stage 0: validity gates
- Stage 1: representation-level signal
- Stage 2: long-run system effect
- Stage 3: minimal mechanism checks

Stage 4 should be a strong-version contribution, not necessarily an MVP blocker.

**Required fix**: split "minimum executable paper" and "strong submission version":

```text
MVP:
Stage 0 + Stage 1A + Stage 2 + minimum Stage 3

Strong version:
MVP + Stage 4 human preference + broader model/map robustness
```

This makes the plan more realistic.

---

### 6. The non-spatial control conditions need stricter generation and leakage rules

v10 usefully distinguishes:

- `C2 Implicit Spatial`
- `C2b Non-Spatial Structural`
- `C2c Truly Non-Spatial`

This is a good design choice. But the generation rules are not detailed enough.

For these controls to work, the plan must define:

- how descriptions are generated;
- how length is matched;
- how sentiment is balanced;
- how informativeness is matched;
- how reverse-inference leakage is measured;
- what cutoff rejects a description;
- whether descriptions are randomized across locations and seeds.

Otherwise, a reviewer can argue that differences come from phrasing, valence, or semantic salience rather than spatial configuration.

**Required fix**: import or restate concrete Stage 0 thresholds from the preflight protocol, especially for reverse-inference audit and lexical norming.

---

### 7. The explicit spatial description may still leak social affordance through language

The plan correctly says explicit descriptions should not say:

```text
This place is good for socializing.
```

But the proposed allowed descriptions still contain words such as:

- exposed
- secluded
- central
- frequent path overlap
- highly integrated

These words may already carry social-behavior priors for an LLM. A model does not necessarily need to reason over topology; it may simply map "exposed" to public/social and "secluded" to private/quiet.

**Required fix**: add a neutral numeric condition or subcondition:

```text
C6m_neutral:
This node has integration index 0.78, rank 3 of 20.
This node has mean depth 1.6, rank 4 of 20.
This node has control value 0.42, rank 8 of 20.
```

Then compare:

```text
C6m_natural vs C6m_neutral
```

If both work, the argument for computable configuration is stronger. If only natural language works, the paper should honestly frame the effect as spatial-vocabulary-mediated rather than purely configurational.

---

## Medium Concerns

### 1. Hypotheses need a preregistration table

The plan has RQs and hypotheses, but they should be rewritten as a table:

| Hypothesis | Direction | Unit | Primary metric | Confirmatory? | Fallback |
|---|---|---|---|---|---|
| H1a | high integration -> more co-presence | run | encounter rate | yes | descriptive |
| H1b | deep nodes -> more private disclosure | run | private disclosure rate | yes | exploratory |
| H2 | topology affects information spread | run | spread reach/speed | yes/no | exploratory |
| H3 | control value affects brokerage | run | brokerage score | conditional | drop if map lacks high-control nodes |

This table should appear before the experimental stages.

### 2. Stage 1 should gate Stage 2

If Stage 1 shows no representation-level effect, the 150-420 run long simulation becomes risky. The plan should say what happens if Stage 1 fails.

Suggested gate:

```text
If C6m-C1 does not show the preregistered direction on H1 microtasks
and C6m does not outperform C_shuffle, Stage 2 is downgraded to an
exploratory pilot.
```

### 3. Power analysis is missing

The plan gives:

```text
4 maps x 15 seeds x 7 conditions = 420 runs
```

and a minimum:

```text
3 maps x 10 seeds x 5 conditions = 150 runs
```

But it does not justify whether this is enough to detect the expected effect under mixed models or paired seed analysis.

Add at least a simulation-based power section for:

- `C4 vs C1`
- `C6m vs C2c`
- `C6f vs C6m`

### 4. Model versioning needs to be frozen before execution

The plan says to record model version, date, parameters, and prompt template. That is good, but before execution the plan should specify:

- primary model;
- backup model;
- temperature;
- top-p;
- max tokens;
- prompt hash or exact prompt file path.

Otherwise reproducibility will be weak.

### 5. The current survey-to-main-paper bridge should point to evidence tables

The plan summarizes survey findings, but the motivation section should link to the exact evidence table or appendix source used for the counts. Otherwise the survey result becomes a claim in prose rather than a traceable evidence base.

---

## What Is Strong in v10

Despite the concerns above, the plan has several important strengths.

### 1. The research gap is meaningful

The gap is not simply:

> nobody has used Space Syntax in LLM agents.

The stronger gap is:

> current LLM-agent environments usually represent space as names, labels, coordinates, or natural-language scene descriptions, but rarely test whether computable spatial relations themselves can become a behavioral input layer.

This is a good gap because it is empirical, testable, and narrower than claiming a full theory of LLM-agent society.

### 2. The survey and main paper now have a clearer relationship

The survey explains why the gap exists:

- built environment research has mature computable spatial theories;
- LLM-agent simulation has rich social behavior but weak spatial abstraction;
- the bridge between these areas is thin.

The main paper then tests one bridge:

> convert spatial configuration into structured input and measure whether agent behavior changes in theory-aligned ways.

This relationship is coherent.

### 3. The control matrix is much better than a binary baseline

The plan does not only ask:

```text
SpatialAgent vs BaseAgent
```

It asks whether the effect comes from:

- topology only;
- implicit spatial semantics;
- structured non-spatial text;
- explicit spatial configuration;
- movement decisions;
- action sampling;
- judge artifacts.

This is the right direction.

### 4. The plan acknowledges negative outcomes

The Tier 1-4 interpretation framework is useful. It prevents the paper from being locked into only one success narrative.

---

## Recommended Revision Structure

The next version should not mainly add more theory. It should make the plan executable.

Suggested `plan_v11.md` structure:

```text
0. One-paragraph claim
1. Survey-derived research gap
2. Core hypothesis table
3. Experimental conditions
4. Implementation binding table
5. Stage 0 validation gates
6. Stage 1 micro-task and gate
7. Stage 2 long-run design
8. Stage 3 mechanism checks
9. Optional Stage 4 human evaluation
10. Metrics and formulas
11. Statistical analysis and power
12. Interpretation tiers
13. Exact run checklist
```

The most important new section is:

```text
Implementation binding table
```

Example:

| Plan concept | Concrete file/config/script |
|---|---|
| `C1` | `configs/experiments/v10_conditions.yaml:conditions.C1` |
| `Plaza` | `configs/layouts/plaza.yaml` |
| run generator | `experiments/run_v10.py` |
| event log schema | `outputs/v10/{map}/{seed}/{condition}/events.jsonl` |
| `TAR_H1_run` | `src/analysis/v10_metrics.py::compute_tar_h1_run` |

---

## Final Recommendation

Do not treat v10 as implementation-ready yet.

The concept is strong enough to keep. The next revision should focus on five fixes:

1. Replace the additive decomposition with diagnostic contrasts.
2. Define `TAR_H1_run` as an explicit formula.
3. Map each condition to actual config/script/output files.
4. Align map names with real layout assets or add missing maps.
5. Move Stage 4 from MVP requirement to strong-version validation.

Once these are fixed, the plan can become a credible experimental protocol rather than a high-level research blueprint.
