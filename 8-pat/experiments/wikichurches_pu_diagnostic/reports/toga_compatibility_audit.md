# TOGA 本机兼容性审计

## 上游版本

- 仓库：`https://github.com/MR-Sherif/TOGA.git`
- commit：`5d6befdd722e2dc924b9f2d2253d78534a46c0c1`
- commit date：2026-06-03

## 已发现的运行阻碍

1. 上游 `utils.py` 在文本编码、cache 构建和特征预计算中直接调用 `.cuda()`；
2. 上游 `main.py` 只在 CUDA 与 CPU 之间选择，没有 MPS 分支；
3. WikiChurches 不在上游 dataset registry 中，需要新增按 church ID 分组的 split；
4. 上游 requirements 未锁版本，不能把一次安装成功当作环境可复现；
5. 当前本机为 Apple M1 Pro 16 GB；完整 100 epoch 图教师训练不适合直接作为首轮诊断。

## 本地最小兼容改动

- 将硬编码 `.cuda()` 改为跟随 CLIP 模型所在 device；
- 载入缓存时显式使用 `map_location=device`；
- 支持环境变量 `TOGA_DEVICE=cpu|mps|cuda`；
- 不改变网络结构、损失或超参数。

## 运行边界

首轮只做：

1. import 和前向 smoke test；
2. 1 epoch、1-shot 的小数据诊断；
3. 与 Tip-Adapter/Ignore 的方向性比较。

在人工补全 Oracle 未完成前，不运行或报告“PU 优于 Oracle”的结论。

## Smoke test 结果

环境：

- Python 3.12；
- PyTorch 2.13.0；
- PyTorch Geometric 2.8.0.post1；
- Apple M1 Pro / MPS。

结果：

| 检查 | 结果 |
|---|---|
| CPU 双图异构图前向 | 通过，graph visual `(2, 32)`，text `(8, 32)`，全部有限 |
| 原生 MPS 前向 | 失败 |
| MPS + CPU fallback 前向 | 通过，输出全部有限 |
| MPS + CPU fallback 反向与 AdamW step | 通过，梯度全部有限 |

原生 MPS 失败点是 PyTorch Geometric 调用的
`aten::_convert_indices_from_coo_to_csr.out` 尚未在 MPS 实现。设置
`PYTORCH_ENABLE_MPS_FALLBACK=1` 可以运行，但会有 CPU/MPS 同步开销。

因此：

- frozen CLIP 特征提取可以原生 MPS；
- TOGA 图教师 smoke test 可以使用 MPS fallback；
- 完整训练的速度和稳定性仍需 1 epoch 计时后再决定；
- 若 1 epoch 明显过慢，应迁移到 CUDA 服务器，而不是在本机硬跑 100 epoch。

## CUDA 服务器复核（2026-07-26）

已在 RTX 2080 8 GB、CUDA 13.2、PyTorch 2.13.0+cu132、
PyTorch Geometric 2.8.0.post1 上完成：

- 通用 PyG CUDA 前向、反向、AdamW step：通过；
- TOGA 双图异构图教师 CUDA 前向、反向、AdamW step：通过；
- EuroSAT 1-shot、batch size 1、seed 1、1 epoch 完整链路：通过；
- 总耗时：113.796 秒；
- 峰值显存：1,372 MiB；
- 运行退出码：0。

EuroSAT smoke 的 test accuracy 为：Zero-shot CLIP 48.35%、
Tip-Adapter 64.01%、1 epoch 后重新搜参的 Tip-Adapter-F 60.32%。
该运行将官方 100 epoch preset 缩短为 1 epoch，结果只用于确认可运行性，
不能作为论文复现或方法有效性证据。

完整日志、环境锁定文件和 checkpoint 见
`reports/server_smoke_20260726/`。

## WikiChurches 真实数据复核（2026-07-26）

新增 `datasets/wikichurches.py` 和 `configs/wikichurches.yaml` 后，已完成：

- 直接读取官方 WikiChurches-4 train/val/test 标签；
- 按 church ID 检查跨 split 泄漏，交集为 0；
- few-shot 支持集按不同 church 采样；
- 7,526 张核心图存在性与解码检查全部通过；
- RTX 2080 上 1-shot、batch size 1、seed 1、1 epoch 完整链路通过；
- 总耗时 86 秒，峰值显存 1,358 MiB，退出码 0。

本次 test accuracy 为 Zero-shot CLIP 56.82%、Tip-Adapter 57.96%、
Tip-Adapter-F 58.16%。这是工程 smoke，不是 TOGA 论文复现，也不是
PU 效应检验。完整日志与数据完整性证据见
`reports/wikichurches_smoke_20260726/`。
