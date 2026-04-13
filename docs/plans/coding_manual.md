# Survey Coding Manual

适用对象：`survey_plan_v4.md` 对应的 scoping review  
版本：v1  
日期：2026-04-11

---

## 0. Purpose

这份 manual 的作用不是替代 `survey_plan_v4.md`，而是把其中最容易在执行时漂移的规则写死，尤其是：

- `corpus` 分层
- `unit of analysis`
- `L0-L5` 判定
- 行为编码
- 质控阈值
- 模糊案例处理

如果计划文本和本 manual 冲突，以本 manual 中更具体的执行规则为准，并在 `taxonomy_change_log` 中记录原因。

---

## 1. Core Principles

1. 本文首先是 `scoping review`，不是效果验证论文。
2. `Evidence map` 的核心对象是 **Core corpus**，不是全部纳入文献。
3. `L0-L5` 只编码 **agent-accessible representation**，不编码环境后端复杂度。
4. “系统里存在空间”不等于“Agent 被提供了空间结构信息”。
5. “系统设计里包含空间 affordance”不等于“空间已被观察到影响行为”。
6. 遇到模糊案例时，先保守编码，再进入 `adjudication_memo`，不要强行做高确定性判断。

---

## 2. Corpus Tiering

### 2.1 Tier Definitions

| Tier | 定义 | 主用途 |
|------|------|--------|
| `Core` | LLM multi-agent systems，且同时具有可识别空间环境与社会行为 | `evidence map` 主编码 |
| `Adjacent` | spatial reasoning benchmarks、spatially-aware single-agent systems、与结构输入可处理性直接相关的工作 | 可行性边界 |
| `Foundational` | Space Syntax 理论、物理空间实证、经典 ABM | 理论背景与可迁移命题 |

### 2.2 Tier Decision Rules

按下面顺序判断：

1. 是否是 LLM-driven system 或直接相关 benchmark？
2. 是否存在可识别空间环境，而不是纯任务空间？
3. 是否存在社会行为或至少与空间输入处理能力直接相关？

判定：

- 同时满足 `LLM multi-agent + spatial environment + social behavior` -> `Core`
- 不满足社会行为，但直接回答“模型能否处理空间/结构输入” -> `Adjacent`
- 不直接属于 LLM agent，但提供理论或物理空间实证基础 -> `Foundational`

### 2.3 Edge Cases

- 单 Agent 3D 导航系统：默认 `Adjacent`
- 传统 ABM：默认不纳入；只有在用于 Space Syntax 或社会结构背景时作为 `Foundational`
- 代码协作、辩论、会议室类纯任务空间：排除
- 有地图但没有任何社会互动的 game agent：通常 `Adjacent` 或排除，不进 `Core`

---

## 3. Unit of Analysis

### 3.1 Default Rule

- `Bibliographic screening` 以 `paper` 为单位
- `Evidence map` 以 `system / environment configuration` 为单位

### 3.2 Split vs Merge

对同一 `system family` 下的新论文，按以下规则决定 `merge` 还是 `split`：

**Split**，如果出现任一情况：

- `agent-accessible representation` 发生变化
- `environment-side representation` 发生结构性变化，且影响 Agent 可获得的信息
- 空间环境配置明显不同，足以改变社会行为机会结构
- agent 数量级、交互机制或行为目标发生显著变化
- 评估对象从局部行为转向宏观社会结构，或反之

**Merge**，仅当以下条件同时成立：

- 同属一个 `system family`
- 核心空间表征方式未变
- 环境配置变化不影响本文关心的空间-行为关系
- 新论文主要是结果补充、规模扩展或实现细节更新

### 3.3 Operational Rule

对每个家族新条目，先问：

1. 它的 `agent-accessible representation` 和旧版本一样吗？
2. 它的空间环境配置是否让行为机会结构变了？
3. 它的行为分析尺度是否变了？

若任一问题答案为“是”，优先 `split`；若均为“否”，再考虑 `merge`。

**默认偏保守**：不确定时先 `split`，并在 `system_family` 字段中保留家族关系。

---

## 4. Field-by-Field Coding

### 4.1 Basic Fields

| Field | Rule |
|------|------|
| `system_name` | 记录具体系统或配置名 |
| `system_family` | 记录家族名，用于去重和演化追踪 |
| `paper_refs` | 挂接所有直接支持该编码的论文 |
| `year` | 以当前编码配置对应论文年份为准 |
| `agent_count` | `1 / 2-10 / 10-100 / 100+` |

### 4.2 Environment-Side Representation

| Value | Meaning |
|------|---------|
| `text-only` | 环境本身以文本状态存在 |
| `2D_grid` | 离散网格世界 |
| `2.5D_isometric` | 伪 3D 或等轴环境 |
| `3D_engine` | 完整 3D 模拟环境 |
| `graph_based` | 环境主要以图结构组织 |

### 4.3 Agent-Accessible Representation: L0-L5

`L0-L5` 只看 Agent 实际收到什么，不看环境后端本来有多复杂。

| Level | Rule |
|------|------|
| `L0` | 无任何位置或环境描述 |
| `L1` | 有地点名/区域标签，但无空间关系 |
| `L2` | 有地点自然语言描述，但无拓扑结构 |
| `L3` | 有邻接、可达或在场信息 |
| `L4` | 有全局拓扑构型指标，如 `integration/depth/control/choice` |
| `L5` | Agent 实际获得几何/坐标/视域/物理约束等完整几何信息 |

