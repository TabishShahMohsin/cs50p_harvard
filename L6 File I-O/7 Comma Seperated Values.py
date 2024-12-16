# To store more than one field in a file
with open("Addresses.csv") as something:
    #"r" is default
    # csv files are very common to seperate data in columns using commas
    for line in sorted(something):
        # to sort use sorted() function
        # or use a list and then sort the list
        # row=line.rstrip().split(",")
            # This will split at every occurance of "," and return a list
        # You can store the sentences in a list and then sort it, but what if you need to mention the name in between thesse sentences
        
        
        name, house=line.rstrip().split(",")
        # This is unpacking
        
        # or could unpack them using 2 variables intead of tow
        #replace row with name, add
    # Introducing split
    # split() returns a list
        print(f"{name} lives at {house} ")