# OPERATIONS ON SETS 
# Consider the following set: 

s = {1,8,2,3}

# • len(s): Returns 4, the length of the set  
# • s.remove(8): Updates the set s and removes 8 from s. 
# • s.pop(): Removes an random element from the set and return the element removed.
# • s.clear():empties the set s. 
# • s.union({8,11}): Returns a new set with all items from both sets. {1,8,2,3,11}. 
# • s.intersection({8,11}): Return a set which contains only item in both sets  {8}. 

# Example on s.add()
s={3, 4, 5,"Anees"}     # no repetition allowed!       
s.add(1) 
s.add(2)           
print(s, type(s))   # or set ={1,2}  

# Example on .len(s)
s = {1,8,2,3}
print(len(s), type(s)) # Output length:4, class:set

# Example on s.remove(8)
s={1,8,2,3}
s.remove(8)
print(s, type(s))   # Output {1, 2, 3, }

# Example on s.pop()
s={1,8, 5, 4, 2,3} # pop will remove randomly atom, which is not good. so don't use to much if you need so use it so.
s.pop()
print(s, type(s))

# Example on s.clear()
s={1,8,2,3}
s.clear()         
print(s,type(s))

print()

# set Union and Intersection are explained in 05_Set_union_Intersection.py



