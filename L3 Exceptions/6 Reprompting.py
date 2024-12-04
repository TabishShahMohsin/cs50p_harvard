#It's unfriendly to reject a user, just bcz he gave the wrong input
#It's better to ask him again and again
while True:
    try:
        x=int(input("Enter a Number: "))
        #Could have used break here
        #Having a single statement increases readibility
        #Only need to try to execute one statement for each try
    except ValueError:
        print("MUST ENTER AN INTEGER!!")
    else:
        #Remember that this block is executed iff the try is sucessful
        break
print(f"The value entered is {x}")
'''
You can skip using the else block and instead write all code that follows the try statement directly within the try block itself.
This approach will work functionally, as the try block will handle any exceptions, and anything that comes after will execute only if no exception occurs.
But else improves readibility and avoids accidental exception masking
'''