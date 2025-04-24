file1 = 'file1.txt'  # Replace with the path of the first source file
file2 = 'file2.txt'  # Replace with the path of the second source file
output_file = 'merged_file.txt'  # Replace with the path for the merged output file
try:
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        # Read lines from both files
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        i, j = 0, 0
        while i < len(lines1) and j < len(lines2):
            # Write alternate lines from both files to the output file
            out.write(lines1[i].strip() + '\n')  # Write line from file1
            out.write(lines2[j].strip() + '\n')  # Write line from file2
            i += 1
            j += 1
        while i < len(lines1):
            out.write(lines1[i].strip() + '\n')
            i += 1
        while j < len(lines2):
            out.write(lines2[j].strip() + '\n')
            j += 1
    print(f"Files have been successfully merged into '{output_file}'.")
except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
