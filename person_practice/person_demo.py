# P Sampson
# Dr. Lawrence - Python 2
# Demo of Person class hierachy (Student, Faculty, Worker)

from person import Person
from student import Student
from faculty import Faculty
from worker import Worker

def main():

    # create each sort of person
    person = Person('woman', 'Latinx', 23, 'Rosario Alejandro')
    student = Student('person', 'Black', 20, 'Alex Aaron', 'Women\'s Studies', 'Spelman College')
    faculty = Faculty('woman', 'Black', 35, 'Dr. Ira Ingram', 'Philosophy', 'Intro to Philosophy', 'Ethics of Gender', 'Critical Thinking')
    worker = Worker('man', 'Japanese', 27, 'Todoroki Shouto', 'Hero', 300000)

    # put them in a list
    people = [person, student, faculty, worker]

    # print all their info
    for person in people:
        print(person)


# call main
main()