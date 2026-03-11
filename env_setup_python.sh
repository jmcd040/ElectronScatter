#!/bin/bash
# ============================================
# ElectronScatter Python environment setup
# Rebuilds the virtual environment from scratch
# version: 3.0
# ============================================

set -e

echo ""
echo "======================================"
echo "ElectronScatter Python Environment Setup"
echo "======================================"
echo ""

# Move to the directory containing this script

cd "$(dirname "$0")"

echo "Working directory:"
pwd
echo ""

# Remove existing virtual environment

if [ -d "venv" ]; then
echo "Removing existing virtual environment..."
rm -rf venv
echo "Old venv removed."
echo ""
fi

# Create a new virtual environment

echo "Creating new virtual environment..."
python3 -m venv venv
echo "Virtual environment created."
echo ""

# Activate the virtual environment

echo "Activating virtual environment..."
source venv/bin/activate

# Verify correct python

echo "Using Python:"
which python
echo ""

# Upgrade pip inside the venv

echo "Upgrading pip..."
python -m pip install --upgrade pip
echo ""

# Install required packages

echo "Installing required packages..."
pip install numpy matplotlib
echo ""

echo "======================================"
echo "Environment setup complete."
echo ""
echo "To activate the environment later:"
echo "    source venv/bin/activate"
echo ""
echo "To run the simulation:"
echo "    python main.py"
echo "======================================"
