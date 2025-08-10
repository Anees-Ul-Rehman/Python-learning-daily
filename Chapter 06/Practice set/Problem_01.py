# Q:1 . Write a program to find the greatest of four numbers entered by the user. 


num1=int(input("Enter number 01:"))

num2=int(input("Enter number 02:"))

num3=int(input("Enter number 03:"))

num4=int(input("Enter number 04:"))

if(num1>num2 and num1>num3 and num1>num4):
    print("Greatest number is num1", num1)

elif(num2>num1 and num2>num3 and num2>num4):
    print("Greatest number is num2", num2)

elif(num3>num1 and num3>num2 and num3>num4):
    print("Greatest number is num3", num3)

elif(num4>num1 and num4>num2 and num4>num3):
    print("Greatest number is num4", num4)



    



