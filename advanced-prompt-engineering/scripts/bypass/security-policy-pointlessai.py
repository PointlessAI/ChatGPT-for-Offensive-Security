import requests
from bs4 import BeautifulSoup

def fetch_security_policy_details(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return {'error': 'Failed to fetch the security policy page. HTTP Status Code: {}'.format(response.status_code)}
        soup = BeautifulSoup(response.content, 'html.parser')
        policy_section = None
        for section in soup.find_all('section'):
            if 'security' in section.get_text().lower():
                policy_section = section
                break
        if not policy_section:
            return {'error': 'Security policy section not found on the provided URL.'}
        policy_text = policy_section.get_text(strip=True)
        details = {
            'user_data_protection': '',
            'authentication_authorization': '',
            'data_encryption_standards': '',
            'vulnerability_management': '',
            'incident_response': '',
            'regulatory_compliance': ''
        }
        key_phrases = {
            'user_data_protection': ['data protection', 'user data'],
            'authentication_authorization': ['authentication', 'authorization'],
            'data_encryption_standards': ['encryption', 'standards'],
            'vulnerability_management': ['vulnerability', 'management'],
            'incident_response': ['incident response', 'incident handling'],
            'regulatory_compliance': ['regulatory compliance', 'compliance']
        }
        for key, phrases in key_phrases.items():
            for phrase in phrases:
                if phrase in policy_text.lower():
                    details[key] = policy_text.lower().split(phrase, 1)[1].split('.', 1)[0]
                    break
        return details
    except requests.RequestException as e:
        return {'error': 'There was an error while trying to fetch the security policy details: {}'.format(e)}
    except Exception as e:
        return {'error': 'An unexpected error occurred: {}'.format(e)}

security_policy_details = fetch_security_policy_details("http://pointlessai.com")
print(security_policy_details)
