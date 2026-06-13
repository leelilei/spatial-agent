"use strict";

// ---------- 小工具 ----------
const $ = (sel, el = document) => el.querySelector(sel);
const el = (tag, props = {}, ...kids) => {
  const n = Object.assign(document.createElement(tag), props);
  for (const k of kids) n.append(k);
  return n;
};
const api = async (path, opts) => {
  const r = await fetch(path, opts);
  return r.json();
};
const esc = (s) => (s ?? "").replace(/[&<>]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));

let STATE = null;
const PRIO = { must: { tag: "✅", word: "必学" }, opt: { tag: "🔶", word: "理解即可" }, skip: { tag: "⏸️", word: "可跳过" } };

function toast(msg) {
  let t = $(".toast");
  if (!t) { t = el("div", { className: "toast" }); document.body.append(t); }
  t.textContent = msg; t.classList.add("show");
  clearTimeout(t._timer); t._timer = setTimeout(() => t.classList.remove("show"), 2600);
}

// ---------- Pyodide（浏览器内 Python，懒加载）----------
let _pyPromise = null;
async function getPy() {
  if (!_pyPromise) {
    toast("首次加载 Python 运行时，请稍候…");
    _pyPromise = loadPyodide();
  }
  return _pyPromise;
}
async function runCaptured(code) {
  const py = await getPy();
  py.runPython("import sys, io\n_b = io.StringIO()\n_old = sys.stdout\nsys.stdout = _b");
  let err = null;
  try { await py.runPythonAsync(code); }
  catch (e) { err = String(e.message || e).split("\n").slice(-3).join("\n"); }
  const out = py.runPython("sys.stdout = _old\n_b.getvalue()");
  return { out, err };
}

// ---------- 渲染：总览 ----------
function renderHome() {
  const cur = (STATE.lectures || []).find((l) => l.id === STATE.current);
  const card = $("#current-card");
  card.innerHTML = "";
  card.append(
    el("div", { className: "label", textContent: "👉 下一步" }),
    el("div", { className: "big", textContent: cur ? `Lec ${cur.num}：${cur.title}` : "🎉 阶段 1 全部学完！" })
  );
  if (cur) {
    const go = el("button", { className: "btn", textContent: "去学这一课" });
    go.onclick = () => { switchTab("course"); setTimeout(() => $(`#row-${cur.id}`)?.scrollIntoView({ behavior: "smooth", block: "center" }), 50); };
    card.append(el("div", { className: "row", style: "margin-top:12px" }, go));
  }

  const wrap = $("#stages"); wrap.innerHTML = "";
  for (const [k, s] of Object.entries(STATE.stages || {})) {
    const total = s.total || 0, done = s.learned || 0;
    const pct = total ? Math.round((done / total) * 100) : 0;
    const locked = !s.active;
    wrap.append(el("div", { className: "stage" + (locked ? " locked" : "") },
      el("div", { className: "name", textContent: `${k}. ${s.name}` }),
      el("div", { className: "bar" }, el("span", { style: `width:${pct}%` })),
      el("div", { className: "pct", textContent: locked && !total ? "未开始" : `${done}/${total}` })
    ));
  }

  const vc = STATE.vibecoding || {};
  $("#vibecoding").innerHTML = `<div class="label">🧩 ${esc(vc.name || "")}</div>
    <div style="margin-top:6px;font-size:13px">${esc(vc.rule || "")}</div>`;
}

// ---------- 渲染：课程清单 ----------
function renderCourse() {
  const list = $("#lecture-list"); list.innerHTML = "";
  for (const lec of STATE.lectures || []) {
    const p = PRIO[lec.priority] || PRIO.opt;
    const stateCls = lec.learned ? "learned" : lec.watched ? "watched" : "new";
    const stateTxt = lec.learned ? "✅ 学会" : lec.watched ? "👁️ 看过" : "未开始";

    const files = el("div", { className: "files" });
    if (lec.hasNotes) files.append(el("a", { href: `/materials/lectures/${lec.id}_notes.pdf`, target: "_blank", textContent: "讲义" }));
    if (lec.hasCode) files.append(el("a", { href: `/materials/lectures/${lec.id}_code.py`, target: "_blank", textContent: "代码" }));

    const checkBtn = el("button", { className: "btn-sm", textContent: lec.learned ? "复习检查点" : "检查点" });
    checkBtn.onclick = () => openCheckpoint(lec.id);

    const watchBtn = el("button", { className: "btn-sm", textContent: lec.watched ? "已看过" : "标看过" });
    watchBtn.onclick = async () => {
      STATE = await api("/api/progress", { method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ lecture: lec.id, watched: !lec.watched }) });
      renderAll();
    };

    const row = el("div", { className: `lec ${stateCls}`, id: `row-${lec.id}` },
      el("div", { className: "tag", title: p.word, textContent: p.tag }),
      el("div", { className: "num", textContent: `Lec ${lec.num}` }),
      el("div", { className: "title", textContent: lec.title, title: "打开讲义", onclick: () => lec.hasNotes && window.open(`/materials/lectures/${lec.id}_notes.pdf`) }),
      files,
      el("span", { className: `state-pill ${stateCls}`, textContent: stateTxt }),
      watchBtn, checkBtn
    );
    list.append(row);
  }
}

