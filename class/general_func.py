import os
import requests
import json

class General_Func:
    def __init__(self):
        pass

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