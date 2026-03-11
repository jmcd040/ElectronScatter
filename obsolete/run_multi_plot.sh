#!/usr/bin/env bash

# ============================================
# Electron Scattering Multi-Run Plot Launcher
# ============================================

echo "----------------------------------------"
echo "Electron Scattering Multi-Run Plot"
echo "----------------------------------------"
echo

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
    echo
fi

# Check required Python modules
python3 - <<EOF
import sys
try:
    import numpy
    import matplotlib
except ImportError as e:
    print("Missing Python dependency:", e)
    sys.exit(1)
EOF

echo "Launching plot generator..."
echo

python3 multi_run_plot.py

echo
echo "Plot program finished."