# SMGA Proposal v4 中文版

## 生成式智能体的结构化记忆

> 工作标题：**生成式智能体的结构化记忆：用于长时程规划的证据支撑社会情境**
> 简称：**SMGA**
> 版本：**0.4**
> 日期：**2026-05-19**
> 状态：在 v3 评审后收缩并强化范围的 proposal
> 与 v3 的关系：将 secondary conditions 和 metrics 减少约 30%；承诺采用一个具体的外部 benchmark，并提供一个我们自己会交付的明确 fallback；进一步明确 SMGA 与 graph-memory baseline 的操作性差异；具体化 `Schema_emergent` 协议；加入分阶段执行计划；加入 *partial success* 成功层级；加入开放科学与 IRB 承诺。

---

## 0. 一句话版本

SMGA 研究的是：**GA-style memory stream 加 reflection 是否足以支持长时程、历史依赖的社会行为**。本文提出一个结构化记忆框架，将 episodic experiences 和开放式 reflections 转换为**类型化、实体锚定、证据验证、可用于规划的社会情境**。

核心问题是：

> 在控制 compute、prompt、schema 和 memory content 的前提下，LLM generative agents 是否能够维护关于人、地点、关系、活动、routine、norm 和 information state 的结构化社会记忆，并使用这些记忆改进未来的规划与行为？

---

## 1. v4 的主要变化

v3 已经回应了 v2 的主要问题，包括 novelty boundary、schema circularity、compute confound、situated-cognition framing、evidence-grounding reliability、causal attribution 和 external benchmark。v3 评审后仍有六个残留问题，v4 分别处理如下：

| 残留问题 | v4 修改 |
|---|---|
| **R1 范围可行性**：9 conditions × 4 schemas × ≥2 models × ≥50 seeds × 2 benchmarks 不可交付 | §8 将 conditions 分为 **Primary / Secondary / Exploratory**；§17 加入带 go/no-go gates 的**分阶段执行计划** |
| **R2 SMGA vs `GraphMemory_social_schema` 看起来像评估差异，而不是架构差异** | §19 加入**操作性差异表**：用 required fields、contracts 和 interfaces 区分 SMGA 与 graph memory |
| **R3 `Schema_emergent` 协议过薄** | §18 明确 emergent-schema 的完整流程：input set、prompt、run count、stability criterion、freeze point，以及与 `Schema_7` 的 overlap analysis |
| **R4 外部 benchmark 承诺仍然含糊** | §9 承诺以 **SOTOPIA-π** 为 primary，并提供一个我们会发布的 **multi-episode extension** 作为明确 fallback，不依赖第三方是否发表 |
| **R5 工程细节缺失，包括 IRB、open-source、statistical fallback** | §11.2 加入 annotator IRB 和 compensation；§13 加入更简单的 fallback mixed-effects model；§21 承诺发布 code、traces、benchmark 和 judge prompts |
| **R6 没有 partial-success 层级** | §15 加入 **partial success**：如果 4 个 primary contrasts 中有 2 个或 3 个成立，分别如何重构论文贡献 |

v4 还删除或合并了以下内容：独立的 promise tracking section 被折叠进 secondary metrics；完整 paper-structure outline 被压缩为一段；§1 到 §7 的重复表述被删减；单独的 response-to-reviewers section 被上面的 change table 替代。

---

## 2. 核心主张

> GA-style reflection 能产生有用的高层想法，但开放式 reflection 本身不是一个可靠机制，无法稳定地把社会经验转换成 evidence-grounded、reusable、planning-actionable memory。SMGA 测试的是：结构化社会记忆对象能否在 **prompted reflection**（廉价 baseline）、**budget-matched reasoning**（compute control）、**placebo memory**（interface control）和 **graph memory with social schema**（architecture control）之上，进一步改进历史依赖的社会 planning 与 behavior。

本文明确**不主张**：

```text
SMGA 是所有 LLM agents 的通用 memory SOTA。
SMGA 证明了 human-like situated cognition。
SMGA 取代 GA reflection。
SMGA 获胜只是因为它调用 LLM 更多次。
```

---

## 3. 研究缺口

### 3.1 GA 的贡献

GA 建立了一个可运行架构：`observation -> memory stream -> retrieval -> reflection -> planning -> action`。SMGA 建立在这个架构之上，并不否定它。

