# Threaded TCP Port Scanner

A lightweight Python TCP port scanner that uses **multithreading** to check a user-defined port range concurrently.

> **Authorized use only:** Run this tool only against systems you own or have explicit permission to test.

## Features

- TCP connectivity checks using Python's `socket` module
- Concurrent scanning with `threading`
- User-defined target IP and port range
- Thread-safe collection of open ports
- Sorted, readable output
- Input validation for valid TCP port ranges

## Requirements

- Python 3.x
- No external packages required

## Usage

From this directory:

```bash
python portscanner.py
```

Enter:

1. Target IP address
2. Starting port
3. Ending port

Example:

```text
Enter target IP: 192.168.56.101
Enter start port: 20
Enter end port: 100

Open ports:
- 22
- 80
```

Use an IP belonging to your own lab/VM or another explicitly authorized target.

## How It Works

1. Creates a TCP socket for each port.
2. Uses `connect_ex()` to test whether the port accepts a connection.
3. Runs port checks concurrently using threads.
4. Uses a lock to safely update the shared list of open ports.
5. Waits for all threads to finish with `join()`.
6. Prints the discovered open ports in sorted order.

## Learning Objective

This tool demonstrates:

- Python socket programming
- TCP connection behavior
- Port scanning fundamentals
- Multithreading
- Thread synchronization with `Lock`
- Basic security automation

## File

| File | Purpose |
| --- | --- |
| `portscanner.py` | Threaded TCP port scanner |
| `README.md` | Documentation and usage guide |
