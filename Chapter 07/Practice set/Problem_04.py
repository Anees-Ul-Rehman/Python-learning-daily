# Q:4. Write a program to find whether a given number is prime or not. 

n = int(input("Enter number: "))

for i in range(2, n):
    if(n%2)==0:
        print("It's not Prime number")
        break
else:
    print("It's Prime number")















# # Odd or Even
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# # Prime check
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not Prime")





