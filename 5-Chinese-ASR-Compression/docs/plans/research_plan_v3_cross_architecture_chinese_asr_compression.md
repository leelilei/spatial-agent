# 研究规划 v3：跨架构中文语音识别模型压缩与端侧部署系统性研究

## 一、选题定位与创新空间

### 1.1 研究背景

中文自动语音识别（ASR）正经历架构范式的快速迭代。以Whisper为代表的自回归（AR）模型、以Paraformer/SenseVoice为代表的非自回归（NAR）模型、以及Fun-ASR-Nano/Qwen2-Audio为代表的LLM-based模型，在准确率上已接近甚至超过人类水平。然而，这些模型的参数量普遍在200M-8B之间，无法直接部署在手机等资源受限设备上。

与此同时，真实IoT产品（如AI录音笔）的主控芯片（如杰理JL7012：640KB RAM）与ASR模型需求之间存在巨大的资源鸿沟，要求设计合理的端云协同架构。

**现有模型压缩研究的盲区**：几乎所有压缩工作都聚焦于Whisper，但Whisper在中文ASR上已不是最优选择。阿里达摩院的Paraformer（非自回归，推理速度比Whisper快10倍以上）和SenseVoice（多任务理解，70ms处理10秒音频）在中文场景下显著优于同级别Whisper，却没有人系统研究过它们的压缩特性。

**核心问题**：对于手机端离线中文ASR，应该压缩哪个架构的模型？AR（Whisper）、NAR（Paraformer/SenseVoice）还是LLM-based？它们在压缩后的准确率-速度-内存Pareto曲线上表现如何？

### 1.2 硬件约束分析（录音笔实际场景）

| 参数 | 杰理 JL7012（录音笔） | Android手机（推理端） | 说明 |
|------|---------------------|---------------------|------|
| CPU | 双核 160MHz DSP | 骁龙680+ (2GHz+) | 手机算力是录音笔的10倍+ |
| RAM | 640KB | 4-8GB | 手机可运行压缩后模型 |
| NPU | 无 | 骁龙有Hexagon DSP | 可加速INT8推理 |
| 连接 | BLE v6.0 | BLE + WiFi | 录音笔→手机音频传输 |
| 角色 | 录音 + VAD + 传输 | ASR推理 + 后处理 | 端-机分工 |

**结论**：录音笔负责高质量录音和智能语音段检测，压缩后的ASR模型部署在配套手机App上实现离线识别。

### 1.3 现有工作的Gap

| 现有工作 | 做了什么 | 没做什么（你的空间） |
|---------|---------|-------------------|
| **DQ-Whisper** (Shao et al., 2023) | 联合蒸馏+量化压缩Whisper，8-bit | 只压缩Whisper；只到8-bit；未对比NAR模型 |
| **LoRA-INT8 Whisper** (Zhang et al., 2025) | LoRA+INT8量化Whisper-tiny做粤语ASR | 只做粤语，只做Whisper，只到INT8 |
| **Distil-Whisper** (Gandhi et al., 2023) | 蒸馏Whisper实现6x加速 | 只做英语；只做Whisper蒸馏 |
| **SLMQuant** (Wang et al., 2025) | 首个SLM量化benchmark | 只做NLP文本模型，没涉及语音 |
| **LieQ** (Xiao et al., 2025) | 混合精度量化SLM到2-bit | 只在文本LLM验证，未用于语音模型 |
| **FunASR** (阿里达摩院) | Paraformer/SenseVoice开源+部署工具 | 未研究压缩/量化对NAR模型的影响 |
| **WhisperKit** (Argmax, 2025) | Whisper在Apple设备实时部署 | 仅Apple生态；未做中文优化；未对比其他架构 |

**关键发现：没有任何工作系统对比过不同架构（AR vs NAR）中文ASR模型的压缩特性。**

### 1.4 你的差异化定位

**论文标题方向**：

*Which Model to Compress? A Cross-Architecture Benchmark for On-Device Chinese ASR*

或

*TinyASR-ZH: Compressing Paraformer, SenseVoice, and Whisper for Offline Chinese Speech Recognition on Mobile Devices*

