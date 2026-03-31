# SpatialAgent Repository Guide

这个仓库按四类内容组织：

- `docs/`: 仓库级研究文档与过程材料
- `assets/`: 长期保存的研究资产，如论文 PDF、阅读笔记、分析 notebook
- `scripts/`: 仓库级辅助脚本
- `spatial-agent-core/`: 可运行的代码子项目

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
- `experiments/`: 实验设计与 preflight 文档
- `background/`: 理论背景与 related work
- `reviews/`: challenge 报告与版本 review
- `guides/`: 项目搭建与研究推进指南
- `references/`: 文献索引与参考说明
- `surveys/`, `vision/`, `decisions/`, `meeting_notes/`: 其余研究文档

推荐阅读顺序：

1. `docs/README.md`
2. `docs/plans/README.md`
3. `docs/plans/plan_v7.md`
4. `docs/experiments/preflight_experiments.md`

### `assets/`

只放需要长期保存的研究资产。

```text
assets/
├── analysis/
│   └── notebooks/
└── papers/
    ├── generated/
    ├── pdfs/
    └── reading_notes/
```

- `assets/papers/pdfs/`: 论文 PDF
- `assets/papers/reading_notes/`: 阅读笔记
- `assets/papers/generated/`: 自动生成的 paper list、BibTeX、下载状态
- `assets/analysis/notebooks/`: 分析 notebook

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
├── paper/
├── results/
├── scripts/
├── src/
├── tests/
├── requirements.txt
└── setup.py
```

它只保留代码、配置、数据和运行输出；研究资产已经迁到顶层 `assets/`。

## Structure Rules

- 仓库级文档只放在 `docs/`
- 长期保存的研究资产只放在 `assets/`
- 仓库级工具脚本只放在 `scripts/`
- 可运行项目代码只放在 `spatial-agent-core/`
