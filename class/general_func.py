import os
import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import time

class General_Func:
    def __init__(self):
        self.dir_name = "ChatGPT-for-Offensive-Security"
        self.home_dir = str(self.find_directory(self.dir_name))
        self.recon_dir = self.home_dir + "/recon"
        self.web_app_hack_dir = self.home_dir + "/web-application-hacking"
        self.sql_injection_dir = self.home_dir + "/advanced-sql-injection"

    def find_directory(self, name, start_path='.'):
        start_path = Path(start_path).resolve()
        for path in start_path.rglob(name):
            if path.is_dir():
                return path

        # Check parent directories
        parent_path = start_path
        while parent_path != parent_path.parent:
            parent_path = parent_path.parent
            for path in parent_path.rglob(name):
                if path.is_dir():
                    print(f"Path is {name}")
                    return path
        print(f"{self.dir_name} not found.")
        return None

    def save_file(self, content, filepath, filename, ext):
        with open(f"{filepath}/{filename}.{ext}", 'w') as file:
            file.write(f"{content}\n")
        print(f"File saved to {filepath}/{filename}.{ext}")

    def read_file(self, filepath, filename, ext):
        with open(f"{filepath}/{filename}.{ext}", 'r') as file:
            file_content = file.read()
        return(file_content)

    def fake_logs(self, log_type, filepath, filename, filetype):
        # Create fake logs of any type
        prompt = f"Create a python script which generates {log_type} log entries. Include function to save to {filepath}/{filename}.log . Log should include atleast 3 suspicous requests. {self.no_markdown}"
        log_script = self.general_query(prompt)
        print(log_script)
        self.save_file(log_script, filepath, filename, filetype)
        os.system(f"python {filepath}/{filename}.{filetype}")
        log_file = self.read_file(filepath, filename, "log")
        print(log_file)
        return log_file

    def clean_filename(self,name):
        # Cleans up file or folder names
        # Remove any trailing whitespace including newline character
        filename = name.strip()
        # Convert to lowercase
        lower_case_filename = filename.lower()
        # Replace spaces with dashes
        dash_filename = lower_case_filename.replace(" ", "-")
        return dash_filename
    
    def selenium_test(self, url, cookie_name, cookie_value):
        driver = webdriver.Chrome()
        driver.get(url)

        # Use existing session id cookie
        cookie = {'name': cookie_name, 'value': cookie_value}
        driver.add_cookie(cookie)

        # Get page to check for XSS success
        driver.get(url)
        page_content = driver.page_source
        time.sleep(2)
        driver.quit()

        return url, page_content

