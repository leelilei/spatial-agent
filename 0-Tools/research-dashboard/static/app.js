let dashboardState = null;
let selectedSourceId = null;
let selectedMapNodeId = null;
let currentView = "home";
let refreshTimer = null;
let projectSectionObserver = null;
let activeNavKey = "map";

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
const nextWorkElement = document.querySelector("#next-work");
const paperReadiness = document.querySelector("#paper-readiness");
const mapNodeDetail = document.querySelector("#map-node-detail");

const PROJECT_NAV_ITEMS = [
  { key: "map", label: "Project Map", targetId: "project-map-section" },
  { key: "history", label: "History", targetId: "history-section" },
  { key: "next", label: "Next Work", targetId: "next-work-section" },
  { key: "paper", label: "Paper Readiness", targetId: "paper-readiness-section" },
];

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
  activeNavKey = "map";
  render();
});

loadState();
refreshTimer = window.setInterval(loadState, 60000);

async function loadState() {
  setRefreshState(true);
  try {
    const response = await fetch(stateUrl, { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    dashboardState = await response.json();

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
  renderSummary();
  renderSources();

  const shouldShowProject = currentView === "project" && selected;
  homeView.hidden = shouldShowProject;
  projectView.hidden = !shouldShowProject;
  clearProjectSectionObserver();

  if (shouldShowProject) {
    renderProject(selected);
    window.requestAnimationFrame(() => {
      setupProjectSectionObserver();
      syncNavFromViewport();
    });
    return;
  }

  renderProjectNav(null);
}

function renderProject(source) {
  const model = projectMapModel(source);
  const defaultNode = defaultMapNode(model);
  if (!selectedMapNodeId || !findMapNode(model, selectedMapNodeId)) {
    selectedMapNodeId = defaultNode?.id || null;
  }

  projectTitle.textContent = model.title || `${source.name} Research Map`;
  projectMainline.textContent = model.currentFocus || source.currentMainline || "暂无当前焦点";
  researchQuestion.textContent = model.researchQuestion
    ? `Research Question: ${model.researchQuestion}`
    : "Research Question: 暂未记录，先用项目路线图和 todo 派生地图。";

  renderProjectNav(source);
  renderProjectMap(source, model);
  renderMapNodeDetail(source, model);
  renderHistory(model);
  renderNextWork(model);
  renderPaperReadiness(model);
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

  summary.innerHTML = [
    metric("项目源", `${totals.readableCount}/${totals.sourceCount}`, "可读取项目"),
    metric("待办任务", totals.openTasks, "当前任务"),
    metric("P0 / P1", `${totals.p0}/${totals.p1}`, "紧急 / 下一步"),
    metric("路线图进度", percent(totals.progressFraction), `${totals.progressCompleted}/${totals.progressTotal} 个阶段任务`),
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
      activeNavKey = "map";
      render();
      window.requestAnimationFrame(() => window.scrollTo({ top: 0, behavior: "smooth" }));
    });
  });
}

function sourceCard(source) {
  const model = projectMapModel(source);
  const active = currentView === "project" && source.id === selectedSourceId ? " active" : "";
  const error = source.error ? " error" : "";
  const mapMode = model.mode === "manifest" ? "Manifest" : "Fallback";
  const progressText = source.progress.total
    ? `路线图 ${percent(source.progress.fraction)}`
    : "暂无路线图进度";
  const status = source.error
    ? `<span class="status-pill error">异常</span>`
    : `<span class="status-pill">${escapeHtml(mapMode)}</span>`;
  const focus = model.currentFocus || source.currentMainline || "暂无当前焦点";
  const foot = source.error
    ? `<p class="error-text">${escapeHtml(source.error)}</p>`
    : `<p class="path">${escapeHtml(source.path)}</p>`;

  return `
    <article class="source-card${active}${error}" data-source-id="${escapeAttr(source.id)}">
      <div class="source-heading">
        <span class="dot" style="background:${safeColor(source.accent)}"></span>
        <h3>${escapeHtml(source.name)}</h3>
        ${status}
      </div>
      <div class="card-stats">
        <div class="stat"><strong>${source.taskCounts.open}</strong><span>待办</span></div>
        <div class="stat"><strong>${source.priorityCounts.P0}</strong><span>P0</span></div>
        <div class="stat"><strong>${(model.mapNodes || []).length}</strong><span>地图节点</span></div>
      </div>
      <p class="mainline">${escapeHtml(focus)}</p>
      <div class="progress-track" aria-label="${escapeAttr(progressText)}">
        <div class="progress-fill" style="width:${clampedPercent(source.progress.fraction)}%;background:${safeColor(source.accent)}"></div>
      </div>
      <p class="phase-meta">${escapeHtml(progressText)}</p>
      ${foot}
    </article>
  `;
}

