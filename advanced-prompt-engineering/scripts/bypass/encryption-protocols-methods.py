import requests
from bs4 import BeautifulSoup

def scan_encryption_protocols(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            meta_tags = soup.find_all('meta')
            encryption_methods = []

            for tag in meta_tags:
                if tag.has_attr('http-equiv') and tag['http-equiv'].lower() == 'content-security-policy':
                    policy_directives = tag.get('content').split(';')
                    for directive in policy_directives:
                        if 'encrypt' in directive:
                            encryption_methods.append(directive.split('=')[-1].strip())

            if encryption_methods:
                return encryption_methods
            else:
                return "No specific encryption protocols mentioned in the Content-Security-Policy headers."

        else:
            return "Failed to retrieve data. Status code: "+ str(response.status_code)

    except Exception as e:
        return "An error occurred: "+ str(e)

url = 'https://brokencrystals.com/'
encryption_protocols = scan_encryption_protocols(url)
print("Encryption Protocols on", url + ":", encryption_protocols)
