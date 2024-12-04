#insisting user and printing meaow
#user must give a positive vlaue
while True:
    n=int(input("Enter the No. of Meaows: "))
    if n>0:
        break
    #if used in a function, could have used return n instead of break to break out of the function itself
    #breaking out of the nearest while loop
print("MEAOW\n"*n, end="")