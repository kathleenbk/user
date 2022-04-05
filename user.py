class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
    
    def transfer_money(self, friend, amount):
        self.account_balance -= amount
        friend.account_balance += amount
        print(f"User: {self.name}, Balance: {self.account_balance}")
        print(f"User: {friend.name}, Balance: {friend.account_balance}")

Nick = User("Nick")
Malcolm = User("Malcolm")
Dennis = User("Dennis")

Nick.make_deposit(68000)
Nick.make_deposit(3200)
Nick.make_deposit(4000)
Nick.make_withdrawal(300)
Nick.display_user_balance()

Malcolm.make_deposit(14000)
Malcolm.make_deposit(32000)
Malcolm.make_withdrawal(7300)
Malcolm.make_withdrawal(1000)
Malcolm.display_user_balance()

Dennis.make_deposit(10000)
Dennis.make_withdrawal(500)
Dennis.make_withdrawal(100)
Dennis.display_user_balance()

Nick.transfer_money(Dennis, 10000)
