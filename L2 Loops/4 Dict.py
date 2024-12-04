#dict stands for dictionaries
#set of key, value pairs
#sort of a 2-d list
#students={"Fahad": "NT", "Noman":"NT", "Tabish":"Mohsin Villa", "Jibraan": "Zakariya Market"}
students={"Fahad": "NT", # can add extra enters in order to beautify it
          "Noman":"NT",
          "Tabish":"Mohsin Villa",
          "Jibraan": "Zakariya Market"}
#dictionaries does not uses numbers as index
#but dictionaries require key to point to the value
print(students["Tabish"])
for stu in students:
    #by defualt it iterates through the keys
    print(stu, students[stu], sep=" from ")

