import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
from utils import logger, exporter
from scanners import tcp_scanner, udp_scanner, syn_scanner

scan_results = []

def run_scanner(target, start_port, end_port, max_threads, timeout, scan_type):
    print(f"\n[*] Starting {scan_type.upper()} scan on {target} ports {start_port}-{end_port}")
    logger.log_scan_start(scan_type, target)

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        for port in range(start_port, end_port + 1):
            if scan_type == "tcp":
                executor.submit(tcp_scanner.tcp_connect_scan, target, port, timeout, scan_results)
            elif scan_type == "udp":
                executor.submit(udp_scanner.udp_scan, target, port, timeout, scan_results)
            elif scan_type == "syn":
                executor.submit(syn_scanner.syn_scan, target, port, timeout, scan_results)

    logger.log_scan_end()
    print(f"[*] Scan Completed. Total open/responsive ports: {len(scan_results)}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Modular Advanced Python Port Scanner")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("-sp", "--start_port", type=int, default=1, help="Start port")
    parser.add_argument("-ep", "--end_port", type=int, default=1024, help="End port")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Max threads")
    parser.add_argument("-to", "--timeout", type=float, default=1.0, help="Timeout (sec)")
    parser.add_argument("-st", "--scan_type", choices=["tcp", "udp", "syn"], default="tcp", help="Scan type")
    parser.add_argument("-o", "--output", choices=["json", "csv", "html"], help="Export format")
    return parser.parse_args()

def main():
    args = parse_arguments()
    try:
        target_ip = socket.gethostbyname(args.target)
        print(f"[*] Resolved target: {args.target} ({target_ip})")
        run_scanner(target_ip, args.start_port, args.end_port, args.threads, args.timeout, args.scan_type)

        if args.output:
            exporter.export_results(args.output, args.target, scan_results)

    except socket.gaierror:
        print("[!] Invalid target address.")
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")

if __name__ == "__main__":
    main()
