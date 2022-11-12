class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if((self.balance - amount) >= 0):
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

savings = BankAccount(.1, 1000)
checking = BankAccount(.05, 5000)

savings.deposit(10).deposit(20).deposit(40).withdraw(500).yield_interest().display_account_info()
checking.deposit(40).deposit(200).withdraw(80).yield_interest().display_account_info()

BankAccount.print_all_accounts()