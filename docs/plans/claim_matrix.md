# Survey Claim Matrix

适用对象：`survey_plan_v4.md` 对应综述  
版本：v2  
日期：2026-04-28

---

## 0. Purpose

这份文档用来约束正文中的论断强度，避免以下常见漂移：

- 文献里“经常出现”被写成“已有强证据”
- 系统“设计上考虑了空间”被写成“空间已被证明影响行为”
- widened-Core 中的 `bridge_core` 被写得和 strict `anchor_core` 一样强
- 物理空间实证、Adjacent work 或 boundary cases 被误写成对 LLM multi-agent social behavior 的直接证据

一句话原则：

**先区分 corpus role，再区分 core layer，再区分 evidence status，最后才决定能写多强的 claim。**

---

## 1. Current Operating Baseline

本轮写作与 claim check 必须以 `2026-04-28` 的 widened-Core 口径为准：

- strict baseline：`17` paper-level `anchor_core` items，`19` rows
- stable widened Core：`32` paper-level items，`34` rows
- row layers：`anchor_core = 19`，`bridge_core = 15`
- representation distribution：`L1 = 1 / L2 = 8 / L3 = 18 / L4 = 1 / L5 = 6`
- evidence status：`observed_effect = 19`，`designed_affordance_only = 15`
- `L4` 只出现在 widened digital-network `bridge_core`，不出现在 strict `anchor_core`
- `TW-02` 只保留为 scope-boundary 对照，不纳入 stable widened-Core
- `HC01` 只作为 Adjacent / boundary / feasibility evidence

这意味着：

- 可以写 widened-Core 的分布描述，但不能把 widened-Core 自动当成 strict nucleus
- 可以写“widened-Core 下 `L4` 不再完全缺失”，但必须立刻补一句“它只出现在单个 digital-network bridge case”
- 不可以把 bridge-layer 恢复出的 `L2 / L4 / L5` 切片写成整个 field 已稳定覆盖这些表示层

---

## 2. Governing Principles

1. `Frequency != strength`  
   很多系统都带空间环境，不代表空间已被证明是行为驱动因素。

2. `Design != effect`  
   系统被设计成有空间 affordance，不代表作者已经观察到空间效应。

3. `Bridge != anchor`  
   widened-Core 是主 evidence map 的有效扩展，但 `bridge_core` 的证据权重仍低于 strict `anchor_core`。

4. `Foundational != direct evidence`  
   Space Syntax 和物理空间实证只能支撑理论与假设迁移，不能直接证明 LLM multi-agent 的行为效应。

5. `Adjacent != social effect evidence`  
   spatial reasoning benchmark、single-agent spatial system 或边界案例只能支撑“模型可能可处理该类输入”或“边界上可行”，不能支撑“社会行为会因此改变”。

6. `Boundary cases stay boundary cases`  
   `TW-02`、`HC01` 等案例可以帮助说明 scope、feasibility 或 exclusion logic，但不能悄悄回流成主结论证据。

---

## 3. Claim Types

| Claim Type | Meaning |
|-----------|---------|
| `descriptive_mapping` | 文献中有哪些系统、表示方式、行为类型、评估方式、evidence roles |
| `distribution_gap` | 某类表示或研究方向在当前 corpus 中稀缺、单薄或只在 widened bridge 层出现 |
| `feasibility` | 当前模型是否可能处理某类结构化空间输入 |
| `observed_effect` | 空间变量与行为之间已被系统论文观察到某种关系 |
| `mechanism` | 空间为何影响行为，涉及因果机制或解释 |
| `transferable_hypothesis` | 来自 Foundational corpus 的命题可迁移为后续研究假设 |
| `boundary_positioning` | 某类系统为什么是 bridge / Adjacent / reserve / excluded |
| `agenda` | 未来应如何设计表征、实验与评估 |

---

## 4. Claim Matrix

