# MultiAgentBench: Evaluating the Collaboration and Competition of LLM Agents

## 基本信息
- **作者**: Kunlun Zhu, Hongyi Du, Zhaochen Hong, Xiaocheng Yang, Shuyi Guo, Zhe Wang, Zhenhailong Wang, Cheng Qian, Xiangru Tang, Heng Ji, Jiaxuan You
- **发表**: ACL 2025 (Main Conference)
- **链接**: https://arxiv.org/abs/2503.01935 | GitHub: https://github.com/MultiagentBench/MARBLE
- **阅读日期**: 2026-03-15

## 一句话总结

提出 MultiAgentBench（MARBLE）基准，使用里程碑式KPI系统化评估LLM多Agent系统在协作与竞争场景中的表现，发现 graph 拓扑结构在研究场景中表现最优，cognitive planning 可提升里程碑达成率3%。

## 核心贡献（3点以内）
1. **里程碑式KPI评估体系**：超越简单的任务完成率，引入分阶段里程碑指标来衡量多Agent协作的过程质量——不仅看最终结果，还看协作过程中各阶段的达成情况
2. **协调拓扑对比实验**：系统比较了 star（星型，中心协调者）、chain（链式）、tree（树形）、graph（图形，自由连接）四种Agent间协调拓扑的效果
3. **创新协调策略**：提出 group discussion（小组讨论）和 cognitive planning（认知规划）两种新策略，后者通过让Agent在行动前进行自我推理提升了里程碑达成率

## 方法
（简要描述核心方法/架构）

**基准设计：**
- 涵盖多种交互场景：合作研究、谈判、辩论、竞争博弈等
- 每个场景定义了一系列有序里程碑（milestones），如"达成信息共享→形成研究方案→完成分工→产出成果"
- KPI = 已达成里程碑数 / 总里程碑数 × 任务特定权重

**四种协调拓扑：**
- **Star**：一个中心Agent协调所有其他Agent——效率高但中心瓶颈
- **Chain**：消息按顺序传递——适合流水线任务
- **Tree**：层级式命令与汇报——适合有明确层级的任务
- **Graph**：所有Agent可自由互相通信——最灵活但通信开销大

**测试的LLM**：GPT-4o, GPT-4o-mini, Claude-3.5-Sonnet, Llama-3 等

## 关键发现/结论

- **GPT-4o-mini** 取得最高平均任务分数——性价比最优
- **Graph拓扑在研究场景中表现最好**——自由信息流动有利于创造性协作
- **Star拓扑在执行类任务中表现较好**——中心化协调适合有明确目标的任务
- **Cognitive planning** 将里程碑达成率提升了约**3%**——让Agent行动前先"想清楚"有帮助
- 多Agent系统的主要瓶颈不是单个Agent的推理能力，而是**Agent间的信息传递效率和协调质量**
- **空间环境对协调效果的影响未被考虑**——所有拓扑都是逻辑层面的，不涉及物理空间布局

## 与我们工作的关系
- **可借鉴**:
  - 里程碑式KPI评估方法——我们可以为信息传播实验设计类似的里程碑（谣言传播到25%/50%/75%/100% Agent的轮数）
  - 四种拓扑的实验设计——我们的三种空间构型（Plaza/Labyrinth/Grid）隐含了不同的通信拓扑：Plaza≈Star（广场为中心），Labyrinth≈Chain（线性通道），Grid≈Graph（多中心互连）
  - GPT-4o-mini作为性价比最优选择——我们的LLM选型可参考

- **我们的差异化**:
  - MultiAgentBench的拓扑是**逻辑层面的预设规则**（规定谁能和谁通信），而我们的空间构型是**物理层面的环境约束**（空间结构自然限制谁更可能遇到谁）
  - 我们不是预设通信拓扑，而是让**空间构型自然涌现**出通信模式——更接近真实世界
  - 将MultiAgentBench的逻辑拓扑与我们的物理空间构型进行关联分析，可以产生一个有趣的讨论点

- **可引用的具体论点**:
  - "Graph topology performs best in research scenarios"——与我们Grid构型（类似graph）的预期优势形成呼应
  - "协调质量比个体推理更重要"——支持我们的论点：空间构型通过影响Agent间的相遇概率来影响协调质量
  - 里程碑式评估优于简单完成率——支持我们采用多维度评估指标

## 值得记住的图/表
- **Figure X**：四种拓扑结构示意图——可在论文中与我们的三种空间构型进行视觉对比
- **Table X**：不同拓扑×不同LLM的性能矩阵——参数选择参考
- **Figure X**：里程碑达成率随时间变化的曲线

## 疑问/待确认
- Graph拓扑在研究场景最优，那在社交模拟场景呢？论文是否有此类场景的测试？
- 是否可以在MARBLE框架内增加"空间约束"维度来评估SpatialAgent？
- Cognitive planning的具体实现——让Agent先生成推理链再行动？与我们的Spatial Action Sampling有何异同？
