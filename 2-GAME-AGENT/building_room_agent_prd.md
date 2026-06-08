# PRD：一个 LLM Agent 在小建筑里找房间的文字游戏

## 1. 项目名称

**Building Room Finder Agent**

中文名：**小建筑寻路智能体**

---

## 2. 项目背景

本项目是一个面向初学者的 Game LLM Agent 入门项目。

用户从建筑学背景转向 AI / LLM Agent 方向，希望通过“做中学”的方式，先完成一个简单但完整的文字游戏智能体原型。

游戏场景设定在一栋小型建筑中。玩家或 LLM Agent 需要根据文字描述，在建筑空间中移动、观察、记忆信息、寻找钥匙，并最终进入目标房间完成任务。

---

## 3. 项目目标

### 3.1 学习目标

通过本项目，学习以下基础能力：

- Python 基础项目结构
- 简单文字游戏环境设计
- LLM Agent 的观察、决策、行动闭环
- 状态管理
- 动作约束
- 简单记忆机制
- 简单评估指标

### 3.2 产品目标 

完成一个可运行的文字游戏 Demo：

> LLM Agent 在一栋小建筑中，根据文字观察信息，自主寻找会议室钥匙，进入会议室，并拿到文件。

---

## 4. 目标用户

### 4.1 主要用户

- 刚入门 LLM Agent 的学习者
- 编程基础较弱但希望通过项目学习的人
- 对空间、建筑、游戏 AI 感兴趣的人

### 4.2 用户特点

- 不是计算机科班出身
- 希望边做边学
- 更容易理解空间、房间、路径、任务等概念
- 需要一个足够小、足够清晰的项目起点

---

## 5. MVP 范围

### 5.1 MVP 必须包含

MVP 版本只做一个命令行文字游戏。

核心功能包括：

1. 一个小建筑地图
2. 房间之间的连接关系
3. 房间文字描述
4. 可交互物品
5. 背包系统
6. 动作系统
7. 成功 / 失败判断
8. LLM Agent 自动选择动作
9. 游戏日志记录

### 5.2 MVP 不包含

第一版不做以下内容：

- 图形界面
- 3D 游戏引擎
- Unity
- 强化学习训练
- 多智能体
- 复杂 NPC 对话
- 视觉识别
- 数据库
- 用户登录系统

---

## 6. 游戏设定

### 6.1 场景

游戏发生在一栋小型建筑中。

建筑包含以下房间：

| 房间 ID | 房间名称 | 描述 |
|---|---|---|
| entrance | 入口大厅 | 建筑入口，有指示牌 |
| corridor | 走廊 | 连接多个房间 |
| office | 办公室 | 可能有线索 |
| storage | 储藏间 | 可能有钥匙 |
| meeting_room | 会议室 | 目标房间，需要钥匙进入 |
| stairwell | 楼梯间 | 暂时无核心功能 |

---

## 7. 地图结构

第一版地图为固定结构：

```text
入口大厅 entrance
    |
走廊 corridor
 /    |      \
办公室 office  储藏间 storage  楼梯间 stairwell
              |
          会议室 meeting_room
```

连接关系：

```json
{
  "entrance": ["corridor"],
  "corridor": ["entrance", "office", "storage", "stairwell"],
  "office": ["corridor"],
  "storage": ["corridor", "meeting_room"],
  "meeting_room": ["storage"],
  "stairwell": ["corridor"]
}
```

---

## 8. 核心任务

### 8.1 主线任务

Agent 的目标是：

1. 从入口大厅出发
2. 探索建筑
3. 找到会议室钥匙
4. 进入会议室
5. 拿到文件
6. 完成游戏

### 8.2 胜利条件

当 Agent 拿到会议室里的文件时，游戏胜利。

```text
Victory condition:
inventory contains "file"
```

### 8.3 失败条件

以下情况视为失败：

- 超过最大步数
- Agent 连续多次选择无效动作
- Agent 没有完成目标

第一版建议最大步数为：

```text
max_steps = 30
```

---

## 9. 可交互物品

