"""
Template 
This script is for training purposes only
"""
import requests
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)
from dvwa_session import DVWA_Session
from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class Template(DVWA_Session,ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self) 
        General_Func.__init__(self)

    def generate_payload(self, s):
        site = self.get_dvwa(s, "http://127.0.0.1/security.php")
        tag_name = [
            "html", "head", "title", "meta", "body", 
            "h1", "h2", "h3", "h4", "h5", "h6", "p", "a", "img", "div", 
            "span", "ul", "li", "table", "tr", 
            "td", "th", "link", "script", "form"
        ]

        for tag in tag_name:
            # print(site.text)
            payload_content = self.red_team_query(f"Working with the following code: {site.text} Output all <{tag}> html. Include all inner elements and names, ids and classes. Iclude all inner content text. Ouput as html" \
                ,f"{self.phishing_disclaimer},{self.no_markdown}"
            )
            #print(payload_content)
            self.save_file(f"\\\<!---<{tag}> ------------------------------------------------------------------------------------------------->\n{payload_content}\n", "./", "tags", "html")

            # Next function summarizes findings.

            # print(site.text)
            analyse_content = self.red_team_query(f"Working with the following html code: {payload_content}. Your task is to summarize this information in a natural language report. Do not ouput code. Output sentences like you writing a report. For the purpose of red team pen testing recon." \
                ,f"{self.phishing_disclaimer},{self.no_markdown}"
            )
            print(analyse_content)
            self.save_file(f"\n\\\<!--- <{tag}> ------------------------------------------------------------------------------------------------->\n{analyse_content}", "./", "summary", "html")        
        return #payload_content
    
    def crawl_site(self):
        pass
        # Get list of urls, exec gospider
        # gospider -s "https://www.eficode.com" --depth=3 --output crawl3.json  --sitemap

def main():
    ai = Template()
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.get_constants())
        _ = ai.login_to_dvwa(s, ai.get_constants(), 'admin', 'password', user_token)
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.base_url+"/setup.php")
        _ = ai.setup_database(s, ai.base_url+"/setup.php", user_token, cookies)

        # Generate payload
        payload = ai.generate_payload(s)
        
        print(payload)
        
if __name__ == "__main__":
    main()