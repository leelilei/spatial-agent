from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNS = ROOT / "sim" / "runs"
OUT = ROOT / "paper" / "supplement"

CURRENT_PAIR = ("sunday", "community center")
STALE_PAIR = ("saturday", "front porch")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def pct(part: int, total: int) -> float:
    return round(100.0 * part / total, 1) if total else 0.0


def clean_text(text: str) -> str:
    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "--",
        "\u2026": "...",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    return text.encode("ascii", "ignore").decode("ascii")


def has_pair(text: str, markers: tuple[str, str]) -> bool:
    lower = text.lower()
    return all(marker in lower for marker in markers)


def has_any(text: str, markers: tuple[str, str]) -> bool:
    lower = text.lower()
    return any(marker in lower for marker in markers)


def infer_scenario(experiment_id: str) -> str:
    if "book_club" in experiment_id:
        return "book_club"
    if "carpool" in experiment_id:
        return "carpool"
    return "repair_drive"


def infer_intervention(experiment_id: str) -> str:
    tail = experiment_id.split("/")[-1]
    if experiment_id.endswith("r1_broadcast"):
        return "early_all_agent_broadcast"
    if experiment_id.endswith("r5_broadcast"):
        return "late_all_agent_broadcast"
    if tail == "baseline" or tail.endswith("_baseline"):
        return "baseline"
    if tail == "source" or tail.endswith("_source"):
        return "source"
    if tail == "broadcast" or tail.endswith("_broadcast"):
        return "broadcast"
    if experiment_id.startswith("p3_power") or experiment_id.startswith("m0_strong"):
        return "capability"
    if experiment_id.startswith("p3b_conn") or experiment_id.startswith("m1/"):
        return "connectivity"
    if experiment_id.startswith("m2_memory") or experiment_id.startswith("m3_verify"):
        return "memory"
    return experiment_id.split("/")[-1]


def infer_meetings_per_round(experiment_id: str) -> str:
    parts = experiment_id.split("/")
    tail = parts[-1]
    match = re.search(r"(?:^|_)m([123])(?:_|$)", tail)
    if match:
        return f"m={match.group(1)}"
    if len(parts) > 1 and parts[1].startswith("m") and parts[1][1:2].isdigit():
        return f"m={parts[1][1]}"
    return "m=2"


def aggregate_counts(rows: list[dict]) -> dict:
    total = sum(row.get("agent_count", 0) for row in rows)
    current = sum(row.get("currency_interview", {}).get("current", 0) for row in rows)
    stale = sum(row.get("currency_interview", {}).get("stale", 0) for row in rows)
    unknown = sum(row.get("currency_interview", {}).get("unknown", 0) for row in rows)
    return {
        "agents_total": total,
        "current": current,
        "stale": stale,
        "unknown": unknown,
        "held_current_rate": pct(current, total),
    }


def build_experiment_tables() -> tuple[list[dict], list[dict]]:
    matrix_rows: list[dict] = []
    seed_rows: list[dict] = []

    for aggregate_path in sorted(RUNS.rglob("aggregate.json")):
        experiment_id = aggregate_path.parent.relative_to(RUNS).as_posix()
        block = experiment_id.split("/")[0]
        aggregate = load_json(aggregate_path)
        rows = aggregate.get("rows", [])
        if not rows:
            continue

        counts = aggregate_counts(rows)
        models = sorted({row.get("model", "") for row in rows})
        memories = sorted({row.get("memory", "") for row in rows})
        seeds = sorted({row.get("schedule_seed") for row in rows if row.get("schedule_seed") is not None})
        rounds = sorted({row.get("rounds") for row in rows if row.get("rounds") is not None})
        turns = sorted({row.get("turns") for row in rows if row.get("turns") is not None})

        matrix_rows.append(
            {
                "experiment_id": experiment_id,
                "block": block,
                "scenario": infer_scenario(experiment_id),
                "intervention": infer_intervention(experiment_id),
                "model": ";".join(models),
                "memory": ";".join(memories),
                "meetings_per_round": infer_meetings_per_round(experiment_id),
                "runs": len(rows),
                "seeds": ";".join(str(seed) for seed in seeds),
                "rounds": ";".join(str(r) for r in rounds),
                "turns": ";".join(str(t) for t in turns),
                **counts,
            }
        )

        for row in rows:
            run_counts = row.get("currency_interview", {})
            total = row.get("agent_count", 0)
            seed_rows.append(
                {
                    "experiment_id": experiment_id,
                    "run_index": row.get("run_index", ""),
                    "schedule_seed": row.get("schedule_seed", ""),
                    "model": row.get("model", ""),
                    "memory": row.get("memory", ""),
                    "meetings_per_round": infer_meetings_per_round(experiment_id),
                    "agent_count": total,
                    "rounds": row.get("rounds", ""),
                    "turns": row.get("turns", ""),
                    "current": run_counts.get("current", 0),
                    "stale": run_counts.get("stale", 0),
                    "unknown": run_counts.get("unknown", 0),
                    "held_current_rate": pct(run_counts.get("current", 0), total),
                    "unsupported_specific": row.get("unsupported_specific", ""),
                }
            )

    return matrix_rows, seed_rows


