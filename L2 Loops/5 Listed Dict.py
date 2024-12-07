#what if we want to save name, address and phone no.
students=[    {"Name": "Noman", "Add": "NT", "Pet": "Cat"},
    {"Name": "Tabish", "Add": "Mohsin Villa", "Pet": "Dino"},
    {"Name": "Jibraan", "Add": "Zakariya Market", "Pet": "Cockroach"},
    {"Name": "Fahad", "Add": "NT", "Pet":None}]
    # rememver the commas that seperate the elements
    # remember how None is written with first letter capital like True & False
    # It represents efficiently, the absence of a value  
for stu in students:
    print(stu["Name"]," from ", stu["Add"], "has the pet: ", stu["Pet"])
# if you see not closing the breacket even after clossing it you must have forgotten a comma