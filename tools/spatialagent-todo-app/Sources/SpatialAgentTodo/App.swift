import SwiftUI
import Foundation
import AppKit

private let defaultTodoPath = "/Users/mac/Documents/6-Research/1-SpatialAgent/docs/guides/todolist.md"
private let personalTodoDir = "/Users/mac/Documents/1-ProjectRes/Personal Todo"
private let sourcesConfigPath = "\(personalTodoDir)/sources.json"

private enum DashboardTab: String, CaseIterable, Identifiable {
    case overview = "Overview"
    case board = "Board"
    case timeline = "Timeline"
    case charts = "Charts"

    var id: String { rawValue }
}

private struct SourceFile: Codable {
    var sources: [TodoSourceConfig]
}

private struct TodoSourceConfig: Codable, Identifiable, Hashable {
    var id: String
    var name: String
    var path: String
    var accent: String
    var enabled: Bool
}

private struct TodoSourceState: Identifiable, Hashable {
    let config: TodoSourceConfig
    let document: TodoDocument?
    let errorMessage: String?

    var id: String { config.id }
    var tasks: [TodoItem] { document?.tasks ?? [] }
    var updateDate: Date? { document?.updateDate }
    var statusLine: String { document?.statusLine ?? "无法读取 todo 源文件。" }
    var openCount: Int { tasks.count }
    var p0Count: Int { tasks.filter { $0.priorityLabel == "P0" }.count }
}

private struct TodoItem: Identifiable, Hashable {
    let id: String
    let title: String
    let rawTitle: String
    let priorityLabel: String
    let priorityName: String
    let priorityValue: Int
    let headingPath: [String]
    let dueDate: Date?
    let isFlagged: Bool
    let lineNumber: Int
    let sourceID: String
    let sourceName: String
    let sourceAccent: String
}

private struct TodoDocument: Hashable {
    let updateDate: Date?
    let statusLine: String
    let tasks: [TodoItem]
    let completedCount: Int
}

private struct PriorityGroup: Identifiable, Hashable {
    let label: String
    let name: String
    let dueDate: Date?
    let tasks: [TodoItem]

    var id: String { label }
}

@MainActor
private final class TodoStore: ObservableObject {
    static let shared = TodoStore()

    @Published private(set) var sources: [TodoSourceState] = []
    @Published private(set) var lastRefresh: Date?
    @Published var selectedSourceID: String = "all"

    private var refreshTimer: Timer?

    init() {
        reload()
        refreshTimer = Timer.scheduledTimer(withTimeInterval: 300, repeats: true) { [weak self] _ in
            Task { @MainActor in
                self?.reload()
            }
        }
    }

    var enabledSourceCount: Int {
        sources.count
    }

    var allTasks: [TodoItem] {
        sources.flatMap(\.tasks).sorted(by: sortTasks)
    }

    var filteredTasks: [TodoItem] {
        if selectedSourceID == "all" {
            return allTasks
        }
        return allTasks.filter { $0.sourceID == selectedSourceID }
    }

    var totalP0Count: Int {
        allTasks.filter { $0.priorityLabel == "P0" }.count
    }

    var menuTitle: String {
        "P0 \(totalP0Count)"
    }

    var latestUpdateDate: Date? {
        sources.compactMap(\.updateDate).max()
    }

    var errorCount: Int {
        sources.filter { $0.errorMessage != nil }.count
    }

    var selectedSourceName: String {
        if selectedSourceID == "all" {
            return "All Lists"
        }
        return sources.first { $0.id == selectedSourceID }?.config.name ?? "Selected List"
    }

    func reload() {
        do {
            let configs = try loadOrCreateConfigs()
            sources = configs.filter(\.enabled).map { config in
                do {
                    let document = try TodoParser.load(config: config)
                    return TodoSourceState(config: config, document: document, errorMessage: nil)
                } catch {
                    return TodoSourceState(config: config, document: nil, errorMessage: error.localizedDescription)
                }
            }
            if selectedSourceID != "all", !sources.contains(where: { $0.id == selectedSourceID }) {
                selectedSourceID = "all"
            }
            lastRefresh = Date()
        } catch {
            sources = [
                TodoSourceState(
                    config: defaultSourceConfig,
                    document: nil,
                    errorMessage: error.localizedDescription
                )
            ]
            selectedSourceID = "all"
            lastRefresh = Date()
        }
    }