**核心贡献（4个亮点）**：

1. **首个跨架构中文ASR压缩Benchmark**：系统对比Whisper(AR)、Paraformer(NAR)、SenseVoice(多任务NAR)三大架构在LoRA微调→知识蒸馏→混合精度量化pipeline下的表现，揭示不同架构的压缩特性差异
2. **NAR模型压缩特性的新发现**：Paraformer的非自回归并行解码架构在量化时的敏感性分析——NAR模型是否比AR模型更robust/更fragile？这是全新的研究问题
3. **Tone-Aware压缩策略**：针对中文声调设计的loss函数，在三种架构上验证其通用性，分析不同架构对声调信息的编码差异
4. **端-机协同系统验证**：JL7012录音笔（TinyVAD前端）+ 手机端最优压缩模型的完整pipeline，报告真实产品场景下的端到端指标

---

## 二、中文ASR模型对比基线

### 2.1 候选基座模型

| 模型 | 架构类型 | 参数量 | 解码方式 | 训练数据 | AISHELL-1 CER | 推理特点 |
|------|---------|--------|---------|---------|--------------|---------|
| **Whisper-Small** | AR Encoder-Decoder | 244M | 自回归逐token生成 | 68万h多语言弱监督 | ~8% | 慢，依赖sequential decoding |
| **Whisper-Tiny** | AR Encoder-Decoder | 39M | 自回归 | 同上 | ~18% | 中速，模型小但精度差 |
| **Paraformer-large** | NAR (非自回归) | 220M | 并行一次性输出 | 6万h中文标注 | ~3-5% | 极快，RTF≈0.009 |
| **Paraformer-zh** (streaming) | NAR 流式 | 220M | 流式并行 | 6万h中文 | ~5-7% | 实时流式，延迟<600ms |
| **SenseVoice-Small** | NAR 多任务 | 234M | 并行，支持ASR+情感+事件 | 40万h多语言 | ~4-6% | 比Whisper-Small快5倍+ |

### 2.2 架构差异对压缩的潜在影响（研究假说）

| 维度 | AR (Whisper) | NAR (Paraformer/SenseVoice) | 研究问题 |
|------|-------------|----------------------------|---------|
| 解码依赖 | Token间强依赖 | 并行独立输出 | 量化误差是否会在AR中累积放大？ |
| Decoder复杂度 | 多层自注意力+交叉注意力 | Predictor+Sampler+并行Decoder | NAR的Predictor对量化敏感吗？ |
| 蒸馏难度 | Teacher-Student对齐成熟 | NAR的token预测对齐方式不同 | 如何为NAR设计有效的蒸馏策略？ |
| 中文优化程度 | 多语言通用，中文非最优 | 专为中文优化训练 | 压缩后中文优势是否保持？ |

**核心假说**：NAR模型（Paraformer）由于并行解码不存在误差累积，在量化后可能比AR模型（Whisper）更鲁棒。如果成立，这将是论文的重要发现。

---

## 三、系统架构

### 3.1 整体端-机协同架构

```
┌─────────────────────────────────────────────────────────────────┐
│                    TinyASR-ZH 系统架构                           │
├─────────────────────┬───────────────┬───────────────────────────┤
│   录音笔端 (JL7012)   │   传输层       │   手机端 (Android)          │
│   640KB RAM          │   BLE Audio   │   4-8GB RAM               │
│                     │               │                           │
│  ┌───────────────┐  │               │  ┌───────────────────┐    │
│  │ 麦克风采集      │  │               │  │ 最优压缩ASR模型     │    │
│  │ 24bit/16kHz   │  │               │  │ (Paraformer/Whisper│    │
│  └───────┬───────┘  │               │  │  /SenseVoice       │    │
│          ▼          │               │  │  压缩后 ~15-30MB)  │    │
│  ┌───────────────┐  │               │  │                   │    │
│  │ TinyVAD        │  │  BLE 音频流    │  │ ONNX Runtime      │    │
│  │ (<100KB)       │──┼──────────────►│  │ Mobile 推理        │    │
│  │ 语音活动检测    │  │               │  └─────────┬─────────┘    │
│  │ + 静音过滤     │  │               │            ▼              │
│  └───────────────┘  │  ◄────────────┼──┌───────────────────┐    │
│                     │   文本结果     │  │ 文本输出 + 时间戳    │    │
└─────────────────────┴───────────────┴──└───────────────────┘────┘
```

