#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <file-or-directory>"
    exit 1
fi

target="$1"

if [ ! -e "$target" ]; then
    echo "Error: '$target' does not exist."
    exit 1
fi

echo "=== Permission Report ==="
ls -ld "$target"
echo
echo "Owner: $(stat -c '%U' "$target")"
echo "Group: $(stat -c '%G' "$target")"
echo "Permissions: $(stat -c '%A' "$target")"
