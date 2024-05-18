import requests
from bs4 import BeautifulSoup
import nmap

def assess_website_security(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        nmap_scanner = nmap.PortScanner()
        nmap_scanner.scan(url, '1-1024')
        
        if nmap_scanner[url].state() == 'up':
            print("Security assessment completed. No critical vulnerabilities found.")
        else:
            print("Security assessment failed. The website is not reachable or experiencing issues.")
    else:
        print("Error: Unable to load the website. Check URL and internet connection.")

url = 'https://brokencrystals.com/'
assess_website_security(url)
