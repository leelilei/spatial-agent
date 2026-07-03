"""Evaluate and, when every gate passes, freeze the CityIntent v1 package."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


BENCHMARK_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = BENCHMARK_ROOT.parents[2]
DEFAULT_AUDIT_DIR = (
    REPO_ROOT
    / "6-city"
    / "annotation"
    / "cityintent_v1_rc1_blind_validation_2026-07-02"
)
DEFAULT_RESULT_DIR = (
    REPO_ROOT
    / "6-city"
    / "results"
    / "cityintent_v1_rc1"
    / "external_frameworks_4x4x1_gpt54mini_2026-07-02"
)
DEFAULT_REPORT_DIR = DEFAULT_AUDIT_DIR / "release_gate"
REQUIRED_OFFICIAL_ADAPTERS = {
    "gatsim_official_planner",
    "sotopia_official_llm_agent",
    "generative_agents_official_planner",
    "agentsociety_official_plan_blocks",
}
IMMUTABLE_AUDIT_INPUTS = {
    "blinded/audit_items.jsonl",
    "blinded/audit_packet.md",
    "blinded/world_reference.json",
    "sealed/audit_key.csv",
    "RUBRIC.md",
}

if str(Path(__file__).parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).parent))

from build_human_audit import file_sha256  # noqa: E402
from score_human_audit import read_csv, score_annotations  # noqa: E402


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8-sig") as f:
        return json.load(f)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write("\n")


def normalized_sha256(path: Path) -> str:
    if path.suffix.lower() in {".json", ".jsonl", ".md", ".py", ".csv"}:
        return file_sha256(path)
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_command(command: list[str]) -> dict[str, Any]:
    completed = subprocess.run(
        command,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    return {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def audit_input_integrity(audit_dir: Path) -> tuple[list[str], dict[str, str]]:
    manifest = load_json(audit_dir / "audit_manifest.json")
    expected = manifest.get("normalized_text_sha256", {})
    blockers: list[str] = []
    observed: dict[str, str] = {}
    for relative in sorted(IMMUTABLE_AUDIT_INPUTS):
        path = audit_dir / relative
        if not path.exists():
            blockers.append(f"missing immutable audit input: {relative}")
            continue
        observed[relative] = normalized_sha256(path)
        if expected.get(relative) != observed[relative]:
            blockers.append(f"immutable audit input checksum changed: {relative}")
    return blockers, observed


def result_archive_checks(result_dir: Path, gate: dict[str, Any]) -> list[str]:
    blockers: list[str] = []
    manifest_path = result_dir / "manifest.json"
    if not manifest_path.exists():
        return [f"missing v1 rc1 result manifest: {manifest_path}"]
    manifest = load_json(manifest_path)
    if manifest.get("benchmark_version") != "1.0-rc1":
        blockers.append("external trace archive must identify benchmark_version 1.0-rc1")
    expected_rows = int(gate["audit_item_count"])
    if int(manifest.get("row_count", 0)) < expected_rows:
        blockers.append(
            f"external trace archive has {manifest.get('row_count', 0)} rows; "
            f"requires at least {expected_rows}"
        )
    agents = set(manifest.get("agents", []))
    missing_agents = sorted(REQUIRED_OFFICIAL_ADAPTERS - agents)
    if missing_agents:
        blockers.append(f"external trace archive missing adapters: {missing_agents}")
    if len(manifest.get("scenario_ids", [])) < int(gate["scenario_count"]):
        blockers.append("external trace archive has too few scenarios")
    traces = sorted(result_dir.glob("repeat_*/traces/traces.json"))
    if not traces:
        blockers.append("external trace archive contains no trace JSON")
    else:
        trace_count = sum(len(load_json(path)) for path in traces)
        if trace_count != int(manifest.get("row_count", -1)):
            blockers.append(
                f"trace count {trace_count} does not match manifest row_count "
                f"{manifest.get('row_count')}"
            )
    return blockers


def annotation_summary(rows: list[dict[str, str]]) -> dict[str, Any]:
    evidence = [row.get("evidence_sufficient", "").strip() for row in rows]
    confidence = [
        int(row["confidence"])
        for row in rows
        if row.get("confidence", "").strip().isdigit()
    ]
    return {
        "evidence_sufficient_rate": (
            round(sum(value == "yes" for value in evidence) / len(evidence), 3)
            if evidence
            else None
        ),
        "mean_confidence": (
            round(sum(confidence) / len(confidence), 3) if confidence else None
        ),
    }


def load_dispositions(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return {
        row.get("finding_id", "").strip(): {
            key: (value or "").strip() for key, value in row.items()
        }
        for row in rows
        if row.get("finding_id", "").strip()
    }


def evaluate_thresholds(
    score: dict[str, Any],
    annotations_a: list[dict[str, str]],
    annotations_b: list[dict[str, str]],
    gate: dict[str, Any],
) -> tuple[list[str], dict[str, Any]]:
    blockers: list[str] = []
    checks: dict[str, Any] = {"inter_annotator": {}, "verifier": {}}
    inter_gate = gate["inter_annotator"]
    for dimension in inter_gate["dimensions"]:
        values = score["inter_annotator_agreement"][dimension]
        passed = (
            values["n"] == score["audit_item_count"]
            and values["exact_agreement"] is not None
            and values["exact_agreement"] >= inter_gate["minimum_exact_agreement"]
            and values["cohen_kappa"] is not None
            and values["cohen_kappa"] >= inter_gate["minimum_cohen_kappa"]
        )
        checks["inter_annotator"][dimension] = {**values, "passed": passed}
        if not passed:
            blockers.append(f"inter-annotator threshold failed: {dimension}")

    calibration_gate = gate["verifier_calibration"]
    for annotator, dimensions in score["verifier_calibration"].items():
        checks["verifier"][annotator] = {}
        for dimension in calibration_gate["dimensions"]:
            values = dimensions[dimension]
            passed = (
                values["n"] > 0
                and values["exact_agreement"] is not None
                and values["exact_agreement"]
                >= calibration_gate["minimum_exact_agreement"]
            )
            checks["verifier"][annotator][dimension] = {
                **values,
                "passed": passed,
            }
            if not passed:
                blockers.append(
                    f"verifier calibration threshold failed: {annotator}/{dimension}"
                )

    summaries = {
        "annotator_a": annotation_summary(annotations_a),
        "annotator_b": annotation_summary(annotations_b),
    }
    checks["annotation_quality"] = summaries
    for annotator, values in summaries.items():
        evidence_rate = values["evidence_sufficient_rate"]
        if evidence_rate is None or evidence_rate < gate["minimum_evidence_sufficient_rate"]:
            blockers.append(f"evidence sufficiency threshold failed: {annotator}")
        confidence = values["mean_confidence"]
        if confidence is None or confidence < gate["minimum_mean_confidence"]:
            blockers.append(f"mean confidence threshold failed: {annotator}")
    return blockers, checks


def evaluate_release_gate(
    audit_dir: Path,
    result_dir: Path,
    run_runtime_checks: bool = True,
) -> dict[str, Any]:
    config = load_json(BENCHMARK_ROOT / "benchmark_config.json")
    gate = config["release_gate"]
    blockers: list[str] = []
    warnings: list[str] = []

    if config.get("version") not in {"1.0-rc1", "1.0"}:
        blockers.append(f"unexpected benchmark version: {config.get('version')}")
    if config.get("status") not in {
        "release_candidate_pending_human_audit",
        "frozen",
    }:
        blockers.append(f"unexpected benchmark status: {config.get('status')}")

    integrity_blockers, integrity = audit_input_integrity(audit_dir)
    blockers.extend(integrity_blockers)
    audit_manifest = load_json(audit_dir / "audit_manifest.json")
    if int(audit_manifest.get("audit_item_count", 0)) != int(gate["audit_item_count"]):
        blockers.append("audit item count does not match release-gate configuration")
    if int(audit_manifest.get("scenario_count", 0)) != int(gate["scenario_count"]):
        blockers.append("audit scenario count does not match release-gate configuration")
    if int(audit_manifest.get("cell_count", 0)) != int(gate["audit_item_count"]):
        blockers.append("audit does not contain one item per scenario-adapter cell")
    blockers.extend(result_archive_checks(result_dir, gate))

    annotations_a_path = audit_dir / "annotations" / "annotator_a.csv"
    annotations_b_path = audit_dir / "annotations" / "annotator_b.csv"
    key_path = audit_dir / "sealed" / "audit_key.csv"
    score = score_annotations(
        annotations_a_path,
        annotations_b_path,
        key_path,
        allow_incomplete=True,
    )
    pending = score["pending_rows"]
    threshold_checks: dict[str, Any] = {}
    if any(pending.values()):
        blockers.append(f"two-person human audit incomplete: {pending}")
        status = "pending_human_audit"
    else:
        threshold_blockers, threshold_checks = evaluate_thresholds(
            score,
            read_csv(annotations_a_path),
            read_csv(annotations_b_path),
            gate,
        )
        blockers.extend(threshold_blockers)
        findings = score.get("material_findings", [])
        disposition_path = audit_dir / "agreement" / "material_findings.csv"
        dispositions = load_dispositions(disposition_path)
        unresolved = []
        for finding in findings:
            disposition = dispositions.get(finding["finding_id"], {})
            if disposition.get("status") != "resolved":
                unresolved.append(finding["finding_id"])
            elif not disposition.get("action") or not disposition.get("rationale"):
                unresolved.append(finding["finding_id"])
            elif disposition.get("action") == "rerun" and not disposition.get(
                "rerun_evidence"
            ):
                unresolved.append(finding["finding_id"])
        if gate.get("require_disposition_for_all_material_findings") and unresolved:
            blockers.append(f"unresolved material audit findings: {len(unresolved)}")
        status = "ready_to_freeze" if not blockers else "pending_audit_resolution"

    runtime_checks: list[dict[str, Any]] = []
    if run_runtime_checks:
        runtime_checks = [
            run_command(
                [
                    sys.executable,
                    "-m",
                    "unittest",
                    "discover",
                    "-s",
                    str(BENCHMARK_ROOT / "tests"),
                    "-p",
                    "test_*.py",
                ]
            ),
            run_command(
                [sys.executable, str(Path(__file__).parent / "validate_cityintent_v0.py")]
            ),
            run_command(
                [
                    sys.executable,
                    str(Path(__file__).parent / "validate_external_adapters.py"),
                    "--framework",
                    "all",
                ]
            ),
        ]
        for check in runtime_checks:
            if check["returncode"] != 0:
                blockers.append(f"runtime check failed: {' '.join(check['command'])}")
        if blockers and status == "ready_to_freeze":
            status = "pending_runtime_validation"

    return {
        "status": status if blockers else "ready_to_freeze",
        "benchmark_version": config.get("version"),
        "benchmark_status": config.get("status"),
        "audit_dir": str(audit_dir),
        "result_dir": str(result_dir),
        "blockers": blockers,
        "warnings": warnings,
        "audit_input_sha256": integrity,
        "human_audit": score,
        "threshold_checks": threshold_checks,
        "runtime_checks": runtime_checks,
        "checked_at": datetime.now(timezone.utc).isoformat(),
    }


def write_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("# CityIntent v1 Release Gate\n\n")
        f.write(f"Status: `{report['status']}`\n\n")
        f.write(f"Benchmark: `{report['benchmark_version']}` / `{report['benchmark_status']}`\n\n")
        f.write("## Blockers\n\n")
        if report["blockers"]:
            for blocker in report["blockers"]:
                f.write(f"- {blocker}\n")
        else:
            f.write("- None.\n")
        f.write("\n## Human Audit\n\n")
        pending = report["human_audit"]["pending_rows"]
        f.write(f"Pending rows: `{json.dumps(pending, sort_keys=True)}`\n\n")
        f.write(
            f"Material findings: {len(report['human_audit'].get('material_findings', []))}\n\n"
        )
        f.write("## Runtime Checks\n\n")
        if report["runtime_checks"]:
            for check in report["runtime_checks"]:
                f.write(
                    f"- `{check['returncode']}`: `{' '.join(check['command'])}`\n"
                )
        else:
            f.write("- Skipped for this gate check.\n")


def release_artifacts() -> list[Path]:
    included: list[Path] = []
    for path in sorted(BENCHMARK_ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in {".json", ".py", ".md"}:
            continue
        relative = path.relative_to(BENCHMARK_ROOT)
        if any(part in {"__pycache__", "tests", "tools"} for part in relative.parts):
            continue
        included.append(path)
    return included


def freeze_release(
    report: dict[str, Any], audit_dir: Path, result_dir: Path, report_dir: Path
) -> dict[str, Any]:
    if report["status"] != "ready_to_freeze":
        raise ValueError("release gate is not ready; refusing to freeze")
    config_path = BENCHMARK_ROOT / "benchmark_config.json"
    config = load_json(config_path)
    config["version"] = "1.0"
    config["status"] = "frozen"
    config["action_protocol"]["version"] = "1.0"
    config["release"] = {
        "release_id": "cityintent_v1",
        "frozen_at": datetime.now(timezone.utc).isoformat(),
        "human_audit": str(audit_dir.relative_to(REPO_ROOT)).replace("\\", "/"),
        "source_result": str(result_dir.relative_to(REPO_ROOT)).replace("\\", "/"),
    }
    write_json(config_path, config)

    release_dir = REPO_ROOT / "6-city" / "releases" / "cityintent_v1"
    artifacts = {
        str(path.relative_to(REPO_ROOT)).replace("\\", "/"): normalized_sha256(path)
        for path in release_artifacts()
    }
    release_manifest = {
        "release_id": "cityintent_v1",
        "version": "1.0",
        "status": "frozen",
        "frozen_at": config["release"]["frozen_at"],
        "source_release_candidate": "1.0-rc1",
        "audit_dir": config["release"]["human_audit"],
        "result_dir": config["release"]["source_result"],
        "release_gate_report": str(
            (report_dir / "release_gate.json").relative_to(REPO_ROOT)
        ).replace("\\", "/"),
        "artifact_sha256": artifacts,
    }
    write_json(release_dir / "manifest.json", release_manifest)
    return release_manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit-dir", type=Path, default=DEFAULT_AUDIT_DIR)
    parser.add_argument("--result-dir", type=Path, default=DEFAULT_RESULT_DIR)
    parser.add_argument("--report-dir", type=Path, default=DEFAULT_REPORT_DIR)
    parser.add_argument("--skip-runtime-checks", action="store_true")
    parser.add_argument("--freeze", action="store_true")
    args = parser.parse_args()

    report = evaluate_release_gate(
        args.audit_dir,
        args.result_dir,
        run_runtime_checks=not args.skip_runtime_checks,
    )
    write_json(args.report_dir / "release_gate.json", report)
    write_report(args.report_dir / "release_gate.md", report)
    if args.freeze:
        freeze_release(report, args.audit_dir, args.result_dir, args.report_dir)
        print("CityIntent v1 frozen.")
        return 0
    print(f"CityIntent v1 release gate: {report['status']}")
    for blocker in report["blockers"]:
        print(f"BLOCKER: {blocker}")
    return 0 if report["status"] == "ready_to_freeze" else 2


if __name__ == "__main__":
    raise SystemExit(main())
