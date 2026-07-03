"""Build a self-contained offline UI for blinded CityIntent human annotation."""

from __future__ import annotations

import argparse
import json
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


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8-sig") as f:
        return json.load(f)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig") as f:
        return [json.loads(line) for line in f if line.strip()]


HTML_TEMPLATE = r'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>CityIntent 盲标工作台</title>
<style>
:root{color-scheme:light;--ink:#17211b;--muted:#607066;--line:#cfd8d1;--paper:#f7f9f7;--panel:#fff;--accent:#176b43;--accent2:#e4f2e9;--warn:#9a5218;--bad:#a53535}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:14px/1.48 Arial,"Microsoft YaHei",sans-serif;letter-spacing:0}
button,input,select,textarea{font:inherit}button{border:1px solid var(--line);background:#fff;color:var(--ink);border-radius:6px;padding:8px 12px;cursor:pointer}button:hover{border-color:var(--accent)}button:disabled{cursor:not-allowed;opacity:.45}.primary{background:var(--accent);border-color:var(--accent);color:#fff}.danger{color:var(--bad)}
.app{min-height:100vh;display:grid;grid-template-columns:248px minmax(0,1fr)}aside{border-right:1px solid var(--line);background:#edf2ee;position:sticky;top:0;height:100vh;overflow:auto;padding:18px 14px}.brand{font-size:18px;font-weight:700}.sub{color:var(--muted);font-size:12px;margin-top:3px}.progress{height:7px;background:#d4ddd6;border-radius:4px;overflow:hidden;margin:16px 0 6px}.bar{height:100%;background:var(--accent);width:0}.item-list{display:grid;grid-template-columns:repeat(2,1fr);gap:6px;margin-top:14px}.item{padding:8px;text-align:left}.item.active{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent)}.item.done{background:var(--accent2)}.aside-actions{display:grid;gap:8px;margin-top:18px}
main{min-width:0}.topbar{height:58px;border-bottom:1px solid var(--line);background:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 24px;position:sticky;top:0;z-index:2}.topbar strong{font-size:15px}.content{max-width:1180px;margin:0 auto;padding:22px 24px 120px}.section{margin:0 0 24px}.section h2{font-size:16px;margin:0 0 10px}.meta{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1px;background:var(--line);border:1px solid var(--line);border-radius:7px;overflow:hidden}.meta>div{background:#fff;padding:12px}.meta b{display:block;font-size:11px;color:var(--muted);margin-bottom:3px}.intention{border-left:4px solid var(--accent);background:#fff;padding:14px 16px;margin-top:12px}.conditions{display:grid;gap:7px}.condition{background:#fff;border:1px solid var(--line);border-radius:6px;padding:10px 12px}.condition code{color:var(--accent);font-weight:700}.table-wrap{overflow:auto;border:1px solid var(--line);border-radius:7px;background:#fff}table{border-collapse:collapse;width:100%;min-width:860px}th,td{border-bottom:1px solid #e6ebe7;padding:8px 9px;text-align:left;vertical-align:top}th{font-size:11px;color:var(--muted);background:#f1f4f2;position:sticky;top:0}tr:last-child td{border-bottom:0}.mono{font-family:Consolas,monospace;font-size:12px}.outcomes{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}.outcome{border:1px solid var(--line);background:#fff;border-radius:6px;padding:10px;overflow:auto}.outcome b{display:block;margin-bottom:5px}.outcome pre{white-space:pre-wrap;margin:0;font:12px/1.45 Consolas,monospace}.world details{background:#fff;border:1px solid var(--line);border-radius:6px;padding:11px}.world summary{cursor:pointer;font-weight:700}
.form{border-top:1px solid var(--line);background:#fff;position:fixed;left:248px;right:0;bottom:0;z-index:3;padding:12px 24px}.form-inner{max-width:1180px;margin:auto;display:grid;grid-template-columns:1.35fr 1.15fr 1.15fr 1fr 100px 110px minmax(140px,1fr);gap:10px;align-items:end}.field label{display:block;font-size:11px;font-weight:700;color:var(--muted);margin-bottom:4px}.field select,.field input,.field textarea{width:100%;border:1px solid var(--line);border-radius:5px;background:#fff;padding:7px 8px}.field textarea{height:38px;resize:vertical}.nav{display:flex;gap:8px;align-items:center}.status{font-size:12px;color:var(--muted)}.error{color:var(--bad)}
@media(max-width:980px){.app{grid-template-columns:1fr}aside{position:static;height:auto;border-right:0;border-bottom:1px solid var(--line)}.item-list{grid-template-columns:repeat(8,1fr)}.form{left:0;position:static}.form-inner{grid-template-columns:repeat(2,minmax(0,1fr))}.content{padding-bottom:24px}.meta{grid-template-columns:repeat(2,1fr)}}
@media(max-width:620px){.topbar{padding:0 14px}.content{padding:16px 14px}.item-list{grid-template-columns:repeat(4,1fr)}.meta,.outcomes,.form-inner{grid-template-columns:1fr}.topbar .status{display:none}}
</style>
</head>
<body>
<div class="app">
<aside>
  <div class="brand">CityIntent 盲标工作台</div>
  <div class="sub" id="annotator"></div>
  <div class="progress"><div class="bar" id="progressBar"></div></div>
  <div class="status" id="progressText"></div>
  <div class="item-list" id="itemList"></div>
  <div class="aside-actions">
    <button class="primary" id="exportBtn" disabled>导出完整 CSV</button>
    <button id="backupBtn">导出当前进度</button>
    <button class="danger" id="clearBtn">清空本地进度</button>
  </div>
  <p class="sub">只判断可见轨迹。不要查看 sealed key、框架名称或另一位标注者的结果。</p>
</aside>
<main>
  <div class="topbar"><strong id="title"></strong><div class="nav"><button id="prevBtn">上一条</button><button id="nextBtn">下一条</button></div></div>
  <div class="content">
    <section class="section"><div class="meta" id="meta"></div><div class="intention" id="intention"></div></section>
    <section class="section"><h2>成功条件</h2><div class="conditions" id="conditions"></div></section>
    <section class="section"><h2>动作轨迹</h2><div class="table-wrap"><table><thead><tr><th>步</th><th>时间</th><th>起点</th><th>动作</th><th>参数</th><th>执行路线</th><th>终点</th><th>预算</th><th>中断</th></tr></thead><tbody id="trace"></tbody></table></div></section>
    <section class="section"><h2>环境接受的结果</h2><div class="outcomes" id="outcomes"></div></section>
    <section class="section world"><h2>世界参考</h2><details><summary>查看地点、开放时间、费用和道路</summary><div id="world"></div></details></section>
  </div>
</main>
</div>
<div class="form"><div class="form-inner">
  <div class="field"><label for="completion">完成度 *</label><select id="completion"><option value="">请选择</option><option value="complete">complete</option><option value="partial">partial</option><option value="not_complete">not_complete</option><option value="uncertain">uncertain</option></select></div>
  <div class="field"><label for="feasibility">可行性 *</label><select id="feasibility"><option value="">请选择</option><option value="feasible">feasible</option><option value="infeasible">infeasible</option><option value="uncertain">uncertain</option></select></div>
  <div class="field"><label for="replan">重规划 *</label><select id="replan"><option value="">请选择</option><option value="successful">successful</option><option value="failed">failed</option><option value="not_applicable">not_applicable</option><option value="uncertain">uncertain</option></select></div>
  <div class="field"><label for="evidence">证据充分 *</label><select id="evidence"><option value="">请选择</option><option value="yes">yes</option><option value="no">no</option><option value="uncertain">uncertain</option></select></div>
  <div class="field"><label for="invalidStep">首个无效步</label><input id="invalidStep" type="number" min="1"></div>
  <div class="field"><label for="confidence">置信度 1-5 *</label><select id="confidence"><option value="">请选择</option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option></select></div>
  <div class="field"><label for="notes">备注</label><textarea id="notes" placeholder="简要说明判断依据"></textarea></div>
</div></div>
<script>
const DATA=__AUDIT_DATA__;
const ANNOTATOR=__ANNOTATOR__;
const STORAGE_KEY=`cityintent-v1-${ANNOTATOR}`;
const fields=['completion','feasibility','replan','evidence','invalidStep','confidence','notes'];
let index=0;
let answers=JSON.parse(localStorage.getItem(STORAGE_KEY)||'{}');
const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const pretty=v=>JSON.stringify(v??[],null,2);
function complete(a){return !!(a?.completion&&a?.feasibility&&a?.replan&&a?.evidence&&a?.confidence)}
function save(){localStorage.setItem(STORAGE_KEY,JSON.stringify(answers));renderSidebar()}
function actionDetail(action){return Object.entries(action||{}).filter(([k,v])=>k!=='kind'&&v!==null&&v!==''&&!(Array.isArray(v)&&!v.length)).map(([k,v])=>`${k}=${Array.isArray(v)?v.join('>'):v}`).join('; ')}
function route(step){const t=step.executed_traversals||[];return t.length?[t[0].from,...t.map(x=>x.to)].join('>'):''}
function renderSidebar(){const done=DATA.items.filter(x=>complete(answers[x.audit_id])).length;document.getElementById('progressBar').style.width=`${done/DATA.items.length*100}%`;document.getElementById('progressText').textContent=`${done} / ${DATA.items.length} 已完成`;document.getElementById('exportBtn').disabled=done!==DATA.items.length;document.getElementById('itemList').innerHTML=DATA.items.map((x,i)=>`<button class="item ${i===index?'active':''} ${complete(answers[x.audit_id])?'done':''}" data-index="${i}">${esc(x.audit_id)}</button>`).join('');document.querySelectorAll('.item').forEach(b=>b.onclick=()=>{storeForm();index=Number(b.dataset.index);render()})}
function renderWorld(){const w=DATA.world;const loc=(w.locations||[]).map(x=>`<tr><td>${esc(x.id)}</td><td>${esc((x.open||[]).join('-'))}</td><td>${esc(x.typical_cost??0)}</td><td>${esc((x.tags||[]).join(', '))}</td></tr>`).join('');const edges=(w.edges||[]).map(x=>`<tr><td>${esc(x.from)}</td><td>${esc(x.to)}</td><td>${esc(x.minutes)}</td></tr>`).join('');document.getElementById('world').innerHTML=`<div class="table-wrap" style="margin-top:10px"><table><thead><tr><th>地点</th><th>开放</th><th>费用</th><th>标签</th></tr></thead><tbody>${loc}</tbody></table></div><div class="table-wrap" style="margin-top:10px"><table><thead><tr><th>From</th><th>To</th><th>分钟</th></tr></thead><tbody>${edges}</tbody></table></div>`}
function storeForm(){const id=DATA.items[index].audit_id;answers[id]=Object.fromEntries(fields.map(f=>[f,document.getElementById(f).value]));save()}
function loadForm(){const a=answers[DATA.items[index].audit_id]||{};fields.forEach(f=>document.getElementById(f).value=a[f]||'')}
function render(){const x=DATA.items[index],s=x.scenario,p=x.primary_agent,o=x.observable_outcomes;document.getElementById('title').textContent=`${x.audit_id} · ${s.title}`;document.getElementById('meta').innerHTML=`<div><b>Episode</b>${esc(s.episode.start_time)} - ${esc(s.episode.end_time)}</div><div><b>Start</b>${esc(p.start_location)}</div><div><b>Budget</b>${esc(p.budget)}</div><div><b>Family</b>${esc(s.family)}</div>`;document.getElementById('intention').innerHTML=`<strong>Private intention</strong><br>${esc(p.private_intention)}`;document.getElementById('conditions').innerHTML=s.success_conditions.map(c=>`<div class="condition"><code>${esc(c.id)}</code> · ${esc(c.role||'')}<div class="mono">${esc(JSON.stringify(c))}</div></div>`).join('');document.getElementById('trace').innerHTML=x.action_trace.map(t=>`<tr><td>${esc(t.step)}</td><td>${esc(t.start_time)}-${esc(t.end_time)}</td><td>${esc(t.start_location)}</td><td><b>${esc(t.action.kind)}</b></td><td class="mono">${esc(actionDetail(t.action))}</td><td class="mono">${esc(route(t))}</td><td>${esc(t.end_location)}</td><td>${esc(t.budget_after)}</td><td>${esc((t.route_interruptions||[]).map(v=>v.event_id).join(', '))}</td></tr>`).join('');document.getElementById('outcomes').innerHTML=Object.entries(o).map(([k,v])=>`<div class="outcome"><b>${esc(k)}</b><pre>${esc(pretty(v))}</pre></div>`).join('');document.getElementById('prevBtn').disabled=index===0;document.getElementById('nextBtn').disabled=index===DATA.items.length-1;loadForm();renderSidebar();window.scrollTo({top:0})}
function csv(includeIncomplete){storeForm();const rows=[['audit_id','annotator_id','completion_label','feasibility_label','replan_label','evidence_sufficient','first_invalid_step','confidence','notes']];for(const item of DATA.items){const a=answers[item.audit_id]||{};if(!includeIncomplete&&!complete(a))throw new Error('仍有未完成条目');rows.push([item.audit_id,ANNOTATOR,a.completion||'',a.feasibility||'',a.replan||'',a.evidence||'',a.invalidStep||'',a.confidence||'',a.notes||''])}return rows.map(r=>r.map(v=>`"${String(v).replaceAll('"','""')}"`).join(',')).join('\r\n')+'\r\n'}
function download(content,name){const blob=new Blob(['\ufeff',content],{type:'text/csv;charset=utf-8'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000)}
fields.forEach(f=>document.getElementById(f).addEventListener('change',storeForm));document.getElementById('notes').addEventListener('input',storeForm);document.getElementById('prevBtn').onclick=()=>{storeForm();if(index>0){index--;render()}};document.getElementById('nextBtn').onclick=()=>{storeForm();if(index<DATA.items.length-1){index++;render()}};document.getElementById('exportBtn').onclick=()=>download(csv(false),`${ANNOTATOR}.csv`);document.getElementById('backupBtn').onclick=()=>download(csv(true),`${ANNOTATOR}_progress.csv`);document.getElementById('clearBtn').onclick=()=>{if(confirm('确定清空本机保存的全部标注进度？')){answers={};save();render()}};document.getElementById('annotator').textContent=`标注者：${ANNOTATOR}`;renderWorld();render();
</script>
</body>
</html>'''


def build_ui(audit_dir: Path, annotator: str, output_path: Path) -> Path:
    if annotator not in {"annotator_a", "annotator_b"}:
        raise ValueError("annotator must be annotator_a or annotator_b")
    payload = {
        "items": load_jsonl(audit_dir / "blinded" / "audit_items.jsonl"),
        "world": load_json(audit_dir / "blinded" / "world_reference.json"),
    }
    html = HTML_TEMPLATE.replace(
        "__AUDIT_DATA__", json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    ).replace("__ANNOTATOR__", json.dumps(annotator))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8", newline="\n")
    return output_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit-dir", type=Path, default=DEFAULT_AUDIT_DIR)
    parser.add_argument("--annotator", choices=["annotator_a", "annotator_b"], required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build_ui(args.audit_dir, args.annotator, args.output)
    print(f"Wrote offline annotation UI to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
