class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdraw(self, amount):
        if((self.balance - amount) >= 0):
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_user_balance(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_user_balance()

savings = BankAccount(.1, 1000)
checking = BankAccount(.05, 5000)

savings.make_deposit(10).make_deposit(20).make_deposit(40).make_withdraw(500).yield_interest().display_user_balance()
checking.make_deposit(40).make_deposit(200).make_withdraw(80).yield_interest().display_user_balance()

BankAccount.print_all_accounts()

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.svings = BankAccount(0.4, 400)
        User.population += 1