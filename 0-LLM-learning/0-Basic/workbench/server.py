#!/usr/bin/env python3
"""个人学习工作台 —— 本地小服务器（只用 Python 标准库，零依赖）。

职责（刻意保持简单）：
  1. 把前端页面 static/ 端给浏览器
  2. 把课程材料 ../MIT-6.100L/ 端出去（PDF / 代码）
  3. 读写硬盘上的学习数据 data/（进度、提交、点评…）

它本身【不含 AI】。AI 助教（Claude Code / Codex 等）通过读写 data/ 里的
文件来点评、出题 —— 详见同目录 TUTOR.md。

启动：  python3 server.py        然后浏览器打开 http://localhost:8765
"""

import json
import re
import shutil
import subprocess
import sys
import threading
import webbrowser
import zipfile
from datetime import date
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

PORT = 8770
ROOT = Path(__file__).resolve().parent          # workbench/
STATIC = ROOT / "static"
DATA = ROOT / "data"
WORKSPACE = ROOT / "workspace"                   # 习题集解压 + 做题的工作区
MATERIALS = ROOT.parent / "MIT-6.100L"          # 0-Basic/MIT-6.100L/
PSETS = MATERIALS / "problem-sets"

# 允许直接打开的材料子目录（白名单，防目录穿越）
MATERIAL_DIRS = {"lectures", "problem-sets", "finger-exercises", "recitations"}

CONTENT_TYPES = {
    ".html": "text/html; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".pdf": "application/pdf",
    ".py": "text/plain; charset=utf-8",
    ".zip": "application/zip",
}

# 写文件时用一把锁，避免并发写坏 json
_lock = threading.Lock()


# ---------- 数据读写小工具 ----------
def read_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def write_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def load_catalog():
    return read_json(DATA / "catalog.json", {"lectures": [], "stages": {}})


def load_progress():
    prog = read_json(DATA / "progress.json", None)
    if prog is None:
        prog = {"lectures": {}, "current": None}
    prog.setdefault("lectures", {})
    return prog


def lecture_state(prog, lec_id):
    return prog["lectures"].get(lec_id, {"watched": False, "learned": False})


def compute_state():
    """把 catalog + progress 合成给前端用的完整状态，阶段进度按 ✅学会 实时算。"""
    catalog = load_catalog()
    prog = load_progress()
    lectures = []
    learned_core = 0
    core_total = 0
    first_unlearned = None
    for lec in catalog["lectures"]:
        st = lecture_state(prog, lec["id"])
        merged = {**lec, **st}
        lectures.append(merged)
        if lec["priority"] != "skip":
            core_total += 1
            if st.get("learned"):
                learned_core += 1
            elif first_unlearned is None:
                first_unlearned = lec["id"]

    stages = catalog.get("stages", {})
    if "1" in stages:
        stages["1"]["learned"] = learned_core
        stages["1"]["total"] = core_total

    return {
        "stages": stages,
        "lectures": lectures,
        "current": prog.get("current") or first_unlearned,
        "vibecoding": catalog.get("vibecoding", {}),
    }


# ---------- 习题集（VSCode + 真实 Python 路径）----------
PS_ID_RE = re.compile(r"ps\d")


def ps_paths(psid):
    """定位某个习题集在工作区的目录、做题子目录、官方测试脚本。"""
    base = WORKSPACE / psid
    if not base.is_dir():
        return {"base": base, "workdir": None, "tester": None, "files": []}
    tops = [p for p in base.iterdir() if not p.name.startswith(".") and p.name != "__MACOSX"]
    pyfiles = [p for p in tops if p.suffix == ".py"]
    subdirs = [p for p in tops if p.is_dir()]
    workdir = subdirs[0] if (not pyfiles and len(subdirs) == 1) else base
    tester = None
    files = []
    for p in sorted(workdir.iterdir()):
        if p.name.startswith(".") or p.name == "__MACOSX":
            continue
        if p.is_file():
            files.append(p.name)
            if p.suffix == ".py" and ("tester" in p.name.lower() or p.name.startswith("test_")):
                tester = p.name
    return {"base": base, "workdir": workdir, "tester": tester, "files": files}


def ps_prepare(psid):
    """把 psN_code.zip 解压到 workspace/psN/（已存在则不覆盖，保住已做的代码）。"""
    base = WORKSPACE / psid
    zip_path = PSETS / f"{psid}_code.zip"
    if not zip_path.is_file():
        return {"ok": False, "error": "缺少代码包"}
    if not base.is_dir():
        base.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(zip_path) as z:
            for m in z.namelist():
                if m.startswith("__MACOSX") or "/._" in m or m.endswith(".DS_Store"):
                    continue
                z.extract(m, base)
        macosx = base / "__MACOSX"
        if macosx.exists():
            shutil.rmtree(macosx, ignore_errors=True)
    info = ps_paths(psid)
    return {"ok": True, "workdir": str(info["workdir"]), "files": info["files"], "tester": info["tester"]}


