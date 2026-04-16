from flask import Flask, render_template, request
import threading
import socket

app = Flask(__name__)

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

lock = threading.Lock()


def scan_port(ip, port, results):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        if sock.connect_ex((ip, port)) == 0:
            service = COMMON_SERVICES.get(port, "Unknown")
            with lock:
                results.append({
                    "port": port,
                    "service": service,
                    "status": "OPEN"
                })

        sock.close()

    except Exception as e:
        with lock:
            results.append({
                "port": port,
                "service": "ERROR",
                "status": str(e)
            })


def scan_target(target):
    results = []

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        return None, [{"error": "Cannot resolve hostname"}]

    threads = []

    for port in common_ports:
        t = threading.Thread(target=scan_port, args=(ip, port, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return ip, results


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        target = request.form.get("ip")

        if not target:
            return render_template("index.html", results=[{"error": "Invalid input"}], resolved_ip=None)

        ip, results = scan_target(target)

        return render_template("index.html", results=results, resolved_ip=ip)

    return render_template("index.html", results=None, resolved_ip=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)