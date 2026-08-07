# WikiChurches CUDA smoke test

日期：2026-07-26

## 结论

WikiChurches-4 已接入 TOGA/Tip-Adapter 代码，并在 RTX 2080 8 GB
上完成真实数据的 1-shot、seed 1、1 epoch 端到端运行。

- 退出码：0；
- 总耗时：86 秒；
- 峰值显存：1,358 MiB；
- Zero-shot CLIP test accuracy：56.82%；
- Tip-Adapter test accuracy：57.96%；
- 1 epoch 后重新搜索超参数的 Tip-Adapter-F test accuracy：58.16%。

该结果只证明数据、采样、特征提取、训练和评估链路可运行。单一 seed、
单一 shot、单一 epoch 的结果不是方法复现，也不构成 PU 方法有效性的证据。

## 数据与完整性

标签来自 WikiChurches 官方 Zenodo 记录 `5166987`。官方 12.39 GB
图像归档的直连速度不足以在本次实例时段内完成，因此图像使用
[Hugging Face 社区镜像](https://huggingface.co/datasets/LZSI-2/WikiChurches)
的 40 个 tar 分片，并用官方本地材料交叉校验。

校验结果：

- 官方 `image_meta.json`：9,502 个文件名；
- 镜像：9,502 张 JPEG，约 12 GB；
- 50 张从官方归档取得的审计样本：SHA-256 50/50 完全一致；
- WikiChurches-4 的 train/val/test 缺图数：0/0/0；
- WikiChurches-4 的 7,526 张图：7,526/7,526 可完整解码；
- 全量文件名差异为 56 行，对应 28 个原始 `.png/.tif` 文件在镜像中
  转换为同 stem 的 `.jpg`；这些文件不影响 WikiChurches-4 三个 split。

40 个分片均先通过 `tar -tf`，再解包；分片 SHA-256、网络重试和文件名
差异均保存在 `logs/`。

## split 与 few-shot 约束

适配器直接读取官方 `wc4_train.txt`、`wc4_val.txt` 和 `wc4_test.txt`：

| split | 图像数 | church 数 |
|---|---:|---:|
| train | 5,838 | 5,750 |
| val | 206 | 199 |
| test | 1,482 | 1,469 |

跨 split 的 church ID 交集为 0。1-shot 支持集按 church 采样，每类只取
一个不同 church；seed 1 选择：

- Romanesque：`Q1464203`；
- Gothic：`Q16318342`；
- Renaissance：`Q3585377`；
- Baroque：`Q538329`。

## 运行配置

- GPU：NVIDIA GeForce RTX 2080 8 GB；
- CUDA：13.2；
- Python：3.12；
- PyTorch：2.13.0+cu132；
- PyTorch Geometric：2.8.0.post1；
- backbone：CLIP ViT-B/16；
- shots：1；
- batch size：1；
- augmentation epochs：10；
- fine-tuning epochs：1；
- seed：1；
- Weights & Biases：disabled；
- 硬超时：1,740 秒。

服务器与本地副本的 `datasets/wikichurches.py`、
`datasets/__init__.py`、`configs/wikichurches.yaml`、`main.py` 和
`utils.py` SHA-256 完全一致，具体值见
`logs/synced_code_sha256.txt`。

## 结果

| 方法 | validation accuracy | test accuracy |
|---|---:|---:|
| Zero-shot CLIP | 64.56% | 56.82% |
| Tip-Adapter | 66.02% | 57.96% |
| Tip-Adapter-F，1 epoch | 68.45%（重新搜参） | 58.16% |

Tip-Adapter-F 相对 Zero-shot 的单次差值为 +1.34 个百分点，相对
Tip-Adapter 为 +0.20 个百分点。这里不做统计推断。

## 证据文件

- `logs/wikichurches_1shot_1epoch.log`：完整 stdout/stderr；
- `logs/wikichurches_1shot_1epoch.status`：退出码与耗时；
- `logs/gpu_wikichurches_1shot_1epoch.csv`：5 秒间隔 GPU 监控；
- `logs/wikichurches_1shot_1epoch.gpu_summary`：峰值显存；
- `logs/wc4_decode_audit.log`：核心 7,526 张解码审计；
- `logs/official_selected_sha256_check.log`：50 张官方样本字节校验；
- `logs/official_mirror_name_diff.txt`：全量扩展名差异；
- `logs/hf_download_extract.log`：分片下载、重试和解包记录；
- `logs/hf_parts_sha256.txt`：分片 SHA-256；
- `logs/synced_code_sha256.txt`：运行代码哈希。

## 下一实验门

CUDA 与真实分类链路不再是阻塞项。下一步仍是：

1. 完成 40 张 core sample 的双人盲审与裁决；
2. 用裁决结果构建真实 PN / Ignore / PU / Oracle 区域诊断；
3. 再把区域教师差异接入同一 WikiChurches few-shot 分类协议，并以多 seed、
   多 shot 报告均值、方差和配对差值。