def load_source_interviews(run_dir: Path) -> tuple[dict[str, dict], dict[str, str]]:
    data = load_json(run_dir / "interview_currency.json")["results"]
    id_for_name = {entry.get("name", ""): agent_id for agent_id, entry in data.items()}
    return data, id_for_name


def build_source_trace() -> tuple[list[dict], list[dict], list[dict]]:
    source_dir = RUNS / "m4_rebroadcast" / "source" / "gpt-5.4-mini" / "ga"
    agent_rows: list[dict] = []
    examples: list[dict] = []

    for run_dir in sorted(source_dir.glob("run_*")):
        interviews, id_for_name = load_source_interviews(run_dir)
        names = {agent_id: entry.get("name", agent_id) for agent_id, entry in interviews.items()}

        heard_pair = Counter()
        heard_pair_from_speech = Counter()
        heard_any_marker = Counter()
        world_pair_injection = Counter()
        heard_examples: dict[str, list[tuple[int, str, str]]] = {agent_id: [] for agent_id in interviews}

        memories = load_json(run_dir / "memory_snapshots.json")
        for agent_id, memory in memories.items():
            for event in memory.get("events", []):
                text = event.get("text", "")
                speaker = event.get("speaker", "")
                if has_pair(text, CURRENT_PAIR):
                    heard_pair[agent_id] += 1
                    if speaker != "world":
                        heard_pair_from_speech[agent_id] += 1
                    if len(heard_examples.setdefault(agent_id, [])) < 3:
                        heard_examples[agent_id].append((event.get("round", -1), speaker, clean_text(text)))
                if has_any(text, CURRENT_PAIR):
                    heard_any_marker[agent_id] += 1
                if speaker == "world" and has_pair(text, CURRENT_PAIR):
                    world_pair_injection[agent_id] += 1

        said_pair = Counter()
        said_any_marker = Counter()
        said_examples: dict[str, list[tuple[int, str, str]]] = {agent_id: [] for agent_id in interviews}
        for round_path in sorted(run_dir.glob("round_*.json")):
            round_data = load_json(round_path)
            round_id = round_data.get("round", "")
            for encounter in round_data.get("encounters", []):
                for utterance in encounter.get("utterances", []):
                    speaker = utterance.get("speaker", "")
                    speaker_id = id_for_name.get(speaker, speaker if speaker in interviews else "")
                    if not speaker_id:
                        continue
                    text = utterance.get("text", "")
                    if has_pair(text, CURRENT_PAIR):
                        said_pair[speaker_id] += 1
                        if len(said_examples.setdefault(speaker_id, [])) < 3:
                            said_examples[speaker_id].append(
                                (round_id, utterance.get("listener", ""), clean_text(text))
                            )
                    if has_any(text, CURRENT_PAIR):
                        said_any_marker[speaker_id] += 1

        for agent_id, interview in sorted(interviews.items()):
            row = {
                "run": run_dir.name,
                "agent_id": agent_id,
                "agent_name": names.get(agent_id, agent_id),
                "final_verdict": interview.get("verdict", ""),
                "heard_current_pair": heard_pair[agent_id],
                "heard_current_pair_from_speech": heard_pair_from_speech[agent_id],
                "said_current_pair": said_pair[agent_id],
                "heard_any_current_marker": heard_any_marker[agent_id],
                "said_any_current_marker": said_any_marker[agent_id],
                "world_current_pair_injection": world_pair_injection[agent_id],
                "final_answer": clean_text(interview.get("answer", "")),
            }
            agent_rows.append(row)

            if row["final_verdict"] != "current" and (
                row["heard_current_pair_from_speech"] or row["said_current_pair"]
            ):
                examples.append(
                    {
                        **row,
                        "heard_examples": heard_examples.get(agent_id, []),
                        "said_examples": said_examples.get(agent_id, []),
                    }
                )

    summary_rows = summarize_source_trace(agent_rows)
    return agent_rows, summary_rows, examples


