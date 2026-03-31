# Space Syntax 理论笔记

> 本文档面向不熟悉建筑学的读者，介绍 Space Syntax 的核心概念。

## 什么是 Space Syntax？
Space Syntax 是由 Bill Hillier 和 Julienne Hanson 在 1984 年提出的空间分析理论，
用于研究空间构型（spatial configuration）与人类行为之间的关系。

## 核心概念

### 1. Integration（整合度）
- 定义：衡量一个空间节点与其他所有节点的平均拓扑距离
- 含义：Integration 高的区域更容易到达，通常是人流聚集的中心
- 与本项目的关系：预测 Agent 社交互动的热点区域

### 2. Connectivity（连通性）
- 定义：一个空间节点直接连接的邻居节点数量
- 含义：Connectivity 高的节点是局部交通枢纽
- 与本项目的关系：影响信息传播的局部速度

### 3. Visual Depth（视觉深度）
- 定义：从一个位置能看到多少其他位置
- 含义：Visual Depth 低的区域更私密、更封闭
- 与本项目的关系：影响 Agent 是否愿意分享敏感信息

### 4. Control Value（控制值）
- 定义：衡量一个节点对其邻居通行的控制程度
- 含义：Control Value 高的节点是必经之路
- 与本项目的关系：预测领导者角色的涌现位置

## 可见性图分析 (VGA)
（TODO: 补充 Visibility Graph Analysis 的详细说明）

## 参考文献
- Hillier, B., & Hanson, J. (1984). The Social Logic of Space.
- Turner, A., et al. (2001). From Isovists to Visibility Graphs.
