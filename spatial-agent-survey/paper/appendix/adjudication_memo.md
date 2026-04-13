# Adjudication Memo

日期：2026-04-13  
阶段：`Phase 0` 关闭前的 pilot adjudication 记录

本 memo 的作用不是穷尽所有模糊案例，而是把 `Phase 0` pilot 中最容易导致执行漂移的边界先写死，作为进入 `Phase 1` 之前的最小裁决集。

---

## Case 1: Generative Agents

1. System / family: `Generative Agents`
2. Contested field: `agent_accessible_representation`
3. Candidate coding A: `L2`
4. Candidate coding B: `L3`
5. Evidence:
   - 论文描述的环境对 agent 主要表现为地点名、地点功能和语义化场景描述。
   - pilot 中没有看到 agent 直接获得显式邻接图、全局拓扑结构或在场关系矩阵。
   - 行为上虽然存在丰富 social interaction，但空间结构信息仍然主要停留在语义描述层。
6. Final ruling: `L2`
7. Triggered taxonomy update: `yes`

裁决说明：

- `semantic scene description` 不能因为“对行为很重要”就上调到 `L3`。
- `L3` 必须要求 agent 明确可用邻接、可达或共在结构，而不只是地点语义。

---

## Case 2: Project Sid

1. System / family: `Project Sid`
2. Contested field: `agent_accessible_representation`
3. Candidate coding A: `L1`
4. Candidate coding B: `L3`
5. Evidence:
   - 后端环境是 rich sandbox world，但论文呈现的 agent-facing 信息以地点、事件和社会状态摘要为主。
   - 没有足够证据支持 agent 直接操作显式拓扑、路径结构或 configurational 指标。
   - 宏观社会结构和规则形成是被观察到的，但这不自动意味着空间表征层级很高。
6. Final ruling: `L1`
7. Triggered taxonomy update: `yes`

裁决说明：

- 编码必须基于 `agent-accessible representation`，不能根据引擎复杂度倒推。
- “大规模 3D / sandbox 环境” 与 “高层级空间输入” 必须严格区分。

---

## Case 3: SARAH

1. System / family: `SARAH`
2. Contested field: `agent_accessible_representation`
3. Candidate coding A: `L3`
4. Candidate coding B: `L5`
5. Evidence:
   - 后端明确为 `3D_engine`，并建模 user-relative trajectory 与 dyadic interaction。
   - 但 pilot 证据更像“结构化空间 awareness + trajectory-conditioned motion”，而不是“agent 直接操作完整几何世界状态”。
   - 当前材料不足以证明 agent 拿到了完整坐标、视域约束和连续几何状态的全量接口。
6. Final ruling: `L3`
7. Triggered taxonomy update: `yes`

裁决说明：

- `3D engine` 不等于 `L5`。
- 只有当论文明确表明 agent 自身直接接收几何/坐标/视域/物理约束等完整状态时，才允许标 `L5`。

---

## Case 4: Evidence Status Boundary

1. System / family: `Generative Agents`
2. Contested field: `evidence_status`
3. Candidate coding A: `designed_affordance_only`
4. Candidate coding B: `observed_effect`
5. Evidence:
   - 论文展示了 believable behavior 和 social interaction。
   - 但 pilot 证据没有把“空间变量如何影响行为”作为被单独隔离测试的 effect。
   - 空间被设计进入系统，不等于空间 effect 已被直接验证。
6. Final ruling: `designed_affordance_only`
7. Triggered taxonomy update: `yes`

裁决说明：

- `design != effect` 必须在 coding 和 claim 两侧同时锁死。
- 对空间相关效果的判断必须保守，不因为系统看起来“很像”就上调为 `observed_effect`。

---

## Case 5: Behavioral Scale Boundary

1. System / family: `Project Sid`
2. Contested field: `behavioral_scale`
3. Candidate coding A: `interaction`
4. Candidate coding B: `emergent_social_structure`
5. Evidence:
   - 论文报告 role differentiation、rule formation、cultural transmission。
   - 这些结果已经超过局部互动，属于宏观涌现层的社会结构现象。
6. Final ruling: `emergent_social_structure`
7. Triggered taxonomy update: `no`

裁决说明：

- 当论文明确报告群体级角色分化、规范形成或社会网络模式时，应优先记为 `emergent_social_structure`。

---

## Phase 0 Outcome

本 memo 在 `Phase 0` 关闭前锁定了 3 条必须贯彻到 `Phase 1` 的执行规则：

1. 永远编码 `agent-accessible representation`，不编码引擎渲染复杂度。
2. `semantic description`、`adjacency/co-presence`、`full geometry` 三层边界必须分开。
3. `designed_affordance_only` 不能被叙事印象误升级为 `observed_effect`。

结论：

- `L0-L5` taxonomy 已经足够 operational，可进入 `Phase 1`。
- 后续新模糊案例继续追加在本文件，不再口头裁决。
