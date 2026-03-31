# SpatialAgent 研究项目：项目框架搭建指南

> 本文档用于指导 Claude Code 搭建完整的研究项目结构。
> 请按照以下目录结构和文件说明，创建所有文件夹和初始文件。

---

## 一、项目根目录结构

```
spatial-agent-core/
├── README.md                          # 项目总览（含一句话描述、快速开始、引用格式）
├── LICENSE                            # MIT License
├── .gitignore                         # Python/Node/LaTeX 通用忽略规则
├── requirements.txt                   # Python 依赖
├── setup.py                           # 可选，用于 pip install -e .
│
├── docs/                              # 文档与计划
│   ├── plans/spatial_agent_research_plan_current.md # 完整研究计划（RQ、假设、时间线）
│   ├── experiments/experiment_design.md # 实验设计详细说明
│   ├── background/spatial_theory.md   # Space Syntax 理论笔记（给不懂建筑学的读者）
│   ├── background/related_work.md     # 相关工作梳理与定位
│   ├── meeting_notes/                 # 讨论/会议记录
│   │   └── 2026-03-09_kickoff.md
│   └── decisions/                     # 关键设计决策记录（ADR风格）
│       └── 001_model_selection.md
│
├── references/                        # 参考论文管理
│   ├── papers.bib                     # BibTeX 文件（所有参考文献统一管理）
│   ├── reading_notes/                 # 论文阅读笔记（每篇一个md）
│   │   ├── park2023_generative_agents.md
│   │   ├── hillier1984_social_logic_of_space.md
│   │   ├── turner2001_visibility_graph.md
│   │   ├── affordable_generative_agents_2024.md
│   │   ├── oh2025_spatially_aware_llm.md
│   │   └── template.md               # 阅读笔记模板
│   └── paper_list.md                  # 必读论文清单（含优先级和阅读状态）
│
├── src/                               # 核心源代码
│   ├── __init__.py
│   │
│   ├── space/                         # Space Syntax 空间计算模块
│   │   ├── __init__.py
│   │   ├── graph.py                   # 空间拓扑图构建（基于NetworkX）
│   │   ├── metrics.py                 # Space Syntax 指标计算
│   │   │                              #   - Integration（整合度）
│   │   │                              #   - Connectivity（连通性）
│   │   │                              #   - Visual Depth（视觉深度）
│   │   │                              #   - Control Value（控制值）
│   │   ├── visibility.py              # 可见性图分析（VGA）
│   │   └── layouts.py                 # 预定义空间构型（广场型/迷宫型/网格型）
│   │
│   ├── agent/                         # Agent 核心架构
│   │   ├── __init__.py
│   │   ├── base_agent.py              # 基础 Agent 类（无空间感知的baseline）
│   │   ├── spatial_agent.py           # SpatialAgent（带空间感知模块）
│   │   ├── perception.py              # Spatial Perception 模块
│   │   │                              #   - 空间属性→自然语言转换器
│   │   │                              #   - 空间上下文注入逻辑
│   │   ├── memory.py                  # 记忆系统（含空间记忆检索）
│   │   ├── planning.py                # 空间效用规划（Goal-Conditioned Spatial Utility）
│   │   ├── action_sampling.py         # 空间条件化行为采样算法
│   │   └── persona.py                 # NPC 人设定义与管理
│   │
│   ├── world/                         # 游戏世界模拟
│   │   ├── __init__.py
│   │   ├── engine.py                  # 模拟引擎主循环
│   │   ├── world_state.py             # 世界状态管理（Agent位置、事件队列）
│   │   ├── event_system.py            # 事件系统（对话、移动、交易等）
│   │   └── renderer.py                # 文本渲染器（将模拟过程输出为可读文本）
│   │
│   ├── llm/                           # LLM 调用封装
│   │   ├── __init__.py
│   │   ├── client.py                  # API 调用封装（支持 Qwen/GPT-4o/DeepSeek）
│   │   ├── prompts.py                 # Prompt 模板管理
│   │   ├── judge.py                   # LLM-as-Judge 评估调用
│   │   └── cache.py                   # API 结果缓存（避免重复调用浪费钱）
│   │
│   └── analysis/                      # 分析工具
│       ├── __init__.py
│       ├── social_network.py          # 社交网络构建与分析（NetworkX）
│       ├── information_spread.py      # 信息传播追踪
│       ├── persona_drift.py           # 人格漂移检测
│       ├── spatial_behavioral.py      # 空间-行为相关性分析
│       └── visualization.py           # 可视化工具（地图、网络图、时序图）
│
├── configs/                           # 配置文件
│   ├── default.yaml                   # 默认实验配置
│   ├── layouts/                       # 空间构型配置
│   │   ├── plaza.yaml                 # 地图A：中心化广场型
│   │   ├── labyrinth.yaml             # 地图B：迷宫通道型
│   │   └── grid.yaml                  # 地图C：多中心网格型
│   ├── agents/                        # Agent 人设配置
│   │   ├── elara_merchant.yaml        # 商人 Elara
│   │   ├── theron_guard.yaml          # 守卫 Theron
│   │   └── ...                        # 其他NPC（共10个）
│   └── experiments/                   # 实验配置
│       ├── exp1_spatial_vs_baseline.yaml
│       ├── exp2_layout_comparison.yaml
│       ├── exp3_ablation.yaml
│       └── exp4_human_eval.yaml
│
├── data/                              # 数据目录
│   ├── raw/                           # 原始模拟输出
│   │   └── .gitkeep
│   ├── processed/                     # 处理后的数据
│   │   └── .gitkeep
│   ├── human_eval/                    # 人类评估数据
│   │   ├── questionnaire.md           # 评估问卷设计
│   │   ├── instructions.md            # 评估者指南
│   │   └── responses/                 # 评估结果
│   │       └── .gitkeep
│   └── synthetic/                     # 合成训练数据（如果需要微调）
│       └── .gitkeep
│
├── experiments/                       # 实验运行脚本
│   ├── run_exp1.py                    # Exp1: 空间感知 vs 无空间感知
│   ├── run_exp2.py                    # Exp2: 三种空间构型对比
│   ├── run_exp3.py                    # Exp3: 空间指标消融
│   ├── run_exp4_prep.py               # Exp4: 生成人类评估材料
│   └── run_all.sh                     # 一键运行所有自动化实验
│
├── results/                           # 实验结果
│   ├── figures/                       # 论文用图表
│   │   └── .gitkeep
│   ├── tables/                        # 论文用表格数据
│   │   └── .gitkeep
│   ├── logs/                          # 实验日志
│   │   └── .gitkeep
│   └── analysis_notebooks/            # 分析用 Jupyter notebooks
│       ├── 01_spatial_metrics_overview.ipynb
│       ├── 02_exp1_results.ipynb
│       ├── 03_exp2_layout_comparison.ipynb
│       ├── 04_exp3_ablation.ipynb
│       ├── 05_social_network_analysis.ipynb
│       └── 06_human_eval_analysis.ipynb
│
├── paper/                             # 论文写作
│   ├── main.tex                       # 论文主文件（AAAI格式）
│   ├── references.bib                 # 论文参考文献（从 references/papers.bib 同步）
│   ├── sections/                      # 分章节管理
│   │   ├── 01_introduction.tex
│   │   ├── 02_related_work.tex
│   │   ├── 03_theory.tex              # Space Syntax 理论框架
│   │   ├── 04_architecture.tex        # SpatialAgent 架构
│   │   ├── 05_experiments.tex
│   │   ├── 06_results.tex
│   │   ├── 07_discussion.tex
│   │   └── 08_conclusion.tex
│   ├── figures/                       # 论文图片源文件
│   │   └── .gitkeep
│   ├── supplementary/                 # 补充材料
│   │   └── appendix.tex
│   └── templates/                     # 会议 LaTeX 模板
│       └── aaai2027/                  # AAAI-27 模板
│           └── .gitkeep
│
├── scripts/                           # 工具脚本
│   ├── setup_env.sh                   # 环境安装脚本
│   ├── scripts/download_papers.py     # 批量下载参考论文PDF
│   ├── calculate_costs.py             # API 调用成本估算器
│   ├── export_results.py              # 导出实验结果为论文表格格式
│   └── validate_layout.py             # 验证空间构型的 Space Syntax 指标
│
└── tests/                             # 单元测试
    ├── test_space_metrics.py          # 测试空间指标计算正确性
    ├── test_agent_perception.py       # 测试空间感知模块
    ├── test_memory_retrieval.py       # 测试空间记忆检索
    ├── test_action_sampling.py        # 测试行为采样算法
    └── test_simulation.py             # 测试模拟引擎基本流程
```

