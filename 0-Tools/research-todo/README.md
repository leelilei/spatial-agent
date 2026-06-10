# Research Todo

Deprecated: the primary visual dashboard is now:

```text
/Users/mac/Documents/6-Research/0-Tools/research-dashboard
```

Native macOS dashboard for research project todo files.

The app is a resident menu bar utility. It reads one or more markdown todo
files from:

```text
/Users/mac/Documents/1-ProjectRes/Personal Todo/sources.json
```

If the config file does not exist, the app creates it with default sources for
projects `1-SpatialAgent` through `4-SpatialAgent-Survey`. Each default source
uses `docs/guides/todolist.md` inside the project.

Build and install:

```bash
cd /Users/mac/Documents/6-Research/0-Tools/research-todo
./build_app.sh
```

The script installs the app to:

```text
/Users/mac/Documents/1-ProjectRes/Personal Todo/Research Todo.app
```