// ---------- 渲染：作业 ----------
async function renderWork() {
  const area = $("#work-area"); area.innerHTML = "加载中…";
  const { assignments } = await api("/api/assignments");
  area.innerHTML = "";
  area.append(el("p", { className: "muted", textContent: "选一道题，在网页里写代码、运行、提交。提交后到 AI 终端说「点评 <题号>」即可获得点评。" }));
  if (!assignments.length) area.append(el("p", { textContent: "暂无作业。可以到终端让 AI 出一道：「给我出一道 lec02 的题」。" }));
  for (const a of assignments) {
    const open = el("button", { className: "btn ghost", textContent: "打开" });
    open.onclick = () => openAssignment(a.id);
    area.append(el("div", { className: "card" },
      el("div", { className: "row", style: "justify-content:space-between" },
        el("div", {}, el("strong", { textContent: a.title }), el("div", { className: "muted", textContent: `${a.id} · 来源:${a.source}` })),
        open)));
  }
}

// ---------- 渲染：习题集（VSCode + 真实 Python）----------
async function renderPsets() {
  const list = $("#pset-list"); list.innerHTML = "加载中…";
  const { problemsets } = await api("/api/problemsets");
  list.innerHTML = "";
  for (const ps of problemsets) {
    const card = el("div", { className: "card" });
    card.append(el("div", { className: "row", style: "justify-content:space-between" },
      el("div", {}, el("strong", { textContent: ps.title }),
        el("div", { className: "muted", textContent: ps.topic + (ps.graded ? "" : " · 不计分") })),
      el("span", { className: "state-pill " + (ps.prepared ? "watched" : "new"),
        textContent: ps.prepared ? "已在工作区" : "未解压" })));

    const out = el("div", { className: "output" });
    const row = el("div", { className: "row", style: "margin-top:10px" });

    if (ps.hasPdf) row.append(el("a", { className: "btn-sm", href: `/materials/problem-sets/${ps.id}.pdf`, target: "_blank", textContent: "📄 看题目" }));

    if (ps.hasZip) {
      const prep = el("button", { className: "btn-sm", textContent: ps.prepared ? "已解压 ✓" : "解压到工作区" });
      prep.onclick = async () => {
        prep.textContent = "解压中…";
        const r = await api("/api/ps/prepare", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ id: ps.id }) });
        if (!r.ok) return toast(r.error || "解压失败");
        toast("已解压到工作区"); renderPsets();
      };
      row.append(prep);
    }

    if (ps.prepared) {
      const openBtn = el("button", { className: "btn-sm", textContent: "🧑‍💻 用 VSCode 打开" });
      openBtn.onclick = async () => {
        const r = await api("/api/ps/open", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ id: ps.id }) });
        if (r.ok) {
          toast(r.note || (r.via === "finder" ? "已在访达打开" : "已在 VSCode 打开"));
        } else {
          out.classList.add("show");
          out.textContent = (r.error || "打开失败") + (r.path ? "\n手动打开此路径：\n" + r.path : "");
        }
      };
      row.append(openBtn);

      const testBtn = el("button", { className: "btn-sm", textContent: "▶ 跑官方测试" });
      testBtn.onclick = async () => {
        testBtn.textContent = "运行中…"; out.classList.add("show"); out.textContent = "正在用真实 Python 运行测试…";
        const r = await api("/api/ps/test", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ id: ps.id }) });
        testBtn.textContent = "▶ 跑官方测试";
        out.textContent = r.ok ? `[${r.tester}]\n` + (r.output || "(无输出)") : "⚠ " + (r.error || "失败");
      };
      row.append(testBtn);

      row.append(el("span", { className: "muted", style: "margin-left:4px",
        textContent: ps.tester ? `测试脚本：${ps.tester}` : "（无自带测试，照 PDF 做）" }));
    }

    card.append(row, out);
    if (ps.prepared) {
      const hint = el("div", { className: "muted", style: "margin-top:8px",
        textContent: `做完后到 AI 终端说「点评 ${ps.id}」，我会读 workspace/${ps.id}/ 里你的代码。` });
      card.append(hint);
    }
    list.append(card);
  }
}

