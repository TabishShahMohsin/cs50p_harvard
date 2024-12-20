# DUNDER METHODS
class Student:
    def __init__(self, Name, House):
        # This is the function that is by default called when we use Student() function
        # Also called as contructor
        # To initialize the contents of a class
        if not Name:
        # more pythonic way than Name==""
           raise ValueError("Missing Name") 
           #Python allows display errors on your own
           # So to use try and error later in the program
        if House not in ["Zakariya", "Nadeem Tareen", "New Sir Syed Nagar"]:
            raise ValueError("Invalid House")
       
       
    # self is a reference to the current instance of the class.
	# It is used to access the attributes (variables) and methods (functions) that belong to that specific object.
        
        # Like we add keys to dictionaries, we are adding variables(instance variables) to objects
        self.name=Name
        self.house=House
        # Capital N and H for marking the difference in their working
        
    
    
    
    
def main():
    student=get_student()
    print(student.name, "is from", student.house)
    
    
def get_student():
    name=input("Name: ")
    house=input("House: ")
    return Student(name, house)
    # Contructor call

if __name__=="__main__":
    main()