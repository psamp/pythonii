# P Sampson
# Dr. Lawrence - Python II
# Superclass for polymorphism exercise

class Person:
    # initialize attributess
    def __init__(self, gender, race, age, name):
        self._gender = gender
        self._race = race
        self._age = age
        self._name = name

    # getters

    def get_gender(self):
        return self._gender
    
    def get_race(self):
        return self._race

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    # setters

    def set_gender(self, gender):
        self._gender = gender

    def set_race(self, race):
        self._race = race

    def set_age(self, age):
        self._age = age

    def set_name(self, name):
        self._name = name
    
    # str
    def __str__(self):
        return ('%s is a %d year(s) old %s %s.') % (self.get_name(), self.get_age(), self.get_race(), self.get_gender())