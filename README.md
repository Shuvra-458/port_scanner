# 🔍 Python CLI Port Scanner

A fast, modular, and customizable port scanner built using Python. Supports **TCP Connect**, **UDP**, and **SYN** scan types. Designed for ethical use only.

---

## 🚀 Features

- 🔧 Supports TCP, UDP, and SYN scanning
- 🚦 Multi-threaded for high performance
- 🧠 Intelligent timeout and response handling
- 📤 Export scan results to JSON, CSV, or HTML
- 🧱 Modular structure for easy extension
- 🐍 Pure Python (Scapy for SYN scanning)

---
## ✅ Installation & Running Locally

 **Clone the repository:**

```bash
git clone https://github.com/YourUsername/YourRepoName.git
cd port_scanner
```

## 🛠️ Requirements

- Python 3.6+
- [Scapy](https://pypi.org/project/scapy/)

Install requirements:

```bash
pip install -r requirements.txt
```
## 🧪 Usage
```bash
python main.py <target> [options]
```
## 🔧 Arguments

| Argument             | Description                                  | Default     |
|----------------------|----------------------------------------------|-------------|
| `target`             | Target IP address or domain name             | *required*  |
| `-sp`, `--start_port`| Start port number                            | `1`         |
| `-ep`, `--end_port`  | End port number                              | `1024`      |
| `-t`, `--threads`    | Number of concurrent threads                 | `100`       |
| `-to`, `--timeout`   | Timeout for each request (in seconds)        | `1.0`       |
| `-st`, `--scan_type` | Scan type: `tcp`, `udp`, or `syn`            | `tcp`       |
| `-o`, `--output`     | Export format: `json`, `csv`, or `html`      | *optional*  |

---

## ✅ Example Usage

Run a basic TCP scan:

```bash
python main.py scanme.nmap.org -sp 20 -ep 25 -st tcp
```

SYN scan with json export
```bash
sudo python3 main.py 45.33.32.156 -sp 22 -ep 80 -st syn -o json
```
## 📁 Output
If -o flag is used, the scan results will be saved in the following format:
```bash
scan_<target>_<timestamp>.json
```
## ⚠️ Disclaimer
This tool is intended for educational and authorized security testing only. Scanning networks or systems without permission is illegal. It is suggested to clone this repository in your local machine and test this program on the devices on your local systems.