### 4.4 L0-L5 Decision Sequence

按以下顺序判断：

1. Agent 输入里有没有任何空间信息？
2. 如果有，是只有地点标签，还是还有语义描述？
3. 如果有结构，是局部邻接/在场，还是全局构型指标？
4. 如果看起来是 3D 系统，Agent 是否真的收到了几何数据，而不只是文本摘要？

**L5 防误判规则**：

- 只有当论文、prompt、API 描述或系统文档明确表明 Agent 直接接收几何信息时，才标 `L5`
- 如果 3D 环境只给人类观看，Agent 只收到文本房间描述，则按 `L1-L3` 编码

### 4.5 Representation Gap Note

以下情况必须写 `representation_gap_note`：

- 环境后端明显比 Agent 输入更丰富
- 编码依赖作者推断而非论文直接说明
- 混合型系统同时使用多种空间信息

### 4.6 Behavioral Scale

| Value | Meaning | Example |
|------|---------|---------|
| `local_action` | 个体决策层 | 移动选择、地点偏好 |
| `interaction` | 双人或小组互动层 | 对话、合作、冲突 |
| `emergent_social_structure` | 宏观涌现层 | 角色分化、规范形成、社会网络结构 |

### 4.7 Behavior Type

可多选，常见值包括：

- `dialogue`
- `cooperation`
- `conflict`
- `mobility`
- `role_differentiation`
- `norm_formation`
- `other`

### 4.8 Evidence Status

| Value | Meaning | Can Support |
|------|---------|-------------|
| `observed_effect` | 论文报告了空间与行为之间被观察到的关系 | 描述性结果与有限 effect claim |
| `designed_affordance_only` | 系统被设计成具有某种空间 affordance，但未测试其行为后果 | 架构描述，不支持 effect claim |
| `hypothesized_but_not_tested` | 作者提出空间可能影响行为，但未给出直接证据 | agenda / hypothesis only |

### 4.9 Spatial-Behavior Coupling

| Value | Rule |
|------|------|
| `none` | 行为逻辑与空间基本无关 |
| `implicit` | 空间通过场景、共现、语义背景间接作用 |
| `explicit` | 系统显式使用空间结构变量、规则或可计算空间关系 |

### 4.10 Evaluation Method

| Value | Rule |
|------|------|
| `human_eval` | 人类主观或任务评审 |
| `auto_metric` | 自动计算指标 |
| `llm_as_judge` | 以 LLM 作为评价者 |
| `mixed` | 多种方式并用 |
| `none` | 无对应评估 |

### 4.11 Space Syntax Construct

标记是否显式涉及：

- `integration`
- `depth`
- `control`
- `choice`
- 明确等价的全局拓扑结构变量

如果只是地点语义或局部邻接，不记为 Space Syntax construct。

---

## 5. Evidence Source Priority

编码证据优先级如下：

1. 论文正文中的系统输入说明
2. appendix / supplementary / prompt 示例
3. 论文配图与流程图
4. 作者仓库或项目文档
5. 编码者基于上下文的保守推断

如果编码依赖第 4-5 层证据，必须在 `representation_gap_note` 中说明。

---

## 6. Ambiguous-Case Handling

以下任一情况进入 `adjudication_memo`：

- `L2` 与 `L3` 边界不清
- 3D 环境是否应记为 `L5` 存疑
- 系统 family 是否应 `merge` 或 `split` 存疑
- 行为证据是 `observed_effect` 还是 `designed_affordance_only` 存疑

记录格式：

1. 系统名 / family
2. 争议字段
3. 可选编码 A / B
4. 支持证据
5. 最终裁决
6. 是否触发 taxonomy 定义调整

---

## 7. Quality Control Thresholds

### 7.1 Pilot Coding

用 `Generative Agents`、`Project Sid`、`SARAH` 做 pilot coding。

- 若 3 个样例中有 2 个及以上无法稳定完成 `L0-L5 + behavioral_scale + evidence_status` 编码，则 **暂停进入 Phase 1**
- 先修订 manual，再重做 pilot

### 7.2 Exclusion Recheck

- 随机抽取 15% 的排除论文二次复核
- 若翻转率 `> 10%`，则全量复核标题摘要筛选

### 7.3 External Audit

- audit sample: 5-8 个系统
- 审阅材料：原论文相关段落 + 你的编码摘录 + 当前 manual
- 记录 `raw_agreement`
- 若一致率 `< 0.8`，修订 manual 后重做 audit sample

### 7.4 Taxonomy Versioning

只要出现以下情况之一，就更新 `taxonomy_change_log`：

- 定义改动
- 判定顺序改动
- 新增边界规则
- 因具体案例触发的层级解释变化

记录格式：

- `old_rule`
- `new_rule`
- `trigger_case`
- `reason`
- `downstream_impact`

---

## 8. Minimum Deliverables Before Phase 1

进入 Phase 1 前，至少完成：

- `evidence_table_template.md`
- `coding_manual.md`
- `claim_matrix.md`
- 3 个系统的 pilot coding

若以上任一缺失，不进入大规模编码。

---

## 9. Quick Checklist

- 我编码的是 `system/configuration`，不是整篇论文吗？
- 我区分了 `environment-side` 和 `agent-accessible` 吗？
- 我把 `designed_affordance_only` 误写成 `observed_effect` 了吗？
- 我是否因为系统是 3D 就草率打了 `L5`？
- 若是模糊案例，我是否已写入 `adjudication_memo`？
