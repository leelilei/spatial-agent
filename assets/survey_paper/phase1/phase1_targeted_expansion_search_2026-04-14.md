# Phase 1 Targeted Expansion Search

日期：2026-04-14  
阶段：`Phase 1` targeted expansion（补强 `Core`，不是扩库）  
目标：补出更多“明确有空间环境 + 社会行为”的 `Core` 候选，并避免再次滑向“泛社会模拟”或“纯空间能力”。

## 1. 本轮策略

本轮不再沿用宽泛的 `LLM social simulation` 搜索，而是把检索焦点收缩到以下交叉边界：

- 明确存在可识别空间环境：`built environment`、`3D virtual environment`、`community`、`grid / world / town`
- 明确存在社会行为：`social interaction`、`collaboration`、`cooperation`、`social norms`、`community dynamics`
- 明确是 LLM / generative agent 系统，而不是纯 benchmark、纯导航、纯单 agent assistant

本轮手工补搜使用的主查询思路：

- `"built environment" "large language model" agents social interactions`
- `"community" "large language model-based" agents movement nearby messages`
- `"large language model" "virtual world" agents social interactions`
- 针对已知锚点做 title backfill：`TravelAgent`、`Lyfe Agents`、`Spontaneous Emergence...`、`community simulation + LLM`

## 2. 新增高置信 Core 候选

以下条目此前不在当前 `Phase 1` 候选池中，本轮判断为值得进入下一轮正式 screening 的高置信 `Core` 候选。

### T01. Lyfe Agents: Generative agents for low-cost real-time social interactions

- 年份：`2023`
- 发表：`CoRR / arXiv`
- DOI：`10.48550/arXiv.2310.02172`
- 链接：
  - `https://arxiv.org/abs/2310.02172`
  - `https://dblp.org/rec/journals/corr/abs-2310-02172`
- 进入原因：
  - 论文明确使用自定义 `LyfeGame` `3D virtual environment platform`
  - 评估对象是多 agent 场景下的 `self-motivation` 与 `sociability`
  - 结果包含自主协作、信息交换、意见变化等社会行为
- 初步判断：
  - 这是比一般“虚拟社会”描述更明确的空间化系统，且不是单纯聊天或纯 benchmark
  - 可作为 `Generative Agents` 路线外的一条独立 `virtual-world social interaction` 样本

### T02. Spontaneous Emergence of Agent Individuality Through Social Interactions in Large Language Model-Based Communities

- 年份：`2024`
- 发表：`Entropy`
- DOI：`10.3390/e26121092`
- 链接：
  - `https://www.mdpi.com/1099-4300/26/12/1092`
  - `https://pmc.ncbi.nlm.nih.gov/articles/PMC11675631/`
- 进入原因：
  - 环境非常明确：`10` 个 LLM agents 处在 `50 x 50` 的 `2D grid` 中
  - agent 会移动，并只和近邻 agent 交换消息，局部共在被写进机制
  - 报告了社会规范、合作、情绪变化、人格分化与社区形成
- 初步判断：
  - 空间环境虽然抽象，但比“无空间的群聊社会模拟”更符合本文 `Core` 边界
  - 很适合作为 `L1-L3` 边界案例，尤其适合分析“空间局部性如何塑造社会涌现”

### T03. Real world community oriented high-definition social simulation: Combining reinforcement learning and large language models

- 年份：`2026`
- 发表：`Cities`
- DOI：`10.1016/j.cities.2025.106468`
- 链接：
  - `https://doi.org/10.1016/j.cities.2025.106468`
  - `https://www.sciencedirect.com/science/article/pii/S0264275125007693`
- 进入原因：
  - 论文基于真实 `GIS / BIM` 数据构建 `Unreal Engine` 高精度 `3D` 社区环境
  - 明确模拟 `3000` 名 AI agents 在社区中的位置、行动与日常活动分布
  - 文中有显式的 `location` / `last location` 观察项与 movement actions
  - 虽是 `RL + LLM` 混合框架，但目标是 community-level social dynamics，而非单纯导航
- 初步判断：
  - 这是目前最接近“社区级空间环境 + 大规模社会行为”的新增命中
  - 需要在正式 screening 时重点核查其 agent-agent social interaction 是否足够直接，但当前值得保留为 `core-candidate`

## 3. 检索到但本轮不纳入新增 Core 的条目

### Exploring Large Language Model-Driven Agents for Environment-Aware Spatial Interactions and Conversations in Virtual Reality Role-Play Scenarios

- 来源：`IEEE VR 2025`
- DOI：`10.1109/vr59515.2025.00025`
- 不纳入原因：
  - 空间环境非常明确，且 agent 会做环境感知与空间交互
  - 但当前更像 `human-AI interaction in VR`，不是多 agent 社会模拟
  - 因此继续维持 `adjacent`，不作为本轮新增 `Core`

### SimWorld: An Open-ended Realistic Simulator for Autonomous Agents in Physical and Social Worlds

- 来源：`arXiv 2025 / NeurIPS 2025 Spotlight`
- DOI：`10.48550/arXiv.2512.01078`
- 不纳入原因：
  - 环境侧非常强，`physical + social worlds` 也很吸引人
  - 但当前主文本更像 simulator / benchmark 平台，展示任务以 delivery、cooperation、competition 为主
  - 现阶段更适合作为后续 `adjacent / future-watch` 候选，而不是本轮“明确空间环境 + 社会行为”的 `Core`

## 4. 本轮结论

本轮 targeted expansion 的主要收获不是数量，而是补到了三类此前 `Core` 中相对稀缺的系统形态：

- `3D virtual-world social interaction`：`Lyfe Agents`
- `explicit local spatiality -> social emergence`：`Spontaneous Emergence...`
- `real-community / urban digital twin social simulation`：`Real world community oriented...`

它们共同改善了当前 `Core` 过于集中在 `Generative Agents / Concordia / sandbox town / Minecraft / digital platform` 这一狭窄带上的问题。

## 5. 建议的下一步

- 将本轮 3 篇新增高置信候选作为独立 seed batch 进入下轮 ingest / dedupe
- screening 时优先核查以下字段：
  - `agent_count`
  - `environment-side representation`
  - `agent-accessible representation`
  - `mobility / co-presence / interaction` 是否同时成立
  - `behavioral_scale` 是否至少达到 `interaction`
- 在当前 `screening_sheet` 仍有未提交改动的情况下，暂不直接改主表，先保留为独立 dated batch
