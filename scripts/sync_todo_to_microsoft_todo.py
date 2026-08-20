#!/usr/bin/env python3
"""Sync actionable Markdown todo items to Microsoft To Do via Microsoft Graph.

Requires a Microsoft Entra app registration that supports public-client/device-code
sign-in. Pass the Application (client) ID with --client-id or MS_TODO_CLIENT_ID.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

import requests

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from sync_todo_to_reminders import (  # noqa: E402
    DEFAULT_TODO,
    REPO_ROOT,
    SECTION_DESCRIPTIONS,
    DueDate,
    TodoItem,
    parse_due_map,
    parse_todos,
    short_section_name,
)


DEFAULT_LIST_NAME = "SpatialAgent Survey"
DEFAULT_STATE_PATH = REPO_ROOT / ".cache" / "microsoft_todo_sync_state.json"
DEFAULT_SCOPE = "Tasks.ReadWrite offline_access"
GRAPH_ROOT = "https://graph.microsoft.com/v1.0"
AUTH_ROOT = "https://login.microsoftonline.com"


def graph_headers(access_token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }


def load_state(state_path: Path) -> dict[str, Any]:
    if not state_path.exists():
        return {"version": 1, "tokens": {}, "lists": {}}
    data = json.loads(state_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return {"version": 1, "tokens": {}, "lists": {}}
    data.setdefault("version", 1)
    data.setdefault("tokens", {})
    data.setdefault("lists", {})
    return data


def save_state(state_path: Path, state: dict[str, Any]) -> None:
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def token_is_valid(tokens: dict[str, Any]) -> bool:
    expires_at = tokens.get("expires_at")
    return isinstance(expires_at, (int, float)) and expires_at > time.time() + 120


def refresh_access_token(client_id: str, tenant: str, scope: str, tokens: dict[str, Any]) -> dict[str, Any] | None:
    refresh_token = tokens.get("refresh_token")
    if not refresh_token:
        return None

    response = requests.post(
        f"{AUTH_ROOT}/{tenant}/oauth2/v2.0/token",
        data={
            "client_id": client_id,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "scope": scope,
        },
        timeout=30,
    )
    if response.status_code != 200:
        return None
    return normalize_token_response(response.json(), client_id, tenant)


def normalize_token_response(token_response: dict[str, Any], client_id: str, tenant: str) -> dict[str, Any]:
    expires_in = int(token_response.get("expires_in", 3600))
    return {
        "client_id": client_id,
        "tenant": tenant,
        "access_token": token_response["access_token"],
        "refresh_token": token_response.get("refresh_token"),
        "scope": token_response.get("scope"),
        "expires_at": int(time.time()) + expires_in,
    }


def acquire_device_token(client_id: str, tenant: str, scope: str) -> dict[str, Any]:
    device_response = requests.post(
        f"{AUTH_ROOT}/{tenant}/oauth2/v2.0/devicecode",
        data={
            "client_id": client_id,
            "scope": scope,
        },
        timeout=30,
    )
    if device_response.status_code != 200:
        raise RuntimeError(f"Device-code request failed: {device_response.status_code} {device_response.text}")

    device = device_response.json()
    print(device.get("message", ""), flush=True)

    interval = int(device.get("interval", 5))
    expires_at = time.time() + int(device.get("expires_in", 900))
    while time.time() < expires_at:
        time.sleep(interval)
        token_response = requests.post(
            f"{AUTH_ROOT}/{tenant}/oauth2/v2.0/token",
            data={
                "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
                "client_id": client_id,
                "device_code": device["device_code"],
            },
            timeout=30,
        )
        if token_response.status_code == 200:
            return normalize_token_response(token_response.json(), client_id, tenant)

        payload = token_response.json()
        error = payload.get("error")
        if error == "authorization_pending":
            continue
        if error == "slow_down":
            interval += 5
            continue
        raise RuntimeError(f"Device-code login failed: {error}: {payload.get('error_description')}")

    raise RuntimeError("Device-code login timed out.")


def get_access_token(client_id: str, tenant: str, scope: str, state: dict[str, Any]) -> str:
    tokens = state.get("tokens", {})
    if tokens.get("client_id") == client_id and tokens.get("tenant") == tenant and token_is_valid(tokens):
        return tokens["access_token"]

    if tokens.get("client_id") == client_id and tokens.get("tenant") == tenant:
        refreshed = refresh_access_token(client_id, tenant, scope, tokens)
        if refreshed:
            state["tokens"] = refreshed
            return refreshed["access_token"]

    state["tokens"] = acquire_device_token(client_id, tenant, scope)
    return state["tokens"]["access_token"]


def request_json(method: str, url: str, access_token: str, **kwargs: Any) -> Any:
    response = requests.request(method, url, headers=graph_headers(access_token), timeout=30, **kwargs)
    if response.status_code >= 400:
        raise RuntimeError(f"Graph request failed: {method} {url} -> {response.status_code} {response.text}")
    if response.status_code == 204:
        return None
    return response.json()


def get_or_create_list(access_token: str, list_name: str) -> str:
    lists = request_json("GET", f"{GRAPH_ROOT}/me/todo/lists", access_token)
    for task_list in lists.get("value", []):
        if task_list.get("displayName") == list_name:
            return task_list["id"]

    created = request_json(
        "POST",
        f"{GRAPH_ROOT}/me/todo/lists",
        access_token,
        json={"displayName": list_name},
    )
    return created["id"]


def graph_due_date(due_date: DueDate | None, time_zone: str) -> dict[str, str] | None:
    if due_date is None:
        return None
    return {
        "dateTime": f"{due_date.value.isoformat()}T09:00:00",
        "timeZone": time_zone,
    }


def reminder_date_for_due(due_date: DueDate | None, time_zone: str) -> dict[str, str] | None:
    if due_date is None:
        return None
    reminder_day = due_date.value
    return {
        "dateTime": f"{reminder_day.isoformat()}T09:00:00",
        "timeZone": time_zone,
    }


def importance_for_item(item: TodoItem) -> str:
    if item.priority_label == "P0":
        return "high"
    if item.priority_label == "P1":
        return "normal"
    return "low"


def body_for_item(item: TodoItem, due_date: DueDate | None) -> dict[str, str]:
    description = SECTION_DESCRIPTIONS.get(item.priority_label, "来自 SpatialAgent survey 当前 todo。")
    return {
        "contentType": "text",
        "content": "\n".join(
            [
                f"板块：{short_section_name(item)}",
                f"目的：{description}",
            ]
        ),
    }


def task_payload(item: TodoItem, due_date: DueDate | None, time_zone: str) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "title": item.title,
        "body": body_for_item(item, due_date),
        "importance": importance_for_item(item),
        "status": "notStarted",
    }
    due = graph_due_date(due_date, time_zone)
    if due:
        payload["dueDateTime"] = due
        payload["reminderDateTime"] = reminder_date_for_due(due_date, time_zone)
        payload["isReminderOn"] = True
    return payload


def sync_task(
    access_token: str,
    list_id: str,
    item: TodoItem,
    due_date: DueDate | None,
    time_zone: str,
    saved_task_id: str,
) -> tuple[str, str]:
    payload = task_payload(item, due_date, time_zone)
    if saved_task_id:
        try:
            updated = request_json(
                "PATCH",
                f"{GRAPH_ROOT}/me/todo/lists/{list_id}/tasks/{saved_task_id}",
                access_token,
                json=payload,
            )
            return "updated", updated["id"]
        except RuntimeError:
            pass

    created = request_json(
        "POST",
        f"{GRAPH_ROOT}/me/todo/lists/{list_id}/tasks",
        access_token,
        json=payload,
    )
    return "created", created["id"]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--todo", type=Path, default=DEFAULT_TODO, help="Markdown todo file to read")
    parser.add_argument("--list", default=DEFAULT_LIST_NAME, help="Microsoft To Do list name")
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE_PATH, help="Local token/task-id state file")
    parser.add_argument("--client-id", default=os.environ.get("MS_TODO_CLIENT_ID", ""), help="Microsoft app client ID")
    parser.add_argument("--tenant", default=os.environ.get("MS_TODO_TENANT", "common"), help="Tenant: common, consumers, organizations, or tenant ID")
    parser.add_argument("--scope", default=DEFAULT_SCOPE, help="OAuth scopes")
    parser.add_argument("--time-zone", default="Asia/Shanghai", help="Graph dateTimeTimeZone timeZone value")
    parser.add_argument(
        "--scope-filter",
        choices=("active", "priority-and-human", "all"),
        default="active",
        help="Which unchecked Markdown tasks to sync.",
    )
    parser.add_argument(
        "--due-map",
        default="",
        help="Optional comma-separated due-date mapping, for example: P0=2026-04-27,P1=2026-04-29.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print parsed tasks without logging in or syncing")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    todo_path = args.todo.resolve()
    if not todo_path.exists():
        print(f"Todo file not found: {todo_path}", file=sys.stderr)
        return 2

    items = parse_todos(todo_path, args.scope_filter)
    due_map = parse_due_map(args.due_map)
    if args.dry_run:
        print(f"List: {args.list}")
        print(f"Todo: {todo_path.relative_to(REPO_ROOT)}")
        print(f"Items: {len(items)}")
        if due_map:
            print("Due map: " + ", ".join(f"{key}={value.value.isoformat()}" for key, value in due_map.items()))
        for item in items:
            due_date = due_map.get(item.priority_label)
            due_suffix = f", due {due_date.value.isoformat()}" if due_date else ""
            print(f"- {item.title} ({item.source_id}{due_suffix})")
        return 0

    if not args.client_id:
        print("Missing Microsoft app client ID. Pass --client-id or set MS_TODO_CLIENT_ID.", file=sys.stderr)
        return 2

    state_path = args.state.resolve()
    state = load_state(state_path)
    access_token = get_access_token(args.client_id, args.tenant, args.scope, state)
    list_id = get_or_create_list(access_token, args.list)

    list_state = state.setdefault("lists", {}).setdefault(args.list, {})
    created = 0
    updated = 0
    for item in items:
        action, task_id = sync_task(
            access_token,
            list_id,
            item,
            due_map.get(item.priority_label),
            args.time_zone,
            list_state.get(item.source_id, ""),
        )
        list_state[item.source_id] = task_id
        if action == "created":
            created += 1
        elif action == "updated":
            updated += 1

    save_state(state_path, state)
    print(f"Synced {len(items)} tasks to Microsoft To Do list '{args.list}': {created} created, {updated} updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
