# Need this in order to generate random 8 digit account numbers
from random import randint

# Create BankAccount class:
class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.name = full_name
        self.account_number = account_number
        self.balance = balance

        balance = 0
        account_number = randint(8)

    # Create deposit method
    # Adds amount to the balance and prints a message
    def deposit(amount):
        amount = input("Please enter an amount to deposit: $")
        deposit = (f" {amount} + {BankAccount.self.balance}")
        print(f"Amount deposited: {amount} new balance: {deposit} ")

    # Create withdraw method
    # Subtracts amount to the balance and prints a message
    # Create if statement where else is insufficient funds with message
    def withdraw(amount):
        amount = input("Please enter an amount to withdraw: $")
        withdraw = (f"{BankAccount.self.balance} - {amount}")
        print(f"Amount deposited: {amount} new balance: {withdraw} ")

    # Create get_balance method
    def get_balance(self):
        print(f"Your current balance is: {self.balance}")
        return BankAccount.self.balance

    # Create add_interest method: Adds interest to the user's balance. 
    def add_interest(self):
        interest = (self.balance * 0.00083)
        print(f"The amount of interest is: ${interest}.")

    # Create print_statement method which prints a message with account name, account number, and balance
    def print_statement(self):
        print(f"{self.name}\nAccount No.: {self.account_number}\nBalance: {self.balance}")

alexa_account = BankAccount("Alexa Whitney", "05546992", 0)
BankAccount.print_statement(alexa_account)