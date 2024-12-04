def main():
    name=input("Enter your name: ")
    hello(name)
    hello()




def hello(string="Brother"): #to get a default value,if left unentered
    print("Hello,", string)


main()
#Problem fixed!!! But now must also take care of the limited scope of the main funciton.