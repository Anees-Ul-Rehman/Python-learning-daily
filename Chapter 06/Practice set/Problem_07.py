# Q:7. Write a program to find out whether a given post is talking about “Harry” or not.

post=input("Enter the post: ")

if ("Anees Ul Rehman".lower() in post.lower()):
    print("Yes, It's in the post.")

else:
    print("No, It's not in the post. ")

