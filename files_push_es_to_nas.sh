#!/usr/bin/env bash

# ==============================
# Sync push ElectronScatter to mcdnas
# ==============================

#!/usr/bin/env bash

set -euo pipefail

trap 'echo; echo "Script stopped due to an error."; read -p "Press Enter to close..."' ERR

SOURCE_DIR="$HOME/Documents/ElectronScatter"
DEST_DIR="/nas/home/Code/ElectronScatter"
MOUNT_POINT="/nas/home"

echo "push ElectronScatter to mcdnas $DEST_DIR"
echo

if ! mountpoint -q "$MOUNT_POINT"; then
    echo "ERROR: NAS not mounted."
    read -p "Press Enter to close..."
    exit 1
fi

mkdir -p "$DEST_DIR"

echo "Starting rsync..."
echo

if ! rsync -rtvh \
    --delete \
    --delete-excluded \
    --omit-dir-times \
    --no-perms --no-owner --no-group \
    --ignore-errors \
    --inplace \
    --exclude venv \
    --exclude __pycache__ \
    --exclude "*.pyc" \
    --exclude ".DS_Store" \
    "$SOURCE_DIR/" "$DEST_DIR/"
then
    echo
    echo "ERROR: rsync failed."
    read -p "Press Enter to close..."
    exit 1
fi

echo
echo "Sync to mcdnas complete."
read -p "Press Enter to close..."