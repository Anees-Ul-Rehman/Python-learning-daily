# Task 4:
# Ek list banao: fruits = ["apple", "banana", "cherry"]
# Isme "mango" add karo aur "banana" remove karo.
# Ek tuple banao jisme 3 cities ka naam ho.
# Tuple me element change karne ki koshish karo aur dekho kya hota hai.

fruits=["apple", "banana", "cherry"]
print(fruits)

# Add mango
fruits.append("mango")
print(fruits)             # ['apple', 'banana', 'cherry', 'mango']

# remove banana
fruits.remove("banana")
print(fruits, type(fruits))           # ['apple', 'cherry', 'mango']


# Tuple
cities=("karachi","lahore","islamabad")
print(cities,type(cities))

# Try changing tuple element
# cities[0]="quetta" # TypeError: 'tuple' object does not support item assignment

 
# set
s={2,3,3,4}
print(type(s))

# Empty sete
s=set()
print(type(s))

s=31
b=str(s)
print(type(b))
