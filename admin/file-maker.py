def process_sentences_from_file(input_file):
    try:
        # Open the input file and read the sentences
        with open(input_file, 'r') as file:
            sentences = file.readlines()

        # Process each sentence
        for sentence in sentences:
            # Remove any trailing whitespace including newline characters
            sentence = sentence.strip()
            # Convert to lowercase
            lower_case_sentence = sentence.lower()
            # Replace spaces with dashes
            dash_sentence = lower_case_sentence.replace(" ", "-")
            # Create a filename for the .py file
            filename = dash_sentence + ".py"
            # Write the modified sentence to a file
            with open(filename, 'w') as file:
                file.write("# " + dash_sentence)

            print(f"File created: {filename}")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Replace 'input.txt' with the path to your text file
process_sentences_from_file('demo-names.txt')