    func priorityGroups(for tasks: [TodoItem]? = nil) -> [PriorityGroup] {
        let labels = ["P0", "P1", "P2", "P3", "P4"]
        let sourceTasks = tasks ?? filteredTasks
        return labels.map { label in
            let groupTasks = sourceTasks.filter { $0.priorityLabel == label }.sorted(by: sortTasks)
            let name = groupTasks.first?.priorityName ?? priorityFallbackName(label)
            let dueDate = groupTasks.compactMap(\.dueDate).min()
            return PriorityGroup(label: label, name: name, dueDate: dueDate, tasks: groupTasks)
        }
    }

    func tasks(for priorityLabel: String, limit: Int? = nil) -> [TodoItem] {
        let tasks = allTasks.filter { $0.priorityLabel == priorityLabel }.sorted(by: sortTasks)
        if let limit {
            return Array(tasks.prefix(limit))
        }
        return tasks
    }

    private func loadOrCreateConfigs() throws -> [TodoSourceConfig] {
        let configURL = URL(fileURLWithPath: sourcesConfigPath)
        let directoryURL = URL(fileURLWithPath: personalTodoDir)
        try FileManager.default.createDirectory(at: directoryURL, withIntermediateDirectories: true)

        if !FileManager.default.fileExists(atPath: configURL.path) {
            let sourceFile = SourceFile(sources: [defaultSourceConfig])
            let data = try JSONEncoder.pretty.encode(sourceFile)
            try data.write(to: configURL)
        }

        let data = try Data(contentsOf: configURL)
        let sourceFile = try JSONDecoder().decode(SourceFile.self, from: data)
        if sourceFile.sources.isEmpty {
            return [defaultSourceConfig]
        }
        return sourceFile.sources
    }
}

@MainActor
private final class DashboardWindowController {
    static let shared = DashboardWindowController()

    private var window: NSWindow?

    func show(store: TodoStore) {
        if window == nil {
            let hostingController = NSHostingController(rootView: DashboardView(store: store))
            let dashboardWindow = NSWindow(contentViewController: hostingController)
            dashboardWindow.title = "SpatialAgent Todo"
            dashboardWindow.setContentSize(NSSize(width: 1220, height: 820))
            dashboardWindow.minSize = NSSize(width: 1080, height: 720)
            dashboardWindow.styleMask = [.titled, .closable, .miniaturizable, .resizable, .fullSizeContentView]
            dashboardWindow.titlebarAppearsTransparent = true
            dashboardWindow.isReleasedWhenClosed = false
            dashboardWindow.center()
            window = dashboardWindow
        }

        window?.makeKeyAndOrderFront(nil)
        NSApp.activate(ignoringOtherApps: true)
    }
}

private final class AppDelegate: NSObject, NSApplicationDelegate {
    func applicationDidFinishLaunching(_ notification: Notification) {
        NSApp.setActivationPolicy(.regular)
        Task { @MainActor in
            DashboardWindowController.shared.show(store: TodoStore.shared)
        }
    }

    func applicationShouldHandleReopen(_ sender: NSApplication, hasVisibleWindows flag: Bool) -> Bool {
        Task { @MainActor in
            DashboardWindowController.shared.show(store: TodoStore.shared)
        }
        return true
    }
}

private let defaultSourceConfig = TodoSourceConfig(
    id: "spatialagent-survey",
    name: "SpatialAgent Survey",
    path: defaultTodoPath,
    accent: "#0071e3",
    enabled: true
)

private extension JSONEncoder {
    static var pretty: JSONEncoder {
        let encoder = JSONEncoder()
        encoder.outputFormatting = [.prettyPrinted, .sortedKeys, .withoutEscapingSlashes]
        return encoder
    }
}

private enum TodoParser {
    static func load(config: TodoSourceConfig) throws -> TodoDocument {
        let content = try String(contentsOfFile: config.path, encoding: .utf8)
        return parse(content, config: config)
    }