| 物品 ID | 名称 | 初始位置 | 用途 |
|---|---|---|---|
| meeting_key | 会议室钥匙 | storage | 打开会议室 |
| file | 文件 | meeting_room | 目标物品 |
| sign | 指示牌 | entrance | 提供方向提示 |
| note | 便签 | office | 提供钥匙线索 |

---

## 10. 动作系统

### 10.1 支持动作

第一版只允许以下动作：

```text
look
go <room_name>
take <item_name>
read <item_name>
open <room_name>
inventory
```

### 10.2 示例动作

```text
look
go corridor
go storage
take meeting_key
open meeting_room
go meeting_room
take file
inventory
```

### 10.3 无效动作处理

如果 Agent 输出不支持的动作，系统返回：

```text
Invalid action. You can only use the allowed actions.
```

如果 Agent 去不存在或不可达的房间，系统返回：

```text
You cannot go there from your current location.
```

如果 Agent 没有钥匙却尝试进入会议室，系统返回：

```text
The meeting room is locked. You need a key.
```

---

## 11. 游戏状态

游戏需要维护以下状态：

```json
{
  "current_room": "entrance",
  "inventory": [],
  "visited_rooms": [],
  "room_items": {
    "entrance": ["sign"],
    "office": ["note"],
    "storage": ["meeting_key"],
    "meeting_room": ["file"]
  },
  "locked_rooms": ["meeting_room"],
  "step_count": 0,
  "done": false,
  "success": false
}
```

---

## 12. Agent 设计

### 12.1 第一版 Agent

第一版 Agent 使用 LLM 作为决策器。

基本循环：

```text
观察当前环境
↓
把观察结果发送给 LLM
↓
LLM 选择下一步动作
↓
游戏环境执行动作
↓
返回新的观察
↓
直到成功或失败
```

### 12.2 Agent 输入

每一步给 Agent 的信息包括：

```text
当前房间
房间描述
可见物品
已访问房间
背包物品
可选动作列表
当前目标
最近几步历史
```

### 12.3 Agent 输出

Agent 每次只输出一个动作。

正确格式：

```text
go corridor
```

错误格式：

```text
I think I should go to the corridor because...
```

第一版要求 Agent 不输出解释，只输出动作。

---

## 13. Prompt 设计

### 13.1 System Prompt

```text
You are an agent playing a text-based building navigation game.
Your goal is to find the meeting room, enter it, and take the file.
You must choose exactly one action from the allowed actions.
Do not explain your reasoning.
Only output the action.
```

### 13.2 User Prompt 模板

```text
Current room: {current_room}

Room description:
{room_description}

Visible items:
{visible_items}

Inventory:
{inventory}

Visited rooms:
{visited_rooms}

Recent actions:
{recent_actions}

Allowed actions:
{allowed_actions}

Goal:
Find the meeting room, enter it, and take the file.

Choose your next action.
```

---

## 14. 游戏流程示例

```text
Step 1
Observation: You are in the entrance hall. There is a sign here.
Action: read sign

Step 2
Observation: The sign says: Meeting room is past the storage room.
Action: go corridor

Step 3
Observation: You are in the corridor. You can go to office, storage, stairwell, or entrance.
Action: go storage

Step 4
Observation: You are in the storage room. There is a meeting key here.
Action: take meeting_key

Step 5
Observation: You picked up the meeting key.
Action: open meeting_room

Step 6
Observation: The meeting room is now unlocked.
Action: go meeting_room

Step 7
Observation: You are in the meeting room. There is a file here.
Action: take file

Game result: success
```

---

## 15. 评估指标

MVP 阶段记录以下指标：

| 指标 | 说明 |
|---|---|
| success | 是否成功完成任务 |
| step_count | 完成任务使用的步数 |
| invalid_action_count | 无效动作次数 |
| repeated_action_count | 重复无意义动作次数 |
| total_tokens | LLM 总 token 消耗 |
| total_cost | LLM 调用成本 |
| trajectory | 完整行动轨迹 |

---

## 16. 日志格式

每一步记录一条日志：

