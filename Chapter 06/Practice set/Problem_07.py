# Q:7. Write a program to find out whether a given post is talking about “Harry” or not.

post=input("Enter the post: ")

if ("Anees Ul Rehman".lower() in post.lower()):
    print("Yes, It's in the post.")

else:
    print("No, It's not in the post. ")

for _ in range(3):
    print("Hello")

fruits=["apple", "banana", "cherry"]
for p in range(len(fruits)):
    print(p, fruits[p])

numbers=list(range(1, 6))
print(numbers)