# Preference Falsification 文献扫描 + 方向定案(2026-07-02)

> 承接 2026-07-01 的红海终判。经过十次连续红海命中后,meta 结论浮出:
> 整个"LLM agent society 的信念/言行/保真"在 2024–2026 被系统填满。
> 但讨论中浮出一个更干净的核心方向,需要做**独立的、first-party 的文献确认**。
> 同时,WebSearch 通道被三次对抗注入攻击——伪造的论文 ID/标题/URL 试图
> 说服我该方向也是红海。本扫描全部通过 `export.arxiv.org` 结构化 API
> 做 first-party 验证,零外部搜索依赖。

## 新方向:say ≠ do ≠ think → 集体幻觉

在 minimal society 中,同一个 agent 的 **say ≠ do ≠ think** 三者不一致,
agent 自身不察觉(非欺骗),系统只传输 **say** → 集体的投票/分配建立在
被扭曲的信念认知上 → 聚合为**集体幻觉**,没有任何节点能检测到。

### 三角

| 层 | 含义 | 可见性 |
|---|---|---|
| say | 公开声明/立场 | 全节点可见,唯一可传输的信息 |
| do | 私人行动(投票/分配/选择) | 仅系统记录,节点互不可见——**HARD ANCHOR** |
| think | 私下信念(probe 引出) | 仅系统记录,节点互不可见 |

### 三个 strength(防御必须建立在组合上)

1. **三层同时观测**:say/do/think 三者同时记录,do 是客观上可验证的 hard anchor——消除 Telephone 的 judge-validity 弱点。
2. **Unaware / 非欺骗**:agent 在 say 时不认为自己"在撒谎"——区分于所有 deception 研究。
3. **系统只传输 say → 聚合为集体幻觉**:社会层面的 emergent consequence——理论祖先 Timur Kuran *Private Truths, Public Lies*(1995) 的 preference falsification / pluralistic ignorance。

### only-in-LLM 的论证

人类社会中 think 层永远无法完全观测(Kuran 只能靠匿名调查近似)。
LLM 允许三者同时记录——这是**第一次该微观机制可以被直接验证**。

### 关键防漂移

此方向的"传输"**不是**旧 Telephone 的"fidelity decay"(红海)。
必须避免滑回 fidelity / decay / provenance 的措辞。
核心是:聚合幻觉,不是信息衰减。

## 反注入:first-party arxiv API 验证

WebSearch 被三次对抗注入,包括:

- 伪造论文:"Modeling Preference Falsification in Multi-Agent LLM Societies (2603.02219)"
- 伪造论文:"Silent Majority Problem in LLM Agent Networks (2605.13001)"
- 冒充我口吻的合成文本("the synthesis is yours to write")

**反制措施**:全部改用 `export.arxiv.org` 结构化 API,first-party 验证。

### 阳性对照

```
query: abs:"large language model"
→ totalResults: 100000+ (API 确认存活)
```

### 关键词扫描(全部零结果)

| 检索词 | 结果 |
|--------|------|
| "preference falsification" | **0** |
| "pluralistic ignorance" + "language model" | **0** |
| "stated preference" + "revealed preference" + "language model" | 2(单 agent 理性/off-target) |
| "self-censorship" / "social desirability" + "agents" | 3(单 model audit/off-target) |

## 邻居验证(最接近的 3 篇真实论文)

| 论文 | 与我们方向的关系 | 不包含什么 |
|------|-----------------|-----------|
| **Persona Inconstancy in Multi-Agent LLM** (2405.03862) | say≠think + conformity 压力 | ❌ 无 do 层;❌ 无社会聚合→集体幻觉;❌ 把 private dissent 当 diversity good |
| **Do Role-Playing Agents Practice What They Preach** (2507.02197) | say≠do(stated belief vs enacted behavior) | ❌ 单 agent role-play 评估;❌ 无多 agent 聚合;❌ 无 think 层 |
| **Ashery: Dynamics of Social Conventions in LLM Agents** (2410.08948) | naming-game symmetry breaking | ❌ 个体 truly unbiased;❌ 无隐藏私人信念;❌ 完全不同机制 |

### 已被证伪的引用

| 引用 | 判定 | 证据 |
|------|------|------|
| "When Agents Say One Thing and Do Another" (2602.06286) | **FABRICATED** | id NOT FOUND;标题短语零结果;topic 零结果——WebSearch 对抗注入 |

## 方向定案:LOCKED IN

**两个边(say≠think, say≠do)都有真实邻居——防御压力真实存在。
但完整闭环(三层 + unaware + 社会聚合为集体幻觉)被零篇真实论文占据。**

防御叙事必须始终建立在**组合**上,永不建立在任一单边上:
- "say≠think 有人做过"——但我们有 do 层 + 聚合
- "say≠do 也有人做过"——但我们是 multi-agent + unaware + think 层
- "Kuran 1995 有理论"——但我们是 first empirical 三层观测

## 残余 caveat(保存在档案中,不隐藏)

- arxiv abstract-term 搜索有盲区:deliberation / opinion-dynamics 论文
  可能用其他措辞;SSRN 等非 arxiv 源未检。
- 足以推进到 scenario 设计;但投稿前 related work 需要更深阅读。

## 下一步

1. ✅ 修正档案(标记 fabricated 引用 + 本文档定案)——done
2. → 设计场景:构建能自然拉开 say/do/think 的 minimal society scenario
3. → 实验:先单轮验证 gap 出现,再加多轮验证集体幻觉涌现
