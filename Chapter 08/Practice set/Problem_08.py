# Q:8. Write a python function to print multiplication table of a given number.

def table():
    n=int(input("Enter number: "))
    for i in range(1, 11):
        print(f"{i}X{n}={i*n}")

table()



def table1():
    n=int(input("Enter number: "))
    for i in range(1, 11):
        print(f"{n}X{11-i}={(11-i)*n}")

table1()