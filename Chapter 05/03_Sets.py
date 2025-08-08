# SETS IN PYTHON. 
# Set is a collection of non-repetitive elements.


# If you are a programming beginner without much knowledge of mathematical operations on sets, you can simply look at sets in python as data types containing unique values. 

# PROPERTIES OF SETS 
# 1. Sets are unordered => Element’s order doesn’t matter 
# 2. Sets are unindexed => Cannot access elements by index 
# 3. There is no way to change items in sets. 
# 4. Sets cannot contain duplicate values. 


s={} # Output 'dic' 
print(type(s))
s= set() # Don't use s={} as it will an empty dictionary
print(type(s)) # Output 'set'

# No Repitation In "SETS"
s= {1,1,1,1,1,2,2,2,3,3,3,3,3,23} # No repitation allowed
print(s) # Output {1, 2, 3, 23}

# sets will not maintain order in output so if you want order you should list there a list method .sort
a= {34,54,56,1,32,2,12,3}
print(a)  # Output inorderd not like {1, 2, 3, 12, 32, 34, 54, 56}
# if you want to order maintain you use sorted like following
print("Original set:",(a))
print("Sorted set",sorted(a)) # But when you print type so type will be list look at following example
result=sorted(a)
print(result, type(result)) # output 'list'



