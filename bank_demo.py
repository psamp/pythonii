from bank import BankAccount
import uuid

def createAccount():
    owner = input('Enter your name: ')
    balance = float(input('Enter your initial deposit: '))
    id = uuid.uuid4().hex

    return BankAccount(owner, balance, id)

def running(account):
    choice = input("1. Deposit\n2. Withdraw\n3. Check\n")

    if choice == '1':
        amount = float(input('How much would you like to deposit?\n'))
        account.deposit(amount)
    if choice == '2':
        amount = float(input('How much would you like to withdraw?\n'))
        account.withdraw(amount)
    else:
        print(account)


def main():
    account = createAccount()
    playing = True

    while playing:
        running(account)
        quit = input('Quit? Y/N')

        playing = True if quit != 'Y' else False

# call main
main()