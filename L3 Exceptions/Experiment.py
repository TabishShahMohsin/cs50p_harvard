try:
    abcdef=int(input("Enter a number: "))
    print(x)
    #This code is tried and the error is checked
except ValueError:
    print("YOU MUST ENTER AN INTEGER!!!")
    #If the error matched, this block is executed
else:
    #If no error is matched than this is executed
    #If an error is matched this portion is skipped
    #Same as writing this blockk with try, but better in practice
    print(f"The value entered is {abcdef}")