# Permission Report Bash Script

## Overview

A Bash script that reports the permissions, owner, and group associated with a file or directory.

## Features

- Accepts a file or directory as an argument
- Checks whether the target exists
- Displays Linux permission information
- Displays the owner and group

## Requirements

- Linux or another Unix-like environment
- Bash

## Usage

Make the script executable:

```bash
chmod +x permission_report.sh
```

Run it:

```bash
./permission_report.sh <file-or-directory>
```

Example:

```bash
./permission_report.sh test.txt
```

## Concepts Practiced

- Positional arguments
- Conditional statements
- File existence checks
- Linux permissions
- Owner and group concepts
- `stat` and `ls`

## Security / Learning Note

Created for the cybersecurity learning journey and intended for use on systems you own or are authorized to administer.
