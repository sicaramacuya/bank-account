from class_module import BankAccount
from helper_module import print_newline

# bank account examples
lyra = BankAccount("Lyra Morales Sanchez")
ezra = BankAccount("Ezra Morales Sanchez")
azul = BankAccount("Azul Morales Sanchez")

# checking the inital values of one of the objects
print(f"Initial value of full name: {lyra.full_name}")
print(f"Initial value of the account number: {lyra.account_number}")
print(f"Initial value of the balance: ${lyra.balance:.2f}\n")

# verifying the randomness of the account numbers
print(f"Lyra's account number: {lyra.account_number}")
print(f"Azul's account number: {azul.account_number}")
print(f"Ezra's account number: {ezra.account_number}\n")

# depositing to every account
lyra.deposit(300)
azul.deposit(250)
ezra.deposit(50)
print_newline()

# withdrawing money from the accounts and overdrafting from ezra's account
lyra.withdraw(150)
azul.withdraw(200)
ezra.withdraw(60)
print_newline()

# getting balance from the accounts and seeing it the overdraft was deducted
lyra.get_balance()
azul.get_balance()
ezra.get_balance()
print_newline()

# applying the interest to all accounts
lyra.add_interest()
azul.add_interest()
ezra.add_interest()

# print a receipt for each account
lyra.print_receipt()
print_newline()
azul.print_receipt()
print_newline()
ezra.print_receipt()
print_newline()