def ps_open_vscode(psid):
    """尽量在 VSCode 里打开工作目录，多重兜底：
    1) code 命令  2) macOS `open -a VSCode`（只要装了 App 就行，无需 PATH）
    3) macOS `open`（退而求其次：在访达里定位文件夹）。"""
    info = ps_paths(psid)
    if not info["workdir"]:
        return {"ok": False, "error": "请先解压到工作区"}
    target = str(info["workdir"])

    code_bin = shutil.which("code")
    if code_bin:
        try:
            subprocess.Popen([code_bin, target])
            return {"ok": True, "via": "code", "path": target}
        except Exception:  # noqa: BLE001
            pass

    if sys.platform == "darwin":
        try:
            r = subprocess.run(["open", "-a", "Visual Studio Code", target],
                               capture_output=True, text=True, timeout=10)
            if r.returncode == 0:
                return {"ok": True, "via": "open-a", "path": target}
        except Exception:  # noqa: BLE001
            pass
        try:  # 没装 VSCode，至少在访达里打开文件夹
            subprocess.Popen(["open", target])
            return {"ok": True, "via": "finder", "path": target,
                    "note": "没找到 VSCode，已在访达里打开该文件夹。"}
        except Exception:  # noqa: BLE001
            pass

    return {"ok": False, "path": target,
            "error": "无法自动打开，请手动用编辑器打开下面的路径。"}


def ps_run_tester(psid):
    info = ps_paths(psid)
    if not info["workdir"]:
        return {"ok": False, "error": "请先解压到工作区"}
    if not info["tester"]:
        return {"ok": False, "error": "这个习题集没找到官方测试脚本，按 PDF 说明自己运行即可"}
    try:
        proc = subprocess.run(
            ["python3", info["tester"]], cwd=str(info["workdir"]),
            stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=25)
        out = (proc.stdout or "") + (proc.stderr or "")
        return {"ok": True, "tester": info["tester"], "output": out[-6000:]}
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "测试超时（可能在等输入或死循环）。请在 VSCode 终端里手动运行。"}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "error": str(e)}


