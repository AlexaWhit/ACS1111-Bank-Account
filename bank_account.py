# Need this in order to generate random 8 digit account numbers
from random import randint

#Create function to randomly assign 8 digit account number
def random_account_number(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

# Create BankAccount class:
class BankAccount:
    def __init__(self, full_name, account_number, current_balance):
        self.name = full_name
        self.account_number = account_number
        self.current_balance = current_balance

        #starting_balance = 0
        account_number = print(random_account_number(8))

    # DEPOSIT METHOD #
    # Adds amount to the balance and prints a message showing the amount deposited and the updated balance
    def deposit(self):
        user_input = input("Please enter an amount to deposit: $")
        amount = float(user_input)
        if amount > 0:
            self.current_balance = self.current_balance + amount 
            print(f"Amount deposited: ${amount} new balance: ${self.current_balance} ")
        else:
            print("Please enter a valid monetary amount in $X.XX format.")

    # WITHDRAW METHOD #
    # Subtracts amount from the current balance and prints a message with withdraw amount and updated current balance
    # If withdraw amount is > current balance, message re insufficient funds appears
    def withdraw(self):
        user_input = input("Please enter an amount to withdraw: $")
        amount = float(user_input)
        if amount < self.current_balance:
            self.current_balance = self.current_balance - amount 
            print(f"Amount withdrawn: ${amount} new balance: ${self.current_balance} ")
        elif amount > self.current_balance:
            print("Insufficient funds.")
        else:
            print("Please enter a valid monetary amount in $X.XX format.")

    # GET BALANCE METHOD #
    # Prints user-friendly message with account balance and also returns the current balance of the account
    def get_balance(self):
        print(f"Your current balance is: ${self.current_balance}")
        return self.current_balance

    # Create add_interest method: Adds interest to the user's balance. 
    def add_interest(self):
        interest = (self.current_balance * 0.00083)
        print(f"The amount of interest is: ${interest}.")

    # Create print_statement method which prints a message with account name, account number, and balance
    def print_statement(self):
        print(f"{self.name}\nAccount No.: {self.account_number}\nBalance: {self.balance}")

alexa_account = BankAccount("Alexa Whitney", "05546992", 0)
BankAccount.deposit(alexa_account)
BankAccount.withdraw(alexa_account)
BankAccount.get_balance(alexa_account)
#BankAccount.add_interest(alexa_account)
#BankAccount.print_statement(alexa_account)