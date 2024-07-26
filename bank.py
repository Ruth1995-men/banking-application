# module is the account
from account import Account 
class Bank:
    def __init__(self) :
        self.accounts = {}

    def create_account(self,name,initial_deposit):
        if name not in self.accounts:
            if initial_deposit >= 0:
                self.accounts[name] = Account(name, initial_deposit)
                print("Account created successfully.")
            else:
                print("initial deposit must not be 0")
        else:
            print("Acconut with the name already exist")

    def deposit(self,name,amount):
        if name in self.accounts:
            self.accounts[name].deposit(amount)
            print("Deposit is successful")

    def withdraw(self,name,amount):
        if name in self.accounts:
            if self.accounts[name].withdraw(amount):
                print("withdrawal succesful")
            else:
                print("Account not found")

    def check_balance(self, name):
        if name in self.accounts:
            balance = self. accounts[name].get_balance()
            print(f"Account balance:{balance}")
        else:
            print("Account not found")
            
            




        



