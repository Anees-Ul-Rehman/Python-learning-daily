# Ek integer, ek float, ek string, aur ek boolean variable banao.type() se inka type check karo.

a=123
b=45.4
c="Anees"
d=4>5
print(d, type(d))  # Output: False <class'bool'>
print(type(a), type(b), type(c))  # Output: <class 'int'> <class 'float'> <class 'str'>

a=567
b=str(a)
print(b, type(b)) # Output: 567 <class 'str'>