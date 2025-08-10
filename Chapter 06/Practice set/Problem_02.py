# Q:2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 


math=int(input("Enter Maths Marks:"))
english=int(input("Enter English Marks:"))
Physics=int(input("Enter Physics Marks:"))


# Check for total percentage

tatal_percentage = (100*(math + english + Physics))/300
if(tatal_percentage>=40 and math>=33 and english>=33 and Physics>=33):
    print("You are passed:",tatal_percentage)

else:
    print("sorry, You failed try again next year:",tatal_percentage)