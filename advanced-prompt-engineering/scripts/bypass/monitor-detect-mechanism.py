import re
import threading
import time

def monitor_logs(log_file):
    def analyze_log(log):
        # Add your log analysis logic here
        if re.search(r'Failed login attempt', log):
            alert('Potential brute force attack detected!')
        elif re.search(r'High traffic from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', log):
            alert('Unusually high traffic from IP: \g<1>')
        elif re.search(r'Accessed sensitive file', log):
            alert('Accessed sensitive file detected!')
    
    def alert(message):
        # Integrate with SIEM system or perform necessary actions, such as logging
        print(f'[ALERT] {message}')
    
    def process_logs():
        while True:
            if not logs_queue.empty():
                log = logs_queue.get()
                analyze_log(log)
    
    logs_queue = Queue()
    threading.Thread(target=process_logs, daemon=True).start()

    # Simulate continuous log monitoring
    with open(log_file, 'r') as f:
        for line in f:
            logs_queue.put(line)
            time.sleep(0.1)  # Adjust as needed for real-time monitoring

# Call the function to start monitoring web server logs
monitor_logs('web_server_logs.log')
