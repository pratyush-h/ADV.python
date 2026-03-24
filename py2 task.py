class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Balance:", self.balance)

acc = BankAccount()
acc.deposit(1000)
acc.withdraw(200)
acc.check_balance()