    static func parse(_ content: String, config: TodoSourceConfig) -> TodoDocument {
        var headings: [Int: String] = [:]
        var updateDate: Date?
        var statusLine = "读取当前 todo。"
        var activeTasks: [TodoItem] = []
        var fallbackTasks: [TodoItem] = []
        var completedCount = 0

        let lines = content.components(separatedBy: .newlines)
        for (index, line) in lines.enumerated() {
            if updateDate == nil, line.contains("更新日期") {
                updateDate = parseDate(from: line)
            }

            if line.contains("当前主线") {
                statusLine = cleanMarkdownText(textAfterColon(line))
            }

            if let heading = parseHeading(line) {
                headings[heading.level] = heading.text
                for key in Array(headings.keys) where key > heading.level {
                    headings.removeValue(forKey: key)
                }
                continue
            }

            guard let task = parseTask(line) else {
                continue
            }

            let headingPath = headings.keys.sorted().compactMap { headings[$0] }
            guard !headingPath.contains(where: { $0.contains("暂不做") }) else {
                continue
            }

            if task.checked {
                completedCount += 1
                continue
            }

            let priority = priorityInfo(from: headingPath)
            let cleanTitle = cleanMarkdownText(task.title)
            let stableID = makeStableID(sourceID: config.id, headingPath: headingPath, rawTitle: cleanTitle)
            let item = TodoItem(
                id: stableID,
                title: "[\(priority.label)] \(cleanTitle)",
                rawTitle: cleanTitle,
                priorityLabel: priority.label,
                priorityName: priority.name,
                priorityValue: priority.value,
                headingPath: headingPath,
                dueDate: dueDate(updateDate: updateDate, priorityLabel: priority.label),
                isFlagged: priority.label == "P0",
                lineNumber: index + 1,
                sourceID: config.id,
                sourceName: config.name,
                sourceAccent: config.accent
            )

            if headingPath.contains("执行优先级") {
                activeTasks.append(item)
            } else {
                fallbackTasks.append(item)
            }
        }

        let chosenTasks = activeTasks.isEmpty ? fallbackTasks : activeTasks
        return TodoDocument(
            updateDate: updateDate,
            statusLine: statusLine,
            tasks: chosenTasks.sorted(by: sortTasks),
            completedCount: completedCount
        )
    }

    private static func parseHeading(_ line: String) -> (level: Int, text: String)? {
        let trimmed = line.trimmingCharacters(in: .whitespaces)
        guard trimmed.hasPrefix("#") else { return nil }
        let level = trimmed.prefix { $0 == "#" }.count
        guard level > 0, trimmed.count > level else { return nil }
        let text = String(trimmed.dropFirst(level)).trimmingCharacters(in: .whitespaces)
        return (level, cleanMarkdownText(text))
    }

    private static func parseTask(_ line: String) -> (checked: Bool, title: String)? {
        let trimmed = line.trimmingCharacters(in: .whitespaces)
        if trimmed.hasPrefix("- [ ] ") {
            return (false, String(trimmed.dropFirst(6)))
        }
        if trimmed.hasPrefix("- [x] ") || trimmed.hasPrefix("- [X] ") {
            return (true, String(trimmed.dropFirst(6)))
        }
        return nil
    }

