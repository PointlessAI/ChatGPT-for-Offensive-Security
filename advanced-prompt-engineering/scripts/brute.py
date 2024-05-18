import io
import sys

# Define your Python code
script = """
def say_hello():
    print("Hello, world!")
say_hello()
"""

# Create a StringIO object to capture the output
output = io.StringIO()

# Save the current stdout (standard output)
current_stdout = sys.stdout

# Redirect standard output to the StringIO object
sys.stdout = output

# Execute the script
exec(script)

# Restore the original stdout
sys.stdout = current_stdout

# Get the content of output
captured_output = output.getvalue()

# Close the StringIO object
output.close()

print("Captured Output:")
print(captured_output)
