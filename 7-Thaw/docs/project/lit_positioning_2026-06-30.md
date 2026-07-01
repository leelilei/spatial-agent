# Thaw 新颖性门槛检索（2026-06-30）

## 结论

**Thaw 不能把“遗忘并非缺陷、适度遗忘有益”作为新颖性主张。** 这个宽泛命题已经被
认知科学、持续学习、单智能体 memory management 和带历史衰减的 opinion dynamics 覆盖。

当前检索尚未发现直接完成以下组合的工作：

> 在自然对话的 LLM 多智能体社会中，让错误事实先形成稳定的社会吸引子，再操纵个体记忆
> 衰减，测量原本失败的晚期权威纠正是否重新生效，并刻画个体遗忘与社会复述强化之间的
> 相边界。

因此 Thaw 可以继续，但必须收窄到 **decay × social rehearsal × delayed correction**，而不是
一般性的“forgetting helps”。

## 四个命题的检索判断

| Thaw 命题 | 判断 | 主要邻居 |
|---|---|---|
| H1：遗忘使晚期纠正重新生效 | **暂未发现直接 LLM-society 实证** | STALE 研究单 agent 过期状态修订；Delayed Verification 研究纠正延迟但不操纵遗忘 |
| H2：static attractor → belief re-flow | **理论上不新，LLM 社会实证可能新** | 经典 opinion dynamics 已研究历史记忆、衰减、稳定性和动态状态 |
| H3：遗忘同时增加攻击面 | **邻近工作拥挤** | Forget to Improve、memory poisoning / governance 已研究陈旧或恶意记忆的淘汰与攻击 |
| H4：存在“健康遗忘”倒 U 区间 | **宽泛稳定—可塑性权衡不新；本设置下的相图可能新** | cognitive alignment、continual learning、历史衰减 opinion models |

## 最重要的直接邻居

### 1. Forgetting as a Feature (2026)

把 LLM 的指数遗忘解释为功能性认知机制，而非纯缺陷。它直接占据“forgetting can help”
这一口号，但不是多智能体传播、社会固化或延迟纠正实验。

### 2. Oblivion (2026)

用 decay-driven activation 控制单 agent 的读写记忆，在动态长程任务中平衡学习与遗忘。
它占据“Ebbinghaus decay for adaptive agent memory”，但没有 collective belief、social rehearsal
或 late-correction recovery。

### 3. STALE (2026)

研究后续观察隐式使旧记忆失效时，agent 能否解析当前状态、抵抗 stale premise 并调整行为。
它与“旧事实阻碍更新”最接近，但单位是单 agent 的状态修订，不是社会传播形成的吸引子。

### 4. How Memory Management Impacts LLM Agents (ACL 2026)

系统研究记忆增加/删除和 experience-following，指出错误经验会传播并复用。它说明“删记忆
可以减少错误继承”并非新颖机制，但没有延迟纠正或群体动力学。

### 5. Forget to Improve (2026)

用 value-minus-harm-per-byte 选择保留、共享和信任的经验，在 task drift、poison 和 stale
memory 下提高性能。它直接占据工程性的“forgetting improves agents”，但属于有监督价值淘汰，
不是无标签的自然衰减，也不研究社会错误吸引子。

### 6. Opinion dynamics with memory (Boschi et al., 2019)

研究社会如何通过带衰减的交互耦合形成 collective memory，并分析外部信号撤除后的保持与
回忆。它说明 memory-driven attractor / decay 的理论语言已有先例。

### 7. Historical-opinion HK model (2026)

显式讨论衰减率在历史惯性与对新信息适应性之间的平衡；高衰减让群体更敏感，也更易受短期
影响。这与 H4 的概念骨架接近，因此 Thaw 不能把“适度遗忘平衡稳定与适应”本身写成首创。

## 新的可守贡献

### 从“遗忘有益”改为“社会复述决定遗忘是否能解冻”

遗忘只作用于个人并不保证旧信念消失，因为邻居会不断把旧版本重新写回。真正的控制量不是
`forget_rate` 单轴，而是两个竞争速率：

- **individual decay**：旧记忆从个人可访问状态消退；
- **social rehearsal**：旧版本被邻居再次说出并重新强化。

因此首个实验应检验二维相图：

`forget_rate × stale-rehearsal / communication rate → late-correction recovery`

可能出现三种区域：

1. **Frozen**：社会复述快于遗忘，旧值持续固化；
2. **Thawed**：遗忘足以侵蚀旧值，晚期纠正可以接管；
3. **Amnesic**：遗忘过强，新旧信息都无法维持。

若只观察到单调下降，Thaw 退化为普通 memory-decay 工程，应停止。若观察到稳定的
Frozen → Thawed → Amnesic 区域，才构成值得继续的核心现象。

## 实验门槛

1. **先建立有效的零遗忘失败基线。** Telephone 的旧 late-broadcast 条件实际未注入，已撤回；
   新 H1 应使用晚期单一权威源等社会传播条件，不能用全体即时覆盖。
2. 晚期纠正 dose 和时间固定，只改变遗忘；否则无法归因于 thaw。
3. 同时记录旧值的社会复述次数，避免把效果误写成纯个体记忆机制。
4. 终点正确率不够：至少报告 recovery latency、belief churn 和纠正后保持时间。
5. 在扩大 n 之前，先证明至少存在一个非单调或相变式候选信号。

## Primary sources

- Boschi, Cammarota, Kühn, *Opinion dynamics with memory: how a society is shaped by its own
  past*, arXiv:1909.12590.
- *Forgetting as a Feature: Cognitive Alignment of Large Language Models*, arXiv:2601.09726.
- Rana et al., *Oblivion: Self-Adaptive Agentic Memory Control through Decay-Driven Activation*,
  arXiv:2604.00131.
- Chao et al., *STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?*,
  arXiv:2605.06527.
- Xiong et al., *How Memory Management Impacts LLM Agents*, ACL 2026.
- Wu et al., *Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated
  Memory*, arXiv:2606.25115.
