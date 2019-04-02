# P Sampson
# Dr. Lawrence - Python II
# Person subclass for college student

from person import Person

class Student(Person):
    
    def __init__(self, gender, race, age, name, major, college):
        Person.__init__(self, gender, race, age, name)
        
        self._major = major
        self._college = college

    # getters
    def get_major(self):
        return self._major

    def get_college(self):
        return self._college

    #setters
    def set_major(self, major):
        self._major = major

    def set_college(self, college):
        self._college = college
    
    def __str__(self):
        # delegate to the person str to get basic info
        person_info = Person.__str__(self)
        student_info = ' They are a %s major at %s.' % (self.get_major(), self.get_college())

        return person_info + student_info