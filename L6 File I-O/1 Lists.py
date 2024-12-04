#Lists are also temporarily stored in memory
name=[]
for _ in range(3):
    name.append(input("Enter name: "))
    #introducting append()
for _ in sorted(name): 
    #introducting sorted()   
    print(f"hello, {_}")