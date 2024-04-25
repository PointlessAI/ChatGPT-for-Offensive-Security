class SessionHijacking:
    """
    Man-in-the-Middle (MitM) Attacks using Ettercap:
    Description: This class implements session hijacking using Ettercap tool.
    Target URL: http://127.0.0.1:81/vulnerabilities/xss_d/

    Usage:
    1. Create an instance of the SessionHijacking class.
    2. Use the provided methods to perform session hijacking.
    """

    def get_target_contents(self, session):
        res = session.get('http://127.0.0.1:81/vulnerabilities/xss_d/')
        print(res.text)

    def modify_request(self, session):
        data = {'key': 'value'}
        res = session.post('http://127.0.0.1:81/vulnerabilities/xss_d/', data=data)
        print(res.text)

    def modify_response(self, session):
        res = session.get('http://127.0.0.1:81/vulnerabilities/xss_d/')
        modified_content = res.text.replace('original_text', 'modified_text')
        print(modified_content)

# Main Function
def main():
    import requests

    with requests.Session() as s:
        hijack = SessionHijacking()
        
        hijack.get_target_contents(s)
        hijack.modify_request(s)
        hijack.modify_response(s)

if __name__ == "__main__":
    main()
