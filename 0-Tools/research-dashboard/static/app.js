let dashboardState = null;
let selectedSourceId = null;
let selectedPhaseNumber = null;
let currentView = "home";
let refreshTimer = null;

const stateUrl = "/api/state";
const refreshButton = document.querySelector("#refresh-button");
const homeView = document.querySelector("#home-view");
const projectView = document.querySelector("#project-view");
const backButton = document.querySelector("#back-button");
const projectTitle = document.querySelector("#project-title");
const projectMainline = document.querySelector("#project-mainline");
const projectMetrics = document.querySelector("#project-metrics");
const phaseModal = document.querySelector("#phase-modal");
const phaseModalClose = document.querySelector("#phase-modal-close");
const phaseModalContent = document.querySelector("#phase-modal-content");

refreshButton.addEventListener("click", () => {
  loadState();
});

backButton.addEventListener("click", () => {
  currentView = "home";
  closePhaseModal();
  render();
});

phaseModalClose.addEventListener("click", () => {
  closePhaseModal();
});

phaseModal.addEventListener("click", (event) => {
  if (event.target === phaseModal) {
    closePhaseModal();
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && !phaseModal.hidden) {
    closePhaseModal();
  }
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
      currentView = "home";
    }
    closePhaseModal();
    render();
  } catch (error) {
    renderError(error);
  } finally {
    setRefreshState(false);
  }
}

function defaultSourceId(sources) {
  const withPhases = sources.find((source) => source.phases.length > 0);
  const readable = sources.find((source) => source.readable);
  return (withPhases || readable || sources[0] || {}).id || null;
}

function render() {
  const selected = selectedSource();
  renderLastUpdated();
  renderSummary();
  renderSources();

  const shouldShowProject = currentView === "project" && selected;
  homeView.hidden = shouldShowProject;
  projectView.hidden = !shouldShowProject;

  if (shouldShowProject) {
    renderProjectHeader(selected);
    renderRoadmap(selected);
    renderNextActions(selected);
    renderTaskBoard(selected);
  }
}

function renderLastUpdated() {
  const label = dashboardState.generatedAt
    ? new Date(dashboardState.generatedAt).toLocaleString()
    : "未知";
  document.querySelector("#last-updated").textContent = `更新 ${label}`;
}

function renderSummary() {
  const totals = dashboardState.totals;
  const summary = document.querySelector("#summary");
  summary.innerHTML = [
    metric("项目源", `${totals.readableCount}/${totals.sourceCount}`, "可读取"),
    metric("待办任务", totals.openTasks, "当前任务"),
    metric("P0 / P1", `${totals.p0}/${totals.p1}`, "紧急 / 下一步"),
    metric("路线图", percent(totals.progressFraction), `${totals.progressCompleted}/${totals.progressTotal} 个阶段任务`),
  ].join("");
}

function renderSources() {
  const grid = document.querySelector("#source-grid");
  grid.innerHTML = dashboardState.sources.map(sourceCard).join("");
  grid.querySelectorAll("[data-source-id]").forEach((card) => {
    card.addEventListener("click", () => {
      selectedSourceId = card.dataset.sourceId;
      currentView = "project";
      closePhaseModal();
      render();
    });
  });
}

