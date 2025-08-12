# THE BREAK STATEMENT 
# ‘break’ is used to come out of the loop when encountered. It instructs the program to – exit the loop now


for i in range (0,80):   # this will print 0,1,2 and 3
    if i==30:
        break
    print(i)    
    # break 


for i in range(100):
    if(i == 34):
        break # Exit the loop right now 
    print(i)

# THE CONTINUE STATEMENT 
# ‘continue’ is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to “skip this iteration”.
 


for i in range(100):
    if(i == 34):
        continue  # skip the iteration
    print(i)

