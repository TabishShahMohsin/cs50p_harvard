#making a boolean function
def main():
    x=int(input("Enter a number: "))
    if is_even(x):
        # This may return True or False 
        # Note: T and F are capital
        print("Even")
    else:
        print("Odd")
        
def is_even(n):
    if n%2==0:
        return True
    # may or maynot write the else return False statement
main()