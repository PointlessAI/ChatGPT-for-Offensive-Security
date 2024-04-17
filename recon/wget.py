import subprocess
import sys

# Define the website to clone and the destination directory
website_url = "https://pointlessai.com"
destination_dir = "/"

# Construct the Wget command
wget_command = ["wget", 
                "--mirror",  # Mirror the website
                "--convert-links",  # Convert links for offline viewing
                "--adjust-extension",  # Save files with .html extension
                "--page-requisites",  # Get all assets needed for the page
                "--no-parent",  # Do not ascend to the parent directory
                "--directory-prefix=" + destination_dir,  # Set download directory
                website_url]

# Execute the Wget command
try:
    print(f"Cloning {website_url} to {destination_dir}...")
    subprocess.run(wget_command, check=True)
    print("Website successfully cloned for offline testing.")
except subprocess.CalledProcessError as e:
    print("An error occurred while cloning the website.", file=sys.stderr)
