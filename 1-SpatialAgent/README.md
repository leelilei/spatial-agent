# SpatialAgent Repository Guide

这个仓库按四类内容组织：

- `docs/`: 仓库级研究文档与过程材料
- `assets/`: 长期保存的研究资产，如论文 PDF、阅读笔记
- `scripts/`: 仓库级辅助脚本
- `spatial-agent-core/`: 可运行的代码子项目

Survey 项目已拆出到独立目录 `../4-SpatialAgent-Survey/`。

## Top-Level Layout

```text
.
├── docs/
├── assets/
├── scripts/
├── spatial-agent-core/
├── README.md
├── .gitignore
└── openai.png
```

## What Goes Where

### `docs/`

只放说明性文档，不放大体积研究资产或运行产物。

- `plans/`: 研究计划与版本迭代
- `reviews/`: challenge 报告与版本 review
- `experiments/`: 实验设计与 preflight 文档
- `guides/`: 项目搭建与研究推进指引
- `background/`: 理论背景、related work 和 survey 材料
- `project/`: 项目级辅助文档，包括参考索引、vision、决策与会议纪要

推荐阅读顺序：

1. `docs/README.md`
2. `docs/plans/README.md`
3. `docs/plans/plan_v8_2.md`
4. `docs/guides/project_setup_guide_v2.md`
5. `docs/experiments/preflight_experiments.md`

### `assets/`

只放需要长期保存的研究资产。

```text
assets/
└── papers/
    ├── generated/
    ├── pdfs/
    └── reading_notes/
```

- `assets/papers/pdfs/`: 论文 PDF
- `assets/papers/reading_notes/`: 阅读笔记
- `assets/papers/generated/`: 自动生成的 paper list、BibTeX、下载状态

### `scripts/`

这些是仓库级工具脚本。

- `scripts/download_papers.py`: 下载论文 PDF 到 `assets/papers/pdfs/`
- `scripts/generate_references.py`: 生成 `assets/papers/generated/` 中的索引文件
- `scripts/download_arxiv_retry.py`: 补下载部分 arXiv 论文

### `spatial-agent-core/`

这是实际运行实验的 Python 子项目。

```text
spatial-agent-core/
├── README.md
├── configs/
├── data/
├── experiments/
├── notebooks/
├── paper/
├── results/
├── scripts/
├── src/
├── tests/
├── requirements.txt
└── setup.py
```

它保留代码、配置、数据、分析 notebook 和运行输出；研究文献资产已经迁到顶层 `assets/`。

### Survey Project

SpatialAgent survey 已迁移为独立项目：

```text
../4-SpatialAgent-Survey/
├── docs/
├── assets/
└── spatial-agent-survey/
```

其中 `spatial-agent-survey/` 继续负责检索导入、screening、evidence table、QC、导出和综述论文组装。

## Structure Rules

- 仓库级文档只放在 `docs/`
- 长期保存的研究资产只放在 `assets/`
- 仓库级工具脚本只放在 `scripts/`
- 可运行项目代码只放在 `spatial-agent-core/`
- survey 相关可运行代码、表格、论文组装和专题资产只放在 `../4-SpatialAgent-Survey/`