// ---------- 弹层 ----------
function showModal(node) { const m = $("#modal"); $("#modal-content").innerHTML = ""; $("#modal-content").append(node); m.classList.remove("hidden"); }
function closeModal() { $("#modal").classList.add("hidden"); }

// 做作业
async function openAssignment(id) {
  const a = await api(`/api/assignment?id=${id}`);
  if (a.error) return toast("题目读取失败");
  const box = el("div");
  box.append(el("h3", { textContent: a.title }));
  box.append(el("div", { style: "white-space:pre-wrap;margin:8px 0", innerHTML: esc(a.description) }));
  const ta = el("textarea", { value: a.starter_code || "", spellcheck: false, style: "min-height:160px" });
  box.append(ta);
  const out = el("div", { className: "output" });
  const verdict = el("div", { className: "verdict" });

  const runBtn = el("button", { className: "btn ghost", textContent: "▶ 运行测试" });
  const submitBtn = el("button", { className: "btn", textContent: "提交" });
  let lastResult = null;

  runBtn.onclick = async () => {
    runBtn.disabled = true; runBtn.textContent = "运行中…";
    const harness = buildTestHarness(ta.value, a.tests || []);
    const { out: o, err } = await runCaptured(harness);
    runBtn.disabled = false; runBtn.textContent = "▶ 运行测试";
    out.classList.add("show");
    if (err) { out.textContent = "出错了：\n" + err; verdict.textContent = ""; return; }
    const m = o.match(/@@RESULT@@(.*)/s);
    let rows = []; try { rows = JSON.parse(m[1]); } catch (e) {}
    let pass = 0;
    out.textContent = rows.map(([call, got, exp, ok]) => `${ok ? "✅" : "❌"} ${call} → ${got}  (期望 ${exp})`).join("\n");
    pass = rows.filter((r) => r[3]).length;
    lastResult = { pass, total: rows.length };
    verdict.className = "verdict " + (pass === rows.length ? "pass" : "fail");
    verdict.textContent = `通过 ${pass}/${rows.length}`;
  };
  submitBtn.onclick = async () => {
    const r = await api("/api/submit", { method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ id, kind: "assignment", code: ta.value, test_result: lastResult }) });
    toast(r.hint || "已提交");
    box.append(reviewBlock(id));
  };
  box.append(el("div", { className: "row", style: "margin-top:10px" }, runBtn, submitBtn), out, verdict);
  showModal(box);
}

