# 3-SMGA 决策日志

记录「为什么这么做」的关键决策。每条一段，最新在上。
（初始条目整理自 docs/guides/project_map.yaml 的 milestones，后续请据实补充。）

## 2026-06-11 把 SMGA 拆成独立项目工作区

- **背景**：SMGA 原本与 spatial-agent 其它工作混在一起，进度难追踪。
- **决定**：拆成独立项目，带独立 todo 清单与项目文档。
- **理由**：让工作区清楚、可恢复，并能按关键里程碑稳定提交。

## 2026-06-11 冻结研究方案与 schema

- **背景**：要进入工程实现，需要先把研究设计与数据结构定稳。
- **决定**：固定 Proposal v4.6、Memory Schema v0.1、Scenario Package Schema v0.1、
  Normalized Probe Response Schema v0.1。
- **理由**：方案与 schema 稳定到足以支撑实现，再开始写代码，避免返工。

## 2026-06-11 先搭 Experiment 0 基础设施

- **背景**：需要一条可重复的「校验—加载—打分」闭环才能评估模型响应。
- **决定**：先把手写的 seed_0001 做成 validate-load-score benchmark 闭环
  （validate_seed.py / benchmark_loader.py / probe_success_scorer.py）。
- **理由**：先有稳定的评测闭环，再跑 baseline，结果才可信、可复现。
