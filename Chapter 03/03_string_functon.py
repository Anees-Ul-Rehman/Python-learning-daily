name= "Anees Ul Rehman Nohrio"
print(name)
print(len(name))
print(name.endswith("rry"))
print(name.startswith("An"))
# print(name.capitalize())
# print(name.startwith()) 

# name.find, this function the occurance that word in the sentence
a=name.find("Ul")
print(a)

# name.replace, This function change the old word to new word
# 1. i.e
replace=name.replace("e","b")
print(replace)

# 2. i.e
replace1=name.replace("U","L")
print(replace1)


n="Anees Ul Rehman is very intelligent student."
replace_n=n.replace("intelligent","weak")
print(replace_n)