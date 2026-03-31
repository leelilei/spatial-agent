# SpatialAgent 论文指导手册：从零到投稿

> 写给：一位有建筑学硕士背景、AI产品经验，但没有独立发表过CS论文的研究者
> 角色：你的论文指导教授
> 目标：手把手带你完成第一篇CCF-A会议论文
> 本手册与 `../plans/spatial_agent_research_plan_v7.md` 同步

---

## 写在最前面：你需要知道的几件事

**第一，做研究不是写代码。** 很多第一次写论文的人会犯一个错误：一上来就开始写代码搭系统，花了两个月把系统做得很漂亮，然后发现不知道这个系统要回答什么问题。正确的顺序是：先想清楚问题 → 再设计实验 → 最后才写代码。代码只是验证想法的工具。

**第二，论文的价值不在于你做了什么，而在于你发现了什么。** 审稿人不关心你搭了多复杂的系统，他们关心的是：你的研究揭示了什么之前不知道的东西？对于我们的项目，关键发现是"结构化空间表征能系统性地改变LLM Agent行为，而且这种改变部分沿着Space Syntax理论方向发生"——这是一个科学发现，不是一个工程成果。

**第三，你的建筑学背景是核心竞争力，不是需要隐藏的弱点。** 在CS会议上发论文不意味着你要假装自己是CS科班出身。相反，你的跨学科视角是这篇论文最不可替代的东西。拥抱它。

**第四，这篇论文经过了6轮评审迭代（v1→v7），方法论已经非常成熟。** 你的任务不是从零设计实验，而是**严格执行已经设计好的实验计划**。计划中的每一个设计决策背后都有审稿人挑战→解决的历史。遇到不理解的设计选择时，先查v3-v7的修订说明表，通常能找到答案。

---

## 阶段零：建立研究素养（第1-2周）

在碰任何跟SpatialAgent相关的东西之前，你需要先学会"怎么做研究"。

### 0.1 学习如何读论文

你不需要逐字读完每篇论文。学术论文的阅读是分层的：

**第一遍（5分钟）**：只读标题、摘要、Introduction最后一段（贡献列表）、看图表。目的是判断"这篇论文跟我的研究有没有关系"。

**第二遍（30分钟）**：读Introduction全文、Method部分的架构图和公式、Experiments的表格和图表、Conclusion。跳过具体实现细节。目的是理解"他们做了什么、怎么做的、效果如何"。

**第三遍（2-3小时）**：精读全文，包括细节、公式推导、实验设置。同时用你的reading_notes模板写笔记。只有P0优先级的论文需要第三遍。

推荐观看：
- 吴恩达（Andrew Ng）的 "How to Read a Research Paper"（YouTube，约15分钟）
- Srinivasan Keshav 的 "How to Read a Paper"（经典3-pass方法，PDF可搜索到）

### 0.2 学习学术写作基础

CS论文有固定的结构和写法规范。在开始写之前，你需要理解这些约定。

推荐阅读：
- Simon Peyton Jones "How to Write a Great Research Paper"（微软研究院Talk，YouTube可搜）——这是CS领域最经典的论文写作指导，30分钟，必看
- "学术写作的核心：每一段都在回答一个问题"——Introduction回答"为什么这个问题重要"，Method回答"你是怎么做的"，Results回答"结果是什么"，Discussion回答"这意味着什么"

### 0.3 了解你要投的会议

在开始研究之前，去看3-5篇你目标会议（AAMAS/AAAI）上最近发表的、跟你方向相关的论文。这会告诉你：审稿人期望什么样的论文？什么样的贡献被认可？什么样的实验设计被认为是充分的？

具体做法：
1. 去 AAMAS 2026 / AAAI 2026 proceedings 搜索关键词 "game agent" "NPC" "multi-agent"
2. 选3篇跟你最相关的，做第二遍阅读，重点关注他们的实验设计和评估方法

### 0.4 理解你的研究计划（v7）

**花半天时间精读 `../plans/spatial_agent_research_plan_v7.md`。** 你需要理解以下核心概念：

- **三阶段递进设计**：阶段1（表征验证）→ 阶段2（架构增量效应）→ 阶段3（探索性扩展）
- **梯度化条件**：C0(Random) → C1(Topology-Only) → C2(Non-Spatial Affordance) → C4(Full SpatialAgent)，每一级只增加一个变量
- **双主因变量**：BSR（有没有空间响应？）+ TAR（响应方向是否符合理论？）
- **两阶段分离评估**：盲行为编码 → 事后空间关联分析
- **Matched Initial Conditions (MIC)**：跨条件共享初始世界状态
- **开源模型优先**：主Actor/Judge用Qwen3.5-Plus，鲁棒性用DeepSeek-V3.2

