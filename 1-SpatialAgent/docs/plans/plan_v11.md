# SpatialAgent 研究计划 v11

## Can Computable Spatial Configuration Shape LLM-Agent Social Behavior?

> 版本: 11.0  
> 日期: 2026-05-02  
> 作者: Li  
> 目标会议: AAMAS-27 首选 / AAAI-27 备选  
> 本版本目标: 基于 `docs/reviews/plan_v10_r1.md` 与 `docs/reviews/plan_v10_r2.md`，把 v10 从概念性 research plan 收敛为可预注册、可执行、可失败的实验协议。

---

## 0. 一句话版本

本文不试图证明 Space Syntax 在 LLM-agent 世界中“成立”。

本文检验的是一个更窄、更可证伪的问题：

> 当 LLM agents 不只接收地点名、语义场景或局部邻接，而是接收可计算的空间构型信息时，它们的社会行为是否会发生可测、可解释、并且沿预注册方向变化的差异？

也就是说，本文关注的不是：

> agent 世界里有没有空间背景？

而是：

> 空间结构能否作为一种 agent-facing behavioral input，而不只是叙事背景、地图贴图或 prompt 装饰？

---

## 1. Survey 到主 Paper 的逻辑

### 1.1 Survey 已经支持的事实

当前 survey evidence table 位于：

```text
spatial-agent-survey/paper/appendix/appendix_evidence_table.csv
```

当前稳定口径应以该 evidence table 为准：

- `35` coded rows
- `anchor_core`: `19` coded rows
- `bridge_core`: `16` coded rows
- representation distribution: `L1 = 1 / L2 = 8 / L3 = 19 / L4 = 1 / L5 = 6`
- strict `anchor_core` 中 `L4 = 0`
- 唯一 `L4` 出现在 widened digital-network `bridge_core`，不构成严格物理空间 / Space Syntax 意义上的 anchor evidence

如果论文正文需要写 paper-level source count，必须在写作前重新区分：

```text
coded rows != unique paper-level sources
```

v10 中 `32 sources / 34 rows` 与 `17 sources / 19 rows` 的 source count 不应直接复用，除非 appendix 同步定义了去重口径。2026-05-02 加入 `TR-01` 后，当前 widened Core 暂按 `33` paper-level sources / `35` coded rows 使用。

### 1.2 Survey 给出的 research gap

LLM-agent 系统并不缺“空间环境”。

已有系统中经常出现：

- towns
- maps
- game worlds
- Minecraft-like worlds
- social VR environments
- 3D scenes
- graph-based environments
- local movement and co-presence interfaces

但 agent-facing spatial representation 通常停留在：

- 地点名
- 动作标签
- 语义场景描述
- 附近对象或附近人物
- 局部邻接关系
- 局部移动选项

因此，survey 支撑的 gap 不是：

> 现有 LLM-agent 系统没有空间。

而是：

> 现有 LLM-agent 研究很少系统检验 agent-facing configurational spatial information 是否能在语义场景描述之外影响社会行为。

### 1.3 主 Paper 接住的问题

Survey 回答：

> 文献中是否存在这种 agent-facing configurational spatial layer？

Main paper 回答：

> 如果我们真的把这种 spatial layer 提供给 agents，它是否有行为价值？

两篇论文的关系：

| 论文 | 回答的问题 | 产物 |
|---|---|---|
| Survey | 现有 LLM-agent 文献是否系统使用 agent-facing configurational spatial information？ | evidence map + taxonomy + research agenda |
| Main paper | 提供这类信息后，agent 行为是否发生可测变化？ | controlled experiment + prototype + evaluation |

---

## 2. Research Gap 的最终表述

### 2.1 不使用的弱 gap

不要把 gap 写成：

> 现有 LLM-agent 系统没有使用 Space Syntax。

这个说法太弱，因为审稿人会问：

- 不用 Space Syntax 又怎样？
- 为什么一定要用 Space Syntax？
- Space Syntax 本身是否可证伪？
- Space Syntax 在现实城市中尚有争议，为什么能直接迁移到 LLM-agent 社会？

### 2.2 使用的强 gap

本文使用下面这个 gap：