### 3.2 仍未解决的问题

1. **Reflection 存在，但没有 schema 约束。** GA reflections 是自然语言 thoughts；它们不要求包含 `memory_type`、`subject_entity`、`supporting_evidence_ids`、`contradicting_evidence_ids`、`validity_scope`、`planning_affordances` 或 `update_history`。因此下游 planning 无法知道一个 thought 是什么类型的 memory，也不知道应该如何使用它。

2. **Entity-indexed memory 已存在于 graph systems 中，但 behavior transfer 仍缺少测试。** 大多数 graph 和 agentic-memory systems 主要评估 retrieval 和 QA，而不是完整链条 `recall -> abstraction -> planning evidence -> action -> outcome`。

3. **Prompted reflection 可能是很强的 baseline。** “请反思 people、places、relationships、activities、routines” 这种 prompt 很便宜。如果它和 structured memory 表现相当，那么贡献就是 prompt engineering，而不是 architecture。v4 将 `M0_prompted` 作为**必需 baseline**。

4. **额外 compute 可能解释收益。** 更多 LLM calls 等于更多 thinking。v4 要求 compute-matched baselines（`M0_plus`）和 cost-normalized reporting。

5. **Evidence-grounding 不能靠模型自报。** 如果同一个 LLM 既生成 claim 又给出 evidence IDs，本质上是在给自己打分。v4 要求在人类外部验证之后，才能信任任何 LLM-judge metric。

---

## 4. 定义

一个**结构化社会记忆对象**满足四个 contract：

1. **Typed**：属于一个声明或发现出来的类别，例如 person / place / relationship / activity / routine / norm / information state。
2. **Entity-grounded**：链接到 simulation log 中的具体 entities、events、agents、places、topics。
3. **Evidence-verified**：同时保存 **supporting** 和 **contradicting** evidence IDs，这些 ID 可以由非 agent evaluator 对照 gold logs 检查。
4. **Planning-actionable**：暴露来自 controlled vocabulary 的 affordances；每个 affordance 都独立地由 evidence 支撑，而不是由 planner 自由发明。

示例：

```json
{
  "memory_id": "smem_0042",
  "memory_type": "relationship_memory",
  "subject_entity": "Klaus-Maria",
  "claim": "Klaus and Maria have a recurring informal research-discussion relationship.",
  "supporting_evidence_ids": ["chat_018", "event_043", "chat_077"],
  "contradicting_evidence_ids": ["event_091"],
  "validity_scope": {
    "time_window": "Day 1-Day 3",
    "contexts": ["cafe", "library", "research discussion"]
  },
  "planning_affordances": [
    {
      "affordance_type": "seek_contact",
      "target": "Maria",
      "suggested_context": "library or cafe",
      "supporting_evidence_ids": ["chat_018", "chat_077"]
    }
  ],
  "confidence": 0.72,
  "calibrated_confidence": null,
  "created_at": "sim_day_3_18:00",
  "updated_at": "sim_day_3_18:00",
  "used_in_plans": []
}
```

关键点是，除了 `claim` 和 `confidence` 之外，**每个字段都可以对照 gold event log 审计**。这让 structured memory 变得可证伪。

---

## 5. 研究问题

v4 将 RQ 从 6 个压缩为 5 个；被删除的 RQ（cost/model dependence）改为 reporting requirement，而不是 primary question。

**RQ1：Memory formation。** 相比 GA reflection、prompted GA reflection 和 graph memory with social schema，SMGA 是否能产生更准确、证据支撑更充分的 structured social memories？

**RQ2：Schema contribution。** 提出的 schema 是否重要？还是 coarse、emergent 或 oracle schemas 能达到相同效果？

**RQ3：Planning transfer。** 在 recall 和 abstraction quality 之外，structured social memories 是否能进一步改进 planning decisions？

**RQ4：Behavioral transfer。** 使用 SMGA 的 agents 是否会采取更好的 history-dependent actions？这种变化是否由 *memory content* 驱动，而不是 interface 或 compute 导致？

**RQ5：External validity。** SMGA 是否能在外部 history-dependent social benchmark 上提升表现，而不仅仅是在自建 diagnostic 上有效？

---

## 6. 假设

