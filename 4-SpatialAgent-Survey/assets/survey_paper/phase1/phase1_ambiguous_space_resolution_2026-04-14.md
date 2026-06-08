# Phase 1 Ambiguous-Space Resolution

日期：2026-04-14  
对象：`phase1_abstract_rereview_round1_2026-04-13.csv` 中原 `hold_ambiguous_space` 的 3 个条目  
目的：把“数字平台/多模态场景是否构成本文所需空间环境”的边界先裁定，避免后续 `screening_sheet` 与 `system-level coding` 反复返工。

---

## 裁定原则

依据 `survey_plan_v4.md` 与 `coding_manual.md`，`Core` 必须同时满足：

1. `LLM multi-agent`
2. 存在可识别空间环境，而不是纯任务场景
3. 涉及社会行为

额外强调两条约束：

- `environment-side` 的复杂度不能自动倒推成更强的 `agent-accessible` 空间输入。
- `rich setting`、`multimodal scenario` 或 `social platform` 只有在提供可识别环境结构时，才可视为空间环境；否则按 `E1` 处理。

---

## Ruling 1: OASIS

论文：`OASIS: Open Agent Social Interaction Simulations with One Million Agents`

最终裁定：

- `r1_decision = keep`
- `r1_recommended_tier = core`

理由：

- 现有扩展摘要已经不只是泛泛的“社交平台背景”，而是明确给出由 `dynamic social network`、`post information`、`recommendation filter` 和动作空间组成的数字平台环境。
- 该环境可被视为可识别的数字/图结构环境，而不是纯对话或纯任务空间。
- 论文同时报告了信息传播、群体极化和从众效应等社会行为结果，因此满足 `Core` 的三项基本条件。

保留提醒：

- 后续编码时必须把它保守记为数字/图结构环境，不要把平台后端复杂度直接上调为更高的 `agent-accessible representation`。
- 是否存在被单独检验的“空间-行为 effect”仍需后续 `evidence_status` 编码时保守处理。

---

## Ruling 2: SoMoSiMu

论文：`Unveiling the Truth and Facilitating Change: Towards Agent-based Large-scale Social Movement Simulation`

最终裁定：

- `r1_decision = exclude`
- `r1_recommended_tier = excluded`
- `r1_exclusion_reason = E1`

理由：

- 当前材料只显示它是 `Twitter-like` 社交媒体响应仿真，并带有 benchmark 组件。
- 现有摘要没有提供足够证据说明系统中存在可识别空间环境，或 agent 实际接收到可判定的空间结构输入。
- 因此它满足“社会行为”，但未满足 `Core` 所需的空间环境条件。

---

## Ruling 3: Multimodal Safety Evaluation

论文：`Multimodal Safety Evaluation in Generative Agent Social Simulations`

最终裁定：

- `r1_decision = exclude`
- `r1_recommended_tier = excluded`
- `r1_exclusion_reason = E1`

理由：

- 摘要强调的是 `multimodal/text-visual scenarios`、安全修正、一致性和 social dynamics。
- 这些表述不足以证明系统包含可识别空间环境，更不足以证明 agent 侧获得了结构化空间输入。
- `rich multimodal settings` 不能直接等同于“空间环境”，否则会把一般多模态社会场景误纳入 `Core`。

---

## 对后续流程的影响

- `hold_ambiguous_space` 已清零。
- 当前 `R1` 统计更新为：`81 keep / 1 downgrade / 27 exclude / 8 hold_missing_abstract`。
- `R1` 推荐层级更新为：`9 core / 36 adjacent / 45 foundational / 27 excluded`。
- 下一步应转向处理 `8 hold_missing_abstract`，并把本次裁定同步进正式 `screening_sheet`。
