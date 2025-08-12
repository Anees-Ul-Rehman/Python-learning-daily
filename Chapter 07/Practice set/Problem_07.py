# Q: 7. Write a program to print the following star pattern. 
'''
   for n = 3
    * 
   *** 
  ***** '''
n=int(input("Enter number of line you want: "))
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="")
    print()


n=int(input("Enter Prime number: "))
for i in range(2, n):
    if(n%2)==0:
        print("No, it's not prime number")
        break
else:
    print("Yes, it's prime number")