    private static func priorityInfo(from headingPath: [String]) -> (label: String, name: String, value: Int) {
        for heading in headingPath.reversed() {
            guard heading.lowercased().hasPrefix("priority") else { continue }
            let priorityNumber = firstCapture(pattern: #"Priority\s*(\d+)"#, in: heading).flatMap(Int.init) ?? 9
            let label = "P\(priorityNumber)"
            let name: String
            if let colon = heading.firstIndex(of: "：") {
                name = String(heading[heading.index(after: colon)...]).trimmingCharacters(in: .whitespaces)
            } else if let colon = heading.firstIndex(of: ":") {
                name = String(heading[heading.index(after: colon)...]).trimmingCharacters(in: .whitespaces)
            } else {
                name = heading
            }
            let value = priorityNumber == 0 ? 1 : (priorityNumber == 1 ? 5 : 9)
            return (label, name, value)
        }
        return ("P4", "General Tasks", 9)
    }

    private static func dueDate(updateDate: Date?, priorityLabel: String) -> Date? {
        let baseDate = updateDate ?? Calendar.current.startOfDay(for: Date())
        let offset: Int
        switch priorityLabel {
        case "P0": offset = 1
        case "P1": offset = 2
        case "P2": offset = 3
        case "P3": offset = 4
        default: offset = 5
        }
        return Calendar.current.date(byAdding: .day, value: offset, to: baseDate)
    }

    private static func parseDate(from line: String) -> Date? {
        guard let value = firstCapture(pattern: #"(\d{4}-\d{2}-\d{2})"#, in: line) else { return nil }
        let formatter = DateFormatter()
        formatter.calendar = Calendar(identifier: .gregorian)
        formatter.locale = Locale(identifier: "en_US_POSIX")
        formatter.dateFormat = "yyyy-MM-dd"
        return formatter.date(from: value)
    }

    private static func firstCapture(pattern: String, in text: String) -> String? {
        guard let regex = try? NSRegularExpression(pattern: pattern) else { return nil }
        let range = NSRange(text.startIndex..<text.endIndex, in: text)
        guard let match = regex.firstMatch(in: text, range: range), match.numberOfRanges > 1 else { return nil }
        guard let captureRange = Range(match.range(at: 1), in: text) else { return nil }
        return String(text[captureRange])
    }

    private static func textAfterColon(_ line: String) -> String {
        if let colon = line.firstIndex(of: "：") {
            return String(line[line.index(after: colon)...])
        }
        if let colon = line.firstIndex(of: ":") {
            return String(line[line.index(after: colon)...])
        }
        return line
    }

    private static func cleanMarkdownText(_ text: String) -> String {
        var result = text
        result = result.replacingOccurrences(of: #"`([^`]+)`"#, with: "$1", options: .regularExpression)
        result = result.replacingOccurrences(of: #"\[([^\]]+)\]\([^)]+\)"#, with: "$1", options: .regularExpression)
        result = result.replacingOccurrences(of: #"\*\*([^*]+)\*\*"#, with: "$1", options: .regularExpression)
        result = result.replacingOccurrences(of: #"^\s*>\s*"#, with: "", options: .regularExpression)
        return result.replacingOccurrences(of: #"\s+"#, with: " ", options: .regularExpression)
            .trimmingCharacters(in: .whitespacesAndNewlines)
    }

    private static func makeStableID(sourceID: String, headingPath: [String], rawTitle: String) -> String {
        let key = (sourceID + "\n" + headingPath.joined(separator: "/") + "\n" + rawTitle)
        var hash: UInt64 = 14695981039346656037
        for byte in key.utf8 {
            hash ^= UInt64(byte)
            hash = hash &* 1099511628211
        }
        return String(format: "todo-%016llx", hash)
    }
}

private enum AppleTheme {
    static let black = Color.black
    static let nearBlack = Color(red: 0.114, green: 0.114, blue: 0.122)
    static let lightGray = Color(red: 0.961, green: 0.961, blue: 0.969)
    static let blue = Color(red: 0.0, green: 0.443, blue: 0.890)
    static let secondaryText = Color.black.opacity(0.58)
}

@main
struct SpatialAgentTodoApp: App {
    @NSApplicationDelegateAdaptor(AppDelegate.self) private var appDelegate
    @StateObject private var store = TodoStore.shared

    var body: some Scene {
        MenuBarExtra(store.menuTitle, systemImage: store.totalP0Count > 0 ? "flag.fill" : "checklist") {
            MenuBarPanel(store: store)
        }

        Settings {
            EmptyView()
        }
    }
}

private struct MenuBarPanel: View {
    @ObservedObject var store: TodoStore

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack {
                Label("P0 \(store.totalP0Count)", systemImage: "flag.fill")
                    .font(.headline)
                Spacer()
                Text("\(store.allTasks.count) open")
                    .foregroundStyle(.secondary)
            }

            Divider()

            if store.sources.isEmpty {
                Text("No sources loaded.")
                    .foregroundStyle(.secondary)
            } else {
                ForEach(store.sources) { source in
                    HStack {
                        SourceDot(hex: source.config.accent)
                        Text(source.config.name)
                        Spacer()
                        Text("P0 \(source.p0Count)")
                            .foregroundStyle(source.p0Count > 0 ? AppleTheme.blue : .secondary)
                    }
                }
            }

            let urgentTasks = store.tasks(for: "P0", limit: 5)
            if !urgentTasks.isEmpty {
                Divider()
                ForEach(urgentTasks) { task in
                    VStack(alignment: .leading, spacing: 2) {
                        Text(task.rawTitle)
                            .lineLimit(2)
                        Text(task.sourceName)
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                }
            }

            Divider()

            Button("Open Dashboard") {
                DashboardWindowController.shared.show(store: store)
            }
            Button("Refresh") {
                store.reload()
            }
            Button("Quit") {
                NSApplication.shared.terminate(nil)
            }
        }
        .padding(12)
        .frame(width: 360)
    }
}

private struct DashboardView: View {
    @ObservedObject var store: TodoStore
    @State private var selectedTab: DashboardTab = .overview

    var body: some View {
        VStack(spacing: 0) {
            navBar
            ScrollView {
                VStack(spacing: 0) {
                    heroSection
                    controlStrip
                    contentSection
                }
            }
            .background(AppleTheme.lightGray)
        }
        .background(AppleTheme.black)
    }

    private var navBar: some View {
        HStack(spacing: 18) {
            Text("SpatialAgent Todo")
                .font(.system(size: 12, weight: .regular))
                .foregroundStyle(.white)
            Spacer()
            Text("\(store.enabledSourceCount) sources · \(formattedTime(store.lastRefresh, fallback: "--"))")
                .font(.system(size: 12, weight: .regular))
                .foregroundStyle(.white.opacity(0.72))
                .lineLimit(1)
            Button(action: store.reload) {
                Text("Refresh")
                    .font(.system(size: 12, weight: .regular))
                    .foregroundStyle(AppleTheme.blue)
            }
            .buttonStyle(.plain)
        }
        .padding(.horizontal, 28)
        .frame(height: 48)
        .background(.black.opacity(0.82))
    }

    private var heroSection: some View {
        VStack(spacing: 24) {
            VStack(spacing: 10) {
                Text("Todo Dashboard")
                    .font(.system(size: 56, weight: .semibold))
                    .lineSpacing(-2)
                    .foregroundStyle(.white)
                Text("多个 markdown todo 的常驻观察面板。")
                    .font(.system(size: 21, weight: .regular))
                    .foregroundStyle(.white.opacity(0.82))
                    .multilineTextAlignment(.center)
            }

            HStack(spacing: 12) {
                HeroMetric(icon: "checklist", title: "Open Tasks", value: "\(store.filteredTasks.count)")
                HeroMetric(icon: "flag.fill", title: "Urgent P0", value: "\(store.filteredTasks.filter { $0.priorityLabel == "P0" }.count)")
                HeroMetric(icon: "folder", title: "Sources", value: "\(store.enabledSourceCount)")
                HeroMetric(icon: "exclamationmark.triangle", title: "Errors", value: "\(store.errorCount)")
            }
            .frame(maxWidth: 920)

            if store.errorCount > 0 {
                Text("Some sources could not be read. Check Sources in Overview.")
                    .font(.system(size: 14, weight: .regular))
                    .foregroundStyle(Color(red: 1.0, green: 0.55, blue: 0.45))
            }
        }
        .padding(.top, 64)
        .padding(.bottom, 58)
        .frame(maxWidth: .infinity)
        .background(AppleTheme.black)
    }

    private var controlStrip: some View {
        HStack(spacing: 18) {
            Picker("Source", selection: $store.selectedSourceID) {
                Text("All Lists").tag("all")
                ForEach(store.sources) { source in
                    Text(source.config.name).tag(source.config.id)
                }
            }
            .pickerStyle(.menu)
            .frame(width: 220)

            Picker("View", selection: $selectedTab) {
                ForEach(DashboardTab.allCases) { tab in
                    Text(tab.rawValue).tag(tab)
                }
            }
            .pickerStyle(.segmented)
            .frame(width: 480)
        }
        .padding(.top, 28)
        .padding(.bottom, 18)
    }

    @ViewBuilder
    private var contentSection: some View {
        VStack(spacing: 22) {
            switch selectedTab {
            case .overview:
                OverviewView(store: store)
            case .board:
                BoardView(groups: store.priorityGroups())
            case .timeline:
                TimelineView(tasks: store.filteredTasks)
            case .charts:
                ChartsView(store: store)
            }
        }
        .padding(.horizontal, 32)
        .padding(.bottom, 48)
        .frame(maxWidth: 1180)
        .frame(maxWidth: .infinity)
    }
}

private struct HeroMetric: View {
    let icon: String
    let title: String
    let value: String

    var body: some View {
        VStack(spacing: 7) {
            Image(systemName: icon)
                .font(.system(size: 18, weight: .semibold))
                .foregroundStyle(AppleTheme.blue)
            Text(value)
                .font(.system(size: 28, weight: .semibold))
                .foregroundStyle(.white)
                .lineLimit(1)
                .minimumScaleFactor(0.7)
            Text(title)
                .font(.system(size: 12, weight: .regular))
                .foregroundStyle(.white.opacity(0.62))
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, 18)
        .background(Color.white.opacity(0.08))
        .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))
    }
}

private struct OverviewView: View {
    @ObservedObject var store: TodoStore

    var body: some View {
        VStack(spacing: 18) {
            HStack(spacing: 14) {
                SummaryCard(icon: "flag.fill", title: "Immediate Focus", value: "\(count("P0"))", caption: "urgent items")
                SummaryCard(icon: "chart.bar.fill", title: "Evidence Map", value: "\(count("P1"))", caption: "synthesis tasks")
                SummaryCard(icon: "clock.fill", title: "Later Work", value: "\(count("P2") + count("P3") + count("P4"))", caption: "queued items")
            }

            HStack(alignment: .top, spacing: 18) {
                VStack(alignment: .leading, spacing: 14) {
                    SectionHeader(title: "Current P0 Blockers", subtitle: "Across \(store.selectedSourceName).")
                    ForEach(store.filteredTasks.filter { $0.priorityLabel == "P0" }) { task in
                        TodoRow(item: task)
                    }
                    if store.filteredTasks.filter({ $0.priorityLabel == "P0" }).isEmpty {
                        EmptyHint(text: "No urgent tasks in this view.")
                    }
                }
                .padding(22)
                .frame(maxWidth: .infinity, alignment: .topLeading)
                .background(.white)
                .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))

                VStack(alignment: .leading, spacing: 14) {
                    SectionHeader(title: "Sources", subtitle: "Configured in sources.json.")
                    ForEach(store.sources) { source in
                        SourceRow(source: source)
                    }
                }
                .padding(22)
                .frame(width: 340, alignment: .topLeading)
                .background(.white)
                .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))
            }
        }
    }