// 检查点（确认学完一课）
async function openCheckpoint(lecId) {
  const cp = await api(`/api/checkpoint?id=${lecId}`);
  if (cp.error) {
    const box = el("div");
    box.append(el("h3", { textContent: `${lecId} 检查点` }),
      el("p", { textContent: "这节课还没有现成检查点。到 AI 终端说「给 " + lecId + " 出一个检查点」即可生成。" }));
    return showModal(box);
  }
  const box = el("div");
  box.append(el("h3", { textContent: cp.title }), el("p", { className: "muted", textContent: cp.intro || "" }));
  const itemEls = [];
  (cp.items || []).forEach((it, i) => {
    const q = el("div", { className: "q" });
    q.append(el("div", { className: "prompt", textContent: `${i + 1}. ${it.prompt}` }));
    if (it.type === "code") {
      const ta = el("textarea", { placeholder: "在这里写代码…", spellcheck: false });
      const out = el("div", { className: "output" });
      const v = el("div", { className: "verdict" });
      const run = el("button", { className: "btn-sm", textContent: "▶ 运行" });
      run.onclick = async () => {
        const { out: o, err } = await runCaptured(ta.value);
        out.classList.add("show");
        if (err) { out.textContent = err; v.textContent = ""; q._passed = false; return; }
        out.textContent = o || "(无输出)";
        const ok = o.trim() === String(it.expected_stdout).trim();
        v.className = "verdict " + (ok ? "pass" : "fail");
        v.textContent = ok ? "✅ 正确" : "❌ 还不对，再试试";
        q._passed = ok;
      };
      q.append(el("div", { className: "row" }, run), out, v);
      q._get = () => ({ type: "code", prompt: it.prompt, code: ta.value, passed: !!q._passed });
    } else {
      const ta = el("textarea", { placeholder: "用自己的话写…", spellcheck: false, style: "min-height:60px" });
      q.append(ta);
      q._get = () => ({ type: "concept", prompt: it.prompt, answer: ta.value });
      q._passed = true; // 理解题不自动判，交给 AI
    }
    itemEls.push(q); box.append(q);
  });

  const submit = el("button", { className: "btn", textContent: "提交检查点" });
  submit.onclick = async () => {
    const answers = itemEls.map((q) => q._get());
    const codeItems = answers.filter((a) => a.type === "code");
    const autoPassed = codeItems.every((a) => a.passed);
    if (codeItems.some((a) => !a.code.trim())) return toast("还有代码题没做哦");
    const r = await api("/api/submit", { method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ id: lecId, kind: "checkpoint", answers, auto_passed: autoPassed }) });
    toast(autoPassed
      ? `已提交！到 AI 终端说「确认我学完 ${lecId}」`
      : `已提交，但有代码题还没通过，建议先订正~`);
    box.append(reviewBlock(lecId));
  };
  box.append(el("div", { style: "margin-top:8px" }, submit));
  showModal(box);
}

// 点评展示块（从 reviews/ 读取）
function reviewBlock(id) {
  const wrap = el("div", { className: "review" });
  wrap.append(el("h4", { textContent: "🧑‍🏫 AI 点评" }));
  const body = el("div", { textContent: "提交后，到终端让 AI 点评；完成后点下面按钮刷新。" });
  const refresh = el("button", { className: "btn-sm", textContent: "刷新点评" });
  refresh.onclick = async () => {
    const r = await api(`/api/review?id=${id}`);
    if (!r.exists) { body.textContent = "还没有点评。到终端说「点评 " + id + "」或「确认我学完 " + id + "」。"; return; }
    body.innerHTML = miniMarkdown(r.markdown);
    refreshState();
  };
  wrap.append(body, refresh);
  return wrap;
}

// 极简 markdown 渲染（够用即可）
function miniMarkdown(md) {
  return esc(md)
    .replace(/^### (.*)$/gm, "<h4>$1</h4>")
    .replace(/^## (.*)$/gm, "<h3>$1</h3>")
    .replace(/^# (.*)$/gm, "<h3>$1</h3>")
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\[\[(.+?)\]\]/g, "<em>🔗$1</em>")
    .replace(/\n/g, "<br>");
}

// 生成测试 harness（注入测试表达式，带 try 保护）
function buildTestHarness(userCode, tests) {
  let lines = [userCode, "\n__out = []"];
  for (const t of tests) {
    const call = t.call, exp = JSON.stringify(String(t.expected));
    lines.push(
      `try:\n    __g = str(${call})\nexcept Exception as __e:\n    __g = "ERROR: " + str(__e)`,
      `__out.append([${JSON.stringify(call)}, __g, ${exp}, __g == ${exp}])`
    );
  }
  lines.push('import json as __json', 'print("@@RESULT@@" + __json.dumps(__out, ensure_ascii=False))');
  return lines.join("\n");
}

// ---------- 框架 ----------
function switchTab(name) {
  document.querySelectorAll(".tab").forEach((t) => t.classList.toggle("active", t.dataset.tab === name));
  document.querySelectorAll(".tab-panel").forEach((p) => p.classList.toggle("active", p.id === `tab-${name}`));
  if (name === "work") renderWork();
  if (name === "psets") renderPsets();
}
function renderAll() { renderHome(); renderCourse(); }
async function refreshState() { STATE = await api("/api/state"); renderAll(); }

function init() {
  document.querySelectorAll(".tab").forEach((t) => (t.onclick = () => switchTab(t.dataset.tab)));
  $("#modal-close").onclick = closeModal;
  $("#modal").onclick = (e) => { if (e.target.id === "modal") closeModal(); };
  refreshState();
}
init();
