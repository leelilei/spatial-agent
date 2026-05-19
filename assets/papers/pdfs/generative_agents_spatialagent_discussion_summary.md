# Generative Agents 论文与 SpatialAgent 研究计划讨论总结

> 对话主题：从 Park et al. 2023《Generative Agents: Interactive Simulacra of Human Behavior》出发，理解其架构实现，并反思我们自己的 SpatialAgent / plan v13 研究设计是否成立。

---

## 1. 论文核心：Generative Agents 是什么

这篇论文提出了 **Generative Agents**：一种由大语言模型驱动、可以在沙盒环境中表现出较可信人类行为的虚拟智能体。

它不是简单地让 LLM 在每一轮“扮演一个人”，而是给 LLM 外挂一套认知架构：

```text
Generative Agent
= LLM
+ memory stream
+ retrieval
+ reflection
+ planning
+ sandbox world state
```

论文中的展示环境是 **Smallville**，一个类似 The Sims 的小镇。25 个 agent 在里面生活、行动、对话、形成关系、传播信息，并在用户只给出少量初始条件的情况下形成一些看似“涌现”的社会行为，例如情人节派对、竞选信息扩散、关系记忆等。

---

## 2. 两层系统：世界层与心智层

### 2.1 世界层：sandbox / game engine

世界层负责维护客观状态：

```text
当前模拟时间
地图结构
agent 的位置
物体状态
谁和谁在同一区域
床是否被占用
炉灶是否在燃烧
agent 当前动作
```

这部分不是 LLM 自己想象出来的，而是沙盒引擎维护的结构化状态。

### 2.2 心智层：agent architecture

心智层负责 agent 的“认知”：

```text
观察什么
记住什么
想起什么
反思什么
计划今天做什么
当前是否要打断计划
是否和别人对话
说什么
下一步去哪
```

论文中的核心心智模块是：

```text
Memory
Reflection
Planning
```

---

## 3. Memory Stream：长期记忆

Memory stream 是每个 agent 自己的长期记忆库。它记录 agent 的经历，包括：

```text
Observation: 看到或经历的事件
Reflection: 从经历中总结出的高层理解
Plan: 未来计划
```

一条 memory 通常包括：

```text
content: 自然语言描述
created_at: 创建时间
last_accessed_at: 最近访问时间
importance / poignancy: 重要性分数
embedding: 用于相关性检索
type: event / thought / chat / plan
```

示例：

```text
John talked with Eddy about his composition project.
Isabella noticed that the stove is burning.
Tom learned that Sam is running for mayor.
Klaus is dedicated to his research on gentrification.
```

### 3.1 Memory 会不会爆炸？

会。

论文和代码中的 memory stream 是持续追加式的，不是固定长度 buffer。长期运行后会面临：

```text
存储增长
检索成本增长
语义噪声增长
旧记忆干扰
```

论文的主要解决办法不是阻止 memory 增长，而是 **每次只检索一小部分相关记忆放入 prompt**。

也就是说：

```text
memory store 会越来越大
但 prompt 不会直接放入全部 memory
```

Reflection 有一定“认知压缩”作用，但它并不会删除原始 observation。因此它不是严格意义上的存储压缩。

---

## 4. Retrieval：如何从记忆中取出相关内容

论文中的 retrieval 主要结合三类分数：

```text
score = recency + importance + relevance
```

### 4.1 Recency

最近发生或最近访问过的记忆更容易被取出。

### 4.2 Importance

更重要的事情更容易被取出。代码中通常让 LLM 给事件打 poignancy 分数。

例如：

```text
brushing teeth: 低
eating breakfast: 低
asking someone on a date: 高
hearing about an election: 中高
```

### 4.3 Relevance

和当前情境更相关的 memory 会被取出。通常通过 embedding cosine similarity 实现。

---

## 5. Reflection：从流水账到高层理解

如果 agent 只有 observation，它只会记录很多碎片事件，很难形成稳定理解。

Reflection 的作用是从多条 observation 中生成高层 insight。

示例：

