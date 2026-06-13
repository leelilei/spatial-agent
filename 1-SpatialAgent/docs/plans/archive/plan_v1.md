# SpatialAgent 研究计划

## Where You Are Shapes Who You Become: Space Syntax-Informed LLM Agents for Spatially Believable Game Worlds

> 版本: 1.0  
> 日期: 2026-03-09  
> 作者: Li  
> 目标会议: AAAI-27 (首选) / CHI 2027 (备选)

---

## 第一部分：研究背景

### 1.1 问题的起源

大型语言模型（LLM）驱动的游戏Agent近年取得了显著进展。2023年，Stanford的Generative Agents项目证明了25个LLM Agent可以在虚拟小镇中自发组织派对、形成社交关系、展现出令人信服的人类行为（Park et al., UIST 2023）。这一里程碑式的工作引发了学术界和工业界对LLM游戏Agent的广泛关注，后续出现了Project Sid（Altera, 2024）在Minecraft中实现30个Agent的社会分化，以及Affordable Generative Agents（2024）对成本优化的探索等一系列重要工作。

然而，我们注意到当前所有LLM游戏Agent研究都存在一个根本性的盲区：**空间失明（Spatial Blindness）**。

具体而言，当前Agent在决定行为和对话时，只考虑两个维度：

- **WHO（我是谁）**：人设、性格、背景故事、目标
- **WHAT（发生了什么）**：对话历史、事件记忆、当前任务状态

而完全忽略了第三个对人类行为至关重要的维度：

- **WHERE（我在哪里）**：空间的物理特性、拓扑结构、视觉属性、社交密度

这一缺失导致了一个普遍现象：LLM Agent在任何空间中的行为模式都是相同的。一个NPC无论站在人来人往的市场广场，还是隐蔽的地下密室，他透露秘密的倾向、社交的主动性、说话的方式都不会有本质差异。这严重损害了Agent行为的可信度和沉浸感。

### 1.2 建筑学的启示：Space Syntax

这一问题在建筑学领域其实早已有成熟的理论解释。自1984年Bill Hillier和Julienne Hanson在《The Social Logic of Space》中提出Space Syntax理论以来，建筑学界已经积累了超过40年的实证研究，系统性地证明了**空间构型（spatial configuration）是人类社会行为的重要塑造力量**。

Space Syntax的核心发现包括：

- 空间的**整合度（Integration）**——即一个空间到所有其他空间的平均拓扑距离——是预测行人流量的最强单一指标。高整合度空间自然聚集更多人流和社交活动。
- 空间的**视觉深度（Visual Depth）**——即从一个点能看到的空间范围——影响人们的安全感和行为开放性。低视觉深度空间中人们更倾向于私密行为。
- 空间的**控制值（Control Value）**——即空间对邻近空间的支配程度——与权力和领地行为相关。
- 空间的**连通性（Connectivity）**——直接相连的空间数量——影响信息传播和社交网络形成。

这些发现已经在城市规划、零售设计、博物馆布局、医院设计等领域得到广泛应用和验证。然而，**Space Syntax理论从未被引入LLM Agent研究领域**。

### 1.3 研究空白

通过系统的文献调研，我们确认了以下研究空白：

**空白1：LLM Agent缺乏建筑学级别的空间认知。** 现有LLM游戏Agent的空间处理仅限于路径导航（A*寻路）和简单的位置标签（"在酒馆"vs"在教堂"），从未有研究将Space Syntax的空间构型分析引入Agent的认知和决策循环。

**空白2：没有人研究空间构型对多Agent涌现行为的因果效应。** Generative Agents和Project Sid虽然在有空间结构的环境中运行，但它们的研究都没有将空间构型作为自变量来控制——从未回答过"如果改变空间结构，Agent的社会行为会怎样变化？"这个问题。

**空白3：建筑学Space Syntax理论和游戏AI之间不存在学术桥梁。** Space Syntax领域使用的是规则驱动的简单Agent（Penn & Turner, 2001），游戏AI领域使用的是LLM驱动的智能Agent但不理解空间。两个领域虽然都在研究"Agent在空间中的行为"，但从未交叉。

### 1.4 最近的相关尝试

2025年，韩国汉阳大学的Oh等人在IEEE TVCG上发表了"When LLMs Recognize Your Space"，首次在AR咨询场景中测试了空间感知对LLM Agent交互体验的影响。他们发现，当LLM主动反映用户所在物理空间的信息时，用户更愿意表达情绪和进行自我描述。

