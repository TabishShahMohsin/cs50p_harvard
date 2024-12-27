# We are going to use tuple packing and unpacking and then use this realizaiton on classes
# To take student details
# This way indirectly uses tuples
    # Immutable data type, values can't be changed
def main():
    # Unpacking
    name, house=get_student()
    print(f"{name} is from {house}")
    
def get_student():
    # Packing
    return input("Enter Name: "), input("Enter House: ")
    # You can return more than one value in python
        # But actually return one single tuple 
    # Similarly, can use dict and lists especially when want to change values
    

if __name__=="__main__":
    main()