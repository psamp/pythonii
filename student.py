# Princess Sampson
# Python II - Dr. Lawrence
# Student class modeling a Spelman student 💙

class Student:

    # constructor
    def __init__(self, id, name, classification, major, gpa, dorm, state):
        self._id = id
        self._name = name
        self._classification = classification
        self._major = major
        self._gpa = gpa
        self._dorm = dorm
        self._state = state

    # getters
    def getID(self):
        return self._id
    
    def getName(self):
        return self._name

    def getClassification(self):
        return self._classification

    def getMajor(self):
        return self._major
    
    def getGPA(self):
        return self._gpa
    
    def getDorm(self):
        return self._dorm
    
    def getState(self):
        return self._state
    
    # setters
    def setID(self, id):
        self._id = id

    def setName(self, name):
        self._name = name

    def setClassification(self, classification):
        self._classification = classification

    def setMajor(self, major):
        self._major = major

    def setGPA(self, gpa):
        self._gpa = gpa

    def setDorm(self, dorm):
        self._dorm = dorm

    def setState(self, state):
        self._state = state
    
    # to tring
    def __str__(self):
        return ('%s | %s') % (self._name, self._id)

