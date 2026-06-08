#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_NAME="SpatialAgent Todo"
EXECUTABLE_NAME="SpatialAgentTodo"
BUILD_DIR="$SCRIPT_DIR/build"
APP_DIR="$BUILD_DIR/$APP_NAME.app"
INSTALL_DIR="/Users/mac/Documents/1-ProjectRes/Personal Todo"
MODULE_CACHE="/tmp/spatialagent_todo_swift_module_cache"

rm -rf "$APP_DIR"
mkdir -p "$APP_DIR/Contents/MacOS" "$APP_DIR/Contents/Resources" "$MODULE_CACHE"

cp "$SCRIPT_DIR/Info.plist" "$APP_DIR/Contents/Info.plist"

swiftc \
  -parse-as-library \
  -module-cache-path "$MODULE_CACHE" \
  "$SCRIPT_DIR/Sources/SpatialAgentTodo/App.swift" \
  -o "$APP_DIR/Contents/MacOS/$EXECUTABLE_NAME"

codesign --force --deep --sign - "$APP_DIR" >/dev/null

mkdir -p "$INSTALL_DIR"
rm -rf "$INSTALL_DIR/$APP_NAME.app"
cp -R "$APP_DIR" "$INSTALL_DIR/$APP_NAME.app"

echo "Installed: $INSTALL_DIR/$APP_NAME.app"
