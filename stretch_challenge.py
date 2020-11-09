from class_module import BankAccount
from helper_module import welcome, print_newline, account_created, login_atm_prompt

class Terminal(BankAccount):
    """When called this class will instanciate an object of type Terminal which is going to create a terminal for the account owner."""

    def __init__(self, full_name):
        super().__init__(full_name)

    # def 
# --------------------------- main -----------------------

# welcoming the user and getting his/her full name.
welcome()
user_fullname = input()
print_newline()

# instanciating the Terminal class which is going to create also a bank account.
atm_user = Terminal(user_fullname)

# providing feedback and user information.
account_created()
atm_user.show_credentials()

# asking the user if he wants to procced to use the ATM terminal.
print(f'Do you want to acces the ATM terminal?')
print(f'Y - yes                         N - no')
user_response = input()

# depending on the response it will decide if continue with the ATM terminal or not.
if user_response.lower() == 'y':
    scenario = 0
    while True:
        if scenario == 0:
            login_atm_prompt()
            login_name = input(f'Full Name: ')
            login_account_num = input(f'Last four digits: ')
            
            if login_name == atm_user.full_name and login_account_num == atm_user.account_number[4:0]:
                scenario += 1
            else:
                print(f'One of the two values provided is wrong. Try again!')

        elif scenario > 0:
            print(f'We are inside!')


elif user_response.lower() == 'n':
    print(f'Have a nice day!')
