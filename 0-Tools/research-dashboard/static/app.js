let dashboardState = null;
let historyData = [];
let selectedSourceId = null;
let selectedMapNodeId = null;
let currentView = "home";
let refreshTimer = null;
let activeDetailPage = "map";

const stateUrl = "/api/state";
const refreshButton = document.querySelector("#refresh-button");
const homeView = document.querySelector("#home-view");
const projectView = document.querySelector("#project-view");
const backButton = document.querySelector("#back-button");
const projectTitle = document.querySelector("#project-title");
const projectMainline = document.querySelector("#project-mainline");
const researchQuestion = document.querySelector("#research-question");
const projectNav = document.querySelector("#project-nav");
const projectMapElement = document.querySelector("#project-map");
const projectHistory = document.querySelector("#project-history");
const overviewElement = document.querySelector("#project-overview");
const paperReadiness = document.querySelector("#paper-readiness");
const mapNodeDetail = document.querySelector("#map-node-detail");

const PROJECT_NAV_ITEMS = [
  { key: "overview", label: "概览", hash: "overview" },
  { key: "map", label: "路线图", hash: "project-map" },
  { key: "history", label: "进展", hash: "history" },
  { key: "paper", label: "论文", hash: "paper-readiness" },
  { key: "decisions", label: "决策", hash: "decisions" },
  { key: "artifacts", label: "产出", hash: "artifacts" },
];

// 决策/产出仅在有内容时出现，避免空 tab。
function availableNavItems(source) {
  const model = projectMapModel(source);
  const hasDecisions = !!(source.decisions && source.decisions.present && (source.decisions.entries || []).length);
  const hasArtifacts = collectArtifacts(model).length > 0;
  return PROJECT_NAV_ITEMS.filter((item) => {
    if (item.key === "decisions") return hasDecisions;
    if (item.key === "artifacts") return hasArtifacts;
    return true;
  });
}

activeDetailPage = detailPageFromHash();

const MAP_LANES = [
  { key: "done", label: "Done", caption: "已经形成的基础" },
  { key: "now", label: "Now", caption: "当前研究焦点" },
  { key: "next", label: "Next", caption: "下一段工作" },
  { key: "paper", label: "Paper", caption: "论文准备度" },
];

const STATUS_LABELS = {
  done: "已完成",
  current: "当前",
  next: "下一步",
  planned: "计划中",
  blocked: "受阻",
  draft: "草稿",
  ready: "就绪",
  missing: "缺失",
};

refreshButton.addEventListener("click", () => {
  loadState();
});

backButton.addEventListener("click", () => {
  currentView = "home";
  selectedMapNodeId = null;
  activeDetailPage = "overview";
  window.history.replaceState(window.history.state, "", window.location.pathname);
  render();
});

const homeNav = document.querySelector("#home-nav");
if (homeNav) {
  homeNav.addEventListener("click", () => {
    currentView = "home";
    selectedSourceId = null;
    selectedMapNodeId = null;
    window.history.replaceState(window.history.state, "", window.location.pathname);
    render();
  });
}

function renderSidebar() {
  const switcher = document.querySelector("#project-switcher");
  if (switcher) {
    switcher.innerHTML = (dashboardState?.sources || []).map(sidebarRow).join("");
    switcher.querySelectorAll("[data-source-id]").forEach((row) => {
      row.addEventListener("click", () => {
        selectedSourceId = row.dataset.sourceId;
        selectedMapNodeId = null;
        currentView = "project";
        activeDetailPage = "overview";
        replaceDetailHash("overview");
        render();
        window.requestAnimationFrame(() => window.scrollTo({ top: 0, behavior: "smooth" }));
      });
    });
  }
  if (homeNav) homeNav.classList.toggle("active", currentView !== "project");
}

function sidebarRow(source) {
  const active = currentView === "project" && source.id === selectedSourceId ? " active" : "";
  const pct = source.progress && source.progress.total ? percent(source.progress.fraction) : "—";
  const level = (source.compliance || {}).achievedLevel || "";
  const meta = [pct, level].filter(Boolean).join(" · ");
  const dotColor = source.error ? "var(--muted)" : safeColor(source.accent);
  return `
    <button type="button" class="nav-row project${active}" data-source-id="${escapeAttr(source.id)}">
      <span class="nav-row-dot" style="background:${dotColor}"></span>
      <span class="nav-row-name">${escapeHtml(source.name)}</span>
      <span class="nav-row-meta">${escapeHtml(meta)}</span>
    </button>
  `;
}

window.addEventListener("popstate", handleDetailLocationChange);
window.addEventListener("hashchange", handleDetailLocationChange);

loadState();
refreshTimer = window.setInterval(loadState, 60000);

async function loadState() {
  setRefreshState(true);
  try {
    const [stateRes, historyRes] = await Promise.all([
      fetch(stateUrl, { cache: "no-store" }),
      fetch("/api/history", { cache: "no-store" }).catch(() => null)
    ]);

    if (!stateRes.ok) {
      throw new Error(`HTTP ${stateRes.status}`);
    }
    dashboardState = await stateRes.json();

    if (historyRes && historyRes.ok) {
      historyData = await historyRes.json();
    } else {
      historyData = [];
    }

    if (selectedSourceId && !dashboardState.sources.some((source) => source.id === selectedSourceId)) {
      selectedSourceId = null;
      selectedMapNodeId = null;
      currentView = "home";
    }

    render();
  } catch (error) {
    renderError(error);
  } finally {
    setRefreshState(false);
  }
}

function render() {
  const selected = selectedSource();
  renderLastUpdated();
  renderSidebar();
  renderSummary();
  renderSources();

  const shouldShowProject = currentView === "project" && selected;
  homeView.hidden = shouldShowProject;
  projectView.hidden = !shouldShowProject;

  const topbar = document.querySelector(".topbar");
  if (topbar) {
    topbar.style.display = shouldShowProject ? "none" : "flex";
  }

  if (shouldShowProject) {
    renderProject(selected);
    return;
  }

  renderTrendChart();

  renderProjectNav(null);
}

function renderProject(source) {
  const model = projectMapModel(source);
  activeDetailPage = normalizeDetailPage(activeDetailPage);
  // 若当前页在本项目不可用（如无决策/产出），回退到概览。
  if (!availableNavItems(source).some((item) => item.key === activeDetailPage)) {
    activeDetailPage = "overview";
  }
  projectView.dataset.activePage = activeDetailPage;
  if (selectedMapNodeId && !findMapNode(model, selectedMapNodeId)) {
    selectedMapNodeId = null;
  }

  projectView.dataset.activePage = activeDetailPage;
  projectTitle.textContent = model.title || `${source.name} Research Map`;
  projectMainline.textContent = model.currentFocus || source.currentMainline || "暂无当前焦点";
  if (model.researchQuestion) {
    researchQuestion.textContent = `Research Question: ${model.researchQuestion}`;
    researchQuestion.hidden = false;
  } else {
    researchQuestion.textContent = "";
    researchQuestion.hidden = true;
  }

  updateProjectPagesVisibility();
  renderProjectNav(source);
  renderOverview(source, model);
  renderProjectMap(source, model);
  renderMapNodeDetail(source, model);
  renderHistory(source, model);
  renderPaperReadiness(model);
  renderDecisions(source);
  renderArtifacts(source, model);
}

