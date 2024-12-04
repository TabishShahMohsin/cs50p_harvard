# To store more than one field in a file
with open("names.csv") as something:
    #"r" is default
    for line in sorted(something):
        # to sort use sorted() function
        # or use a list and then sort the list
        row=line.rstrip().split(",")
        # or could unpack them using 2 variables intead of tow
        #replace row with name, add
    # Introducing split
    # split() returns a list
        print(f"{row[0]} lives at {row[1]} ")