# Bank Account
## Description
The main focus of this project is to create a Python progra mthat simulates a bank account using object-oriented programming concepts.

### Class variables and Instance variables
The account will have a class variables that will contain the routing number which is going to be the same for all accounts and instance variables that will store things like full name, account number, routing number and balance for every  instance of the Bank Account class.

### Methods
Each account will have a series of methods: deposit, withdraw, get_balance, add_interest and print_receipt.

#### Deposit
This method will get one parameter which is going to be the amount and then it will add that amount to the balance. After adding the amount it will print a message with the amount deposited.

#### Withdraw
This method will take one parameter which is also going to be the amount and then it will substract that amount from the balance. After substracting it will print a message of the withdraw amount. If the account have insufficient founds it will display it and charge the account ten dollars.

#### Get Balance
This method will print a message of the account balance.

#### Add Interest
This method adds interest to the account. The interest on the account will be the product of the balance and 0.00083. The number 0.00083 comes from the annual interest rate which is 1% divided by 12 which represent the months. 

#### Print Receipt
This method prints a receipt with everything in it. The account name, account number, routing number, and balance.
