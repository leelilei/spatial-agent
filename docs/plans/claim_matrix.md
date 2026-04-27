# Survey Claim Matrix

适用对象：`survey_plan_v4.md` 对应综述  
版本：v1  
日期：2026-04-11

---

## 0. Purpose

这份文档用来约束正文中的论断强度，避免以下常见漂移：

- 文献里“经常出现”被写成“已有强证据”
- 系统“设计上考虑了空间”被写成“空间已被证明影响行为”
- 物理空间实证被误写成对 LLM multi-agent systems 的直接证据

一句话原则：

**先区分证据来源，再区分证据状态，最后才决定能写多强的 claim。**

---

## 1. Governing Principles

1. `Frequency != strength`  
   很多系统都带空间环境，不代表空间已被证明是行为驱动因素。

2. `Design != effect`  
   系统被设计成有空间 affordance，不代表作者已经观察到空间效应。

3. `Foundational != direct evidence`  
   Space Syntax 和物理空间实证只能支撑理论与假设迁移，不能直接证明 LLM multi-agent 的行为效应。

4. `Adjacent != social effect evidence`  
   spatial reasoning benchmark 只能支撑“模型可能可处理该类输入”，不能支撑“社会行为会因此改变”。

---

## 2. Claim Types

| Claim Type | Meaning |
|-----------|---------|
| `descriptive_mapping` | 文献中有哪些系统、表示方式、行为类型、评估方式 |
| `distribution_gap` | 某类表示或研究方向在当前 corpus 中稀缺或缺失 |
| `feasibility` | 当前模型是否可能处理某类结构化空间输入 |
| `observed_effect` | 空间变量与行为之间已被系统论文观察到某种关系 |
| `mechanism` | 空间为何影响行为，涉及因果机制或解释 |
| `transferable_hypothesis` | 来自 Foundational corpus 的命题可迁移为后续研究假设 |
| `agenda` | 未来应如何设计表征、实验与评估 |

---

## 3. Claim Matrix

| Claim Type | Minimum Evidence Required | Allowed Language | Disallowed Language |
|-----------|---------------------------|------------------|---------------------|
| `descriptive_mapping` | Core corpus 的结构化编码 | `coded systems show`, `most coded systems use`, `the evidence map indicates` | `the field has proven`, `it is established that` |
| `distribution_gap` | Core corpus 的 coverage 统计 + 明确编码规则 | `L4 is absent in the coded core corpus`, `configurational input appears underexplored` | `L4 does not work`, `the field has rejected L4` |
| `feasibility` | Adjacent corpus + 与 Core corpus 最近邻工作 | `benchmarks suggest`, `current models may be able to process`, `evidence is consistent with feasibility` | `models understand configuration`, `LLMs have solved configurational reasoning` |
| `observed_effect` | Core corpus 中 `observed_effect` 条目 | `some systems report`, `observed in limited settings`, `reported association` | `space generally determines`, `space robustly shapes` |
| `mechanism` | 多来源综合且有直接测试；通常本综述中证据不足 | `possible mechanism`, `one interpretation is`, `remains unresolved whether` | `the mechanism is`, `this shows causal mediation` |
| `transferable_hypothesis` | Foundational corpus + 与 Core gap 对照 | `suggests a hypothesis for`, `motivates testing whether`, `offers a transferable proposition` | `therefore LLM societies behave this way`, `this demonstrates the same effect in agents` |
| `agenda` | gap analysis + claim discipline | `future work should test`, `a promising direction is`, `evaluation may require` | `the next step is obvious`, `this method should be adopted as standard` |

---

## 4. Evidence-Status Rules

| Evidence Status | What It Can Support | What It Cannot Support |
|----------------|---------------------|------------------------|
| `observed_effect` | 有限的 system-level effect claim；可写“在若干系统中观察到” | 普遍性结论、稳健机制结论 |
| `designed_affordance_only` | 架构描述；可写“系统被设计为让空间参与行为生成” | “空间已影响行为”的 empirical claim |
| `hypothesized_but_not_tested` | agenda、future work、transferable hypothesis | 当前系统已有支持的效果结论 |

