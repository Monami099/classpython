source_file = 'source.txt'  # Replace with your source file path
destination_file = 'destination.txt'  # Replace with your destination file path
try:
    with open(source_file, 'r') as src:
        content = src.read()
    content_uppercase = content.upper()
    with open(destination_file, 'w') as dest:
        dest.write(content_uppercase)
    print(f"Contents of '{source_file}' have been copied to '{destination_file}' with uppercase characters.")
except FileNotFoundError:
    print(f"The file '{source_file}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