def summarize_source_trace(agent_rows: list[dict]) -> list[dict]:
    classes = [
        ("all_source_condition_agents", lambda row: True),
        ("heard_current_pair_from_speech", lambda row: row["heard_current_pair_from_speech"] > 0),
        ("said_current_pair", lambda row: row["said_current_pair"] > 0),
        (
            "heard_or_said_current_pair",
            lambda row: row["heard_current_pair_from_speech"] > 0 or row["said_current_pair"] > 0,
        ),
        ("heard_any_current_marker", lambda row: row["heard_any_current_marker"] > 0),
        ("said_any_current_marker", lambda row: row["said_any_current_marker"] > 0),
        ("world_current_pair_injection", lambda row: row["world_current_pair_injection"] > 0),
    ]

    summary_rows: list[dict] = []
    for label, predicate in classes:
        matched = [row for row in agent_rows if predicate(row)]
        verdicts = Counter(row["final_verdict"] for row in matched)
        total = len(matched)
        summary_rows.append(
            {
                "trace_class": label,
                "agents": total,
                "final_current": verdicts.get("current", 0),
                "final_stale": verdicts.get("stale", 0),
                "final_unknown": verdicts.get("unknown", 0),
                "final_current_rate": pct(verdicts.get("current", 0), total),
                "final_unknown_rate": pct(verdicts.get("unknown", 0), total),
            }
        )
    return summary_rows


def write_examples(examples: list[dict]) -> None:
    path = OUT / "source_trace_examples.md"
    lines = [
        "# Source Trace Examples",
        "",
        "These are source-condition agents that encountered a strict current pair",
        "(`Sunday` and `community center`) in speech and still failed to give a",
        "current final interview answer.",
        "",
    ]
    for ex in examples:
        lines.append(
            f"## {ex['run']} / {ex['agent_id']} {ex['agent_name']} -> {ex['final_verdict']}"
        )
        lines.append("")
        lines.append(f"- Final answer: {ex['final_answer'] or '[empty]'}")
        lines.append(
            "- Counts: "
            f"heard_from_speech={ex['heard_current_pair_from_speech']}, "
            f"said={ex['said_current_pair']}, "
            f"heard_any_marker={ex['heard_any_current_marker']}"
        )
        for round_id, speaker, text in ex["heard_examples"]:
            lines.append(f"- Heard r{round_id} from {speaker}: {text}")
        for round_id, listener, text in ex["said_examples"]:
            lines.append(f"- Said r{round_id} to {listener}: {text}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    matrix_rows, seed_rows = build_experiment_tables()
    write_csv(
        OUT / "experiment_matrix.csv",
        matrix_rows,
        [
            "experiment_id",
            "block",
            "scenario",
            "intervention",
            "model",
            "memory",
            "meetings_per_round",
            "runs",
            "seeds",
            "rounds",
            "turns",
            "agents_total",
            "current",
            "stale",
            "unknown",
            "held_current_rate",
        ],
    )
    write_csv(
        OUT / "seed_table.csv",
        seed_rows,
        [
            "experiment_id",
            "run_index",
            "schedule_seed",
            "model",
            "memory",
            "meetings_per_round",
            "agent_count",
            "rounds",
            "turns",
            "current",
            "stale",
            "unknown",
            "held_current_rate",
            "unsupported_specific",
        ],
    )

    agent_rows, summary_rows, examples = build_source_trace()
    write_csv(
        OUT / "source_trace_agents.csv",
        agent_rows,
        [
            "run",
            "agent_id",
            "agent_name",
            "final_verdict",
            "heard_current_pair",
            "heard_current_pair_from_speech",
            "said_current_pair",
            "heard_any_current_marker",
            "said_any_current_marker",
            "world_current_pair_injection",
            "final_answer",
        ],
    )
    write_csv(
        OUT / "source_trace_summary.csv",
        summary_rows,
        [
            "trace_class",
            "agents",
            "final_current",
            "final_stale",
            "final_unknown",
            "final_current_rate",
            "final_unknown_rate",
        ],
    )
    write_examples(examples)

    print(f"Wrote {len(matrix_rows)} experiment rows")
    print(f"Wrote {len(seed_rows)} seed rows")
    print(f"Wrote {len(agent_rows)} source trace agent rows")
    print(f"Wrote {len(summary_rows)} source trace summary rows")
    print(f"Wrote {len(examples)} source trace examples")


if __name__ == "__main__":
    main()
