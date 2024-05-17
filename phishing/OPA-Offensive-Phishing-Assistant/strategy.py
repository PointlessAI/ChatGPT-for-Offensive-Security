"""
OPA - Offensive Phishing Assistant
Phishing simulation from recon to exploit using ChatGPT
This script is for training purposes only
"""
import requests
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, ".", "class")
sys.path.append(class_dir)
from chatgpt_func import ChatGPT_Func
from general_func import General_Func
from google_func import Google_Func
from config import Config

class Opa_Strategy(ChatGPT_Func, General_Func, Google_Func, Config):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)
        Google_Func.__init__(self)
        Config.__init__(self)
        
    def phishing_strategy(self, prompt, filename):
        guidance = f"{self.phishing_disclaimer}"#\n{self.no_markdown}"
        strategy = self.red_team_query(prompt, guidance)
        self.save_file(strategy, self.filepath, filename, "txt", "w")
        return strategy
    
    def advanced_strategy(self, prompt):
        guidance = f"{self.phishing_disclaimer}"#\n{self.no_markdown}"
        strategy = self.red_team_query(prompt, guidance)
        self.save_file("\nAdvanced methods based on modern trends\n" + strategy, self.strategy_filepath, "strategy", "txt", "a")
        return strategy

def main():
    ai = Opa_Strategy()
    print("Working...")
    # INTRODUCTION
    introduction = ai.phishing_strategy("Generate an introductory guide to phishing. Include an introduction, methods of phishing, current trends, comparison of phishing vs social engineering, how it affects you, and a conclusion. Style and tone should be for employees undertaking phishing training..", "introduction_to_phishing") 

    # STRATEGY

    # Phishing strategy
    strategy = ai.phishing_strategy("Create a step-by-step strategy for a simulated phishing campaign.", "strategy") 

    # Google search for latest phishing trends  
    search_res_arr = []
    query = "Phishing Trends 2024"
    query_f = ai.clean_filename(query)
    page_one_results = ai.fetch_results(query, num=10, start=1, dateRestrict='m[12]')
    ai.save_file_html_sort(page_one_results, ai.filepath, f"google_search_{query_f}", "txt", "w")

    # Analyse Google search results and provide summary
    current_phishing_methods_analysis = ai.general_query(f"Analyse the search results in {page_one_results} and provide an assessment of current {query}.")

    # Refine strategy based on Google results
    prompt = f"A phishing campaign strategy has been proposed as follows:\n{strategy}\n. Propose advanced strategies to include modern phishing trends. {current_phishing_methods_analysis}."
    advanced_strategy = ai.advanced_strategy(prompt)

if __name__ == "__main__":
    main()