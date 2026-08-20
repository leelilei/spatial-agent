#!/bin/bash
# 环境安装脚本
# 用法: bash scripts/setup_env.sh

set -e

echo "Creating virtual environment..."
python -m venv .venv
source .venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Environment setup complete!"
echo "Activate with: source .venv/bin/activate"
