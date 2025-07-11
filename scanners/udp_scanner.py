import socket

def udp_scan(target, port, timeout, scan_results):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(timeout)
            s.sendto(b"", (target, port))
            try:
                data, _ = s.recvfrom(1024)
                status = "Open/Responsive"
                banner = data.decode(errors="ignore")
            except socket.timeout:
                status = "Open|Filtered"
                banner = "No response"
            result_dict = {
                "port": port,
                "protocol": "UDP",
                "status": status,
                "banner": banner
            }
            scan_results.append(result_dict)
            print(f"[+] UDP {port} - {status} - {banner}")
    except Exception:
        pass
