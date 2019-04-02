# P Sampson
# Dr. Lawrence - Python II
# Person subclass for worker

from person import Person

class Worker(Person):

    def __init__(self, gender, race, age, name, position, salary):
        Person.__init__(self, gender, race, age, name)
        
        self._position = position
        self._salary = salary

    # getters
    def get_position(self):
        return self._position

    def get_salary(self):
        return self._salary
    
    #setters
    def set_position(self, position):
        self._position = position

    def set_salary(self, salary):
        self._salary = salary

    # str
    def __str__(self):
        # delegate to the person str to get basic info
        person_info = Person.__str__(self)
        worker_info = ' They make $%d as a %s.' % (self.get_salary(), self.get_position())

        return person_info + worker_info
    