```text
Observation:
- Klaus went to the library.
- Klaus read papers on gentrification.
- Klaus wrote a research paper.

Reflection:
- Klaus is deeply interested in research on gentrification.
```

Reflection 生成后也会写回 memory stream，并参与后续 retrieval。

### 5.1 Reflection 触发时机

论文和代码中不是每条 memory 都触发 reflection，而是当近期事件的重要性累计超过某个阈值时触发。

代码中的默认阈值类似：

```text
importance_trigger_max = 150
```

也就是说，agent 经历足够多重要事件后才会“反思”。

---

## 6. Planning：让 agent 的行为跨时间保持一致

LLM 单步生成容易造成短期合理、长期不一致的问题。

例如：

```text
12:00 吃午饭
12:30 又吃午饭
13:00 又吃午饭
```

所以论文加入 planning。

### 6.1 日计划

一天开始时，agent 根据身份、性格、生活习惯、近期状态等生成一天的大致计划。

示例：

```text
08:00 wake up and complete morning routine
09:00 go to work
12:00 have lunch
13:00 continue work
18:00 have dinner
22:00 go to bed
```

### 6.2 递归细化

粗计划会被逐步拆细：

```text
13:00-17:00 work on composition
```

拆成：

```text
13:00 brainstorm melody ideas
14:00 draft main theme
15:00 revise harmony
16:00 take a short break
16:30 polish composition
```

再拆成更细的 5–15 分钟动作。

### 6.3 睡觉 8 小时如何实现？

agent 不是自己“睡着数 8 小时”。

真实机制更像：

```text
planner 生成：
01:00-09:00 sleeping

world clock 推进：
01:00 sleeping
02:00 sleeping
...
09:00 sleep action expires
09:00 next action: wake up
```

也就是说：

```text
planner 先生成睡眠计划
sandbox clock 负责推进时间
scheduler 检查当前 action 是否结束
到点后触发下一项行动
```

LLM 只在决策点被调用，并被告知当前时间。

---

## 7. 世界时间如何推进

系统有一个全局模拟时间，由 sandbox backend 维护。

在 repo 实现中：

```text
curr_time += sec_per_step
```

README 说明一个 game step 代表 10 秒游戏时间。

agent 的“时间感”不是内部持续意识，而是每次调用时由系统注入：

```text
It is February 13, 2023, 9:00 am.
```

所以 agent 知道时间，是因为 prompt / scratch state 里有当前模拟时间。

---

## 8. Planner 的生成时机

Planner 不是每一秒都重新生成全天计划。

主要有三种时机：

### 8.1 新一天开始

生成 day plan / hourly schedule。

### 8.2 当前 action 到期

当前 action 的 duration 到期后，系统调用 planner 确定下一项 action。

### 8.3 发生 reaction

如果 agent 感知到值得反应的事件，比如遇到别人、看到紧急状态、进入对话，则会插入一个新 action，并对当前时间块做局部重排。

### 8.4 两个 agent 对话时会进入 planner 吗？

会，但不是重新生成整天计划。

更准确地说：

```text
perceive another agent
→ retrieve relevant memory
→ decide whether to talk
→ if talk, generate conversation
→ insert chat action into both agents' schedules
→ locally rewrite affected schedule block
```

所以对话是 reaction 机制的一部分，会触发局部 re-planning。

---

## 9. Observation 如何实现

Observation 不是 LLM 自己“看见世界”，而是 sandbox world 把结构化状态转成自然语言事件。

在 repo 中，`perceive.py` 大致做：

```text
1. 根据 agent 当前 tile 和 vision_r 找 nearby tiles
2. 更新 agent 的 spatial memory tree
3. 在同一 arena 中收集附近 tile 的 events
4. 按距离排序
5. 只取 attention bandwidth 个最近事件
6. 去重：最近 retention 条已经记过的不重复写
7. 转成自然语言 description
8. 写入 associative memory
```

默认值类似：

```text
vision_r = 4
att_bandwidth = 3
retention = 5
```

因此 agent 不是全知的，也不是看到全地图，而是受到：

```text
视野半径
同 arena 过滤
注意力带宽
事件去重
距离排序
```

这些规则限制。

