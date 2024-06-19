# Date: 5th February 2024 Monday
# Start Time : 11 : 13 PM
# End Time : 11 : 38 PM

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def __str__(self):
        return f"Account Holder Name: {self.name}\nBalance: {self.balance}"
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance!!!")
        else:
            self.balance -= amount    

a = BankAccount("Taimur", 1000)
print(a)
a.deposit(200)
print(a)
a.withdraw(700)
print(a)
a.withdraw(1500)
