import requests
from bs4 import BeautifulSoup

def scan_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Testing SSL configuration
    if response.url.startswith('https://'):
        print('SSL configuration is secure')
    else:
        print('SSL configuration may need improvement')
    
    # Analyzing input/output validation
    input_fields = soup.find_all('input')
    for field in input_fields:
        if field.get('name'):
            print(f'Input field found: {field.get("name")}')
    
    # Testing for potential injection flaws
    payloads = ["'", '"', '<script>alert(1)</script>', '<img src="invalid" onerror="alert(1)">']
    for payload in payloads:
        inject_url = url + '?query=' + payload
        inject_response = requests.get(inject_url)
        if payload in inject_response.text:
            print(f'Potential injection vulnerability found with payload: {payload}')
    
    # Testing for Cross-Site Scripting (XSS) vulnerabilities
    xss_payload = '<script>alert(1)</script>'
    xss_url = url + '?input=' + xss_payload
    xss_response = requests.get(xss_url)
    if xss_payload in xss_response.text:
        print('XSS vulnerability found')
    
    # Identifying misconfigurations
    all_links = [link.get('href') for link in soup.find_all('a')]
    suspicious_links = [link for link in all_links if 'http' in link]
    if suspicious_links:
        print('Misconfigured links found:')
        for link in suspicious_links:
            print(link)

scan_website('https://brokencrystals.com/')