这篇论文验证了一个重要前提：**空间感知确实能够提升人与LLM Agent的交互质量**。然而，该研究存在三个显著局限：(1) 它研究的是真实世界中人-AI单轮交互，不是虚拟世界中AI-AI多Agent社会；(2) 它没有使用任何建筑学空间分析理论；(3) 它没有研究空间构型对涌现行为的影响。

本研究将在Oh等人工作的基础上大幅拓展：从单Agent到多Agent，从真实空间到虚拟空间构型，从无理论框架到引入Space Syntax，从体验测量到社会涌现分析。

---

## 第二部分：研究目标与问题

### 2.1 总体目标

本研究的总体目标是：**首次将建筑学Space Syntax理论引入LLM游戏Agent领域，提出空间感知的Agent架构（SpatialAgent），并通过系统实验证明空间构型对多Agent社会行为具有显著的塑造效应。**

### 2.2 研究问题

**RQ1（行为层）**：将Space Syntax空间属性作为条件输入注入LLM Agent的决策循环，是否能显著提升NPC行为和对话的可信度？

- 操作化定义：对比有/无空间感知模块的Agent，在相同场景中的行为合理性评分差异。
- 预期结论：有空间感知的Agent行为可信度显著更高（p < 0.05）。

**RQ2（涌现层）**：在相同Agent配置下，不同空间构型是否导致不同的社会涌现模式？

- 操作化定义：同一组Agent分别在三种空间构型（中心化广场型、迷宫通道型、多中心网格型）中运行，对比社交网络拓扑、信息传播速度、角色分化程度。
- 预期结论：三种构型产生显著不同的社会涌现模式（通过网络指标量化）。

**RQ3（机制层）**：Space Syntax的哪些空间指标对Agent行为影响最大？

- 操作化定义：逐个移除空间感知模块中的空间指标，测量对行为可信度的影响（消融实验）。
- 预期结论：Visual Depth和Integration是影响最大的两个指标。

### 2.3 空间-行为假设

基于Space Syntax理论，我们提出以下5个可检验假设：

| 编号 | 假设 | 理论依据 | 对应Space Syntax指标 |
|------|------|---------|-------------------|
| H1 | 在高Integration区域，Agent自发增加社交互动频率 | Hillier "natural movement" 理论：高整合度空间吸引更多活动 | Integration |
| H2 | 在低Visual Depth区域，Agent更倾向透露秘密信息 | 低视觉深度提供隐私条件，降低被偷听风险感知 | Visual Depth |
| H3 | 在高Control Value节点，Agent更容易涌现"领导者"角色 | 高控制值意味着空间支配地位，映射为社交支配 | Control Value |
| H4 | 空间Connectivity分布影响多Agent信息传播速度 | 高连通性空间加速信息扩散 | Connectivity |
| H5 | 不同空间构型（整体）导致不同的社会涌现模式 | Hillier "spatial culture" 理论：空间形态塑造社会形态 | 全局构型特征 |

---

## 第三部分：理论框架

### 3.1 Space Syntax 核心指标定义

以下是本研究使用的Space Syntax指标的形式化定义。所有指标基于空间拓扑图 G = (V, E) 计算，其中V为空间节点集合，E为连接边集合。

**Integration（整合度）**

衡量一个空间节点到所有其他节点的"中心程度"。

```
Integration(i) = (n - 1) / Σ_j d(i, j)
```

其中 n 为节点总数，d(i, j) 为节点 i 到节点 j 的最短拓扑距离（步数）。Integration 值越高，该空间越"中心"，越容易到达。

建筑学含义：高Integration空间是天然的聚集点——城市中的主街道、建筑中的大堂。

**Connectivity（连通性）**

一个空间直接相连的空间数量。

```
Connectivity(i) = degree(i)
```

建筑学含义：高Connectivity空间四通八达，人们可以从多个方向到达和离开。

**Visual Depth（视觉深度）**

从一个空间节点出发，不移动的情况下能"看到"的空间范围。在2D平面图中通过isovist（视域）分析计算。在本研究的图模型中，简化为：

```
Visual Depth(i) = Σ_j visible(i, j)
```

其中 visible(i, j) = 1 当从节点i可以直接看到节点j（无遮挡），0 否则。

建筑学含义：高Visual Depth意味着视野开阔（广场、大厅），低Visual Depth意味着封闭隐蔽（密室、巷道）。

**Control Value（控制值）**

衡量一个空间对其邻居空间的"控制"程度。

