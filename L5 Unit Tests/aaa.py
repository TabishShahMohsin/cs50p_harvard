# Best way to keep testing your code again and again is by writing your own code
def main():
    a=int(input("Enter a Number: "))
    print(square(a))
    
def square(a):
    return a*a
    # can also try replacing a*a to a+a

if __name__ == "__main__":
    main()
    # Note: __name__ doesn't have double quotes surrounding it.