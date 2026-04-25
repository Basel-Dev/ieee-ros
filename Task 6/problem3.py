class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into BankAccount")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawn {amount} from BankAccount")

bankAcc = BankAccount()
bankAcc.deposit(500)

print(bankAcc.balance)
