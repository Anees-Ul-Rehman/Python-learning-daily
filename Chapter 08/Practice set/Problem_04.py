# Q:4. Write a recursive function to calculate the sum of first n natural numbers.



# n=int(input("Enter number: "))
# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1)+n
#     print(sum(n))

# print(sum(n))

n=int(input("Enter number: "))
def sum(n):
    if(n==1):
        return 1
    return(sum(n-1)+n)
print(sum(n))