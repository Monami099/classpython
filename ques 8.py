input_file = 'input.txt'  # Replace with your input file path
output_file = 'output.txt'  # Replace with your output file path
words_to_replace = ['a', 'the', 'an']
def remove_words(input_file, output_file, words_to_replace):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()
        for word in words_to_replace:
            content = content.replace(f' {word} ', ' ')  # Replace words with blank space
            content = content.replace(f' {word}.', '.')  # Replace words with blank space when followed by a period
            content = content.replace(f' {word},', ',')  # Replace words with blank space when followed by a comma
            content = content.replace(f' {word}!', '!')  # Replace words with blank space when followed by an exclamation mark
            content = content.replace(f' {word}?', '?')  # Replace words with blank space when followed by a question mark
        with open(output_file, 'w') as outfile:
            outfile.write(content)
        print(f"File processed and saved to '{output_file}'")
    except FileNotFoundError:
        print(f"The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
remove_words(input_file, output_file, words_to_replace)