---

## 阶段一：建立知识基础（第2-3周）

这个阶段的目标是：搞懂你要站在谁的肩膀上。

### 1.1 必须精读的论文（P0）

以下每篇论文都需要做第三遍精读，并用reading_notes模板写笔记。

**论文1：Generative Agents（Park et al., UIST 2023）**

这是你的直接前置工作。你的SpatialAgent-Lite架构是在LLM Agent框架基础上增加空间模块。

精读时重点关注：
- Agent认知架构（Perceive-Plan-Retrieve-Reflect-Act）是怎么设计的？
- 他们的虚拟小镇中空间以什么形式表示？（剧透：主要是地点名称和邻接关系——正是v7所说的"Topology-Only"）
- 他们怎么评估Agent行为的"可信度"？
- 他们提到了哪些局限性？

在哪找：arXiv:2304.03442

**论文2：The Social Logic of Space（Hillier & Hanson, 1984）第3-5章**

这是Space Syntax的奠基之作。你不需要读完整本书，但第3章（空间构型的形式化定义）和第5章（空间与社会行为的关系）是必读的。

精读时重点关注：
- Integration、Connectivity、Control Value的原始定义
- "natural movement"理论的核心论点
- Hillier用什么实证证据证明"空间影响行为"？
- inhabitants vs visitors 的区分（v7中用到了这个概念）

在哪找：Z-Library或Research Gate搜PDF。替代阅读：Al-Sayed et al. "Space Syntax Methodology"（2014），比原著更容易入门。

**论文3：From Isovists to Visibility Graphs（Turner et al., 2001）**

定义了VGA（Visibility Graph Analysis），是Openness/Mean Depth指标的方法论基础。

精读时重点关注：
- Isovist（视域）的定义
- Visibility Graph是怎么从空间平面图构建的？
- v7中使用了 `visible(i,j)` 函数——理解它的物理含义

在哪找：搜索论文标题 + "Environment and Planning B"

**论文4：Affordable Generative Agents（2024）**

精读时重点关注：
- 他们发现Agent在固定环境中的可信行为有上限
- 成本优化策略

在哪找：arXiv:2402.02053

**论文5：When LLMs Recognize Your Space（Oh et al., IEEE TVCG 2025）**

目前最接近你工作的论文，必须精读。

精读时重点关注：
- 他们怎么定义"spatial awareness"？
- 他们设计了哪三种空间感知条件？和你的7个梯度条件（C0-C7）有什么异同？
- 他们的局限性是什么？

在哪找：IEEE Xplore 搜索标题

### 1.2 需要泛读的论文（P1）

- LLM Game Agent Survey（arXiv:2404.02039）——了解游戏Agent全景
- Project Sid / Altera（2024）——Minecraft中的多Agent涌现
- Penn & Turner "Space Syntax Based Agent Simulation"（2001）——建筑学领域的Agent模拟前辈
- MultiAgentBench（arXiv:2503.01935）——多Agent评测方法论
- Artificial Leviathan（2024）——LLM Agent社会演化实验
- Hillier et al. (1993) "Natural movement"——H1推导链的核心文献
- Penn et al. (1998)——Integration与行人流量的实证关系

### 1.3 补充学习材料

**Space Syntax 入门**：
- UCL Space Syntax Lab 官网有教程和视频
- YouTube 搜索 "Space Syntax explained" 有多个10-20分钟的入门视频
- depthmapX 软件的官方教程

**LLM Agent 入门**：
- Lilian Weng的博客 "LLM Powered Autonomous Agents"
- Andrew Ng的 "Building AI Agents" 系列短课（DeepLearning.AI）

**NetworkX（图计算工具）**：
- 官方教程：networkx.org/documentation/stable/tutorial.html
- 你需要掌握：创建图、添加节点/边、计算shortest path、计算centrality指标

**统计方法**：
- 混合效应模型（Mixed-Effects Models）：v7的核心统计框架。推荐搜索 "mixed effects models tutorial R/Python"
- 你需要理解：chi-square检验、Spearman相关、Fisher z变换、Cohen's d、ICC
- Python工具：`scipy.stats`、`statsmodels`、`pingouin`

### 1.4 阅读阶段的输出物

