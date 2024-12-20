# Wouldn't it be great if python developers would have created a student data type
    # But they have allowed use to create such a thing
    # A kind of blueprint of objects
    # https://docs.python.org/3/tutorial/classes.html
    
class Student:
    # By convention we use capital S
    # can even use this code with just writing ...
    ...


def main():
    student=get_student()
    print(f"{student.name} is from {student.house}")
    
    
def get_student():
    student=Student()
    # Creating an object or instance
    
    
    student.name=input("Enter name: ")
    student.house=input("Enter House: ")
    # Creating attributes and instances veriables
    # Name and house are attributes while the variable student.name is an instance variable

    
    return student

if __name__=="__main__":
    main()