每个 hypothesis 都包含一个 **primary metric**、一组**必需 contrast**（必须全部成立）和一个 **smallest effect of interest（SESOI）**。如果观察到的 effect 小于 SESOI，即便统计显著，也视为不支持该假设。

### H1：Evidence-supported structured recall

- Primary metric：`evidence-supported structured recall F1`
- Required：`M3 > M0_prompted` 且 `M3 > M0_plus`
- SESOI：相对 `M0_prompted` 绝对提升 +0.08

### H2：Valid abstraction beyond prompted reflection

- Primary metric：`human-verified abstraction validity`
- Required：`M2 or M3 > M0_prompted` 且 `M2 or M3 > GraphMemory_social_schema`
- SESOI：相对两个 baseline 中更强者绝对提升 +0.10

### H3：Evidence-supported planning

- Primary metric：`evidence-supported planning rate`
- Required：`M3 > M3_placebo` 且 `M3 > M0_prompted`
- SESOI：相对 `M0_prompted` 绝对提升 +0.10

### H4：Behavior change driven by memory content

- Primary metric：`target-consistent behavior rate`
- Required：`M3 > M3_placebo` 且 `M3 > M0_prompted`
- SESOI：相对 `M0_prompted` 绝对提升 +0.08
- 这是最强的 hypothesis。`M3 > M3_placebo` 是 **memory-content sensitivity** 测试。

### H5：External benchmark improvement

- Primary metric：SOTOPIA-π multi-episode extension 上的 `history-dependent social task success`（见 §9.1）
- Required：`M3 > strongest baseline`
- SESOI：normalized score +0.05

---

## 7. 架构

四个可 ablate 的层级。

**L1 Episodic memory。** GA-compatible memory stream（event_id、text、time、actors、location、activity、topic、valence）。

**L2 Entity indexing。** 每条 episodic memory 按 people、places、relationships、activities、routines、norms、information states 建立索引。Indexing 本身不是主要贡献，而是一个必要中间条件（`M1_indexed`）。

**L3 Typed social abstraction。** 按 §4 定义生成 structured memory objects。v4 不再把单一 schema 呈现为 canonical；schema 本身成为实验变量（§8.2）。

**L4 Planning-actionable memory。** Planning 接收 structured memory candidates，并附带 supporting 和 contradicting evidence。Planner output 必须记录 `chosen_action`、`used_memory_ids`、`supporting_evidence_ids`、`negative_evidence_ids`、`rejected_memory_ids`、`rationale`、`outcome`。Affordances 来自 controlled vocabulary（§12）。

---

## 8. 实验条件（分层）

v4 将 conditions 分层，以保证 scope 可控。Primary conditions 在两个 benchmarks 上用完整 seed budget 运行。Secondary conditions 只在 diagnostic 上运行。Exploratory conditions 只在 pilot scale 上运行。

### 8.1 Primary conditions（必须全规模运行）

| Condition | 描述 | 目的 |
|---|---|---|
| `M0_GA` | GA-style memory + reflection | classic baseline |
| `M0_prompted` | GA reflection prompt 明确要求反思 people / places / relationships / activities / routines / norms / information | cheap-prompt control |
| `M3_actionable` | 完整 SMGA（L1+L2+L3+L4） | main treatment |
| `M3_placebo` | M3 interface，但使用随机或无关 memory content | memory-content control |
| `GraphMemory_social_schema` | 带 social schema 的 graph memory，但没有 SMGA planning interface | 相对 A-MEM-style 的 architecture control |

**这 5 个是最小可发表条件集。** 所有 primary hypotheses 都由这些 conditions 之间的 contrasts 判定。

### 8.2 Secondary conditions（只在 diagnostic 上、reduced seeds）

| Condition | 目的 |
|---|---|
| `M0_plus` | reflection frequency / token budget / call count 与 M3 匹配，是 compute control |
| `M1_indexed` | 测试 indexing alone 是否解释收益 |
| `M2_typed` | 隔离 typed abstraction 与 planning interface 的作用 |
| `GraphMemory_generic` | 没有 social schema 的 graph structure |

### 8.3 Schema ablation（secondary）

