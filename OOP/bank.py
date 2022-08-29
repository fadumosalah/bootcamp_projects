class BankAccount:
    all_accounts= []
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print ("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        return self
    def display_account_infor(self):
        print(f"Balance ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.interest_rate)
        return self
    @classmethod
    def display_accounts(cls):
        for all_accounts in cls.all_accounts:
            all_accounts.display_account_infor()

#account_1 = BankAccount(0.6, 2300)
#account_2 = BankAccount(0.4, 1500)

#account_1.deposit(200).deposit(200).deposit(500).withdraw(1000).yield_interest().display_account_infor()
#account_2.deposit(500).deposit(1000).withdraw(200).withdraw(100).withdraw(50).withdraw(40).yield_interest().display_account_infor()

#BankAccount.display_accounts()