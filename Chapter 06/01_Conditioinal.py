# CHAPTER 6 – CONDITIONAL EXPRESSION

# Sometimes we want to play PUBG on our phone if the day is Sunday. 

# Sometimes we order Ice Cream online if the day is sunny.
#  
# Sometimes we go hiking if our parents allow.
# All these are decisions which depend on a condition being met. 

# In python programming too, we must be able to execute instructions on a condition(s) being met. 

# This is what conditionals are for! 


# IF ELSE AND ELIF IN PYTHON 
# If else and elif statements are a multiway decision taken by our program due to certain conditions in our code.

a=input("Enter you name:")

# If statement no1
if(a=="Anees Ul Rehman"):
    print("Your Name")

elif(a=="Yasir Ul Rehman"):
    print("Your Brother name")

elif(a=="Nasir Ul Rehaman"):
    print("Your 2nd Brother")

elif(a=="Khalil Ul Rehman"):
    print("Your Younger Brother")

elif(a=="Aliza"):
    print("Your Sister name")

else:
    print("other")

# End of If statement no 1



a=int(input("Enter your age:"))

# If statement no 02
if(a%2==0):
    print("Even number")
# End of If statement no 02


# If statement no 03
if(a%2==1):
    print("Odd number")
# End of If statement no 03


# If statement no 04
if(a>=18):
    print("you are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entring an invalid negative age")

elif(a==0):
    print("You are entering 0 which is not a valid age")

else:
    print("You are below the age of consent")

# End of If statement no 04


print("End of program")


a=int(input("Enter your age:"))

# If statement no 05
if(a>=18):
    print("Yes")

elif(a<0):
    print("You enterd negative number which is not valid age")

elif(a==0):
    print("you are entering 0 which is not valid age")

else:
    print("No")

# End of If statement no 05