#!/usr/bin/env bash

# ============================================
# ElectronScatter Environment Verification
# Versio 4.0
# ============================================

set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

MODE="$1"

echo
echo "========================================"
echo "ElectronScatter Environment Check"
echo "========================================"
echo

cd "$PROJECT_DIR"

echo "Project directory:"
echo "$PROJECT_DIR"
echo

echo "Checking Python..."

if command -v python3 >/dev/null 2>&1; then
python3 --version
else
echo "ERROR: python3 not installed"
exit 1
fi

echo

if [ ! -d "venv" ]; then
echo "ERROR: venv not found."
echo "Run env_setup_python.sh first."
exit 1
fi

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
module = **import**(pkg)
version = getattr(module, "**version**", "unknown")
print(f"{pkg} OK (version {version})")
except Exception as e:
print(f"{pkg} MISSING:", e)
sys.exit(1)

check("numpy")
check("matplotlib")

print("\nPackage verification successful.")
EOF

echo

if [ "$MODE" = "quick" ]; then
echo "Quick check mode — skipping matplotlib GUI test."
echo
echo "Environment check completed."
exit 0
fi

echo "Testing matplotlib GUI..."

python <<EOF
import matplotlib.pyplot as plt
plt.plot([1,2,3])
plt.title("ElectronScatter test plot")
plt.show()
EOF

echo
echo "Environment check completed successfully."
echo

read -p "Press Enter to close..."
