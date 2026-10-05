"""
Threaded TCP Port Scanner

Scans a user-specified TCP port range on an authorized target and
reports ports that accept TCP connections.

Use only against systems you own or have explicit permission to test.
"""

import socket
import threading


def scan_port(target, port, open_ports, lock):
    """Check whether a TCP port is accepting connections."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        result = sock.connect_ex((target, port))

        if result == 0:
            with lock:
                open_ports.append(port)
    finally:
        sock.close()


def main():
    """Collect scan parameters, run threaded scans, and print results."""
    target = input("Enter target IP: ").strip()
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range. Use ports 1-65535 with start <= end.")
        return

    open_ports = []
    lock = threading.Lock()
    threads = []

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(
            target=scan_port,
            args=(target, port, open_ports, lock),
        )
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("\nOpen ports:")
    if open_ports:
        for port in sorted(open_ports):
            print(f"- {port}")
    else:
        print("No open TCP ports found in the specified range.")


if __name__ == "__main__":
    main()
