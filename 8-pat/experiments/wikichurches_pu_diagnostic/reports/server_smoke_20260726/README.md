# CUDA 服务器真实数据 smoke test

日期：2026-07-26  
性质：环境与完整训练链路诊断，不是论文复现

## 结论

**通过。** RTX 2080 8 GB 服务器能够运行当前本地兼容版 TOGA 的
PyTorch Geometric CUDA 前向/反向，以及 EuroSAT 1-shot、1 epoch 的完整
CLIP → cache → Tip-Adapter → graph teacher → Tip-Adapter-F 链路。

本次结果只证明链路可运行。由于将官方 EuroSAT 1-shot preset 的
`batch_size=16, train_epoch=100` 改为 `batch_size=1, train_epoch=1`，
不能把下列准确率与论文表格直接比较，也不能据此判断 TOGA 是否有效。

## 服务器审计

| 项目 | 实测 |
|---|---|
| 系统 | Ubuntu 22.04.5 LTS，容器化环境 |
| GPU | NVIDIA GeForce RTX 2080，8,192 MiB，compute capability 7.5 |
| 驱动 / CUDA toolkit | 595.80 / 13.2 |
| CPU / 内存 | 8 vCPU / 39 GiB，无 swap |
| 可用磁盘 | 初始约 76 GiB；实验后约 70 GiB |
| Python | 3.12.11 |
| PyTorch / torchvision | 2.13.0+cu132 / 0.28.0+cu132 |
| PyTorch Geometric | 2.8.0.post1 |

环境位于独立 Conda 环境 `toga-smoke`；未修改系统驱动或全局 CUDA。
完整环境见 `environment.yml` 和 `pip-freeze.txt`。

## 数据与权重

- EuroSAT：27,000 张图、10 类；
- 固定划分：train 13,500、val 5,400、test 8,100；
- 划分中缺失路径：0；
- split SHA-256：
  `541503a77d0b26b735d85ec7a3e672804fe0aa466c2e5f07da772cc6c0af8ad2`；
- CLIP ViT-B/16 SHA-256：
  `5806e77cd80f8b59890b7e101eabd078d9fb84e6937f9e85e4ecb61988df416f`。

EuroSAT 通过 torchvision 固定 revision 下载器获得并执行内置 MD5 校验；
固定 train/val/test 划分遵循 CoOp/Tip-Adapter 目录和协议。

## 运行配置

```text
dataset=eurosat
shots=1
backbone=ViT-B/16
seed=1
batch_size=1
train_epoch=1
num_workers=0
wandb_mode=disabled
device=cuda
hard_timeout=1740 seconds
```

TOGA 上游基线 commit：
`5d6befdd722e2dc924b9f2d2253d78534a46c0c1`。
运行副本包含本地设备兼容改动，主要文件哈希记录在
`logs/final_resource_audit.log`。

## 结果

| 阶段 | 指标 |
|---|---:|
| Zero-shot CLIP val accuracy | 48.37% |
| Tip-Adapter val accuracy（preset 初值） | 59.31% |
| Tip-Adapter val accuracy（搜参） | 64.54% |
| Zero-shot CLIP test accuracy | 48.35% |
| Tip-Adapter test accuracy | 64.01% |
| 1 epoch 训练准确率 | 20.00%（2/10） |
| 1 epoch loss | 13.5564 |
| Tip-Adapter-F test accuracy（训练后 preset 初值） | 56.00% |
| Tip-Adapter-F test accuracy（重新搜参） | 60.32% |

总耗时 113.796 秒。真实运行退出码为 0。

1 epoch 后的最终 Tip-Adapter-F（60.32%）低于未训练 Tip-Adapter
（64.01%），差值为 -3.69 个百分点。这是欠训练条件下的 smoke 结果，
不支持“TOGA 改善性能”的结论。

## GPU 资源

| 指标 | 实测 |
|---|---:|
| 峰值显存 | 1,372 MiB |
| 峰值 GPU 利用率 | 99% |
| 峰值功耗 | 211.01 W |
| 运行后残留 GPU 进程 | 0 |

因此 8 GB 显存在 `batch_size=1` 的 EuroSAT smoke 中有充分余量。
但 WikiChurches 的区域/patch 数可能更大，仍需单独记录图节点数分布和显存峰值，
不能从本次结果直接外推完整 PN / Ignore / PU / Oracle 实验。

## 透明失败记录

以下失败均保留在日志中，且未被描述为成功：

1. 第一次通用 PyG smoke 错把双输入卷积放入标准 `nn.Sequential`，
   触发调用签名错误；显式 GCN 重试后通过。
2. 首个真实运行命令引用了精简镜像中不存在的 `/usr/bin/time`，
   在 Python 启动前退出 127；改用 shell 内置计时后成功。
3. DFKI 原始下载端证书链在精简系统 CA 下验证失败，未使用 `curl -k`；
   改用 torchvision 固定 revision、带 MD5 的镜像。
4. Google Drive split 下载长时间无输出后被中止；改用公开 GitHub 镜像，
   并验证 split 计数、SHA-256 和全部 27,000 条图像路径。

## 产物索引

- 完整真实运行：`logs/eurosat_1shot_1epoch_retry.log`
- GPU 5 秒采样：`logs/eurosat_1shot_1epoch_retry_gpu.csv`
- 环境安装：`logs/conda_clone.log`、`logs/pip_install.log`
- PyG CUDA smoke：`logs/pyg_cuda_smoke_retry.log`
- TOGA graph teacher CUDA smoke：`logs/toga_teacher_cuda_smoke.log`
- 最终资源审计：`logs/final_resource_audit.log`
- 小型 checkpoint/cache：`best_F_1shots.pt`、`keys_1shots.pt`、
  `values_1shots.pt`

## 对 proposal 的含义

服务器与 TOGA 链路已不再是阻碍。下一步应把 WikiChurches 先作为普通
few-shot 分类数据接入，验证 split、类别和 1-shot 单 seed 单 epoch；
随后再进入 PN / Ignore / PU / Oracle。正式 PU 结论仍受双人盲审、
裁决后 Missing Positive Rate 和真实 Oracle 标签规模约束。
