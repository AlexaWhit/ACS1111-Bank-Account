# Need this in order to generate random 8 digit account numbers
from random import randint

#Create function to randomly assign 8 digit account number
def random_account_number(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

#Function to clear terminal for better readability
def clear_terminal():
    print("\033[H\033[J")

# Create BankAccount class:
class BankAccount:
    def __init__(self, full_name, account_number, current_balance):
        self.name = full_name
        self.account_number = account_number
        self.current_balance = current_balance

        #starting_balance = 0
        account_number = random_account_number(8)

    # DEPOSIT METHOD #
    # Adds amount to the balance and prints a message showing the amount deposited and the updated balance
    def deposit(self):
        # STRETCH CHALLENGE - Prompt for amount
        user_input = input(f"Please enter an amount to deposit for {self.name}: $")
        amount = float(user_input)
        if amount > 0:
            self.current_balance = self.current_balance + amount 
            print(f"Amount deposited: ${amount} | New balance: ${self.current_balance} ")
        else:
            print("Please enter a valid monetary amount in $X.XX format.")

    # WITHDRAW METHOD #
    # Subtracts amount from the current balance and prints a message with withdraw amount and updated current balance
    # If withdraw amount is > current balance, message re insufficient funds appears
    def withdraw(self):
        # STRETCH CHALLENGE - Prompt for amount
        user_input = input("Please enter an amount to withdraw: $")
        amount = float(user_input)
        if amount < self.current_balance:
            self.current_balance = self.current_balance - amount 
            print(f"Amount withdrawn: ${amount} | New balance: ${self.current_balance} ")
        elif amount > self.current_balance:
            print("Insufficient funds.")
        else:
            print("Please enter a valid monetary amount in $X.XX format.")

    # GET BALANCE METHOD #
    # Prints user-friendly message with account balance and also returns the current balance of the account
    def get_balance(self):
        print(f"Your current balance is: ${self.current_balance}")
        return self.current_balance

    # ADD INTEREST METHOD #
    # Adds monthly interest to the user's balance. 
    def add_interest(self):
        #Using round function to round to 2 decimal places
        interest = round((self.current_balance * 0.00083), 2)
        self.current_balance = self.current_balance + interest
        print(f"The amount of interest is: ${interest}. New balance is: ${self.current_balance}")

    # PRINT STATEMENT METHOD #
    # Prints a message with account name, account number, and balance
    def print_statement(self):
        print(f"{self.name}\nAccount No.: {self.account_number}\nBalance: ${self.current_balance}")

clear_terminal()

# EXAMPLE 1
alexa_account = BankAccount("Alexa Whitney", random_account_number(8), 0)
BankAccount.deposit(alexa_account)
BankAccount.withdraw(alexa_account)
BankAccount.get_balance(alexa_account)
BankAccount.add_interest(alexa_account)
BankAccount.print_statement(alexa_account)

# EXAMPLE 2
peyton_account = BankAccount("Peyton Manning", random_account_number(8), 500000)
BankAccount.deposit(peyton_account)
BankAccount.withdraw(peyton_account)
BankAccount.get_balance(peyton_account)
BankAccount.add_interest(peyton_account)
BankAccount.print_statement(peyton_account)

# EXAMPLE 3
## FIX CODE TO TAKE IN AMOUNT INSTEAD OF SELF -- MAY NEED TO ASK DANI
mitchell_account = BankAccount("Mitchell Moore", "03141592", 0)
BankAccount.deposit(mitchell_account) # DEPOSIT $400,000
BankAccount.print_statement(mitchell_account)
BankAccount.add_interest(mitchell_account)
BankAccount.print_statement(mitchell_account)
BankAccount.withdraw(mitchell_account) # WITHDRAW $150
BankAccount.print_statement(mitchell_account)


