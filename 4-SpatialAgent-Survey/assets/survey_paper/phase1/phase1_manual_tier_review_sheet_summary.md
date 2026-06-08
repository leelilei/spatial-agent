# Phase 1 Manual Tier Review Sheet Summary

日期：2026-04-13

## 总体情况

- 总保留池：`117` 篇
- `core`：`21`
- `adjacent`：`43`
- `foundational`：`53`

## 本地 PDF 覆盖情况

- `core`: ready=`8`, metadata_only=`0`, missing=`13`
- `adjacent`: ready=`6`, metadata_only=`1`, missing=`36`
- `foundational`: ready=`4`, metadata_only=`1`, missing=`48`

## 下载建议

- `local_pdf_ready`: `18` 篇，可直接全文复核
- `download_before_fulltext_screen`: `13` 篇，若摘要复核后仍保留为 `Core`，建议优先下载
- `abstract_first_download_if_retained`: `86` 篇，先做摘要复核，不需要立即下载全文

## 摘要字段覆盖情况

- 英文摘要来自 candidate pool：`99`
- 英文摘要来自 local PDF 抽取：`10`
- 英文摘要仍缺失：`8`
- 中文摘要已填充：`117`
- 中文摘要待填充：`0`

## 建议人工复核顺序

1. 先看 `core + local_pdf_ready`
2. 再看 `core + missing PDF`，确认值得保留后再补全文
3. 然后处理 `adjacent`
4. 最后收束 `foundational`，防止理论文献无限膨胀

## 主文件

- `phase1_manual_tier_review_sheet_2026-04-13.csv`
- `phase1_manual_tier_review_sheet_translation_input_2026-04-13.json`
