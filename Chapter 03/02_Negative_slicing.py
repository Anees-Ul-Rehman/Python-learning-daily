# Negative Indices: Negative indices can also be used as shown as positive but it will start from enf of word  above. -1 corresponds to the (length - 1) index, -2 to (length - 2). 


# negative counting start from -1,-2,-3-,4...
name= "Anees Ul Rehman"
letter1=name[-4]
print(letter1)

name= "Anees Ul Rehman"

# i.e 
print(name[0:11])
print(name[-5:])
print(name[10:15])

print(name[:12]) # is same as print(name[0:12])
print(name[0:12]) # is same as print(name[:12])

print(name[1:]) # is same as print(name[1:15])
print(name[1:15]) # is same as print(name[1:]) 


# SLICING WITH SKIP VALUE 

# We can provide a skip value as a part of our slice like this:

word = "amazing" 
a=word[1: 6: 2] # "mzn"  
print(a)

# Other advanced slicing techniques: 
Word = "amazing" 
a=Word  [0:7]  # word [0:7] – 'amazing' 
b=Word  [0:]  # word [0:7] – 'amazing'
print (a,b) 