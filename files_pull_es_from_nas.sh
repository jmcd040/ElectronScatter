#!/usr/bin/env bash

# ==============================
# Sync pull ElectronScatter from mcdnas
# ==============================

set -euxo pipefail

SOURCE_DIR="/nas/home/Code/ElectronScatter"
DEST_DIR="$HOME/Documents/ElectronScatter"
MOUNT_POINT="/nas/home"

echo "pull ElectronScatter from mcdnas $SOURCE_DIR"
echo

# Verify NAS is mounted
if ! mountpoint -q "$MOUNT_POINT"; then
    echo "ERROR: NAS not mounted."
    echo "Check network or NAS."
    read -p "Press Enter to close..."
    exit 1
fi

# Ensure destination exists
mkdir -p "$DEST_DIR"

echo "Starting rsync..."
echo

rsync -ah --delete \
--info=progress2 \
--no-perms --no-owner --no-group \
"$SOURCE_DIR/" "$DEST_DIR/"

echo
echo "Sync from mcdnas complete."
read -p "Press Enter to close..."