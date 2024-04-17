import nmap3
import json
import nmap
import threading

def scan_ip(ip, timeout=10):
    nm = nmap.PortScanner()
    try:
        nm.scan(ip)
        return nm[ip]
    except Exception as e:
        print(f"Error scanning {ip}: {str(e)}")
        return None

def scan_ips_with_timeout(ip_list, timeout=10):
    results = {}
    
    def scan_and_store(ip):
        results[ip] = scan_ip(ip, timeout)
    
    threads = []
    for ip in ip_list:
        thread = threading.Thread(target=scan_and_store, args=(ip,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join(timeout)
    
    return results

ip_addresses = ['185.114.98.6', '46.183.13.250', '46.183.12.6']
scan_results = scan_ips_with_timeout(ip_addresses, timeout=10)

for ip, result in scan_results.items():
    if result:
        print(f"Scan results for {ip}:")
        for proto in result.all_protocols():
            print(f"Protocol : {proto}")
            ports = result[proto].keys()
            for port in ports:
                print (f"port : {port} state : {result[proto][port]['state']}")
    else:
        print(f"Unable to scan {ip}")