| Schema | 描述 |
|---|---|
| `Schema_4` | coarse：person、place、relation、event |
| `Schema_7` | proposed：person、place、relationship、activity、routine、norm、information |
| `Schema_emergent` | LLM 从 held-out logs 中提出 types，并在 evaluation 前冻结（§18） |
| `Schema_oracle` | human 在看过 task family 后设计，作为 upper-bound only |

### 8.4 Held-out experience types

为了防止 benchmark-schema circularity，以下 social patterns 会从 schema examples 和 Phase-1 templates 中**保留不用**：

```text
triadic mediation
indirect reputation transfer
failed promise
shared secret
norm violation
repair after conflict
```

每个 Phase-2 evaluation 至少包含一个 held-out type。预注册内容包括：哪些 types 用于 train，哪些作为 held out，并在任何 model run 之前锁定。

---

## 9. Benchmark 策略

### 9.1 外部 benchmark：已承诺

**Primary external benchmark：** `SOTOPIA-π multi-episode extension`（SOTOPIA-π-ME）。

如果投稿时已有公开的、更广的 *Lifelong-SOTOPIA* benchmark，则使用它。否则 SOTOPIA-π-ME 是**本项目的 deliverable**：我们将 SOTOPIA-π scenarios 扩展为每个 scenario 3 到 5 个 paired episodes，其中第二个及之后的 episodes 需要使用第一个 episode 的 interaction history（commitments、relationships、conflicts、information ownership）。我们会随论文发布这个 extension。

这消除了 v3 的 hedge：外部 benchmark 无论如何都会存在，因为我们会自己交付。

符合条件的 task subsets 重点包括：

```text
remembering prior interactions
tracking promises and commitments
adapting to changed relationships
using prior conflict or cooperation
maintaining persona-consistent social history
```

### 9.2 Diagnostic benchmark

自建 benchmark，用于 mechanism validation、schema ablation、placebo controls、provenance checking 和 behavioral probes，**不用于 headline SOTA claims**。

规模：

```text
agents: 6-10
locations/contexts: 6-10
simulation length: 3-5 days
seeds: minimum 50 for primary contrasts
phase 1 (controlled exposure) + phase 2 (planning/behavior probes)
```

Phase-1 safeguards：event templates 在任何 model run 之前生成；held-out types 不出现在 templates 中；包含 distractor events；同一个 event log 会在不同 memory conditions 中 replay，以支持 paired comparison。

---

## 10. Metrics（合并版）

### 10.1 Recall and memory quality

`structured recall F1`、`unsupported memory claim rate`、`hallucinated provenance rate`、`contradiction awareness rate`、`calibration error`

### 10.2 Abstraction quality

`abstraction validity`（human-verified）、`overgeneralization rate`、`schema assignment accuracy`、`held-out type generalization`

### 10.3 Planning quality

`evidence-supported planning rate`、`negative-evidence use rate`、`memory-content sensitivity (M3 vs M3_placebo)`、`prompted-baseline gain (M3 vs M0_prompted)`

### 10.4 Behavior

`target-consistent behavior rate`、`history-dependent task success`、`relationship-consistency score`、`social coherence rating`（blinded，condition-hidden）

### 10.5 Cost（每个表格都必须报告）

`input/output tokens`、`LLM calls`、`wall-clock latency`、`cost-normalized success`

**从 v3 删除：** 独立的 promise-follow-through section。Promise tracking 现在只是 10.4 中的一个 secondary metric，只有当 detection pipeline 通过 §11 的 agreement threshold 后才验证。

---

## 11. Evidence-Grounding 协议

### 11.1 为什么需要这一点

一条 memory 可能引用了一个存在的 evidence ID，但该 evidence 实际并不支持对应 claim。让 LLM judge 去评估其他 LLM 的 provenance 会叠加问题。因此 evidence-grounding 必须在 agent 外部、judge LLM 外部，通过 gold event log 和 human annotation 进行验证。

### 11.2 Human annotation

最低要求：

```text
sample size: ≥ 200 memory/planning claims, stratified across conditions and memory types
labels: supports / contradicts / irrelevant / insufficient
annotators: ≥ 2 independent, blinded to condition
agreement target: Cohen's κ ≥ 0.6 on a 50-claim pilot before scaling
```

**IRB 与 compensation。** Annotators 通过本机构 IRB-approved protocol 招募，用于 non-clinical text annotation。报酬不低于当地 minimum wage equivalent。Annotation guidelines、examples 和 edge cases 会作为 supplementary material 发布。

