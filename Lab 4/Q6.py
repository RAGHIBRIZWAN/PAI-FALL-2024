class Bank_Account:
    def __init__(self,account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Amount of {amount} is deposited!")
    
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount of {amount} is withdrawl!")
            
    def check_balance(self):
        print(f"{self.customer_name} your current balance is {self.balance}")

acc = Bank_Account(123,1000,'30-June-2005','Raghib')
acc.check_balance()
acc.deposit(500)
acc.check_balance()
acc.withdraw(200)
acc.check_balance()