    private func count(_ label: String) -> Int {
        store.filteredTasks.filter { $0.priorityLabel == label }.count
    }
}

private struct BoardView: View {
    let groups: [PriorityGroup]

    var body: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(alignment: .top, spacing: 14) {
                ForEach(groups) { group in
                    PriorityColumn(group: group)
                }
            }
            .padding(.vertical, 4)
        }
    }
}

private struct TimelineView: View {
    let tasks: [TodoItem]

    private var groupedTasks: [(date: Date, tasks: [TodoItem])] {
        let dated = Dictionary(grouping: tasks.compactMap { item -> (Date, TodoItem)? in
            guard let dueDate = item.dueDate else { return nil }
            return (Calendar.current.startOfDay(for: dueDate), item)
        }, by: { $0.0 })
        return dated.keys.sorted().map { date in
            (date, dated[date]?.map(\.1).sorted(by: sortTasks) ?? [])
        }
    }

    var body: some View {
        VStack(spacing: 14) {
            ForEach(groupedTasks, id: \.date) { group in
                VStack(alignment: .leading, spacing: 14) {
                    HStack {
                        Text(formattedDate(group.date, fallback: "No date"))
                            .font(.system(size: 21, weight: .semibold))
                            .foregroundStyle(AppleTheme.nearBlack)
                        Spacer()
                        Text("\(group.tasks.count) tasks")
                            .font(.system(size: 14, weight: .regular))
                            .foregroundStyle(AppleTheme.secondaryText)
                    }
                    ForEach(group.tasks) { task in
                        TodoRow(item: task)
                    }
                }
                .padding(22)
                .background(.white)
                .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))
            }
        }
    }
}

