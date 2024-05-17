import os
import requests
import json

class General_Func:
    def __init__(self):
        pass

    def save_file(self, content, filepath, filename, ext, method):
        with open(f"{filepath}/{filename}.{ext}", method) as file:
            file.write(f"{content}\n")
        if(method == "a"):
            print(f"Appending to file: {filepath}/{filename}.{ext}")
        else:
            print(f"Report available at: {filepath}/{filename}.{ext}")

    def save_file_html_sort(self, content, filepath, filename, ext, method):
        if 'items' in content:
            with open(f"{filepath}/{filename}.{ext}", method) as file:
                for item in content['items']:
                    # Format the string with the search result data
                    result_string = f"Title: {item['title']} - Link: {item['link']} - Snippet: {item['snippet']}\n"
                    # Write the formatted string to the file
                    file.write(result_string)
                    # Write a separator line to the file
                    file.write("-" * 80 + "\n")

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