| Claim Type | Minimum Evidence Required | Allowed Language | Disallowed Language |
|-----------|---------------------------|------------------|---------------------|
| `descriptive_mapping` | Core corpus 的结构化编码；必要时显式区分 `anchor_core` / `bridge_core` | `coded systems show`, `the evidence map indicates`, `within the widened core`, `anchor-core cases mostly` | `the field has proven`, `it is established that` |
| `distribution_gap` | Core corpus 的 coverage 统计 + 明确编码规则 + 当前 widened/strict 边界说明 | `appears underexplored`, `remains sparse`, `is absent from the strict anchor core`, `appears only in a single widened bridge case` | `does not work`, `has been rejected`, `is no longer a gap` |
| `feasibility` | Adjacent corpus + 与 Core 最近邻工作 + 明确非 direct-effect 提醒 | `benchmarks suggest`, `may be able to process`, `is consistent with feasibility`, `supports an input-side possibility` | `models understand configuration`, `LLMs have solved configurational reasoning` |
| `observed_effect` | Core corpus 中 `observed_effect` 条目；若依赖 bridge，需明示 | `some systems report`, `observed in limited settings`, `a subset of widened-core cases reports`, `reported association` | `space generally determines`, `space robustly shapes`, `the literature demonstrates` |
| `mechanism` | 多来源综合且有直接测试；通常本综述中证据不足 | `possible mechanism`, `one interpretation is`, `remains unresolved whether` | `the mechanism is`, `this shows causal mediation` |
| `transferable_hypothesis` | Foundational corpus + 与 Core gap 对照 | `suggests a hypothesis for`, `motivates testing whether`, `offers a transferable proposition` | `therefore LLM societies behave this way`, `this demonstrates the same effect in agents` |
| `boundary_positioning` | tiering rule + scope memo + 个案裁决 memo | `is treated here as boundary evidence`, `is retained only as a scope comparison`, `does not enter the stable widened core` | `is effectively core anyway`, `can be read as equivalent evidence` |
| `agenda` | gap analysis + claim discipline + evaluation needs | `future work should test`, `a promising direction is`, `evaluation may require` | `the next step is obvious`, `this method should be adopted as standard` |

---

## 5. Evidence-Status Rules

| Evidence Status | What It Can Support | What It Cannot Support |
|----------------|---------------------|------------------------|
| `observed_effect` | 有限的 system-level effect claim；可写“在若干系统中观察到” | 普遍性结论、稳健机制结论 |
| `designed_affordance_only` | 架构描述；可写“系统被设计为让空间参与行为生成” | “空间已影响行为”的 empirical claim |
| `hypothesized_but_not_tested` | agenda、future work、transferable hypothesis | 当前系统已有支持的效果结论 |

补充规则：

- `observed_effect` 也不等于强因果，只表示论文报告了某种空间-行为关联或差异
- 如果一个结论同时依赖 `observed_effect` 与 `designed_affordance_only`，应按更弱口径写

---

## 6. Corpus and Layer Rules

### 6.1 `anchor_core`

`anchor_core` 可以支撑：

- 最强的 descriptive mapping
- 最干净的 strict-gap 叙述
- 最谨慎的 limited `observed_effect` claim

`anchor_core` 不自动支撑：

- 机制结论
- 跨系统普遍规律
- 对 `L2 / L4 / L5` 丰富覆盖的乐观表述

优先表述：

- `in the strict anchor core`
- `among anchor-core systems`
- `the strict baseline shows`

### 6.2 `bridge_core`

`bridge_core` 可以支撑：

- widened-Core 分布讨论
- bridge-level descriptive mapping
- 有限定语的 bridge-level `observed_effect` discussion

`bridge_core` 不应单独支撑：

- 强机制论断
- field-level generalization
- “该表示层已经被系统性验证”的写法

优先表述：

- `within the widened core`
- `bridge-core cases suggest`
- `widened-core cases indicate`
- `socially situated bridge cases show`

### 6.3 `Adjacent`

`Adjacent` 只支撑：

- `feasibility`
- boundary discussion
- 输入处理能力的最近邻参照

`Adjacent` 不支撑：

- 社会行为 effect claim
- `L4 gap` 的实现覆盖结论
- Core evidence map 的分布统计

### 6.4 `Foundational`

`Foundational` 只支撑：

- 理论背景
- transferable hypotheses
- boundary conditions

`Foundational` 不支撑：

- 对 LLM multi-agent systems 的直接 empirical claim

正文中引用 Foundational corpus 时，优先使用：

