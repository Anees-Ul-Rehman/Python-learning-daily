# Q:4. Write a python program to print the contents of a directory using the os module. Search online for the function which does that.  


import os

# Specify the directory you want to list
directory_path = '/'

# This command will list all files and direction in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)