> Although LLM-agent systems increasingly place agents in maps, towns, games, and simulated communities, the spatial layer is rarely treated as an explicit, computable, and experimentally controlled behavioral variable. Existing systems often expose place names, semantic scene descriptions, nearby entities, or local movement options, but seldom test whether agent-facing configurational structure, such as depth, integration, control, or global network position, changes social behavior beyond semantic prompting. As a result, we do not yet know whether spatial structure functions as a genuine behavioral signal in LLM-agent societies, or merely as narrative background.

中文解释：

> 虽然现有 LLM-agent 系统越来越常把 agent 放进地图、小镇、游戏和模拟社区里，但空间层很少被当作明确、可计算、可操控的行为变量。现有系统多给 agent 地点名、语义场景、附近对象或局部移动选项，却很少检验 agent 可见的构型信息，例如 depth、integration、control 或 global network position，是否能在语义 prompt 之外改变社会行为。因此我们还不知道，空间结构在 LLM-agent 社会中到底是一种真正的行为信号，还是只是叙事背景。

### 2.3 本文的理论边界

本文不主张：

> Space Syntax 是现实社会空间的已验证真理，因此 LLM agents 应该使用它。

本文主张：

> Space Syntax-inspired topological descriptors provide a computable representation layer for testing whether LLM agents can respond to configurational information beyond semantic scene descriptions.

Space Syntax 在本文中的角色是方法性而非本体性：

- 它提供一组可计算的空间关系变量。
- 它帮助我们把“空间”从场景文本变成可控实验变量。
- 它不自动保证 LLM-agent 社会会产生真实城市或建筑中的社会规律。

---

## 3. 核心贡献

本文预期贡献分为四类。

### 3.1 Conceptual contribution

提出一个从 survey gap 到实验系统的桥：

```text
space as narrative background
-> space as computable agent-facing behavioral input
```

### 3.2 System contribution

构建一个 SpatialAgent prototype，使 agent 可以在不同条件下接收：

- topology-only information
- implicit spatial affordance text
- non-spatial structured descriptions
- explicit configurational descriptors
- movement-level spatial metrics
- action-sampling spatial priors

### 3.3 Experimental contribution

通过 controlled simulation 检验：

- spatial descriptors 是否改变行为；
- 这种改变是否超出语义 prompting；
- 这种改变是否沿预注册理论方向；
- 这种改变是否来自 actor，而不是 judge 或 scorer。

### 3.4 Negative-result contribution

即便结果为负，本文仍能说明：

> 有地图、有地点名、有 3D backend、有空间词，并不自动意味着 LLM-agent 系统具有可用的空间机制。

---

## 4. 可说与不可说

### 4.1 本文可以说

- Computable spatial configuration can be represented as agent-facing input.
- LLM agents may respond differently to topology-only, semantic, and explicit configurational spatial inputs.
- Some behavioral differences can be tested against preregistered Space Syntax-inspired directions.
- Spatial descriptors may improve behavioral controllability, interpretability, or spatial appropriateness in simulation.

### 4.2 本文不可以说

- Space Syntax 在 LLM-agent 社会中被证明成立。
- LLM agents 真实理解了空间。
- LLM-agent 社会等同于真实城市社会。
- 任何显著行为差异都能自动归因于“空间机制”。

### 4.3 最安全的主张

最终论文应使用这句话作为主张边界：

> We do not claim that Space Syntax is validated in LLM-agent societies. Instead, we use Space Syntax-inspired topological descriptors as a computable representation layer to test whether LLM agents can respond to configurational information beyond semantic scene labels, and whether such responses improve behavioral controllability, interpretability, and spatial appropriateness.

---

## 5. Hypothesis Registration

v11 把 RQ 改写为可预注册 hypothesis table。

### 5.1 Research questions

| RQ | 问题 | 对应 hypothesis |
|---|---|---|
| RQ1 | explicit configurational input 是否改变行为？ | H1a, H1b |
| RQ2 | 这种效果是否超出语义 prompt 和结构化格式？ | H1c |
| RQ3 | 行为变化是否沿 Space Syntax-inspired 方向？ | H1a, H2, H3 |
| RQ4 | 效果来自结构信息还是语言联想？ | H1d, H1e |
| RQ5 | 效果是否足够稳定和可感知？ | H4 |

### 5.2 Confirmatory hypotheses

