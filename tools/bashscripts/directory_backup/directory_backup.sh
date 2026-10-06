#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <source-directory> <backup-directory>"
    exit 1
fi

source_dir="$1"
backup_dir="$2"

if [ ! -d "$source_dir" ]; then
    echo "Error: source directory '$source_dir' does not exist."
    exit 1
fi

mkdir -p "$backup_dir"

timestamp=$(date +"%Y%m%d_%H%M%S")
archive="$backup_dir/backup_$timestamp.tar.gz"

tar -czf "$archive" "$source_dir"

echo "Backup created: $archive"
