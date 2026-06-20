"""Apply deep-read note bodies to Telephone paper notes.

Input: JSON list on stdin. Each entry must include a `telephone_index` and the
deep-read fields rendered below.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "notes"


def parse_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("unterminated frontmatter")
    return text[: end + 5], text[end + 5 :].lstrip("\n")


def front_value(frontmatter: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.*)$", frontmatter, flags=re.M)
    return match.group(1).strip().strip('"') if match else ""


def set_front_value(frontmatter: str, key: str, value: str) -> str:
    line = f"{key}: {value}"
    if re.search(rf"^{re.escape(key)}:", frontmatter, flags=re.M):
        return re.sub(rf"^{re.escape(key)}:.*$", line, frontmatter, flags=re.M)
    return frontmatter.replace("\n---\n", f"\n{line}\n---\n")


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def render(title: str, item: dict) -> str:
    return f"""# {title}

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

{item["matter"]}

## Core Question

{item["problem"]}

## Method / Evidence Base

{item["method"]}

## Core Claim / Result

{item["findings"]}

## Evidence We May Cite

{bullets(item["evidence"])}

## Telephone Bridge

{bullets(item["bridge"])}

## What We Add Beyond This Paper

{item["add"]}

## Draft-Ready Use Sentence

> {item["sentence"]}

## Caveats

{bullets(item["caveats"])}

## Citation Decision

Decision: `{item["decision"]}`

Reason: {item["reason"]}
"""


def main() -> int:
    items = json.load(sys.stdin)
    by_index = {int(item["telephone_index"]): item for item in items}
    updated: list[str] = []

    for path in sorted(ROOT.glob("[0-9][0-9]_*/*.md")):
        text = path.read_text(encoding="utf-8")
        match = re.search(r"^telephone_index:\s*(\d+)", text, flags=re.M)
        if not match:
            continue
        index = int(match.group(1))
        if index not in by_index:
            continue

        frontmatter, _ = parse_frontmatter(text)
        title = front_value(frontmatter, "title")
        frontmatter = set_front_value(frontmatter, "read_status", "deep-read")
        frontmatter = set_front_value(
            frontmatter,
            "deep_read_scope",
            "abstract-introduction-method-results-conclusion-fulltext-pass",
        )
        path.write_text(
            frontmatter + "\n\n" + render(title, by_index[index]),
            encoding="utf-8",
            newline="\n",
        )
        updated.append(f"{index:02d} {path.relative_to(ROOT)}")

    missing = sorted(set(by_index) - {int(line[:2]) for line in updated})
    print(f"updated={len(updated)}")
    for line in updated:
        print(line)
    if missing:
        print("missing=" + ",".join(str(index) for index in missing))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
