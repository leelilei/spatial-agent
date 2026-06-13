#!/bin/bash
# 双击我即可启动学习工作台（macOS）。
# 它会启动本地服务器并自动打开浏览器。关闭：回到本窗口按 Ctrl+C。
cd "$(dirname "$0")" || exit 1
echo "正在启动学习工作台…"
python3 server.py
