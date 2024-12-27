#Name Errors
#Eg:
try:
    asdf=int(input("Enter a number: "))
except ValueError:
    print("Must Enter an Integer! ")
print(f"The value entered is {asdf}")


#NameError if cat is entered
#NameError might not come in py-notebook/jupiter if asdf is used in previous codes
#The int operator is signalling ValueError,  and as the assignment never takes place
    #Calling asdf, but the compiler doesn't find it
#To fix it,  while quiting it graciosly we would need Else
