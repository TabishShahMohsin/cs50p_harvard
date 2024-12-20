# Functions in a class are called as methods
class Students:
    def __init__(self, Name, House, Branch):
        self.name=Name
        self.house=House
        self.branch=Branch
    def __str__(self):
        return f"{self.name} is from {self.house}"
    
    def emoji(self):
        # Custom methods are methods that will be designed by you
            # A Custum method can be an instance or a class method
        match self.branch:
            # match doesn't work in order version of python
            case "Computer Engineering":
                return "💻"
            case "Electrical":
                return "⚡" 
            case _:
                return "Koi Baat Nhi"
                


def get_student():
    return Students(input("Enter Name: "), input("Enter House: "), input("Enter Branch:"))

def main():
    student=get_student()
    print(f"His branch is : {student.emoji()}")
    
if __name__=="__main__":
    main()
    