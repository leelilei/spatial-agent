# WikiChurches PU diagnostic

这是 proposal 的阶段一可运行实验目录。它先完成官方框清点和双人盲审，再决定是否启动 PU 方法训练。

2026-07-26 状态：WikiChurches-4 的 CUDA 1-shot / 1-epoch
端到端 smoke 已通过，数据完整性、church-disjoint split、运行日志和结果见
`reports/wikichurches_smoke_20260726/README.md`。该 smoke 不是 PU
有效性证据；真实 PN / Ignore / PU / Oracle 仍以双人盲审裁决为前置条件。

同日增加无裁决探索性路线：
`reports/real_pu_no_adjudication_20260726/README.md`。该路线已在真实
P/U 上完成 PN / Ignore / 三档 nnPU 的 30-repeat 诊断，并否决标准
nnPU；它不包含 Oracle，也不估计真实漏标率。

随后完成 selection-aware propensity-proxy 诊断：
`reports/selection_aware_pu_20260726/README.md`。简单逆 proxy-propensity
加权只带来不稳定的 +0.002 AUC，仍显著差于 Ignore，因此判定 No-Go；
若继续无裁决路线，需要改为具有已知随机纳入概率的候选采样。

已知随机纳入概率实验也已完成：
`reports/stochastic_ipw_pu_20260726/README.md`。IPW 相对未加权 sampled-U
提高 AUC 0.016，并在聚合层面接近 FullPool；但 FullPool 本身仍显著低于
Ignore。因此候选 sampling correction 有限通过，当前 PU 方法整体不通过。

随后以 8 个固定抽样种子完成复现：
`reports/stochastic_ipw_multiseed_20260726/README.md`。共 10,800 行结果；
IPW 相对未加权 nnPU 的 AUC 增益为 `+0.018`
（分层 95% CI `+0.005–+0.034`），但相对 Ignore 仍为 `−0.082`
（`−0.125–−0.043`）。因此抽样校正机制在 AUC 上可复现，PU 方法
No-Go 结论不变。

最后完成不把 U 当负例的保守正例扩展：
`reports/positive_expansion_multiseed_20260726/README.md`。该方法在
8/8 种子上均未超过 Ignore，聚合差值为 AUC `−0.002`、AP `−0.007`，
两个分层 CI 均全负。因此无裁决方法搜索冻结；下一项能识别真实漏标的
实验是完成最小人工盲审。

## 运行

```bash
python3 scripts/analyze_annotations.py \
  --parts data/raw/building_parts.json \
  --out-dir data/derived

python3 scripts/select_audit_sample.py \
  --parts data/raw/building_parts.json \
  --out-dir audit/sealed \
  --seed 20260725
```

将 `audit/sealed/blinded_manifest.csv` 复制到 `audit/blinded/` 后，优先使用
Zenodo ZIP 的 HTTP Range 只提取选中的 50 张：

```bash
python3 -m pip install --target vendor/python -r requirements-bootstrap.txt

PYTHONPATH=vendor/python python3 scripts/extract_selected_from_remote_zip.py \
  --zip-url https://zenodo.org/api/records/5166987/files/images.zip/content \
  --manifest audit/blinded/blinded_manifest.csv \
  --dataset-dir data/dataset_selected \
  --audit-dir audit/blinded/images \
  --max-side 1920
```

`download_selected_images.py` 是 Wikimedia 回退路径；它通过 imageinfo API 获取标准缩略图 URL：

```bash
python3 scripts/download_selected_images.py \
  --manifest audit/blinded/blinded_manifest.csv \
  --image-meta data/raw/image_meta.json \
  --original-dir data/wikimedia_selected \
  --audit-dir audit/blinded/images \
  --download-mode thumbnail \
  --max-side 1920
```

生成盲审 HTML 与密封官方框覆盖图：

```bash
python3 scripts/render_audit_packet.py \
  --manifest audit/blinded/blinded_manifest.csv \
  --parts data/raw/building_parts.json \
  --image-dir audit/blinded/images \
  --blinded-html audit/blinded/index.html \
  --overlay-dir audit/sealed/official_overlays
```

可选的 frozen-CLIP 框外候选排序（只用于人工审计优先级）：

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements-model.txt

.venv/bin/python scripts/clip_outside_box_triage.py \
  --manifest audit/blinded/blinded_manifest.csv \
  --parts data/raw/building_parts.json \
  --image-dir data/dataset_selected \
  --out-dir reports/model_assisted_triage \
  --device auto
```

受控 25% 正框缺失的 PN / Ignore / Oracle 线性探针：

```bash
.venv/bin/python scripts/synthetic_missing_positive_probe.py \
  --manifest audit/blinded/blinded_manifest.csv \
  --parts data/raw/building_parts.json \
  --image-dir data/dataset_selected \
  --out-dir reports/synthetic_missing_positive_probe \
  --device auto \
  --repeats 100
```

无裁决的真实 P/U 诊断：

```bash
TOGA_ROOT=vendor/TOGA .venv/bin/python \
  scripts/real_pu_no_adjudication_probe.py \
  --manifest audit/blinded/blinded_manifest.csv \
  --parts data/raw/building_parts.json \
  --official-boxes data/derived/official_box_inventory.csv \
  --unlabeled-candidates \
    reports/model_assisted_triage/outside_box_candidates.csv \
  --image-dir data/dataset_selected \
  --out-dir reports/real_pu_no_adjudication_local \
  --repeats 30 \
  --class-priors 0.10 0.25 0.50
```

两名标注者完成并裁决为 `audit/annotations/adjudicated.csv` 后：

```bash
python3 scripts/score_completed_audit.py \
  --parts data/raw/building_parts.json \
  --selection audit/sealed/sealed_selection.csv \
  --adjudicated audit/annotations/adjudicated.csv \
  --out-dir reports/audit
```

## 目录边界

- `data/raw/`：官方原始元数据；
- `data/derived/`：可重建统计产物；
- `audit/blinded/`：可交给标注者；
- `audit/sealed/`：官方框和选样依据，不交给标注者；
- `audit/annotations/`：两位标注者的独立结果；
- `reports/`：统计报告与 go/no-go 结论。
