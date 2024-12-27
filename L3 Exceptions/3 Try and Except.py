try:
    #in best practice: you should only use a single line of code in try
    # If an exception occurs within a try block, nothing after the exception will get executed.
    # otherwise try will try the whole of the block
    # What to do to write a single line,  will be shown in NameError and Else
    print("Line 6")
    x=int(input("Enter a number: "))
    print(f"The value entered is {x}")
except ValueError:
    print("Must Enter an Integer! ")
    # except (ValueError, ZeroDivisionError): can be used to catch multiple errors in the same block