# 个人学习工作台（Phase 1 MVP）

按 [`../个人学习工作台-PRD.md`](../个人学习工作台-PRD.md) 实现。本地、单人、零依赖。

## 怎么启动

**方式一（最简单）**：双击 `启动.command`，浏览器会自动打开。

**方式二（命令行）**：
```bash
cd workbench
python3 server.py
```
然后浏览器访问 http://localhost:8770 （脚本会自动打开）。

> 只需要电脑里有 `python3`，**不用 pip 安装任何东西**。
> 浏览器内运行 Python 用的是 Pyodide（首次打开会联网加载一次，之后有缓存）。

## 能做什么（MVP）
- **总览**：看五阶段进度、当前该学哪一课。
- **课程**：26 节 6.100L 课程，打开本地讲义/代码，标「👁️看过」，做「检查点」。
- **作业**：在网页里写 Python、运行测试、提交。
- **被点评 / 确认学完**：见下。

## 和 AI 助教怎么配合（文件桥接，工具中立）
工作台只把你的学习「存到硬盘」，真正点评你的是 AI 编码 agent（Claude Code / Codex 等）。
协议见 [`TUTOR.md`](TUTOR.md)（`CLAUDE.md` / `AGENTS.md` 都指向它）。

- **做完作业** → 提交后，到 AI 终端说「**点评 auto-001**」。
- **学完一课** → 做完检查点提交后，到 AI 终端说「**确认我学完 lec01**」。
  AI 通过后会把这一课标记为 ✅「学会」并写下点评。
- **想要新题** → 到 AI 终端说「**给我出一道 lec02 的题**」。

数据都在 `data/` 下：`progress.json` / `submissions/` / `reviews/` / `assignments/` / `checkpoints/`。
纯文本，可被 Obsidian 打开、可 git 备份。