### 11.3 LLM judge validation

LLM judges 只会在人类-LLM agreement 已经在 pilot set 上验证后，才用于 scale-up。报告内容包括：human-LLM agreement（κ）、disagreement analysis、support detection 的 precision/recall、hallucinated-provenance detection rate。

如果 human-LLM κ < 0.5，则 LLM-judge metric 降级为 exploratory。

### 11.4 Calibration

Raw confidence 会被记录，但 headline metrics 使用 **calibrated** confidence。Calibration map 在 dev set（1000 claims）上拟合，并在 test 前冻结。每个 condition 都报告 expected calibration error。

### 11.5 Negative evidence

每个 structured memory 和每个 planning trace 都记录 `contradicting_evidence_ids` / `negative_evidence_ids` / `rejected_memory_ids`。如果一个 plan 只引用 supporting evidence，同时忽略 log 中强 contradictory evidence，则标记为 **biased evidence use**，这是一个独立于 “unsupported” 的 metric。

---

## 12. Planning Affordances

Free-form affordances 会爆炸；fixed lists 又会限制 generalization。v4 使用一个**混合 controlled vocabulary**：

```text
seek_contact · avoid_contact · seek_information · share_information
repair_relationship · maintain_privacy · choose_collaboration_context · follow_commitment
```

Primary metrics 只评估这个冻结 vocabulary。允许 open-extension affordances，但只作为 exploratory analysis 单独记录。

Affordances 由 structured memory 通过 constrained prompts 或 rule templates 生成；trace 会记录每个 affordance 是 `rule-derived` / `LLM-derived under constrained vocabulary` / `human-validated`。

---

## 13. Statistical Analysis

### 13.1 Unit of analysis

Paired seeds：相同 agent profiles、initial states、scripted event log、task prompts、model configuration，唯一变化是 memory architecture。

### 13.2 Primary mixed-effects model

```text
outcome ~ condition + task_type + schema_condition + model_family
        + (1 | seed) + (1 | agent) + (1 | scenario)
```

### 13.3 Fallback model

在 50 seeds × 8 agents × 约 6 scenarios 的设置下，三个 crossed random effects 可能无法收敛。**预注册 fallback** 顺序如下：

1. 如果 scenario variance 出现 singular fit，则删除 `(1 | scenario)`。
2. 如果仍然 singular，则删除 `(1 | agent)`，并在 agent level 使用 cluster-robust SEs。
3. 如果仍然 singular，则切换为 seed-level aggregated metrics 上的 paired-difference tests，并对 4 个 primary contrasts 使用 Holm correction。

选择 primary 还是 fallback 只由 convergence diagnostics 决定，而不是由 effect size 决定，并在 results 中记录。

### 13.4 Main contrasts（family 内 FDR-controlled）

```text
M3 > M0_prompted        (cheap-prompt test)
M3 > M0_plus            (compute test, secondary scale)
M3 > M3_placebo         (memory-content test)
M3 > GraphMemory_social_schema   (architecture test)
```

---

## 14. Model Dependence and Cost

### 14.1 Model plan

Required：一个 frontier API model，一个 strong open-weight model。Optional：一个 smaller open model 作为 stress test。

每个 model 都报告：gains 是否复现；structured memory 对 weaker models 的帮助更强还是更弱；weaker models 是否主要受 schema-following failures 限制。

如果只有 frontier model 显示 gains，则 claim 收缩为：*SMGA improves structured memory use for strong instruction-following LLM agents; model generality is limited.*

### 14.2 Cost

每个 result table 都报告 cost（tokens、calls、latency、storage）以及 raw performance，并加入 cost-normalized column。Interpretation guide：

| Pattern | Interpretation |
|---|---|
| SMGA better and cost-normalized better | strong architecture result |
| SMGA better but cost-normalized worse | trade-off；当 reliability/auditability 重要时有用 |
| SMGA better than M0_GA but not M0_plus | gain 来自 extra reasoning，而不是 structure |

---

## 15. Success Criteria

### 15.1 Partial success（v4 新增）

如果 4 个 primary contrasts（H1-H4）中有 2 个成立，论文围绕成立的部分重新 framing：

