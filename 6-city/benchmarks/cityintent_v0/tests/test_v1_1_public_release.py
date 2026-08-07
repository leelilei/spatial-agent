import importlib.util
import subprocess
import sys
import tarfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "v1_1" / "build_public_release.py"
SPEC = importlib.util.spec_from_file_location("cityintent_v1_1_build_public_release", MODULE_PATH)
assert SPEC and SPEC.loader
release = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = release
SPEC.loader.exec_module(release)


def test_public_archive_excludes_private_assets(tmp_path):
    archive_path = release.build_archive(tmp_path / "public.tar.gz")
    with tarfile.open(archive_path, "r:gz") as archive:
        names = archive.getnames()
        assert not any("private_test" in name or "worlds/private" in name or "/internal/" in name for name in names)
        assert any(name.endswith("submission/score_submission.py") for name in names)
        assert any(name.endswith("manifests/scenarios_manifest.json") for name in names)


def test_public_archive_regenerates_and_validates_from_clean_extract(tmp_path):
    archive_path = release.build_archive(tmp_path / "public.tar.gz")
    extract_root = tmp_path / "extract"
    extract_root.mkdir()
    with tarfile.open(archive_path, "r:gz") as archive:
        archive.extractall(extract_root, filter="data")
    package = next(extract_root.iterdir())
    subprocess.run([sys.executable, "generate_worlds.py", "--public-only"], cwd=package, check=True, capture_output=True, text=True)
    subprocess.run([sys.executable, "generate_scenarios.py", "--public-only"], cwd=package, check=True, capture_output=True, text=True)
    completed = subprocess.run(
        [sys.executable, "tools/validate_cityintent_v0.py", "--benchmark-config", "benchmark_config.json"],
        cwd=package,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "validation passed" in completed.stdout
