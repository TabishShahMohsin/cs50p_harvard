def main():
    x=int(input("Enter Base:"))
    y=int(input("Enter Power: "))
    print(raiseto(x, y))
def raiseto( x,  y):
    # use x**y or pow(x,y)
    return x**y #to make a function get something value back to the function.
main()