| 成立的 pattern | Reframing |
|---|---|
| H1 + H2 only | “structured memory as a high-fidelity, auditable representation of social experience”：recall/abstraction contribution，撤回 behavioral claim |
| H2 + H3 only | “structured memory improves planning-rationale quality”：撤回 behavior claim，但对 simulation 和 audit 有用 |
| H3 + H4 only | “structured memory affects behavior even when recall is comparable”：abstraction claim 降为 secondary |
| H4 alone with H1-H3 null | 可能存在 confound；结果重构为 exploratory；不提交 main paper |

Partial success 是可发表的；partial + H5 是 strong paper。

### 15.2 Minimum success

H1 + H2 成立，并且都要同时优于 `M0_prompted` 和 `GraphMemory_social_schema`。低于这个标准，architecture claim 不被支持。

### 15.3 Strong success

H1 + H2 + H3 + H4 对所有 required baselines 都成立。

### 15.4 SOTA-level success

Strong success **加上** H5 在 external benchmark 成立，**加上** cost reporting，**加上** validated judge reliability。

可接受的 claim 形式是：*SMGA achieves state-of-the-art performance on history-dependent social memory tasks under the evaluated benchmark and baseline set.* 不做更宽泛主张。

---

## 16. Downgrade Rules

| Result | Downgrade |
|---|---|
| `M0_prompted` matches `M3` | 贡献是 prompt-level guidance，而不是 architecture |
| `M0_plus` matches `M3` | gains 来自 extra reasoning，而不是 structure |
| `M3_placebo` matches `M3` on behavior | behavior change 是 interface effect，而不是 memory content |
| `GraphMemory_social_schema` matches `M3` | social graph memory 已经足够；SMGA 的 planning-interface contribution 不是 load-bearing |
| `Schema_4` matches `Schema_7` | fine schema 不必要 |
| `Schema_emergent` outperforms `Schema_7` | hand-engineered schema 不够优；围绕 emergent schema 重新 framing |
| Recall improves but planning does not | 只是 memory-reporting improvement |
| Planning improves but behavior does not | 只是 rationale improvement |
| Evidence IDs fail human validation | evidence-grounding claim 无效；降级为 recall-only paper |
| Human-LLM κ < 0.5 | LLM-judge metrics 仅为 exploratory |
| External benchmark fails | diagnostic-only contribution；不做 SOTA claim |
| Only one model shows gains | model-specific result |
| Cost-normalized performance much worse | reliability/audit trade-off，而不是 efficiency gain |

---

## 17. 分阶段执行计划

为回应 R1（scope feasibility），项目分三阶段执行，并设置明确 go/no-go gates。

### Stage 1：Pilot（约 6 周）

在 diagnostic benchmark 上运行 **5 primary conditions × 5 seeds × frontier model only**。验证：

- annotation pipeline（50 claims pilot 上 κ ≥ 0.6）
- planning-trace logging 是否完整且可 parse
- `M3_placebo` 是否与 `M3` 操作上明确不同（interface 中没有 information leakage）
- H1 和 H4 的 pilot effect direction

**Gate 1**：满足以下条件再进入 Stage 2：
- annotation κ ≥ 0.6
- `M3` 相比 `M0_GA` 至少在 H1 或 H4 中显示 directional improvement
- `M3_placebo` 在 H4 上**没有** match `M3`（否则即便在 pilot 阶段 architecture 也可疑）

如果 gate 1 失败，回到 design iteration，不扩大规模。

### Stage 2：Main diagnostic（约 10 周）

在 diagnostic 上运行 5 primary conditions × **50 seeds** × **2 models**（frontier + open-weight）。Schema ablations（`Schema_4`、`Schema_7`、`Schema_emergent`）只在 frontier model 上以每组 25 seeds 运行。

**Gate 2**：满足以下条件再进入 Stage 3：
- 4 个 primary contrasts（H1-H4）中至少 2 个相对 `M0_prompted` 成立，并达到 SESOI
- evidence-grounding validation 完成（§11）

### Stage 3：External benchmark + secondary conditions（约 8 周）

在 SOTOPIA-π-ME 上运行 5 primary conditions、frontier model、full seed budget。Secondary conditions（`M0_plus`、`M1_indexed`、`M2_typed`、`GraphMemory_generic`）只在 diagnostic 上以 reduced seeds 运行。