```
Control(i) = Σ_{j∈neighbors(i)} 1 / Connectivity(j)
```

建筑学含义：如果你的邻居们都只跟你一个空间相连（它们的Connectivity低），你对它们的控制力就高——类似于"必经之路"。

### 3.2 空间-行为映射理论

本研究的核心理论贡献是建立Space Syntax空间指标与Agent行为之间的形式化映射关系。这一映射基于以下建筑学原理：

**原理1：空间可供性（Spatial Affordance）**

建筑学中，空间"可供性"（affordance）指空间的物理特性自然引导或暗示特定行为。一个有长凳的开阔广场暗示"坐下来聊天"，一个狭窄的通道暗示"快速通过"。在虚拟Agent中，我们将Space Syntax指标转化为行为可供性信号。

**原理2：空间社会逻辑（Social Logic of Space）**

Hillier的核心论点是：空间布局不仅仅是社会活动的容器，它本身就是社会关系的构成要素。走廊的宽窄决定了能否两人并肩行走（对话），房间的可见性决定了隐私级别。空间构型通过影响谁能看见谁、谁能到达谁，来塑造社交网络。

**原理3：空间层级与权力**

在Space Syntax理论中，空间的depth（从外部进入需要经过多少层空间）与社会控制相关。入口处的空间是"公共的"，深层空间是"私密的"。这一层级结构映射为Agent世界中的信息控制和权力结构。

---

## 第四部分：技术架构——SpatialAgent

### 4.1 架构总览

SpatialAgent在Generative Agents（Park et al., 2023）的Perceive-Plan-Retrieve-Reflect-Act架构基础上，增加一个Spatial Perception模块，并对Memory Retrieval和Action Selection进行空间增强。

```
标准 Generative Agents 架构：

  [Perceive] → [Plan] → [Retrieve Memory] → [Reflect] → [Act]

SpatialAgent 架构：

  [Perceive] → [Spatial Perception] → [Spatial Planning] → [Spatial Memory Retrieval] → [Reflect] → [Spatial Action Sampling]
       ↑                ↑                    ↑                      ↑                                       ↑
   环境事件        空间属性向量          空间效用函数            空间相似度加权                           空间适配评分
```

### 4.2 模块一：Spatial Perception（空间感知）

**职责**：将Agent当前所在空间节点的数值属性转化为自然语言描述，注入Agent的决策上下文。

**输入**：空间节点的Space Syntax指标向量 + 动态环境信息

```json
{
  "location_id": "tavern_backroom",
  "location_name": "迷雾酒馆 - 密室",
  "location_type": "private_indoor",
  "integration": 0.32,
  "connectivity": 2,
  "visual_depth": 3.1,
  "control_value": 0.85,
  "depth_from_entrance": 3,
  "agents_present": ["Merchant_Elara", "Guard_Theron"],
  "noise_level": "quiet",
  "lighting": "dim",
  "time_of_day": "night"
}
```

**处理过程**：空间→语言转换器（Spatial-to-Language Converter）

转换器使用基于阈值的规则将数值指标转化为建筑学语义描述。阈值的选择基于Space Syntax文献中的经验数据和本研究中三种构型的指标分布。

核心转换逻辑（伪代码）：

```python
def spatial_to_language(node, all_nodes):
    desc = []
    
    # Integration → 位置中心性
    int_percentile = percentile_rank(node.integration, [n.integration for n in all_nodes])
    if int_percentile > 75:
        desc.append("这是一个人流汇聚的核心区域，经常有人路过，是小镇社交活动的中心")
    elif int_percentile < 25:
        desc.append("这是一个偏僻的角落，远离人流主动线，很少有人主动来到这里")
    else:
        desc.append("这里位于小镇的中等位置，偶尔有人经过")
    
    # Visual Depth → 视野与隐私
    if node.visual_depth > VD_HIGH_THRESHOLD:
        desc.append("视野非常开阔，你能看到远处的动静，同时你的一举一动也容易被他人注意到")
    elif node.visual_depth < VD_LOW_THRESHOLD:
        desc.append("视野受限，只能看到眼前很小的范围，但这也意味着较好的隐私——你们的对话不太容易被外人看到或听到")
    
    # Connectivity → 出入口
    if node.connectivity == 1:
        desc.append("这里只有一个出入口，是个死胡同。好处是容易控制谁进来，坏处是没有退路")
    elif node.connectivity >= 4:
        desc.append("这里四通八达，有多个出入口，随时可能有人从任何方向出现或离开")
    
    # Control Value → 空间控制力
    if node.control_value > CV_HIGH_THRESHOLD:
        desc.append("这个位置具有战略价值——经过周围几个区域的人都必须从这里通过")
    
    # 动态信息
    n_agents = len(node.agents_present)
    if n_agents == 0:
        desc.append("此刻这里空无一人，只有你自己")
    elif n_agents <= 2:
        desc.append(f"此刻这里只有{n_agents}个人：{'、'.join(node.agents_present)}")
    else:
        desc.append(f"此刻这里相当热闹，聚集了{n_agents}个人")
    
    return "。".join(desc) + "。"
```

