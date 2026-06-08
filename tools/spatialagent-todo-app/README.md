# SpatialAgent Todo App

Native macOS dashboard for `docs/guides/todolist.md`.

The app is a resident menu bar utility. It reads one or more markdown todo
files from:

```text
/Users/mac/Documents/1-ProjectRes/Personal Todo/sources.json
```

If the config file does not exist, the app creates it with the SpatialAgent
survey todo as the first source.

Build and install:

```bash
./tools/spatialagent-todo-app/build_app.sh
```

The script installs the app to:

```text
/Users/mac/Documents/1-ProjectRes/Personal Todo/SpatialAgent Todo.app
```
