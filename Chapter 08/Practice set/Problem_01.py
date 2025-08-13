# Q:1. Write a program using functions to find greatest of three numbers.


def greatest_number(n1, n2, n3):
    if(n1>=n2 and n1>=n3):
        return n1
    elif(n2>=n1 and n2>=n3):
        return(n2)
    elif(n3>=n1 and n3>=n2):
        return(n3)

    
n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
n3=int(input("Enter number 3: "))

# greatest_number(n1, n2,n3)
# greatest_number(n1, n2,n3)
print(f"Greatest number entered by you is: {greatest_number(n1, n2, n3)}")
