# SpatialAgent Repository Guide

这个仓库现在按“文档 / 工具 / 代码子项目”三层来组织：

- `docs/`
  - 仓库级研究文档、计划、评审、综述、理论笔记。
- `scripts/`
  - 仓库级辅助脚本，主要处理论文下载、文献整理、参考资料生成。
- `spatial-agent-core/`
  - 真正可运行的代码子项目，包含实验、配置、数据、结果和测试。

## 顶层目录树

```text
.
├── docs/
├── scripts/
├── spatial-agent-core/
├── README.md
├── .gitignore
└── openai.png
```

## `docs/` 是什么

`docs/` 是仓库唯一文档目录，已经按主题归档。

```text
docs/
├── README.md
├── background/      # 理论背景与 related work
├── decisions/       # 关键决策记录
├── experiments/     # 实验设计与 preflight 文档
├── guides/          # 项目搭建与研究推进指南
├── meeting_notes/   # 会议纪要
├── plans/           # 各版研究计划与当前主计划
├── references/      # 文献清单与参考资料来源
├── reviews/         # challenge 报告与各版 review
├── surveys/         # survey 正文与综述材料
└── vision/          # 方向构想与蓝天草案
```

推荐阅读顺序：

1. `docs/README.md`
2. `docs/plans/README.md`
3. `docs/plans/spatial_agent_research_plan_v7.md`
4. `docs/experiments/preflight_experiments.md`

## `scripts/` 是什么

这些脚本是仓库级工具，不是主项目代码。

- `scripts/download_papers.py`
  - 按文献清单批量下载 PDF。
- `scripts/generate_references.py`
  - 生成文献列表、BibTeX 和下载状态。
- `scripts/download_arxiv_retry.py`
  - 对部分 arXiv 论文做补下载重试。

## `spatial-agent-core/` 是什么

这是实际运行实验的 Python 子项目。

```text
spatial-agent-core/
├── README.md
├── configs/         # 配置文件
├── data/            # 输入数据与原始素材
├── experiments/     # 实验入口
├── paper/           # 论文写作材料
├── references/      # 子项目内部参考文献产物
├── results/         # 实验输出
├── scripts/         # 子项目内部脚本
├── src/             # 核心实现代码
├── tests/           # 测试
├── requirements.txt
└── setup.py
```

## 怎么找东西

- 想看研究计划、背景、评审：去 `docs/`
- 想跑代码和实验：去 `spatial-agent-core/`
- 想整理文献和辅助资料：去 `scripts/`

## 当前结构原则

- 仓库级文档只放在根目录 `docs/`
- 仓库级辅助脚本只放在根目录 `scripts/`
- 可运行项目代码只放在 `spatial-agent-core/`