private struct ChartsView: View {
    @ObservedObject var store: TodoStore

    private var groups: [PriorityGroup] {
        store.priorityGroups()
    }

    var body: some View {
        VStack(spacing: 18) {
            VStack(alignment: .leading, spacing: 18) {
                SectionHeader(title: "Priority Distribution", subtitle: "Counts and share by P0-P4.")
                PriorityBars(groups: groups)
            }
            .padding(22)
            .background(.white)
            .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))

            VStack(alignment: .leading, spacing: 14) {
                SectionHeader(title: "Source Comparison", subtitle: "Open and urgent tasks by list.")
                ForEach(store.sources) { source in
                    SourceRow(source: source)
                }
            }
            .padding(22)
            .background(.white)
            .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))
        }
    }
}

private struct PriorityBars: View {
    let groups: [PriorityGroup]

    private var maxCount: Int {
        max(groups.map { $0.tasks.count }.max() ?? 1, 1)
    }

    private var total: Int {
        max(groups.map { $0.tasks.count }.reduce(0, +), 1)
    }

    var body: some View {
        VStack(spacing: 12) {
            ForEach(groups) { group in
                let count = group.tasks.count
                let share = Double(count) / Double(total)
                HStack(spacing: 12) {
                    Text(group.label)
                        .font(.system(size: 17, weight: .semibold))
                        .frame(width: 44, alignment: .leading)
                    GeometryReader { proxy in
                        ZStack(alignment: .leading) {
                            Capsule()
                                .fill(AppleTheme.lightGray)
                            Capsule()
                                .fill(group.label == "P0" ? AppleTheme.blue : AppleTheme.nearBlack.opacity(0.72))
                                .frame(width: max(6, proxy.size.width * CGFloat(count) / CGFloat(maxCount)))
                        }
                    }
                    .frame(height: 18)
                    Text("\(count)")
                        .font(.system(size: 17, weight: .semibold))
                        .frame(width: 36, alignment: .trailing)
                    Text(percentFormatter.string(from: NSNumber(value: share)) ?? "0%")
                        .font(.system(size: 12, weight: .regular))
                        .foregroundStyle(AppleTheme.secondaryText)
                        .frame(width: 54, alignment: .trailing)
                }
            }
        }
    }
}

