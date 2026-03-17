#!/usr/bin/env bash

set -e

cd "$(dirname "$0")"

echo
echo "========================================"
echo "ElectronScatter Runner" version 3.0
echo "========================================"
echo

python3 env_setup.py

source venv/bin/activate

python main.py
