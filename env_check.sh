#!/usr/bin/env bash

# ============================================
# ElectronScatter Environment Verification
# ============================================

set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "----------------------------------------"
echo "ElectronScatter Environment Check"
echo "----------------------------------------"
echo

cd "$PROJECT_DIR"

echo "Project directory:"
echo "$PROJECT_DIR"
echo

# Check Python
echo "Checking Python..."
if command -v python3 >/dev/null 2>&1; then
    echo "python3 found:"
    python3 --version
else
    echo "ERROR: python3 not installed"
    exit 1
fi

echo

# Check virtual environment
if [ -d "venv" ]; then
    echo "Virtual environment found."
else
    echo "WARNING: venv not found."
    echo "Run setup_python_env.sh first."
    exit 1
fi

echo

# Activate venv
echo "Activating virtual environment..."
source venv/bin/activate

echo
echo "Python being used:"
which python

echo
echo "Checking Python packages..."

python <<EOF
import sys

def check(pkg):
    try:
        module = __import__(pkg)
        print(f"{pkg} OK ({module.__version__})")
    except Exception as e:
        print(f"{pkg} MISSING:", e)
        sys.exit(1)

check("numpy")
check("matplotlib")

print()
import matplotlib
print("Matplotlib backend:", matplotlib.get_backend())
EOF

echo
echo "Checking DISPLAY variable..."
echo "DISPLAY=$DISPLAY"

echo

echo "Testing matplotlib GUI..."

python <<EOF
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
plt.plot([1,2,3])
plt.title("ElectronScatter test plot")
plt.show()
EOF

echo
echo "Environment check completed successfully."
echo

read -p "Press Enter to close..."