# Task 5:
# Ek dictionary banao: student = {"name": "Ali", "age": 20, "marks": 85}
# Age ko update karo aur ek new key "grade" add karo.
# Ek set banao jisme duplicate numbers ho aur dekhna output me duplicates remove ho rahe hain ya nahi.
# Do sets ka union aur intersection print karo.

student={
    "name":"ali",
    "age":20,
     "marks":85,
}

student.update({"age":34, "grade":"A"})
print(student)  #  Output: {'name': 'ali', 'age': 34, 'marks': 85, 'grade': 'A'}

s={1,3,4,1,3,4,5,6,7,6,8,9,8}
print(s)    #  Output: {1, 3, 4, 5, 6, 7, 8, 9}


s1={1, 1, 3, 3, 4, 4, 5, 5, 6, 7, 6, 8, 9, 65, 8}
s2={3,2,4,1,5,6,7,56}
print(s1.union(s2)) # Output: {65, 1, 3, 4, 5, 6, 7, 8, 9, 2, 56}

print(s1.intersection(s2)) # Output: {1, 3, 4, 5, 6, 7}