| ID | Direction | Unit | Primary metric | Main comparison | Status |
|---|---|---|---|---|---|
| H1a | Higher integration nodes have higher social-event rate. | run | `tar_h1_run_early`, `tar_h1_run_full` | `C4 > C1` | confirmatory |
| H1b | Explicit configurational perception increases H1 alignment beyond topology-only input. | run | `tar_h1_run_early`, `tar_h1_run_full` | `C6m > C1` | confirmatory |
| H1c | Explicit configurational perception exceeds non-spatial and implicit semantic controls. | run | `tar_h1_run_full` | `C6m > C2`, `C6m > C2b`, `C6m > C2c` | confirmatory with FDR |
| H1d | Correct structure-location mapping matters. | run | `tar_h1_run_full` | `C6m > C_shuffle` | mechanism confirmatory |
| H1e | Neutral numeric spatial descriptors preserve part of the effect. | micro-task | `h1_micro_alignment` | `C6m_neutral > C1` | mechanism confirmatory |

### 5.3 Secondary and exploratory hypotheses

| ID | Direction | Unit | Metric | Status |
|---|---|---|---|---|
| H2 | Higher mean depth nodes have higher privacy-event rate. | run | `tar_h2_run` | secondary |
| H3 | Higher control-value nodes have higher gatekeeping-event rate. | run | `tar_h3_run` | conditional secondary |
| H4 | Human judges prefer SpatialAgent trajectories as more spatially appropriate. | participant | pairwise preference | strong-version secondary |

H3 只有在地图中存在足够高 control-value 节点时进入确认性分析。若 high-control 节点数不足，H3 自动降级为 descriptive analysis。

---

## 6. Implementation Binding

v11 的目标是让每个研究概念都能绑定到文件、配置或待实现任务。

### 6.1 Current implementation status

| Component | Current state | File |
|---|---|---|
| Preflight protocol | partially implemented | `spatial-agent-core/configs/experiments/preflight_v7.yaml` |
| Preflight runner | implemented | `spatial-agent-core/experiments/run_preflight.py` |
| Run-level TAR/BSR analysis | implemented for v7-style logs | `spatial-agent-core/src/analysis/spatial_behavioral.py` |
| Main experiment config | placeholder only | `spatial-agent-core/configs/experiments/exp1_spatial_vs_baseline.yaml` |
| Layout assets | `plaza`, `labyrinth`, `grid` available | `spatial-agent-core/configs/layouts/` |
| Bridge / irregular layouts | not yet available | implementation task |

### 6.2 Required v11 implementation files

Before Stage 1 or Stage 2 can run, create or update:

| Need | Proposed file |
|---|---|
| v11 condition definitions | `spatial-agent-core/configs/experiments/v11_conditions.yaml` |
| v11 main experiment config | `spatial-agent-core/configs/experiments/exp_v11_main.yaml` |
| v11 run launcher | `spatial-agent-core/experiments/run_v11.py` |
| v11 metric wrapper | `spatial-agent-core/src/analysis/v11_metrics.py` |
| v11 power simulation | `spatial-agent-core/src/analysis/v11_power.py` |
| v11 output schema doc | `spatial-agent-core/docs/v11_output_schema.md` |

### 6.3 Condition-to-config binding

| Condition | Config key | Movement input | Arrival description | Sampling | Role |
|---|---|---|---|---|---|
| `C1` | `conditions.C1` | adjacency + place name + co-presence count | none | none | topology-only baseline |
| `C2` | `conditions.C2` | same as `C1` | implicit affordance text | none | semantic spatial baseline |
| `C2b` | `conditions.C2b` | same as `C1` | non-spatial structured text | none | format control |
| `C2c` | `conditions.C2c` | same as `C1` | randomized non-spatial norms or time patterns | none | true non-spatial control |
| `C6m` | `conditions.C6m` | same as `C1` | natural-language configurational descriptors | none | perception effect |
| `C6m_neutral` | `conditions.C6m_neutral` | same as `C1` | neutral numeric spatial descriptors | none | language-prior audit |
| `C6f` | `conditions.C6f` | spatial metrics + adjacency + place name + co-presence count | configurational descriptors | none | movement contribution |
| `C4` | `conditions.C4` | same as `C6f` | configurational descriptors | enabled | full SpatialAgent |
| `C_shuffle` | `conditions.C_shuffle` | same as `C6m` | spatial metrics shuffled across locations | none | mapping audit |
| `C_counter` | `conditions.C_counter` | same as `C6m` | structure conflicts with semantic label | none | structure vs semantic audit |
| `C_judge_only` | `conditions.C_judge_only` | agent sees `C1`; judge sees spatial info | none for agent | none | judge artifact audit |
| `C_rule_scorer` | `conditions.C_rule_scorer` | same as relevant condition | same as relevant condition | same | non-LLM scoring audit |

