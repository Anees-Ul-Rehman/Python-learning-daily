# Q:6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. 

# I tried but not as harry bhai 😂
dic={}
name=input("Enter friend name:")
lang=input("Enter friend lang:")
dic.update({name:lang})

name=input("Enter friend name:")
lang=input("Enter friend lang:")
dic.update({name:lang})

name=input("Enter friend name:")
lang=input("Enter friend lang:")
dic.update({name:lang})

name=input("Enter friend name:")
lang=input("Enter friend lang:")
dic.update({name:lang})

print(dic)

friends={
    "Ali":input("Facourite Lang:",),
    "Mahmood":input("Facourite lang:",),
    "Anees":input("Facourite lang:",),
    "Bharat":input("Facourite lang:",),
    "Bharat":input("Facourite lang:",),
} 

print(friends.values())
print(friends.keys())
print(friends.items())
# friends.update({"Bharat":sindhi,})
print(friends.get("Bharat"))
