from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from typing import Any


ROOM_GRAPH: dict[str, list[str]] = {
    "entrance": ["corridor"],
    "corridor": ["entrance", "office", "storage", "stairwell"],
    "office": ["corridor"],
    "storage": ["corridor", "meeting_room"],
    "meeting_room": ["storage"],
    "stairwell": ["corridor"],
}

ROOM_NAMES: dict[str, str] = {
    "entrance": "Entrance Hall",
    "corridor": "Corridor",
    "office": "Office",
    "storage": "Storage Room",
    "meeting_room": "Meeting Room",
    "stairwell": "Stairwell",
}

ROOM_DESCRIPTIONS: dict[str, str] = {
    "entrance": "You are in the entrance hall. A sign is mounted near the doorway.",
    "corridor": "You are in a narrow corridor connecting several rooms.",
    "office": "You are in a small office with a desk and a note.",
    "storage": "You are in the storage room. Shelves line the walls.",
    "meeting_room": "You are in the meeting room. A file lies on the table.",
    "stairwell": "You are in the stairwell. It is quiet here.",
}

ITEM_DESCRIPTIONS: dict[str, str] = {
    "sign": "The sign says: Meeting room is past the storage room.",
    "note": "The note says: The meeting room key is stored in the storage room.",
}

TAKEABLE_ITEMS = {"meeting_key", "file"}
READABLE_ITEMS = {"sign", "note"}


@dataclass
class StepResult:
    observation: str
    reward: float
    done: bool
    success: bool
    is_valid_action: bool


