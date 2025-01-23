# Python figures out the type of the bariable itself unlike c++. java, c, etc.
    # It's dynamicslly typed languge
    # Better for usage but not for bug detection
# Tool to check that the variables are storing the intended variable types

def meow(n: int) -> None:
    # This int is an annotation/hint to the language, that this variable is an integer but not enforced so.
       
    for _ in range(n): print("meow")

def main():
    number : int = input("Enter a number: ")
    meaows : str = meow(number)
    meow(number)

if __name__=="__main__":
    main()

# Use mypy filename.py to check the types of variables
