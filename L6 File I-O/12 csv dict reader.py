
import csv
# Using dictreader for column names in the first row
with open("Problem.csv", "r") as something:
    hand=csv.DictReader(something)
    
    print(hand)
    for i in hand:
        print(f"{i['name']} is from {i['address']}")
        # as this code accesses the columns with their names not positions
            # this code will work even if someone shifts columns here and there 