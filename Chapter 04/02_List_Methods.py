# LIST METHODS. 
# Consider the following list: 

l1 = [1,8,7,2,21,15] 
a=l1.sort()        # updates the list to [1,2,7,8,15,21] 
b=l1.reverse()     # updates the list to [15,21,2,7,8,1] 
c=l1.append(8)     # adds 8 at the end of the list  
d=l1.insert(3,8)   # This will add 8 at 3 index 
e=l1.pop(2)        # Will delete element at index 2 and return its value. 
f=l1.remove(21)    # Will remove 21 from the list.  

print(l1)

ie= "Example on .append"
Friends=["apple", "banana", "grapes", "lemon", 123, 34.3]
print(Friends)
Friends.append("Anees UL Rehman")
print(ie)
print(Friends)

ie = "Example on .sort" 
Friends=[1,54,23,34,2,3,4]
Friends.sort()
print(ie)
print("Thsi is .sorted",Friends)

ie= "Example on .reverse"
Friends=Friends
Friends.reverse()
print(ie)
print("This is .reversed",Friends)

ie= "Example on .insert"
Friends=Friends
Friends.insert(3,8888888)
print(ie)
print("This is .inserted",Friends)

ie= "Example on .pop"
Friends=Friends
Friends.pop(5)
print(ie)
print("This is .poped",Friends)

