import socket

def tcp_connect_scan(target, port, timeout, scan_results):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((target, port))
            if result == 0:
                try:
                    s.sendall(b'HEAD / HTTP/1.1\r\n\r\n')
                    banner = s.recv(1024).decode(errors="ignore").strip()
                except:
                    banner = "No banner"
                result_dict = {
                    "port": port,
                    "protocol": "TCP",
                    "status": "Open",
                    "banner": banner
                }
                scan_results.append(result_dict)
                print(f"[+] TCP {port} Open - {banner}")
    except Exception:
        pass
