# Simple Bank Software

class BankAccount:
    def __init__(self, name, phone, balance = 0.00):
        self.name = name
        self.phone = phone
        self.balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"Deposited{amount: .2f} to {self.name}'s account.")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from {self.name}'s account.")
        else:
            print('Invalid withdrawal amount or insufficient balance.')

    def get_amount(self):
        return f"{self.name}'s current balance: ${self.balance:.2f}"
    

ram = BankAccount("Ram Thapa", "0451123155")
ram.deposit(5000)
ram.withdraw(2000)
print(ram.get_amount())


# Python Codes
