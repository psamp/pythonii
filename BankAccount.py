class BankAccount:

    def __init__(self, owner, balance, accountNumber):
        self._owner = owner
        self._balance = balance
        self._accountNumber = accountNumber

    def setOwner(self, owner):
        self._owner = owner
    
    def setBalance(self, balance):
        self._balance = balance

    def accountNumber(self, accountNumber):
        self._accountNumber = accountNumber

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount