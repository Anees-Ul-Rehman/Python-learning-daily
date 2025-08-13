# Q:5. Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3
def star():
    n=int(input("Enter number of lines you want: "))
    for i in range(1, 1+n):
        print("*"*(n-i), end="")
        print()

star()

    