---

## 二、关键初始文件内容

### 2.1 README.md 应包含

```markdown
# SpatialAgent: Space Syntax-Informed LLM Agents for Spatially Believable Game Worlds

> "Where You Are Shapes Who You Become"

## 一句话描述
将建筑学 Space Syntax 理论引入 LLM 游戏 Agent，
首次系统性研究空间构型如何影响多 Agent 社会行为涌现。

## 核心假设
- H1: 高 Integration 区域 → Agent 社交互动频率更高
- H2: 低 Visual Depth 区域 → Agent 更倾向透露秘密信息
- H3: 高 Control Value 节点 → Agent 更容易涌现领导者角色
- H4: 空间 Connectivity 分布 → 影响信息传播速度
- H5: 空间构型整体差异 → 导致不同的社会涌现模式

## 快速开始
（安装和运行说明）

## 项目结构
（指向本文档）

## 引用
（BibTeX 格式）
```

### 2.2 references/paper_list.md 应包含

```markdown
# 必读论文清单

## 优先级说明
- P0: 必须精读，直接影响论文设计
- P1: 需要精读，Related Work 核心引用
- P2: 需要泛读，补充背景知识

## 论文列表

### 游戏 AI / LLM Agent
| 优先级 | 论文 | 状态 | 笔记 |
|--------|------|------|------|
| P0 | Park et al. "Generative Agents" (UIST 2023) | ☐ 未读 | [笔记](reading_notes/park2023_generative_agents.md) |
| P0 | "Affordable Generative Agents" (arXiv:2402.02053) | ☐ 未读 | [笔记](reading_notes/affordable_generative_agents_2024.md) |
| P1 | Oh et al. "Spatially Aware LLM Agents" (IEEE TVCG 2025) | ☐ 未读 | [笔记](reading_notes/oh2025_spatially_aware_llm.md) |
| P1 | "LLM Game Agent Survey" (arXiv:2404.02039) | ☐ 未读 | |
| P1 | Project Sid - Altera (2024) | ☐ 未读 | |
| P2 | "MultiAgentBench" (arXiv:2503.01935) | ☐ 未读 | |
| P2 | "LIGS" (CHI EA 2025) | ☐ 未读 | |

### 建筑学 / Space Syntax
| 优先级 | 论文 | 状态 | 笔记 |
|--------|------|------|------|
| P0 | Hillier & Hanson "The Social Logic of Space" (1984) Ch.3-5 | ☐ 未读 | [笔记](reading_notes/hillier1984_social_logic_of_space.md) |
| P0 | Turner et al. "From Isovists to Visibility Graphs" (2001) | ☐ 未读 | [笔记](reading_notes/turner2001_visibility_graph.md) |
| P1 | Penn & Turner "Space Syntax Based Agent Simulation" (2001) | ☐ 未读 | |
| P1 | Hillier "Space is the Machine" (1996) Ch.1-3 | ☐ 未读 | |
| P2 | Al-Sayed et al. "Space Syntax Methodology" (2014) | ☐ 未读 | |

### 方法论
| 优先级 | 论文 | 状态 | 笔记 |
|--------|------|------|------|
| P1 | "Artificial Leviathan" - LLM Agent 社会演化 (2024) | ☐ 未读 | |
| P1 | "AgeMem" - Agent 记忆管理 (arXiv:2601.01885) | ☐ 未读 | |
| P2 | "SARAH" - Spatially Aware Real-time Agentic Humans (2026) | ☐ 未读 | |
```

