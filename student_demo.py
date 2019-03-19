# Princess Sampson
# Dr. Lawrence - Python II
# Student demo illustrating getters and setters, init and str

from student import Student

def main():

    # test setters
    test = Student('900000000', 'Laura Ipsum', 'Freshman', 'Undecided', 0.0, 'N/A', 'NY')
    test.setID('900888777')
    test.setName('Laura Spelman')
    test.setClassification('Sophomore')
    test.setMajor('English')
    test.setGPA(3.85)
    test.setDorm('Abby')
    print(test)

    # ask user for info
    id = input('900#: ')
    name = input('Name: ')
    classification = input('Classification: ')
    major = input('Major: ')
    gpa = float(input('GPA on a 4.0 scale: '))
    dorm = input('Dorm (N/A if off campus): ')
    state = input('State: ')

    # create student from info
    student = Student(id, name, classification, major, gpa, dorm, state)

    # create 2 more students
    lupita = Student('900456890', 'Lupita Nyong\'o', 'Senior', 'Theatre', 4.0, 'LLC1', 'CA')
    naomi = Student('900438944', 'Naomi Osaka', 'Sophomore', 'Economics', 3.67, 'Manley', 'FL')

    # place into a list
    students = [student, lupita, naomi]

    # print students, test other getters
    print()
    
    for student in students:
        print(student)
        print('A %s %s major from %s with a %0.2f GPA. They live in %s.' % (student.getClassification(), student.getMajor(), student.getState(), student.getGPA(), student.getDorm()))


# call main
main()