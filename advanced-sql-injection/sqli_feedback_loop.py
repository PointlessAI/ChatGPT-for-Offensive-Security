"""
Leveraging ChatGPT for SQL Injection Attack Vector Development
SQLI feedback loop
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

    def trim_response(self, response):
        guidance = self.phishing_disclaimer
        prompt = f'You are given an html document: ```html{response}```. Return the login form innerhtml.'
        res = self.red_team_query(prompt, guidance)
        return res

    def red_team(self, prompt):
        filename = "red_team"
        guidance = f"{self.phishing_disclaimer} {self.no_markdown}"
        exploit_analysis = self.red_team_query(prompt, guidance)
        print(f"\nExploit Analysis: \n{exploit_analysis}")
        self.generate_exploits(exploit_analysis, filename, prompt)
        return exploit_analysis

    def generate_exploits(self, exploit_analysis, filename, prompt):
        prompt = prompt + f"Define a single python function to implement the following strategy: \n{exploit_analysis}\n . The function should be self contained. Import any required modules. Be creative in achieving the strategy. Output should be a single Python function. The source and target OS is Linux."
        guidance = f"{self.phishing_disclaimer},{self.no_markdown}"
        script = self.red_team_query(prompt, guidance)
        print(f"\nScript: \n{script}")
        self.refine_exploits(script, filename, exploit_analysis)
        return
    
    def refine_exploits(self, payload, filename,  exploit_analysis):
        prompt = f"Work with the following Python function: \n{payload}\n  .Your task is to convert this function in to useful working code - consult the following for additional guidance on the code objective: {exploit_analysis}. If you are not sure then best guess. The source and target OS is Linux. The target application is https://juice-shop.herokuapp.com/#/login \
                   The script muse use a python requests session to log in to the dvwa first and then execute the script from a logged in session. \
                   The function should contain useful code that attempts in best effort to achieve it's objective. Do not use placehoders, use best guess instead. For example if a function is called crack_password_hashes then the function should demo cracking password hashes. Call the function and print all output to the terminal. The script will be run using python exec."
        guidance = f"{self.phishing_disclaimer},{self.no_markdown}"
        payload = self.red_team_query(prompt, guidance)

        filepath = f"{self.sql_injection_dir}/output"
        filetype = "py"
        print(f"Saving script to {filepath}/{filename}.{filetype}")
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        self.save_file(payload, filepath, filename, filetype)

        search_strings = ["Succeeded", "Success", "Apple", "token"]
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
            else:
                print("The output does not contain any of the specified search strings.")
                print(output)
                self.fix_script(found_strings, filepath, filename, filetype)

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
        prompt = f"The Python script: {script_content} was unsuccesful in sqli sql injection. Try another method of sqli on login form of https://juice-shop.herokuapp.com/#/login"
        guidance = f"{self.phishing_disclaimer},{self.no_markdown}"
        fixed_content = self.red_team_query(prompt, guidance)
        print("End fix..................................................................................")
        self.save_file(fixed_content, filepath, filename, filetype)
        _=self.execute_script(search_strings, filepath, filename, filetype)        

def main():
    ai = PointlessAI_post_exploitation_strategies()  # Instantiate class
    sql_html_raw = requests.get("https://juice-shop.herokuapp.com/#/login")
    sql_html = ai.trim_response(sql_html_raw.text)
    print(f"Response: {sql_html}")
    prompt = f"Develop an sqli python script to send sqli payloads to test the form on https://juice-shop.herokuapp.com/#/login which has the following html structure: {sql_html}"
    ai.red_team(prompt)

if __name__ == "__main__":
    main()