import threading
import socket

COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS"
}

common_ports = list(COMMON_SERVICES.keys())


def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))

        if result == 0:
            service = COMMON_SERVICES.get(port, "Unknown")
            print(f"Port {port} ({service}) → OPEN")

        sock.close()

    except Exception as e:
        print(f"Error scanning port {port}: {e}")


def scan_target(ip):
    print(f"\nScanning target: {ip}\n")

    threads = []

    for port in common_ports:
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


# Run scanner
target = input("Enter IP address to scan: ")
scan_target(target)