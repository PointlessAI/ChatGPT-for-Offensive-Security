import requests
import random
import time
from itertools import cycle
from requests.adapters import HTTPAdapter
from requests.sessions import Session

class PenTesterTools:

    def __init__(self):
        self.ip_cycle = cycle(["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4"])
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.3"
        ]
        self.proxy_list = [
            "http://192.168.1.5:8000", "http://192.168.1.6:8000", "http://192.168.1.7:8000"
        ]
        self.proxy_cycle = cycle(self.proxy_list)
        self.session_tokens = ["token1", "token2", "token3"]

    def ip_rotation(self):
        return next(self.ip_cycle)

    def user_agent_switching(self):
        return random.choice(self.user_agents)

    def proxy_usage(self):
        return next(self.proxy_cycle)

    def request_throttling(self, interval=2):
        time.sleep(interval)

    def off_peak_timing(self, function, *args, **kwargs):
        if time.localtime().tm_hour < 9 or time.localtime().tm_hour > 21:
            function(*args, **kwargs)

    def distributed_testing(self, url):
        url_same_action = [
            url, 
            url.replace("http:", "http://127.0.0.1"),
            url.replace("http:", "http://localhost"),
        ]
        response = requests.get(random.choice(url_same_action))
        print(response.status_code)

    def session_token_generation(self):
        return random.choice(self.session_tokens)

    def parameter_randomization(self, url):
        params = {'param1': random.randint(1, 100), 'param2': random.randint(101, 200)}
        response = requests.get(url, params=params)
        print(response.status_code)

    def dynamic_payload_construction(self):
        payload = {'name': f'user{random.randint(1, 100)}', 'age': random.randint(15, 50)}
        return payload

    def analyze_rate_limiting(self, url):
        session = Session()
        session.mount('http://', HTTPAdapter(max_retries=3))
        for i in range(5):
            response = session.get(url)
            if response.status_code == 429:
                print('Rate limit exceeded')
                break
                
def main():
    tester = PenTesterTools()
    ip = tester.ip_rotation()
    user_agent = tester.user_agent_switching()
    proxy = tester.proxy_usage()
    tester.request_throttling()
    tester.off_peak_timing(lambda: print("testing during off-peak"))
    tester.distributed_testing("http://127.0.0.1:5000")
    session_token = tester.session_token_generation()
    tester.parameter_randomization("http://127.0.0.1:5000")
    payload = tester.dynamic_payload_construction()
    tester.analyze_rate_limiting("http://127.0.0.1:5000/api")

if __name__ == "__main__":
    main()
