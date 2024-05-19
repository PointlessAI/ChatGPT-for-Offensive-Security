import random
import datetime

def generate_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

def generate_log_entry():
    ip = generate_ip()
    timestamp = datetime.datetime.now().strftime("%d/%b/%Y:%H:%M:%S %z")
    request_methods = ['GET', 'POST', 'PUT', 'DELETE']
    urls = ['/account', '/login', '/admin', '/backup', '/shell']
    user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15)']
    
    if random.random() < 0.2:
        return f'{ip} - - [{timestamp}] "SUSPICIOUS_REQUEST" 404'
    
    return f'{ip} - - [{timestamp}] "{random.choice(request_methods)} {random.choice(urls)} HTTP/1.1" 200 "-" "{random.choice(user_agents)}"'

with open('/home/kali/shellassistant/training-assistant/code/redteam/logs/dummy.log', 'a') as log_file:
    for _ in range(100):
        log_entry = generate_log_entry()
        log_file.write(log_entry + '\n')
