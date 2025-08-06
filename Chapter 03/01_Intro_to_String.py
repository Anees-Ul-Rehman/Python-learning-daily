# String is a data type in python. 

# String is a sequence of characters enclosed in quotes. 
# We can primarily write a string in these three ways. 

a='Anees Ul Rehman' # This is single quoted string
b="Anees Ul Rehman" # This is double quoted string
c= '''Anees Ul Rehman''' # This is triple quoted string


# STRING SLICING 

# The index in a sting starts from 0 to (length -1) in Python. In order to slice a string, we use the following syntax: 

# sl[0:3] return         This will return chrachter from 0 to3
# sl [1:3] returns         This will ruturn chracter from 1 to 3

# i.e 

# A string in python can be sliced for getting a part of the strings. 
# strings are immutable
name="Anees Ul Rehman"
nameshort=name[0:9] # Start from index 0 all the way till 3
print(nameshort)
 
 
# positive counting in pyton start from 0,1,2....
letter=name[3]
print(letter)



# len use for count how many  letters or digit or space used in string
nameshort=len(name)
print(nameshort)