- [ ] 5篇P0论文的详细阅读笔记（每篇1-2页）
- [ ] 6-7篇P1论文的简要笔记（每篇半页）
- [ ] 对H1-H3推导链的理解（能用自己的话讲清楚：Hillier原始理论 → 物理实证 → 文本Agent推导 → 可能失效条件）
- [ ] 能用NetworkX创建一个20节点图并计算Integration、Connectivity、Control Value、Mean Depth

---

## 阶段二：设计空间构型与预实验准备（第3-4周）

### 2.1 空间构型设计

验证性阶段（阶段1-2）只使用一张主地图：**Plaza**。探索性阶段（阶段3）额外使用 Labyrinth 和 Bridge。

三种构型的设计需要满足 v7 的**指标空间最大散布原则**：

| 构型 | 设计意图 | Integration分布 | Mean Depth分布 |
|------|---------|:-:|:-:|
| **Plaza** | 中心化、有明确公共核心 | 右偏（少数高值核心） | 左偏（多数浅层） |
| **Labyrinth** | 去中心化、深层复杂 | 均匀 | 右偏（多数深层） |
| **Bridge** | 多中心、瓶颈连接 | 双峰 | 中等 |

### 2.2 具体步骤

**步骤1：手绘草图。** 在纸上画Plaza的拓扑关系草图。凭你的建筑学直觉画——什么样的20节点图能有一个明确的中心广场、若干环路和若干死胡同？

**步骤2：转化为图数据。** 格式如下：

```yaml
# configs/layouts/plaza.yaml
nodes:
  - id: gate
    name: 城门
    type: public_outdoor
  - id: main_street
    name: 主街道
    type: public_outdoor
  - id: plaza
    name: 广场
    type: public_outdoor
  # ... 20个节点

edges:
  - [gate, main_street]
  - [main_street, plaza]
  # ... 所有连接
```

**步骤3：计算Space Syntax指标。** 运行metrics.py计算每个节点的Integration、Connectivity、Control Value、Mean Depth。

**步骤4：指标质量预检。**（对应v7 §6.0.1）
- 画四指标的分布直方图和相关矩阵
- 检查CV（变异系数）是否 ≥ 0.2——如果某指标CV太低，说明这张图在该维度上区分力不够
- 检查Openness与Connectivity的相关：若r > 0.8，则H2改用Mean Depth
- 检查高Control Value节点数量：若 < 3个，则H3降级为描述性观察

**步骤5：绘制四指标雷达图。** 三种构型的雷达图，确认它们在指标空间中形成足够散布。

### 2.3 NPC角色设计（对应v7 §4.3）

10个NPC沿三个维度系统性设计：

| 维度 | 水平 | 分布 |
|------|------|------|
| 社交倾向 | 高(外向)/中/低(内向) | 4/3/3 |
| 职业角色 | 公共型/中性型/隐蔽型 | 3-4/3/3-4 |
| 目标类型 | 社交型/信息型/独立型 | 3-4/3/3-4 |

**三个铁律**：
1. 社交倾向与职业正交（存在"外向的刺客"和"内向的酒保"）
2. 角色描述中**不包含**任何空间偏好暗示
3. 背景故事不绑定固定地点

### 2.4 C2 描述池设计（对应v7 §5.5）

C2（Stable Non-Spatial Affordance）是最重要的基线之一。你需要：

1. 编写20条等长度的非空间氛围描述，涵盖社交/警惕/放松/好奇四种引导方向（每种5条）
2. 描述与空间结构特征**无系统性关联**
3. **关键**：完成后做 reverse-inference audit——让LLM看描述，问"这个地方可能是高Integration还是低Integration？"。如果LLM能从描述推断出空间特征，说明描述泄露了空间信息，需要替换

### 2.5 Lexical Norming（对应v7 §6.0.4，Exp1C需要）

Exp1C的2×2因子设计需要"公共语义标签"和"私密语义标签"。你需要：

1. 准备候选标签（如"繁忙集市"、"隐蔽暗道"、"开放露台"等）
2. 收集五维评分：publicness, privacy, danger, valence, brightness
3. 保留那些在public/private维度上差异大、其他维度差异小的标签

### 2.6 这个阶段的输出物

- [ ] Plaza构型的yaml配置文件 + 可视化拓扑图
- [ ] Labyrinth和Bridge的初步设计（不需要最终版）
- [ ] 三种构型的Space Syntax指标汇总表 + 指标预检报告
- [ ] 10个NPC角色人设文档（附录D的初稿）
- [ ] C2描述池（20条）+ reverse-inference audit结果
- [ ] Exp1C的lexical norming结果

---

## 阶段三：搭建模拟系统（第4-6周）

### 3.1 系统搭建的正确顺序

