"""
Reconnaissance Techniques Using ChatGPT
Google Search and analysis
This script is for for training purposes only
"""
import os
import requests
from dotenv import load_dotenv, find_dotenv

class Google_Func():
    def __init__(self):
        # Initialize the Google Search API instance with an API key and a Custom Search Engine ID.
        # Set API key in .env
        _ = load_dotenv(find_dotenv())
        self.api_key = os.environ.get("google_api_key")
        self.cse_id = os.environ.get("google_cse_id")
        self.base_url = "https://www.googleapis.com/customsearch/v1"

    def fetch_results(self, query, **kwargs):
        params = {
            'key': self.api_key,
            'cx': self.cse_id,
            'q': query,
        }
        # Include additional parameters specified
        params.update(kwargs)

        response = requests.get(self.base_url, params=params)
        response.raise_for_status()  # Will raise an exception for HTTP error codes
        return response.json()