# Princess Sampson
# Python II - Dr. Lawrence
# Mammal class hierachy assignment

class Mammal:
    # The _init_ method accepts an argument for
    # the mammal's species.

    def __init__(self, species):
        self._species = species

    # The show_species method displays a message
    # indicating the mammal's species
    def show_species(self):
        print('I am a', self._species)

    # The make_sound method is the mammal's
    # way of making a generic sound.
    def make_sound(self):
        return 'Grrrrrr'

    # The action method is the mammal's
    # way of making a generic sound.
    def action(self):
        return '*grow hair*'

    # __str___
    def __str__(self):
        return 'I am a mammal'

class Dog(Mammal):
    # The __init__ method calls the superclass's
    # __init__ method passing 'Dog' as the species.
    def __init__(self):
        Mammal.__init__(self, 'Dog')

    # The make_sound method overrides the superclass's
    # make_sound method
    def make_sound(self):
        return 'Boof'
    
    # The action method is the dog's
    # way of licking people.
    def action(self):
        return '*licks owner on face*'

    # __str___
    def __str__(self):
        return 'I am a dog'

class Cat(Mammal):
    # The __init__ method calls the superclass's
    # __init__ method passing 'Cat' as the species.
    def __init__(self):
        Mammal.__init__(self, 'Cat')

    # The make_sound method overrides the superclass's
    # make_sound method
    def make_sound(self):
        return 'Prrr'

    # The action method is the cat's
    # way of landing on its face.
    def action(self):
        return '*lands on feet*'

    # __str___
    def __str__(self):
        return 'I am a cat'

class Raccoon(Mammal):
    # The __init__ method calls the superclass's
    # __init__ method passing 'Racoon' as the species.
    def __init__(self):
        Mammal.__init__(self, 'Raccoon')

    # The make_sound method overrides the superclass's
    # make_sound method
    def make_sound(self):
        return 'Hrrrrrrr'

    # The action method is the raccoon's
    # way of eating garbage.
    def action(self):
        return '*eats garbage*'

    # __str___
    def __str__(self):
        return 'I am a raccoon'

    