#list is a way to store multiple vlaues in a single array
#lists are mutable, meaning that their elements can be changed,added or removed
for i in [4,5,6]:
    # first assigns i to the first element at 0 index namely 4
    # secondly assigns i to the second element at 1 index namely 5
    # finally assigns i to the third element at 2 index namely 6
    
    print("meaow")
students=["Tabish", "Fahad", "Jibraan"]
for stu in students:
    print(stu)
    #anything iterable can be used here 
    #could have done the same thing using number and list[index] till len(list)
    #using underscore instead of stu will work but its not recommeded
    #underscore is tough for the user to track