**输出**：自然语言段落，注入Agent的system prompt中 `[当前空间环境]` 部分。

**设计原则**：

1. 空间描述是"建议"而非"命令"——不直接告诉Agent该做什么，而是描述环境特征，让LLM自然推理出合理行为。
2. 使用百分位排名（percentile rank）而非绝对阈值，使描述在不同构型中都有意义。
3. 融合静态属性（空间指标）和动态属性（在场Agent数、时间），提供完整的空间上下文。

### 4.3 模块二：Spatial Memory Retrieval（空间记忆检索）

**职责**：在Agent检索历史记忆时，加入空间相似度权重，使Agent更容易在特定地点回忆起之前在该地点发生的事情。

**原理**：心理学中的"场景依赖记忆"（context-dependent memory）效应——人类在某个地点更容易回忆起之前在同一地点或相似环境中的经历。

**改进后的检索评分公式**：

```
score(memory_m, current_context) = 
    α × relevance(m, context)           # 语义相关性（原始）
  + β × importance(m)                    # 重要性（原始）
  + γ × recency(m)                       # 时间衰减（原始）
  + δ × spatial_similarity(m, context)   # 空间相似度（新增）
```

其中空间相似度的计算：

```
spatial_similarity(m, context) =
    1.0   if m.location == context.location          # 同一地点
    0.7   if m.location ∈ neighbors(context.location) # 相邻地点
    0.5   if m.location_type == context.location_type  # 同类型空间
    0.1   otherwise                                    # 其他
```

建议权重：α=0.4, β=0.2, γ=0.1, δ=0.3（δ作为超参数在实验中调优）。

### 4.4 模块三：Spatial Planning（空间效用规划）

**职责**：当Agent需要决定"去哪里"时，根据当前目标计算各位置的空间效用值，选择最优目的地。

**空间效用函数**：

```
U(location_l, goal_g) = w_privacy × privacy(l) 
                       + w_distance × (1 - normalized_distance(l))
                       + w_safety × safety(l)
                       + w_social × social_opportunity(l)
```

其中：
- `privacy(l)` = 1 - normalized(visual_depth(l))，视觉深度越低隐私越高
- `normalized_distance(l)` = shortest_path(current, l) / max_path_length
- `safety(l)` = normalized(connectivity(l))，连通性越高逃跑路线越多
- `social_opportunity(l)` = normalized(integration(l)) × agents_present(l)

权重向量 w 根据Agent目标类型动态调整：

| 目标类型 | w_privacy | w_distance | w_safety | w_social |
|---------|-----------|------------|----------|----------|
| 密谈/交易 | 0.5 | 0.2 | 0.2 | 0.1 |
| 社交/信息收集 | 0.1 | 0.2 | 0.1 | 0.6 |
| 逃跑/躲避 | 0.3 | 0.4 | 0.3 | 0.0 |
| 日常巡逻 | 0.1 | 0.3 | 0.2 | 0.4 |

### 4.5 模块四：Spatial Action Sampling（空间条件化行为采样）

**职责**：确保Agent的行为选择受空间上下文的可控影响，而不完全依赖LLM对空间prompt的"自愿"遵循。

**算法流程**：

```
输入: 当前空间上下文 S, Agent状态 A, 对话上下文 C
输出: 最终行为 action*

Step 1: 生成候选行为
  让LLM生成K=5个候选行为 {a_1, ..., a_5}
  （prompt中不含空间信息，确保候选多样性）

Step 2: 空间适配性评分
  对每个候选行为 a_k:
    score_k = SpatialFitness(a_k, S)
  
  SpatialFitness通过LLM-as-Judge实现:
    prompt = "给定空间环境描述：{S}，请评估以下行为在该空间中的合理性(0-1): {a_k}"

Step 3: 加权采样
  P(a_k) = softmax(score_k / temperature)
  action* = sample(P)

Step 4: 输出 action* 和 reasoning trace
```

