# TOGA EuroSAT 官方方向复现

日期：2026-07-27

## 裁决

**实现链路通过，但“TOGA 稳定大幅超过强配对 Tip-Adapter-F”的主张未通过。**

TOGA 的绝对准确率曲线接近论文报告值，五个 shot 的平均绝对差仅为
`1.03` 个百分点；特别是 2/4/8/16-shot，差距均不超过 `1.01` 点。
这足以排除 WikiChurches 负结果由明显的数据、模型或训练链路错误造成。

| Shots | 内部 Tip-F | TOGA | 配对差 | 论文 Tip-F | 论文 TOGA | TOGA 与论文差 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 68.72 ± 2.82 | 65.16 ± 4.76 | −3.56 ± 5.77 | 59.5 | 67.4 | −2.24 |
| 2 | 75.65 ± 3.84 | 74.02 ± 2.97 | −1.63 ± 1.93 | 66.1 | 74.9 | −0.88 |
| 4 | 78.81 ± 0.28 | 79.29 ± 1.21 | +0.47 ± 1.22 | 74.1 | 80.3 | −1.01 |
| 8 | 82.99 ± 2.81 | 83.58 ± 1.89 | +0.58 ± 1.10 | 77.9 | 84.1 | −0.52 |
| 16 | 88.21 ± 0.92 | 88.93 ± 0.63 | +0.72 ± 0.41 | 84.5 | 89.4 | −0.47 |

五个 shot、三个 seed 共 15 组配对中，TOGA 赢 7 组、输 8 组。整体配对差
为 `−0.68 ± 2.95` 点，主要由 1-shot seed 2 的 `−9.96` 点驱动。

16-shot 是最稳定的正向结果：三个 seed 的 TOGA 增益分别为
`+1.20/+0.48/+0.48`。4-shot 和 8-shot 虽然均值为正，但都只有一个 seed
明显获益。

## 为什么这仍算实现链路复现通过

本次复现的主要控制目标是论文 TOGA 绝对曲线，而不是要求内部基线逐字等于
论文引用的历史 Tip-Adapter-F 行：

- 论文 TOGA：67.4 / 74.9 / 80.3 / 84.1 / 89.4；
- 本次 TOGA：65.16 / 74.02 / 79.29 / 83.58 / 88.93；
- 曲线单调性、量级和高 shot 端均得到复现；
- 2–16-shot 的单点偏差为 0.47–1.01 点。

内部 Tip-F 使用当前 TOGA 仓库的 shot-specific preset、相同的 support
sample、validation checkpoint 选择和 validation cache 超参数搜索，因此它
比论文表中引用的历史 Tip-Adapter-F 行高 3.71–9.55 点。它是更严格的内部
因果对照，但不应被误写成对历史论文行的同协议复现。

## 协议

- 官方 EuroSAT RGB 图像：27,000 张；
- CoOp/Tip-Adapter 固定 split：
  train 13,500 / val 5,400 / test 8,100；
- 10 类，split 中 27,000 条路径全部存在；
- CLIP ViT-B/16，backbone frozen；
- 1/2/4/8/16-shot；
- seeds 1/2/3；
- TOGA 仓库提供的 dataset/shot-specific presets；
- 每个配置 100 epochs；
- Tip-F 与 TOGA 使用同一 seed、同一 support sample；
- checkpoint 只按 validation accuracy 选择；
- beta/alpha 只在 validation 上搜索；
- test 在模型和超参数固定后评估一次；
- 30/30 个最终作业均退出码 0。

论文主文写明 AdamW 初始学习率为 `1e-3`，但公开仓库的 EuroSAT presets
按 shot 提供的学习率分别约为
`0.0028/0.0050/0.0339/0.0240/0.0436`。本次选择仓库 presets，因为仓库
“Reproducing Results”入口明确会自动加载 dataset/shot preset。这个
论文—代码差异必须在任何复现声明中保留。

## 机器使用与运行

- NVIDIA GeForce RTX 3080 Ti 12 GB；
- 12 CPU cores，32 GB RAM；
- Python 3.12；
- PyTorch 2.13.0+cu132；
- 2 秒 GPU 监控共 1,988 个样本；
- GPU 利用率峰值 100%，P95 98%；
- 显存峰值 9,594 MiB；
- 功耗峰值 337.03 W；
- 温度峰值 61°C。

正式运行从 `09:14:32` 到 `11:15:41` UTC。初始 6 路并行虽然提高了 GPU
占用，但使 5 个长任务触发 30 分钟保护性超时；这些任务随后以 3 路并行、
60 分钟上限完整重跑，最终 30 个结果全部成功。超时的部分结果未进入聚合。

## 对 WikiChurches 的含义

EuroSAT 控制实验改变了故障定位：

1. TOGA 的公开实现能够在母数据集上形成接近论文的绝对性能曲线；
2. WikiChurches 上没有稳定增益，更可能是域适配或超参数失配，而不是实现
   链路完全错误；
3. 但强配对基线显示 TOGA 的边际收益远小于论文历史表格暗示的幅度，尤其在
   1/2-shot 不稳定；
4. 因此仍不能直接把 TOGA 设为 proposal 的已验证母体，更不能立即接入
   构件框或 PU 分支。

合理的最后验证是：只使用 WikiChurches validation 对 teacher 相关超参数
做小规模选择，冻结后用全新的 seeds 4/5/6 对 Tip-F 与 TOGA 做配对确认。
seeds 1/2/3 的 test 已经看过，不能再作为无偏确认集。

## 证据

- `formal/aggregate/README.md`：自动聚合结果；
- `formal/aggregate/per_run_results.csv`：30 个逐次结果；
- `formal/aggregate/summary.csv`：按 shot/method 汇总及论文差值；
- `formal/json/`：机器可读的运行配置与结果；
- `formal/logs/`：完整 stdout/stderr；
- `formal/audit/run_status.tsv`：最终 30 个任务状态；
- `formal/audit/code_sha256.txt`：运行代码哈希；
- `formal/audit/data_sha256.txt`：数据与 split 哈希；
- `formal/audit/pip_freeze.txt`：环境快照；
- `formal/audit/gpu*.csv`：2 秒 GPU 监控。

回收证据包：

- `../eurosat_toga_reproduction_20260727.tar.gz`
- SHA-256:
  `37deb7e30749c905ef5ccf9c71bc52af231e4d235531dce10b8ec2cc2178bb32`

## 外部依据

- TOGA 论文：https://arxiv.org/abs/2603.18101
- TOGA 官方仓库：https://github.com/MR-Sherif/TOGA
- Tip-Adapter 数据准备协议：
  https://github.com/gaopengcuhk/Tip-Adapter/blob/main/DATASET.md
