from bank import BankAccount

def main():
    fatima = BankAccount("Fatima Haiz", 0.0, "67255")
    cesaire = BankAccount("Aime Cesaire", 75.0, "12345")

    fatima.deposit(100.0)
    cesaire.withdraw(50.0)

    print(fatima)
    print(cesaire)

# call main
main()