**第一步：最小可运行版本（MVP）。** 1个Agent，Plaza构型，10轮。目标是让整个pipeline跑通：Agent接收空间描述 → 调用Qwen3.5-Plus API → 生成行为 → 更新世界状态 → 进入下一轮。不需要任何Space Syntax算法，用硬编码的空间描述就行。

这一步应该在2-3天内完成。

**第二步：加入Spatial Perception模块。** 实现v7 §5.2中的Absolute Structural表征。让Agent收到动态计算的空间描述：

```text
该位置与其他位置的平均拓扑距离为 1.8 步。
该位置直接连接 4 个相邻位置。
经过该位置可控制进出 3 个区域的通行。
此刻在场 2 人：Elara、Theron。
```

**第三步：加入多Agent。** 从1个Agent扩展到3个，实现交互机制。重点关注：Agent之间的对话怎么触发？一个Agent怎么感知到"这个房间里还有谁"？

**第四步：加入Spatial Action Sampling。** 实现v7 §5.3的Judge评分+softmax采样流程：
1. Actor生成K=5个候选行为
2. Judge（同一个Qwen3.5-Plus）根据空间上下文评分
3. softmax(score/τ) 采样，τ=0.5

**第五步：完整版本。** 10个Agent、20个节点、200轮。在Plaza上跑一次完整模拟，检查有没有明显的bug。

**第六步：实现所有Agent条件。** 按v7 §5.4的条件矩阵，实现C0-C7以及C6m、C6f的配置切换。

### 3.2 关键实现建议

**API调用配置**：
- 主Actor和Judge都用 Qwen3.5-Plus（通过第三方平台API）
- 在代码中做好model抽象层，方便后续切换到DeepSeek-V3.2做鲁棒性检查
- 实现API调用的重试机制（指数退避）和错误处理

**Matched Initial Conditions (MIC) 实现**：
```python
for seed in range(30):
    # 固定以下所有随机参数
    rng = np.random.RandomState(seed)
    npc_positions = rng.choice(20, 10, replace=False)
    c2_mapping = assign_c2_descriptions(rng)
    event_sequence = generate_events(rng)

    # 在同一seed下运行所有条件
    for condition in [C1, C2, C6m, C6f, C4]:
        run_simulation(seed, condition, npc_positions, c2_mapping, event_sequence)
```

**日志存储**：每一轮存JSON Lines，包含：轮次、Agent名字、所在位置、空间属性、收到的prompt、LLM原始回复、解析出的行为和对话。这些日志是后续分析的数据来源。

**行为结构化输出**：要求LLM返回JSON格式：

```json
{
  "thought": "这里人太多了，不适合谈秘密的事...",
  "action": "move",
  "action_target": "tavern_backroom",
  "dialogue": null,
  "dialogue_target": null
}
```

**LLM调用缓存**：实现 (prompt_hash → response) 的磁盘缓存，调试期间避免重复API调用。

### 3.3 预实验全套（对应v7 §6.0）

在正式实验之前，需要完成以下预实验：

| 预实验 | 目的 | 判断标准 |
|--------|------|---------|
| LLM空间理解门控 | Qwen3.5-Plus能否理解空间描述？ | Comprehension ≥ 85%, Behavioral Inference ≥ 70% |
| Prompt位置测试 | 空间描述插在prompt哪里效果最好？ | 选最稳定的位置并固定 |
| MIC有效窗口pilot | matched seed的方差缩减能持续多久？ | 报告ICC(seed)，不依赖MIC作为功效前提 |
| 收敛性pilot | 200轮够不够达到稳态？ | 连续3个20轮窗口内指标变化 < 5% |
| C2 reverse-inference audit | C2描述是否泄露空间信息？ | LLM无法从C2描述推断空间特征 |
| Exp1C lexical norming | 语义标签是否干净？ | public/private维度差异大，其他维度差异小 |

**如果Qwen3.5-Plus未通过理解门控**：这是一个严重问题。备选方案：
1. 换用Qwen3-Max（能力更强，但贵3倍）
2. 调整Absolute Structural表征的措辞使其更易理解
3. 如果所有开源模型都不通过 → 需要重新评估研究的可行性

### 3.4 这个阶段的输出物

- [ ] 完整的模拟系统，支持所有Agent条件（C0-C7, C6m, C6f）的配置切换
- [ ] MIC实现：同一seed下跨条件共享初始世界状态
- [ ] API缓存和重试机制
- [ ] 预实验全套结果报告
- [ ] → **决策点1**：主表征格式、Openness vs Mean Depth、prompt位置、轮次数

