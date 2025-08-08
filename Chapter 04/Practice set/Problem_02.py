# Q:2. Write a program to accept marks of 6 students and display them in a sorted manner. 
Students_mark=[]

S1=int(input("Enter Marks S01="))
Students_mark.append(S1)
S2=int(input("Enter Marks S02="))
Students_mark.append(S2)
S3=int(input("Enter Marks S03="))
Students_mark.append(S3)
# S3=int(input("Enter Marks S03="))
# Students_mark.append(S3)
S4=int(input("Enter Marks S04="))
Students_mark.append(S4)
S5=int(input("Enter Marks S05="))
Students_mark.append(S5)
S6=int(input("Enter Marks S06="))
Students_mark.append(S6)

Students_mark.sort()
print(Students_mark)







# marks= [34, 45, 67, 7, 87, 8]
# # print(type(marks))
# marks.sort()
# print(marks)