---

## 5. Corpus-Specific Rules

### 2026-04-27 Anchor/Bridge Addendum

When the widened boundary is active, treat the main coded corpus as two layers:

- `anchor_core`: strict nucleus
- `bridge_core`: widened bridge layer inside the main coded corpus

Claim discipline under the widened boundary:

- `anchor_core` can support the strongest descriptive mapping and the cleanest limited `observed_effect` claims.
- `bridge_core` can support descriptive mapping and limited bridge-level effect discussion, but should not be treated as equal in evidential weight to the anchor nucleus.
- If a sentence relies mainly on `bridge_core`, prefer wording like `bridge cases suggest`, `widened-core cases indicate`, or `socially situated spatial systems show`.
- Do not let `bridge_core` alone support strong field-level mechanism claims.
- If `L4` appears only after the widened rule, state that clearly and do not back-project the widened definition onto earlier strict-gap claims without qualification.

### 5.1 Core Corpus

Core corpus 支撑：

- `descriptive_mapping`
- `distribution_gap`
- 有条件的 `observed_effect`

Core corpus 不自动支撑：

- 机制结论
- 跨系统普遍规律

### 5.2 Adjacent Corpus

Adjacent corpus 只支撑：

- `feasibility`
- 与第 4 节相关的边界讨论

Adjacent corpus 不支撑：

- 社会行为 effect claim
- `L4 gap` 的实现覆盖结论

### 5.3 Foundational Corpus

Foundational corpus 只支撑：

- 理论背景
- transferable hypotheses
- boundary conditions

Foundational corpus 不支撑：

- 对 LLM multi-agent systems 的直接 empirical claim

正文中引用 Foundational corpus 时，优先使用：

- `in physical-space studies`
- `Space Syntax literature suggests`
- `this motivates testing whether`

避免使用：

- `agents therefore`
- `LLM systems thus`

---

## 6. Allowed and Disallowed Sentences

### 6.1 Allowed

- `Most coded core systems expose agent-accessible spatial information at L1-L3 rather than at configurational level.`
- `Configurational input appears underexplored in the coded core corpus.`
- `Adjacent benchmark evidence suggests that current models may process some topological structure, though this does not yet establish social-behavior effects.`
- `Space Syntax findings in physical environments motivate testable hypotheses for future LLM multi-agent studies.`

### 6.2 Disallowed

- `Current evidence shows that spatial configuration shapes LLM-agent social behavior.`
- `The absence of L4 systems implies that configurational input is ineffective.`
- `Because Space Syntax predicts encounter patterns in buildings, the same mechanism applies to LLM agents.`
- `Spatially aware models already demonstrate socially valid configurational reasoning.`

---

## 7. Section-by-Section Guardrails

| Section | Strongest Safe Claim |
|--------|----------------------|
| `§3 Evidence Map` | 描述系统覆盖、表示分布、L4 gap |
| `§4 Feasibility` | 说明结构化输入“可能可处理”，而非已被社会模拟验证 |
| `§5 Social Simulation` | 说明空间目前如何被使用、何处缺乏直接 effect evidence |
| `§6 Evaluation` | 提出候选维度，不声称已有标准答案 |
| `§7 Agenda` | 提出可测试假设和研究方向 |

---

## 8. Pre-Submission Checklist

在写完每个 section 后检查：

1. 这句话是在描述文献分布，还是在宣称 empirical effect？
2. 如果是 effect claim，它是否只基于 `observed_effect` 条目？
3. 这句话引用的是 Core、Adjacent 还是 Foundational corpus？
4. 我有没有把物理空间实证直接嫁接成 agent 结果？
5. 如果把句子里的动词从 `suggests/may/appears` 改成 `shows/proves/demonstrates` 会不会过头？

如果答案是“会”，就说明当前句子已经太强。
