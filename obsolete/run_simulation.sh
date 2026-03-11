#!/usr/bin/env bash

# ============================================
# Relativistic Two-Electron Scattering Runner
# ============================================

# Exit immediately if a command fails
set -e

echo "----------------------------------------"
echo "Relativistic Two-Electron Simulator"
echo "----------------------------------------"

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Check that required packages exist
python3 - <<EOF
import sys
try:
    import numpy
    import matplotlib
except ImportError as e:
    print("Missing dependency:", e)
    sys.exit(1)
EOF

echo "Launching simulation..."
echo

python3 main.py

echo
echo "Simulation finished."