#Name Errors
#Eg:
try:
    asdf=int(input("Enter a number: "))
except ValueError:
    print("Must Enter an Integer! ")
print(f"The value entered is {asdf}")
#NameError if cat is entered
#NameError might not come in py-notebook/jupiter if asdf is used in previous codes
#The int operator is signalling an error and hence the assignment never takes place
#Calling something with a name, but the compiler does'nt found it
#To fix it, quiting it graciosly we need Else