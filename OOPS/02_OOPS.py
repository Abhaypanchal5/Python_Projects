class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.bal = balance

    def deposit(self, amount):
        self.bal += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.bal:
            print(f"WARNING: Insufficient balance. Transaction of ₹{amount} cancelled.")
            return
        self.bal -= amount
        print(f"₹{amount} withdrawn successfully.")

    def display(self):
        print(f"Owner   : {self.name}")
        print(f"Balance : ₹{self.bal}")


owner1 = BankAccount('Abhay', 60000)
owner1.deposit(10000)
owner1.withdraw(80000)   # should trigger warning
owner1.display()

owner2 = BankAccount('Yash')   # default balance = 0
owner2.deposit(50000)
owner2.withdraw(20000)
owner2.display()