function renderLastUpdated() {
  const label = dashboardState?.generatedAt
    ? new Date(dashboardState.generatedAt).toLocaleString()
    : "未知";
  document.querySelector("#last-updated").textContent = `更新 ${label}`;
}

function renderSummary() {
  const totals = dashboardState?.totals;
  const summary = document.querySelector("#summary");
  if (!totals) {
    summary.innerHTML = "";
    return;
  }

  const delta = Number(totals.weeklyCompletedDelta) || 0;
  const deltaCaption = delta > 0 ? `本周净完成 +${delta}` : delta < 0 ? `本周净变化 ${delta}` : "本周暂无净完成";
  summary.innerHTML = [
    metric("活跃 / 停滞", `${totals.activeCount ?? totals.readableCount} / ${totals.staleCount ?? 0}`, "≤30天有更新 / 超30天"),
    metric("待办任务", totals.openTasks, deltaCaption),
    metric("P0 / P1", `${totals.p0}/${totals.p1}`, "紧急 / 下一步"),
    metric("总进度", percent(totals.progressFraction), `${totals.progressCompleted}/${totals.progressTotal} 个任务`),
  ].join("");
}

function renderSources() {
  const grid = document.querySelector("#source-grid");
  grid.innerHTML = (dashboardState?.sources || []).map(sourceCard).join("");
  grid.querySelectorAll("[data-source-id]").forEach((card) => {
    card.addEventListener("click", () => {
      selectedSourceId = card.dataset.sourceId;
      selectedMapNodeId = null;
      currentView = "project";
      activeDetailPage = "overview";
      replaceDetailHash("overview");
      render();
      window.requestAnimationFrame(() => window.scrollTo({ top: 0, behavior: "smooth" }));
    });
  });
}

function renderDonutChart(fraction, color, size = 56, strokeWidth = 6) {
  const radius = (size - strokeWidth) / 2;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - fraction * circumference;
  return `
    <svg class="donut-chart" width="${size}" height="${size}" viewBox="0 0 ${size} ${size}">
      <circle cx="${size/2}" cy="${size/2}" r="${radius}" fill="none" stroke="var(--soft)" stroke-width="${strokeWidth}" />
      <circle cx="${size/2}" cy="${size/2}" r="${radius}" fill="none" stroke="${escapeAttr(color)}" stroke-width="${strokeWidth}"
        stroke-dasharray="${circumference}" stroke-dashoffset="${offset}" stroke-linecap="round"
        transform="rotate(-90 ${size/2} ${size/2})" />
      <text x="50%" y="50%" class="donut-label" dominant-baseline="central" text-anchor="middle">
        ${percent(fraction)}
      </text>
    </svg>
  `;
}

function sourceCard(source) {
  const active = currentView === "project" && source.id === selectedSourceId ? " active" : "";
  const error = source.error ? " error" : "";
  const progress = source.progress || {};
  const modeLabel = progress.mode === "checkbox" ? "按任务" : progress.mode === "phase" ? "按阶段" : "";
  const progressText = progress.total
    ? `${progress.completed}/${progress.total}${modeLabel ? " · " + modeLabel : ""}`
    : "暂无进度";
  const status = source.error
    ? `<span class="status-pill error">异常</span>`
    : complianceBadge(source.compliance);
  const focus = source.currentMainline || projectMapModel(source).currentFocus || "暂无当前焦点";
  const phaseLabel = currentPhaseLabel(source);
  const nextActions = (source.nextActions || []).slice(0, 2);

  const foot = source.error
    ? `<p class="error-text">${escapeHtml(source.error)}</p>`
    : (nextActions.length
        ? `<div class="card-next"><span class="card-next-label">下一步</span><ul>${nextActions.map((t) => `<li>${escapeHtml(t.title)}</li>`).join("")}</ul></div>`
        : `<p class="path">${escapeHtml(source.path)}</p>`);

  const fraction = progress.fraction || 0;
  const donutHtml = progress.total > 0
    ? renderDonutChart(fraction, safeColor(source.accent))
    : `<div style="width:56px;height:56px;border-radius:50%;border:2px dashed var(--line);display:flex;align-items:center;justify-content:center;color:var(--muted);font-size:10px;">-</div>`;

  return `
    <article class="source-card${active}${error}" data-source-id="${escapeAttr(source.id)}">
      <div class="source-heading">
        <span class="dot" style="background:${safeColor(source.accent)}"></span>
        <h3>${escapeHtml(source.name)}</h3>
        ${status}
      </div>

      <div class="card-confidence">
        ${phaseLabel ? `<span class="card-phase">${escapeHtml(phaseLabel)}</span>` : ""}
        ${stalenessBadge(source.staleness)}
      </div>

      <div class="card-body-row">
        <div class="card-stats-col">
          <div class="card-stats" style="display:flex; gap:12px; margin:0;">
            <div class="stat"><strong>${source.taskCounts.open}</strong><span>待办</span></div>
            <div class="stat"><strong>${source.priorityCounts.P0}</strong><span>P0</span></div>
            <div class="stat"><strong>${source.priorityCounts.P1}</strong><span>P1</span></div>
          </div>
          <p class="mainline" style="margin:4px 0 0 0; line-height:1.4; display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;">${escapeHtml(focus)}</p>
        </div>

        <div class="card-donut">
          ${donutHtml}
          <span style="font-size:10px; color:var(--muted); font-weight:600; white-space:nowrap;">${progressText}</span>
        </div>
      </div>

      ${foot}
    </article>
  `;
}

function currentPhaseLabel(source) {
  const phases = source.phases || [];
  const current = phases.find((p) => p.isCurrent) || phases.find((p) => p.status === "current");
  if (!current) return "";
  return current.number !== undefined && current.number !== null
    ? `Phase ${current.number} · ${current.title}`
    : String(current.title || "");
}

function stalenessBadge(staleness) {
  const s = staleness || {};
  if (s.level === "unknown" || s.days === null || s.days === undefined) {
    return `<span class="freshness-badge unknown">更新日期未知</span>`;
  }
  const text = s.days === 0 ? "今日更新" : `${s.days} 天前更新`;
  const suffix = s.level === "stale" ? " · 可能停滞" : "";
  return `<span class="freshness-badge ${escapeAttr(s.level)}">${escapeHtml(text + suffix)}</span>`;
}

function complianceBadge(compliance) {
  if (!compliance) return "";
  const level = compliance.achievedLevel || "—";
  const title = level === "—" ? "未达 L0" : `规范合规 ${level}`;
  return `<span class="compliance-badge level-${escapeAttr(String(level))}" title="${escapeAttr(title)}">${escapeHtml(level)}</span>`;
}

function renderProjectNav(source) {
  if (!source || source.error) {
    projectNav.innerHTML = "";
    return;
  }

  projectNav.innerHTML = availableNavItems(source).map((item) => projectNavLink(item)).join("");
  projectNav.querySelectorAll("[data-nav-key]").forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      const key = link.dataset.navKey;
      setActiveDetailPage(key, { updateHash: true });
    });
  });
}

function projectNavLink(item) {
  const active = item.key === activeDetailPage ? " active" : "";
  return `
    <a class="project-nav-link${active}" href="#${escapeAttr(item.hash)}" data-nav-key="${escapeAttr(item.key)}">
      ${escapeHtml(item.label)}
    </a>
  `;
}

