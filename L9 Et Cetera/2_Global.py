# If we put something outside every function like in c, we can make it global
# But in python we can use the global keyword to make variables inside the variables as global

balance=0

def main():
    print("Balance:", balance)
    # Can see global variables
    try:
        deposit(100)
        withdraw(5)
    except UnboundLocalError:
         print("UnboundLocalError for changing a global variable without global keyword ")
    deposit2(100)
    withdraw2(5)
    print("Balance:", balance)

def withdraw(n):
    balance-=n
    print("Using withdraw without global")

def deposit(n):
    balance+=n
    print("Using deposit without global")

def withdraw2(n):
    global balance
    balance -=n
    print("Using withdraw with global")

def deposit2(n):
    global balance
    balance += n
    print("Using deposit with global")

# Can read a global variable but can't edit it


if __name__=="__main__":
    main()
