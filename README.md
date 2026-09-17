# Network Scanner

**Multithreaded TCP Port Scanner with a Flask Web Interface**

Network Scanner is a Python and Flask application that scans a target hostname or IP address for open TCP ports and identifies common services associated with those ports.

The project demonstrates fundamental network reconnaissance concepts using Python socket programming, TCP connections, hostname resolution, and multithreading, with scan results presented through a web-based network diagnostics interface.

**Live Demo:** https://network-scanner-r6a5.onrender.com/

---

## Key Features

- Scan hostnames or IP addresses
- Resolve hostnames to IPv4 addresses
- Test 10 commonly used TCP ports
- Detect ports accepting TCP connections
- Identify commonly associated network services
- Perform concurrent scanning using multithreading
- Display target and resolved IP information
- Show the number of ports tested and open ports detected
- Present detected services in a structured results table
- Handle invalid or unresolvable targets

---

## Ports & Services

The current version tests the following common TCP ports:

| Port | Service |
|---:|---|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 139 | NetBIOS |
| 143 | IMAP |
| 443 | HTTPS |

The service name represents the service commonly associated with each port. An open port does not guarantee that the expected service is actually running on that port.

---

## How It Works

```text
        Hostname / IP Address
                 │
                 ▼
          Flask Web Interface
                 │
                 ▼
          Resolve Target Host
                 │
                 ▼
        Multithreaded Scanner
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
      Port 1   Port 2   Port ...
        │        │        │
        └────────┼────────┘
                 │
                 ▼
          TCP Connection Tests
                 │
                 ▼
          Detect Open Ports
                 │
                 ▼
        Map Common Services
                 │
                 ▼
          Display Scan Results
```

The scanner first resolves the submitted hostname to an IP address.

Python sockets then attempt TCP connections to the configured ports. A thread pool allows multiple ports to be tested concurrently rather than checking every port sequentially.

Ports that accept a connection are reported as open and mapped to their commonly associated service.

---

## Scan Results

After a scan completes, the web interface displays:

- Target hostname or IP address
- Resolved IP address
- Number of ports tested
- Number of open ports detected
- Port number
- Common service name
- Protocol
- Open status

If none of the configured ports accept a connection, the application clearly reports that no open ports were detected among the ports tested.

---

## Example

### Target

```text
scanme.nmap.org
```

Example scan output may include:

```text
PORT    SERVICE    PROTOCOL    STATUS
22      SSH        TCP         OPEN
53      DNS        TCP         OPEN
80      HTTP       TCP         OPEN
```

Actual results can change depending on the target host, its network configuration, firewall rules, and the time of the scan.

---

## Tech Stack

### Backend

- Python
- Flask

### Networking

- Python Sockets
- TCP/IP
- Hostname Resolution
- Multithreading
- TCP Port Scanning
- Service Identification

### Frontend

- HTML
- CSS
- Jinja2

---

## Networking Concepts

### Hostname Resolution

The application resolves submitted hostnames to IPv4 addresses before beginning a scan.

### TCP Port Scanning

The scanner attempts TCP connections to configured ports to determine whether they accept connections.

### Socket Programming

Python's socket library is used to create TCP connections between the scanner and the target host.

### Multithreading

A thread pool allows multiple ports to be tested concurrently, improving scan speed compared with sequential scanning.

### Service Identification

Open ports are mapped to commonly associated services such as SSH, HTTP, DNS, and HTTPS.

This is port-based service identification rather than banner grabbing or active service fingerprinting.

---

## Project Structure

```text
network-scanner/
│
├── app.py
├── network_scanner.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── requirements.txt
├── README.md
└── .gitignore
```

`app.py` provides the Flask web application and scan interface.

`network_scanner.py` provides the standalone network-scanning implementation.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/manav1777/network-scanner.git
cd network-scanner
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python3 app.py
```

Flask will display the local development URL in the terminal.

Open the displayed address in your web browser.

---

## What This Project Demonstrates

Network Scanner demonstrates practical experience with:

- Python network programming
- TCP/IP fundamentals
- Socket programming
- Hostname and IP resolution
- Network reconnaissance
- TCP port scanning
- Multithreading and concurrent execution
- Common network services
- Flask web development
- Presenting network scan results through a web interface

---

## Limitations

The current version is intentionally focused on fundamental TCP scanning concepts.

It currently:

- Tests a predefined set of 10 common TCP ports
- Performs TCP connection-based scanning
- Uses port numbers for common service identification
- Does not perform banner grabbing
- Does not perform service/version fingerprinting
- Does not perform UDP scanning
- Does not attempt vulnerability exploitation

A port reported as closed or not detected may also be affected by firewall rules, filtering, network conditions, or timeouts.

---

## Future Improvements

Potential improvements include:

- Custom port range selection
- Expanded TCP port coverage
- UDP scanning
- Banner grabbing
- Service and version detection
- Host availability detection
- Configurable scan timeouts
- Scan history
- Export results to CSV or JSON
- Additional service identification
- Improved scan reporting

---

## Authorized Use Only

Network Scanner is an educational cybersecurity project designed to demonstrate network reconnaissance, TCP port scanning, socket programming, and service identification concepts.

Only scan systems and networks that you own or have explicit authorization to test. Do not use this tool to scan systems without permission.

---

## Author

**Manav Patel**  
Cybersecurity Student at Drexel University

[GitHub](https://github.com/manav1777) · [LinkedIn](https://linkedin.com/in/manavpatel017)
