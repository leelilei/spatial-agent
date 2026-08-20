#!/usr/bin/env python3
"""Sync actionable Markdown todo items to macOS Reminders.

Default behavior is intentionally conservative:
- reads docs/guides/todolist.md
- syncs unchecked tasks under the current execution-priority section only
- creates or updates reminders in a single Reminders list
- stores reminder ids in .cache/ so Reminders notes stay readable
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TODO = REPO_ROOT / "docs" / "guides" / "todolist.md"
DEFAULT_LIST_NAME = "SpatialAgent Survey"
DEFAULT_STATE_PATH = REPO_ROOT / ".cache" / "todo_reminders_sync_state.json"
SOURCE_MARKER_PREFIX = "SpatialAgentTodoID:"
SECTION_DESCRIPTIONS: dict[str, str] = {}
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TASK_RE = re.compile(r"^(\s*)-\s+\[([ xX])\]\s+(.+?)\s*$")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
INLINE_CODE_RE = re.compile(r"`([^`]+)`")


@dataclass(frozen=True)
class TodoItem:
    line_no: int
    title: str
    detail: str
    raw_title: str
    heading_path: tuple[str, ...]
    priority_label: str
    priority_value: int
    source_id: str


@dataclass(frozen=True)
class DueDate:
    label: str
    value: date

    @property
    def applescript_text(self) -> str:
        return f"{self.value.isoformat()} 18:00:00"


def clean_markdown_text(text: str) -> str:
    text = MARKDOWN_LINK_RE.sub(r"\1", text)
    text = INLINE_CODE_RE.sub(r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def short_section_name(item: TodoItem) -> str:
    for heading in reversed(item.heading_path):
        if heading.lower().startswith("priority"):
            if "：" in heading:
                return heading.split("：", 1)[1].strip()
            if ":" in heading:
                return heading.split(":", 1)[1].strip()
            return heading
    return item.priority_label


def should_flag_item(item: TodoItem) -> bool:
    return item.priority_label == "P0"


def trim_text(text: str, max_len: int) -> str:
    if len(text) <= max_len:
        return text
    if max_len <= 3:
        return text[:max_len]
    return text[: max_len - 3].rstrip() + "..."


def parse_task_parts(raw_title: str) -> tuple[str, str]:
    parts = [clean_markdown_text(part) for part in raw_title.split("|")]
    parts = [part for part in parts if part]

    title = parts[0] if parts else clean_markdown_text(raw_title)
    detail = parts[1] if len(parts) >= 2 else ""
    return title, detail


def build_detail(priority_label: str, detail: str) -> str:
    detail = re.sub(rf"^{re.escape(priority_label)}\s*", "", detail, flags=re.IGNORECASE)
    return detail.strip()


def priority_from_headings(headings: tuple[str, ...]) -> tuple[str, int]:
    joined = " / ".join(headings)
    match = re.search(r"Priority\s*(\d+)", joined, re.IGNORECASE)
    if match:
        priority_num = int(match.group(1))
        if priority_num == 0:
            return "P0", 1
        if priority_num == 1:
            return "P1", 5
        return f"P{priority_num}", 9

    for heading in reversed(headings):
        phase_match = re.search(r"Phase\s*(\d+)", heading, re.IGNORECASE)
        if phase_match:
            return f"Phase {phase_match.group(1)}", 9

    return "Todo", 9


def should_include_task(headings: tuple[str, ...], scope: str) -> bool:
    joined = " / ".join(headings)
    if "暂不做" in joined:
        return False

    in_execution_priorities = (
        "执行优先级" in headings
        or "接下来一周的主线任务" in headings
        or any(heading.lower().startswith("priority ") for heading in headings)
    )

    if scope == "all":
        return True

    if scope == "active":
        return in_execution_priorities

    if scope == "priority-and-human":
        return in_execution_priorities or "需要人工优先提供的材料" in headings

    raise ValueError(f"Unsupported scope: {scope}")


def make_source_id(todo_path: Path, headings: tuple[str, ...], raw_title: str) -> str:
    relative_path = todo_path.relative_to(REPO_ROOT)
    stable_key = f"{relative_path}\n{' / '.join(headings)}\n{clean_markdown_text(raw_title)}"
    digest = hashlib.sha1(stable_key.encode("utf-8")).hexdigest()[:16]
    return f"spatialagent:{digest}"


def parse_todos(todo_path: Path, scope: str) -> list[TodoItem]:
    headings_by_level: dict[int, str] = {}
    items: list[TodoItem] = []

    for line_no, line in enumerate(todo_path.read_text(encoding="utf-8").splitlines(), start=1):
        heading_match = HEADING_RE.match(line)
        if heading_match:
            level = len(heading_match.group(1))
            headings_by_level[level] = clean_markdown_text(heading_match.group(2))
            for stale_level in list(headings_by_level):
                if stale_level > level:
                    del headings_by_level[stale_level]
            continue

        task_match = TASK_RE.match(line)
        if not task_match:
            continue

        checked = task_match.group(2).lower() == "x"
        if checked:
            continue

        headings = tuple(headings_by_level[level] for level in sorted(headings_by_level))
        if not should_include_task(headings, scope):
            continue

        raw_title = task_match.group(3).strip()
        priority_label, priority_value = priority_from_headings(headings)
        short_title, detail_text = parse_task_parts(raw_title)
        title = f"[{priority_label}] {clean_markdown_text(short_title)}"
        detail = build_detail(priority_label, detail_text)
        source_id = make_source_id(todo_path, headings, raw_title)

        items.append(
            TodoItem(
                line_no=line_no,
                title=title,
                detail=detail,
                raw_title=raw_title,
                heading_path=headings,
                priority_label=priority_label,
                priority_value=priority_value,
                source_id=source_id,
            )
        )

    return items


def parse_update_date(todo_path: Path) -> date | None:
    for line in todo_path.read_text(encoding="utf-8").splitlines():
        if "更新日期" not in line:
            continue
        match = re.search(r"(\d{4}-\d{2}-\d{2})", line)
        if not match:
            continue
        return date.fromisoformat(match.group(1))
    return None


def default_due_date(update_date: date | None, priority_label: str) -> DueDate | None:
    today = date.today()
    base_date = max(update_date or today, today)
    if priority_label == "P0":
        offset = 1
    elif priority_label == "P1":
        offset = 2
    elif priority_label == "P2":
        offset = 3
    elif priority_label == "P3":
        offset = 4
    else:
        offset = 5
    return DueDate(label=priority_label, value=base_date.fromordinal(base_date.toordinal() + offset))


SYNC_APPLESCRIPT = r"""
on run argv
    set listName to item 1 of argv
    set taskName to item 2 of argv
    set taskBody to item 3 of argv
    set taskPriority to (item 4 of argv) as integer
    set markerText to item 5 of argv
    set savedReminderId to item 6 of argv
    set dueText to item 7 of argv
    set taskFlagged to false
    if item 8 of argv is "true" then set taskFlagged to true

    tell application id "com.apple.reminders"
        if not (exists list listName) then
            make new list with properties {name:listName}
        end if

        set targetList to list listName
        set matchedReminder to missing value

        if savedReminderId is not "" then
            repeat with candidateReminder in reminders of targetList
                try
                    if (id of candidateReminder as text) is savedReminderId then
                        set matchedReminder to candidateReminder
                        exit repeat
                    end if
                end try
            end repeat
        end if

        if matchedReminder is missing value then
            repeat with candidateReminder in reminders of targetList
                try
                    if body of candidateReminder contains markerText then
                        set matchedReminder to candidateReminder
                        exit repeat
                    end if
                end try
            end repeat
        end if

        if matchedReminder is missing value then
            repeat with candidateReminder in reminders of targetList
                try
                    if name of candidateReminder is taskName then
                        set matchedReminder to candidateReminder
                        exit repeat
                    end if
                end try
            end repeat
        end if

        if matchedReminder is missing value then
            set matchedReminder to make new reminder at end of reminders of targetList with properties {name:taskName, body:taskBody, priority:taskPriority}
            set flagged of matchedReminder to taskFlagged
            if dueText is not "" then
                set due date of matchedReminder to date dueText
            end if
            return "created" & tab & (id of matchedReminder as text)
        else
            set name of matchedReminder to taskName
            set body of matchedReminder to taskBody
            set priority of matchedReminder to taskPriority
            set flagged of matchedReminder to taskFlagged
            set completed of matchedReminder to false
            if dueText is not "" then
                set due date of matchedReminder to date dueText
            end if
            return "updated" & tab & (id of matchedReminder as text)
        end if
    end tell
end run
"""


COMPLETE_APPLESCRIPT = r"""
on run argv
    set listName to item 1 of argv
    set savedReminderId to item 2 of argv

    tell application id "com.apple.reminders"
        if not (exists list listName) then
            return "missing-list"
        end if

        set targetList to list listName
        repeat with candidateReminder in reminders of targetList
            try
                if (id of candidateReminder as text) is savedReminderId then
                    set completed of candidateReminder to true
                    return "completed"
                end if
            end try
        end repeat
    end tell

    return "missing-reminder"
end run
"""


def parse_due_map(raw_due_map: str) -> dict[str, DueDate]:
    if not raw_due_map:
        return {}

    due_map: dict[str, DueDate] = {}
    for part in raw_due_map.split(","):
        part = part.strip()
        if not part:
            continue
        if "=" not in part:
            raise ValueError(f"Invalid due-map entry: {part!r}. Expected LABEL=YYYY-MM-DD.")

        raw_label, raw_value = part.split("=", 1)
        label = raw_label.strip()
        try:
            due_value = date.fromisoformat(raw_value.strip())
        except ValueError as exc:
            raise ValueError(f"Invalid due date for {label}: {raw_value!r}. Expected YYYY-MM-DD.") from exc

        due_map[label] = DueDate(label=label, value=due_value)

    return due_map


def load_state(state_path: Path) -> dict[str, dict[str, str]]:
    if not state_path.exists():
        return {}
    data = json.loads(state_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return {}
    lists = data.get("lists", {})
    return lists if isinstance(lists, dict) else {}


def save_state(state_path: Path, lists_state: dict[str, dict[str, str]]) -> None:
    state_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "version": 1,
        "lists": lists_state,
    }
    state_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def prune_duplicate_state_entries(
    list_state: dict[str, str],
    active_source_to_reminder: dict[str, str],
) -> None:
    active_reminder_ids = {rid for rid in active_source_to_reminder.values() if rid}
    for source_id, reminder_id in list(list_state.items()):
        if source_id in active_source_to_reminder:
            continue
        if reminder_id in active_reminder_ids:
            del list_state[source_id]


def clean_reminder_body(item: TodoItem, due_date: DueDate | None, marker: str) -> str:
    if item.detail:
        return item.detail
    return ""


def sync_item(
    list_name: str,
    item: TodoItem,
    due_date: DueDate | None,
    saved_reminder_id: str,
) -> tuple[str, str]:
    marker = f"{SOURCE_MARKER_PREFIX} {item.source_id}"
    body = clean_reminder_body(item, due_date, marker)
    due_text = due_date.applescript_text if due_date is not None else ""
    flagged_text = "true" if should_flag_item(item) else "false"

    result = subprocess.run(
        [
            "osascript",
            "-e",
            SYNC_APPLESCRIPT,
            list_name,
            item.title,
            body,
            str(item.priority_value),
            marker,
            saved_reminder_id,
            due_text,
            flagged_text,
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        stderr = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(stderr)

    action, _, reminder_id = result.stdout.strip().partition("\t")
    if not action or not reminder_id:
        raise RuntimeError(f"Unexpected osascript result: {result.stdout.strip()!r}")
    return action, reminder_id


def complete_item(list_name: str, saved_reminder_id: str) -> str:
    result = subprocess.run(
        [
            "osascript",
            "-e",
            COMPLETE_APPLESCRIPT,
            list_name,
            saved_reminder_id,
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        stderr = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(stderr)

    return result.stdout.strip() or "missing-reminder"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--todo", type=Path, default=DEFAULT_TODO, help="Markdown todo file to read")
    parser.add_argument("--list", default=DEFAULT_LIST_NAME, help="macOS Reminders list name")
    parser.add_argument(
        "--scope",
        choices=("active", "priority-and-human", "all"),
        default="active",
        help="Which unchecked tasks to sync. Default: only current execution-priority tasks.",
    )
    parser.add_argument(
        "--due-map",
        default="",
        help="Optional comma-separated due-date mapping, for example: P0=2026-04-27,P1=2026-04-29.",
    )
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE_PATH, help="Local sync state file")
    parser.add_argument(
        "--complete-missing",
        action="store_true",
        help="Mark reminders as completed when they are no longer active in the synced scope.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print parsed reminders without changing Reminders")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    todo_path = args.todo.resolve()
    if not todo_path.exists():
        print(f"Todo file not found: {todo_path}", file=sys.stderr)
        return 2

    items = parse_todos(todo_path, args.scope)
    update_date = parse_update_date(todo_path)
    due_map = parse_due_map(args.due_map)
    if args.dry_run:
        print(f"List: {args.list}")
        print(f"Todo: {todo_path.relative_to(REPO_ROOT)}")
        print(f"Scope: {args.scope}")
        if update_date is not None:
            print(f"Update date: {update_date.isoformat()}")
        if due_map:
            print("Due map: " + ", ".join(f"{key}={value.value.isoformat()}" for key, value in due_map.items()))
        print(f"Items: {len(items)}")
        for item in items:
            due_date = due_map.get(item.priority_label) or default_due_date(update_date, item.priority_label)
            due_suffix = f", due {due_date.value.isoformat()}" if due_date is not None else ""
            print(
                f"- {item.title} | {item.detail} "
                f"({item.source_id}, line {item.line_no}, priority {item.priority_value}{due_suffix})"
            )
        return 0

    created = 0
    updated = 0
    completed = 0
    lists_state = load_state(args.state.resolve())
    list_state = lists_state.setdefault(args.list, {})
    active_source_ids = {item.source_id for item in items}
    active_source_to_reminder: dict[str, str] = {}
    for item in items:
        due_date = due_map.get(item.priority_label) or default_due_date(update_date, item.priority_label)
        action, reminder_id = sync_item(
            args.list,
            item,
            due_date,
            list_state.get(item.source_id, ""),
        )
        list_state[item.source_id] = reminder_id
        active_source_to_reminder[item.source_id] = reminder_id
        if action == "created":
            created += 1
        elif action == "updated":
            updated += 1
        else:
            print(f"{item.title}: {action}")

    prune_duplicate_state_entries(list_state, active_source_to_reminder)
    active_reminder_ids = {rid for rid in active_source_to_reminder.values() if rid}
    if args.complete_missing:
        for source_id, reminder_id in list(list_state.items()):
            if source_id in active_source_ids or not reminder_id:
                continue
            if reminder_id in active_reminder_ids:
                del list_state[source_id]
                continue
            action = complete_item(args.list, reminder_id)
            if action == "completed":
                completed += 1
            del list_state[source_id]

    save_state(args.state.resolve(), lists_state)
    print(
        f"Synced {len(items)} reminders to '{args.list}': "
        f"{created} created, {updated} updated, {completed} completed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
