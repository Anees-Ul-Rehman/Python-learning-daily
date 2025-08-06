# Q:5. Label the program written in problem 4 with comments.  

# This is os module this is include with pythin system you will don't download using pip
import os

# Specify directory that you will select  then all files will show
directory_path = '/' 

# select the same directory path
contents = os.listdir(directory_path)

# this will show the all files and filder from that path 
for item in contents:
  print(item)