function renderOverview(source, model) {
  if (!overviewElement) return;
  if (source.error) {
    overviewElement.innerHTML = emptyState(source.error);
    return;
  }

  const progress = source.progress || {};
  const phaseLabel = currentPhaseLabel(source) || "未标注当前阶段";
  const progressLine = progress.total
    ? `${progress.completed}/${progress.total} 任务${progress.mode === "checkbox" ? "（按任务）" : ""}`
    : "暂无进度";

  const focusNode = defaultMapNode(model);
  let doNext = (focusNode?.nextActions || []).filter(Boolean);
  if (!doNext.length) doNext = (source.nextActions || []).map((t) => t.title).filter(Boolean);
  doNext = doNext.slice(0, 3);

  const sections = model.paper?.sections || [];
  const blockers = sections.flatMap((s) => (s.blockers || []).map((b) => ({ section: s.title, text: b })));
  const readiness = model.readinessSummary || readinessSummary(sections);

  const delta = sourceWeeklyDelta(source.id);
  const lastMilestone = (model.history || model.milestones || []).slice(-1)[0] || null;
  const upgrade = nextComplianceGap(source.compliance);
  const accent = safeColor(source.accent);

  overviewElement.innerHTML = `
    <div class="cockpit">
      <article class="cockpit-card cockpit-now">
        <p class="eyebrow">当前阶段</p>
        <h3>${escapeHtml(phaseLabel)}</h3>
        <div class="cockpit-progress">
          <div class="cockpit-bar"><span style="width:${clampedPercent(progress.fraction)}%; background:${accent}"></span></div>
          <strong>${percent(progress.fraction || 0)}</strong>
        </div>
        <p class="muted">${escapeHtml(progressLine)}</p>
        <div class="cockpit-badges">${stalenessBadge(source.staleness)}${complianceBadge(source.compliance)}</div>
      </article>

      <article class="cockpit-card cockpit-donext">
        <p class="eyebrow">此刻该做</p>
        ${doNext.length
          ? `<ol class="cockpit-donext-list">${doNext.map((t) => `<li>${escapeHtml(t)}</li>`).join("")}</ol>`
          : emptyState("当前没有明确下一步，去 todolist 补几条。")}
      </article>

      <article class="cockpit-card cockpit-blockers">
        <p class="eyebrow">卡住 / 风险</p>
        ${blockers.length
          ? `<ul class="cockpit-blocker-list">${blockers.slice(0, 4).map((b) => `<li><span class="blocker-sec">${escapeHtml(b.section)}</span>${escapeHtml(b.text)}</li>`).join("")}</ul>${blockers.length > 4 ? `<p class="muted">+${blockers.length - 4} 更多</p>` : ""}`
          : `<p class="cockpit-clear">✓ 暂无记录的阻塞</p>`}
      </article>

      <article class="cockpit-card cockpit-paper">
        <p class="eyebrow">论文准备度</p>
        ${readiness.total
          ? `<div class="cockpit-progress"><div class="cockpit-bar"><span style="width:${clampedPercent(readiness.fraction)}%; background:var(--green)"></span></div><strong>${readiness.ready}/${readiness.total}</strong></div><p class="muted">${readiness.ready} ready · ${readiness.blocked || 0} blocked · ${readiness.missing || 0} missing</p>`
          : emptyState("还没有 paper 章节清单。")}
      </article>

      <article class="cockpit-card cockpit-recent">
        <p class="eyebrow">最近动态</p>
        <p class="cockpit-delta"><strong>${delta > 0 ? "+" + delta : delta}</strong> 本周净完成</p>
        ${lastMilestone ? `<p class="muted">上次里程碑：${escapeHtml(lastMilestone.title)}${lastMilestone.date ? " (" + escapeHtml(lastMilestone.date) + ")" : ""}</p>` : ""}
      </article>

      ${upgrade ? `
      <article class="cockpit-card cockpit-upgrade">
        <p class="eyebrow">规范升级</p>
        <p>距 <strong>${escapeHtml(upgrade.code)}</strong> 还差：</p>
        <ul class="cockpit-upgrade-list">${upgrade.missing.map((m) => `<li>${escapeHtml(m)}</li>`).join("")}</ul>
      </article>` : ""}
    </div>
  `;
}

function sourceWeeklyDelta(sourceId) {
  const rows = (historyData || [])
    .map((d) => {
      const s = (d.sources || []).find((x) => x.id === sourceId);
      return s ? { date: d.date, completed: Number(s.completed) || 0 } : null;
    })
    .filter(Boolean)
    .sort((a, b) => a.date.localeCompare(b.date));
  if (rows.length < 2) return 0;
  const latest = rows[rows.length - 1];
  const target = new Date(`${latest.date}T00:00:00`);
  target.setDate(target.getDate() - 7);
  const targetKey = formatDateKey(target);
  const onOrBefore = rows.filter((r) => r.date <= targetKey);
  const baseline = onOrBefore.length ? onOrBefore[onOrBefore.length - 1] : rows[0];
  return latest.completed - baseline.completed;
}

function nextComplianceGap(compliance) {
  if (!compliance || !Array.isArray(compliance.levels)) return null;
  const next = compliance.levels.find((l) => !l.complete);
  if (!next || !next.missing || !next.missing.length) return null;
  const missing = next.missing.map((m) => (m.includes("|") ? m.split("|").join(" 或 ") : m));
  return { code: next.code, missing };
}

function normalizeRef(item) {
  if (item && typeof item === "object") {
    return {
      label: item.label || item.path || "Asset",
      path: item.path || "",
      type: item.type || (item.path ? "file" : "output"),
      status: item.status || "",
      exists: !!item.exists,
    };
  }
  return { label: String(item), path: "", type: "output", status: "", exists: false };
}

function collectArtifacts(model) {
  const buckets = [
    ...(model.mapNodes || []).flatMap((n) => n.outputs || []),
    ...(model.milestones || []).flatMap((m) => m.outputs || []),
    ...((model.paper && model.paper.sections) || []).flatMap((s) => s.assets || []),
  ];
  const seen = new Set();
  const out = [];
  buckets.forEach((raw) => {
    const ref = normalizeRef(raw);
    const key = (ref.path || ref.label).toLowerCase();
    if (!key || seen.has(key)) return;
    seen.add(key);
    out.push(ref);
  });
  return out;
}

function renderDecisions(source) {
  const el = document.querySelector("#project-decisions");
  if (!el) return;
  const entries = (source.decisions && source.decisions.entries) || [];
  if (!entries.length) {
    el.innerHTML = emptyState("还没有 docs/project/decisions.md，或其中没有 ## 决策条目。");
    return;
  }
  el.innerHTML = `
    <div class="decisions-list">
      ${entries.map((e) => `
        <article class="decision-item">
          <div class="decision-dot"></div>
          <div>
            <h3>${escapeHtml(e.title)}</h3>
            ${e.body ? `<p>${escapeHtml(e.body)}</p>` : ""}
          </div>
        </article>
      `).join("")}
    </div>
  `;
}

