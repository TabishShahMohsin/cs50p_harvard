#just like switch
#compacting if-else statements
name=input("What's your name? ")
#though we can use match to do much more powerful work, here use it limitedly
match name:
    case "Fahad"|"Danish"|"Noman":
        print("NT")
    case "Jibraan":
        print("Zakariya Market")
    case "Tabish":
        print("Mohsin Villa")
    case _:
        print("Who?")