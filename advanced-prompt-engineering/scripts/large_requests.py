import requests
import threading
import multiprocessing
import time
import json
import logging

# Configure logging
logging.basicConfig(filename='request_log.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
class StressTester:
    def __init__(self, url, num_threads, num_processes, headers=None, payload_get=None, payload_post=None, rate_limit_secs=1):
        self.url = url
        self.num_threads = num_threads
        self.num_processes = num_processes
        self.headers = headers or {'User-Agent': 'Mozilla/5.0'}
        self.payload_get = payload_get or {'param': 'value'}
        self.payload_post = payload_post or {'key': 'value'}
        self.rate_limit_secs = rate_limit_secs

    def send_request(self, method):
        try:
            if method == 'GET':
                response = requests.get(self.url, headers=self.headers, params=self.payload_get)
            elif method == 'POST':
                response = requests.post(self.url, headers=self.headers, data=json.dumps(self.payload_post))
            else:
                return

            logging.info(f'Method: {method}, URL: {self.url}, Status Code: {response.status_code}, Response: {response.text[:200]}')
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")

    def run_threads(self):
        methods = ['GET', 'POST']
        threads = []

        def worker():
            while True:
                for method in methods:
                    self.send_request(method)
                    time.sleep(self.rate_limit_secs)

        for _ in range(self.num_threads):
            thread = threading.Thread(target=worker)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    def run_processes(self):
        processes = []
        for _ in range(self.num_processes):
            process = multiprocessing.Process(target=self.run_threads)
            process.start()
            processes.append(process)

        for process in processes:
            process.join()

if __name__ == "__main__":
    url = "http://127.0.0.1"  # Example target URL
    num_threads = 10          # Number of threads to be run per process
    num_processes = 4         # Number of processes
    headers = {'User-Agent': 'Mozilla/5.0', 'Authorization': 'Bearer token'}
    payload_get = {'param1': 'value1'}
    payload_post = {'key1': 'value1'}
    rate_limit_secs = 1       # Time delay to control request rate (in seconds)

    stress_tester = StressTester(url, num_threads, num_processes, headers=headers, payload_get=payload_get, payload_post=payload_post, rate_limit_secs=rate_limit_secs)
    stress_tester.run_processes()
