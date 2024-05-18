import requests
import threading
import multiprocessing
import random
import time

url = 'http://127.0.0.1/'
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'
]

def send_requests():
    session = requests.Session()
    while True:
        headers = {'User-Agent': random.choice(user_agents)}
        try:
            response = session.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                print("Successful request")
            time.sleep(random.uniform(0.5, 3))  # Add random delay between requests
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    num_threads = 100
    num_processes = 10
    
    for _ in range(num_processes):
        p = multiprocessing.Process(target=send_requests)
        p.start()

    for _ in range(num_threads):
        t = threading.Thread(target=send_requests)
        t.start()
