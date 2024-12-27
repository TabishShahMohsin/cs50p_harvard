class Students:
    def __init__(self, Name, House, Branch):
        self.name=Name
        self.house=House
        self.branch=Branch
    def __str__(self):
        # This function will always be called whenever python wants to see your funciton as a string
        # Like in print()
        #  This method is called when you use the str() function or when you print an object. It helps make the object’s string representation more readable and meaningful.
        return f"{self.name} is from {self.house}"
        
    
    
def get_student():
    return Students(input("Enter Name:"), input("Enter House:"), input("Enter Branch: "))

def main():
    student=get_student()
    print(student)
    # if student is printed without ..., then memory address will be printed
                  
                  
                  
if __name__=="__main__":
    main()   