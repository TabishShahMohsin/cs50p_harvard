class Account:
    # Definting classes like so is better in practice
    # More obvious and readable, easier to dry run
    # Better to acoid collisions 
    def __init__(self):
        self._balance=0
    
    @property
    def balance(self):
        return self._balance
    # Without the setter you will not be able to change it directly within the main program by doing account.balance=100000000000
    
    def deposit(self, n):
        self._balance += n
    
    def withdraw(self, n):
        self._balance -= n

def main():
    account=Account()
    print("Account Balance:", account.balance)
    account.deposit(100)
    account.withdraw(5)
    print("Account Balance:", account.balance)


if __name__=="__main__":
    main()
