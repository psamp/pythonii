# Princess Sampson
# Dr. Lawrence - Python II
# Demo testing all vehicle types

from vehicles import *

def main():
    auto = Automobile('Volkswagen', 'Bug', 2000, 1700)
    car = Car('Chevrolet', 'Impala', 200000, 150000, 2)
    truck = Truck('Ford', 'F-150', 1575, 28155, 4)
    suv = SUV('GMC', 'Yukon XL', 60000, 55000, 8)
    train = Train('Trainmaker', 'Transporta', 200000, 1000000, 6)

    automobiles = [auto, car, truck, suv, train]

    for automobile in automobiles:
        print(automobile)

# call main
main()