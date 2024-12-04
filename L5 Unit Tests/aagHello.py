def main():
    name=input("Enter Name: ")
    print(hello(name))
    
def hello(to="World"):
    # to is the argument and world is the default value
    return f"Hello, {to}"
    # using fstring or format-string
    # as print will lead to a side effect(some visual artifact)
    # hence its better to not include print in a funciton to test
    # as more and more complex of a funciton is more tough it is to unit test   
    
if __name__=="__main__":
    main()