function renderArtifacts(source, model) {
  const el = document.querySelector("#project-artifacts");
  if (!el) return;
  const artifacts = collectArtifacts(model);
  if (!artifacts.length) {
    el.innerHTML = emptyState("暂无登记的产出物（在 project_map / roadmap 的 outputs 里声明）。");
    return;
  }
  const present = artifacts.filter((a) => a.exists);
  const missing = artifacts.filter((a) => !a.exists);
  el.innerHTML = `
    <div class="artifacts-summary">
      <span><strong>${present.length}</strong> 已存在</span>
      <span><strong>${missing.length}</strong> 待产出 / 缺失</span>
    </div>
    <ul class="artifacts-list">
      ${artifacts.map((a) => `
        <li class="artifact-item ${a.exists ? "exists" : "absent"}">
          <span class="artifact-mark">${a.exists ? "✓" : "○"}</span>
          <div>
            <span class="artifact-label">${escapeHtml(a.label)}</span>
            ${a.path ? `<code class="artifact-path">${escapeHtml(a.path)}</code>` : ""}
          </div>
          ${a.type ? `<span class="artifact-type">${escapeHtml(a.type)}</span>` : ""}
        </li>
      `).join("")}
    </ul>
  `;
}

function renderProjectMap(source, model) {
  if (source.error) {
    projectMapElement.innerHTML = emptyState(source.error);
    return;
  }

  const nodes = model.mapNodes || [];
  const warning = model.error
    ? `<p class="map-warning">${escapeHtml(model.error)} 已使用现有 todo / roadmap 生成简版地图。</p>`
    : "";

  if (!nodes.length) {
    projectMapElement.innerHTML = `${warning}${emptyState("这个项目暂时没有可视化节点。")}`;
    return;
  }

  const trackGroups = groupNodesByTrack(source, nodes);
  const timelineHtml = trackGroups.map((group, index) => trackColumn(group, index)).join("");

  // Check if we need to render the modal overlay
  let modalOverlayHtml = "";
  if (selectedMapNodeId) {
    const selectedNode = nodes.find(n => n.id === selectedMapNodeId);
    if (selectedNode) {
      const phaseText = selectedNode.phase !== undefined ? `Phase ${selectedNode.phase}` : "General";
      const outputsHtml = referenceList(selectedNode.outputs, "暂无产物。");
      const nextActionsHtml = plainList(selectedNode.nextActions, "暂无下一步动作。");
      const relations = [
        ...(selectedNode.dependsOn || []).map((item) => `Depends on: ${item}`),
        ...(selectedNode.taskRefs || []).map((item) => `Task: ${item}`)
      ];
      const relationsHtml = plainList(relations, "暂无关联。");

      modalOverlayHtml = `
        <div class="map-node-modal-overlay" id="node-modal-overlay">
          <div class="map-node-modal-card" style="--project-accent:${safeColor(source.accent)};">
            <div class="node-header-row" style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--soft); padding-bottom: 14px; margin-bottom: 10px;">
              <div style="display: flex; align-items: center; gap: 10px;">
                <span class="node-status status-${statusClass(selectedNode.status)}" style="padding: 5px 10px; font-weight: 800; border-radius: 999px;">${escapeHtml(statusLabel(selectedNode.status))}</span>
                <span style="font-size: 12px; font-weight: 800; color: var(--muted); background: var(--soft); padding: 5px 10px; border-radius: 999px;">${phaseText}</span>
                <span style="font-size: 12px; font-weight: 800; color: var(--muted); background: var(--surface-2); border: 1px solid var(--line); padding: 5px 10px; border-radius: 999px;">${escapeHtml(laneLabel(selectedNode.lane))}</span>
              </div>
              <button class="close-expansion-btn" type="button" style="cursor: pointer; font-size: 12px; font-weight: 800; color: var(--muted); padding: 6px 12px; border-radius: 999px; border: 1px solid var(--line); background: var(--surface-2);" title="关闭">关闭 ✕</button>
            </div>
            
            <div class="node-modal-body" style="display: flex; flex-direction: column; gap: 14px;">
              <h2 style="font-size: 24px; color: var(--ink); margin: 0; font-family: Georgia, serif;">${escapeHtml(selectedNode.title)}</h2>
              <p style="font-size: 15px; color: var(--muted); line-height: 1.6; margin: 0; white-space: pre-wrap;">${escapeHtml(selectedNode.summary || "暂无节点摘要。")}</p>
              
              <div class="node-expanded-details-grid" style="border-top: 1px solid var(--soft); padding-top: 20px; margin-top: 10px;">
                <div>
                  <h4 style="margin: 0 0 10px 0; font-size: 14px; color: var(--blue); font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; border-bottom: 2px solid color-mix(in srgb, var(--blue) 20%, transparent); padding-bottom: 6px;">产物 / 证据</h4>
                  ${outputsHtml}
                </div>
                <div>
                  <h4 style="margin: 0 0 10px 0; font-size: 14px; color: var(--amber); font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; border-bottom: 2px solid color-mix(in srgb, var(--amber) 20%, transparent); padding-bottom: 6px;">下一步动作</h4>
                  ${nextActionsHtml}
                </div>
                <div>
                  <h4 style="margin: 0 0 10px 0; font-size: 14px; color: var(--muted); font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; border-bottom: 2px solid color-mix(in srgb, var(--line) 50%, transparent); padding-bottom: 6px;">关联与依赖</h4>
                  ${relationsHtml}
                </div>
              </div>
            </div>
          </div>
        </div>
      `;
    }
  }

  projectMapElement.innerHTML = `
    ${warning}
    <div class="map-canvas track-canvas" style="--project-accent:${safeColor(source.accent)}">
      <div class="track-timeline" aria-label="研究阶段流程图">
        ${timelineHtml}
      </div>
    </div>
    ${modalOverlayHtml}
  `;

  projectMapElement.querySelectorAll("[data-node-id]").forEach((card) => {
    const nodeId = card.dataset.nodeId;
    card.addEventListener("click", () => {
      selectedMapNodeId = nodeId;
      render();
    });
  });

  // Attach event listener to close the modal if open
  if (selectedMapNodeId) {
    const overlay = document.getElementById("node-modal-overlay");
    if (overlay) {
      overlay.addEventListener("click", (e) => {
        if (e.target === overlay) {
          selectedMapNodeId = null;
          render();
        }
      });
      const closeBtn = overlay.querySelector(".close-expansion-btn");
      if (closeBtn) {
        closeBtn.addEventListener("click", () => {
          selectedMapNodeId = null;
          render();
        });
      }
    }
  }
}

window.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && selectedMapNodeId) {
    selectedMapNodeId = null;
    render();
  }
});

function nodePhaseValue(node) {
  return node.phase !== undefined && node.phase !== null ? node.phase : 9999;
}