function renderProjectNav(source) {
  if (!source || source.error) {
    projectNav.innerHTML = "";
    return;
  }

  projectNav.innerHTML = PROJECT_NAV_ITEMS.map((item) => projectNavLink(item)).join("");
  projectNav.querySelectorAll("[data-nav-key]").forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      const key = link.dataset.navKey;
      const item = PROJECT_NAV_ITEMS.find((candidate) => candidate.key === key);
      const target = item ? document.getElementById(item.targetId) : null;
      if (!target) {
        return;
      }
      setActiveNavKey(key);
      target.scrollIntoView({ behavior: "smooth", block: "start" });
      window.history.replaceState(window.history.state, "", `#${item.targetId}`);
    });
  });
}

function projectNavLink(item) {
  const active = item.key === activeNavKey ? " active" : "";
  return `
    <a class="project-nav-link${active}" href="#${escapeAttr(item.targetId)}" data-nav-key="${escapeAttr(item.key)}">
      ${escapeHtml(item.label)}
    </a>
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

  const lanes = MAP_LANES.map((lane) => {
    const laneNodes = nodes.filter((node) => normalizedLane(node.lane) === lane.key);
    return `
      <section class="map-lane map-lane-${escapeAttr(lane.key)}">
        <header class="map-lane-header">
          <div>
            <h3>${escapeHtml(lane.label)}</h3>
            <p>${escapeHtml(lane.caption)}</p>
          </div>
          <span>${laneNodes.length}</span>
        </header>
        <div class="map-node-list">
          ${laneNodes.length ? laneNodes.map((node) => mapNodeButton(node)).join("") : emptyState("暂无节点")}
        </div>
      </section>
    `;
  }).join("");

  projectMapElement.innerHTML = `
    ${warning}
    <div class="map-canvas" style="--project-accent:${safeColor(source.accent)}">
      <svg class="map-flow-lines" viewBox="0 0 1000 160" preserveAspectRatio="none" aria-hidden="true">
        <path d="M 34 82 C 210 24 324 136 500 82 S 790 34 966 82" />
      </svg>
      <div class="map-lanes">${lanes}</div>
    </div>
  `;

  projectMapElement.querySelectorAll("[data-node-id]").forEach((button) => {
    button.addEventListener("click", () => {
      selectedMapNodeId = button.dataset.nodeId;
      updateMapNodeActiveStates();
      renderMapNodeDetail(selectedSource(), projectMapModel(selectedSource()));
    });
  });
}

function mapNodeButton(node) {
  const active = node.id === selectedMapNodeId ? " active" : "";
  const phase = node.phase ? `<span>Phase ${escapeHtml(node.phase)}</span>` : "";
  return `
    <button
      class="map-node status-${statusClass(node.status)}${active}"
      type="button"
      data-node-id="${escapeAttr(node.id)}"
      aria-pressed="${node.id === selectedMapNodeId ? "true" : "false"}"
    >
      <span class="node-status">${escapeHtml(statusLabel(node.status))}</span>
      <strong>${escapeHtml(node.title)}</strong>
      <p>${escapeHtml(node.summary || "暂无节点摘要。")}</p>
      <div class="node-meta">
        ${phase}
        <span>${escapeHtml(laneLabel(node.lane))}</span>
      </div>
    </button>
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
  const node = findMapNode(model, selectedMapNodeId) || defaultMapNode(model);
  if (!source || source.error || !node) {
    mapNodeDetail.innerHTML = emptyState(source?.error || "请选择一个地图节点。");
    return;
  }

  mapNodeDetail.innerHTML = `
    <div class="drawer-kicker">${escapeHtml(laneLabel(node.lane))} / ${escapeHtml(statusLabel(node.status))}</div>
    <h2>${escapeHtml(node.title)}</h2>
    <p class="drawer-summary">${escapeHtml(node.summary || "暂无节点摘要。")}</p>

    <div class="drawer-meta-grid">
      <div><span>Phase</span><strong>${node.phase || "N/A"}</strong></div>
      <div><span>Tasks</span><strong>${(node.taskRefs || []).length}</strong></div>
      <div><span>Outputs</span><strong>${(node.outputs || []).length}</strong></div>
      <div><span>Depends</span><strong>${(node.dependsOn || []).length}</strong></div>
    </div>

    <section class="drawer-section">
      <h3>产物 / 证据</h3>
      ${referenceList(node.outputs, "这个节点还没有记录产物。")}
    </section>

    <section class="drawer-section">
      <h3>下一步动作</h3>
      ${plainList(node.nextActions, "这个节点暂时没有下一步动作。")}
    </section>

    <section class="drawer-section">
      <h3>关联</h3>
      ${plainList([...(node.dependsOn || []).map((item) => `Depends on: ${item}`), ...(node.taskRefs || []).map((item) => `Task: ${item}`)], "暂无依赖或任务引用。")}
    </section>
  `;
}

