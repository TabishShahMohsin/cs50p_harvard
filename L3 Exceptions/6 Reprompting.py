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
        y=int(input("Enter num or  face ValueError, the choice is yours: "))
        #Remember that this block is executed iff the try is sucessful
        break
print(f"The value entered is {x}")