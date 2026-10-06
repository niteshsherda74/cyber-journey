# Directory Backup Bash Script

## Overview

A Bash script that creates a timestamped compressed backup of a specified directory.

## Features

- Accepts source and backup directories as arguments
- Checks that the source directory exists
- Creates the backup directory when needed
- Creates a compressed `.tar.gz` archive
- Adds a timestamp to the backup filename

## Requirements

- Linux or another Unix-like environment
- Bash
- `tar`

## Usage

Make the script executable:

```bash
chmod +x directory_backup.sh
```

Run it:

```bash
./directory_backup.sh <source-directory> <backup-directory>
```

Example:

```bash
./directory_backup.sh ~/Documents ~/backups
```

## Concepts Practiced

- Positional arguments
- Conditional statements
- Directory creation
- Command substitution
- Timestamps
- `tar` compression
- Basic backup automation

## Security / Learning Note

Created for the cybersecurity learning journey and intended for use on systems you own or are authorized to administer.
