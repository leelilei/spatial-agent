#!/bin/bash
# 一键运行所有自动化实验
# 用法: bash experiments/run_all.sh

set -e

echo "=== Running Exp1: Spatial vs Baseline ==="
python experiments/run_exp1.py

echo "=== Running Exp2: Layout Comparison ==="
python experiments/run_exp2.py

echo "=== Running Exp3: Ablation Study ==="
python experiments/run_exp3.py

echo "=== Preparing Exp4: Human Evaluation Materials ==="
python experiments/run_exp4_prep.py

echo "=== All experiments completed ==="
