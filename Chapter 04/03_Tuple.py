# TUPLES IN PYTHON 
# A tuple is an immutable data type in python. 

a = () # empty tuple 
a = (1,) # tuple with only one element needs a comma
a= (1,7,2) # tuple with more than one element
print(type(a))


# TUPLE METHODS 
# Consider the following tuple. 
#  a.count (7): a count (3) will return number of times 7 occurs in a. 
#  a.index (7) will return the index of first occurrence of 7 in a.
a = (1, 1, 7, 7, 7, 2) 
print(a.count(7))
print(a)
print(a.index(7))
print(len(a))

# tuples are always with comma 
a=1,2,3,4,5,6,7,8,9
print(type(a))

# integers are without comma 
a= 1233456789
print(type(a))