function groupNodesByTrack(source, nodes) {
  const byPhase = (a, b) => nodePhaseValue(a) - nodePhaseValue(b);
  const tracks = (source.roadmap?.tracks || [])
    .slice()
    .sort((a, b) => (a.order ?? 999) - (b.order ?? 999));

  // No structured roadmap tracks: keep a single track so the view still works.
  if (!tracks.length) {
    return [{ id: "all", name: "研究阶段", accent: source.accent, nodes: [...nodes].sort(byPhase) }];
  }

  const phaseToTrack = {};
  (source.roadmap?.phases || []).forEach((phase) => {
    if (phase.number !== undefined && phase.number !== null) {
      phaseToTrack[phase.number] = phase.track;
    }
  });

  const groups = tracks.map((track) => ({ ...track, nodes: [] }));
  const byId = Object.fromEntries(groups.map((group) => [group.id, group]));
  const untracked = [];
  nodes.forEach((node) => {
    const trackId = phaseToTrack[node.phase];
    if (trackId && byId[trackId]) {
      byId[trackId].nodes.push(node);
    } else {
      untracked.push(node);
    }
  });
  if (untracked.length) {
    groups.push({ id: "untracked", name: "其他", accent: source.accent, nodes: untracked });
  }
  groups.forEach((group) => group.nodes.sort(byPhase));
  return groups.filter((group) => group.nodes.length);
}

function trackStatus(nodes) {
  if (nodes.some((node) => node.status === "current") || nodes.some((node) => node.lane === "now")) {
    return "current";
  }
  if (nodes.length && nodes.every((node) => node.status === "done")) {
    return "done";
  }
  if (nodes.some((node) => node.status === "next")) {
    return "next";
  }
  return "planned";
}

function trackColumn(group, index) {
  const status = trackStatus(group.nodes);
  const subnodes = group.nodes.map((node) => phaseSubnode(node)).join("");
  return `
    <article class="track-column status-${statusClass(status)}">
      <header class="track-header">
        <span class="eyebrow">Track ${index + 1}</span>
        <h3>${escapeHtml(group.name)}</h3>
      </header>
      <div class="track-mainline-row" aria-hidden="true">
        <span class="track-dot">${index + 1}</span>
      </div>
      <div class="track-phases">
        ${subnodes}
      </div>
    </article>
  `;
}

function phaseSubnode(node) {
  const statusCls = statusClass(node.status);
  const activeClass = node.id === selectedMapNodeId ? " active" : "";
  const phaseLabel = node.phase !== undefined && node.phase !== null ? `Phase ${node.phase}` : "General";
  return `
    <button type="button" class="phase-subnode status-${statusCls}${activeClass}" data-node-id="${escapeAttr(node.id)}">
      <span class="phase-subnode-top">
        <span class="phase-badge">${escapeHtml(phaseLabel)}</span>
        <span class="phase-status">${escapeHtml(statusLabel(node.status))}</span>
      </span>
      <strong>${escapeHtml(node.title)}</strong>
    </button>
  `;
}

function mapNodeButton(node) {
  const activeClass = node.id === selectedMapNodeId ? " active" : "";
  const phaseText = node.phase !== undefined ? `Phase ${node.phase}` : "";
  const statusLabelText = statusLabel(node.status);
  const statusCls = statusClass(node.status);

  // Render count badges for outputs and nextActions if they exist
  const outputsBadge = node.outputs && node.outputs.length
    ? `<span class="compact-badge">${node.outputs.length} 产物</span>`
    : '';
  const actionsBadge = node.nextActions && node.nextActions.length
    ? `<span class="compact-badge">${node.nextActions.length} 待办</span>`
    : '';

  return `
    <div
      class="map-node status-${statusCls}${activeClass}"
      data-node-id="${escapeAttr(node.id)}"
      style="display: flex; flex-direction: column; gap: 8px;"
    >
      <div class="node-compact-header">
        <span class="node-status">${escapeHtml(statusLabelText)}</span>
        ${phaseText ? `<span class="node-phase-badge">${escapeHtml(phaseText)}</span>` : ""}
      </div>
      <strong>${escapeHtml(node.title)}</strong>
      <p class="node-compact-summary">${escapeHtml(node.summary || "暂无节点摘要。")}</p>
      <div class="node-meta-row">
        ${outputsBadge}
        ${actionsBadge}
      </div>
    </div>
  `;
}

function updateMapNodeActiveStates() {
  projectMapElement.querySelectorAll("[data-node-id]").forEach((button) => {
    const isActive = button.dataset.nodeId === selectedMapNodeId;
    button.classList.toggle("active", isActive);
    button.setAttribute("aria-pressed", isActive ? "true" : "false");
  });
}

function renderMapNodeDetail(source, model) {
  // No-op. Details are shown inline in expanded cards.
}

function renderHistory(source, model) {
  const heatmapHtml = renderHistoryHeatmap(source);
  const history = model.history || model.milestones || [];
  if (!history.length) {
    projectHistory.innerHTML = `${heatmapHtml}${emptyState("还没有记录历史 milestone。")}`;
    return;
  }

  projectHistory.innerHTML = `
    ${heatmapHtml}
    <div class="history-list">
      ${history.map((item) => `
        <article class="history-item">
          <div class="history-dot"></div>
          <div>
            <div class="history-heading">
              <h3>${escapeHtml(item.title)}</h3>
              <span>${escapeHtml(item.date || statusLabel(item.status))}</span>
            </div>
            <p>${escapeHtml(item.summary || "暂无摘要。")}</p>
            ${referenceList(item.outputs, "暂无产物。")}
          </div>
        </article>
      `).join("")}
    </div>
  `;
}

function renderHistoryHeatmap(source) {
  const accent = safeColor(source.accent);
  const rows = historyData
    .filter((entry) => (entry.sources || []).some((item) => item.id === source.id))
    .map((entry) => {
      const matched = (entry.sources || []).find((item) => item.id === source.id) || {};
      return {
        date: entry.date,
        completed: Number(matched.completed) || 0,
        total: Number(matched.total) || 0,
        fraction: Number(matched.fraction) || 0,
        openTasks: Number(matched.openTasks) || 0,
      };
    })
    .filter((entry) => entry.date)
    .sort((a, b) => a.date.localeCompare(b.date));

  const today = new Date();
  today.setHours(0, 0, 0, 0);
  const endDate = new Date(today);
  const startDate = new Date(endDate);
  startDate.setDate(startDate.getDate() - (7 * 53 - 1));
  const gridStart = new Date(startDate);
  gridStart.setDate(gridStart.getDate() - gridStart.getDay());

  const seriesByDate = new Map(rows.map((item, index) => {
    const prev = index > 0 ? rows[index - 1] : null;
    return [item.date, {
      ...item,
      delta: Math.max(0, item.completed - (prev ? prev.completed : item.completed)),
    }];
  }));

  const weekDays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
  const dayCells = [];
  const cursor = new Date(gridStart);

  while (cursor <= endDate) {
    const iso = formatDateKey(cursor);
    const entry = seriesByDate.get(iso) || null;
    const delta = entry ? entry.delta : 0;
    const level = heatmapLevel(delta);
    const label = entry
      ? `${iso} · 新增完成 ${delta} · 累计完成 ${entry.completed}/${entry.total || "-"}`
      : `${iso} · 没有快照`;

    dayCells.push(`
      <div class="heatmap-cell-wrap" style="grid-column:${heatmapWeekColumn(gridStart, cursor)}; grid-row:${weekRow(cursor)};">
        <span class="heatmap-cell heatmap-level-${level}${entry ? " heatmap-has-snapshot" : ""}" title="${escapeAttr(label)}"></span>
      </div>
    `);

    cursor.setDate(cursor.getDate() + 1);
  }

  const monthMarkers = heatmapMonthMarkers(gridStart, endDate);
  const visibleEntries = Array.from(seriesByDate.values()).filter((entry) => {
    const date = new Date(`${entry.date}T00:00:00`);
    return date >= startDate && date <= endDate;
  });
  const activeDays = visibleEntries.filter((entry) => entry.delta > 0).length;
  const totalDelta = visibleEntries.reduce((sum, entry) => sum + entry.delta, 0);
  const latest = rows[rows.length - 1] || null;

  return `
    <section class="history-heatmap-panel" style="--heatmap-accent:${accent};">
      <div class="history-heatmap-header">
        <div>
          <p class="eyebrow">Activity Heatmap</p>
          <h3>过去一年推进热力图</h3>
        </div>
        <div class="history-heatmap-legend" aria-label="热力图图例">
          <span>少</span>
          <i class="heatmap-cell heatmap-level-0" aria-hidden="true"></i>
          <i class="heatmap-cell heatmap-level-1" aria-hidden="true"></i>
          <i class="heatmap-cell heatmap-level-2" aria-hidden="true"></i>
          <i class="heatmap-cell heatmap-level-3" aria-hidden="true"></i>
          <i class="heatmap-cell heatmap-level-4" aria-hidden="true"></i>
          <span>多</span>
        </div>
      </div>
      <div class="history-heatmap-stats">
        <span><strong>${totalDelta}</strong> 新增完成</span>
        <span><strong>${activeDays}</strong> 活跃天</span>
        <span><strong>${latest ? latest.completed : 0}/${latest && latest.total ? latest.total : "-"}</strong> 当前完成</span>
      </div>
      ${rows.length < 2 ? `<p class="muted history-heatmap-note">需要更多每日快照后，热力图才会开始显示连续推进趋势。</p>` : ""}
      <div class="history-heatmap-scroll" role="img" aria-label="项目每日推进热力图">
        <div class="history-heatmap-grid-wrap">
        <div class="history-heatmap-weekdays">
          ${weekDays.map((day) => `<span>${day}</span>`).join("")}
        </div>
        <div class="history-heatmap-grid">
          ${monthMarkers}
          ${dayCells.join("")}
        </div>
        </div>
      </div>
    </section>
  `;
}

