import os
import shutil
source_file = 'path_to_source_directory/source_file.txt'  # Change this to your source file path
destination_directory = 'path_to_new_subdirectory/new_subdirectory'  # Change this to your destination directory
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)
    print(f"Directory '{destination_directory}' created successfully.")
if os.path.exists(source_file):
    # Define the destination file path
    destination_file = os.path.join(destination_directory, os.path.basename(source_file))
    shutil.copy(source_file, destination_file)
    print(f"File '{source_file}' copied successfully to '{destination_file}'.")
else:
    print(f"Source file '{source_file}' does not exist.")
