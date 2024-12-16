addresses=[]
with open("Addresses.csv", "r") as something:
    for a in something:
        name, address=a.rstrip().split(",")
        student={"name":name, "address":address}
        addresses.append(student)
def get_name(d):
    # To see what and when d is called, using print.
    print(d)
    return d["name"]
for i in sorted(addresses, key=get_name, reverse=True):
    # Python allows you to pass functions as arguments in other functions
    # The sorted function calls get_name function and enters every i
    # Then sorts it on the basis of return value of get_name function
    # Can use key=len with a list of string elements
        # To sort on the basis of length of strings
    # Using a function one time and giving it a name can be avoided using lambda function
    
    print(f"{i['name']} is from {i['address']}") 


    