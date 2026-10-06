# Bash Scripts

Small Bash scripts created during the cybersecurity learning journey.

## Scripts

| Script | Purpose |
| --- | --- |
| `system_info.sh` | Displays basic system and session information |
| `permission_report.sh` | Reports permissions, owner, and group for a file or directory |
| `directory_backup.sh` | Creates a timestamped compressed backup of a directory |

## How to Run

Make the scripts executable:

```bash
chmod +x system_info.sh permission_report.sh directory_backup.sh
```

### System Information

```bash
./system_info.sh
```

### Permission Report

```bash
./permission_report.sh <file-or-directory>
```

Example:

```bash
./permission_report.sh test.txt
```

### Directory Backup

```bash
./directory_backup.sh <source-directory> <backup-directory>
```

Example:

```bash
./directory_backup.sh ~/Documents ~/backups
```

## Learning Objectives

- Bash variables and command substitution
- Conditional checks and positional arguments
- File and directory permissions
- Owner and group concepts
- Creating executable scripts with `chmod`
- Basic backup automation
- Timestamped filenames
- Understanding how a script can be scheduled with cron

## Security Note

These scripts are intended for learning and use on systems you own or are authorized to administer.
