import subprocess
import sys

def run_script(script_name):
    try:
        subprocess.run(['python', script_name])
    except subprocess.CalledProcessError as e:
        print(f"Error in {script_name}: {e}\n{e.stderr}")
        sys.exit(0)
def main():
    scripts = ['strategy.py', 'company_profile.py', 'simulation.py', 'conversations.py', 'landing_page.py']
    for script in scripts:
        run_script(script)

if __name__ == "__main__":
    main()