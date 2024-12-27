#As we use else when nothing is relevant

'''
The use of the else clause is better than adding additional code to the try clause
because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the try ... except statement.
'''
try:
    x=int(input("Enter a number, if wrong then no ValueError: "))
    #This code is tried and the error is checked
except ValueError:
    print("YOU MUST ENTER AN INTEGER!!!")
    #If the error matched, this block is executed
else:
    y=int(input('Enter a num, if wrong then ValueError will be shown: '))
    #If no error is matched, then this is executed
    #If an error is matched this portion is skipped
    print(f"The value entered is {x} then {y}")