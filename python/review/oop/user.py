# Assignment: User
# For this assignment you will create the user class and add a couple methods!

class User:

    def __init__(self, first_name, last_name, email, age):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    # Methods:
    # display_info(self) - Have this method print all 
    # of the users' details on separate lines.

    def display_info(self):
        print("------------------------------------")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        print("------------------------------------")

    def enroll(self): 

        # Add logic in the enroll method to check if 
        # they are a member already, and if they are, 
        # print "User already a member." and return False, otherwise return True.
        if self.is_rewards_member:
            print("User already a member")
            return False

        # Have this method change the user's member 
        # status to True and 
        self.is_rewards_member = True

        # set their gold card points to 200.
        self.gold_card_points = 200




    def spend_points(self, amount):

        # Add logic in the spend points method 
        # to be sure they have enough points to 
        # spend that amount and handle appropriately.
        if self.gold_card_points < amount:
            "Not enough points!"
            return 

        # decrease the user's points by the amount specified.
        self.gold_card_points -= amount



    # Ninja Bonuses:


my_user = User("Justin", "Satchwell", "jsatchwell@codingdojo.com", 32)
my_user.display_info()
my_user.enroll()
my_user.display_info()
my_user.spend_points(300)
my_user.display_info()
