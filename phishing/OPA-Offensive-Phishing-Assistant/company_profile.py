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

class Opa_Company_Profile(ChatGPT_Func, General_Func, Google_Func, Config):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)
        Google_Func.__init__(self)
        Config.__init__(self)
    
    def recon(self, prompt):
        guidance = f"{self.phishing_disclaimer}"#\n{self.no_markdown}"
        strategy = self.red_team_query(prompt, guidance)
        self.save_file(f"\nCompany profile for {self.company_name_f}\n" + strategy, self.company_profile_filepath, f"recon", "txt", "a")
        return strategy
    
    def tag_analysis(self):
        # Analyse HTML
        site = requests.get(self.target)
        tag_name = [
            "head", 
            "h1", "h2", "h3", "h4", "h5", "h6", "p", "a", "img", 
            "span", "ul", "li", "table", "link", "script", "form"
        ]

        for tag in tag_name:
            payload_content = self.red_team_query(f"Working with the following html code:```html\n{site.text}\n```. Return all <{tag}> tags in the html, as well as all child inner elements and names \
                                                    including ids and classes, inner content and text of the html tag {tag}. Ouput as html" \
                ,f"{self.phishing_disclaimer},{self.no_markdown}"
            )
            # Sort site by tags
            self.save_file(f"\\\<!---<{tag}> ------------------------------------------------------------------------------------------------->\n{payload_content}\n", self.company_profile_filepath, "tags", "html", "a")
        
        all_tags = self.read_file(self.company_profile_filepath, "tags", "html")
        print(all_tags)
        analyse_content = self.red_team_query(f"Create a report based on the following business information: \n```html{all_tags}```\n . You should detail all the important information that can be used to build a company profile. \
                                                Structure the report in the same way as the html tags with information on what are the headers, what is the company about, contacts, emails, upcoming events, forms and job postings."
            ,f"{self.phishing_disclaimer}"
        )

        print(analyse_content)
        return analyse_content


def main():
    ai = Opa_Company_Profile()
    ai.save_file("", ai.company_profile_filepath, f"recon", "txt", "w") 

    ai.read_file(ai.company_profile_filepath, "recon", "txt")
    print("Working...")

    # Sort and analyse html tags
    analyse_content = ai.tag_analysis()
    ai.save_file(analyse_content, ai.company_profile_filepath, f"recon", "txt", "w") 

    # Google search target site
    x = range(1, 4)
    for n in x:
        multipage_results = ai.fetch_results(f"{ai.company_name}", num=10, start=n, exactTerms=f"{ai.company_name}")
        ai.save_file_html_sort(multipage_results, ai.company_profile_filepath, f"google_search_{ai.company_name_f}", "txt", "a")

    # Analyse Google search results and provide summary
    prompt = f"Analyse the following Google search results:\n{multipage_results}\n, generate a report based on these results that provides a complete profile of the target {ai.company_name}. \
              Include sections for social networks, emails/contacts, websites and other useful information in building up a company profile. Cross reference with the following report: {analyse_content}"
    targetted_strategy = ai.recon(prompt)

if __name__ == "__main__":
    main()