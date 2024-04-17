import subprocess
from openai import OpenAI
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = OpenAI(
   api_key=os.environ.get("OPENAI_API_KEY"),
 )

# Interpreting Scan Results with ChatGPT
def analyze_scan_results_with_chatgpt(scan_results):
    message = f"Summarize website from content:\n\n{scan_results}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": message},
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    website = "pointlessai.com"
    output_dir = "/"

    # Construct and run the HTTrack command
    subprocess.run(["httrack", f"https://{website}", "-O", output_dir], check=True)

    with open(f'{website}{output_dir}index.html', 'r') as file:
        input_text = file.read()

    description = analyze_scan_results_with_chatgpt(input_text)

    print(description)