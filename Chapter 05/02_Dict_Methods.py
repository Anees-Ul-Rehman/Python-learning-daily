# PROPERTIES OF PYTHON DICTIONARIES 

# 1. It is unordered. 
# 2. It is mutable. 
# 3. It is indexed. 
# 4. Cannot contain duplicate keys. 

# DICTIONARY METHODS 
# Consider the following dictionary. 
d={} # Empty dictionary
print(type(d))

marks={
    "Anees":100,
    "Yasir":90,
    "Nasir":80,
    "Khalil":70,
    "Ikhtiar":60,
    "Abdul Rehman":50,
}

# • marks.items(): Returns a list of (key,value)tuples. 
# • marks.keys(): Returns a list containing dictionary's keys. 
# • marks.update({"friends":}): Updates the dictionary with supplied key-value pairs. 
# • marks.get("Khalil"): Returns the value of the specified keys (and value is returned eg."70" is returned here).
print(marks.items())
print(marks.keys())
print(marks.get("Khalil"))

# In .update If one key is already in Dictionary so that will be update if you write new key in .update so it will be added in dictionary
marks.update({"Anees":99, "Aliza":100})
print(marks.values())
print(marks)

# Difference between print(marks.get("Khalil")) and print(marks["Khalil"])
# Example
print(marks.get("Khalil")) # Output will be 70
print(marks["Khalil"])     # Output same 70
# But when we enter wrong keys values like print(marks.get("Khalil2"))so its output will none and if we do this print(marks["Khalil2"] output will error syntax 
# Example
print(marks.get("Khalil2"))
print(marks["Khalil2"])

