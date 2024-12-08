# Best way to keep testing your code again and again is by writing your own code
# Great for testing corner cases again and again

def main():
    a=int(input("Enter a Number: "))
    print(square(a))
    
def square(a):
    return a*a
    # can also try replacing a*a to a+a
    
def square_(a):
    return a+a

if __name__ == "__main__":
    main()
    # Note: __name__ doesn't have double quotes surrounding it.