function heatmapLevel(delta) {
  if (delta <= 0) return 0;
  if (delta === 1) return 1;
  if (delta === 2) return 2;
  if (delta <= 4) return 3;
  return 4;
}

function heatmapWeekColumn(gridStart, date) {
  const dayMs = 24 * 60 * 60 * 1000;
  return Math.floor((date - gridStart) / (7 * dayMs)) + 1;
}

function weekRow(date) {
  return date.getDay() + 2;
}

function heatmapMonthMarkers(startDate, endDate) {
  const markers = [];
  const seen = new Set();
  const cursor = new Date(startDate);
  while (cursor <= endDate) {
    if (cursor.getDate() === 1) {
      const key = formatDateKey(cursor).slice(0, 7);
      if (!seen.has(key)) {
        seen.add(key);
        markers.push(`
          <span class="heatmap-month-label" style="grid-column:${heatmapWeekColumn(startDate, cursor)};">
            ${cursor.toLocaleDateString("en-US", { month: "short" })}
          </span>
        `);
      }
    }
    cursor.setDate(cursor.getDate() + 1);
  }
  return markers.join("");
}

function formatDateKey(date) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
}

function renderNextWork(model) {
  const work = model.nextWork || [];
  const focusNode = defaultMapNode(model);
  if (!work.length) {
    nextWorkElement.innerHTML = emptyState("暂时没有下一步工作。");
    return;
  }

  const actionItems = nextWorkActionItems(focusNode, work);
  const doNext = actionItems.slice(0, 3);
  const thenQueue = actionItems.slice(3, 10);
  const nextPhase = work.find((item) => item.source === "map" && item.status !== "current") || null;
  const outputs = focusNode?.outputs || [];
  const dependencies = focusNode?.dependsOn || [];
  const taskRefs = focusNode?.taskRefs || [];

  nextWorkElement.innerHTML = `
    <div class="execution-board">
      <section class="execution-focus-panel">
        <p class="eyebrow">Now Focus</p>
        <div class="execution-focus-row">
          <div>
            <h3>${escapeHtml(focusNode?.title || work[0]?.title || "下一步工作")}</h3>
            <p>${escapeHtml(focusNode?.summary || work[0]?.summary || "暂无当前阶段说明。")}</p>
          </div>
          <div class="execution-focus-meta">
            <span>${escapeHtml(statusLabel(focusNode?.status || work[0]?.status))}</span>
            ${focusNode?.phase ? `<span>Phase ${escapeHtml(focusNode.phase)}</span>` : ""}
            ${nextPhase ? `<span>Then: ${escapeHtml(nextPhase.title)}</span>` : ""}
          </div>
        </div>
      </section>

      <div class="execution-layout">
        <section class="execution-main">
          <div class="execution-section-title">
            <p class="eyebrow">Do Next</p>
            <h3>先做这几件</h3>
          </div>
          <div class="do-next-list">
            ${doNext.length ? doNext.map((item, index) => executionActionCard(item, index)).join("") : emptyState("当前节点没有明确下一步动作。")}
          </div>

          <div class="execution-section-title compact">
            <p class="eyebrow">Then</p>
            <h3>后续队列</h3>
          </div>
          <ol class="then-queue-list">
            ${thenQueue.length ? thenQueue.map((item) => executionQueueItem(item)).join("") : `<li class="then-queue-empty">后续任务会在完成当前动作后展开。</li>`}
          </ol>
        </section>

        <aside class="execution-context">
          <section>
            <p class="eyebrow">Expected Outputs</p>
            ${referenceList(outputs, "当前阶段还没有记录产物。")}
          </section>
          <section>
            <p class="eyebrow">Dependencies</p>
            ${plainList(dependencies, "暂无阻塞依赖。")}
          </section>
          <section>
            <p class="eyebrow">Task Refs</p>
            ${plainList(taskRefs, "暂无任务引用。")}
          </section>
        </aside>
      </div>
    </div>
  `;
}

function nextWorkActionItems(focusNode, work) {
  const focusActions = (focusNode?.nextActions || []).map((title, index) => ({
    id: `focus-action-${index}`,
    title,
    status: index === 0 ? "current" : "next",
    summary: index === 0 ? "当前最小可执行动作" : "当前阶段动作",
    source: "map",
  }));
  const todoActions = work
    .filter((item) => item.source === "todo")
    .map((item) => ({ ...item, summary: item.summary || "Todo" }));

  const seen = new Set();
  return [...focusActions, ...todoActions].filter((item) => {
    const key = String(item.title || "").trim().toLowerCase();
    if (!key || seen.has(key)) {
      return false;
    }
    seen.add(key);
    return true;
  });
}

function executionActionCard(item, index) {
  return `
    <article class="do-next-item status-${statusClass(item.status)}">
      <div class="action-index">${index + 1}</div>
      <div>
        <span>${escapeHtml(statusLabel(item.status))} · ${escapeHtml(item.source || "map")}</span>
        <h4>${escapeHtml(item.title)}</h4>
        ${item.summary ? `<p>${escapeHtml(item.summary)}</p>` : ""}
      </div>
    </article>
  `;
}

