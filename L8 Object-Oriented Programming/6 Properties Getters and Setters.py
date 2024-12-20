# To Prevent coders form messing up the attributes
# As shown earliesr within coding you could use student.someotherthing="something"
    # This method can be used to bypass every condition related to the variable in __init__
    # To break this bypassing method we need to madate the coder to use to the setter and getter for data entry
# @property is a keyword in python
# decorators are the functions that modify behaviour of other functions

#Both the instance variable and function can't be called with a single name
    # Usually the instance variable is named as _house
        # and the property(fancier attribute) is called house

class Students:
    def __init__(self, Name, House):
        
        # As we are using dot notation here, it will also call the setter
        self.name=Name
        self.house=House
        
        #REMEMBER!!!!!!!!!!: self._house will not call the setter in initialization 
            
        
    def __str__(self):
        return f"{self.name} is from {self.house}"
    
    # Getter
    @property
    def house(self):
        #print("THE PROPERTY PART IS WORKING")
        # Naming the function as same as the property is necessary
        return self._house
    # Can't do self.house otherwise python will misinterpret it as recursion
    
    # Setter
    # The same name gives python the clue that this should have something to do with the property
    # But with 2 arguments
    @house.setter
    def house(self, HOUSE):
        if HOUSE in ["Zakariya", "New Sir Syed Nagar", "Nadeem Tareen"]:
            self._house=HOUSE
        else:
            raise ValueError("HOUSE NOT IN LIST")
        
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, NAME):
        if not NAME:
            raise ValueError("No Name")
        self._name=NAME
        
def get_student():
    return Students(input("Enter name: "), input("Enter House: "))

def main():
    student=get_student()
    # Trying to bypass
    #student._house="Something not in the list"
    # After the creation of setter function, python has enough clues that it would need to use the setter function in order to set an attribute
    
    #IMPORTANT: Still can be bypassed by student._house="something not in the list"
    # It's a coding nome in python if you see a underscore before a variable name, pls don't touch it
    # 2 __ mean really don't touch it 
    
    print(student)
    print(f"student.house: {student.house} student._house: {student._house} ")



if __name__=="__main__":
    main()