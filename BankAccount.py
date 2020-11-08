from random import randint

class BankAccount:
    """When called this class will instanciate an object of type BankAccount which is going to create an account for the user."""

    # the routing number will be the same for all accounts in the same bank.
    routing_number = 322271627

    def __init__(self, full_name):

        self.full_name = full_name
        self.account_number = generate_account_number()
        self.balance = 0.00

    def deposit(self, amount):
        """When called this method will deposit the amount passed as the parameter and also prints the balance."""
        
        self.balance += amount
        print(f'Amount Deposited: ${self.balance:.2f}')

    def withdraw(self, amount):
        """When called this method will withdraw the amount passed as the parameter and also prints the balance. If there is insufficient founds it will print a notification"""

        if amount > self.balance:
            self.balance -= 10
            print(f'Insufficient founds. It had been charge $10 as a fee for overdraft.')
        else:
            self.balance -= amount
            print(f'Amount Withdrawn: ${amount:.2f}')
    
    def get_balance(self):
        """When called this method will print the account balance and also return it."""

        print(f'Your account balance is {self.balance:.2f}')
        return self.balance

    def add_interest(self):
        """When called this method will calculate the interested for the month of an anual interest rate of 1% and add it to the balance."""

        interest = self.balance * 0.00083
        self.balance += interest

    def print_receipt(self):
        """When called this method prints a receipt with the account name, account nomber, routing number and balance."""

        print(f'{self.full_name}')
        print(f'Account Number: ****{self.account_number[4:]}')
        print(f'Routing Number: {self.routing_number}')
        print(f'Balance: {self.balance}')

def generate_account_number():
    """Helper function that return a eight digit random number which is going to be of type string."""
    account_number = ""
    for _ in range(8):
        account_number += str(randint(0,9))

    return account_number