### 3.2 模块分工

| 模块 | 运行位置 | 功能 | 资源需求 |
|------|---------|------|---------|
| **TinyVAD** | JL7012 录音笔 | 语音/静音检测，只传有效语音段 | <100KB模型，<50KB RAM |
| **音频编码** | JL7012 录音笔 | 16kHz PCM → LC3/SBC编码传输 | JL7012原生支持 |
| **压缩ASR模型** | Android手机 | 离线中文语音识别 | ~15-30MB模型，~200MB运行 |
| **后处理** | Android手机 | 标点恢复(ct-punc)、时间戳对齐 | 轻量模型 |

---

## 四、技术路线图

### 4.1 Part A — 跨架构压缩Benchmark（论文核心）

对三大架构的模型施加**统一的压缩pipeline**，公平对比：

```
                    统一压缩流水线
                    ┌─────────────────┐
Whisper-Small ──────┤                 │
(244M, AR)         │  Step 1: LoRA   │
                    │  中文微调       │
Paraformer-large ──┤                 ├──► 压缩后模型 ──► 手机端评测
(220M, NAR)        │  Step 2: 知识   │    (CER/RTF/
                    │  蒸馏(可选)     │     内存/功耗)
SenseVoice-Small ──┤                 │
(234M, NAR多任务)   │  Step 3: 混合   │
                    │  精度量化       │
                    │  (4/8-bit)     │
                    │                 │
                    │  Step 4: 手机端 │
                    │  ONNX部署       │
                    └─────────────────┘
```

### 4.2 各步骤技术细节

**Step 1 — 中文LoRA微调**

对三个基座模型统一进行中文数据微调：

- LoRA配置：rank=8, alpha=16
- 训练数据：AISHELL-1 (178h) + WenetSpeech精选子集 (500h)
- Whisper：微调全部encoder+decoder attention层
- Paraformer：微调encoder attention + Predictor + Decoder层
- SenseVoice：微调encoder attention + Decoder层（冻结非ASR任务头）
- **创新点 — Tone-Aware Loss**：
  - 在标准CTC/Attention loss基础上，增加声调混淆对惩罚项
  - 构建~2000对中文声调最小对词表（如"买mǎi/卖mài"、"问wèn/吻wěn"）
  - 对三种架构统一施加，分析不同架构对声调信息的编码差异
  - Loss = L_ASR + λ·L_tone，其中λ为声调惩罚权重

**Step 2 — 知识蒸馏（架构内蒸馏）**

由于三种模型架构不同，采用架构内蒸馏策略：

| Teacher | Student | 蒸馏方法 |
|---------|---------|---------|
| Whisper-Small (244M) | Whisper-Tiny (39M) | Logit KD + Hidden Dynamic Matching (DQ-Whisper方案) |
| Paraformer-large (220M) | Paraformer-small/剪枝版 (~60M) | Logit KD + Predictor对齐蒸馏（需创新设计） |
| SenseVoice-Small (234M) | SenseVoice剪枝版 (~60M) | Logit KD + ASR-head选择性蒸馏 |

**创新点**：为Paraformer的NAR架构设计蒸馏策略——NAR模型的Predictor模块负责预测token数量，如何在蒸馏中保持这个能力是一个新问题。

**Step 3 — 混合精度量化**

- 方法：Post-Training Quantization (PTQ)
- 统一使用AWQ/GPTQ方法，适配不同架构
- 混合精度策略：
  - 层级敏感性分析：逐层量化到低bit → 测CER退化 → 排序
  - 敏感层保持8-bit，冗余层压到4-bit
  - **关键对比**：AR模型的Decoder层 vs NAR模型的Predictor/Sampler层的量化敏感性差异
