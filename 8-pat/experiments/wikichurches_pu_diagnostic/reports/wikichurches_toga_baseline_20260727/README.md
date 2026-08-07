# WikiChurches-4：Tip-Adapter-F vs TOGA 母体筛选

日期：2026-07-27

## 决策

**TOGA 直接迁移到 WikiChurches-4：当前 No-Go。**

在固定、未针对 WikiChurches 调优的超参数下，TOGA 没有稳定优于真正的
Tip-Adapter-F：

| Shots | Tip-Adapter-F | TOGA | 配对差 TOGA − Tip-F |
|---:|---:|---:|---:|
| 1 | 59.20 ± 1.31 | 58.25 ± 1.05 | −0.94 ± 1.28 |
| 4 | 58.84 ± 1.84 | 57.98 ± 0.85 | −0.85 ± 1.05 |
| 16 | 59.29 ± 0.27 | 58.95 ± 2.34 | −0.34 ± 2.58 |

9 组 matched run 中，TOGA 赢 4 组、输 5 组；全部配对差的描述性平均为
`−0.71 ± 1.56` 个百分点。每个 shot 只有 3 个 seed，区间会很宽，因此这
不是“TOGA 显著更差”的统计结论；它否定的是更弱也更直接的主张：

> 不能假设 TOGA 不经域内验证就能在 WikiChurches 上提供稳定增益。

因此，现阶段不应继续把构件框或 PU 分支接到 TOGA，也不应将 TOGA 写成已经
验证有效的母体。它可以暂时保留为参考方法和待复核对照。

## 协议

- 官方 WikiChurches-4 train/val/test；
- split 按 church ID 审计，跨 split church 交集为 0；
- 1/4/16-shot；
- seeds 1/2/3；
- 每类 shot 来自不同 church；
- CLIP ViT-B/16 frozen；
- 两个方法共享完全相同的 support cache；
- 20 epochs；
- batch size 16；
- validation accuracy 选择 checkpoint；
- cache 的 beta/alpha 只在 validation 上搜索；
- test 不参与 checkpoint、epoch 或超参数选择；
- 每个配置独立保存 JSON 和完整日志。

本次修复了早期 smoke 中按 test accuracy 选择最佳 epoch 的问题；早期 smoke
数值不并入本表。

## 方法边界

### Tip-Adapter-F

只训练 cache adapter，损失为：

\[
\mathcal L_{\mathrm{CE}}
\left(
L_{\mathrm{ZS}}+\alpha L_{\mathrm{Cache}}, y
\right)
\]

不包含图教师。

### TOGA

在同一学生 cache adapter 上增加训练期 image-patch-text 图教师、MGT、
Top-N 节点筛选和教师 Focal Loss。测试时仍只保留 Tip-Adapter-F 路径。

## 运行与完整性

- 实例：NVIDIA GeForce RTX 3080 Ti 12 GB；
- CPU：12 核；
- 内存：32 GB；
- Python 3.12；
- PyTorch 2.13.0+cu132；
- PyTorch Geometric 2.8.0.post1；
- 数据镜像：9,502 张图像；
- WikiChurches-4：train 5,838、val 206、test 1,482；
- 18/18 个正式作业退出码均为 0；
- 正式矩阵端到端约 21 分钟；
- 2 秒 GPU 监控：最高利用率 96%，最高显存 1,680 MiB，
  最高功耗 242.98 W，最高温度 48°C。

图教师的 frozen CLIP 多尺度裁块特征在单次 run 内缓存。该优化不缓存随机
增强的整图分支，不改变网络、训练样本或损失，只避免每个 epoch 重复编码
同一组确定性裁块。

## 解释限制

1. TOGA 论文使用数据集/shot 特定超参数；本实验是固定超参数的域迁移筛选，
   不是对 TOGA 论文结果的完整复现。
2. WikiChurches 不在 TOGA 原论文的 11 个 benchmark 中。
3. 3 seeds 足以发现方向不稳定，但不足以证明很小的差异。
4. 当前结果与构件框无关，不能回答不完整区域标注是否成立。

## 若要继续验证 TOGA

合理的最后一次复核应为：

1. 先在 TOGA 论文中的一个官方 benchmark（建议 EuroSAT）复现论文方向，
   排除实现链路问题；
2. 只用 WikiChurches validation 做小规模超参数选择；
3. 冻结超参数后，使用新的 seeds 4/5/6 做确认，不复用本次 test 结果调参；
4. 若仍不能稳定超过 Tip-Adapter-F，则放弃 TOGA 作为母体。

在完成这项复核前，更保守的研究选择是以 Tip-Adapter-F 作为基线，把 TOGA
降级为比较方法，而不是继续围绕其 Patch 筛选设计构件监督。

## 证据

- `aggregate/README.md`：自动生成的聚合结论；
- `aggregate/per_run_results.csv`：18 个正式结果；
- `aggregate/summary.csv`：按 shot/method 汇总；
- `json/`：每个 run 的机器可读配置与结果；
- `logs/`：每个 run 的完整 stdout/stderr；
- `audit/run_status.tsv`：时间、耗时和退出码；
- `audit/code_sha256.txt`：运行代码哈希；
- `audit/pip_freeze.txt`：环境快照；
- `audit/gpu.csv`：2 秒 GPU 监控。

回收证据包：

- `../wikichurches_toga_baseline_20260727.tar.gz`
- SHA-256:
  `d7b9b77c1f2bed0b4a3b11c9bd048e3805dc83811dff9e7f341c345fb2d2ba11`