Stage 3 之后，根据达到 §15 中哪个 success tier 来决定最终 framing。

### Stage budget summary

| Stage | LLM calls（数量级） | Annotation cost | Duration |
|---|---|---|---|
| 1：pilot | ~5×10^4 | ~$1.5k | 6 weeks |
| 2：main diagnostic | ~5×10^5 | ~$4k（scaling to 200 claims） | 10 weeks |
| 3：external + secondary | ~5×10^5 | ~$2k（incremental） | 8 weeks |

这只是数量级估计；Stage 1 pilot 会测量真实 per-condition cost，然后进一步 refine。

---

## 18. `Schema_emergent` 协议（具体版）

为了去除 hand-engineering bias，v4 明确 emergent-schema 流程：

1. **Input set。** 从一个**独立于任何 evaluation run** 的 schema-development simulation 中均匀采样 200 条 episodic memories。该 schema-development simulation 的 agents 和 scenarios 与 Phase-2 probes disjoint。
2. **Prompt。** 固定 constrained prompt，要求 LLM：“Propose 5-10 memory types that organize these social experiences. For each type, give: name, one-sentence definition, 2 example claims drawn from the input. Avoid types that overlap by more than 50% in scope.” 该 prompt 会公开。
3. **Replication。** 使用 frontier model、temperature 0.7，运行 prompt **5 次**。
4. **Stability criterion。** 如果一个 proposed type 在 5 次运行中有 ≥3 次出现语义等价类型，则保留该 type。Semantic equivalence 由单独 LLM call with chain-of-thought 判断，并用 30 个 human labels 验证到 κ ≥ 0.6。
5. **Freeze。** 被保留的 types 构成 `Schema_emergent`。该 schema 在任何 Phase-2 evaluation 前冻结。Type definitions 不会在看到 evaluation data 后再编辑。
6. **Overlap analysis。** 计算 `Schema_emergent` 与 `Schema_7` 在两个层面的 Jaccard-style overlap：（a）type names；（b）example-claim assignment。无论 overlap 高低都报告，因为两种结果都有信息量。

如果 `Schema_emergent` 收敛到接近 `Schema_7`，则支持 proposed schema。如果它明显不同且表现更好，论文围绕 emergent schema 重新 framing（见 §16 downgrade rule）。如果它明显不同但表现更差，则 proposed schema 得到温和验证；我们诚实报告 schema-design risk。

---

## 19. SMGA vs Graph Memory：操作性差异

v3 review 正确指出：“planning-actionable interface” 太模糊，无法把 SMGA 和 graph memory 作为 architectures 区分开。v4 将操作性差异定义为 memory objects 上的 contract：

| Contract | Generic graph memory | `GraphMemory_social_schema`（A-MEM-like） | SMGA |
|---|---|---|---|
| Typed nodes | optional | required（social types） | required（social types） |
| Edges with relation type | yes | yes | n/a（record-based；relations 存在 `related_entities` 中） |
| **`supporting_evidence_ids`**：链接到 episodic IDs 的 required field | optional | optional | **required** |
| **`contradicting_evidence_ids`**：用于 negative evidence 的 required field | usually absent | usually absent | **required** |
| **`validity_scope`**：time window + context list | absent | absent | **required** |
| **Controlled-vocabulary `planning_affordances`** with per-affordance evidence | absent | absent | **required** |
| Planner contract：必须记录 `used_memory_ids`、`supporting_evidence_ids`、`negative_evidence_ids`、`rejected_memory_ids` | not specified | not specified | **required** |
| External provenance audit interface（gold-log checkable） | not standard | not standard | **required** |
| Update history with reason and contradiction-driven revisions | optional | optional | **required** |

Architecture claim 是：**加粗行是可测试差异**。`GraphMemory_social_schema` 原则上也可以采用这些 contracts，但当前实践中通常没有。因此，与 baseline `GraphMemory_social_schema` 比较，测的是这些 fields 和 contracts 是否是 load-bearing。

**Falsifiability：** 如果我们把加粗 contracts 加到 `GraphMemory_social_schema` 上，而它随后 match `M3`，论文将重新 framing：*贡献是 contract set，而不是 data structure。* Architecture claim 会替换为 “memory contract” claim。这个 contingency 已写入 downgrade rules。