- 量化配置扫描：FP16 → INT8 → INT4 → Mix4/8

**Step 4 — 手机端部署**

- 统一导出为ONNX格式
- 使用ONNX Runtime Mobile在Android上推理
- 优化：算子融合、KV-cache优化（AR模型）、多线程调度
- 测试硬件：
  - 中端机：骁龙680/天玑7200级别，4-6GB RAM
  - 高端机：骁龙8 Gen2+，8-12GB RAM

### 4.3 Part B — TinyVAD端侧模块（系统贡献）

在JL7012上部署超轻量VAD：

- 模型：基于简化RNNoise/FSMN-VAD的微型版本，<100KB
- 功能：实时判断"有没有人在说话"，静音段不传输
- 部署：TensorFlow Lite Micro 或纯C实现
- 预期效果：减少30-50%无效音频传输，降低手机端功耗

### 4.4 Part C — 端到端系统集成

录音笔TinyVAD → BLE传输 → 手机端最优压缩模型 → 文字输出

---

## 五、实验设计

### 5.1 数据集

| 数据集 | 规模 | 用途 | 特点 |
|-------|------|------|------|
| AISHELL-1 | 178h | 主训练+标准评测 | 朗读风格，干净，学术标配 |
| AISHELL-2 | 1000h | 扩展训练（可选） | 更大规模 |
| WenetSpeech (子集) | ~500h | 训练微调 | 会议/播客/有声书多场景 |
| Common Voice zh-CN | ~100h | 多样性测试 | 社区贡献，口音丰富 |
| 自有录音笔数据 | 50-100h | 真实场景测试 | 会议/远场/噪声/多人 |
| MUSAN + RIR | - | 噪声增强 | 训练VAD + 测试鲁棒性 |

### 5.2 核心实验矩阵

#### 表1：基线对比（FP16，无压缩）

| 模型 | 架构 | 参数量 | 模型大小 | AISHELL-1 CER | RTF (手机) |
|------|------|--------|---------|--------------|-----------|
| Whisper-Large-V3 | AR | 1.55B | ~3GB | ~5% | >1 (不可用) |
| Whisper-Small | AR | 244M | 488MB | ~8% | ~0.8 |
| Whisper-Tiny | AR | 39M | 78MB | ~18% | ~0.15 |
| Paraformer-large | NAR | 220M | 440MB | ~3-5% | ~0.05 |
| SenseVoice-Small | NAR | 234M | 468MB | ~4-6% | ~0.03 |

#### 表2：压缩后对比（核心实验）

| ID | 基座模型 | 压缩方法 | 量化 | 目标大小 | 预期CER | 预期RTF |
|----|---------|---------|------|---------|---------|---------|
| W1 | Whisper-Tiny | LoRA | FP16 | 78MB | ~14% | ~0.15 |
| W2 | Whisper-Tiny | LoRA+KD | FP16 | 78MB | ~11% | ~0.15 |
| W3 | Whisper-Tiny | LoRA+Tone+KD | Mix4/8 | ~20MB | ~11% | ~0.10 |
| **P1** | **Paraformer剪枝** | **LoRA** | **FP16** | **~120MB** | **~5-7%** | **~0.03** |
| **P2** | **Paraformer剪枝** | **LoRA+KD** | **FP16** | **~120MB** | **~4-6%** | **~0.03** |
| **P3** | **Paraformer剪枝** | **LoRA+Tone+KD** | **Mix4/8** | **~25-30MB** | **~5-8%** | **~0.02** |
| S1 | SenseVoice剪枝 | LoRA | FP16 | ~120MB | ~5-7% | ~0.02 |
| S2 | SenseVoice剪枝 | LoRA+KD | FP16 | ~120MB | ~5-7% | ~0.02 |
| S3 | SenseVoice剪枝 | LoRA+Tone+KD | Mix4/8 | ~25-30MB | ~6-9% | ~0.015 |

**预期关键发现**：P3（压缩后的Paraformer，~25MB）的CER可能在5-8%，远优于W3（压缩后的Whisper Tiny，~20MB，CER~11%），同时推理速度也更快。如果验证成立，这将是论文最有价值的结论。