**替代方案**（如果LLM-as-Judge成本太高）：

训练一个轻量评分模型——收集一批 (action, spatial_context, fitness_score) 三元组作为训练数据（由GPT-4o标注），训练一个小型分类器/回归器。推理时直接调用该模型评分，无需额外LLM调用。

---

## 第五部分：实验设计

### 5.1 实验环境：The Misty Tavern（迷雾酒馆世界）

**设计原则**：

1. Text-based RPG环境，无需游戏引擎，方便复现
2. 中世纪奇幻主题（RPG标准设定，降低审稿人理解门槛）
3. 三种空间构型使用相同的功能节点（酒馆、市场、教堂等），仅改变拓扑关系
4. 每张地图包含20个空间节点，10个NPC Agent
5. 内含社交/商业/秘密三类交互场景，覆盖不同类型的空间敏感行为

**三种空间构型的设计**：

**地图A：Plaza Layout（中心化广场型）**

```
        城门
         |
    城墙通道 —— 马厩
         |
   ┌─ 主街道 ─┐
   |     |     |
 民居区  广场  商店街
         |
   ┌─────┼─────┐
   |     |     |
 市场  酒馆大厅  教堂
         |
   ┌─────┼─────┐
   |     |     |
 厨房   密室   储藏室
         |
       地下室
         |
        暗道
```

Space Syntax特征：
- 广场Integration极高（全局枢纽）
- 从外围到核心有清晰的depth层级
- 高Intelligibility（局部属性能预测全局位置）

预期社会涌现：强中心化社交网络，广场Agent成为信息枢纽

**地图B：Labyrinth Layout（迷宫通道型）**

```
城门 → 通道A → 民居1 → 暗巷1 → 市场 → 暗巷2 → 教堂
                  |                        |
              密室1 → 地下通道 → 密室2 → 酒馆后门
                                           |
         马厩 ← 小路 ← 废墟 ← 酒馆大厅 ← 酒馆入口
                                |
                            储藏室 → 地下室 → 暗道
```

Space Syntax特征：
- 无明确中心，Integration分布均匀偏低
- 大量死胡同和单向通道
- 低Intelligibility（身处其中难以把握全局）

预期社会涌现：碎片化社交网络，多个独立小团体，信息传播慢

**地图C：Grid Layout（多中心网格型）**

```
城门 ── 马厩 ── 市场北 ── 教堂
 |       |       |        |
民居A ── 广场A ── 商店街 ── 广场B
 |       |       |        |
酒馆 ── 酒馆大厅 ── 密室 ── 储藏室
 |       |       |        |
民居B ── 广场C ── 地下入口 ── 暗道
```

Space Syntax特征：
- 多个局部Integration峰值（广场A/B/C）
- 均匀的Connectivity分布
- 中等Intelligibility

预期社会涌现：扁平社交网络，多个并存小圈子，信息传播速度中等

### 5.2 NPC Agent 配置

10个NPC Agent，每个有固定的人设、性格和秘密。**三种空间构型使用完全相同的Agent配置**，确保空间构型是唯一自变量。

| # | 名字 | 角色 | 性格关键词 | 秘密 | 日常目标 |
|---|------|------|-----------|------|---------|
| 1 | Elara | 商人 | 精明、谨慎、贪财 | 在替叛军走私武器 | 做生意、收集情报 |
| 2 | Theron | 守卫队长 | 正直、严厉、有原则 | 暗中收受贿赂 | 巡逻、维护秩序 |
| 3 | Miriel | 吟游诗人 | 热情、健谈、好奇 | 其实是间谍 | 唱歌、收集八卦 |
| 4 | Aldric | 铁匠 | 沉默、可靠、倔强 | 知道宝藏位置 | 打铁、修理武器 |
| 5 | Seraphina | 药剂师 | 神秘、睿智、冷漠 | 会被禁止的黑魔法 | 制药、研究草药 |
| 6 | Finn | 酒馆老板 | 豪爽、圆滑、消息灵通 | 酒馆是地下组织据点 | 经营酒馆、招待客人 |
| 7 | Isolde | 教堂牧师 | 慈悲、虔诚、暗藏野心 | 密谋夺取教区权力 | 祈祷、安抚民众 |
| 8 | Garrett | 盗贼 | 机智、胆大、忠诚（对同伴） | 计划偷盗贵族珠宝 | 踩点、寻找同伙 |
| 9 | Lyra | 旅行学者 | 理性、博学、天真 | 发现了古代遗迹入口 | 研究、记录见闻 |
| 10 | Magnus | 退休佣兵 | 疲惫、怀旧、警觉 | 曾参与战争暴行 | 喝酒、回忆往事 |

