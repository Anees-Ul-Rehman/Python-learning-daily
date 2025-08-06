# TYPE() FUNCTION AND TYPECASTING.  

# type() function is used to find the data type of a given variable in python. 


# Integers Classes
a=31
t=type(a)
print(type(a),(t))
print(t)

# Floating Point Number Classes
a=31.5
t=type(a) 
print(type(a),(t))
print(t)

# Strings Classes
# If any words, digits, and symbol will come in doubole quote so it becomes String
a="Anees Ul Rehman"
b="3434"
t=type(a) 
print(type(a),t)
print(type(b))

# it's possible to change the strings number into floating or integers
# there are some examples

# Example 1 string to float 
a="32.4"
b=float(a) # b = a but the type should be float
t=type(a)  
print(type(a),t,)
print(type(b))

# Example 2 Float to string 
a=32.3
b=str(a) # b=a but the type should be string
t=type(a) 
print(type(a),t)
print(type(b))

# Example 3 integer to String
a=54
b=str(a)

print(type(a))
print(type(b))


# Example 4 String to integer 
# if you want to convert string to int so it will not convert string alphabetic to int it will work on string numeric to int
a="434"
b=int(a)
print(type(a))
print(type(b))

# Example 5 int to float
a=87
b=float(a)

print(type(b))