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

```bash
# 克隆仓库
git clone <repo-url>
cd spatial-agent-core

# 创建虚拟环境
python -m venv .venv
source .venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 配置 API keys
cp .env.example .env
# 编辑 .env 填入你的 API keys

# 运行基础实验
python experiments/run_exp1.py
```

## 项目结构
详见 `../docs/guides/project_setup_guide.md`

## 资产位置

本子项目只保留代码、配置、数据和运行结果。

- 论文 PDF：`../assets/papers/pdfs/`
- 阅读笔记：`../assets/papers/reading_notes/`
- 生成的 BibTeX / paper list：`../assets/papers/generated/`
- 分析 notebooks：`../assets/analysis/notebooks/`

## 引用
```bibtex
@article{spatialagent2026,
  title={SpatialAgent: Space Syntax-Informed LLM Agents for Spatially Believable Game Worlds},
  author={},
  year={2026}
}
```