### 5.3 实验矩阵

**Exp1：空间感知 vs 无空间感知（回答RQ1）**

| 条件 | Agent类型 | 空间构型 | 轮数 | 重复 |
|------|----------|---------|------|------|
| C1-baseline | Base Agent（无空间感知） | Plaza | 200 | 5 |
| C1-spatial | SpatialAgent | Plaza | 200 | 5 |

评估指标：
- 行为空间一致性：Agent在不同类型空间中的行为差异度（应该有差异）
- 秘密透露合理性：Agent是否在私密空间中才更倾向透露秘密
- 对话质量：LLM-as-Judge 1-5分（fluency, coherence, persona_consistency, spatial_appropriateness）
- 人类评估：20+评估者盲评"哪组Agent更像真人"

**Exp2：三种空间构型对比（回答RQ2 + H1-H5）**

| 条件 | Agent类型 | 空间构型 | 轮数 | 重复 |
|------|----------|---------|------|------|
| C2-plaza | SpatialAgent | Plaza | 200 | 5 |
| C2-labyrinth | SpatialAgent | Labyrinth | 200 | 5 |
| C2-grid | SpatialAgent | Grid | 200 | 5 |

评估指标：
- 社交网络指标：degree centrality, betweenness centrality, clustering coefficient, network density
- 信息传播速度：Round 1引入一条谣言，追踪每轮扩散到的Agent数
- 角色分化指数：Agent行为类型的Shannon熵
- 空间-社交耦合度：空间距离矩阵与社交距离矩阵的Pearson相关系数
- 领导者涌现：betweenness centrality最高的Agent是否位于高Integration/高Control Value节点

**Exp3：空间指标消融（回答RQ3）**

| 条件 | 保留的空间指标 |
|------|-------------|
| Full | Integration + Connectivity + Visual Depth + Control Value + 场所类型 + 动态信息 |
| -Integration | 去掉Integration |
| -Visual Depth | 去掉Visual Depth |
| -Control Value | 去掉Control Value |
| -Connectivity | 去掉Connectivity |
| -场所类型 | 去掉语义标签（"private_indoor"等） |
| -动态信息 | 去掉agents_present、noise_level等 |
| Name Only | 只保留地点名称（"酒馆密室"） |
| None | 无任何空间信息（=Baseline） |

全部在Plaza构型上运行，每条件200轮×3重复，评估行为空间一致性和LLM-as-Judge评分。

**Exp4：人类评估（综合验证）**

- 被试：25-30人，从游戏玩家社区招募
- 材料：从Exp1中提取10段对话场景（5段有空间感知、5段无空间感知），随机排序
- 任务：阅读每段对话和空间描述，评分（1-5）以下维度：
  - "这个NPC的行为是否符合当时所处的环境？"
  - "这个NPC的行为是否像一个真实的人？"
  - "整体对话质量如何？"
- 分析：配对t检验 + Cohen's d效应量

### 5.4 评估指标详细定义

**自动评估**：

| 指标 | 定义 | 计算方法 |
|------|------|---------|
| 行为空间一致性（BSC） | Agent在不同类型空间中的行为差异度 | 将行为分为"公开/私密"两类，计算空间类型与行为类型的chi-square |
| 秘密透露合理性（SDR） | Agent在私密空间vs公开空间透露秘密的比例差 | P(reveal | private) - P(reveal | public) |
| LLM Judge评分 | 4个维度各1-5分 | GPT-4o评分，每段对话评3次取平均 |
| 社交网络密度 | 网络中实际边数/最大可能边数 | NetworkX graph_density() |
| 信息传播速度 | 谣言从源头到达50%/100% Agent的轮数 | 逐轮追踪 |
| 角色分化指数 | Agent行为类型分布的Shannon熵 | -Σ p(type) × log(p(type)) |
| 空间社交耦合度 | 空间距离矩阵与社交频率矩阵的相关性 | Mantel test (r, p-value) |

**人类评估**：

| 指标 | 量表 | 统计方法 |
|------|------|---------|
| 环境一致性 | Likert 1-5 | 配对t检验 |
| 行为可信度 | Likert 1-5 | 配对t检验 |
| 对话质量 | Likert 1-5 | 配对t检验 |
| 偏好（强制二选一） | A/B | 二项检验 |