### 6.4 Map-to-layout binding

MVP uses only existing assets:

| Map name in paper | Layout file | Status |
|---|---|---|
| `Plaza` | `configs/layouts/plaza.yaml` | available |
| `Labyrinth` | `configs/layouts/labyrinth.yaml` | available |
| `Grid` | `configs/layouts/grid.yaml` | available |

Strong version may add:

| Map name | Required file | Status |
|---|---|---|
| `Bridge` | `configs/layouts/bridge.yaml` | to create |
| `Irregular` | `configs/layouts/irregular.yaml` | to create |

The paper must not list `Bridge` or `Irregular` as formal design maps until the files exist and pass Stage 0 gates.

### 6.5 Output schema

Every run must produce:

```text
results/v11/{map}/{seed}/{condition}/metadata.json
results/v11/{map}/{seed}/{condition}/visits.csv
results/v11/{map}/{seed}/{condition}/events.csv
results/v11/{map}/{seed}/{condition}/messages.jsonl
results/v11/{map}/{seed}/{condition}/metrics_run.json
```

Required `visits.csv` columns:

```text
round, agent_id, location
```

Required `events.csv` columns:

```text
round, agent_id, target_id, location, event_type, event_text, judge_source
```

Allowed `event_type` values for confirmatory metrics:

```text
social, privacy, gatekeeping, other
```

---

## 7. Experimental Conditions

### 7.1 Main conditions

| Condition | Purpose | Included in MVP? |
|---|---|---|
| `C1` | minimum topology-only baseline | yes |
| `C2c` | true non-spatial control | yes |
| `C6m` | explicit spatial perception | yes |
| `C6m_neutral` | neutral numeric spatial descriptor audit | Stage 1 yes, Stage 2 optional |
| `C6f` | movement-level spatial metrics | yes |
| `C4` | full system | yes |
| `C2` | implicit spatial affordance baseline | strong version |
| `C2b` | structured non-spatial format control | strong version |

### 7.2 Mechanism and audit conditions

| Condition | Purpose | Minimum use |
|---|---|---|
| `C_shuffle` | checks whether correct metric-location mapping matters | Stage 1 and minimum Stage 3 |
| `C_counter` | checks structure vs semantic label conflict | Stage 1 or Stage 3 |
| `C_judge_only` | checks whether evaluation creates the effect | Stage 3 |
| `C_rule_scorer` | checks whether non-LLM scorer preserves direction | Stage 3 |

### 7.3 Explicit spatial description rules

Forbidden direct affordance claims:

```text
This place is good for socializing.
This place is suitable for private conversation.
This place should make agents gather.
```

Natural configurational description may mention structure:

```text
This location is highly integrated in the layout. It has short average topological distance to many other locations, high connectivity, and frequent path overlap.
```

But natural words such as `integrated`, `central`, `exposed`, and `secluded` may carry language priors. Therefore `C6m_neutral` must also be tested:

```text
This node has integration_z = 1.24, integration_rank = 3 of 20.
This node has mean_depth_z = -0.81, depth_rank = 4 of 20.
This node has control_value_z = 0.36, control_rank = 9 of 20.
```

Interpretation rule:

| Result | Interpretation |
|---|---|
| `C6m` and `C6m_neutral` both positive | stronger evidence for configurational input |
| only `C6m` positive | effect may be spatial-vocabulary-mediated |
| neither positive | no robust evidence for configurational responsiveness |

---

## 8. Experimental Materials

### 8.1 Maps

MVP maps:

- `Plaza`: high integration / public convergence case
- `Labyrinth`: high depth / privacy and separation case
- `Grid`: regular control topology

Strong-version maps:

- `Bridge`: brokerage and control-value case
- `Irregular`: ecological robustness case

Each map must pass Stage 0 checks before entering Stage 2:

- connected graph
- no isolated required location
- enough variation in integration and mean depth
- high-control nodes if H3 is analyzed
- labels pass lexical leakage checks

### 8.2 Agents

MVP:

```text
10 agents per run
200 rounds per run
```

Convergence pilot may adjust round count to `300` if metrics do not stabilize.