```json
{
  "episode_id": 1,
  "step": 3,
  "current_room": "corridor",
  "observation": "You are in the corridor.",
  "allowed_actions": ["go entrance", "go office", "go storage", "go stairwell", "look", "inventory"],
  "agent_action": "go storage",
  "is_valid_action": true,
  "reward": 0,
  "done": false
}
```

---

## 17. 奖励设计

第一版可以使用简单奖励：

| 行为 | 奖励 |
|---|---:|
| 拿到钥匙 | +1 |
| 打开会议室 | +1 |
| 拿到文件 | +5 |
| 无效动作 | -1 |
| 每走一步 | -0.1 |
| 成功完成任务 | +10 |

---

## 18. 版本规划

### v0.1：手动文字游戏

目标：玩家可以在命令行里手动输入动作完成游戏。

功能：

- 固定地图
- 房间描述
- 物品拾取
- 背包
- 上锁房间
- 胜利判断

### v0.2：接入 LLM Agent

目标：LLM 可以自动玩游戏。

功能：

- Prompt 模板
- LLM 动作输出
- 动作校验
- 游戏日志

### v0.3：加入简单记忆

目标：Agent 能减少重复探索。

功能：

- visited_rooms
- recent_actions
- inventory memory
- simple state summary

### v0.4：加入评估脚本

目标：可以连续运行多次并统计成功率。

功能：

- run 10 episodes
- 统计 success rate
- 统计平均步数
- 统计无效动作率

---

## 19. 成功标准

MVP 项目完成时，需要满足：

1. 可以通过命令行运行游戏
2. 人类玩家可以手动完成任务
3. LLM Agent 可以自动完成任务
4. 至少运行 10 次测试
5. 输出成功率、平均步数、无效动作次数
6. 保存完整日志
7. 项目有 README

---

## 20. 推荐项目目录结构

```text
building-room-agent/
├── README.md
├── main.py
├── env.py
├── agent.py
├── prompts.py
├── evaluator.py
├── logs/
│   └── episode_001.json
└── requirements.txt
```

---

## 21. 技术栈

第一版建议使用：

```text
Python
OpenAI API 或其他 LLM API
JSON
命令行界面
```

暂时不使用：

```text
Unity
PyTorch
强化学习
数据库
前端框架
```

---

## 22. 风险与解决方案

| 风险 | 说明 | 解决方案 |
|---|---|---|
| Agent 输出乱七八糟 | LLM 可能输出解释而不是动作 | 限制输出格式，只允许动作 |
| Agent 重复原地打转 | LLM 可能重复 look 或 inventory | 加 recent_actions |
| 动作不可执行 | LLM 可能编造动作 | 使用 allowed_actions |
| 项目变复杂 | 初学者容易过早扩展 | 第一版只做固定地图 |
| 不知道是否进步 | 没有评估指标 | 记录 success rate 和 invalid action rate |

---

## 23. 后续扩展方向

MVP 完成后，可以扩展：

1. 增加更多房间
2. 增加 NPC
3. 增加多任务
4. 加入地图记忆
5. 加入失败反思
6. 加入自动生成建筑平面
7. 加入建筑空间语义，例如大厅、走廊、核心筒、公共区、私密区
8. 做成 Web 可视化版本

---

## 24. 第一阶段开发任务

### Day 1

- 创建项目目录
- 写固定地图
- 写房间描述
- 实现 `look`

### Day 2

- 实现 `go`
- 实现房间连接
- 实现不可达提示

### Day 3

- 实现物品系统
- 实现 `take`
- 实现 `inventory`

### Day 4

- 实现会议室上锁逻辑
- 实现 `open meeting_room`

### Day 5

- 实现胜利条件
- 完成人类可玩版本

### Day 6

- 接入 LLM API
- 实现 Agent 自动选择动作

### Day 7

- 保存日志
- 运行 10 次测试
- 写 README

---

## 25. 一句话总结

本项目的目标不是做一个复杂游戏，而是用一个足够小的建筑文字游戏，跑通 Game LLM Agent 最核心的闭环：

```text
观察环境 → 生成动作 → 执行动作 → 更新状态 → 评估结果
```
