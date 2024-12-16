l=[]
with open("Addresses.csv", "r") as something:

    for a in something:
        name, add=a.rstrip().split(",")
        l.append({"name":name, "address":add})
        
        
for i in sorted(l, key=lambda some_other_thing: some_other_thing["name"]):
    # Here some_other_thing is a name given to each i and then i can be used as a simple dictionary to return a value on which sortting is to be done
    print(i)