### 2.3 references/reading_notes/template.md 应包含

```markdown
# [论文标题]

## 基本信息
- **作者**:
- **发表**:（会议/期刊，年份）
- **链接**:
- **阅读日期**:

## 一句话总结


## 核心贡献（3点以内）
1.
2.
3.

## 方法
（简要描述核心方法/架构）

## 关键发现/结论


## 与我们工作的关系
- **可借鉴**:
- **我们的差异化**:
- **可引用的具体论点**:

## 值得记住的图/表
（记录图表编号和要点）

## 疑问/待确认

```

### 2.4 docs/experiments/experiment_design.md 应包含

```markdown
# 实验设计

## 实验总览

| 实验 | 目的 | 自变量 | 因变量 | 预计工作量 |
|------|------|--------|--------|-----------|
| Exp1 | 验证空间感知提升行为可信度 | 有/无空间感知 | 行为可信度评分 | 2周 |
| Exp2 | 验证空间构型塑造涌现 | 3种空间构型 | 社交网络指标 | 2周 |
| Exp3 | 消融各空间指标的贡献 | 逐个去除指标 | 行为可信度 | 1周 |
| Exp4 | 人类评估 | 有/无空间感知 | 主观评分 | 2周 |

## Exp1: 空间感知 vs Baseline
### 条件设置
### 运行参数
### 评估指标
### 预期结果

## Exp2: 三种空间构型对比
### 地图设计原则
### 控制变量
### 评估指标
### 假设对应

## Exp3: 消融实验
### 消融矩阵
### 评估方法

## Exp4: 人类评估
### 被试招募
### 评估流程
### 问卷设计
### 统计分析方法
```

### 2.5 configs/default.yaml 应包含

