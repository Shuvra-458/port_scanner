import json
import csv
from datetime import datetime

def export_results(format_type, target, scan_results):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename_base = f"scan_{target.replace('.', '_')}_{timestamp}"

    if format_type == "json":
        with open(f"{filename_base}.json", "w") as f:
            json.dump(scan_results, f, indent=4)
        print(f"[+] Results saved to {filename_base}.json")

    elif format_type == "csv":
        with open(f"{filename_base}.csv", "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["port", "protocol", "status", "banner"])
            writer.writeheader()
            writer.writerows(scan_results)
        print(f"[+] Results saved to {filename_base}.csv")

    elif format_type == "html":
        with open(f"{filename_base}.html", "w") as f:
            f.write("<html><body><h2>Port Scan Report</h2><table border='1'>")
            f.write("<tr><th>Port</th><th>Protocol</th><th>Status</th><th>Banner</th></tr>")
            for entry in scan_results:
                f.write(f"<tr><td>{entry['port']}</td><td>{entry['protocol']}</td><td>{entry['status']}</td><td>{entry['banner']}</td></tr>")
            f.write("</table></body></html>")
        print(f"[+] Results saved to {filename_base}.html")
