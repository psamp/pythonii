# Princess Sampson
# Dr. Lawrence - Python II
# Class modeling a simple bank account with depositing and withdrawals

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

    def __str__(self):
        return ('%s >> $%.2f' % (self._owner, self._balance))