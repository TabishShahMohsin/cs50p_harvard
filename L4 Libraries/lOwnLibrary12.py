# Instead of writing your code again and again
# Can save your own lib locally and use it instead
# Or can bundle it and upload it to pypi
def main():
    hello("World")
    goodbye("World")
# this main function is not necessary but used to check the functions when needed
def hello(name):
    print(f"Hello, {name}")
def goodbye(name):
    print(f"Good Bye, {name}")
if __name__=="__main__":
    
    # To prevent the main function to be called everytime this file is called
    # Now main only gets executed if this program by its own is executed
    main()
    