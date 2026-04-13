# A Survey on Large Language Model-Based Game Agents

## 基本信息
- **作者**: Sihao Hu, Tiansheng Huang, Gaowen Liu, Ramana Rao Kompella, Fatih Ilhan, Selim Furkan Tekin, Yichang Xu, Zachary Yahn, Ling Liu
- **发表**: arXiv preprint（2024年4月提交，2025年11月修订）
- **链接**: https://arxiv.org/abs/2404.02039
- **本地 PDF**: `assets/survey_paper/pdfs/03_Hu2024_LLM_Game_Agents_Survey.pdf`
- **阅读日期**: 2026-03-15

## 一句话总结

针对LLM游戏Agent的全面综述，提出统一参考架构（memory-reasoning-perception/action），按六种游戏类型分类分析Agent设计挑战，涵盖单Agent和多Agent两个层级。

## 核心贡献（3点以内）
1. **统一参考架构**：将现有LLM游戏Agent研究归纳为三核心组件框架——Memory（记忆）、Reasoning（推理）、Perception-Action Interface（感知-行动接口）
2. **挑战导向分类法**：将游戏环境按六种类型（动作、冒险、策略、RPG、沙盒、竞技）组织，识别每种类型的主要Agent设计挑战
3. **多Agent扩展**：在单Agent架构之上，系统梳理新增组件——Communication Protocol（通信协议）和 Organizational Model（组织模型），覆盖协作与竞争场景

## 方法
（简要描述核心方法/架构）

**单Agent层级的统一架构**：
- **Memory**：分为短期记忆（对话上下文、最近观察）和长期记忆（向量数据库存储的经历）。综述了 Memory Stream（Park 2023）、MemGPT（Packer 2023）、Reflexion（Shinn 2023）等方案
- **Reasoning**：覆盖 Chain-of-Thought、Tree-of-Thoughts、ReAct 等推理策略。特别讨论了从 text-based 到 multimodal 推理的演进
- **Perception-Action**：输入端支持文本、视觉（截图/像素）、结构化数据（API状态）；输出端支持文本动作、API调用、键鼠操控

**多Agent层级的扩展组件**：
- **Communication**：Agent间消息传递机制，含自由对话、结构化消息、共享黑板
- **Organization**：星型（中心协调者）、链式（顺序传递）、树形（层级命令）、图形（自由连接）四种拓扑

**游戏类型挑战映射**：
- 动作类 → 低延迟控制
- 冒险类 → 长距离规划
- 策略类 → 不完全信息博弈
- RPG类 → 角色一致性 + 开放叙事
- 沙盒类 → 开放目标生成
- 竞技类 → 实时对抗优化

## 关键发现/结论

- LLM游戏Agent在 **sandbox/RPG** 类型中表现最好——开放文本交互天然匹配LLM优势
- 在需要 **精确时序控制** 的动作/竞技类游戏中，LLM仍无法与专用RL/规则AI匹敌
- **记忆系统是最关键的瓶颈**：上下文长度限制导致Agent长期一致性下降，各种外部记忆方案仍不完善
- **空间感知是一个被显著忽视的维度**——综述中几乎没有专门讨论Agent如何理解和利用空间环境的研究
- 多Agent系统中 **graph topology** 在研究场景中表现最优——信息可自由流动而非受限于层级

## 与我们工作的关系
- **可借鉴**:
  - 统一参考架构作为我们定位SpatialAgent的框架——在其Memory-Reasoning-Perception三组件中增加Spatial层
  - 六种游戏类型分类——明确SpatialAgent定位于sandbox/RPG类型
  - 多Agent组织拓扑分类——我们的三种空间构型（Plaza/Labyrinth/Grid）实际上隐含了不同的通信拓扑
  - 论文收录清单（github.com/git-disl/awesome-LLM-game-agent-papers）作为文献追踪资源

- **我们的差异化**:
  - 该综述未识别"空间失明"作为一个独立问题——我们填补这一盲区
  - 综述中的Perception模块讨论视觉/文本感知，但没有涉及建筑级空间感知
  - 综述对"环境"的讨论局限于游戏类型分类，未将环境的空间结构作为影响Agent行为的变量

- **可引用的具体论点**:
  - "sandbox worlds require open-ended goal formation"——支持我们选择sandbox RPG作为实验环境
  - 记忆系统被识别为关键瓶颈——支持我们提出空间增强记忆检索的动机
  - Graph拓扑在多Agent协调中最优——可与我们Grid构型（类似graph拓扑）的实验结果形成呼应

## 值得记住的图/表
- **Figure 1/2**：统一参考架构图——在Related Work中引用此图来定位SpatialAgent的扩展点
- **Table 1**：六种游戏类型的Agent挑战对照表
- **Table X**（多Agent拓扑对比结果）：graph > tree > chain > star 在研究场景中的排序

## 疑问/待确认
- 综述是否在最新修订版（2025.11）中新增了对空间感知相关工作的讨论？需要检查最新版
- 论文中是否明确提到了Space Syntax或建筑学文献？（几乎可以确定没有——这正是我们的Gap）