---

## 20. Related Work（压缩版）

**Generative Agents。** 直接基础。GA 贡献了 memory stream、reflection、planning。SMGA 问的是：reflections 是否应该成为 typed、evidence-verified、planning-actionable objects，并在 behavior transfer 上受控评估。

**CoALA。** 为 language agents 提供 cognitive-architecture frame。SMGA 是一个与该框架一致的具体 memory architecture 和 evaluation protocol。

**MemoryBank, MemGPT。** 关注 long-term storage、retrieval、forgetting。SMGA 关注的是 social experiences 如何变成 structured planning context，而不是 storage capacity。

**Reflexion, Voyager。** 关注 verbal reflection 和 skill libraries，用于 future-task improvement。SMGA 的差异在于目标是 social memories、entity grounding、evidence verification 和 history-dependent social behavior。

**A-MEM, AriGraph, G-Memory, generic graph memory。** 最接近的 competitors。SMGA 不主张 novelty 来自 links、evidence 或 entity indexing 本身。增量贡献是 §19 中的 field/contract set，以及在 matched controls 下的 behavior-transfer evaluation。Headline comparison 是 **SMGA vs `GraphMemory_social_schema`**；如果 SMGA 输了，architecture claim 会撤回。

**SOTOPIA, SOTOPIA-π。** Social interaction benchmarks。SMGA 扩展到 multi-episode（SOTOPIA-π-ME），用于 history-dependent evaluation，并发布该 extension。

---

## 21. Open Science Commitment

本工作会发布：

- code（agent loop、memory architectures M0-M3、graph-memory baselines）
- diagnostic benchmark（event templates、scenarios、gold logs）
- SOTOPIA-π-ME multi-episode extension
- judge prompts and calibration data
- human annotation guidelines and the labeled validation set（200+ claims）
- per-condition planning traces（with PII review）
- analysis scripts and pre-registration of contrasts、SESOI、fallback model

使用 permissive license。Stage 2 前提交 pre-registration。

---

## 22. Remaining Risks

| Risk | Mitigation in v4 |
|---|---|
| `M0_prompted` matches `M3` | Partial-success tier（§15.1）；重新 framing 为 “prompt is enough”；不是灾难 |
| `GraphMemory_social_schema` with §19 contracts matches `M3` | 重新 framing 为 “memory contract” contribution（§19 falsifiability） |
| Scale infeasible inside the staged budget | §17 的 stage gates 在 sunk cost 扩大前停止项目 |
| Human-LLM judge agreement low | LLM-judge metrics 降级为 exploratory（§11.3）；recall metrics 仍来自 gold logs |
| External benchmark unavailable | 我们自己发布 SOTOPIA-π-ME（§9.1） |
| Statistical model non-convergent | 预注册 fallback chain（§13.3） |
| Memory-content sensitivity（`M3 > M3_placebo`）失败 | 这是**信息量最大的失败**；撤回 H4；论文重构为 recall/abstraction contribution（§15.1） |

---

## 23. Final Position

> 本研究是一项分阶段、受控的 architecture-and-evaluation study，检验结构化、证据验证的社会记忆是否能改进 GA-style agents 的 long-horizon、history-dependent planning，并且这种改进是否超越 reflection、prompted reflection、extra reasoning budget、placebo interfaces 和 graph memory with social schema。

本文最强版本并不主张 memory 已被解决。它用可证伪 contrasts 和预注册 downgrade rules，识别**什么时候 structured social memory 有用，什么时候 prompted reflection 已经足够，以及 memory object 的哪些字段对 behavior transfer 是 load-bearing 的**。

Primary make-or-break contrasts：

```text
M3 > M0_prompted        — architecture vs cheap prompt
M3 > M3_placebo         — memory content vs interface
M3 > GraphMemory_social_schema   — SMGA contracts vs graph memory
M3 > strongest baseline on SOTOPIA-π-ME   — external validity
```

如果 4 个 contrasts 中有 2 个成立且达到 SESOI，论文可以在 partial-success framing 下发表。如果 4 个全部成立，论文可以声称在所评估 benchmark 和 baseline set 下达到 history-dependent social memory 的 SOTA，并且不做更宽泛的主张。
