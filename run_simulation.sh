#!/usr/bin/env bash

# ============================================
# Relativistic Two-Electron Scattering Runner
# ============================================

set -e

echo "----------------------------------------"
echo "Relativistic Two-Electron Simulator"
echo "----------------------------------------"
echo

# Ensure script runs from its own directory
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_DIR"

# Ensure python3 exists
if ! command -v python3 >/dev/null 2>&1; then
    echo "ERROR: python3 is not installed."
    read -p "Press Enter to close..."
    exit 1
fi

# Create virtual environment if missing
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
    echo
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo

# Ensure pip exists
python -m ensurepip --upgrade >/dev/null 2>&1

# Check and install required packages
echo "Checking Python dependencies..."

python - <<EOF
import sys
missing = []

try:
    import numpy
except ImportError:
    missing.append("numpy")

try:
    import matplotlib
except ImportError:
    missing.append("matplotlib")

if missing:
    print("Installing missing packages:", ", ".join(missing))
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing)
EOF

echo
echo "Launching simulation..."
echo

python main.py

echo
echo "Simulation finished."
read -p "Press Enter to close..."#!/usr/bin/env bash

# ============================================
# Relativistic Two-Electron Scattering Runner
# ============================================

set -e

echo "----------------------------------------"
echo "Relativistic Two-Electron Simulator"
echo "----------------------------------------"
echo

# Ensure script runs from its own directory
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_DIR"

# Ensure python3 exists
if ! command -v python3 >/dev/null 2>&1; then
    echo "ERROR: python3 is not installed."
    read -p "Press Enter to close..."
    exit 1
fi

# Create virtual environment if missing
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
    echo
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo

# Ensure pip exists
python -m ensurepip --upgrade >/dev/null 2>&1

# Check and install required packages
echo "Checking Python dependencies..."

python - <<EOF
import sys
missing = []

try:
    import numpy
except ImportError:
    missing.append("numpy")

try:
    import matplotlib
except ImportError:
    missing.append("matplotlib")

if missing:
    print("Installing missing packages:", ", ".join(missing))
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing)
EOF

echo
echo "Launching simulation..."
echo

python main.py

echo
echo "Simulation finished."
read -p "Press Enter to close..."