function renderHistory(model) {
  const history = model.history || model.milestones || [];
  if (!history.length) {
    projectHistory.innerHTML = emptyState("还没有记录历史 milestone。");
    return;
  }

  projectHistory.innerHTML = `
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

function renderNextWork(model) {
  const work = model.nextWork || [];
  if (!work.length) {
    nextWorkElement.innerHTML = emptyState("暂时没有下一步工作。");
    return;
  }

  nextWorkElement.innerHTML = `
    <div class="next-work-list">
      ${work.map((item) => `
        <article class="next-work-item status-${statusClass(item.status)}">
          <span>${escapeHtml(statusLabel(item.status))} · ${escapeHtml(item.source || "map")}</span>
          <h3>${escapeHtml(item.title)}</h3>
          ${item.summary ? `<p>${escapeHtml(item.summary)}</p>` : ""}
        </article>
      `).join("")}
    </div>
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

function setupProjectSectionObserver() {
  if (typeof window.IntersectionObserver !== "function") {
    return;
  }

  const sections = PROJECT_NAV_ITEMS
    .map((item) => document.getElementById(item.targetId))
    .filter(Boolean);

  if (!sections.length) {
    return;
  }

  projectSectionObserver = new window.IntersectionObserver(handleSectionIntersections, {
    root: null,
    rootMargin: "-18% 0px -56% 0px",
    threshold: [0.1, 0.25, 0.5, 0.75],
  });

  sections.forEach((section) => {
    projectSectionObserver.observe(section);
  });
}

function handleSectionIntersections(entries) {
  const visible = entries
    .filter((entry) => entry.isIntersecting)
    .sort((left, right) => {
      if (right.intersectionRatio !== left.intersectionRatio) {
        return right.intersectionRatio - left.intersectionRatio;
      }
      return Math.abs(left.boundingClientRect.top) - Math.abs(right.boundingClientRect.top);
    });

  if (!visible.length) {
    return;
  }

  const sectionKey = visible[0].target.dataset.section;
  if (sectionKey) {
    setActiveNavKey(sectionKey);
  }
}

function syncNavFromViewport() {
  const sectionStates = PROJECT_NAV_ITEMS
    .map((item) => {
      const element = document.getElementById(item.targetId);
      if (!element) {
        return null;
      }
      const rect = element.getBoundingClientRect();
      return {
        key: item.key,
        distance: Math.abs(rect.top - 140),
      };
    })
    .filter(Boolean)
    .sort((left, right) => left.distance - right.distance);

  if (sectionStates.length) {
    setActiveNavKey(sectionStates[0].key);
  }
}

function clearProjectSectionObserver() {
  if (projectSectionObserver) {
    projectSectionObserver.disconnect();
    projectSectionObserver = null;
  }
}

function setActiveNavKey(key) {
  activeNavKey = key;
  projectNav.querySelectorAll("[data-nav-key]").forEach((link) => {
    link.classList.toggle("active", link.dataset.navKey === key);
  });
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
  return /^#[0-9a-fA-F]{6}$/.test(value || "") ? value : "#0071e3";
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
  clearProjectSectionObserver();
  homeView.hidden = false;
  projectView.hidden = true;
  renderProjectNav(null);
  document.querySelector("#last-updated").textContent = "加载失败";
  document.querySelector("#summary").innerHTML = "";
  document.querySelector("#source-grid").innerHTML = "";
  projectMapElement.innerHTML = emptyState(error.message);
  projectHistory.innerHTML = "";
  nextWorkElement.innerHTML = "";
  paperReadiness.innerHTML = "";
  mapNodeDetail.innerHTML = "";
}
