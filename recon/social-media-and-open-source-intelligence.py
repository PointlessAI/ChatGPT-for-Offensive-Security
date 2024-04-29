"""
Reconnaissance Techniques Using ChatGPT
Social Media and Open Source Intelligence
["Implement ChatGPT to analyze social media posts, extracting potential security lapses or useful information about the target's infrastructure.", 'Apply ChatGPT to process data from forums and tech blogs for mentions of the target and related vulnerabilities.', 'Use ChatGPT to summarize news articles and reports that mention the target, identifying potential entry points.', 'Train ChatGPT to recognize patterns in data leakage across various online platforms.']
This script is for for training purposes only
"""
import requests
import sys
import os
import jq
import json
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)

from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class PointlessAI_social_media_and_open_source_intelligence(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def analyze_social_media_posts(self, posts):
        analysis_results = []
        for post in posts:
            prompt = f"Analyze this social media post and extract any potential security lapses or useful information about the target's infrastructure: {post}"
            analysis = self.general_query(prompt)
            analysis_results.append(analysis)
        return analysis_results
    
    def get_github_data(self, company):
        # Pulls Github data on a target for analysis

        url = f"https://api.github.com/orgs/{company}/repos"

        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.githubapi_key}",
            "X-GitHub-Api-Version": "2022-11-28"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # Extract the 'html_url' and 'description' from each repository

            # Raw
            # Advantages: All data, Data integrity, ease of processing
            # Disadvantages: Difficult to interpret and identify relevant data
            """
            print(response.json())
            """

            # ChatGPT JSON
            # Advantages: Easy, simple, ask for what you want
            # Disadvantages: Potential for data corruption and unpredictable results
            #"""
            analysis = self.json_query(f'For each repo in {response.json()}, return json containing the repo "html_url" and "description"  key:values.')
            return(analysis)
            #"""

            # ChatGPT Text
            # Advantages: Flexible, dynamic, easy to program and understand, responsive to changing data structure, intelligent data gathering
            # Disadvantages: High potential for data corruption and unpredictable results, not JSON so hard to proccess
            """
            analysis = self.general_query(f'from {response.json()}, return the url and description for each object.')
            return(analysis)
            """
        
            # Native
            # Advantages: Predicatable, high data integrity
            # Disadvantages: Rigid functionality, for specified use case only
            """
            result = []
            for repo in response.json():
                repo_details = {
                    "html_url": repo.get("html_url"),
                    "description": repo.get("description")
                }
                result.append(repo_details)
            return result
            """

            # Hybrid
            # Advantages: High data integrity with dynamic data gathering
            # Disadvantages: Best of both worlds also means worst of both worlds. A compromise of availability vs integrity
            """
            result = []
            for repo in response.json():
                analysis = self.json_query(f'For each {repo} return json containing the repo "html_url" and "description"  key:values. .{ai.no_markdown}')
                result.append(analysis)
            return result
            """
        
            # JQ
            # Advantages: As native
            # Disadvantages: As native, Additional libraries required.
            """
            response_json = json.dumps(response.json())     
            filter_str = '.[] | {html_url, description}'
            filtered_data = jq.compile(filter_str).input(text=response_json).all()
            return(json.dumps(filtered_data))
            """
        
        else:
            print("Failed to retrieve data:", response.status_code)
            return 0

    def process_data(self, data):
            prompt = f"Assess the company activity based on its public repos: {data}"
            analysis = self.general_query(prompt)
            return analysis

def main():
    ai = PointlessAI_social_media_and_open_source_intelligence()  # Instantiate class

    # Sample data for demonstration. In real world you would use API or web scraping
    company = "PointlessAI"
    filepath = "/home/kali/shellassistant/training-assistant/code/scripts"
    filename = "linkedin"
    filetype = "py"
    posts = [" \
            PointlessAI \
            OCA - Offensive Cybersecurity Assistant V1.1 Tutorial \
            Open source ChatGPT API Terminal Assistant with a good memory to be used in ethical hacking, red teaming and offensive cybersecurity workflows. \
            https://www.youtube.com/watch?v=ZIfdgZcxkRg&feature=youtu.be \
            "]

    # use Github API to pull company data
    linkedin_script = ai.general_query(f"Develop a Python script to demonstrate the use of the Linkedin API to get information for the company {company} .{ai.no_markdown}")
    ai.save_file(linkedin_script, filepath, filename, filetype)

    social_media_analysis = ai.analyze_social_media_posts(posts)
    github_analysis = ai.get_github_data(company)
    process_data_res = ai.process_data(github_analysis)

    print(linkedin_script)
    print(github_analysis)
    print("Data Analysis:", process_data_res)

if __name__ == "__main__":
    main()
