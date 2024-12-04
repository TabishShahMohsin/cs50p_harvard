#to choose between some lines of codes
#use <,>,==, !=, <=, >= 
#use if, elif, else
x=int(input("What's x? "))
y=int(input("What's y? "))
if x>y:
    # these are boolean expressions
    #indentation is required in python to indentify the block
    #indent is to be executed iff the condition is true
    print(f"{x} is greater than {y}")
elif x<y:
    #This is only checked if the if condition is false
    print(f"{x} is less than {y}")
else:
    #This is to be executed if all the conditions above stand false
    #This does decrease the time and resources for a code to run
    #The decrement in time isn't visible due to how small this program is. 
    print(f"{x} equals {y}")
#we can add more to the condiitons using "or" as or and "and " as and