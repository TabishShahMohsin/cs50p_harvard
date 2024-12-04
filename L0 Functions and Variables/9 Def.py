#it's handy to declare a piece of code as a function and use it
#it will look neat
def hello(string="Brother"): #to get a default value,if left unentered
    print("Hello,", string)

name=input("Enter your name: ")
hello(name)
hello()

#Problem!!! Must pile up all the functions with their huge definitions at the top