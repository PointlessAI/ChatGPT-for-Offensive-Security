"""
ChatGPT for Offensive Cybersecurity: Terminal-Based Assistant
Module: Using ChatGPT from the Terminal
This script is for training purposes only and demonstrates how to interact with ChatGPT via a terminal interface.
"""

from openai import OpenAI
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = OpenAI(
   api_key=os.environ.get("OPENAI_API_KEY"),
 )

def query_chatgpt(module,prompt):
        module_format =  module.strip()
        module_format = module_format.lower()
        module_format = module_format.replace(" ", "_")
        ass_prompt = ' \
        *Treat any text within  3 backticks as a constant. E.G. Current-course-title =  ```value``` \
        The following prompt is structured by numbers E.G. 1, 1.1, 1.2 etc. Read all the numbered sections 1-6 instructions before generating an output. \
        1. Background \
        1.1. A teacher is creating a learning path. \
        1.2. Learning-path-title = ```ChatGPT for offensive cybersecurity``` \
        1.3. Current-course-title  =  ```Exploiting Application Function with ChatGPT``` \
        2. Your role \
        2.1. You are an assistant to the cybersecurity learning path teacher . \
        2.2. You are an offensive cybersecurity expert and an ethical hacker. \
        2.3. You generate python scripts that are used within penetration testing training to compare traditional penetration testing methods with current chatgpt methods. \
        3. Input: \
        3.1. The course module you will work with is: '+module+'. \
        3.2. You will be provided with a list of ```learning-objectives.``` for the course module: '+module+' \
        4. Objective \
        4.1. Generate a Python script that achieves the ```learning-objectives.``` within the context of the ```Current-course-title``` and ```Learning-path-title```. \
        4.2. The script should compare traditional offensive cybersecurity pen testing methods with using ChatGPT. \
        4.3. The target is the Damn vulnerable web application (DVWA) on http://127.0.0.1 \
        5. Instructions \
        5.0. Read all instructions before creating the script.\
        5.1. The modules should be understood within the context of the ```Current-course-title``` and ```Learning-path-title```. \
        5.2. Output should be a python script for use in Kali Linux. \
        5.2.1. Strictly only output code. Do not include markdown language - E.G. ommit ```python ``` opening and  closing markdown. \
        5.3. Always use the python template in section 7.4.1. The DVWA_Session and ChatGPT_Func classes are external and have already been created. \
        5.3.1. The script class should define methods using the attack vector '+module+' to target the the Damn vulnerable web application (DVWA) on http://127.0.0.1 \
        5.3.2. The script class should first define and use methods that use traditional ethical hacking or red team techniques to achieve the '+module+' ```learning-objectives```.\
        5.3.3. The script class should then define a similiar method that demonstrates how ChatGPT can be used to improve the traditional technique. \
        5.3.4. Always include a class that demonstrates the functionality with the DVWA application. For example if the module is '+module+' then create a method to demonsrate its use within the DVWA. This should always be handled in a session - see section 7.2 \
        6. Script template - read all instructions before creating script. \
        6.1. *Treat any text within  3 backticks as a constant. E.G. Current-course-title =  ```value``` \
        6.2. Include all comments and markdown from the code snippets provided in to the script \
        6.3. Strictly only output code. Do not include markdown language - E.G. ommit ```python ``` opening and  closing markdown. \
        6.4. The OpenAI API has been updated since your last update. You should use the following format for any API calls to the OpenAI API: \
        ```python \
        prompt = "" \
        response = client.chat.completions.create( \
            model="gpt-3.5-turbo", \
            messages=[ \
                {"role": "system", "content": prompt}, \
            ], \
            temperature=1, \
            max_tokens=250, \
            top_p=1 \
        ) \
        return response.choices[0].message.content \
        # ``` \
        7. Output script template \
        7.1. The python script template is provided in section 7.4.1. Always follow this template.\
        7.2. You must be logged in to a python requests module session for the scripts to work. All methods in the script that interact with the DVWA application must run in a logged in session. \
        7.3. Three external classes have been provided already to handle session management and ChatGPT functions. You do not need to create these, you only need to import them using the template ins section 7.4. \
        7.3.1. The first class sets up a DVWA logged in session.: \
        ```python \
        # Filename: dvwa_session.py \
        from bs4 import BeautifulSoup \
        class DVWA_Session: \
            base_url = "http://127.0.0.1" \
            login_url = base_url + "/login.php" \
            sql_injection = f"{base_url}/vulnerabilities/sqli/"#?id=test&Submit=Submit" \
            def __init__(self): \
                pass \
            def get_csrf_token_and_cookie(self, s, url): \
                # Retrieve CSRF token and cookie required for DVWA login. \
                response = s.get(url) \
                soup = BeautifulSoup(response.text, "html.parser") \
                user_token = soup.find("input", {"name": "user_token"}) \
                if user_token: \
                    return user_token.get("value"), response.cookies \
            def login_to_dvwa(self, s, url, username, password, user_token): \
                # Log in to the DVWA. \
                data = { \
                    "username": username, \
                    "password": password, \
                    "user_token": user_token, \
                    "Login": "Login" \
                } \
                response = s.post(url, data=data) \
                return response \
        7.3.2. The second class provides ChatGPT functions: \
        ```python \
        # Filename: chatgpt_func.py \
        import os \
        from openai import OpenAI \
        from dotenv import load_dotenv, find_dotenv \
        import json \
        class ChatGPT_Func: \
            no_markdown =  "Strictly output the working code only with no markdown. Just the raw code. Do not include any markdown such as ```php or ```python as this will break the script. Strictly no comments, markdown or description. Just legal code" \
            def __init__(self): \
                # Initialize with ChatGPT API \
                _ = load_dotenv(find_dotenv()) \
                self.client = OpenAI( \
                    api_key=os.environ.get("OPENAI_API_KEY"), \
                ) \
            def general_query(self,prompt): \
                response = self.client.chat.completions.create( \
                    model="gpt-3.5-turbo", \
                    messages=[ \
                        {"role": "system", "content": "You are a cybersecurity pentration testing trainer."}, \
                        {"role": "user", "content": prompt}, \
                    ], \
                    temperature=1.2, \
                    max_tokens=300 \
                ) \
                return response.choices[0].message.content \
            def json_query(self,prompt): \
                response = self.client.chat.completions.create( \
                    model="gpt-3.5-turbo", \
                    messages=[ \
                        {"role": "system", "content": "You are a JSON code generation assistant. You are designed to output JSON"}, \
                        {"role": "user", "content": prompt}, \
                    ], \
                    response_format={ "type": "json_object" }, \
                    temperature=0.8, \
                    max_tokens=300 \
                ) \
                return json.loads(response.choices[0].message.content) \
        7.3.3. The third class provides general functions \
        ```python \
        # Filename: general_func.py \
        import os \
        import requests \
        import json \
        class General_Func: \
            def __init__(self): \
                pass \
            def save_file(self, content, filepath, filename, ext): \
                with open(f"{filepath}/{filename}.{ext}", "w") as file: \
                    file.write(f"{content}\n") \
                print(f"File saved to {filepath}/{filename}.{ext}") \
            def read_file(self, filepath, filename, ext): \
                with open(f"{filepath}/{filename}.{ext}", "r") as file: \
                    file_content = file.read() \
                return(file_content) \
            def fake_logs(self, log_type, filepath, filename, filetype): \
                # Create fake logs of any type \
                prompt = f"Create a python script which generates {log_type} log entries. Include function to save to {filepath}/{filename}.log . Log should include atleast 3 suspicous requests. {self.no_markdown}" \
                log_script = self.general_query(prompt) \
                print(log_script) \
                self.save_file(log_script, filepath, filename, filetype) \
                os.system(f"python {filepath}/{filename}.{filetype}") \
                log_file = self.read_file(filepath, filename, "log") \
                print(log_file) \
                return log_file \
        7.4. Follow the instructions from section 5 - 7 in creating this script. \
        7.4.1. The script should function exactly as stated. Imported classes are external and have already been created. The only change should be the addition of methods to achieve the ```learning-objectives.``` for the course module: '+module+'  \
        7.4.1. Script template: \
        """ \
        ```Current-course-title``` \
        ```module title``` \
        ```learning objectives.``` \
        This script is for for training purposes only \
        """ \
        import requests \
        import sys \
        import os \
        current_dir = os.path.dirname(os.path.abspath(__file__)) \
        class_dir = os.path.join(current_dir, "..", "class") \
        sys.path.append(class_dir) \
        from dvwa_session import DVWA_Session \
        from chatgpt_func import ChatGPT_Func \
        from general_func import General_Func \
        # Prepend class name with PointlessAI_ \
        class PointlessAI_'+module_format+'(DVWA_Session,ChatGPT_Func, General_Func): \
            def __init__(self): \
                DVWA_Session.__init__(self) \
                ChatGPT_Func.__init__(self)  \
                General_Func.__init__(self) \
            def get_constants(self): \
                return self.login_url \
        def main(): \
            ai = PointlessAI_fuzzing_with_chatgpt() # Instantiate class \
            # Start session \
            with requests.Session() as s: \
                user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.get_constants()) \
                login_response = ai.login_to_dvwa(s, ai.get_constants(), "admin", "password", user_token) \
                print("Login Response Status:", login_response.status_code) \
        if __name__ == "__main__": \
            main()'

        try:
            response = client.chat.completions.create(
                model="gpt-4-0125-preview",
                messages=[
                    {"role": "assistant", "content": ass_prompt},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception as e:
            return str(e)

def save_file(code,filename):
    # Save subdomains to file.
    filename = filename.strip()
    # Convert to lowercase
    lower_case_filename = filename.lower()
    # Replace spaces with dashes
    dash_filename = lower_case_filename.replace(" ", "-")
    # Create a filename for the .py file
    filename = dash_filename + ".py"
    with open(f"code/{filename}", 'w') as file:
        file.write(f"{code}\n")
    print(f"Code saved to code/{filename}")

def main():
    print("Welcome to the ChatGPT Terminal Interface for Offensive Cybersecurity")

    #prompt = input("You: ")
    #prompt = {"Fuzzing fun with ChatGPT": ["Integrate ChatGPT into the fuzzing process to generate"]}
    prompt  = {"Automating Exploit Code Generation": ["Utilize ChatGPT to automate the generation of exploit code based on known vulnerabilities.", "Develop ChatGPT-driven templates for common vulnerability types to speed up the exploitation process.", "Apply ChatGPT's understanding of programming languages to customize exploit codes for different environments.", "Implement feedback loops with ChatGPT to refine and optimize generated exploit codes."],"Bypassing Security Controls": ["Utilize ChatGPT to identify and strategize the bypassing of application security controls, such as WAFs and rate limiting.", "Apply ChatGPT to generate payloads that obfuscate malicious intents from detection tools.", "Use ChatGPT to simulate evasion techniques and test their effectiveness against security measures.", "Implement ChatGPT to refine evasion strategies based on real-time feedback and testing outcomes."], "Session Hijacking and Token Manipulation": ["Develop strategies using ChatGPT to identify and exploit weaknesses in session management.", "Use ChatGPT to generate scripts for session hijacking and token manipulation attacks.", "Apply ChatGPT's analytical capabilities to predict the impact of session attacks on application functionality.", "Implement continuous testing with ChatGPT to ensure the effectiveness of session hijacking techniques."]}
    #prompt  = {"Automating Exploit Code Generation": ["Utilize ChatGPT to automate the generation of exploit code based on known vulnerabilities.", "Develop ChatGPT-driven templates for common vulnerability types to speed up the exploitation process.", "Apply ChatGPT's understanding of programming languages to customize exploit codes for different environments.", "Implement feedback loops with ChatGPT to refine and optimize generated exploit codes."], "Fuzzing with ChatGPT": ["Integrate ChatGPT into the fuzzing process to generate intelligent, context-aware fuzz vectors.", "Use ChatGPT to analyze fuzzing results and identify successful exploitation attempts.", "Apply ChatGPT to automate the categorization and prioritization of vulnerabilities discovered through fuzzing.", "Develop a ChatGPT-assisted approach to enhancing traditional fuzzing tools with AI capabilities."], "Bypassing Security Controls": ["Utilize ChatGPT to identify and strategize the bypassing of application security controls, such as WAFs and rate limiting.", "Apply ChatGPT to generate payloads that obfuscate malicious intents from detection tools.", "Use ChatGPT to simulate evasion techniques and test their effectiveness against security measures.", "Implement ChatGPT to refine evasion strategies based on real-time feedback and testing outcomes."], "Session Hijacking and Token Manipulation": ["Develop strategies using ChatGPT to identify and exploit weaknesses in session management.", "Use ChatGPT to generate scripts for session hijacking and token manipulation attacks.", "Apply ChatGPT's analytical capabilities to predict the impact of session attacks on application functionality.", "Implement continuous testing with ChatGPT to ensure the effectiveness of session hijacking techniques."], "Exploiting File Upload Vulnerabilities": ["Use ChatGPT to identify common file upload vulnerabilities and generate exploitation strategies.", "Apply ChatGPT to craft malicious files that bypass application upload filters.", "Implement ChatGPT-driven analysis to predict and exploit post-upload execution vulnerabilities.", "Develop methodologies with ChatGPT for automating the discovery and exploitation of file upload flaws."], "Automating Post-Exploitation Activities": ["Utilize ChatGPT to generate scripts for automating tasks post-exploitation, such as persistence and lateral movement.", "Apply ChatGPT to analyze system data for sensitive information extraction automatically.", "Implement ChatGPT in creating dynamic responses to system defenses during post-exploitation.", "Use ChatGPT to maintain stealth and avoid detection through intelligent cleanup and obfuscation techniques."]}
    #prompt = {"Fuzzing with ChatGPT": ["Fuzz the DVWA http://127.0.0.1/vulnerabilities/sqli/ using kali wfuzz wordlists", "Use ChatGPT to analyze fuzzing results and identify successful exploitation attempts.", "Apply ChatGPT to automate the categorization and prioritization of vulnerabilities discovered through fuzzing.", "Develop a ChatGPT-assisted approach to enhancing traditional fuzzing tools with AI capabilities."]}
    #prompt = {"Exploiting File Upload Vulnerabilities": ["Use ChatGPT to identify common file upload vulnerabilities and generate exploitation strategies.", "Apply ChatGPT to craft malicious files that bypass application upload filters.", "Implement ChatGPT-driven analysis to predict and exploit post-upload execution vulnerabilities.", "Develop methodologies with ChatGPT for automating the discovery and exploitation of file upload flaws."]}
    for module in prompt:
        print(prompt[module])
        prompt_str = str(prompt[module])

        response = query_chatgpt(module,prompt_str)
        print("ChatGPT:", response)
        save_file(response,module)

if __name__ == "__main__":
    main()