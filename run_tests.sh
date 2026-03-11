#!/usr/bin/env bash

# ============================================
# Relativistic Two-Electron Simulator
# Test Harness Runner (with logging)
# ============================================

LOGFILE="test_results.log"

echo "----------------------------------------"
echo "Running Verification Tests"
echo "Log file: $LOGFILE"
echo "----------------------------------------"

# Activate virtual environment if present
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Run tests and capture ALL output
{
    echo "===== Test Run Started ====="
    date
    echo

    python3 test_harness.py

    echo
    echo "===== Test Run Completed ====="
    date
} 2>&1 | tee "$LOGFILE"

echo
echo "Results written to $LOGFILE"

# Optional: pause so window doesn't close immediately
echo
read -p "Press Enter to close..."