---

## 阶段四：运行阶段1实验（第4-5周）

### 4.1 Exp1A：6条件微任务对比

这是一个**轻量级实验**，不需要跑完整的200轮模拟。

**条件**：
| 条件 | 描述 |
|------|------|
| C0 | No Space（无任何空间信息） |
| C1 | Name Only（只有地点名称） |
| C2 | Stable Non-Spatial Affordance（非空间氛围描述） |
| C3 | Raw Numeric（原始数字指标） |
| C4 | Absolute Structural（主方案表征） |
| C5 | Shuffled Signal（空间信息与位置错配） |

**微任务**：每个条件 × 每种微任务类型（透露秘密、主动搭话、位置选择、停留/离开）× 若干场景。

**主比较**：C4 > C0, C1, C2, C3, C5

**主报告**：BSR + 连续型TAR_H1 + TAR_H2

> 阶段1的API成本几乎可以忽略（~¥3），所以不用担心成本。放心多跑几个调试回合。

### 4.2 Exp1C：反直觉2×2因子设计

| | 公共标签 | 私密标签 |
|---|:---:|:---:|
| 高拓扑中心性 | 一致 | **冲突** |
| 低拓扑中心性 | **冲突** | 一致 |

- 每cell至少10个独立场景，每场景20个微任务
- 使用lexical norming筛选过的标签
- 这是**探索性**实验，不承担确认性主结论

### 4.3 → 决策点2

阶段1完成后，检查：
- C4的BSR是否显著高于C0/C1/C2？
- TAR方向是否与理论预测一致？
- Exp1C的主效应和交互项如何？

如果C4并不显著优于C2 → 需要认真反思：空间结构信息是否真的比一般上下文增强更有效？这可能改变论文的定位。

---

## 阶段五：运行阶段2实验（第6-8周）

### 5.1 核心5条件（验证性主实验）

这是**整篇论文最重要的实验**。

| 条件 | Movement | 对话空间描述 | Action Sampling |
|------|----------|------------|----------------|
| C1 Topology-Only | 邻接+地名+在场数 | 无 | 无 |
| C2 Non-Spatial Affordance | 同C1 | 非空间描述 | 无 |
| C6m Perception-Only (Matched-Move) | **同C1** | Absolute Structural | 无 |
| C6f Perception-Only (Free-Move) | 空间指标+邻接 | Absolute Structural | 无 |
| C4 Full SpatialAgent | 空间指标+邻接 | Absolute Structural | 有 |

**运行参数**：
- 30 MIC seeds × 5条件 × 10 NPC × 250轮
- 每个seed下所有5个条件共享初始世界状态

**主比较链**（v7的核心）：
```
比较A: C4 - C1  = 完整空间化架构的总增益
比较B: C6m - C1 = 到位后Perception的纯认知贡献（Movement相同）
比较C: C6f - C6m = Movement信息优势的贡献
比较D: C4 - C6f = Action Sampling的独立增量
比较E: C6m - C2 = 空间结构信息 vs 非空间affordance基线
```

> 特别注意 C6m 和 C6f 的区别：C6m的Movement策略和C1一样（不用空间指标选目的地），C6f的Movement策略用空间指标。这是为了分离"Movement驱动的效应"和"到位后认知驱动的效应"。

### 5.2 主分析模型

**一级：MIC run-level主验证模型**（每个seed×condition汇总为一个数据点）

```
DV_run ~ condition + (1|seed)
```

这是论文**主结论的唯一依据**。

**二级：agent×seed聚合异质性模型**（探索性）

```
DV_agent_seed ~ condition + social_tendency + condition:social_tendency
                + (1|seed) + (1|agent_id)
```

### 5.3 机制探测条件（较小规模）

| 条件 | 作用 | seeds |
|------|------|:-----:|
| C3 Shuffled | 错误空间信息是否仍有效？ | 16 |
| C5 Judge-Only | Judge先验知识是否足以制造效应？ | 16 |
| C7 Fixed-Path | 分离Movement vs 到位后认知 | 20 |
| Full-RuleScorer | LLM Judge是否放大效应？ | 16 |

### 5.4 时间动态分析

每次run必须报告：
- 收敛曲线（每20轮的网络指标变化）
- 前半程vs后半程的空间效应差异
- 前50轮的"空间启动效应"单独分析

### 5.5 模型鲁棒性子集

在核心条件（C1/C6m/C4）上，用DeepSeek-V3.2-exp重复10个seeds。检查主效应方向是否一致。

### 5.6 这个阶段的输出物