function executionQueueItem(item) {
  return `
    <li>
      <span>${escapeHtml(item.title)}</span>
      ${item.summary ? `<small>${escapeHtml(item.summary)}</small>` : ""}
    </li>
  `;
}

function renderPaperReadiness(model) {
  const sections = model.paper?.sections || [];
  const summary = model.readinessSummary || readinessSummary(sections);
  const overview = `
    <div class="readiness-overview">
      <div>
        <p class="eyebrow">Paper Progress</p>
        <strong>${percent(summary.fraction)}</strong>
      </div>
      <div class="readiness-stats">
        <span>${summary.ready || 0} ready/draft</span>
        <span>${summary.blocked || 0} blocked</span>
        <span>${summary.missing || 0} missing</span>
      </div>
    </div>
  `;

  if (!sections.length) {
    paperReadiness.innerHTML = `${overview}${emptyState("这个项目还没有 paper manifest，先显示简版地图。")}`;
    return;
  }

  paperReadiness.innerHTML = `
    ${overview}
    <div class="paper-section-grid">
      ${sections.map((section) => paperSectionCard(section)).join("")}
    </div>
  `;
}

function paperSectionCard(section) {
  return `
    <article class="paper-section-card status-${statusClass(section.status)}">
      <div class="paper-section-top">
        <h3>${escapeHtml(section.title)}</h3>
        <span>${escapeHtml(statusLabel(section.status))}</span>
      </div>
      <p>${escapeHtml(section.summary || "暂无章节摘要。")}</p>
      <div class="paper-subsection">
        <strong>Assets</strong>
        ${referenceList(section.assets, "暂无资产。")}
      </div>
      <div class="paper-subsection">
        <strong>Gaps</strong>
        ${plainList(section.blockers, "暂无明确缺口。")}
      </div>
      <div class="paper-subsection">
        <strong>Next</strong>
        ${plainList(section.nextActions, "暂无下一步。")}
      </div>
    </article>
  `;
}

function setActiveDetailPage(key, options = {}) {
  activeDetailPage = normalizeDetailPage(key);
  projectView.dataset.activePage = activeDetailPage;
  updateProjectPagesVisibility();
  projectNav.querySelectorAll("[data-nav-key]").forEach((link) => {
    link.classList.toggle("active", link.dataset.navKey === activeDetailPage);
  });

  if (options.updateHash) {
    pushDetailHash(activeDetailPage);
  }

  if (options.scrollTop) {
    projectView.scrollIntoView({ behavior: "smooth", block: "start" });
  }
}

function updateProjectPagesVisibility() {
  document.querySelectorAll(".project-page").forEach((section) => {
    section.hidden = section.dataset.section !== activeDetailPage;
  });
}

function handleDetailLocationChange() {
  const page = detailPageFromHash();
  if (page === activeDetailPage) {
    return;
  }
  activeDetailPage = page;
  if (currentView === "project") {
    render();
  }
}

