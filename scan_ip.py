from ping3 import ping
import concurrent.futures

used_ips = []
def scan_ip(ip):
    response_time = ping(ip)
    if response_time is not None:
        used_ips.append(ip)
        print(f"IP地址 {ip} 被占用")
    else:
        print(f"IP地址 {ip} 可用")

ip_range = "10.1.1."
def scan_ip_range(ip_range):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        ips = [ip_range + str(i) for i in range(2, 255)]
        results = executor.map(scan_ip, ips)

ip_range = "10.1.1."

scan_ip_range(ip_range)
print(used_ips)
