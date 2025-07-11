import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "scan_results.txt")

def log_result(message):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(message + "\n")

def log_scan_start(scan_type, target):
    log_result(f"\n=== {scan_type.upper()} Scan Started at {datetime.now()} on {target} ===")

def log_scan_end():
    log_result(f"=== Scan Finished at {datetime.now()} ===\n")
