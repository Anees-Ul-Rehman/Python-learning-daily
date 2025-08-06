import os

# Specify the directory you want to list
directory_path = '/'

# This command will list all files and direction in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)