Agents should vary in:

- role
- public/private preference
- information sensitivity
- movement tendency
- social openness

But these traits must be fixed across matched conditions within the same seed.

### 8.3 Models

Before running confirmatory experiments, freeze:

| Role | Current candidate | Config source |
|---|---|---|
| primary model | `qwen3.5-plus` | `preflight_v7.yaml` |
| robustness model | `deepseek-chat` | `preflight_v7.yaml` |
| optional OpenAI-compatible model | `gpt-5.4` | `preflight_v7.yaml` |

Default parameters from current preflight config:

```text
temperature = 0.0
max_tokens = 300
```

Before execution, record:

- model endpoint name
- provider
- date
- temperature
- top-p if available
- max tokens
- prompt template path
- prompt hash

---

## 9. Stage 0: Preflight Gates

Stage 0 does not enter main conclusion. It decides whether the planned experiment is valid enough to run.

### 9.1 Existing thresholds to retain

From `preflight_v7.yaml`:

| Gate | Threshold |
|---|---|
| comprehension accuracy | `>= 0.85` |
| behavioral inference accuracy | `>= 0.70` |
| reverse-inference leak cutoff | `<= 0.65` |
| prompt-position min accuracy | `>= 0.70` |
| lexical primary gap | `>= 1.5` |
| lexical nuisance spread | `<= 1.25` |

### 9.2 Required preflight checks

| Check | Purpose | If fail |
|---|---|---|
| metric sanity | verifies integration/depth/control are well-formed | fix map or remove map |
| model comprehension | verifies model understands descriptor format | revise prompt |
| reverse-inference audit | checks whether labels reveal hidden spatial class | rewrite labels/descriptions |
| lexical norming | checks valence/publicness/privacy leakage | rebalance text |
| prompt-position audit | checks descriptor placement stability | fix prompt template |
| event-coding pilot | checks event parser/judge agreement | revise coding manual |
| MIC pilot | checks matched seed variance reduction | revise seed/run design |
| convergence pilot | chooses 200 vs 300 rounds | set round count |

### 9.3 Pass condition

Stage 0 passes only if:

```text
all mandatory gates pass
and
at least Plaza, Labyrinth, Grid pass map sanity checks
and
event_type coding supports social/privacy/gatekeeping labels
```

If any mandatory gate fails, Stage 1 and Stage 2 are not confirmatory.

---

## 10. Stage 1: Micro-task Representation Experiment

### 10.1 Purpose

Stage 1 asks:

> Before running long simulations, does the spatial representation itself change single-step behavioral judgment?

This prevents wasting 150-420 long-run simulations if the model shows no response to the representation layer.

### 10.2 Task types

| Task | Description | Main signal |
|---|---|---|
| choice task | choose where to go or act | spatial preference |
| behavioral inference | infer likely behavior from spatial descriptor | H1/H2/H3 direction |
| counter-label task | structure conflicts with semantic label | structure vs language |
| neutral descriptor task | numeric descriptors replace natural spatial language | language-prior audit |

### 10.3 Stage 1 conditions

Minimum:

```text
C1, C2c, C6m, C6m_neutral, C_shuffle
```

Strong version:

```text
C1, C2, C2b, C2c, C6m, C6m_neutral, C_shuffle, C_counter
```

### 10.4 Stage 1 gate into Stage 2

Stage 2 remains confirmatory only if:

```text
C6m - C1 is positive on preregistered H1 direction
and
C6m - C_shuffle is positive
and
C6m_neutral - C1 is non-negative
```

Recommended effect gate:

```text
d >= 0.30 for C6m vs C1 on H1 microtasks
```

If Stage 1 fails:

- Stage 2 may still run as an exploratory pilot.
- The paper cannot claim confirmatory evidence for configurational behavioral input.
- The result should be written as a negative or boundary-condition paper.

---

## 11. Stage 2: Long-run Multi-agent Simulation

### 11.1 Purpose

Stage 2 is the main experiment.

It tests:

> In long-run multi-agent simulations, does agent-facing spatial configuration alter movement, encounters, interaction, information spread, and social-network behavior in preregistered directions?

### 11.2 Run definition

```text
run = map × seed × condition
```

Matched initial conditions within the same `map × seed`:

- initial agent locations
- personas
- initial goals
- initial world events
- initial non-spatial description mapping
- random seed

