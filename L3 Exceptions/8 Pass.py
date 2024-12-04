# Sometimes you just want to ignore the user's mistake, and prompt him again
def main():
    print("The number that you have entered is:", get_int())
    #Remember No need to give an extra spaces if using comma
def get_int():
    while True:
        try:
            return int(input("Enter a Number: "))
        except ValueError:
            pass # Ignoring the user's mistake
                # But still ensures that the only ignored error is ValueError
main()