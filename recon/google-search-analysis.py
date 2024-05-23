"""
Reconnaissance Techniques Using ChatGPT
Google Search and analysis
["Implement ChatGPT to analyze social media posts, extracting potential security lapses or useful information about the target's infrastructure.", 
'Apply ChatGPT to process data from forums and tech blogs for mentions of the target and related vulnerabilities.', 
'Use ChatGPT to summarize news articles and reports that mention the target, identifying potential entry points.']
This script is for for training purposes only
"""
import requests
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)

from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class Google_Search_Analysis(ChatGPT_Func, General_Func):
    def __init__(self):
        # Initialize the Google Search API instance with an API key and a Custom Search Engine ID.
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

        # Set API key in .env
        self.api_key = self.google_api_key
        self.cse_id = self.google_cse_id
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

def main():
    ai = Google_Search_Analysis()
    query = 'PointlessAI'

    # Additional parameters can be added directly in the function call
    # https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list
    """
    ?c2coff=1&
    cr=uk&
    dateRestrict=d[10]
    exactTerms=PointlessAI&
    excludeTerms=Pointltess%20AI&
    fileType=html&
    filter=0&
    gl=uk&
    highRange=100&
    hq=fun%20times&
    linkSite=pointlessai.com&
    num=10&
    orTerms=pai&
    q=pointlessai&
    safe=off&
    siteSearch=pointlessai.com&
    sort=date&
    start=11&
    prettyPrint=true&
    key=[YOUR_API_KEY]
    """

    # Loop through first 4 pages of Google
    x = range(1, 4)
    search_res_arr = []

    for n in x:
        results = ai.fetch_results(query, num=10, start=n, dateRestrict='m[10]', exactTerms='PointlessAI')

        # Print the results
        print(results)
        if 'items' in results:
            for item in results['items']:
                search_res_arr.append(f"Title: {item['title']} - Link: {item['link']} - Snippet: {item['snippet']}")
                print(f"Title: {item['title']}")
                print(f"Link: {item['link']}")
                print(f"Snippet: {item['snippet']}")
                print("-" * 80)

    # Analyse search results and provide actionable intelligence
    google_res_analysis = ai.general_query(f"Analyse the search results in {search_res_arr} and provide an assessment of the company {query} current activities.")
    print(google_res_analysis)

    google_res_analysis = ai.general_query(f"Analyse the search results in {search_res_arr} and provide a list of all discovered accounts for the company {query}.")
    print(google_res_analysis)

    google_res_analysis = ai.general_query(f"Analyse the search results in {search_res_arr} and provide a list of all employees of {query}.")
    print(google_res_analysis)

if __name__ == "__main__":
    main()