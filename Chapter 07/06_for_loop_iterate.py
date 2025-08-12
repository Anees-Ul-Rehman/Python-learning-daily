# for loop with lists 
l=[1, 3, 6, 234, 6, 764]
for i in l:
    print(i)

# for loop wirh tuple
t= {1, 34, 1, 2, 3, 2, 3, 4, 5, 6, 454, 34, 23, 123,}
for i in t:
    print(i)

# for loop with strings
s="Anees Ul Rehman"
print(s, type(s))
for i in s:
    print(i)


# FOR LOOP WITH ELSE 
# An optional else can be used with a for loop if the code is to be  executed when the loops exhausts. 

l=[1,3,4,5,7]
for item in l:
    print(item)
else:
    print("done") # Output: 1 7 8 done