- [ ] 阶段2核心：30 seeds × 5条件的完整日志
- [ ] 阶段2机制：各条件的完整日志
- [ ] DeepSeek鲁棒性子集日志
- [ ] 主比较链的统计结果（BSR + TAR + 效应量 + CI）
- [ ] 收敛曲线和时间动态分析
- [ ] → **决策点3**：空间效应是否显著？是否继续阶段3？

---

## 阶段六：行为编码与评估（第9-10周）

### 6.1 两阶段分离评估——这是关键方法论创新

v7的评估设计经过多轮审稿打磨。**不要自作主张修改评估流程。**

**阶段A：盲行为编码**

标注者只看行为文本，**不看空间信息**。标注维度：
- 行为类型（社交/警惕/探索/交易/守门等）
- 交互强度（1-5）
- 信息敏感度（1-5）
- 守门/监视/拦截行为（有/无）

**阶段B：空间关联分析**

研究者（你）将盲编码结果与空间特征进行事后关联。

> 为什么要分两阶段？如果让标注者同时看空间信息和行为，他们的标注会被空间信息影响——知道Agent在"隐蔽角落"就更容易把行为标为"私密"。分两阶段消除了这种循环定义风险。

### 6.2 Coding Manual开发

你需要写一份标注手册，定义每个标注维度的评分标准和边界案例。步骤：

1. 先自己标注50条样本，建立直觉
2. 写初版coding manual
3. 找2名标注者用你的manual各自独立标注100条样本
4. 计算Cohen's κ
5. 如果κ < 0.6：讨论分歧案例，修改manual，重新标注一批
6. 如果κ ≥ 0.6：manual定稿

### 6.3 LLM辅助标注

大规模标注用LLM（Qwen3.5-Plus），但：
- 用人类标注子集做calibration，确认LLM标注与人类标注的一致性
- 特别关注Shuffled条件的标注：如果LLM Judge对Shuffled条件仍给高分，说明Judge有先验偏见

### 6.4 TAR的计算

按v7的双轨实现：

**主实现（连续型）**：
```python
# 对每个seed×condition，计算location-level Spearman相关
for seed in seeds:
    for condition in conditions:
        rho_H1 = spearman(integration_per_location, sociality_per_location)
        rho_H2 = spearman(mean_depth_per_location, privacy_per_location)
        # Fisher z变换
        z_H1 = np.arctanh(rho_H1)

# run-level TAR = Fisher z值
TAR_H1_run = z_H1
```

**辅助实现（高/低分组）**：仅用于可视化。

---

## 阶段七：数据分析（第10-12周）

### 7.1 分析的核心原则

**run-level分析是主结论的唯一依据。** 不管event-level分析多么显著，如果run-level不显著，主结论就是"未发现大效应的证据"。

### 7.2 分析步骤

**步骤1：计算每个run的汇总指标**
```python
for seed in range(30):
    for condition in conditions:
        BSR_run = compute_bsr(logs[seed][condition])  # chi-square / Cramer's V
        TAR_H1_run = compute_tar_h1(logs[seed][condition])  # Fisher z
        TAR_H2_run = compute_tar_h2(logs[seed][condition])
        entropy_run = compute_behavioral_entropy(logs[seed][condition])
```

**步骤2：主验证模型**
```python
import statsmodels.formula.api as smf

model = smf.mixedlm("BSR_run ~ condition", data=df, groups="seed")
result = model.fit()
# 报告：condition系数、p值、95% CI
# 计算：Cohen's d（事后对比）
```

**步骤3：主比较链的逐一检验**
- C4 vs C1, C6m vs C1, C6m vs C2, C4 vs C6f 等
- **Benjamini-Hochberg FDR校正**
- 每个比较报告：效应量d + 95% CI + 校正后p值

**步骤4：时间动态**
- 收敛曲线图
- 前半程 vs 后半程的agent_type × time_half交互

**步骤5：机制条件分析**（探索性，附录报告）

### 7.3 如果结果不如预期

| 情况 | 应对 |
|------|------|
| run-level显著，方向符合理论 | 最佳情况，按计划写论文 |
| run-level显著，方向不符合理论 | 重新检查数据；诚实报告；调整Discussion |
| run-level不显著，event-level显著 | 报告为"存在中小效应迹象，需更大样本验证" |
| 两者都不显著 | 如实报告负面结果；论文重新定位为方法论贡献 |

> **不要因为p > 0.05就恐慌。** 本研究的run-level功效只能检测d ≥ 0.74的效应。如果真实效应是中等大小（d ≈ 0.5），run-level不显著是预期内的结果。用event-level的效应量估计和CI讲清楚故事。