@dataclass
class BuildingRoomEnv:
    max_steps: int = 30
    max_invalid_actions: int = 5
    current_room: str = "entrance"
    inventory: list[str] = field(default_factory=list)
    visited_rooms: list[str] = field(default_factory=lambda: ["entrance"])
    room_items: dict[str, list[str]] = field(
        default_factory=lambda: {
            "entrance": ["sign"],
            "office": ["note"],
            "storage": ["meeting_key"],
            "meeting_room": ["file"],
        }
    )
    locked_rooms: set[str] = field(default_factory=lambda: {"meeting_room"})
    step_count: int = 0
    invalid_action_count: int = 0
    repeated_action_count: int = 0
    done: bool = False
    success: bool = False
    last_action: str | None = None

    def reset(self) -> str:
        self.current_room = "entrance"
        self.inventory = []
        self.visited_rooms = ["entrance"]
        self.room_items = {
            "entrance": ["sign"],
            "office": ["note"],
            "storage": ["meeting_key"],
            "meeting_room": ["file"],
        }
        self.locked_rooms = {"meeting_room"}
        self.step_count = 0
        self.invalid_action_count = 0
        self.repeated_action_count = 0
        self.done = False
        self.success = False
        self.last_action = None
        return self.observe()

    def observe(self) -> str:
        room_items = self.room_items.get(self.current_room, [])
        exits = ROOM_GRAPH[self.current_room]
        item_text = ", ".join(room_items) if room_items else "nothing"
        exit_text = ", ".join(exits)
        return (
            f"{ROOM_DESCRIPTIONS[self.current_room]}\n"
            f"Visible items: {item_text}.\n"
            f"Exits: {exit_text}."
        )

    def get_state(self) -> dict[str, Any]:
        return {
            "current_room": self.current_room,
            "room_name": ROOM_NAMES[self.current_room],
            "room_description": ROOM_DESCRIPTIONS[self.current_room],
            "visible_items": list(self.room_items.get(self.current_room, [])),
            "inventory": list(self.inventory),
            "visited_rooms": list(self.visited_rooms),
            "room_items": deepcopy(self.room_items),
            "locked_rooms": sorted(self.locked_rooms),
            "step_count": self.step_count,
            "invalid_action_count": self.invalid_action_count,
            "repeated_action_count": self.repeated_action_count,
            "done": self.done,
            "success": self.success,
        }

    def allowed_actions(self) -> list[str]:
        actions = ["look", "inventory"]
        actions.extend(f"go {room}" for room in ROOM_GRAPH[self.current_room])

        for item in self.room_items.get(self.current_room, []):
            if item in TAKEABLE_ITEMS:
                actions.append(f"take {item}")
            if item in READABLE_ITEMS:
                actions.append(f"read {item}")

        if (
            self.current_room == "storage"
            and "meeting_room" in self.locked_rooms
            and "meeting_key" in self.inventory
        ):
            actions.append("open meeting_room")

        return actions

    def step(self, action: str) -> StepResult:
        if self.done:
            return StepResult(
                observation="The game is already over.",
                reward=0.0,
                done=True,
                success=self.success,
                is_valid_action=False,
            )

        action = action.strip()
        self.step_count += 1
        if action == self.last_action and action in {"look", "inventory"}:
            self.repeated_action_count += 1
        self.last_action = action

        result = self._execute_action(action)
        if not result.is_valid_action:
            self.invalid_action_count += 1

        if "file" in self.inventory:
            self.success = True
            self.done = True
            result.done = True
            result.success = True
            result.reward += 10.0
            result.observation = f"{result.observation}\nGame result: success."

        if not self.done and self.step_count >= self.max_steps:
            self.done = True
            result.done = True
            result.observation = f"{result.observation}\nGame result: failed. Max steps reached."

        if not self.done and self.invalid_action_count >= self.max_invalid_actions:
            self.done = True
            result.done = True
            result.observation = (
                f"{result.observation}\nGame result: failed. Too many invalid actions."
            )

        result.done = self.done
        result.success = self.success
        return result

    def _execute_action(self, action: str) -> StepResult:
        if not action:
            return self._invalid("Invalid action. You can only use the allowed actions.")

        verb, _, target = action.partition(" ")
        target = target.strip()

        if verb == "look" and not target:
            return StepResult(self.observe(), -0.1, self.done, self.success, True)

        if verb == "inventory" and not target:
            items = ", ".join(self.inventory) if self.inventory else "empty"
            return StepResult(
                f"Inventory: {items}.", -0.1, self.done, self.success, True
            )

        if verb == "go":
            return self._go(target)

        if verb == "take":
            return self._take(target)

        if verb == "read":
            return self._read(target)

        if verb == "open":
            return self._open(target)

        return self._invalid("Invalid action. You can only use the allowed actions.")

    def _go(self, room: str) -> StepResult:
        if room not in ROOM_GRAPH:
            return self._invalid("You cannot go there from your current location.")
        if room not in ROOM_GRAPH[self.current_room]:
            return self._invalid("You cannot go there from your current location.")
        if room == "meeting_room" and room in self.locked_rooms:
            return self._invalid("The meeting room is locked. You need a key.")

        self.current_room = room
        if room not in self.visited_rooms:
            self.visited_rooms.append(room)
        return StepResult(self.observe(), -0.1, self.done, self.success, True)

    def _take(self, item: str) -> StepResult:
        current_items = self.room_items.get(self.current_room, [])
        if item not in current_items or item not in TAKEABLE_ITEMS:
            return self._invalid("You cannot take that item here.")

        current_items.remove(item)
        self.inventory.append(item)
        reward = 1.0 if item == "meeting_key" else 5.0
        return StepResult(
            f"You picked up the {item}.", reward, self.done, self.success, True
        )

    def _read(self, item: str) -> StepResult:
        current_items = self.room_items.get(self.current_room, [])
        if item not in current_items or item not in READABLE_ITEMS:
            return self._invalid("You cannot read that item here.")
        return StepResult(
            ITEM_DESCRIPTIONS[item], -0.1, self.done, self.success, True
        )

    def _open(self, room: str) -> StepResult:
        if room != "meeting_room":
            return self._invalid("You cannot open that.")
        if self.current_room != "storage":
            return self._invalid("You must be in the storage room to open meeting_room.")
        if "meeting_key" not in self.inventory:
            return self._invalid("The meeting room is locked. You need a key.")
        if room not in self.locked_rooms:
            return StepResult(
                "The meeting room is already unlocked.",
                -0.1,
                self.done,
                self.success,
                True,
            )

        self.locked_rooms.remove(room)
        return StepResult(
            "The meeting room is now unlocked.", 1.0, self.done, self.success, True
        )

    def _invalid(self, observation: str) -> StepResult:
        return StepResult(observation, -1.0, self.done, self.success, False)
