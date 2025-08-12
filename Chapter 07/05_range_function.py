# RANGE FUNCTION IN PYTHON 

# The range() function in python is used to generate a sequence of number. We can also specify the start, stop and step-size as follows: 

# range(start, stop, step_size) 
# step_size is usually not used with range()

# This will print from 0 to 6 it doesn't print 7
for i in range(0, 7): # range(7) can also be used. 
    print(i) # prints 0 to 6
else:
    print("done")


# But if we want numbers from 1 to 50 but not in sequence in step like 1, 4, 7, 10 and so on until stop number


# in below command 1 start point 50 is stop point and 3 steps_size
for i in range(1, 50, 3):
    print(i)
else:
    print('done')


