import re
import time
import logging
import subprocess
from collections import defaultdict

LOG_FILE = '/var/log/nginx/access.log'
BLOCKLIST_FILE = '/etc/nginx/blocklist.conf'
THRESHOLD = 100
BLOCK_DURATION = 300

logging.basicConfig(filename='/var/log/ddos_mitigation.log', level=logging.INFO)

def parse_log_line(line):
    match = re.match(r'(\d+\.\d+\.\d+\.\d+) - - \[(.+?)\] "(.+?)" (\d+) (\d+) "(.+?)" "(.+?)"', line)
    if match:
        return match.group(1), time.strptime(match.group(2), '%d/%b/%Y:%H:%M:%S %z')
    return None, None

def monitor_traffic(log_file=LOG_FILE):
    ip_requests = defaultdict(list)
    with open(log_file, 'r') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue
            ip, timestamp = parse_log_line(line)
            if not ip or not timestamp:
                continue
            ip_requests[ip].append(timestamp)
            ip_requests[ip] = [t for t in ip_requests[ip] if time.mktime(time.gmtime()) - mktime(t) <= 60]
            if len(ip_requests[ip]) > THRESHOLD:
                block_ip(ip)

def block_ip(ip, block_duration=BLOCK_DURATION):
    try:
        with open(BLOCKLIST_FILE, 'a') as f:
            f.write(f"deny {ip};\n")
        subprocess.call(['nginx', '-s', 'reload'])
        logging.info(f"Blocked IP {ip} at {time.ctime()} for {block_duration} seconds")
        time.sleep(block_duration)
        unblock_ip(ip)
    except Exception as e:
        logging.error(f"Failed to block IP {ip}: {str(e)}")

def unblock_ip(ip):
    try:
        with open(BLOCKLIST_FILE, 'r') as f:
            lines = f.readlines()
        with open(BLOCKLIST_FILE, 'w') as f:
            for line in lines:
                if ip not in line:
                    f.write(line)
        subprocess.call(['nginx', '-s', 'reload'])
        logging.info(f"Unblocked IP {ip} at {time.ctime()}")
    except Exception as e:
        logging.error(f"Failed to unblock IP {ip}: {str(e)}")

if __name__ == "__main__":
    monitor_traffic()
