# 6. Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 –80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        
# => F 

l=int(input("Enter student Marks: "))
if(l<=100 and l>90):
    print("Ex")
elif(l<=90 and l>80):
    print("A")
elif(l<=80 and l>70):
    print("B")
elif(l<=70 and l>60):
    print("C")
elif(l<=60 and l>50):
    print("D")
elif(l<50):
    print("Fail")

else:
    print("You are entering invalid marks")