```yaml
# SpatialAgent 默认实验配置

project:
  name: "spatial-agent"
  version: "0.1.0"
  seed: 42

simulation:
  num_rounds: 200          # 每次模拟轮数
  num_repeats: 5           # 每个条件重复次数
  num_agents: 10           # Agent 数量

llm:
  provider: "qwen"         # qwen / openai / deepseek
  model: "qwen-max"        # 具体模型名
  temperature: 0.7
  max_tokens: 512
  cache_enabled: true
  cache_dir: "data/llm_cache"

judge:
  provider: "openai"
  model: "gpt-4o"
  dimensions:
    - fluency
    - persona_consistency
    - spatial_appropriateness
    - coherence

space:
  metrics:
    - integration
    - connectivity
    - visual_depth
    - control_value
  spatial_to_language: true  # 是否启用空间→语言转换

agent:
  memory:
    max_items: 100
    spatial_retrieval_weight: 0.3   # δ in retrieval formula
  action_sampling:
    num_candidates: 5
    spatial_scoring: true
  planning:
    spatial_utility: true

output:
  base_dir: "data/raw"
  log_level: "INFO"
```

### 2.6 docs/decisions/001_model_selection.md 应包含

```markdown
# ADR-001: LLM 模型选择

## 状态
待定

## 背景
需要选择 Agent 推理用的 LLM 和 Judge 评估用的 LLM。

## 候选方案
| 方案 | 模型 | 优势 | 劣势 | 成本 |
|------|------|------|------|------|
| A | Qwen-Max (API) | 中文强、便宜 | 闭源 | ~¥0.02/千token |
| B | GPT-4o (API) | 质量最高 | 贵 | ~$0.01/千token |
| C | DeepSeek-V3 (API) | 极便宜 | 质量不确定 | ~¥0.001/千token |

## 决策


## 理由


## 后果

```

---

## 三、Python 依赖 (requirements.txt)

```
# 核心
networkx>=3.0          # 图计算、Space Syntax、社交网络分析
numpy>=1.24
pandas>=2.0
pyyaml>=6.0
pydantic>=2.0          # 数据模型验证

# LLM
openai>=1.0            # GPT API
httpx>=0.25            # 通用 HTTP 客户端（Qwen/DeepSeek API）

# 分析与可视化
matplotlib>=3.7
seaborn>=0.12
scipy>=1.10            # 统计检验
scikit-learn>=1.3      # 聚类、相关性分析

# Jupyter
jupyter>=1.0
ipykernel>=6.0

# 测试
pytest>=7.0

# 工具
tqdm>=4.65             # 进度条
python-dotenv>=1.0     # 环境变量管理（API keys）
diskcache>=5.6         # API 结果磁盘缓存
```

---

## 四、.gitignore 应包含

```
# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/
.eggs/
*.egg
venv/
.venv/

# 环境变量（API keys）
.env

# 数据（大文件不入库）
data/raw/*
data/processed/*
data/human_eval/responses/*
data/synthetic/*
data/llm_cache/*
!data/**/.gitkeep

# Jupyter
.ipynb_checkpoints/

# LaTeX
paper/*.aux
paper/*.log
paper/*.out
paper/*.synctex.gz
paper/*.fdb_latexmk
paper/*.fls
paper/*.bbl
paper/*.blg
paper/*.pdf

# 实验日志
results/logs/*
!results/logs/.gitkeep

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
```

---

## 五、第一周要完成的任务清单

搭建完项目框架后，按以下顺序推进：

```markdown
### Week 1 Checklist

- [ ] 用 Claude Code 按本文档创建完整目录结构
- [ ] 配置 .env 文件（API keys）
- [ ] pip install -r requirements.txt
- [ ] 实现 src/space/graph.py 基础版（能构建空间图）
- [ ] 实现 src/space/metrics.py（至少 Integration 和 Connectivity）
- [ ] 在 configs/layouts/ 中设计三种空间构型的初始版本
- [ ] 运行 scripts/validate_layout.py 确认指标计算正确
- [ ] 精读 Generative Agents 论文，写阅读笔记
- [ ] 精读 Hillier "Social Logic of Space" Ch.3-5，写阅读笔记
- [ ] 手绘三种空间构型草图，拍照存入 docs/
```

---

## 六、给 Claude Code 的指令模板

将以下内容粘贴给 Claude Code 来创建项目：

```
请按照 docs/guides/project_setup_guide.md 中的目录结构，
创建 spatial-agent-core/ 项目的完整文件夹和初始文件。

具体要求：
1. 创建所有文件夹和 .gitkeep 文件
2. 创建所有 __init__.py 文件（内容为空或含模块说明注释）
3. 创建 README.md（按文档中的模板）
4. 创建 requirements.txt（按文档中的内容）
5. 创建 .gitignore（按文档中的内容）
6. 创建 configs/default.yaml（按文档中的内容）
7. 创建 references/paper_list.md（按文档中的内容）
8. 创建 references/reading_notes/template.md（按文档中的内容）
9. 创建 docs/ 下的所有 .md 文件（用文档中的模板填充框架内容）
10. 创建 docs/decisions/001_model_selection.md
11. 所有 Python 源文件创建时添加模块级 docstring 说明该文件的职责
12. 初始化 git 仓库并做第一次 commit

不需要实现具体逻辑，只需要创建文件骨架和注释说明。
```
