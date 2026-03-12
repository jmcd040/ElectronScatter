#!/usr/bin/env bash

# ============================================
# ElectronScatter Run Script
# version 4.0
# ============================================

set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

cd "$PROJECT_DIR"

echo
echo "========================================"
echo "ElectronScatter Runner"
echo "========================================"
echo

# ------------------------------------------------
# Ensure virtual environment exists
# ------------------------------------------------

if [ ! -d "venv" ]; then
echo "Virtual environment not found."
echo "Running environment setup..."
echo
./env_setup_python.sh
fi

# ------------------------------------------------
# Activate virtual environment
# ------------------------------------------------

echo "Activating virtual environment..."
source venv/bin/activate

# ------------------------------------------------
# Verify correct Python is being used
# ------------------------------------------------

PYTHON_PATH=$(which python)

if [[ "$PYTHON_PATH" != *"/venv/bin/python"* ]]; then
echo "ERROR: venv activation failed."
echo "Python being used:"
echo "$PYTHON_PATH"
exit 1
fi

echo "Using Python:"
echo "$PYTHON_PATH"
echo

# ------------------------------------------------
# Optional quick environment check
# ------------------------------------------------

echo "Verifying environment..."
./env_check.sh quick

echo
echo "Running ElectronScatter simulation..."
echo

python main.py

echo
echo "Simulation finished."
echo
