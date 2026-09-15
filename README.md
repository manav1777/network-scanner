# Network Scanner

**Multithreaded TCP Port Scanner with a Flask Web Interface**

Network Scanner is a Python and Flask application that scans a target hostname or IP address for open TCP ports and identifies common services associated with those ports.

The project demonstrates fundamental network reconnaissance concepts using Python socket programming, TCP connections, and multithreading, with scan results presented through a simple web interface.

**Live Demo:** https://network-scanner-r6a5.onrender.com/

---

## Key Features

- Scan hostnames or IP addresses for open TCP ports
- Identify common services associated with detected ports
- Perform concurrent port scanning using multithreading
- Display scan results through a Flask web interface
- Accept user-supplied scan targets
- Present open ports in a clear, readable format

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
                 ▼
          TCP Connection Tests
                 │
                 ▼
          Detect Open Ports
                 │
                 ▼
        Identify Common Services
                 │
                 ▼
          Display Scan Results
```

The scanner attempts TCP connections to ports on the selected target. Multithreading allows multiple ports to be tested concurrently rather than sequentially.

Ports that accept a connection are reported as open and can be associated with common services such as HTTP or HTTPS.

---

## Example

### Target

```text
scanme.nmap.org
```

### Example Result

```text
Port 80 (HTTP) OPEN
Port 443 (HTTPS) OPEN
```

Actual results depend on the target host and its network configuration.

---

## Tech Stack

### Backend

- Python
- Flask

### Networking

- Python Sockets
- TCP/IP
- Multithreading
- Port Scanning
- Service Identification

### Frontend

- HTML
- CSS

---

## Networking Concepts

### TCP Port Scanning

The application tests TCP ports on a target system to determine whether connections can be established.

### Socket Programming

Python sockets are used to create network connections and communicate with target hosts.

### Multithreading

Multiple scan operations can run concurrently to improve scanning speed compared with checking each port sequentially.

### Service Identification

Detected ports can be mapped to commonly associated network services, such as HTTP and HTTPS.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/manav1777/network-scanner.git
cd network-scanner
```

### 2. Install Dependencies

```bash
pip install flask
```

If the repository contains a `requirements.txt` file, you can instead use:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## What This Project Demonstrates

Network Scanner demonstrates practical experience with:

- Python network programming
- TCP/IP fundamentals
- Socket programming
- Network reconnaissance
- TCP port scanning
- Multithreading
- Flask web development
- Presenting network scan results through a web interface

---

## Future Improvements

Potential improvements include:

- Custom port range selection
- UDP scanning
- Banner grabbing for improved service identification
- Host availability detection
- Scan history
- Export results to CSV or JSON
- Additional service identification

---

## Authorized Use Only

Network Scanner is an educational cybersecurity project designed to demonstrate network reconnaissance and TCP port scanning concepts.

Only scan systems and networks that you own or have explicit authorization to test. Unauthorized network scanning may violate organizational policies or applicable laws.

---

## Author

**Manav Patel**  
Cybersecurity Student at Drexel University

[GitHub](https://github.com/manav1777) · [LinkedIn](https://linkedin.com/in/manavpatel017)
