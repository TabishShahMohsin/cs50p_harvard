class Students:
    def __init__(self, name, house):
        self.name=name
        self.house=house
        print("__init__ was used")
    
    def __str__(self):
        print("__str__ was used")
        return f"{self.name} is from {self.house}"
    
    @classmethod
    # A classmethod doesn't need to create an object first
    # This is imp due to kind of recursion forming here (hen before egg kind of)
        # You should not need to create an object in order to get another object
    def get_student(cls):
        name=input("Enter name: ")
        house=input("Enter house: ")
        print("get_student was used")
        return cls(name, house)
    # You can use Students(...) but it may create prob in future more complicated codes
    
    
def main():
        student=Students.get_student()
        '''
        get_student was used first
        __init__ was used second
        Before printing student
        __str__ was used third
        '''
        print("Before printing student")
        print(student)
        
if __name__=="__main__":
    main()
        