### 9.1 Observation 的来源

主要有三类：

```text
自己的行动
看到其他 agent 的行动
看到环境 / 物体状态变化
```

示例：

```text
John saw Eddy taking a short walk.
Isabella noticed that the stove is burning.
Tom learned that Sam is running for mayor.
```

---

## 10. Repo 真实实现中的核心结构

项目中术语和论文有一些对应关系：

```text
Generative Agent → Persona
Memory Stream → AssociativeMemory
Spatial memory → MemoryTree
Short-term state → Scratch
Simulation framework → Reverie
```

每个 persona 有三套 memory/state：

```text
s_mem: spatial memory
a_mem: associative memory
scratch: short-term runtime state
```

### 10.1 Scratch 中保存什么

Scratch 里保存 agent 当前运行时状态：

```text
curr_time
curr_tile
identity stable set
daily_req
f_daily_schedule
act_address
act_start_time
act_duration
act_description
act_event
planned_path
chatting_with
chatting_end_time
```

### 10.2 当前 action 如何结束

代码里通过：

```text
end_time = act_start_time + act_duration
if end_time == curr_time:
    action finished
```

如果正在聊天，则用 `chatting_end_time`。

---

## 11. Action 如何落到地图和对象上

当 planner 确定了当前 action description 和 duration 后，系统还会生成：

```text
action sector
action arena
action game object
emoji
event triple
object description
object event triple
```

所以一个 action 不只是：

```text
sleeping
```

而是类似：

```text
description: sleeping
duration: 480
address: house:bedroom:bed
event: (agent, is, sleeping)
object_event: (bed, is, occupied)
emoji: 💤
```

这些再被写到 maze tile 上，供其他 agent 感知。

---

## 12. 对话触发并不完全“自然涌现”

Repo 实现中，对话触发有很多硬规则。

两个 agent 能不能聊天，至少受这些约束：

```text
双方都有当前 action
双方都不是 sleeping
不是 23 点
目标不是 waiting
双方当前没有在聊天
chatting_with_buffer 冷却结束
最后再调用 LLM decide_to_talk
```

如果决定聊天，系统会：

```text
生成 conversation
总结 conversation
估算 conversation duration
给双方插入 chat action
设置 chatting_with / chat / chatting_end_time / buffer
局部重排日程
```

这说明 Generative Agents 的“涌现社会行为”并不是纯 LLM 自发产生，而是：

```text
程序化世界规则
+ 调度器
+ 感知规则
+ 记忆检索
+ LLM 判断
+ 对话生成
```

共同作用的结果。

---

## 13. 对我们 SpatialAgent plan 的影响

我们讨论后认为：

**如果直接基于 Generative Agents 原始架构，声称“空间拓扑自然塑造 LLM-agent 社会网络”，这个 claim 会不稳。**

原因是 Generative Agents 中，空间效应可能来自很多外部机制：

```text
pathfinding
同 arena 感知规则
vision radius
attention bandwidth
action duration
daily schedule
LLM 对地点语义的偏好
hard-coded talk eligibility
chat buffer
```

所以 dialogue network 的边不一定说明 agent 理解了空间拓扑。

---

## 14. 哪些 claim 不成立，哪些 claim 仍然成立

### 14.1 不稳的强 claim

这个 claim 风险很大：

```text
LLM agents naturally infer spatial topology from a world
and spontaneously form social networks according to spatial integration.
```

因为原始 Generative Agents 并没有让 agent 自然计算 integration / depth / control 等空间指标。

### 14.2 可救但需要控制的 claim

这个 claim 可做，但必须严格控制：

```text
Controlled spatial topology shapes emergent dialogue networks.
```

问题在于 spatial topology 可能只是改变 encounter opportunity，而不是 agent 使用空间结构。

### 14.3 最稳的 claim

更稳的表述是：

```text
We evaluate whether LLM-based multi-agent systems use agent-facing spatial
configurational representations, under matched controls, and whether such
representation sensitivity transfers into dialogue-network structure.
```

这更接近 plan v13-A 的方向。

---

## 15. 对 plan v13 / v13-A 的判断

我们认为：