private struct PriorityColumn: View {
    let group: PriorityGroup

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack(alignment: .firstTextBaseline) {
                VStack(alignment: .leading, spacing: 4) {
                    Text(group.label)
                        .font(.system(size: 28, weight: .semibold))
                        .foregroundStyle(group.label == "P0" ? AppleTheme.blue : AppleTheme.nearBlack)
                    Text(group.name)
                        .font(.system(size: 13, weight: .regular))
                        .foregroundStyle(AppleTheme.secondaryText)
                        .lineLimit(2)
                }
                Spacer()
                Text("\(group.tasks.count)")
                    .font(.system(size: 14, weight: .semibold))
                    .foregroundStyle(.white)
                    .padding(.horizontal, 10)
                    .padding(.vertical, 4)
                    .background(group.label == "P0" ? AppleTheme.blue : AppleTheme.nearBlack.opacity(0.72))
                    .clipShape(Capsule())
            }

            Text(formattedDate(group.dueDate, fallback: "No date"))
                .font(.system(size: 12, weight: .regular))
                .foregroundStyle(AppleTheme.secondaryText)

            if group.tasks.isEmpty {
                EmptyHint(text: "No tasks.")
            } else {
                ForEach(group.tasks) { task in
                    TodoCard(item: task)
                }
            }
        }
        .padding(18)
        .frame(width: 278, alignment: .top)
        .background(.white)
        .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))
    }
}

private struct TodoCard: View {
    let item: TodoItem

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            HStack(spacing: 6) {
                SourceDot(hex: item.sourceAccent)
                Text(item.sourceName)
                    .font(.system(size: 10, weight: .semibold))
                    .foregroundStyle(AppleTheme.nearBlack.opacity(0.72))
                    .lineLimit(1)
                if item.isFlagged {
                    Image(systemName: "flag.fill")
                        .font(.system(size: 10, weight: .semibold))
                        .foregroundStyle(AppleTheme.blue)
                }
                Spacer()
                Image(systemName: priorityIcon(item.priorityValue))
                    .font(.system(size: 12, weight: .semibold))
                    .foregroundStyle(item.priorityValue == 1 ? AppleTheme.blue : AppleTheme.secondaryText)
            }

            Text(item.title)
                .font(.system(size: 14, weight: .semibold))
                .foregroundStyle(AppleTheme.nearBlack)
                .lineLimit(4)
                .fixedSize(horizontal: false, vertical: true)
        }
        .padding(14)
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(AppleTheme.lightGray)
        .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))
    }
}

private struct TodoRow: View {
    let item: TodoItem

    var body: some View {
        HStack(spacing: 12) {
            SourceDot(hex: item.sourceAccent)
            VStack(alignment: .leading, spacing: 3) {
                Text(item.title)
                    .font(.system(size: 17, weight: .semibold))
                    .foregroundStyle(AppleTheme.nearBlack)
                    .lineLimit(2)
                Text("\(item.sourceName) · \(item.priorityName) · \(formattedDate(item.dueDate, fallback: "No date"))")
                    .font(.system(size: 12, weight: .regular))
                    .foregroundStyle(AppleTheme.secondaryText)
            }
            Spacer()
            Image(systemName: item.isFlagged ? "flag.fill" : priorityIcon(item.priorityValue))
                .foregroundStyle(item.priorityValue == 1 ? AppleTheme.blue : AppleTheme.secondaryText)
        }
        .padding(.vertical, 8)
    }
}

private struct SummaryCard: View {
    let icon: String
    let title: String
    let value: String
    let caption: String

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            HStack {
                Image(systemName: icon)
                    .foregroundStyle(AppleTheme.blue)
                Text(title)
                    .font(.system(size: 14, weight: .semibold))
                    .foregroundStyle(AppleTheme.secondaryText)
            }
            Text(value)
                .font(.system(size: 40, weight: .semibold))
                .foregroundStyle(AppleTheme.nearBlack)
            Text(caption)
                .font(.system(size: 14, weight: .regular))
                .foregroundStyle(AppleTheme.secondaryText)
        }
        .padding(22)
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(.white)
        .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))
    }
}

