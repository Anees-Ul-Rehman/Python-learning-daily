# ESCAPE SEQUENCE CHARACTERS 
 
# Sequence of characters after backslash "\" → Escape Sequence characters.



 
#  so if we want a new line and we do like that so its incorrect way 
# a="Anees is a good boy 
# but not a bad boy."

# print(a)

# for  new line we use '\n'
a='Anees is a good boy\nnot a bad boy'
print(a) 

# and another Escape seq character is \t this will gave space equal to tab
# i.e
a="Anees is a good boy.\nnot a bad\tboy."
print(a)

# other one Escape seq character is \" it will manuplated as "" in strings 
# i.e
a="Anees is a good boy.\n not a \"bad\" boy." 
print(a)

# if I want to boy with single code like this 'boy' so it will show witout using Escape_set if I use double code in string 
a="Anees is a good boy.\n not a 'bad' boy." 
print(a)

# if I use single code in string so "boy" wil show without using \" 
a='Anees is a good boy.\n not a "bad" boy.'
print(a)

# if we use single code in string and we want boy in singel code for that same \'
a="Anees is a good boy.\n not a \'bad\' boy." 
print(a)

# one other Escape is \\ for use backslash in sentence
a="Anees is a good boy.\n not \\ a 'bad' boy." 
print(a)