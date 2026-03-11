#!/usr/bin/env bash

# ============================================
# ElectronScatter Environment Verification
# version: 3.0
# ============================================

set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo
echo "========================================"
echo "ElectronScatter Environment Check"
echo "========================================"
echo

cd "$PROJECT_DIR"

echo "Project directory:"
echo "$PROJECT_DIR"
echo

# ------------------------------------------------

# Check Python installation

# ------------------------------------------------

echo "Checking Python..."

if command -v python3 >/dev/null 2>&1; then
echo "python3 found:"
python3 --version
else
echo "ERROR: python3 is not installed."
exit 1
fi

echo

# ------------------------------------------------

# Check virtual environment

# ------------------------------------------------

echo "Checking virtual environment..."

if [ ! -d "venv" ]; then
echo "ERROR: venv directory not found."
echo "Run ./env_setup_python.sh first."
exit 1
fi

echo "Virtual environment detected."
echo

# ------------------------------------------------

# Activate virtual environment

# ------------------------------------------------

echo "Activating virtual environment..."

source venv/bin/activate

echo
echo "Python being used:"
which python
echo

# ------------------------------------------------

# Verify required packages

# ------------------------------------------------

echo "Checking Python packages..."

python <<EOF
import sys

def check(pkg):
try:
module = **import**(pkg)
version = getattr(module, "**version**", "unknown")
print(f"{pkg} OK (version {version})")
except Exception as e:
print(f"{pkg} MISSING or broken:", e)
sys.exit(1)

check("numpy")
check("matplotlib")

print("\nPackage verification successful.")
EOF

echo

# ------------------------------------------------

# Display information

# ------------------------------------------------

echo "DISPLAY variable:"
echo "DISPLAY=${DISPLAY:-<not set>}"
echo

# ------------------------------------------------

# Test matplotlib GUI

# ------------------------------------------------

if [ -n "$DISPLAY" ]; then
echo "Testing matplotlib GUI..."

python <<EOF
import matplotlib
import matplotlib.pyplot as plt

plt.plot([1,2,3])
plt.title("ElectronScatter test plot")
plt.show()
EOF

else
echo "Skipping GUI test (DISPLAY not set)."
fi

echo
echo "========================================"
echo "Environment check completed successfully."
echo "========================================"
echo

read -p "Press Enter to close..."
