# Create BankAccount class:
class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.name = full_name
        self.account_number = account_number
        self.balance = balance

    # Create deposit method
    # Adds amount to the balance and prints a message
    def deposit(amount):
        pass
    # Create withdraw method
    # Subtracts amount to the balance and prints a message
    # Create if statement where else is insufficient funds with message
    def withdraw(amount):
        pass

    # Create get_balance method
    def get_balance(self):
        pass

    # Create add_interest method: Adds interest to the user's balance. 
    def add_interest(self):
        pass
        #interest = (self.balance * 0.00083)

    # Create print_statement method which prints a message with account name, account number, and balance
    def print_statement(self):
        print(f"{self.name}\nAccount No.: {self.account_number}\nBalance: {self.balance}")

alexa_account = BankAccount("Alexa Whitney", "05546992", 0)
BankAccount.print_statement(alexa_account)