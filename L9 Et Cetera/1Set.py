# A collection of objects without the duplicates
students = [
{"name": "Tabish", "house": "New Sir Syed Nagar"},
{"name": "Fahad", "house": "Nadeem Tareen"},
{"name": "Noman", "house": "Nadeem Tareen"},
{"name": "Jibraan", "house": "Near Zakariya Market"},
{"name": "Talha", "house": "New Sir Syed Nagar"},
]

house_list=[]
house_set=set()
# Can check using in or not in in conditionals while dealing with sets
# Can't use {} for initializing empty sets
    # Considers it as a dictionary

for i in students:
    house_list.append(i["house"])
    house_set.add(i["house"])

print("list:", house_list,"\nset:",house_set)
