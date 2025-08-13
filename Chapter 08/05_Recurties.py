# RECURSION 
# Recursion is a function which calls itself. 
# It is used to directly use a mathematical formula as function.  
# Example: 

'''
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1


factorail(n) = n*factorial(n-1)
'''

def fact(n):
    if(n==0 or n==1):
        return 1
    return n* fact(n-1)


n=int(input("Enter number: "))
print(f"factorail of {n} is {fact(n)}")
