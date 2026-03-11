#!/usr/bin/env bash

# ============================================
# ElectronScatter Python Environment Setup
# Works on fresh Ubuntu or existing install
# ============================================

set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "----------------------------------------"
echo "ElectronScatter Python Environment Setup"
echo "----------------------------------------"
echo

cd "$PROJECT_DIR"

echo "Installing required Ubuntu packages..."
sudo apt update
sudo apt install -y \
    python3 \
    python3-venv \
    python3-pip \
    python3-tk \
    build-essential

echo
echo "Creating virtual environment..."

if [ ! -d "venv" ]; then
    python3 -m venv venv
else
    echo "venv already exists"
fi

echo
echo "Activating virtual environment..."
source venv/bin/activate

echo
echo "Upgrading pip..."
python -m pip install --upgrade pip

echo
echo "Installing Python dependencies..."
python -m pip install numpy matplotlib

echo
echo "Verifying Python environment..."

python <<EOF
import sys
import numpy
import matplotlib
print("Python version:", sys.version)
print("NumPy version:", numpy.__version__)
print("Matplotlib version:", matplotlib.__version__)
print("Matplotlib backend:", matplotlib.get_backend())
EOF

echo
echo "Testing matplotlib display..."

python <<EOF
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
plt.plot([1,2,3])
plt.title("Matplotlib test plot")
plt.show()
EOF

echo
echo "Environment setup complete."
echo

read -p "Press Enter to close..."