```text
v13 更像社会模拟 / spatial-to-social phenomenon paper
v13-A 更像 AI evaluation / mechanism-identification paper
```

在理解 Generative Agents 真实架构后，**v13-A 明显更稳**。

v13-A 的核心问题是：

```text
Do LLM agents actually use environment structure,
or do apparent spatial-social effects arise from prompt richness,
semantic labels, encounter opportunity, or evaluator artifacts?
```

这个 framing 能容纳 positive、mixed、negative results，也更像 AAAI / AI evaluation 论文。

---

## 16. 最重要的实验控制

我们认为 plan 里最值得保留的是四个主条件：

```text
C1: Topology-only
C2c: Non-spatial information-volume control
C6m: Configurational perception
C_shuffle: Shuffled mapping
```

它们分别控制：

```text
C6m > C1:
不是普通 graph movement 本身造成的

C6m > C2c:
不是 prompt 更长、信息更多造成的

C6m > C_shuffle:
不是看到 integration/depth/control 这些词就泛化地变社交了

H2 after co-occurrence control:
不是单纯相遇机会造成的
```

这些条件是 plan 成立的关键。

---

## 17. H1 / H2 / H3 的重新理解

### H1: Local interaction

原始说法：

```text
High-integration locations produce more social interaction.
```

更稳说法：

```text
Under configurational perception, agents allocate more dialogue interaction
to high-integration locations than matched controls.
```

### H2: Agent centrality

这是最重要的 hypothesis。

```text
Agents exposed to high-integration locations become more central
in the dialogue network.
```

但必须控制 co-occurrence / encounter opportunity：

```text
dialogue centrality
~ exposure-weighted integration
+ co-occurrence exposure
+ condition
+ map / seed / run effects
```

否则 reviewer 会说 centrality 只是因为 agent 去了人多的地方。

### H3: Dyadic tie formation

H3 是最脆弱的 hypothesis：

```text
Dialogue tie probability decreases with topological distance.
```

它必须用 QAP / MRQAP / run-level coefficient aggregation，不能把 dyads 当独立样本做普通 logistic regression。

H3 可以作为 Tier 1 加分项，但不应该成为整个 paper 的唯一支柱。

---

## 18. 关键设计建议：不要复刻 Smallville，而要做受控实验 substrate

如果直接复刻 Generative Agents 的 Smallville 式生活模拟，会混入太多因素。

更适合 SpatialAgent 的设计是：

```text
固定 graph
固定 agent population
固定 initial states
固定每轮 movement opportunity
可控 encounter opportunity
显式操纵 agent-facing spatial descriptors
rule-based dialogue event extraction
run-level / QAP inference
```

研究应聚焦：

```text
spatial representation
→ local choice conditional on opportunity
→ dialogue network
```

而不是泛泛地说：

```text
space → society
```

---

## 19. 推荐最终定位

我们最后的结论是：

```text
如果 claim 是：
“基于 Generative Agents 的自然模拟证明空间拓扑塑造社会网络”
→ 不稳，甚至可能不成立。

如果 claim 是：
“设计一个受控评估协议，测试 LLM agents 是否使用显式空间结构信息，
并检验这种使用是否进入 dialogue network”
→ 成立，而且 v13-A 已经很接近。
```

最应该弱化的表述：

```text
emergent society
space naturally shapes social structure
Generative Agents already demonstrate this mechanism
```

最应该强化的表述：

```text
controlled evaluation
mechanism identification
matched controls
spatial representation sensitivity
dialogue-network outcome
co-occurrence control
null models
downgrade rules
```

---

## 20. 一句话总结

Generative Agents 的真正启发不是“空间自然产生社会”，而是：

> LLM 可以被嵌入一个由程序控制时间、空间、记忆、感知和调度的外部架构中，从而产生连续行为。

对我们的 SpatialAgent 计划来说，最稳的研究问题不是：

> 空间是否塑造 agent 社会？

而是：

> 在严格控制 prompt、信息量、相遇机会和评估方式后，LLM agents 是否真的会使用空间结构表示，并让这种使用体现在可观测的 dialogue network 中？