MIC only matches initial conditions. It does not claim that trajectories remain comparable after interactions diverge.

### 11.3 MVP design

```text
3 maps × 10 seeds × 5 conditions = 150 runs
```

MVP maps:

```text
Plaza, Labyrinth, Grid
```

MVP conditions:

```text
C1, C2c, C6m, C6f, C4
```

MVP has enough structure for a first confirmatory test only if Stage 1 passes and power analysis shows acceptable sensitivity.

### 11.4 Strong-version design

```text
3 maps × 15 seeds × 8 main conditions = 360 runs
```

Strong main conditions:

```text
C1, C2, C2b, C2c, C6m, C6m_neutral, C6f, C4
```

Optional expanded version after new maps exist:

```text
5 maps × 15 seeds × 8 main conditions = 600 runs
```

### 11.5 Diagnostic contrasts

Do not interpret the following as strict additive causal decomposition.

Use them as diagnostic contrasts:

| Contrast | Interpretation |
|---|---|
| `C4 - C1` | full SpatialAgent vs topology-only baseline |
| `C6m - C1` | arrival-time configurational perception effect |
| `C6m - C2c` | explicit spatial structure vs true non-spatial control |
| `C6m - C2` | explicit structure vs implicit affordance semantics |
| `C6m - C2b` | spatial content vs structured non-spatial format |
| `C6m_neutral - C1` | neutral metric representation effect |
| `C6f - C6m` | movement-level spatial metric contribution |
| `C4 - C6f` | action-sampling contribution |

Reason:

> Long-run multi-agent simulation is path-dependent. Movement changes encounters; encounters change memory; memory changes future action. Therefore contrasts probe mechanisms, but their differences should not be treated as additive components of one linear total effect.

### 11.6 Early and full-run endpoints

Because MIC trajectories can diverge after early rounds, preregister both:

```text
tar_h1_run_early = tar_h1_run over rounds 1-50
tar_h1_run_full = tar_h1_run over all rounds
```

Interpretation:

| Pattern | Interpretation |
|---|---|
| early positive, full weak | spatial priming |
| early and full positive | sustained spatial guidance |
| early weak, full positive | delayed network-level effect |
| neither positive | no robust H1 support |

---

## 12. Stage 3: Mechanism and Robustness

### 12.1 Minimum Stage 3

Minimum mechanism checks:

```text
3 maps × 10 seeds × 3 audit conditions
```

Audit conditions:

```text
C_shuffle, C_judge_only, C_rule_scorer
```

### 12.2 Strong Stage 3

Strong mechanism checks:

```text
C_shuffle, C_counter, C_judge_only, C_rule_scorer, robustness model
```

### 12.3 Downgrade rules

| Result | Consequence |
|---|---|
| `C_judge_only` reproduces main effect | conclusion downgraded to judge artifact risk |
| `C_rule_scorer` reverses direction | conclusion downgraded to LLM-evaluator-dependent |
| `C_shuffle` remains as strong as `C6m` | conclusion downgraded to language prior or generic prompt effect |
| `C_counter` follows semantic label over structure | conclusion downgraded to semantic affordance effect |
| robustness model fully fails | conclusion limited to primary model |

---

## 13. Stage 4: Human Evaluation

Stage 4 is not part of the MVP.

It belongs to the strong submission version because it tests perceived spatial appropriateness, not the primary causal mechanism.

### 13.1 Human evaluation task

Participants compare paired trajectories:

```text
same map
same seed
different condition
```

Question:

> Which trajectory appears more spatially appropriate and socially plausible?

### 13.2 Minimum human evaluation

```text
N = 60 participants
```

But `N = 60` may be underpowered for small preference shifts. If possible, target:

```text
N = 80 participants
```

Primary comparison:

```text
C4 vs C1
```

Secondary comparisons:

```text
C6m vs C2c
C6m vs C2
C6m_neutral vs C1
```

### 13.3 Interpretation

Human preference supports practical value only if it aligns with simulation metrics.

If simulation metrics are positive but humans cannot distinguish trajectories, the paper should claim behavioral controllability but not perceived realism.

---

## 14. Metrics and Formulas

### 14.1 Existing TAR/BSR implementation

Current code already provides a v7-style run-level alignment function:

```text
spatial-agent-core/src/analysis/spatial_behavioral.py::compute_run_level_alignment
```

