def main():
    print("The number that you have entered is:", get_int())
    #Remember No need to give an extra spaces if using comma
def get_int():
    while True:
        try:
            return int(input("Enter a Number: "))
        except ValueError:
            print("MUST ENTER AN INTEGER!!")
main()