- `in physical-space studies`
- `Space Syntax literature suggests`
- `this motivates testing whether`

避免使用：

- `agents therefore`
- `LLM systems thus`

### 6.5 Boundary / Reserve Cases

以下对象只能用于 boundary positioning，不能回流为主证据：

- `TW-02`：scope-boundary 对照，不纳入 stable widened-Core
- `HC01`：Adjacent / feasibility / boundary evidence
- reserve 或 borderline cases：除非明确升级写入 stable coding rows，否则不进入正文主结论

---

## 7. Representation-Specific Rules

### 7.1 `L4`

允许写：

- `L4 remains absent from the strict anchor core`
- `L4 appears only in a single widened bridge case`
- `configurational agent-facing representation remains highly underexplored`

不允许写：

- `the L4 gap is solved`
- `the field now covers L4`
- `L4 has been demonstrated in social simulation`

### 7.2 `L5`

允许写：

- `L5 appears in a limited subset of widened-core cases`
- `some systems provide richer geometry or embodiment, but this does not by itself establish configurational social effects`

不允许写：

- `3D environments solve the representation problem`
- `L5 evidence validates spatial-social mediation`

### 7.3 `L2`

允许写：

- `the recovered L2 slice is mainly bridge-core interactional evidence`
- `L2 coverage improves under widening but remains concentrated in specific bridge settings`

不允许写：

- `L2 is broadly established across the field`

---

## 8. Allowed and Disallowed Sentences

### 8.1 Allowed

- `Most anchor-core systems expose agent-accessible spatial information at L1-L3 rather than at configurational level.`
- `Configurational input remains absent from the strict anchor core and appears only in a single widened bridge case.`
- `Adjacent benchmark evidence suggests that current models may process some topological structure, though this does not yet establish social-behavior effects.`
- `Space Syntax findings in physical environments motivate testable hypotheses for future LLM multi-agent studies.`
- `Within the widened core, bridge cases broaden L2 and L5 coverage, but they do not erase the strict-gap interpretation.`
- `TW-02 is retained only as a scope-boundary comparison and does not enter the stable widened core evidence map.`

### 8.2 Disallowed

- `Current evidence shows that spatial configuration shapes LLM-agent social behavior.`
- `The L4 gap has now been filled by widened-core evidence.`
- `Because Space Syntax predicts encounter patterns in buildings, the same mechanism applies to LLM agents.`
- `Spatially aware models already demonstrate socially valid configurational reasoning.`
- `Bridge-core evidence proves that the field has moved beyond local spatial representations.`

---

## 9. Section-by-Section Guardrails

| Section | Strongest Safe Claim |
|--------|----------------------|
| `§1 Introduction` | 邻近 survey 空间已拥挤，但 `agent-accessible spatial representation -> social behavior` 的 WHERE gap 仍未被中心化 |
| `§2 Space Syntax Primer` | 物理空间文献提供可迁移命题与解释变量来源，不提供 agent direct evidence |
| `§3 Evidence Map` | 描述系统覆盖、表示分布、anchor/bridge 分层、strict vs widened gap |
| `§4 Feasibility` | 结构化输入“可能可处理”，而非已被社会模拟验证 |
| `§5 Social Simulation` | 说明空间目前如何被使用、哪些 effect evidence 存在、哪些仍停留在局部或 bridge 层 |
| `§6 Evaluation` | 提出候选维度与控制需求，不声称已有标准答案 |
| `§7 Agenda` | 提出可测试假设和研究方向，不预设机制已经成立 |

---

## 10. Pre-Submission Checklist

在写完每个 section 后检查：

1. 这句话是在描述文献分布，还是在宣称 empirical effect？
2. 如果是 effect claim，它是否只基于 `observed_effect` 条目？
3. 这句话依赖的是 `anchor_core`、`bridge_core`、`Adjacent` 还是 `Foundational`？
4. 我有没有把 widened-Core 说成 strict baseline？
5. 我有没有把物理空间实证或 Adjacent 能力结果直接嫁接成 agent social-effect 结果？
6. 如果把句子里的动词从 `suggests/may/appears` 改成 `shows/proves/demonstrates` 会不会过头？

如果答案是“会”，就说明当前句子已经太强。