#### 表3：极致压缩探索

| ID | 基座模型 | 量化 | 目标大小 | 预期CER | 意义 |
|----|---------|------|---------|---------|------|
| W4 | Whisper-Tiny+KD | 2-bit | ~10MB | ~15%+ | AR极限 |
| P4 | Paraformer剪枝+KD | 2-bit | ~15MB | ~10%? | NAR极限（关键实验） |
| S4 | SenseVoice剪枝+KD | 2-bit | ~15MB | ~12%? | 多任务NAR极限 |

### 5.3 系统级评测

| 评测维度 | 指标 | 测试条件 |
|---------|------|---------|
| 准确率 | CER (%) | AISHELL-1 test + 自有录音笔数据 |
| 手机端延迟 | RTF, 首字延迟 (ms) | 骁龙680 / 骁龙8 Gen2 |
| 手机端内存 | 峰值RSS (MB) | Android profiler |
| 手机端功耗 | mW, mAh/小时 | 1小时持续识别 |
| 端到端延迟 | 说话→出文字 (ms) | 含VAD+BLE传输+推理 |
| VAD节省 | 传输数据量减少比例 (%) | 会议/独白/嘈杂场景 |

### 5.4 消融实验

**模型压缩消融：**
- Tone-Aware Loss在三种架构上的效果差异
- 量化位宽扫描：FP16→INT8→INT4→INT2，三条Pareto曲线对比
- AR Decoder vs NAR Predictor/Sampler的量化敏感性对比
- 蒸馏策略对比：Logit-only vs Hidden-layer matching vs Quantization-aware
- Encoder vs Decoder/Predictor量化敏感性差异

**系统级消融：**
- 有/无VAD对端到端延迟和功耗的影响
- 不同噪声条件（SNR=5/10/20dB）下三种架构的鲁棒性对比
- 手机CPU核心数对不同架构模型RTF的影响
- 声调混淆对错误率的架构间差异分析

---

## 六、必读论文清单

### 核心方法论（必读8篇）

1. **Paraformer** — Gao et al., "Paraformer: Fast and Accurate Parallel Transformer for Non-autoregressive End-to-End Speech Recognition", Interspeech 2022
   - NAR架构的核心论文，理解Predictor+Sampler机制
2. **SenseVoice** — FunAudioLLM, "SenseVoice: Multilingual Voice Understanding Model", 2024
   - 多任务NAR架构，理解其与Paraformer的区别
3. **Fun-ASR Technical Report** — An et al., arXiv 2509.12508
   - FunASR最新全景，包含Fun-ASR-Nano (0.8B)和Fun-ASR (7.7B)
4. **DQ-Whisper** — Shao et al., "Whisper-KDQ: Joint Distillation and Quantization for Efficient ASR", Interspeech 2024
   - Whisper压缩baseline，联合蒸馏+量化框架
5. **Distil-Whisper** — Gandhi et al., "Distil-Whisper: Robust KD via Large-Scale Pseudo Labelling", 2023
   - Whisper蒸馏的标准方法
6. **LieQ** — Xiao et al., "Layer-wise Information Effectiveness for PTQ in SLMs", arXiv 2508.03332
   - 混合精度量化的层敏感性方法
7. **SLMQuant** — Wang et al., "Benchmarking SLM Quantization for Practical Deployment", ACM 2025
   - SLM量化的系统性发现
8. **LoRA-INT8 Whisper** — Zhang et al., Sensors 2025
   - 粤语LoRA+量化，直接对比对象

### 背景知识（推荐阅读6篇）

9. **Whisper** — Radford et al., "Robust Speech Recognition via Large-Scale Weak Supervision", ICML 2023
10. **AWQ** — Lin et al., "AWQ: Activation-aware Weight Quantization", MLSys 2024
11. **LoRA** — Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models", ICLR 2022
12. **WhisperKit** — Argmax, "On-device Real-time ASR with Billion-Scale Transformers", arXiv 2507.10860
13. **Edge ASR Survey** — "Speech Recognition in Edge Environments", Springer 2026
14. **FireRedASR** — 小红书开源ASR模型，了解竞品格局

