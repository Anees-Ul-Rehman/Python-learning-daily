# Q: 6. Write a python function which converts inches to cms.

def cms():
    n=int(input("Enter inches you want in cms:"))
    for i in range(1, n+1):
        print(n*2.54)
        break

cms()