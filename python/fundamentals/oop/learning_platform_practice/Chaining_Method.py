
class User:
    def __init__(self,first_name, last_name, age, email):
        self.first_name= first_name
        self.last_name= last_name
        self.age= age
        self.email= email
        self.gold_cardvalue= 0
        self.is_rewards_member= False    
    def display_info(self):
        print(f'{self.first_name}\n{self.last_name}\n{self.age}\n{self.email}\n{self.gold_cardvalue}\n{self.is_rewards_member}')
        return self
    def enroll(self):
        self.is_rewards_member = True
        self.gold_cardvalue = 200
        return self
    def spend_points(self,amount):
        self.gold_cardvalue-=amount
        return self
        
new_user = User("Zacc","Buk",20,"Zacfa@gmail.com")
new_user2 = User("Will","Fa",18,"Willfa@gmail.com")
new_user3 = User("Richardson","Faze",21,"Richardsonfa@gmail.com")

new_user.display_info()
new_user2.enroll().spend_points(50).display_info()
new_user3.enroll().spend_points(80).display_info()