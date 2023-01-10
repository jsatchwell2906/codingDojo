# Create a User class with an __init__ method
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}

    def open_new_account(self, int_rate = 0.02, balance = 0, account_name = "checking"):
        new_account = BankAccount(int_rate, balance)
        print("*******************", new_account.balance)
        self.accounts[account_name] = new_account
        return self

# Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def make_deposit(self, amount, account_name = "checking"):
        self.accounts[account_name].deposit(amount)
        return self

# Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

# Add a display_user_balance method to the User class that displays user's account balance
    def display_user_balance(self, account_name):
        print(self.name)
        self.accounts[account_name].display_account_info()
        return self

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.

class BankAccount:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


savings = BankAccount(.05,1000)
checking = BankAccount(.02,5000)

savings.deposit(10).deposit(20).deposit(40).withdraw(600).yeild_interest().display_account_info()
checking.deposit(100).deposit(200).deposit(400).withdraw(60).yeild_interest().display_account_info()

# BankAccount.print_all_accounts()

# user1 = User("Justin", "justin@codingdojo.com")
# user1.make_deposit(100).make_deposit(250).display_user_balance()

# user2 = User("Analisa", "analisa@codingdojo.com")
# user2.make_deposit(1000).display_user_balance().make_withdrawal(450).display_user_balance()

justin = User("Justin Satchwell", "jsatchwell@codingdojo.com")
justin.open_new_account(0.05, 0)
justin.make_deposit(100).display_user_balance("checking")
justin.open_new_account(0, 500, "savings")

analisa = User("Analisa Arnold", "analisa@codingdojo.com")
analisa.open_new_account(0.045, 300, "savings").display_user_balance("savings")
#analisa.transfer_money(analisa, "checking", 100, "checking").make_withdrawal(150)