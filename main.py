
from bank import Bank

def main():
    bank = Bank()
    # this will only execute when the statement is True 
    
    while True:
        print("\nWelcome to  your BankName\n")
        print("1. Create Account")
        print("2. Deposit")
        print("3.Withdraw")
        print("4.Check Balance")
        print("5.Exit")
    

        # we are going to store all these options in a variable called choice
        choice = input("Enter your preferred choice:")
        if choice =="1":
          name = input("Enter your name:")
          initial_deposit = float(input("Enter initial deposit amount:"))
          bank.create_account(name, initial_deposit)
        
        elif choice =="2":
            name = input("Enter your account name:")
            amount = float(input("Enter deposit amount:"))
            bank.deposit(name,amount)
            
        elif choice =="3":
            name = input("Enter your account name:")
            amount = float(input("Enter withdrawal amount:"))
            bank.withdraw(name,amount)

        elif choice =="4":
            name = input("Enter your account name:")
            bank.check_balance(name)

        elif choice =="5":
            print("Thank you for Banking With Us!.")
            break
        else:
            print("Invalid choice entered. Please Try Again")

        
if __name__ == main():
    main()