private struct SourceRow: View {
    let source: TodoSourceState

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack {
                SourceDot(hex: source.config.accent)
                Text(source.config.name)
                    .font(.system(size: 14, weight: .semibold))
                    .lineLimit(1)
                Spacer()
                Text("\(source.openCount) open")
                    .font(.system(size: 12, weight: .regular))
                    .foregroundStyle(AppleTheme.secondaryText)
                Text("P0 \(source.p0Count)")
                    .font(.system(size: 12, weight: .semibold))
                    .foregroundStyle(source.p0Count > 0 ? AppleTheme.blue : AppleTheme.secondaryText)
            }
            if let error = source.errorMessage {
                Text(error)
                    .font(.system(size: 12, weight: .regular))
                    .foregroundStyle(Color(red: 0.82, green: 0.18, blue: 0.14))
                    .lineLimit(2)
            } else {
                Text(source.config.path)
                    .font(.system(size: 11, weight: .regular))
                    .foregroundStyle(AppleTheme.secondaryText)
                    .lineLimit(1)
                    .truncationMode(.middle)
            }
        }
        .padding(.vertical, 6)
    }
}

private struct SourceDot: View {
    let hex: String

    var body: some View {
        Circle()
            .fill(colorFromHex(hex) ?? AppleTheme.blue)
            .frame(width: 9, height: 9)
    }
}

private struct SectionHeader: View {
    let title: String
    let subtitle: String

    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            Text(title)
                .font(.system(size: 28, weight: .semibold))
                .foregroundStyle(AppleTheme.nearBlack)
            Text(subtitle)
                .font(.system(size: 14, weight: .regular))
                .foregroundStyle(AppleTheme.secondaryText)
        }
    }
}

private struct EmptyHint: View {
    let text: String

    var body: some View {
        Text(text)
            .font(.system(size: 14, weight: .regular))
            .foregroundStyle(AppleTheme.secondaryText)
            .frame(maxWidth: .infinity, alignment: .leading)
            .padding(14)
            .background(AppleTheme.lightGray)
            .clipShape(RoundedRectangle(cornerRadius: 8, style: .continuous))
    }
}

private let percentFormatter: NumberFormatter = {
    let formatter = NumberFormatter()
    formatter.numberStyle = .percent
    formatter.maximumFractionDigits = 0
    return formatter
}()

private func sortTasks(_ lhs: TodoItem, _ rhs: TodoItem) -> Bool {
    if lhs.priorityValue != rhs.priorityValue {
        return lhs.priorityValue < rhs.priorityValue
    }
    if lhs.sourceName != rhs.sourceName {
        return lhs.sourceName < rhs.sourceName
    }
    return lhs.lineNumber < rhs.lineNumber
}

private func priorityFallbackName(_ label: String) -> String {
    switch label {
    case "P0": return "Urgent"
    case "P1": return "Next"
    case "P2": return "Boundary Work"
    case "P3": return "Claim Check"
    case "P4": return "Maintenance"
    default: return "Todo"
    }
}

private func priorityIcon(_ priority: Int) -> String {
    switch priority {
    case 1:
        return "exclamationmark.circle.fill"
    case 5:
        return "circle.lefthalf.filled"
    default:
        return "circle"
    }
}

private func formattedDate(_ date: Date?, fallback: String) -> String {
    guard let date else { return fallback }
    let formatter = DateFormatter()
    formatter.locale = Locale(identifier: "zh_CN")
    formatter.dateFormat = "M月d日 EEEE"
    return formatter.string(from: date)
}

private func formattedTime(_ date: Date?, fallback: String) -> String {
    guard let date else { return fallback }
    let formatter = DateFormatter()
    formatter.locale = Locale(identifier: "zh_CN")
    formatter.dateFormat = "HH:mm"
    return formatter.string(from: date)
}

private func colorFromHex(_ hex: String) -> Color? {
    var value = hex.trimmingCharacters(in: .whitespacesAndNewlines)
    if value.hasPrefix("#") {
        value.removeFirst()
    }
    guard value.count == 6, let intValue = Int(value, radix: 16) else {
        return nil
    }
    let red = Double((intValue >> 16) & 0xff) / 255.0
    let green = Double((intValue >> 8) & 0xff) / 255.0
    let blue = Double(intValue & 0xff) / 255.0
    return Color(red: red, green: green, blue: blue)
}
