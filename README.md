# Network Scanner Tool

## Overview

The **Network Scanner Tool** is a Python and Flask application that scans a target host to identify open TCP ports and the common services running on them. It provides a simple web interface where users can enter a hostname or IP address and view the scan results in real time.

This project was built to demonstrate fundamental network reconnaissance techniques using Python socket programming and multithreading.

---

## Features

* Scan a target host for open TCP ports
* Detect common services such as HTTP and HTTPS
* Simple web-based interface built with Flask
* Supports scanning hostnames or IP addresses
* Fast scanning using multithreading
* Displays open ports in an easy-to-read format

---

## Tech Stack

* Python
* Flask
* Socket Programming
* Threading
* HTML
* CSS

---

## Example

Input:

```text id="ef9y07"
scanme.nmap.org
```

Output:

```text id="yd8vja"
Port 80 (HTTP) OPEN
Port 443 (HTTPS) OPEN
```

---

## Installation

Install the required dependency:

```bash id="vud1q4"
pip install flask
```

Run the application:

```bash id="vtjylm"
python app.py
```

Open your browser:

```text id="1s6a2b"
http://127.0.0.1:5000
```

---

## Skills Demonstrated

* Python programming
* Socket programming
* Network reconnaissance
* TCP/IP fundamentals
* Multithreading
* Flask web development

---

## Key Learning Outcomes

* Understanding how TCP port scanning works
* Building web applications with Flask
* Working with sockets and network connections
* Improving scan performance using concurrent threads
* Presenting scan results through a user-friendly interface

---

## Future Improvements

* Custom port range selection
* UDP scanning
* Banner grabbing for improved service identification
* Export scan results to CSV or JSON
* Scan history
* Host availability detection

---

## Author

**Manav Patel**
Cybersecurity Student
Drexel University
