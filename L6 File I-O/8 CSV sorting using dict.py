students=[]
with open("Addresses.csv") as something:


    for a in something:
        name, add=a.rstrip().split(",")
        student={"name":name, "address":add}
        students.append(student)
    
for i in students:
    print(f"{i['name']} is from {i['address']}")