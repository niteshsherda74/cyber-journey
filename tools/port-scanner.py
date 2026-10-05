import socket
import threading

target = input("Enter target IP: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

open_ports = []
lock = threading.Lock()

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        with lock:
            open_ports.append(port)

    sock.close()

threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("\nOpen ports:")
for port in sorted(open_ports):
    print(port)
