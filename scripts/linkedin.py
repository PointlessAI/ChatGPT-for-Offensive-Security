import requests
import json
import os
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

client_id = 'Your_Client_ID'
client_secret = 'Your_Client_Secret'
token_url = 'https://www.linkedin.com/oauth/v2/accessToken'

client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)

headers = {
    'Authorization': f"Bearer {token['access_token']}",
    'Content-Type': 'application/json'
}

company_name = 'PointlessAI'
params = {
    'q': 'universalName',
    'universalName': company_name
}
response = requests.get(f"https://api.linkedin.com/v2/organizations", headers=headers, params=params)

company_info = response.json()
print(json.dumps(company_info, indent=2))