### 7.4 这个阶段的输出物

- [ ] 完整的分析Jupyter notebook（可复现）
- [ ] 主比较链结果表（效应量 + CI + 校正p值）
- [ ] BSR和TAR的条件对比图（箱线图+误差线）
- [ ] 收敛曲线图
- [ ] 时间动态分析结果
- [ ] 机制条件结果汇总
- [ ] DeepSeek鲁棒性子集方向一致性检查

---

## 阶段八：人类评估（第12-13周，如时间允许）

### 8.1 评估设计

**被试招募**：从游戏玩家社区招募30-50人。

**评估材料**：
1. 从阶段2的日志中选取行为片段
2. 去除所有空间信息（盲呈现）
3. 让被试评估行为的合理性、角色一致性

**与v7的对应**：人类评估是"外部有效性增强"，不是核心验证分析。如果时间不够，可以跳过，论文仍然成立。

### 8.2 LLM-人类一致性

- 在人类标注子集上，比较人类标注与LLM标注的Cohen's κ
- 特别关注不一致案例的系统性模式

---

## 阶段九：论文写作（第13-17周）

### 9.1 写作顺序

```
1. 先写 Experiments 和 Results → 数据已全，最确定
2. 再写 Method（SpatialAgent-Lite架构）→ 系统已实现
3. 然后写 Theoretical Framework → H1-H3推导链
4. 然后写 Related Work
5. 然后写 Discussion → 解读所有可能的结果模式
6. 最后写 Introduction 和 Abstract
7. 最最后定 Title
```

### 9.2 论文结构（对应v7 §10）

```
1. Introduction (1.5页)
   - 问题：LLM Agent缺乏构型级空间认知
   - 三个理论跳跃
   - 贡献（4条）

2. Related Work (1页)

3. Theoretical Framework (1.25页)
   - Space Syntax指标 + 决策树
   - H1-H3推导链（Hillier → 物理实证 → 文本Agent推导 → 失效条件）
   - BSR + TAR双主因变量定义

4. SpatialAgent-Lite (0.75页)
   - Spatial Perception（Absolute Structural）
   - Spatial Action Sampling（Judge+softmax）
   - 信息访问矩阵（所有条件一览表）

5. Experimental Design (1.5页)
   - NPC设计 + 位置随机化
   - MIC设计
   - 阶段1 + 阶段2 + 统计框架

6. Results (1.5页)

7. Discussion (1页)
   - 理论归因
   - Perception vs Sampling贡献
   - 局限性（功效限制、20节点、单地图、模型泛化性）

8. Conclusion (0.25页)
```

### 9.3 写作要点

**主张边界非常重要**。v7明确了只支撑以下级别的结论：
- 结构化空间表征**可以**系统性影响LLM Agent行为
- 这种影响在若干关键比较中**超出**稳定的非空间affordance基线
- 这些影响中**有一部分**沿着Space Syntax理论方向发生

**绝对不要写**：
- "prove"（改用"provide evidence for"）
- "首次"（除非你100%确定）
- "显著提升"（如果只有event-level显著）

### 9.4 图表清单

**必须包含的图**：
- Figure 1：Plaza构型可视化（节点大小=Integration）
- Figure 2：SpatialAgent-Lite架构图
- Figure 3：信息访问矩阵（所有条件对比表）
- Figure 4：阶段1的BSR/TAR条件对比
- Figure 5：阶段2的主比较链结果
- Figure 6：Exp1C的2×2因子结果
- Figure 7：收敛曲线 / 时间动态

### 9.5 这个阶段的输出物

- [ ] 完整论文初稿
- [ ] 所有图表的出版质量版本（300dpi PNG或矢量PDF）
- [ ] 附录（角色详情、指标预检、消融结果等）
- [ ] 至少收到2人的review反馈并修改

---

## 阶段十：投稿（第17-18周）

### 10.1 投稿前自检清单

直接使用v7 §10的完整清单，逐一打勾：

**理论**：
- [ ] H1-H3推导链完整
- [ ] TAR_run的protocol已明确
- [ ] 主张没有强于设计能支撑的内容

**预实验**：
- [ ] Openness vs Mean Depth决策完成
- [ ] Lexical norming完成
- [ ] C2 reverse-inference audit完成
- [ ] MIC有效窗口分析完成
- [ ] Prompt位置固定
- [ ] 收敛性pilot完成

**阶段1**：
- [ ] 同时报告BSR与TAR
- [ ] Exp1C使用composite structural profile解释

