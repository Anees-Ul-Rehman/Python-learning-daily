# Q:3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

message = input("Enter your commet:")

if (p1 in message or p2 in message or p3 in message or p4 in message):
    print("This comment is a spam")

else:
    print("This comment is not spam")





spam=input("Enter keyword:")

if(spam=="Make a lot of money"):
    print("Spam detectd")

elif(spam=="buy now"):
    print("Spam")

elif(spam=="subscribe this"):
    print("Spam")

elif(spam=="click this"):
    print("spam")

else:
    print("not spam")
