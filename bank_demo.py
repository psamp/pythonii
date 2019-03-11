# Princess Sampson
# Dr. Lawrence - Python II
# Bank account class advanced demo

from bank import BankAccount
import uuid

# create account
def createAccount():
    # get information from user and generate an id
    owner = input('Enter your name: ')
    balance = float(input('Enter your initial deposit: '))
    id = uuid.uuid4().hex

    # return the new bank account object
    return BankAccount(owner, balance, id)

# given an account, ask a user to choose a menu option and print appropriate info
def running(account):
    # user input
    choice = input("1. Deposit\n2. Withdraw\n3. Check\n")
    
    # print info based on user choice
    if choice == '1':
        amount = float(input('How much would you like to deposit?\n'))
        account.deposit(amount)
    if choice == '2':
        amount = float(input('How much would you like to withdraw?\n'))
        account.withdraw(amount)
    else:
        print(account)


def main():
    # create an account
    account = createAccount()

    # game loop flag
    playing = True

    # while the user wants to play
    while playing:
        # delegate to menu/info function
        running(account)

        # ask the user if they would like to quit
        quit = input('Quit? Y/N')

        # set the flag to false if they want to quit
        playing = True if quit != 'Y' else False

# call main
main()