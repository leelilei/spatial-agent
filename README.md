# SpatialAgent Repository Guide

这个仓库分成三块，看目录时先按这个顺序理解：

- `docs/`
  - 仓库级研究文档、计划、评审、综述、理论笔记。
  - 如果你想看“为什么做、研究怎么设计、文档放哪”，先看这里。
- `scripts/`
  - 仓库级辅助脚本。
  - 主要用于下载论文、整理参考文献、生成参考资料，不属于 `spatial-agent-core/` 子项目本体代码。
- `spatial-agent-core/`
  - 真正的代码子项目。
  - 这里包含实验代码、配置、数据、结果、测试和子项目自己的 README。

## 顶层目录说明

### `docs/`

研究与写作材料统一放这里，目前是仓库唯一文档目录。

- `plans/`: 各版本研究计划与 survey 计划
- `guides/`: 项目搭建、研究推进、写作指导
- `references/`: 论文清单与参考资料来源
- `reviews/`: 对研究计划的评审与 review
- `surveys/`: survey 正文和综述材料
- `vision/`: 早期构想、蓝天方向
- `decisions/`: 关键决策记录
- `meeting_notes/`: 会议纪要
- 根目录下若干 `.md`: 当前实验设计、预实验报告、理论笔记、challenge 报告等专题文档

先读建议：

1. `docs/README.md`
2. `docs/research_plan.md`
3. `docs/preflight_experiments.md`

### `scripts/`

这些是仓库级工具脚本，不是模型/实验主代码。

- `scripts/download_papers.py`: 按整理好的论文清单批量下载 PDF
- `scripts/generate_references.py`: 从文献清单生成参考资料和状态文件
- `scripts/download_arxiv_retry.py`: 对部分 arXiv 论文做补下载重试

### `spatial-agent-core/`

这是实际运行实验的 Python 子项目。

- `src/`: 核心实现代码
- `experiments/`: 预实验和主实验入口
- `configs/`: 配置文件
- `data/`: 输入数据、任务数据或中间原始素材
- `results/`: 实验输出结果
- `references/`: 子项目内部使用的参考文献产物，如 PDF、bib、paper list
- `paper/`: 论文写作相关材料
- `scripts/`: 子项目内部脚本
- `tests/`: 测试
- `README.md`: 子项目运行说明

## 怎么找东西

- 想看研究计划和评审：去 `docs/`
- 想跑代码和实验：去 `spatial-agent-core/`
- 想处理文献与资料整理：去 `scripts/`

## 当前结构原则

- 仓库级文档只放在根目录 `docs/`
- 仓库级辅助脚本只放在根目录 `scripts/`
- 可运行项目代码只放在 `spatial-agent-core/`
