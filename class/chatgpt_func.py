import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import json

class ChatGPT_Func:
    no_markdown =  "Strictly output the working code only with no markdown. Just the raw code. ' \
                    Do not include any markdown such as ```php or ```python as this will break the script. Strictly no comments, markdown or description. Just legal code"

    def __init__(self):
        # Initialize with ChatGPT API
        _ = load_dotenv(find_dotenv())
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )
        
    def general_query(self,prompt):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an offensive cybersecurity pentration testing trainer."},
                {"role": "user", "content": prompt},
            ],
            temperature=1.2,
            max_tokens=600
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