from random import randint

def generate_account_number():
    """Helper function that return a eight digit random number which is going to be of type string."""
    account_number = ""
    for _ in range(8):
        account_number += str(randint(0,9))

    return account_number

def print_newline():
    """Helper function that just add a new empty line."""

    print("")

def welcome():
    """Helper function to greet the user and ask from the full name."""

    print_newline()
    print(f"Welcome to: Power Rest with The Rich\n")
    print(f"To create a new account provide your full name: ", end="")

def account_created():
    """Helper function that will provided feedback on the completion of the account creation."""
    
    print(f"Account successfully create.\n")

def login_atm_prompt():
    print_newline()
    print(f'Please enter your full name and the four digits of the account number (i.e. ****1234)')
