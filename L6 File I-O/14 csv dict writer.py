import csv
name=input("Enter Name: ")
address=input("Enter Address: ")

with open("dictwriter.csv", "a") as something:
    writer=csv.DictWriter(something, fieldnames=["name", "address"])
    writer.writerow({"name": name, "address": address})
    