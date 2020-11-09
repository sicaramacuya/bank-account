from random import randint

def generate_account_number():
    """Helper function that return a eight digit random number which is going to be of type string."""
    account_number = ""
    for _ in range(8):
        account_number += str(randint(0,9))

    return account_number

def print_newline():
    print("")