# ---------- HTTP 处理 ----------
class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass  # 安静一点

    # --- 回复小工具 ---
    def _send(self, code, body=b"", ctype="application/json; charset=utf-8"):
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def _json(self, obj, code=200):
        self._send(code, json.dumps(obj, ensure_ascii=False), CONTENT_TYPES[".json"])

    def _body(self):
        length = int(self.headers.get("Content-Length", 0))
        if not length:
            return {}
        try:
            return json.loads(self.rfile.read(length).decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return {}

    # --- 路由 ---
    def do_GET(self):
        url = urlparse(self.path)
        path = url.path
        query = parse_qs(url.query)

        if path in ("/", "/index.html"):
            return self._file(STATIC / "index.html")
        if path == "/api/state":
            return self._json(compute_state())
        if path == "/api/checkpoint":
            return self._get_named(DATA / "checkpoints", query, "lec01")
        if path == "/api/assignment":
            return self._get_named(DATA / "assignments", query, "auto-001")
        if path == "/api/review":
            return self._get_review(query)
        if path == "/api/assignments":
            return self._list_assignments()
        if path == "/api/problemsets":
            return self._list_problemsets()
        if path.startswith("/materials/"):
            return self._material(path)
        if path.startswith("/static/"):
            return self._file(STATIC / path[len("/static/"):])
        return self._send(404, "Not Found", "text/plain; charset=utf-8")

    def do_POST(self):
        path = urlparse(self.path).path
        body = self._body()
        if path == "/api/progress":
            return self._update_progress(body)
        if path == "/api/submit":
            return self._submit(body)
        if path == "/api/log":
            return self._log(body)
        if path in ("/api/ps/prepare", "/api/ps/open", "/api/ps/test"):
            return self._ps_action(path, body)
        return self._send(404, "Not Found", "text/plain; charset=utf-8")

    # --- 具体动作 ---
    def _file(self, p: Path):
        if not p.is_file():
            return self._send(404, "Not Found", "text/plain; charset=utf-8")
        ctype = CONTENT_TYPES.get(p.suffix, "application/octet-stream")
        self._send(200, p.read_bytes(), ctype)

    def _material(self, path):
        rel = path[len("/materials/"):]
        parts = rel.split("/")
        if len(parts) != 2 or parts[0] not in MATERIAL_DIRS:
            return self._send(403, "Forbidden", "text/plain; charset=utf-8")
        if not re.fullmatch(r"[\w.\-]+", parts[1]):
            return self._send(403, "Forbidden", "text/plain; charset=utf-8")
        return self._file(MATERIALS / parts[0] / parts[1])

    def _get_named(self, folder: Path, query, default_id):
        item_id = (query.get("id") or [default_id])[0]
        if not re.fullmatch(r"[\w.\-]+", item_id):
            return self._send(400, "bad id", "text/plain; charset=utf-8")
        data = read_json(folder / f"{item_id}.json", None)
        if data is None:
            return self._json({"error": "not found", "id": item_id}, 404)
        return self._json(data)

    def _get_review(self, query):
        item_id = (query.get("id") or [""])[0]
        if not re.fullmatch(r"[\w.\-]+", item_id or ""):
            return self._send(400, "bad id", "text/plain; charset=utf-8")
        p = DATA / "reviews" / f"{item_id}.review.md"
        if not p.is_file():
            return self._json({"exists": False})
        return self._json({"exists": True, "markdown": p.read_text(encoding="utf-8")})

    def _list_assignments(self):
        folder = DATA / "assignments"
        items = []
        if folder.is_dir():
            for f in sorted(folder.glob("*.json")):
                d = read_json(f, {})
                items.append({"id": d.get("id", f.stem), "title": d.get("title", f.stem),
                              "source": d.get("source", "?")})
        return self._json({"assignments": items})

    def _list_problemsets(self):
        catalog = load_catalog()
        out = []
        for ps in catalog.get("problemsets", []):
            psid = ps["id"]
            info = ps_paths(psid)
            out.append({
                **ps,
                "hasPdf": (PSETS / f"{psid}.pdf").is_file(),
                "hasZip": (PSETS / f"{psid}_code.zip").is_file(),
                "prepared": info["workdir"] is not None,
                "files": info["files"],
                "tester": info["tester"],
            })
        return self._json({"problemsets": out})

    def _ps_action(self, path, body):
        psid = body.get("id", "")
        if not PS_ID_RE.fullmatch(psid or ""):
            return self._json({"ok": False, "error": "bad id"}, 400)
        if path == "/api/ps/prepare":
            return self._json(ps_prepare(psid))
        if path == "/api/ps/open":
            return self._json(ps_open_vscode(psid))
        return self._json(ps_run_tester(psid))

    def _update_progress(self, body):
        lec_id = body.get("lecture")
        if not lec_id or not re.fullmatch(r"[\w.\-]+", lec_id):
            return self._json({"error": "bad lecture"}, 400)
        with _lock:
            prog = load_progress()
            st = prog["lectures"].setdefault(lec_id, {"watched": False, "learned": False})
            if "watched" in body:
                st["watched"] = bool(body["watched"])
            if "learned" in body:
                st["learned"] = bool(body["learned"])
                # 注：把一课标 learned 通常由 AI 确认后写入；这里也允许手动撤销
            if body.get("current"):
                prog["current"] = lec_id
            write_json(DATA / "progress.json", prog)
        return self._json(compute_state())

    def _submit(self, body):
        item_id = body.get("id", "")
        kind = body.get("kind", "assignment")   # assignment | checkpoint
        if not re.fullmatch(r"[\w.\-]+", item_id or ""):
            return self._json({"error": "bad id"}, 400)
        (DATA / "submissions").mkdir(parents=True, exist_ok=True)
        if kind == "checkpoint":
            payload = {
                "id": item_id, "kind": "checkpoint",
                "submitted_at": date.today().isoformat(),
                "answers": body.get("answers", []),
                "auto_passed": body.get("auto_passed"),
            }
            (DATA / "submissions" / f"{item_id}.checkpoint.json").write_text(
                json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        else:
            code = body.get("code", "")
            (DATA / "submissions" / f"{item_id}.py").write_text(code, encoding="utf-8")
            meta = {"id": item_id, "submitted_at": date.today().isoformat(),
                    "test_result": body.get("test_result")}
            (DATA / "submissions" / f"{item_id}.meta.json").write_text(
                json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
        return self._json({"ok": True, "id": item_id,
                           "hint": "已保存。到 Claude Code / Codex 终端说「点评 %s」即可。" % item_id})

    def _log(self, body):
        text = (body.get("text") or "").strip()
        if not text:
            return self._json({"error": "empty"}, 400)
        DATA.mkdir(parents=True, exist_ok=True)
        entry = {"date": date.today().isoformat(), "text": text}
        with _lock, (DATA / "log.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        return self._json({"ok": True})


def main():
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://localhost:{PORT}"
    print(f"📚 学习工作台已启动 → {url}")
    print("   关闭：按 Ctrl+C")
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n再见，继续加油！")
        server.shutdown()


if __name__ == "__main__":
    main()
