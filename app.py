from flask import Flask, render_template, request
import threading
import socket

app = Flask(__name__)

# Scanner logic
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
scan_results = []

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            service = COMMON_SERVICES.get(port, "Unknown")
            scan_results.append(f"Port {port} ({service}) → OPEN")
        sock.close()
    except Exception as e:
        scan_results.append(f"Error scanning port {port}: {e}")

def scan_target(target):
    global scan_results
    scan_results = []

    try:
        ip = socket.gethostbyname(target)  # resolve hostname
    except socket.gaierror:
        scan_results.append(f"Cannot resolve hostname: {target}")
        return None

    threads = []
    for port in common_ports:
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    return ip

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        target = request.form.get("ip")
        if not target:
            return render_template("index.html", results=["Invalid input"], resolved_ip=None)

        resolved_ip = scan_target(target)
        return render_template("index.html", results=scan_results, resolved_ip=resolved_ip)

    return render_template("index.html", results=None, resolved_ip=None)

if __name__ == "__main__":
    app.run(debug=True)