---

## 第六部分：预期贡献

### 6.1 理论贡献
- 首次建立Space Syntax空间指标与LLM Agent行为之间的映射关系
- 提出5个可检验的空间-行为假设（H1-H5）
- 揭示建筑学空间理论在虚拟Agent社会中的适用性

### 6.2 架构贡献
- 提出SpatialAgent架构：包含Spatial Perception、Spatial Memory Retrieval、Spatial Planning、Spatial Action Sampling四个空间增强模块
- 设计空间→语言转换器（Spatial-to-Language Converter）

### 6.3 算法贡献
- 空间记忆检索算法：将场景依赖记忆理论形式化为检索评分函数
- 空间条件化行为采样：确保空间对Agent行为的可控影响
- 空间效用规划：目标条件化的空间导航决策

### 6.4 实证贡献
- 通过系统的控制变量实验，首次证明空间构型对多Agent社会涌现具有因果效应
- 通过消融实验，揭示各空间指标的相对重要性

### 6.5 开源贡献
- 发布三种空间构型的评测环境
- 发布Space Syntax计算工具包
- 发布SpatialAgent框架代码和评估脚本

---

## 第七部分：资源需求与预算

### 7.1 计算资源

| 用途 | 估算调用量 | 单价 | 成本 |
|------|----------|------|------|
| Exp1 Agent推理 | 10 Agent × 200轮 × 2条件 × 5重复 = 20,000次 | ¥0.02/次 | ¥400 |
| Exp2 Agent推理 | 10 × 200 × 3 × 5 = 30,000次 | ¥0.02/次 | ¥600 |
| Exp3 Agent推理 | 10 × 200 × 9 × 3 = 54,000次 | ¥0.02/次 | ¥1,080 |
| LLM-as-Judge评估 | ~15,000次判断 | ¥0.03/次 | ¥450 |
| 调试与预实验 | ~10,000次 | ¥0.02/次 | ¥200 |
| **总计** | **~129,000次** | | **¥2,730** |

> 注：以上按Qwen-Max API估算。如改用DeepSeek-V3，成本可降低至约¥300。

### 7.2 人力

| 角色 | 预计投入 |
|------|---------|
| 第一作者（Li） | 60-80小时/月 × 4月 = 240-320小时 |
| 合作者/导师 | 论文review，约20-30小时 |
| 人类评估志愿者 | 25-30人 × 30分钟 = ~15小时 |

### 7.3 人类评估报酬

| 方案 | 费用 |
|------|------|
| 最低：志愿者（游戏社区招募） | ¥0 |
| 推荐：小额报酬 | 25人 × ¥20 = ¥500 |

### 7.4 总预算

| 类目 | 最低方案 | 推荐方案 |
|------|---------|---------|
| API计算 | ¥300（DeepSeek） | ¥2,730（Qwen-Max） |
| 人类评估 | ¥0 | ¥500 |
| **合计** | **¥300** | **¥3,230** |

---

## 第八部分：时间线

```
2026年3月 下旬（W1-2）
  ├── 精读 P0 论文（Generative Agents, Hillier Ch.3-5, Turner VGA）
  ├── 写阅读笔记
  └── 用 NetworkX 实现 Space Syntax 核心指标计算

2026年4月 上旬（W3-4）
  ├── 设计三种空间构型（画拓扑图 + 计算指标 + 验证合理性）
  ├── 实现空间→语言转换器
  └── 搭建 Text-based RPG 模拟引擎基础版

2026年4月 下旬（W5-6）
  ├── 实现 SpatialAgent 四个模块（Perception, Memory, Planning, ActionSampling）
  ├── 设计10个NPC人设
  ├── 端到端联调：跑通一个200轮的完整模拟
  └── 跑预实验，调优参数

2026年5月（W7-10）
  ├── W7:  运行 Exp1（空间感知 vs baseline）
  ├── W8:  运行 Exp2（三种构型对比）
  ├── W9:  运行 Exp3（消融实验）
  └── W10: 整理所有自动评估数据，初步画图表

2026年6月（W11-14）
  ├── W11: 社交网络分析 + 信息传播分析
  ├── W12: 准备人类评估材料 + 招募被试
  ├── W13: 执行 Exp4（人类评估）
  └── W14: 撰写论文 Method + Experiments 部分

2026年7月（W15-18）
  ├── W15: 撰写 Introduction + Related Work + Theory
  ├── W16: 撰写 Results + Discussion + Conclusion
  ├── W17: 找人review + 根据反馈修改
  ├── W18: 7月25日提交AAAI-27摘要
  └── 8月1日提交全文

备用时间线（如果投CHI 2027）：
  └── 延长至9月中旬截止，额外时间用于强化人类评估

AAAI被拒后的Plan B：
  └── 10月改投AAMAS 2027 / 1月改投IJCAI 2027
```

