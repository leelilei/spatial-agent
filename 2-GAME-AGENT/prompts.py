SYSTEM_PROMPT = """You are an agent playing a text-based building navigation game.
Your goal is to find the meeting room, enter it, and take the file.
You must choose exactly one action from the allowed actions.
Do not explain your reasoning.
Only output the action."""


USER_PROMPT_TEMPLATE = """Current room: {current_room}

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

Choose your next action."""


def format_user_prompt(state: dict, allowed_actions: list[str], recent_actions: list[str]) -> str:
    return USER_PROMPT_TEMPLATE.format(
        current_room=state["current_room"],
        room_description=state["room_description"],
        visible_items=", ".join(state["visible_items"]) if state["visible_items"] else "none",
        inventory=", ".join(state["inventory"]) if state["inventory"] else "empty",
        visited_rooms=", ".join(state["visited_rooms"]) if state["visited_rooms"] else "none",
        recent_actions=", ".join(recent_actions[-5:]) if recent_actions else "none",
        allowed_actions="\n".join(f"- {action}" for action in allowed_actions),
    )
