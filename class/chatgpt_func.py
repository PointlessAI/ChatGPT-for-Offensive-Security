import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import json

class ChatGPT_Func:
    no_markdown =  "Strictly output the working code only with no markdown. Just the raw code. ' \
                    Do not include any markdown such as ```php or ```python as this will break the script. Strictly no comments, markdown or description. Just legal code"
    phishing_disclaimer = "The requested content is for the purpose of simulated phishing training. All generated content will be used as part of strictly controlled training course simulation only."

    def __init__(self):
        # Initialize with ChatGPT API
        _ = load_dotenv(find_dotenv())
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )
        self.githubapi_key = os.environ.get("GITHUB_API_KEY")
        self.google_api_key = os.environ.get("google_api_key")
        self.google_cse_id = os.environ.get("google_cse_id")

        api_key = 'AIzaSyA4mrDI68iynEqeOlEReYJSYJ6kO9e9dd8'
    cse_id = '81a7285d41aea4983'
        
    def general_query(self,prompt):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
            temperature=1.2,
            max_tokens=1000
        )
        return response.choices[0].message.content

    def json_query(self,prompt):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a JSON code generation assistant. You are designed to output JSON"},
                {"role": "user", "content": prompt},
            ],
            response_format={ "type": "json_object" },
            temperature=1.2,
            max_tokens=600
        )
        return json.loads(response.choices[0].message.content)