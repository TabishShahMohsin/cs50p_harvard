# Open is used to open a file programmatically
# To read and write on it by code
# Requires file and the way to open it
# Open reuturns a file handler, special value allowing it to be accessed subsequently
name=input("Enter a name: ")
file=open("Open.txt", "w")
# w not only creates the file, but also recreates it
# w will delete the previous contents
# a to append 
file.write(f"{name}\n") # a function that comes with open to write in the file
file.close() # closing the file, effectively saving it