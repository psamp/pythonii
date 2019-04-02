# P Sampson
# Dr. Lawrence - Python II
# Person subclass for faculty

from person import Person

class Faculty(Person):

    def __init__(self, gender, race, age, name, department, *classes):
        Person.__init__(self, gender, race, age, name)
        
        self._department = department
        self._classes = classes

    # getters
    def get_department(self):
        return self._department

    def get_classes(self):
        return self._classes
    
    #setters
    def set_department(self, dept):
        self._department = dept

    def set_classes(self, classes):
        self._classes = classes

    # str
    def __str__(self):
        # delegate to the person str to get basic info
        person_info = Person.__str__(self)
        fac_info = ' They teach %s in the %s department.' % (str(self.get_classes()), self.get_department())

        return person_info + fac_info
    