function sourceCard(source) {
  const active = currentView === "project" && source.id === selectedSourceId ? " active" : "";
  const error = source.error ? " error" : "";
  const progressText = source.progress.total
    ? `路线图 ${percent(source.progress.fraction)}`
    : "暂无路线图";
  const status = source.error
    ? `<span class="status-pill error">错误</span>`
    : `<span class="status-pill">就绪</span>`;
  const mainline = source.currentMainline || "暂无当前主线";
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
        <div class="stat"><strong>${source.phases.length}</strong><span>阶段</span></div>
      </div>
      <p class="mainline">${escapeHtml(mainline)}</p>
      <div class="progress-track" aria-label="${escapeAttr(progressText)}">
        <div class="progress-fill" style="width:${clampedPercent(source.progress.fraction)}%;background:${safeColor(source.accent)}"></div>
      </div>
      <p class="phase-meta">${escapeHtml(progressText)}</p>
      ${foot}
    </article>
  `;
}

function renderProjectHeader(source) {
  projectTitle.textContent = `${source.name} 项目详情`;
  projectMainline.textContent = source.currentMainline || "暂无当前主线";
  projectMetrics.innerHTML = [
    projectMetric("待办", source.taskCounts.open),
    projectMetric("P0", source.priorityCounts.P0),
    projectMetric("阶段", source.phases.length),
    projectMetric("路线图", source.progress.total ? percent(source.progress.fraction) : "暂无"),
  ].join("");
}

function projectMetric(label, value) {
  return `
    <article class="project-metric">
      <strong>${escapeHtml(String(value))}</strong>
      <span>${escapeHtml(label)}</span>
    </article>
  `;
}

function renderRoadmap(source) {
  document.querySelector("#roadmap-title").textContent = source
    ? `${source.name} 路线图`
    : "项目路线图";

  const roadmap = document.querySelector("#roadmap");
  if (!source) {
    roadmap.innerHTML = emptyState("暂无项目源。");
    return;
  }
  if (source.error) {
    roadmap.innerHTML = emptyState(source.error);
    return;
  }

  const roadmapData = source.roadmap || { mode: "derived", phases: source.phases, tracks: [] };
  const phases = roadmapData.phases || source.phases;
  const warning = roadmapData.error ? `<p class="roadmap-warning">${escapeHtml(roadmapData.error)}</p>` : "";

  if (roadmapData.mode === "structured" && phases.length) {
    roadmap.innerHTML = `${warning}${structuredRoadmap(roadmapData)}`;
    bindPhaseCardInteractions();
    return;
  }

  if (!phases.length) {
    roadmap.innerHTML = emptyState("这个项目暂无阶段路线图。");
    return;
  }

  roadmap.innerHTML = `
    ${warning}
    <div class="roadmap-strip">
      ${phases.map((phase, index) => phaseNode(phase, index, phases.length)).join("")}
    </div>
  `;
}

function structuredRoadmap(roadmapData) {
  const phases = roadmapData.phases || [];
  const tracks = roadmapData.tracks || [];
  return `
    ${roadmapTimeline(phases, roadmapData)}
    <div class="roadmap-lanes">
      ${tracks.map((track) => roadmapLane(track, phases)).join("")}
    </div>
  `;
}

function roadmapTimeline(phases, roadmapData) {
  const completed = phases.reduce((sum, phase) => sum + phase.completedCount, 0);
  const total = phases.reduce((sum, phase) => sum + phase.totalCount, 0);
  const current = phases.find((phase) => phase.isCurrent);
  const fill = clampedPercent(total ? completed / total : 0);
  return `
    <section class="roadmap-timeline" aria-label="路线图进度线">
      <div class="timeline-header">
        <div>
          <p class="eyebrow">进度线</p>
          <h3>${current ? `当前 Phase ${current.number}：${escapeHtml(current.title)}` : "暂无当前阶段"}</h3>
        </div>
        <strong>${completed}/${total} · ${percent(total ? completed / total : 0)}</strong>
      </div>
      <div class="timeline-scroll">
        <div class="timeline-bar" style="--timeline-fill:${fill}%">
          <div class="timeline-track"></div>
          <div class="timeline-fill"></div>
          <div class="timeline-markers" style="grid-template-columns: repeat(${Math.max(phases.length, 1)}, minmax(72px, 1fr));">
            ${phases.map((phase) => timelineMarker(phase)).join("")}
          </div>
        </div>
      </div>
    </section>
  `;
}

function timelineMarker(phase) {
  const status = phase.isCurrent ? "current" : phase.status;
  return `
    <div class="timeline-marker ${statusClass(status)}">
      <span>${phase.number}</span>
      <p>${escapeHtml(phase.title)}</p>
    </div>
  `;
}

function roadmapLane(track, phases) {
  const lanePhases = phases.filter((phase) => phase.track === track.id);
  const accent = safeColor(track.accent);
  const content = lanePhases.length
    ? lanePhases.map((phase) => structuredPhaseCard(phase, accent)).join("")
    : emptyState("这个轨道暂无阶段。");

  return `
    <section class="roadmap-lane" style="--track-accent:${accent}">
      <div class="lane-label">
        <span class="lane-dot"></span>
        <h3>${escapeHtml(track.name)}</h3>
      </div>
      <div class="lane-phases">
        ${content}
      </div>
    </section>
  `;
}

function structuredPhaseCard(phase, fallbackAccent) {
  const accent = safeColor(phase.sourceAccent || fallbackAccent);
  const status = statusLabel(phase.status);
  const phaseClasses = ["structured-phase", statusClass(phase.status)];
  if (phase.isCurrent && phase.status !== "current") {
    phaseClasses.push("current");
  }
  const outputs = (phase.outputs || []).slice(0, 4);
  return `
    <article
      class="${phaseClasses.join(" ")}"
      style="--phase-accent:${accent}"
      data-phase-number="${phase.number}"
      role="button"
      tabindex="0"
      aria-label="查看 Phase ${phase.number} ${escapeAttr(phase.title)} 详情"
    >
      <div class="structured-phase-top">
        <span>Phase ${phase.number}</span>
        <strong>${escapeHtml(status)}</strong>
      </div>
      <h3>${escapeHtml(phase.title)}</h3>
      <p>${escapeHtml(phase.summary || "暂无阶段摘要。")}</p>
      <div class="progress-track">
        <div class="progress-fill" style="width:${clampedPercent(phase.fraction)}%;background:${accent}"></div>
      </div>
      <div class="structured-phase-meta">
        <span>${phase.completedCount}/${phase.totalCount} 个任务</span>
        <span>${percent(phase.fraction)}</span>
      </div>
      ${outputs.length ? `<ul>${outputs.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul>` : ""}
    </article>
  `;
}

function bindPhaseCardInteractions() {
  document.querySelectorAll(".structured-phase[data-phase-number]").forEach((card) => {
    card.addEventListener("click", () => {
      openPhaseModal(Number(card.dataset.phaseNumber));
    });
    card.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        openPhaseModal(Number(card.dataset.phaseNumber));
      }
    });
  });
}

function openPhaseModal(phaseNumber) {
  const source = selectedSource();
  const phase = source?.phases.find((item) => item.number === phaseNumber);
  if (!source || !phase) {
    return;
  }

  selectedPhaseNumber = phaseNumber;
  phaseModalContent.innerHTML = phaseModalMarkup(source, phase);
  phaseModal.hidden = false;
  document.body.classList.add("modal-open");
  phaseModalClose.focus();
}

function closePhaseModal() {
  selectedPhaseNumber = null;
  phaseModal.hidden = true;
  phaseModalContent.innerHTML = "";
  document.body.classList.remove("modal-open");
}

function phaseModalMarkup(source, phase) {
  const track = source.roadmap?.tracks.find((item) => item.id === phase.track);
  const openTasks = (phase.tasks || []).filter((task) => !task.completed);
  const completedTasks = (phase.tasks || []).filter((task) => task.completed);
  const outputs = phase.outputs || [];
  const accent = safeColor(track?.accent || phase.sourceAccent);

  return `
    <div class="phase-detail" style="--phase-accent:${accent}">
      <header class="phase-detail-header">
        <div>
          <p class="eyebrow">${escapeHtml(track?.name || "路线图阶段")}</p>
          <h2 id="phase-modal-title">Phase ${phase.number}：${escapeHtml(phase.title)}</h2>
        </div>
        <span class="phase-detail-status">${escapeHtml(statusLabel(phase.status))}</span>
      </header>

      <div class="phase-detail-progress">
        <div class="progress-track">
          <div class="progress-fill" style="width:${clampedPercent(phase.fraction)}%;background:${accent}"></div>
        </div>
        <div class="phase-detail-meta">
          <span>${phase.completedCount}/${phase.totalCount} 个任务</span>
          <span>${percent(phase.fraction)}</span>
        </div>
      </div>

      <p class="phase-detail-summary">${escapeHtml(phase.summary || "暂无阶段摘要。")}</p>

      <section class="phase-detail-section">
        <h3>阶段产物</h3>
        ${outputs.length ? `<ul class="phase-output-list">${outputs.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul>` : emptyState("暂无阶段产物。")}
      </section>

      <div class="phase-task-groups">
        ${phaseTaskGroup("未完成任务", openTasks, false)}
        ${phaseTaskGroup("已完成任务", completedTasks, true)}
      </div>
    </div>
  `;
}

function phaseTaskGroup(title, tasks, isCompleted) {
  const content = tasks.length
    ? tasks.map((task) => phaseDetailTask(task, isCompleted)).join("")
    : emptyState("暂无任务。");
  return `
    <section class="phase-task-group">
      <h3>${escapeHtml(title)} <span>${tasks.length}</span></h3>
      <div class="phase-detail-tasks">
        ${content}
      </div>
    </section>
  `;
}

function phaseDetailTask(task, isCompleted) {
  return `
    <article class="phase-detail-task ${isCompleted ? "completed" : ""}">
      <span class="task-state">${isCompleted ? "已完成" : "待办"}</span>
      <p>${escapeHtml(task.title)}</p>
      <small>第 ${task.lineNumber} 行</small>
    </article>
  `;
}

function phaseNode(phase, index, total) {
  const statusClass = phase.status === "complete" ? "complete" : phase.isCurrent ? "current" : "";
  const connector = index < total - 1 ? `<span class="phase-connector"></span>` : "";
  const circleColor = phase.status === "complete" || phase.isCurrent ? safeColor(phase.sourceAccent) : "";

  return `
    <div class="phase-node">
      <div class="phase-top">
        <div class="phase-circle ${statusClass}" style="${circleColor ? `background:${circleColor}` : ""}">
          ${phase.number}
        </div>
        ${connector}
      </div>
      <h3>${escapeHtml(phase.title)}</h3>
      <div class="progress-track">
        <div class="progress-fill" style="width:${clampedPercent(phase.fraction)}%;background:${safeColor(phase.sourceAccent)}"></div>
      </div>
      <p class="phase-meta">${phase.completedCount}/${phase.totalCount} · ${statusLabel(phase.status)}</p>
    </div>
  `;
}

function renderNextActions(source) {
  document.querySelector("#now-title").textContent = source
    ? `${source.name} 下一步`
    : "下一步";
  const panel = document.querySelector("#next-actions");
  if (!source || source.error) {
    panel.innerHTML = emptyState(source ? source.error : "暂无选中项目。");
    return;
  }
  if (!source.nextActions.length) {
    panel.innerHTML = emptyState("暂无下一步任务。");
    return;
  }
  panel.innerHTML = `
    <div class="next-list">
      ${source.nextActions.map((task) => taskItem(task, "next-item")).join("")}
    </div>
  `;
}

function renderTaskBoard(source) {
  document.querySelector("#task-title").textContent = source
    ? `${source.name} 优先级任务板`
    : "优先级任务板";
  const board = document.querySelector("#task-columns");
  if (!source || source.error) {
    board.innerHTML = `<div>${emptyState(source ? source.error : "暂无选中项目。")}</div>`;
    return;
  }
  board.innerHTML = ["P0", "P1", "P2"].map((label) => taskColumn(source, label)).join("");
}

function taskColumn(source, label) {
  const tasks = source.tasks.filter((task) => task.priorityLabel === label);
  const items = tasks.length
    ? tasks.map((task) => taskItem(task, "task-item")).join("")
    : emptyState("暂无任务。");
  return `
    <section class="task-column">
      <h3>${label} <span class="task-count">${tasks.length}</span></h3>
      <div class="task-list">${items}</div>
    </section>
  `;
}

function taskItem(task, className) {
  const meta = task.priorityLabel
    ? `${task.priorityLabel} · 第 ${task.lineNumber} 行`
    : `第 ${task.lineNumber} 行`;
  return `
    <article class="${className}">
      <p>${escapeHtml(task.title)}</p>
      <span>${escapeHtml(meta)}</span>
    </article>
  `;
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

function selectedSource() {
  return dashboardState.sources.find((source) => source.id === selectedSourceId) || null;
}

function emptyState(message) {
  return `<p class="empty-state">${escapeHtml(message)}</p>`;
}

function statusLabel(status) {
  const labels = {
    complete: "已完成",
    current: "当前",
    in_progress: "进行中",
    not_started: "未开始",
    empty: "空阶段",
  };
  return labels[status] || status;
}

function statusClass(status) {
  return String(status || "unknown").replaceAll("_", "-").replace(/[^a-zA-Z0-9-]/g, "");
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
  refreshButton.textContent = isLoading ? "刷新中" : "刷新";
}

function renderError(error) {
  currentView = "home";
  homeView.hidden = false;
  projectView.hidden = true;
  document.querySelector("#last-updated").textContent = "加载失败";
  document.querySelector("#summary").innerHTML = "";
  document.querySelector("#source-grid").innerHTML = "";
  document.querySelector("#roadmap").innerHTML = emptyState(error.message);
  document.querySelector("#next-actions").innerHTML = emptyState(error.message);
  document.querySelector("#task-columns").innerHTML = "";
}
