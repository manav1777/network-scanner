from flask import Flask, render_template, request
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

app = Flask(__name__)

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
}


def scan_port(target_ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.8)
            result = sock.connect_ex((target_ip, port))

            if result == 0:
                return {
                    "port": port,
                    "service": COMMON_PORTS.get(port, "Unknown"),
                    "status": "OPEN",
                }

    except (socket.timeout, socket.error, OSError):
        pass

    return None


def scan_host(hostname):
    target_ip = socket.gethostbyname(hostname)

    results = []

    with ThreadPoolExecutor(max_workers=20) as executor:

        futures = [
            executor.submit(
                scan_port,
                target_ip,
                port
            )
            for port in COMMON_PORTS
        ]

        for future in as_completed(futures):

            result = future.result()

            if result:
                results.append(result)

    results.sort(key=lambda item: item["port"])

    return target_ip, results


@app.route("/", methods=["GET", "POST"])
def index():

    target = ""
    target_ip = None
    results = []
    error = None
    scanned = False

    if request.method == "POST":

        target = request.form.get("target", "").strip()

        if not target:

            error = "Enter a hostname or IP address."

        else:

            try:

                target_ip, results = scan_host(target)
                scanned = True

            except socket.gaierror:

                error = (
                    "The hostname could not be resolved. "
                    "Check the target and try again."
                )

            except Exception:

                error = (
                    "The scan could not be completed. "
                    "Please verify the target and try again."
                )

    return render_template(
        "index.html",
        target=target,
        target_ip=target_ip,
        results=results,
        error=error,
        scanned=scanned,
        ports_scanned=len(COMMON_PORTS),
    )


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )