# In while loops, the condition is checked first. If it evaluates to true, the body of the loop is executed otherwise not!
 
# If the loop is entered, the process of [condition check & execution] is continued until the condition becomes False.

# Quick Quiz: Write a program to print 1 to 50 using a while loop. 

i=1
while(i<51):
    print(i)
    i +=1
else:
    print("done")
# Note:  If the condition never become false, the loop keeps getting executed.


i = 1

while(i<10):
    print(i)
    i +=1
else:
    print('done')


''' 
Output 
1
2
3
4
5
6
7
8
9'''

print("Then exit from control loop")


i = 0 
while (i< 5):
    print("Harry")  # print "Harry" – 5 times! 
     
    i = i + 1 
else:
    print("done")  # This is printed when the loop exhausts! 
 
# i="condition"
# while (i):
    # print(i)  # The block keeps executing until the condition is true Body of the loop




    