---

## 七、执行时间线（共18周）

### Phase 0: 准备期（第1-3周）
- [ ] 精读8篇核心论文，重点理解Paraformer架构和FunASR工具链
- [ ] 配置实验环境：GPU服务器 + FunASR + HuggingFace + PEFT
- [ ] 下载数据集：AISHELL-1（必须）+ WenetSpeech子集
- [ ] 下载预训练模型：Whisper-Small/Tiny, Paraformer-large, SenseVoice-Small
- [ ] 在Android手机上分别跑通三个模型的ONNX推理，建立FP16 baseline

### Phase 1: LoRA微调 + Tone-Aware Loss（第4-7周）
- [ ] Whisper-Small/Tiny中文LoRA微调
- [ ] Paraformer-large中文LoRA微调（研究FunASR的微调接口）
- [ ] SenseVoice-Small中文LoRA微调
- [ ] 设计并实现Tone-Aware Loss + 构建声调混淆词表
- [ ] 在三个模型上分别验证Tone-Aware Loss的效果
- [ ] 完成表2中W1, P1, S1实验

### Phase 2: 知识蒸馏（第8-10周）
- [ ] Whisper蒸馏：复现DQ-Whisper的KD pipeline
- [ ] Paraformer蒸馏：设计NAR蒸馏策略（Predictor对齐+并行Decoder蒸馏）
- [ ] SenseVoice蒸馏：ASR-head选择性蒸馏
- [ ] 完成表2中W2, P2, S2实验

### Phase 3: 量化 + 手机端部署（第11-14周）
- [ ] 实现混合精度量化（AWQ/GPTQ适配三种架构）
- [ ] 三种架构的层级量化敏感性分析
- [ ] 完成表2中W3, P3, S3实验（核心结果）
- [ ] 完成表3中极致压缩实验W4, P4, S4
- [ ] ONNX导出 + Android手机全面评测（CER/RTF/内存/功耗）
- [ ] 绘制三条Pareto曲线（CER vs Model Size）

### Phase 4: VAD + 系统集成（第15-16周）
- [ ] 训练TinyVAD模型
- [ ] JL7012开发板上部署（或模拟环境验证资源占用）
- [ ] BLE音频传输 + 手机端推理端到端Demo
- [ ] 系统级评测（端到端延迟/功耗/传输节省）

### Phase 5: 写作 + 投稿（第17-18周）
- [ ] 整理实验数据，绘制核心图表
- [ ] 撰写论文初稿（英文）
- [ ] CTO/导师审阅 + 修改
- [ ] arXiv预印本发布
- [ ] 投稿目标会议

---

## 八、投稿策略

### 第一选择：arXiv + 语音会议
- 先挂arXiv建立priority
- **Interspeech 2027**（语音主会，Benchmark类工作受欢迎）
- **ICASSP 2027**（信号处理+语音，影响力大）

### 第二选择：应用/系统型会议（强烈推荐）
- **AAAI Applied AI Track** — 跨架构对比+真实产品故事
- **ACM MobiSys / MobiCom** — 移动端部署系统贡献
- **ACM SenSys** — IoT+端云协同系统

### 第三选择：期刊
- **IEEE/ACM Transactions on Audio, Speech and Language Processing** — 语音领域顶刊
- **IEEE Internet of Things Journal** — IoT+AI交叉
- **Computer Speech & Language** (Elsevier)

---

## 九、算力与资源估算

| 资源 | 需求 | 费用估算 | 备注 |
|------|------|---------|------|
| GPU训练 | 1×A100 (40GB) | 约800-1500元 | 三个模型微调+蒸馏+量化，约300 GPU-hours |
| 存储 | ~1TB | - | 三个模型 + 数据集 + checkpoints |
| Android手机 | 中端+高端各1台 | 已有或借用 | 骁龙680级 + 骁龙8 Gen2级 |
| JL7012开发板 | 1块 | 公司有 | 用于VAD部署 |
| 树莓派5（可选） | 1块 | ~350元 | 通用学术benchmark |
| 开源工具 | FunASR, HuggingFace, PEFT, ONNX Runtime | 免费 | - |

