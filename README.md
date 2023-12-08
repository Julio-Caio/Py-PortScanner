# Py-PortScanner

**Welcome to Py-PortScanner!**

![Python](https://github.com/walkxcode/dashboard-icons/blob/main/svg/python.svg)

## Overview

Py-PortScanner is an dynamic Python-based port scanner designed to simplify network reconnaissance. It empowers users to explore and analyze open ports on a target system efficiently. Whether you're a cybersecurity enthusiast, network administrator, or curious learner, Py-PortScanner provides a user-friendly interface and robust functionality.

## Features

- **Dynamic Param Selection:** Choose from a variety of scan types, from TCP SYN scans to aggressive scans, using a simple menu interface.
- **Flexible Target Specification:** Define target hosts using IP ranges or specific addresses.
- **Custom Port Specification:** Scan a single port or a range of ports to tailor your reconnaissance.
- **Output to File:** Save scan results directly to a file for later analysis.
- **Exception Handling:** Gracefully handle invalid parameters with an exception system.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Julio-Caio/Py-PortScanner.git
   ```

2. Navigate to the PortSweeper directory:
   ```bash
   cd Py-PortScanner
   ```

3. Run the script:
   ```bash
   python main.py
   ```

4. Follow the on-screen instructions to customize your scan.

## Examples

### Basic Scan

Scan a range of IP addresses for open port 22:

```bash
python main.py
```

### Aggressive Scan

Perform an aggressive scan on a specific host:

```bash
python main.py -sA
```

## Requirements

- Python 3.x
- python-nmap library

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Disclaimer

This tool is meant for educational and ethical use only. Users are responsible for compliance with local laws and ethical standards.

## Contribution

We welcome contributions! Feel free to open issues, submit pull requests, or provide suggestions.

## License

Py-PortScanner is licensed under the [MIT License](LICENSE).

---

Feel free to customize this template according to your project's specific details and needs. Add or remove sections as necessary.