It defines:

```python
HYPOTHESIS_SPECS = {
    "h1": {"event_type": "social", "metric": "integration_z"},
    "h2": {"event_type": "privacy", "metric": "mean_depth_z"},
    "h3": {"event_type": "gatekeeping", "metric": "control_value_z"},
}
```

v11 retains this as the primary metric logic unless `v11_metrics.py` intentionally revises it.

### 14.2 Operational formula

For each run and hypothesis:

```text
For each location:
  event_rate_h = number of events of type h at location / visits to location

rho_h_run = SpearmanCorr(event_rate_h, spatial_metric_h)
tar_h_run = FisherZ(rho_h_run)
bsr_h_run = abs(tar_h_run)
```

Mapping:

| Hypothesis | Event type | Spatial metric | Expected direction |
|---|---|---|---|
| H1 | `social` | `integration_z` | positive |
| H2 | `privacy` | `mean_depth_z` | positive |
| H3 | `gatekeeping` | `control_value_z` | positive |

Minimum valid location inclusion:

```text
min_location_visits = 5
```

### 14.3 Primary endpoint

Primary endpoints:

```text
tar_h1_run_early
tar_h1_run_full
```

Primary comparison:

```text
C4 vs C1
```

Primary success requires:

```text
tar_h1_run_early positive
and
tar_h1_run_full positive
and
at least one remains significant after planned correction
and
effect size is practically non-trivial
```

Recommended practical threshold:

```text
d >= 0.5 for C4 vs C1 on tar_h1_run_full
```

If early and full endpoints disagree, use the interpretation table in Section 11.6.

### 14.4 Secondary metrics

| Layer | Metrics |
|---|---|
| movement | high-integration visit share, mean visited depth, location entropy |
| encounter | co-presence rate, encounter diversity, repeat encounter |
| interaction | active dialogue rate, partner diversity, sensitive disclosure rate |
| information spread | reach, speed, source concentration |
| social network | degree centralization, clustering, brokerage |
| role behavior | guarding, mediating, withholding, public/private action choice |

Secondary metrics do not replace the primary endpoint.

---

## 15. Statistical Analysis and Power

### 15.1 Confirmatory model

Primary model:

```r
tar_h1_run_full ~ condition + map + condition:map + (1|seed)
```

Early endpoint model:

```r
tar_h1_run_early ~ condition + map + condition:map + (1|seed)
```

If the model is unstable due to small map count:

```r
tar_h1_run_full ~ condition + (1|seed)
```

and report map-specific estimates descriptively.

### 15.2 Confirmatory comparisons

| Priority | Comparison | Endpoint | Correction |
|---|---|---|---|
| 1 | `C4 vs C1` | `tar_h1_run_full`, `tar_h1_run_early` | primary |
| 2 | `C6m vs C1` | `tar_h1_run_full`, `tar_h1_run_early` | FDR |
| 3 | `C6m vs C2c` | `tar_h1_run_full` | FDR |
| 4 | `C6m vs C2` | `tar_h1_run_full` | FDR, strong version |
| 5 | `C6m vs C2b` | `tar_h1_run_full` | FDR, strong version |
| 6 | `C6m_neutral vs C1` | `tar_h1_run_full` | FDR, strong version |
| 7 | `C6f vs C6m` | movement and H1 endpoints | diagnostic |
| 8 | `C4 vs C6f` | H1 and sampling-sensitive endpoints | diagnostic |

### 15.3 Power analysis requirement

Before confirmatory Stage 2, run simulation-based power for at least:

```text
C4 vs C1
C6m vs C2c
C6f vs C6m
```

Power simulation should vary:

- seeds: `10`, `15`, `20`
- maps: `3`, `5`
- effect sizes: `d = 0.3`, `0.5`, `0.7`
- seed ICC assumptions
- map heterogeneity assumptions

Decision rule:

| Result | Action |
|---|---|
| MVP power >= 0.80 for `C4 vs C1` at plausible d | MVP can support confirmatory claim |
| MVP power between 0.70 and 0.80 | MVP can support cautious confirmatory claim |
| MVP power < 0.70 | MVP becomes pilot, not confirmatory main paper |

### 15.4 Exploratory analyses

Exploratory:

- H2 privacy/depth
- H3 control/gatekeeping if high-control nodes are sparse
- time-window heterogeneity beyond early/full
- model-specific effects
- agent-trait moderation
- social-network macro metrics

