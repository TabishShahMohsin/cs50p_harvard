class Students:
    def __init__(self, name, house):
        self.name=name
        self.house=house
    
    def __str__(self):
        return f"{self.name} is from {self.house}"
    
    @classmethod
    # A classmethod doesn't need to create an object first
    # This is imp due to kind of recursion forming here
        # You should not need to create an object in order to get another object
    def get_student(cls):
        name=input("Enter name: ")
        house=input("Enter house: ")
        return cls(name, house)
    # You can use Students(...) but it may create prob in future more complicated codes
    
    
def main():
        student=Students.get_student()
        print(student)
        
if __name__=="__main__":
    main()
        