#Caller is the function using it
#Calee is the funciton being called
#We can make the caller tell the calee which error to show
    #This allows us to pass the name of the variable
    #Now we can label error codes wrt the parts of the main function
def main():
     x=get_int("Error code x?1234")
     print(f"The value entered is: {x}")
def get_int(something):
    while True:
        try:
            a=int(input("Enter a  number: "))
        except ValueError:
            print(something)
        else:
            return a
main() 