**总预算**：约1000-2000元（主要是GPU租赁费用）

---

## 十、风险与备选方案

| 风险 | 概率 | 应对策略 |
|------|------|---------|
| Paraformer的LoRA微调接口不成熟 | 中 | 用FunASR原生微调脚本替代LoRA；或用全量微调小数据 |
| NAR模型蒸馏效果差 | 中 | 论文聚焦"量化对比"而非蒸馏，减少蒸馏步骤的权重 |
| Paraformer量化后CER退化严重 | 低 | 这本身就是有价值的发现——"NAR模型对量化更敏感" |
| Paraformer压缩后反而不如Whisper | 低 | 同上，负面结果也是有价值的Benchmark贡献 |
| 手机端ONNX导出三个模型工程量大 | 中 | 优先做Paraformer+Whisper，SenseVoice作为可选项 |
| 时间不够18周 | 中 | 砍掉SenseVoice只做Whisper vs Paraformer双架构对比 |
| 投稿被拒 | 中 | arXiv先发，根据反馈改投 |

---

## 十一、论文结构预览

```
1. Introduction
   - 中文ASR模型的架构多样化（AR/NAR/LLM-based）
   - 现有压缩工作仅聚焦Whisper的盲区
   - 核心问题：哪个架构最适合压缩后的手机端部署？

2. Related Work
   2.1 中文ASR模型（Whisper, Paraformer, SenseVoice, Qwen2-Audio）
   2.2 模型压缩技术（蒸馏, 量化, 剪枝）
   2.3 端侧ASR部署

3. Cross-Architecture Compression Pipeline
   3.1 统一压缩框架设计
   3.2 LoRA微调 + Tone-Aware Loss
   3.3 架构内知识蒸馏策略
   3.4 混合精度量化 + CER-based敏感性分析

4. System Design: Edge-Phone Collaborative ASR
   4.1 硬件约束分析（JL7012 vs 手机）
   4.2 TinyVAD端侧模块
   4.3 端到端Pipeline

5. Experiments
   5.1 实验设置（数据集/模型/硬件）
   5.2 FP16基线对比
   5.3 压缩后跨架构Pareto曲线（核心结果）
   5.4 量化敏感性分析：AR vs NAR
   5.5 手机端部署评测（RTF/内存/功耗）
   5.6 端到端系统评测
   5.7 消融实验

6. Analysis & Discussion
   6.1 NAR vs AR的压缩鲁棒性差异
   6.2 Tone-Aware Loss的跨架构通用性
   6.3 "应该压缩哪个模型？"——实用建议
   6.4 局限性

7. Conclusion
   - 核心发现总结
   - 实用建议：中文手机端ASR的最优选择
```

---

## 十二、最后提醒

### 和CTO沟通的话术

1. **产品价值**："这个研究直接回答'我们录音笔配套App应该用哪个ASR模型'的问题。目前我们可能还在用云端API，做完后可以切换到本地离线识别，降低服务器成本+保护用户隐私。"

2. **学术价值**："所有人都在压缩Whisper，但没人研究过Paraformer这种国产最强中文ASR模型的压缩特性。我们做第一个跨架构对比，抢占这个研究空白。"

3. **发表前景**："Benchmark类论文在语音会议很受欢迎（参考SLMQuant被ACM收录）。而且我们有真实产品硬件数据，比纯学术实验更有说服力。"

4. **资源需求**："约300小时A100（~1500元GPU租赁），其他资源公司内部都有。"

### 核心执行原则

- **先跑baseline再写代码**：第一步是在手机上跑通三个模型的FP16推理，看原始CER和速度
- **Paraformer优先**：它最可能是最终答案，优先投入精力
- **负面结果也是结果**：如果发现NAR压缩后反而不如AR，这本身就是重要发现
- **最小可发表版本**：即使只做完Whisper vs Paraformer的量化对比（不做蒸馏和VAD），也已经是一篇有价值的论文
