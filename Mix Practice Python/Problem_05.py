
# 'import' used to import any modules here
import os 

# here you can give the path of that files that you want to list by program
directory_path='/'

# here you telling the computer what he list in output
contents=os.listdir(directory_path)

# it will print that files that in folders you gave path
for item in contents:
    print(item)