"""Prompt 模板管理模块。"""

from __future__ import annotations

import json
from typing import Any


def build_preflight_messages(task: dict[str, Any]) -> list[dict[str, str]]:
    family = task["task_family"]
    payload = task["prompt_payload"]
    metadata = task.get("metadata", {})

    if family in {"comprehension", "behavioral_inference", "reverse_inference_audit", "prompt_position"}:
        body_lines = [payload["instruction"]]
        if family == "reverse_inference_audit":
            body_lines.append(metadata["description_stub"])
        prompt_position = metadata.get("prompt_position")
        if prompt_position == "system_prefix":
            system_prompt = "你是严谨的空间推理评估器。先关注空间描述，再回答问题。"
            user_prompt = "\n".join(
                [
                    *body_lines,
                    f"问题：{payload['question']}",
                    f"选项：{json.dumps(payload['options'], ensure_ascii=False)}",
                    '输出格式：{"answer": "<选项>"}',
                ]
            )
        elif prompt_position == "memory_suffix":
            system_prompt = "你是严谨的空间推理评估器。"
            user_prompt = "\n".join(
                [
                    f"问题：{payload['question']}",
                    f"选项：{json.dumps(payload['options'], ensure_ascii=False)}",
                    "补充记忆：先使用上面的空间线索，再作答。",
                    *body_lines,
                    '输出格式：{"answer": "<选项>"}',
                ]
            )
        elif prompt_position == "action_context":
            system_prompt = "你是严谨的空间推理评估器。"
            user_prompt = "\n".join(
                [
                    f"你即将做一个空间决策判断。{payload['question']}",
                    *body_lines,
                    f"候选项：{json.dumps(payload['options'], ensure_ascii=False)}",
                    '输出格式：{"answer": "<选项>"}',
                ]
            )
        else:
            system_prompt = "你是严谨的空间推理评估器。"
            user_prompt = "\n".join(
                [
                    *body_lines,
                    f"问题：{payload['question']}",
                    f"选项：{json.dumps(payload['options'], ensure_ascii=False)}",
                    '输出格式：{"answer": "<选项>"}',
                ]
            )
        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

    if family == "lexical_norming":
        return [
            {"role": "system", "content": "你是一个做词汇规范化评分的研究助理。"},
            {
                "role": "user",
                "content": "\n".join(
                    [
                        payload["instruction"],
                        f"标签：{payload['label']}",
                        f"维度：{json.dumps(payload['dimensions'], ensure_ascii=False)}",
                        '输出格式：{"publicness": 1-7, "privacy": 1-7, "danger": 1-7, "valence": 1-7, "brightness": 1-7}',
                    ]
                ),
            },
        ]

    if family == "coding_pilot_llm":
        return [
            {"role": "system", "content": "你是一个按照 coding manual 做盲编码的研究助理。"},
            {
                "role": "user",
                "content": "\n".join(
                    [
                        payload["instruction"],
                        f"行为文本：{payload['behavior_text']}",
                        f"标签空间：{json.dumps(payload['labels'], ensure_ascii=False)}",
                        '输出格式：{"behavior_type": "...", "interaction_intensity": "...", "information_sensitivity": "...", "gatekeeping": "..."}',
                    ]
                ),
            },
        ]

    raise ValueError(f"Unsupported task family: {family}")
