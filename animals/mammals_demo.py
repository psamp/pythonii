# Princess Sampson
# Python II - Dr. Lawrence
# Mammal class hierachy assignment - demo

from mammal import *

def main():
    mammal = Mammal('Whale')
    dog = Dog()
    cat = Cat()
    raccoon = Raccoon()

    animals = [mammal, dog, cat, raccoon]

    for animal in animals:
        print('Sound: ', animal.make_sound())

    for animal in animals:
        print('Action:', animal.action())

    for animal in animals:
        print(animal)

# call main
main()