Exploratory analyses cannot overturn a failed primary endpoint.

---

## 16. Budget and Scale

### 16.1 MVP

```text
Stage 0: preflight gates
Stage 1: C1, C2c, C6m, C6m_neutral, C_shuffle
Stage 2: 3 maps × 10 seeds × 5 conditions = 150 runs
Stage 3: minimum audit checks
Stage 4: not required
```

MVP maps:

```text
Plaza, Labyrinth, Grid
```

MVP conditions:

```text
C1, C2c, C6m, C6f, C4
```

### 16.2 Strong submission version

```text
Stage 0: all gates
Stage 1: full micro-task condition set
Stage 2: 3 maps × 15 seeds × 8 conditions = 360 runs
Stage 3: mechanism and model robustness
Stage 4: human pairwise preference, N = 80 target
```

### 16.3 Expanded version

Only after `bridge.yaml` and `irregular.yaml` exist:

```text
5 maps × 15 seeds × 8 conditions = 600 runs
```

---

## 17. Result Interpretation Tiers

| Tier | Main result | Mechanism checks | Human eval | Claim |
|---|---|---|---|---|
| Tier 1 | H1 positive early and full | `C_shuffle` weaker, `C_rule_scorer` consistent | preference positive | configuration is a meaningful behavioral input |
| Tier 2 | H1 positive but mechanism mixed | some semantic or language-prior dependence | preference mixed | spatial descriptors help but are entangled with language |
| Tier 3 | only weakly better than minimal baseline | judge/scorer/model dependence | unclear | effect may be prompt-format or evaluator-driven |
| Tier 4 | no stable effect | no mechanism support | no preference | current descriptors do not support robust configurational control |

Negative result is still publishable if framed as:

> Current LLM-agent systems do not automatically acquire spatial mechanisms from maps, labels, or spatial vocabulary; explicit configurational representations may also fail unless models can operationalize them.

---

## 18. Paper Structure

### 18.1 Main paper

```text
1. Introduction
2. Related Work and Survey-Derived Gap
3. SpatialAgent Representation Layer
4. Hypotheses and Experimental Design
5. Stage 0 and Stage 1 Validation
6. Stage 2 Long-run Results
7. Mechanism and Robustness
8. Discussion
9. Limitations
10. Conclusion
```

### 18.2 Appendix

```text
A. Survey evidence bridge
B. Layout metrics
C. Prompt templates
D. Condition descriptions
E. Event coding manual
F. Power simulation
G. Additional robustness
H. Human evaluation materials
```

---

## 19. Execution Checklist

### 19.1 Before coding

- [ ] Freeze v11 condition definitions.
- [ ] Decide whether `C2` and `C2b` are strong-version only or included in first run.
- [ ] Freeze primary model and parameters.
- [ ] Freeze prompt templates and hash them.
- [ ] Confirm map assets for MVP: `plaza`, `labyrinth`, `grid`.

### 19.2 Before Stage 1

- [ ] Implement `v11_conditions.yaml`.
- [ ] Implement or adapt Stage 1 task generator.
- [ ] Add neutral numeric descriptor templates.
- [ ] Run reverse-inference and lexical audits.
- [ ] Define Stage 1 result table format.

### 19.3 Before Stage 2

- [ ] Implement `exp_v11_main.yaml`.
- [ ] Implement `run_v11.py`.
- [ ] Confirm output schema.
- [ ] Implement `v11_metrics.py` wrapper if needed.
- [ ] Run power simulation.
- [ ] Run convergence pilot.

### 19.4 Before writing results

- [ ] Report early and full endpoints.
- [ ] Report all diagnostic contrasts as diagnostic, not additive decomposition.
- [ ] Apply downgrade rules.
- [ ] Keep exploratory analyses separate from confirmatory claims.

---

## 20. Final Positioning

v11 的最终定位是：

> This paper tests whether computable spatial configuration can become a controlled behavioral input layer for LLM agents.

不是：

> This paper proves Space Syntax in artificial societies.

最理想的结果不是简单证明“空间有效”，而是回答：

> 哪一种空间表征有效，在哪些行为层面有效，是否超出语义 prompt，是否能通过非 LLM scorer 和机制审计，是否值得未来 agent simulation 系统认真建模。

这才是 survey 和 main paper 之间最稳的桥。
