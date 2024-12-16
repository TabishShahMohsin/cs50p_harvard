with open("With.txt", "r") as something:
    #Stores all lines as list
#  (More pythonic way):
    for a in something:
        print(a, end="")
    #Or use this: 
    something.seek(0)
    # Puts the cursor to the very beginning
    
    
    
    # The second approach is bad as it first reads every line then itterates over them
    lines=something.readlines()
for line in lines:
    print(f"{line}", end="")
    # it also stores the newline char at the end to each line
    