**阶段2**：
- [ ] 30 MIC seeds × 5核心条件完成
- [ ] 主比较链全部报告
- [ ] run-level主模型写为 `DV ~ condition + (1|seed)`
- [ ] 收敛曲线与时间分段分析完成

**模型与评估**：
- [ ] Qwen3.5-Plus空间理解门控通过
- [ ] DeepSeek鲁棒性子集方向一致性检查完成
- [ ] Actor-Judge同源偏见检测完成
- [ ] Coding manual完成，人类κ ≥ 0.6

**写作**：
- [ ] 摘要主结论只依赖MIC run-level验证性分析
- [ ] RQ4明确写为探索性
- [ ] 阶段3明确写为可选扩展

### 10.2 投稿后

**立刻做**：
1. 把论文放到arXiv上
2. 整理代码仓库，准备开源（使用开源模型的优势：审稿人可以完整复现）
3. 准备项目总结发社交媒体

**等待期间**：
1. 准备Plan B投稿目标
2. 思考后续工作

---

## 预算与成本管理

### 模型配置

| 角色 | 模型 | 价格（输入/输出） |
|------|------|------:|
| 主Actor | Qwen3.5-Plus | ¥0.56/M / ¥3.36/M |
| 主Judge | Qwen3.5-Plus | 同上 |
| 鲁棒性Actor+Judge | DeepSeek-V3.2-exp | ¥1.4/M / ¥1.4/M |
| 偏见对照 | Rule-Based Scorer | ¥0 |

### 三档预算

| 方案 | 内容 | 费用 |
|------|------|-----:|
| **A: MVP** | 预实验+阶段1+阶段2核心+编码pilot | **~¥1,500-1,900** |
| **B: 推荐版** | A+机制条件+鲁棒性+人类评估 | **~¥4,200-4,700** |
| **C: 全量版** | B+阶段3+Exp3-Minimal | **~¥6,800-7,400** |

> API成本不是制约因素。按方案B执行，30个MIC seeds完整保留。

---

## 常见陷阱与建议

### 陷阱1：完美主义
不要试图做一个"完美"的系统。它只需要能够可靠地运行实验并产出有意义的数据。

### 陷阱2：只做工程不做分析
每周至少花30%的时间在"思考"上——思考实验结果意味着什么、你的假设是否合理、有没有更好的解释。

### 陷阱3：篡改评估流程
两阶段分离评估的设计是经过多轮审稿挑战形成的。不要为了"方便"而把盲编码和空间关联分析合并在一起做。

### 陷阱4：事后合理化
做实验之前就要把假设写清楚。H1-H3已经在v7中确定了，不管实验结果是否支持它们，都要诚实报告。RQ4和阶段3已经明确标注为"探索性"。

### 陷阱5：过度解读event-level结果
run-level不显著但event-level显著时，**绝不能**在摘要中写"显著提升"。这是学术诚信底线。

### 陷阱6：忽视Actor-Judge同源偏见
主Actor和Judge都用Qwen3.5-Plus，审稿人一定会问。确保Rule-Based Scorer对照和DeepSeek交叉验证的结果在论文中有清楚的报告。

### 陷阱7：低估写作时间
论文写作通常比预期多花50%。给写作阶段预留至少4周。

---

## 总结：你的研究旅程地图

```
第1-2周    学习做研究的方法 + 精读v7研究计划 + 建立知识基础
           ↓
第3-4周    设计Plaza构型 + NPC角色 + C2描述池 + lexical norming
           ↓
第4-6周    搭建模拟系统 + 预实验全套
           → 决策点1：表征格式、指标选择、轮次数
           ↓
第4-5周    阶段1：Exp1A + Exp1C
           → 决策点2：C4是否有效？RQ4先导证据？
           ↓
第6-8周    阶段2：核心5条件 + 机制条件 + 鲁棒性子集
           → 决策点3：空间效应是否显著？是否继续阶段3？
           ↓
第9-10周   行为编码 + 评估（coding manual + 两阶段分离评估）
           ↓
第10-12周  数据分析（run-level主分析 + event-level补充 + 时间动态）
           ↓
第12-13周  人类评估（如时间允许）
           ↓
第13-17周  论文写作
           ↓
第17-18周  Review + 修改 + 投稿 AAMAS-27
           ↓
           你的第一篇论文投出去了
```

记住：这个过程不是线性的。你会反复回到前面的阶段。这是完全正常的。

祝你研究顺利。这个方向真的很棒，而且经过6轮评审迭代，你的方法论已经非常扎实——现在最需要的是**执行力**。