function detailPageFromHash() {
  const hash = window.location.hash.replace(/^#/, "");
  const legacyHashes = {
    "project-map-section": "map",
    "history-section": "history",
    "next-work-section": "overview",
    "next-work": "overview",
    "next": "overview",
    "paper-readiness-section": "paper",
  };
  if (legacyHashes[hash]) {
    return legacyHashes[hash];
  }
  const item = PROJECT_NAV_ITEMS.find((candidate) => candidate.hash === hash || candidate.key === hash);
  return item ? item.key : "overview";
}

function normalizeDetailPage(key) {
  return PROJECT_NAV_ITEMS.some((item) => item.key === key) ? key : "map";
}

function pushDetailHash(key) {
  const item = PROJECT_NAV_ITEMS.find((candidate) => candidate.key === key);
  if (!item) {
    return;
  }
  window.history.pushState(window.history.state, "", `#${item.hash}`);
}

function replaceDetailHash(key) {
  const item = PROJECT_NAV_ITEMS.find((candidate) => candidate.key === key);
  if (!item) {
    return;
  }
  window.history.replaceState(window.history.state, "", `#${item.hash}`);
}

function projectMapModel(source) {
  if (!source) {
    return emptyProjectMap();
  }

  if (source.projectMap && Array.isArray(source.projectMap.mapNodes)) {
    return {
      ...emptyProjectMap(),
      ...source.projectMap,
      paper: { sections: source.projectMap.paper?.sections || [] },
    };
  }

  return deriveClientProjectMap(source);
}

function deriveClientProjectMap(source) {
  const phases = source.roadmap?.phases || source.phases || [];
  const nodes = phases.map((phase, index) => {
    const status = phase.isCurrent ? "current" : phase.status === "complete" ? "done" : index === 0 ? "next" : "planned";
    const lane = status === "done" ? "done" : status === "current" ? "now" : "next";
    return {
      id: phase.id || `${source.id}-phase-${phase.number || index + 1}`,
      title: phase.number ? `Phase ${phase.number}: ${phase.title}` : phase.title,
      lane,
      status,
      phase: phase.number,
      summary: phase.summary || source.currentMainline || "从 roadmap / todo 自动生成的简版地图节点。",
      dependsOn: [],
      outputs: (phase.outputs || []).map((item) => ({ label: item, path: "", type: "output", status: "ready" })),
      taskRefs: (phase.tasks || []).slice(0, 8).map((task) => `line-${task.lineNumber}`),
      nextActions: (phase.tasks || []).filter((task) => !task.completed).slice(0, 4).map((task) => task.title),
    };
  });

  return {
    ...emptyProjectMap(),
    mode: "derived",
    project: source.name,
    title: source.name,
    currentFocus: source.currentMainline || "",
    mapNodes: nodes,
    history: nodes.filter((node) => node.status === "done"),
    nextWork: (source.nextActions || []).map((task) => ({
      id: `task-${task.lineNumber}`,
      title: task.title,
      status: "next",
      summary: task.lineNumber ? `Todo line ${task.lineNumber}` : "",
      source: "todo",
    })),
  };
}

function emptyProjectMap() {
  return {
    mode: "none",
    title: "",
    currentFocus: "",
    researchQuestion: "",
    milestones: [],
    mapNodes: [],
    paper: { sections: [] },
    history: [],
    nextWork: [],
    readinessSummary: { total: 0, ready: 0, blocked: 0, missing: 0, planned: 0, fraction: 0 },
    error: null,
  };
}

function defaultMapNode(model) {
  const nodes = model.mapNodes || [];
  return nodes.find((node) => node.status === "current")
    || nodes.find((node) => node.lane === "now")
    || nodes[0]
    || null;
}

function findMapNode(model, nodeId) {
  return (model.mapNodes || []).find((node) => node.id === nodeId) || null;
}

function selectedSource() {
  return dashboardState?.sources.find((source) => source.id === selectedSourceId) || null;
}

function referenceList(items, emptyMessage) {
  const refs = (items || []).filter(Boolean);
  if (!refs.length) {
    return emptyState(emptyMessage);
  }
  return `
    <ul class="reference-list">
      ${refs.map((item) => {
        const ref = typeof item === "string" ? { label: item, path: "", type: "output", status: "ready" } : item;
        const meta = [ref.type, ref.status ? statusLabel(ref.status) : "", ref.path].filter(Boolean).join(" · ");
        return `
          <li>
            <span>${escapeHtml(ref.label || ref.path || "Asset")}</span>
            ${meta ? `<small>${escapeHtml(meta)}</small>` : ""}
          </li>
        `;
      }).join("")}
    </ul>
  `;
}

function plainList(items, emptyMessage) {
  const values = (items || []).filter(Boolean);
  if (!values.length) {
    return emptyState(emptyMessage);
  }
  return `
    <ul class="plain-list">
      ${values.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}
    </ul>
  `;
}

function readinessSummary(sections) {
  const total = sections.length;
  const ready = sections.filter((section) => ["ready", "done", "draft"].includes(section.status)).length;
  const blocked = sections.filter((section) => section.status === "blocked").length;
  const missing = sections.filter((section) => section.status === "missing").length;
  const planned = sections.filter((section) => section.status === "planned").length;
  return { total, ready, blocked, missing, planned, fraction: total ? ready / total : 0 };
}

function normalizedLane(lane) {
  return ["done", "now", "next", "paper"].includes(lane) ? lane : "next";
}

function laneLabel(lane) {
  const item = MAP_LANES.find((candidate) => candidate.key === normalizedLane(lane));
  return item ? item.label : "Next";
}

function statusLabel(status) {
  return STATUS_LABELS[status] || status || "未知";
}

function statusClass(status) {
  return String(status || "unknown").replaceAll("_", "-").replace(/[^a-zA-Z0-9-]/g, "");
}

function metric(title, value, caption) {
  return `
    <article class="metric">
      <p class="eyebrow">${escapeHtml(title)}</p>
      <div class="metric-value">${escapeHtml(String(value))}</div>
      <p class="muted">${escapeHtml(caption)}</p>
    </article>
  `;
}

function emptyState(message) {
  return `<p class="empty-state">${escapeHtml(message)}</p>`;
}

function percent(value) {
  return `${Math.round((Number(value) || 0) * 100)}%`;
}

function clampedPercent(value) {
  return Math.max(0, Math.min(100, Math.round((Number(value) || 0) * 100)));
}

function safeColor(value) {
  return /^#[0-9a-fA-F]{6}$/.test(value || "") ? value : "#2563eb";
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function escapeAttr(value) {
  return escapeHtml(value);
}

function setRefreshState(isLoading) {
  refreshButton.disabled = isLoading;
  refreshButton.textContent = isLoading ? "刷新中..." : "刷新";
}

function renderError(error) {
  currentView = "home";
  homeView.hidden = false;
  projectView.hidden = true;
  renderProjectNav(null);
  document.querySelector("#last-updated").textContent = "加载失败";
  document.querySelector("#summary").innerHTML = "";
  document.querySelector("#source-grid").innerHTML = "";
  projectMapElement.innerHTML = emptyState(error.message);
  projectHistory.innerHTML = "";
  if (overviewElement) overviewElement.innerHTML = "";
  paperReadiness.innerHTML = "";
  if (mapNodeDetail) mapNodeDetail.innerHTML = "";
}

function renderTrendChart() {
  const section = document.querySelector("#trend-section");
  const svg = document.querySelector("#trend-chart");
  const legend = document.querySelector("#trend-legend");
  
  if (!section || !svg || !legend) return;
  
  if (!historyData || historyData.length < 2) {
    section.style.display = "none";
    return;
  }
  
  section.style.display = "block";
  
  // Get all unique active sources in the history
  const sourceIds = Array.from(new Set(
    historyData.flatMap(d => (d.sources || []).map(s => s.id))
  ));
  
  // Find accent colors from dashboardState
  const colorMap = {};
  const nameMap = {};
  if (dashboardState && dashboardState.sources) {
    dashboardState.sources.forEach(s => {
      colorMap[s.id] = s.accent || "#2563eb";
      nameMap[s.id] = s.name;
    });
  }
  
  const width = 800;
  const height = 220;
  const paddingLeft = 50;
  const paddingRight = 30;
  const paddingTop = 20;
  const paddingBottom = 30;
  
  const graphWidth = width - paddingLeft - paddingRight;
  const graphHeight = height - paddingTop - paddingBottom;
  
  const days = historyData.length;
  
  // Generate Y axis grid lines (0%, 25%, 50%, 75%, 100%)
  let gridHtml = "";
  for (let pct = 0; pct <= 100; pct += 25) {
    const y = paddingTop + graphHeight * (1 - pct / 100);
    gridHtml += `
      <line x1="${paddingLeft}" y1="${y}" x2="${width - paddingRight}" y2="${y}" stroke="var(--soft)" stroke-width="1" stroke-dasharray="4 4" />
      <text x="${paddingLeft - 10}" y="${y}" fill="var(--muted)" font-size="11" text-anchor="end" dominant-baseline="central">${pct}%</text>
    `;
  }
  
  // Generate X axis date labels (Start, Middle, End)
  let datesHtml = "";
  const dateIndices = days > 2 ? [0, Math.floor((days - 1) / 2), days - 1] : [0, days - 1];
  dateIndices.forEach(idx => {
    const dateStr = historyData[idx].date;
    const x = paddingLeft + (idx / (days - 1)) * graphWidth;
    datesHtml += `
      <text x="${x}" y="${height - 10}" fill="var(--muted)" font-size="11" text-anchor="middle">${dateStr.substring(5)}</text>
    `;
  });
  
  // Draw lines for each project
  let linesHtml = "";
  let legendHtml = "";
  
  sourceIds.forEach(sourceId => {
    const color = colorMap[sourceId] || "#999";
    const name = nameMap[sourceId] || sourceId;
    
    // Build path points
    const points = [];
    historyData.forEach((day, dayIdx) => {
      const src = (day.sources || []).find(s => s.id === sourceId);
      if (src && src.total > 0) {
        const fraction = src.fraction || 0;
        const x = paddingLeft + (dayIdx / (days - 1)) * graphWidth;
        const y = paddingTop + graphHeight * (1 - fraction);
        points.push({ x, y, fraction, date: day.date, completed: src.completed, total: src.total });
      }
    });
    
    if (points.length < 2) return;
    
    const pathD = points.map((p, idx) => `${idx === 0 ? 'M' : 'L'} ${p.x.toFixed(1)} ${p.y.toFixed(1)}`).join(" ");
    
    // Draw line and circles
    linesHtml += `
      <path d="${pathD}" fill="none" stroke="${escapeAttr(color)}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
    `;
    
    // Draw circles at data points
    points.forEach(p => {
      linesHtml += `
        <circle cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="4" fill="var(--surface)" stroke="${escapeAttr(color)}" stroke-width="2">
          <title>${name}: ${percent(p.fraction)} (${p.completed}/${p.total} 节点) 于 ${p.date}</title>
        </circle>
      `;
    });
    
    // Build legend
    legendHtml += `
      <div class="legend-item" style="display: flex; align-items: center; gap: 6px;">
        <span style="width: 10px; height: 10px; border-radius: 50%; background: ${escapeAttr(color)}; display: inline-block;"></span>
        <span style="font-weight: 600; color: var(--ink);">${escapeHtml(name)}</span>
      </div>
    `;
  });
  
  svg.innerHTML = `
    <!-- Grid and axes -->
    ${gridHtml}
    ${datesHtml}
    <!-- Lines and markers -->
    ${linesHtml}
  `;
  
  legend.innerHTML = legendHtml;
}
