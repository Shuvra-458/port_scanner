from scapy.all import IP, TCP, sr1, conf
import logging

conf.verb = 0  # Suppress Scapy verbose output

def syn_scan(target, port, timeout, scan_results):
    try:
        ip_layer = IP(dst=target)
        tcp_layer = TCP(dport=port, flags='S')

        response = sr1(ip_layer / tcp_layer, timeout=timeout)

        if response is None:
            status = "Filtered"
            banner = "No response"
        elif response.haslayer(TCP):
            if response.getlayer(TCP).flags == 0x12:  # SYN-ACK
                status = "Open"
                banner = "SYN-ACK received"
                # Send RST to close the half-open connection
                rst = IP(dst=target) / TCP(dport=port, flags='R')
                sr1(rst, timeout=timeout)
            elif response.getlayer(TCP).flags == 0x14:  # RST-ACK
                status = "Closed"
                banner = "RST received"
            else:
                status = "Unknown"
                banner = str(response.summary())
        else:
            status = "Unknown"
            banner = str(response.summary())

        if status == "Open":
            print(f"[+] SYN {port} Open - {banner}")
            scan_results.append({
                "port": port,
                "protocol": "TCP-SYN",
                "status": status,
                "banner": banner
            })
    except Exception as e:
        logging.warning(f"Exception on port {port}: {e}")
