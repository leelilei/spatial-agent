# Building Room Finder Agent

小建筑寻路智能体是一个命令行文字游戏 Demo。玩家或 Agent 从入口大厅出发，探索小建筑，找到会议室钥匙，打开会议室，并拿到文件。

## Files

- `env.py`: game state, room graph, actions, rewards, success/failure rules
- `agent.py`: OpenAI Agent, rule-based fallback Agent, action normalization
- `prompts.py`: LLM prompt templates
- `main.py`: manual game and single-agent episode runner
- `evaluator.py`: multi-episode evaluation script
- `logs/`: generated episode logs

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

OpenAI mode needs an API key:

```bash
export OPENAI_API_KEY="your-api-key"
```

If no key is set, `--agent auto` falls back to the rule-based Agent so the demo still runs locally.

## Run

Manual play:

```bash
python3 main.py --mode manual
```

Rule Agent:

```bash
python3 main.py --mode agent --agent rule
```

OpenAI first, rule fallback:

```bash
python3 main.py --mode agent --agent auto
```

Evaluate 10 episodes:

```bash
python3 evaluator.py --episodes 10 --agent rule
```

## Example Winning Path

```text
read sign
go corridor
go storage
take meeting_key
open meeting_room
go meeting_room
take file
```