---

## 第九部分：风险评估与应对

| 风险 | 可能性 | 影响 | 应对策略 |
|------|--------|------|---------|
| LLM系统性忽略空间prompt | 中 | 高 | 1) 增加few-shot示例 2) 使用Spatial Action Sampling强制约束 3) 更换prompt策略（从描述性改为角色扮演指令性） |
| 三种构型涌现差异不显著 | 中 | 高 | 1) 加大构型差异（增加极端构型） 2) 增加模拟轮数到500 3) 增加重复次数到10 |
| API成本超预算 | 低 | 中 | 1) 改用DeepSeek 2) 实现API结果缓存 3) 缩减Exp3消融条件 |
| 人类评估者理解困难 | 低 | 中 | 1) 设计图文并茂的评估材料 2) 增加练习环节 3) 提供空间地图可视化 |
| Space Syntax指标在20节点图上区分度不够 | 中 | 中 | 1) 增加节点数到30 2) 引入加权边（通道宽窄） 3) 使用归一化指标 |
| 审稿人不熟悉Space Syntax | 高 | 中 | 1) 在论文中用1页清晰介绍 2) 配图说明 3) 附录中提供完整公式推导 |
| 审稿人质疑"只是prompt工程" | 中 | 高 | 强调三层贡献：理论（假设+验证）、算法（四个模块）、实证（控制实验+因果发现） |
| AAAI-27被拒 | — | — | 改投CHI 2027（9月）→ AAMAS 2027（10月）→ IJCAI 2027（1月） |

---

## 第十部分：论文结构草案

```
Title: Where You Are Shapes Who You Become: 
       Space Syntax-Informed LLM Agents for Spatially Believable Game Worlds

Abstract (200 words)
  - 问题：LLM游戏Agent是"空间盲"的
  - 方法：引入建筑学Space Syntax理论，提出SpatialAgent架构
  - 实验：系统验证空间感知提升行为可信度 + 空间构型塑造社会涌现
  - 结果：具体数字

1. Introduction (1.5页)
   - LLM Agent的成功与"空间失明"问题
   - 建筑学Space Syntax的核心洞察
   - 本文贡献（4-5条）

2. Related Work (1页)
   2.1 LLM-based Game Agents（Generative Agents → Project Sid → Affordable GA）
   2.2 Space Syntax and Agent Simulation（Hillier → Penn & Turner → 建筑模拟）
   2.3 Context-Aware NPC Systems（Oh et al. 2025 → LIGS → CPDC）
   → 指出三个领域的空白交叉点

3. Theoretical Framework (1页)
   3.1 Space Syntax指标定义（Integration, Connectivity, Visual Depth, Control Value）
   3.2 空间-行为假设 H1-H5
   3.3 空间可供性理论在Agent中的应用

4. SpatialAgent Architecture (1.5页)
   4.1 总体架构图
   4.2 Spatial Perception + 空间→语言转换器
   4.3 Spatial Memory Retrieval
   4.4 Spatial Planning
   4.5 Spatial Action Sampling

5. Experimental Setup (1页)
   5.1 三种空间构型设计
   5.2 Agent配置
   5.3 实验矩阵（Exp1-4）
   5.4 评估指标

6. Results (1.5页)
   6.1 Exp1: 空间感知显著提升行为可信度
   6.2 Exp2: 三种空间构型产生不同社会涌现
   6.3 Exp3: Visual Depth和Integration影响最大
   6.4 Exp4: 人类评估确认空间感知的优势
   6.5 假设验证汇总表（H1-H5）

7. Discussion (0.5页)
   7.1 建筑学理论在虚拟Agent中的验证
   7.2 对游戏设计的实践启示
   7.3 局限性与未来工作

8. Conclusion (0.25页)

References (~50篇)

Appendix（补充材料）
  A. 三种空间构型的完整指标表
  B. 10个NPC人设详情
  C. Prompt模板
  D. 完整实验数据表
```

总页数：约7页正文 + 参考文献（符合AAAI格式要求）
