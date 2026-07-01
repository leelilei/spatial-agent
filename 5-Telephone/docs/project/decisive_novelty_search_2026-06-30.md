# Telephone / Thaw 决定性新颖性检索（2026-06-30）

## 决策结论

1. **宽泛的 SAY != HOLD（公开表达与私下回答不一致）不是新现象。**
   Baltaji et al. (C3NLP 2024) 已同时测量多智能体聊天中的中间表达与讨论后的私下回答，
   并明确报告部分 agent 在聊天中因同伴压力顺从、随后私下恢复原观点。
2. **Telephone 仍可能保留一个更窄、可发表的组合贡献：**
   在有客观新旧版本的时变事实上，沿自然社会传播过程分别测量 SAID 与 HELD，并显示
   权威源可以持续修复公开表达，却不能修复最终持有状态。新颖性不能再写成“首次发现
   SAY/HOLD 解离”，而应写成“事实更新传播中的 intervention-selective dissociation”。
3. **Thaw 不是完全空白，但核心因果问题暂未发现直接先例。**
   现有工作研究记忆衰减、删除、过期记忆修订和 selective forgetting；尚未发现工作把
   forgetting 作为群体信念去固化机制，并检验它是否让原本失败的晚期纠正重新生效。

## 最接近 Telephone 的直接先例

### Baltaji et al., 2024 — Conformity, Confabulation, and Impersonation

- 设计：agent 独立回答（onboarding）→ 多智能体讨论 → 再次私下回答（reflection）。
- 直接重合：比较聊天中的 intermediate opinion 与讨论后 private response；明确识别
  “公开顺从但私下未真正改变”的 peer-pressure conformity。
- 与 Telephone 的边界：该工作研究文化 persona 与主观观点，无唯一时效真值；不是长程
  telephone 式事实传播；没有比较“权威干预修复 SAID 但不修复 HELD”。
- 判断：它否定“首次区分公开表达与私下持有”的强 novelty claim，但没有完全覆盖我们的
  时变事实、传播轨迹和选择性干预结果。

### 其他邻近工作

- Choi et al., Findings ACL 2025：多智能体争论中的群体顺从和多数/高能力 agent 影响；
  重点是立场变化，不是公开—私下解离。
- Yao et al., 2025, *Peacemaker or Troublemaker*：形式化多智能体辩论中的 sycophancy；
  重点是过早共识与性能损失，不是时变事实的 SAID/HELD 轨迹。
- Ko et al., ACL 2026：系统研究社会压力、专家身份和修辞如何降低代表 agent 的客观判断；
  与权威影响邻近，但没有当前检索所见的“表达修复/持有不修复”干预对照。
- Corona Mendozza & Søgaard, ACL 2026：用激活探针研究模型内部 belief-like representation；
  概念相关，但与 Telephone 的 operational held answer 和社会传播层次不同。

## Thaw 检索结果

### 已拥挤的相邻区域

- **Oblivion (2026)：** 用 decay-driven activation 做选择性遗忘，目标是控制检索干扰和成本。
- **How Memory Management Impacts LLM Agents (ACL 2026)：** 研究记忆增加/删除、经验跟随、
  错误传播与错误经验重放。
- **STALE (2026)：** 测试新证据使旧记忆失效后，agent 是否能识别并修订过期状态。
- **Forget to Improve (2026)：** 用预算和价值/危害评分淘汰低价值、陈旧或有毒经验。

### 暂未发现的精确问题

> 在多智能体社会中，受控遗忘是否侵蚀已固化的错误吸引子，从而使原本无效的晚期真值纠正
> 重新生效；该效果是否呈倒 U 型，并伴随 static attractor → belief re-flow 的动力学转变？

上述命题与现有“提高单 agent 记忆性能/删除坏经验/识别 stale memory”有实质区别。当前检索
支持把 Thaw 视为**更空、但必须用动力学结果证明价值**的方向，而不是一般 memory-decay 工程。

## 建议动作

1. **停止把 Telephone 的 novelty 锚在 SAY != HOLD 本身。**
2. 将核心 claim 收窄为：
   **authoritative correction can repair public factual speech without repairing socially held state**。
3. 在 Telephone 中补一个与 Baltaji 2024 的正面区别表，并引用 conformity / sycophancy 邻居。
4. 不再扩展 provenance 工程线；只做足以验证上述窄 claim 的分析或实验。
5. 并行启动 Thaw 的最低成本 H1 pilot：`forget-rate × late correction`，先看是否存在真正的
   re-correction 区域；若只有单调性能下降，就尽早终止。

## Primary sources

- Baltaji, Hemmatian, Varshney (2024), *Conformity, Confabulation, and Impersonation: Persona
  Inconstancy in Multi-Agent LLM Collaboration*, C3NLP, DOI: 10.18653/v1/2024.c3nlp-1.2.
- Choi et al. (2025), *An Empirical Study of Group Conformity in Multi-Agent Systems*, Findings ACL,
  DOI: 10.18653/v1/2025.findings-acl.265.
- Yao et al. (2025), *Peacemaker or Troublemaker: How Sycophancy Shapes Multi-Agent Debate*,
  arXiv:2509.23055.
- Chao et al. (2026), *STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?*,
  arXiv:2605.06527.
- Rana et al. (2026), *Oblivion: Self-Adaptive Agentic Memory Control through Decay-Driven
  Activation*, arXiv:2604.00131.
- Xiong et al. (2026), *How Memory Management Impacts LLM Agents: An Empirical Study of
  Experience-Following Behavior*, ACL 2026.
