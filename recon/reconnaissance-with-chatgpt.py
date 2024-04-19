"""
Reconnaissance Techniques Using ChatGPT
Reconnaissance with ChatGPT
Learning objectives: Utilize ChatGPT to automate the collection of public domain information about a target,
implement custom scripts that interact with ChatGPT to parse and summarize findings from various online sources,
and apply ChatGPT's language capabilities to craft social engineering attacks based on gathered intel.
This script is for training purposes only.
"""

import requests
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

# Load the environment variable from .env file
_ = load_dotenv(find_dotenv())

# Initialize OpenAI client with API key
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

class Reconnaissance:
    def __init__(self, target):
        self.target = target
        self.data_sources = {
            'google': f"https://www.google.com/search?q={target}",
            'linkedin': f"https://www.linkedin.com/search/results/people/?keywords={target}",
            'twitter': f"https://twitter.com/search?q={target}&src=typed_query"
        }
        self.collected_data = {}

    def fetch_data(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        for source, url in self.data_sources.items():
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                self.collected_data[source] = response.text
            else:
                print(f"Failed to fetch data from {source}")

    def analyze_data_with_chatgpt(self):
        summaries = {}
        for source, data in self.collected_data.items():
            prompt = f"Summarize the key information about {self.target} from the following data source: {source}\n\n{data}"
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": prompt},
                ],
                temperature=1,
                max_tokens=250,
                top_p=1
            )
            summaries[source] = response.choices[0].message.content
        return summaries

    def prepare_social_engineering(self, summaries):
        social_engineering_strategies = {}
        for source, summary in summaries.items():
            prompt = f"Based on the following summary from {source}, suggest potential social engineering tactics: {summary}"
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": prompt},
                ],
                temperature=1,
                max_tokens=250,
                top_p=1
            )
            social_engineering_strategies[source] = response.choices[0].message.content
        return social_engineering_strategies

# Example usage:
target = "PointlessAI"
recon = Reconnaissance(target)
recon.fetch_data()
summaries = recon.analyze_data_with_chatgpt()
social_engineering_approaches = recon.prepare_social_engineering(summaries)

print("Summarized Data: ", summaries)
print("Suggested Social Engineering Tactics: ", social_engineering_approaches)
