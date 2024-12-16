import csv

with open("Writing.csv", "+a") as something:
    write_to=csv.writer(something)
    write_to.writerow([input("Enter Name: "), input("Enter Home: ")])
    
    '''
    
    Very wierd ouput:
Tabish,"New Sir Syed Nagar, Aligarh"
Jibraan,Zakariya
Fahad,Nadeem Tareen

    
    
    
    
    '''