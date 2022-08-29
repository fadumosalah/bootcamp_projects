from bankaccount import BankAccount

class User(BankAccount):
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.account = BankAccount(interest_rate= 0.02, balance=0)
        #default attribute
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(self.first_name, self.last_name, self.email, self.age, self.is_rewards_member, self.gold_card_points)
        return self
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
    def checkmembership(self):
        if self.is_rewards_member == True:
            print ("User already a member")
            print(f"You have {self.gold_card_points} points")
        else:
            print("You are not a member. Enroll to get 200 points!")
        return self
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        print(f"You have {self.gold_card_points} points left")
        if self.gold_card_points < 40:
            print("You are overspending")
        return self
    def make_deposit(self,amount):
        self.account.deposit(self, amount)
        return self
    def make_withdrawel(self, amount):
        self.account.withdraw(self, amount)
        return self
    def display_use_balance(self):
        self.account.display_account_infor(self)
    
    



fatima = User("Fatima", "Salah", "sala0197@umn.edu", 28)


#nadia = User("Nadia", "Mohamed", "nadia@gmail.com", 29)
#sara = User("Sara", "Jama", "sara@yahoo.com", 30)
#fatima.enroll().display_info()
#sara.enroll().display_info().spend_points(80)
#nadia.spend_points(50).display_info().checkmembership()

