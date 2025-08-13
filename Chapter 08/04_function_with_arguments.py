# FUNCTIONS WITH ARGUMENTS 
# A function can accept some value it can work with. We can put these values in the parentheses. 

# A function can also return value as shown below: 

# argument function 
def greet1(name, thanks):
    print("Good day, "+name)
    print(thanks)

greet1("Anees Ul Rehman",  "Thank you")
greet1(" Yasir ", "Thank you")
greet1("Nasir",  "Thanks")

# Default argument
# DEFAULT PARAMETER VALUE 
# We can have a value as default as default argument in a function. 
# If we specify name = “stranger” in the line containing def, this value is used when no 
# argument is passed. 
# Example: 
def greet2(name, ending="Thank you"):
    gd=(f"Good day, {name} {ending}")

    print(gd)

greet2("Anees Ul Rehman","Thanks")
greet2("Yasir")
greet2("Nasir")

# return function 
def greet3(name, ending):
    gd="Good day "+ name + ending
    print(gd)
    return gd

a=greet3("Anees Ul Rehman", " Thank you")
print(a)
# print(type(a))

# b=("aneees",)
# print(type(b))
 


























