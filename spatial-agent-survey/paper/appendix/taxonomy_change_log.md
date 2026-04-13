# Taxonomy Change Log

日期：2026-04-13  
状态：`Phase 0` 初始化完成，后续在 `Phase 1/2` 持续追加

| date | old_rule | new_rule | trigger_case | reason | downstream_impact |
|---|---|---|---|---|---|
| 2026-04-13 | 语义化地点描述如果足够详细，可能会被编码为 `L3` | 只有当 agent 明确可用邻接、可达或共在结构时，才编码为 `L3`；纯语义场景描述编码为 `L2` | `Generative Agents` | 避免把 rich semantic context 误当作 structural adjacency | 影响 `L2/L3` 边界；要求后续编码时更重视 agent 输入结构而非行为丰富度 |
| 2026-04-13 | 大型 sandbox / 3D world 可能会被直觉性上调为空间高层级 | `agent_accessible_representation` 只能按 agent 实际接收的信息编码；复杂引擎后端不自动提高层级 | `Project Sid` | 防止从环境渲染或 world richness 反推 agent 输入结构 | 影响所有 3D/sandbox 系统；要求 `representation_gap_note` 更严格记录 backend vs agent input |
| 2026-04-13 | `3D_engine` 环境可能被直接等同于 `L5` | 只有当 agent 明确直接接收几何/坐标/视域/物理约束等完整状态时，才允许 `L5` | `SARAH` | 当前文献容易把“3D”与“full geometry access”混淆 | 影响 `L5` 判定；后续默认偏保守，防止 `L5` 膨胀 |
| 2026-04-13 | 系统看起来强依赖空间时，可能会直接标 `observed_effect` | 只有论文直接报告被观察到的空间-行为关系时，才编码为 `observed_effect`；否则优先 `designed_affordance_only` | `Generative Agents` | 需要把 design / affordance / effect 三者严格分开 | 影响 claim discipline；降低过强 effect claim 风险 |
