# Q: 2. Write a python program using function to convert Celsius to Fahrenheit.

def temperature(f):
    c=5*(f-32)/9
    return c

f=int(input("Enter temperature: "))
c=temperature(f)
print(f"{temperature(f)}Degree C")
print(f"{round(c, 2)} Degree C")  
