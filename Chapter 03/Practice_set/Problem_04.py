# Q: 4. Replace the double space from problem 3 with single spaces. 

a="Anees Ul    Rehman "
b="Aliza   ali "
print(a.replace("a","b").replace("    "," "))
print(b.replace("   "," "))

# if I print the a so it spaces are not change in single space because .replace function not change the original string it make a new string
# Because  strings are immutable
print(a)
