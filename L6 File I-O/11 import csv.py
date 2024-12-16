# now if we use comma in csv files
    # would need to write multiple lines of code to now use this comma
        # use this comma to split iff it is not between quotes
    # would need to find roots and use them again and again to solve basic issued that everyone may face
    # Dealing with corner cases using conditions again and again 
    # what if such functions are already formed in csv lib
students=[]
import csv
with open("Problem.csv", "r") as problem:
    something=csv.reader(problem)
    
    for row in something:
        try:
            name, add=row
        #unpacking in the for loop syntax
            students.append({"name": name, "add": add})
        except ValueError:
            print(f"Problem Unsolved in {row}")
    # Just firgured out that even a space ruins csv files
        #Tabish,"New Sir Syed Nagar, Aligarh" works
        #Tabish, "New Sir Syed Nagar, Aligarh" doesn't work
for i in sorted(students, key=lambda some_other:some_other["name"]):
    print(f"{i['name']} is from {i['add']} ")
        
